from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "002_add_description_to_products"
down_revision: Union[str, None] = "001_create_products"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("products") as batch_op:
        batch_op.add_column(sa.Column("description", sa.String(), nullable=False, server_default="No description"))


def downgrade() -> None:
    with op.batch_alter_table("products") as batch_op:
        batch_op.drop_column("description")
