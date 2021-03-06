# Copyright 2016 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------


class SawtoothException(Exception):
    def __init__(self, msg):
        super(SawtoothException, self).__init__(msg)


class ClientException(SawtoothException):
    def __init__(self, msg):
        super(ClientException, self).__init__(msg)


class MessageException(Exception):
    """
    A class to capture communication exceptions
    """
    pass


class NotAvailableException(Exception):
    """
    Indicates a required service is not available and the action should be
    tried again later.
    """
    pass


class TransactionException(SawtoothException):
    """
    Exception raised from Transaction implementations.
    """

    def __init__(self, msg):
        super(TransactionException, self).__init__(msg)


class InvalidTransactionError(TransactionException):
    """
    Exception raised from Transaction.check_valid(), indicating that the
    transaction is not valid.  The corresponding message is logged by the
    validator and may be provided to a client (and end-user) as a reason
    the transaction was not accepted.
    """

    def __init__(self, msg):
        super(InvalidTransactionError, self).__init__(msg)


class ManagementError(SawtoothException):
    def __init__(self, msg):
        super(ManagementError, self).__init__(msg)
