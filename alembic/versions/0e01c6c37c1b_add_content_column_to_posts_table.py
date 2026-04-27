"""add content column to posts table

Revision ID: 0e01c6c37c1b
Revises: 2209e4297b0b
Create Date: 2026-04-26 08:12:36.987470

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e01c6c37c1b'
down_revision: Union[str, Sequence[str], None] = '2209e4297b0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
