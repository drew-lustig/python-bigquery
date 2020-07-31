# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.cloud.bigquery_v2.proto import model_pb2 as google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ModelServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetModel = channel.unary_unary(
                '/google.cloud.bigquery.v2.ModelService/GetModel',
                request_serializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.GetModelRequest.SerializeToString,
                response_deserializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.Model.FromString,
                )
        self.ListModels = channel.unary_unary(
                '/google.cloud.bigquery.v2.ModelService/ListModels',
                request_serializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.ListModelsRequest.SerializeToString,
                response_deserializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.ListModelsResponse.FromString,
                )
        self.PatchModel = channel.unary_unary(
                '/google.cloud.bigquery.v2.ModelService/PatchModel',
                request_serializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.PatchModelRequest.SerializeToString,
                response_deserializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.Model.FromString,
                )
        self.DeleteModel = channel.unary_unary(
                '/google.cloud.bigquery.v2.ModelService/DeleteModel',
                request_serializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.DeleteModelRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ModelServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetModel(self, request, context):
        """Gets the specified model resource by model ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListModels(self, request, context):
        """Lists all models in the specified dataset. Requires the READER dataset
        role.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PatchModel(self, request, context):
        """Patch specific fields in the specified model.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteModel(self, request, context):
        """Deletes the model specified by modelId from the dataset.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetModel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetModel,
                    request_deserializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.GetModelRequest.FromString,
                    response_serializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.Model.SerializeToString,
            ),
            'ListModels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListModels,
                    request_deserializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.ListModelsRequest.FromString,
                    response_serializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.ListModelsResponse.SerializeToString,
            ),
            'PatchModel': grpc.unary_unary_rpc_method_handler(
                    servicer.PatchModel,
                    request_deserializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.PatchModelRequest.FromString,
                    response_serializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.Model.SerializeToString,
            ),
            'DeleteModel': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteModel,
                    request_deserializer=google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.DeleteModelRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.cloud.bigquery.v2.ModelService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ModelService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.bigquery.v2.ModelService/GetModel',
            google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.GetModelRequest.SerializeToString,
            google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.Model.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListModels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.bigquery.v2.ModelService/ListModels',
            google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.ListModelsRequest.SerializeToString,
            google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.ListModelsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PatchModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.bigquery.v2.ModelService/PatchModel',
            google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.PatchModelRequest.SerializeToString,
            google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.Model.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.bigquery.v2.ModelService/DeleteModel',
            google_dot_cloud_dot_bigquery__v2_dot_proto_dot_model__pb2.DeleteModelRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
