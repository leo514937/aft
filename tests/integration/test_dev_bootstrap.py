from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def test_repo_root_imports_api_without_editable_install() -> None:
    root = Path(__file__).resolve().parents[2]
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)

    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "from uvicorn.importer import import_from_string; "
            "app = import_from_string('ontology_audit_hub.api:app'); "
            "print(type(app).__name__); "
            "app.state.audit_service.close()",
        ],
        cwd=root,
        capture_output=True,
        text=True,
        env=env,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    assert "FastAPI" in result.stdout
