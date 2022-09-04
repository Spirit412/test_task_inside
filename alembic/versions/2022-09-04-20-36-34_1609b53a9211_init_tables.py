"""init tables

Revision ID: 1609b53a9211
Revises: 
Create Date: 2022-09-04 20:36:34.189197

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1609b53a9211'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'messages',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True),
        sa.Column('message', sa.Text, nullable=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True),
        sa.Column('name', sa.String(length=255), nullable=False, unique=True),
        sa.Column('password_digest', sa.String, nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    pass
