# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import boxd_client.protocol.generated.common_pb2 as common__pb2
import boxd_client.protocol.generated.control_pb2 as control__pb2


class ContorlCommandStub(object):
  """The box control command service definition.
  set boxd debug level
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SetDebugLevel = channel.unary_unary(
        '/rpcpb.ContorlCommand/SetDebugLevel',
        request_serializer=control__pb2.DebugLevelRequest.SerializeToString,
        response_deserializer=common__pb2.BaseResponse.FromString,
        )
    self.UpdateNetworkID = channel.unary_unary(
        '/rpcpb.ContorlCommand/UpdateNetworkID',
        request_serializer=control__pb2.UpdateNetworkIDRequest.SerializeToString,
        response_deserializer=common__pb2.BaseResponse.FromString,
        )
    self.GetNetworkID = channel.unary_unary(
        '/rpcpb.ContorlCommand/GetNetworkID',
        request_serializer=control__pb2.GetNetworkIDRequest.SerializeToString,
        response_deserializer=control__pb2.GetNetworkIDResponse.FromString,
        )
    self.AddNode = channel.unary_unary(
        '/rpcpb.ContorlCommand/AddNode',
        request_serializer=control__pb2.AddNodeRequest.SerializeToString,
        response_deserializer=common__pb2.BaseResponse.FromString,
        )
    self.GetBlockHeight = channel.unary_unary(
        '/rpcpb.ContorlCommand/GetBlockHeight',
        request_serializer=control__pb2.GetBlockHeightRequest.SerializeToString,
        response_deserializer=control__pb2.GetBlockHeightResponse.FromString,
        )
    self.GetBlockHash = channel.unary_unary(
        '/rpcpb.ContorlCommand/GetBlockHash',
        request_serializer=control__pb2.GetBlockHashRequest.SerializeToString,
        response_deserializer=control__pb2.GetBlockHashResponse.FromString,
        )
    self.GetBlockHeader = channel.unary_unary(
        '/rpcpb.ContorlCommand/GetBlockHeader',
        request_serializer=control__pb2.GetBlockRequest.SerializeToString,
        response_deserializer=control__pb2.GetBlockHeaderResponse.FromString,
        )
    self.GetBlock = channel.unary_unary(
        '/rpcpb.ContorlCommand/GetBlock',
        request_serializer=control__pb2.GetBlockRequest.SerializeToString,
        response_deserializer=control__pb2.GetBlockResponse.FromString,
        )
    self.GetNodeInfo = channel.unary_unary(
        '/rpcpb.ContorlCommand/GetNodeInfo',
        request_serializer=control__pb2.GetNodeInfoRequest.SerializeToString,
        response_deserializer=control__pb2.GetNodeInfoResponse.FromString,
        )
    self.GetBlockByHeight = channel.unary_unary(
        '/rpcpb.ContorlCommand/GetBlockByHeight',
        request_serializer=control__pb2.GetBlockByHeightReq.SerializeToString,
        response_deserializer=control__pb2.GetBlockResponse.FromString,
        )
    self.GetBlockTransactionCountByHash = channel.unary_unary(
        '/rpcpb.ContorlCommand/GetBlockTransactionCountByHash',
        request_serializer=control__pb2.GetBlockTransactionCountByHashReq.SerializeToString,
        response_deserializer=control__pb2.GetBlockTxCountResp.FromString,
        )
    self.GetBlockTransactionCountByHeight = channel.unary_unary(
        '/rpcpb.ContorlCommand/GetBlockTransactionCountByHeight',
        request_serializer=control__pb2.GetBlockTransactionCountByHeightReq.SerializeToString,
        response_deserializer=control__pb2.GetBlockTxCountResp.FromString,
        )
    self.GetTransactionByBlockHashAndIndex = channel.unary_unary(
        '/rpcpb.ContorlCommand/GetTransactionByBlockHashAndIndex',
        request_serializer=control__pb2.GetTransactionByBlockHashAndIndexReq.SerializeToString,
        response_deserializer=control__pb2.GetTxResp.FromString,
        )
    self.GetTransactionByBlockHeightAndIndex = channel.unary_unary(
        '/rpcpb.ContorlCommand/GetTransactionByBlockHeightAndIndex',
        request_serializer=control__pb2.GetTransactionByBlockHeightAndIndexReq.SerializeToString,
        response_deserializer=control__pb2.GetTxResp.FromString,
        )


class ContorlCommandServicer(object):
  """The box control command service definition.
  set boxd debug level
  """

  def SetDebugLevel(self, request, context):
    """rpc SetDebugLevel (DebugLevelRequest) returns (BaseResponse) {
    option (google.api.http) = {
    post: "/v1/ctl/debuglevel"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateNetworkID(self, request, context):
    """rpc UpdateNetworkID (UpdateNetworkIDRequest) returns (BaseResponse) {
    option (google.api.http) = {
    post: "/v1/ctl/networkid"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNetworkID(self, request, context):
    """rpc GetNetworkID (GetNetworkIDRequest) returns (GetNetworkIDResponse) {
    option (google.api.http) = {
    post: "/v1/ctl/getnetwork"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddNode(self, request, context):
    """rpc AddNode (AddNodeRequest) returns (BaseResponse) {
    option (google.api.http) = {
    post: "/v1/ctl/addnode"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlockHeight(self, request, context):
    """rpc GetBlockHeight (GetBlockHeightRequest) returns (GetBlockHeightResponse) {
    option (google.api.http) = {
    post: "/v1/ctl/getblockheight"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlockHash(self, request, context):
    """rpc GetBlockHash (GetBlockHashRequest) returns (GetBlockHashResponse) {
    option (google.api.http) = {
    post: "/v1/ctl/getblockhash"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlockHeader(self, request, context):
    """rpc GetBlockHeader (GetBlockRequest) returns (GetBlockHeaderResponse) {
    option (google.api.http) = {
    post: "/v1/ctl/getblockheader"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlock(self, request, context):
    """rpc GetBlock (GetBlockRequest) returns (GetBlockResponse) {
    option (google.api.http) = {
    post: "/v1/ctl/getblock"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNodeInfo(self, request, context):
    """rpc GetNodeInfo (GetNodeInfoRequest) returns (GetNodeInfoResponse) {
    option (google.api.http) = {
    post: "/v1/ctl/getnodeinfo"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlockByHeight(self, request, context):
    """rpc GetBlockByHeight (GetBlockByHeightReq) returns (GetBlockResponse) {
    option (google.api.http) = {
    post: "/v1/ctl/getBlockByHeight"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlockTransactionCountByHash(self, request, context):
    """rpc GetBlockTransactionCountByHash (GetBlockTransactionCountByHashReq) returns (GetBlockTxCountResp) {
    option (google.api.http) = {
    post: "/v1/ctl/block/txCountByHash"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlockTransactionCountByHeight(self, request, context):
    """rpc GetBlockTransactionCountByHeight (GetBlockTransactionCountByHeightReq) returns (GetBlockTxCountResp) {
    option (google.api.http) = {
    post: "/v1/ctl/block/txCountByHeight"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransactionByBlockHashAndIndex(self, request, context):
    """rpc GetTransactionByBlockHashAndIndex (GetTransactionByBlockHashAndIndexReq) returns (GetTxResp) {
    option (google.api.http) = {
    post: "/v1/ctl/getTxByHash"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransactionByBlockHeightAndIndex(self, request, context):
    """rpc GetTransactionByBlockHeightAndIndex (GetTransactionByBlockHeightAndIndexReq) returns (GetTxResp) {
    option (google.api.http) = {
    post: "/v1/ctl/getTxByHeight"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ContorlCommandServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SetDebugLevel': grpc.unary_unary_rpc_method_handler(
          servicer.SetDebugLevel,
          request_deserializer=control__pb2.DebugLevelRequest.FromString,
          response_serializer=common__pb2.BaseResponse.SerializeToString,
      ),
      'UpdateNetworkID': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateNetworkID,
          request_deserializer=control__pb2.UpdateNetworkIDRequest.FromString,
          response_serializer=common__pb2.BaseResponse.SerializeToString,
      ),
      'GetNetworkID': grpc.unary_unary_rpc_method_handler(
          servicer.GetNetworkID,
          request_deserializer=control__pb2.GetNetworkIDRequest.FromString,
          response_serializer=control__pb2.GetNetworkIDResponse.SerializeToString,
      ),
      'AddNode': grpc.unary_unary_rpc_method_handler(
          servicer.AddNode,
          request_deserializer=control__pb2.AddNodeRequest.FromString,
          response_serializer=common__pb2.BaseResponse.SerializeToString,
      ),
      'GetBlockHeight': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlockHeight,
          request_deserializer=control__pb2.GetBlockHeightRequest.FromString,
          response_serializer=control__pb2.GetBlockHeightResponse.SerializeToString,
      ),
      'GetBlockHash': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlockHash,
          request_deserializer=control__pb2.GetBlockHashRequest.FromString,
          response_serializer=control__pb2.GetBlockHashResponse.SerializeToString,
      ),
      'GetBlockHeader': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlockHeader,
          request_deserializer=control__pb2.GetBlockRequest.FromString,
          response_serializer=control__pb2.GetBlockHeaderResponse.SerializeToString,
      ),
      'GetBlock': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlock,
          request_deserializer=control__pb2.GetBlockRequest.FromString,
          response_serializer=control__pb2.GetBlockResponse.SerializeToString,
      ),
      'GetNodeInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetNodeInfo,
          request_deserializer=control__pb2.GetNodeInfoRequest.FromString,
          response_serializer=control__pb2.GetNodeInfoResponse.SerializeToString,
      ),
      'GetBlockByHeight': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlockByHeight,
          request_deserializer=control__pb2.GetBlockByHeightReq.FromString,
          response_serializer=control__pb2.GetBlockResponse.SerializeToString,
      ),
      'GetBlockTransactionCountByHash': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlockTransactionCountByHash,
          request_deserializer=control__pb2.GetBlockTransactionCountByHashReq.FromString,
          response_serializer=control__pb2.GetBlockTxCountResp.SerializeToString,
      ),
      'GetBlockTransactionCountByHeight': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlockTransactionCountByHeight,
          request_deserializer=control__pb2.GetBlockTransactionCountByHeightReq.FromString,
          response_serializer=control__pb2.GetBlockTxCountResp.SerializeToString,
      ),
      'GetTransactionByBlockHashAndIndex': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransactionByBlockHashAndIndex,
          request_deserializer=control__pb2.GetTransactionByBlockHashAndIndexReq.FromString,
          response_serializer=control__pb2.GetTxResp.SerializeToString,
      ),
      'GetTransactionByBlockHeightAndIndex': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransactionByBlockHeightAndIndex,
          request_deserializer=control__pb2.GetTransactionByBlockHeightAndIndexReq.FromString,
          response_serializer=control__pb2.GetTxResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rpcpb.ContorlCommand', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
