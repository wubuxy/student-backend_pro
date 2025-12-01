import os
import pytest
import yaml
from app.core.config import get_config
from app.utils.profile import Profile

@pytest.fixture(autouse=True)
def clear_config_cache():
    get_config.cache_clear()
    yield
    get_config.cache_clear()

@pytest.fixture
def fake_config_file():
    project_dir = Profile.get_project_root()

    real_config_path = project_dir / "config.yaml"
    if not os.path.exists(real_config_path):
        raise FileNotFoundError("file not found: config.yaml")
    with open(real_config_path, "r", encoding="utf-8") as f:
        config_data = yaml.safe_load(f)

    config_data.pop("env")

    test_config = config_data.copy()

    if "dev" in test_config:
        #test_config["dev"]["app"]["name"] = "Student Information Management System(dev)"
        test_config["dev"]["app"]["port"] = 8000
        test_config["dev"]["app"]["reload"] = True
        test_config["dev"]["db"]["host"] = "localhost"
        test_config["dev"]["db"]["database"] = "dev-db"
    if "prod" in test_config:
        #test_config["prod"]["app"]["name"] = "Student Information Management System(prod)"
        test_config["prod"]["app"]["port"] = 8001
        test_config["prod"]["app"]["reload"] = False
        test_config["prod"]["db"]["host"] = "prod-host"
        test_config["prod"]["db"]["database"] = "prod-db"

    file_name = "fake_config.yaml"
    config_file = project_dir / file_name
    with open(config_file, "w", encoding="utf-8") as f:
        yaml.dump(test_config, f)

    return file_name

class TestConfig:
    def test_dev_config(self, fake_config_file):
        config = get_config(fake_config_file, "dev")
        #assert config.app.name == "Student Information Management System(dev)"
        assert config.app.port == 8000
        assert config.app.reload is True
        assert config.db.host == "localhost"
        assert config.db.database == "dev-db"
