"""Initial Migration

Revision ID: 358e5538fe81
Revises: 628adcb2d60e
Create Date: 2024-04-20 10:08:21.728304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '358e5538fe81'
down_revision: Union[str, None] = '628adcb2d60e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', sa.Enum('ANONYMOUS', 'AUTHENTICATED', 'MANAGER', 'ADMIN', name='userrole'), nullable=False))
    op.add_column('users', sa.Column('is_professional', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('professional_status_updated_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'professional_status_updated_at')
    op.drop_column('users', 'is_professional')
    op.drop_column('users', 'role')
    # ### end Alembic commands ###