"""empty message

Revision ID: 825619d79662
Revises: f05717b38561
Create Date: 2023-05-01 13:39:08.506491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '825619d79662'
down_revision = 'f05717b38561'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_category_name'), ['name'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_name'), ['name'], unique=True)

    op.create_table('debt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('category_id', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('debt', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_debt_name'), ['name'], unique=False)

    op.create_table('veiaco',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=40), nullable=True),
    sa.Column('occupation', sa.String(length=40), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('veiaco', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_veiaco_email'), ['email'], unique=False)
        batch_op.create_index(batch_op.f('ix_veiaco_name'), ['name'], unique=False)

    op.create_table('Veiaco_has_Debt',
    sa.Column('veiaco_id', sa.Integer(), nullable=False),
    sa.Column('debt_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['debt_id'], ['debt.id'], ),
    sa.ForeignKeyConstraint(['veiaco_id'], ['veiaco.id'], ),
    sa.PrimaryKeyConstraint('veiaco_id', 'debt_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Veiaco_has_Debt')
    with op.batch_alter_table('veiaco', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_veiaco_name'))
        batch_op.drop_index(batch_op.f('ix_veiaco_email'))

    op.drop_table('veiaco')
    with op.batch_alter_table('debt', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_debt_name'))

    op.drop_table('debt')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_name'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_category_name'))

    op.drop_table('category')
    # ### end Alembic commands ###
