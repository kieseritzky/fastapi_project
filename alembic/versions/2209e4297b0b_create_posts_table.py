"""create posts table

Revision ID: 2209e4297b0b
Revises: 
Create Date: 2026-04-19 16:56:03.060117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2209e4297b0b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts', sa.Column('id', sa.Integer, nullable=False, primary_key=True),
                    sa.Column('title', sa.String, nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts")
    pass
