"""subscribtion table added

Revision ID: 97f8fb9925b6
Revises: fc9ccdd51242
Create Date: 2023-08-06 20:43:11.148665

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '97f8fb9925b6'
down_revision = 'fc9ccdd51242'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('subscriber_id', sa.Integer(), nullable=False),
    sa.Column('subscribed_to_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subscribed_to_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['subscriber_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('subscribtion')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribtion',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('date_created', mysql.DATETIME(), nullable=False),
    sa.Column('subscriber_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('subscribed_to_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['subscribed_to_id'], ['user.id'], name='subscribtion_ibfk_1'),
    sa.ForeignKeyConstraint(['subscriber_id'], ['user.id'], name='subscribtion_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('subscription')
    # ### end Alembic commands ###