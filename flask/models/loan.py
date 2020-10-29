from db import db

class LoanModel(db.Model):
    __tablename__ = 'loans'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    amount = db.Column(db.Integer)

    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'))
    store = db.relationship('AgentModel')

    def __init__(self, name, amount, agent_id):
        self.name = name
        self.amount = amount
        self.agent_id = agent_id

    def json(self):
        return {'name': self.name, 'amount': self.amount}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()