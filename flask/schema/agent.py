from ma import ma
from models.loan import LoanModel
from models.agent import AgentModel
from schema.loan import LoanSchema


class AgentSchema(ma.SQLAlchemyAutoSchema):
    loans = ma.Nested(LoanSchema, many=True)
    class Meta:
        model = LoanModel
        load_instance = True
        include_fk = True