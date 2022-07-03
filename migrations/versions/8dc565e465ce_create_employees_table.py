"""create_employees_table

Revision ID: 8dc565e465ce
Revises: 
Create Date: 2022-07-03 14:30:57.933776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dc565e465ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'employees',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(200), nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('phone', sa.BIGINT, nullable=False)
    )


def downgrade():
    op.drop_table('employees')
