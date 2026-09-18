from pathlib import Path

from sqlmesh.core.config import ModelDefaultsConfig
from sqlmesh.dbt.loader import sqlmesh_config

# SQLMesh refuses to load a dbt project without a backfill start date, and it
# only looks for one in the `models:` block of dbt_project.yml. The datamart
# used to carry `+start: Jan 1 2000` there purely for us; dbt v2 rejects it as
# an unrecognised key, so the start date lives here now - in the stack that
# needs it, rather than in the shared model.
config = sqlmesh_config(
    Path(__file__).parent,
    model_defaults=ModelDefaultsConfig(start="2000-01-01"),
)
