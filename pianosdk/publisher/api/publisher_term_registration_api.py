from datetime import datetime
from io import StringIO
from typing import TextIO, Dict, List, Union

from pianosdk.api_response import ApiResponse
from pianosdk.base_api import BaseApi
from pianosdk.configuration import Configuration
from pianosdk.httpwrap import HttpCallBack
from pianosdk.utils import _json_deserialize, _encode_parameter
from pianosdk.publisher.models.term import Term


class PublisherTermRegistrationApi(BaseApi):
    def __init__(self, config: Configuration, http_callback: HttpCallBack = None) -> None:
        super().__init__(config, http_callback)

    def create_registration_term(self, aid: str, rid: str, name: str, description: str = None, registration_access_period: int = None, registration_grace_period: int = None) -> ApiResponse[Term]:
        _url_path = '/api/v3/publisher/term/registration/create'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {

        }

        _headers = {
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {
            'aid': _encode_parameter(aid),
            'rid': _encode_parameter(rid),
            'name': _encode_parameter(name),
            'description': _encode_parameter(description),
            'registration_access_period': _encode_parameter(registration_access_period),
            'registration_grace_period': _encode_parameter(registration_grace_period)
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
        _result = _json_deserialize(_response, Term)
        return _result

    def update_registration_term(self, term_id: str, rid: str = None, name: str = None, description: str = None, registration_access_period: int = None, registration_grace_period: int = None) -> ApiResponse[Term]:
        _url_path = '/api/v3/publisher/term/registration/update'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {

        }

        _headers = {
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {
            'term_id': _encode_parameter(term_id),
            'rid': _encode_parameter(rid),
            'name': _encode_parameter(name),
            'description': _encode_parameter(description),
            'registration_access_period': _encode_parameter(registration_access_period),
            'registration_grace_period': _encode_parameter(registration_grace_period)
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
        _result = _json_deserialize(_response, Term)
        return _result

