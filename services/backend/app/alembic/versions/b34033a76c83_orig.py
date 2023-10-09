"""orig

Revision ID: b34033a76c83
Revises: 0bd8723f72d4
Create Date: 2023-10-08 22:08:58.378088

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b34033a76c83'
down_revision: Union[str, None] = '0bd8723f72d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
