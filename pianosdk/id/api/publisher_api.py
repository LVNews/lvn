from datetime import datetime
from io import StringIO
from typing import TextIO, Dict, List, Union

from pianosdk.api_response import ApiResponse
from pianosdk.base_api import BaseApi
from pianosdk.configuration import Configuration
from pianosdk.httpwrap import HttpCallBack
from pianosdk.utils import _json_deserialize, _encode_parameter
from pianosdk.id.models.logout_response import LogoutResponse


class PublisherApi(BaseApi):
    def __init__(self, config: Configuration, http_callback: HttpCallBack = None) -> None:
        super().__init__(config, http_callback)

    def custom_form_submit(self, aid: str, uid: str, custom_fields: str, form_id: str = None, api_token: str = None, authorization: str = None) -> ApiResponse[Dict]:
        _url_path = '/id/api/v1/publisher/form'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {
            'aid': _encode_parameter(aid),
            'uid': _encode_parameter(uid),
            'custom_fields': _encode_parameter(custom_fields),
            'form_id': _encode_parameter(form_id),
            'api_token': _encode_parameter(api_token)
        }

        _headers = {
            'Authorization': authorization,
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {

        }

        _body = None
        _files = None

        _request = self.config.http_client.build_request('POST',
                                                         _query_url,
                                                         headers=_headers,
                                                         query_parameters=_query_parameters,
                                                         parameters=_parameters,
                                                         json=_body,
                                                         files=_files)
        _response = self._execute_request(_request)
        _result = _json_deserialize(_response)
        return _result

    def logout(self, aid: str, token: str, api_token: str = None, authorization: str = None) -> ApiResponse[LogoutResponse]:
        _url_path = '/id/api/v1/publisher/logout'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {
            'aid': _encode_parameter(aid),
            'token': _encode_parameter(token),
            'api_token': _encode_parameter(api_token)
        }

        _headers = {
            'Authorization': authorization,
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {

        }

        _body = None
        _files = None

        _request = self.config.http_client.build_request('POST',
                                                         _query_url,
                                                         headers=_headers,
                                                         query_parameters=_query_parameters,
                                                         parameters=_parameters,
                                                         json=_body,
                                                         files=_files)
        _response = self._execute_request(_request)
        _result = _json_deserialize(_response, LogoutResponse)
        return _result

