{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # or "unstable"
  services.docker.enable = true;
  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.sudo
    pkgs.apt
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.virtualenv
    pkgs.docker-compose
    pkgs.unixtools.ifconfig
    pkgs.firewalld
  ];
  # Sets environment variables in the workspace
  env = {
    PYTHONPATH = "${toString ./.}";
  };
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      # "vscodevim.vim"
    ];
    # Enable previews
    previews = {
      enable = true;
      previews = {
        web = {
          # Run streamlit with the configured port
          command = [".venv/bin/streamlit" "run" "ui/streamlit_ui.py" "--server.port" "$PORT" "--server.address" "0.0.0.0" "--server.enableWebsocketCompression=false" "--server.enableCORS=false" "--server.headless=true"];
          manager = "web";
          env = {
            # Environment variables to set for your server
            PORT = "$PORT";
            PYTHONPATH = ".";
          };
        };
      };
    };
    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # Create and activate a virtual environment
        create-env = "python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ ".idx/dev.nix" "README.md" ];
        # Setup firewall and allow port 8501
        setup-firewall = "sudo firewall-cmd --permanent --add-port=8501/tcp && sudo firewall-cmd --reload";
      };
      # Runs when the workspace is (re)started
      onStart = {
        # Activate Python environment
        activate-python-env = "source .venv/bin/activate";
        # Ensure firewall is configured correctly
        ensure-firewall = "sudo firewall-cmd --permanent --add-port=8501/tcp && sudo firewall-cmd --reload";
      };
    };
  };
}
