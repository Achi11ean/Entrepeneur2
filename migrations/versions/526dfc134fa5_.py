"""empty message

Revision ID: 526dfc134fa5
Revises: 4be302a6493d
Create Date: 2024-11-12 18:16:53.496891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '526dfc134fa5'
down_revision = '4be302a6493d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('engineering_bookings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('engineering_bookings', schema=None) as batch_op:
        batch_op.drop_column('rating')

    # ### end Alembic commands ###
