from pathlib import Path
import shutil
from frontier.utils import prepare_scaffold
from .Preset import update_packages


class ReactBootstrap():
    def install(self, resource_path, base_dir):
        prepare_scaffold(base_dir, resource_path)
        components_dir = Path.joinpath(resource_path, "js/")
        base_packages_path = Path.joinpath(
            Path(__file__).resolve().parent, "samples/default")
        components_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/react_bootstrap/src")
        babel_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/react/config")

        shutil.copytree(str(components_source), str(components_dir))
        shutil.copy2(str(f"{base_packages_path}/package.json"), str(base_dir))
        shutil.copy2(str(f"{babel_source}/.babelrc"), str(base_dir))
        dependencies = {
            "react": "^17.0.1",
            "react-dom": "^17.0.1",
            "bootstrap": "^4.5.1",
            "jquery": "^3.2",
            "popper.js": "^1.14"
        }
        devDependencies = {
            "@babel/core": "^7.12.3",
            "@babel/preset-env": "^7.12.1",
            "@babel/preset-react": "^7.12.5",
            "babel-loader": "^8.2.1",
        }
        update_packages(base_dir, dependencies, devDependencies)
