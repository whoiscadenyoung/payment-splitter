"""added fields

Revision ID: d041952676fd
Revises: b34033a76c83
Create Date: 2023-10-08 22:09:14.480421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd041952676fd'
down_revision: Union[str, None] = 'b34033a76c83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
