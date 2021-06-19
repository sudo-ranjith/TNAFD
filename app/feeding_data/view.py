from flask import request
from flask_restplus import Resource, Namespace
import app.feeding_data.model as feeding_data_model
import app.feeding_data.serializers as feeding_data_serializers
from app import app
import app.Common.serializers as common_serializers
import app.Common.helpers as common_helpers
from datetime import  datetime
import traceback
from flask_jwt_simple import JWTManager, jwt_required, get_jwt_identity
from bson import json_util
from bson.objectid import ObjectId


feeding_ns = Namespace('feeding_data', description='fire man api')


@feeding_ns.route('')
# @jwt_required
class Login(Resource):
    """
         This class get form data
         @return: success or failure message
     """

    @feeding_ns.expect(feeding_data_serializers.feeding_data, validate=True)
    @feeding_ns.response(200, app.config["SUCCESS_MESSAGE_200"], feeding_data_serializers.feeding_data)
    @feeding_ns.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @feeding_ns.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @feeding_ns.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @feeding_ns.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @feeding_ns.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @feeding_ns.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @feeding_ns.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @feeding_ns.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def post(self):
        try:
            if not (request.content_type == 'application/json'):
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_400"],
                                               'Content type should be application/json',
                                               [], 400)
            post_data = request.get_json()
            token = post_data.get("token")
            current_user = get_jwt_identity()
            # check user has valid access token

            post_data['created_at'] = datetime.now().strftime('%Y%m%d%H%M%S%f')
            post_data['created_by'] = current_user
            post_data['_id'] = str(ObjectId())
            post_data['active'] = 1
            user_item = feeding_data_model.RegisterCurb()
            user_item = user_item.insert_data(post_data)

            more_info = "Successfully inserted feeding_ns data"
            return common_helpers.response('success',
                                           app.config["SUCCESS_MESSAGE_200"],
                                           more_info,
                                           [],
                                           200,
                                           post_data.get('token'))
        except Exception as e:
            e = f"{traceback.format_exc()}"
            more_info = "Unable to Inserted data :Exception occurred - " + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)

@feeding_ns.route('/count')
# @jwt_required
class Login(Resource):
    """
         This class get form data
         @return: success or failure message
     """

    @feeding_ns.response(200, app.config["SUCCESS_MESSAGE_200"], feeding_data_serializers.feeding_data)
    @feeding_ns.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @feeding_ns.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @feeding_ns.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @feeding_ns.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @feeding_ns.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @feeding_ns.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @feeding_ns.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @feeding_ns.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def get(self):
        try:
            # post_data['created_by'] = current_user
            user_item = feeding_data_model.RegisterCurb()
            user_item = user_item.get_count()
            # user_item = json_util.dumps(user_item)

            more_info = "Successfully fetched feeding_ns count"
            return common_helpers.response('success',
                                           app.config["SUCCESS_MESSAGE_200"],
                                           more_info,
                                           user_item,
                                           200)
        except Exception as e:
            e = f"{traceback.format_exc()}"
            more_info = "Unable to Inserted data :Exception occurred - " + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)

@feeding_ns.route('/feeding')
# @jwt_required
class Feeding(Resource):
    """
         This class get form data
         @return: success or failure message
     """

    @feeding_ns.response(200, app.config["SUCCESS_MESSAGE_200"], feeding_data_serializers.feeding_data)
    @feeding_ns.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @feeding_ns.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @feeding_ns.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @feeding_ns.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @feeding_ns.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @feeding_ns.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @feeding_ns.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @feeding_ns.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def post(self):
        try:
            user_item = feeding_data_model.RegisterCurb()
            user_item = user_item.get_count()
            """
            when feeding_ns completes his firecall
            input: id_number
            output: feeding info updated in feeding_ns name account successfully.
            find query-> fetch user data -> update feeding dict to user dict
            update in feeding collection
            {
                "username": "feeding_ns", feeding_amount:1000
            }

            """

            more_info = "Successfully fetched feeding_ns count"
            return common_helpers.response('success',
                                           app.config["SUCCESS_MESSAGE_200"],
                                           more_info,
                                           user_item,
                                           200)
        except Exception as e:
            e = f"{traceback.format_exc()}"
            more_info = "Unable to Inserted data :Exception occurred - " + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)