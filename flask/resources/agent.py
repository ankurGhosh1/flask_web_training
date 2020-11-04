from flask_restful import Resource
from flask import request
from ma import ma

from models.agent import AgentModel
from schema.agent import AgentSchema


agent_schema = AgentSchema()
allagents = AgentSchema(many=True)

class Agent(Resource):
    def get(self, name):
        agent = AgentModel.find_by_name(name)
        if agent:
            return agent_schema.dump(agent)
        return {'message': 'Agent not found'}, 404

    def post(self, name):
        if AgentModel.find_by_name(name):
            return {'message': "A agent with name '{}' already exists.".format(name)}, 400

        agent = AgentModel(name=name)
        try:
            agent.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return agent_schema.dump(agent), 201

    def delete(self, name):
        agent = AgentModel.find_by_name(name)
        if agent:
            agent.delete_from_db()

        return {'message': 'agent deleted'}


class AgentList(Resource):
    def get(self):
        return {'agent': allagents.dump(AgentModel.find_all())}