"""add user table

Revision ID: b73198f4e99e
Revises: 8e1c4fbe3082
Create Date: 2021-12-23 22:43:56.491904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b73198f4e99e'
down_revision = '8e1c4fbe3082'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("id", sa.Integer,
                              primary_key=True, nullable=False),
                    sa.Column("email", sa.String, nullable=False, unique=True),
                    sa.Column("password", sa.String, nullable=False),
                    sa.Column("created_at",
                              sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")
                              ),

                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
