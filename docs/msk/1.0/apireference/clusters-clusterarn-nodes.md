---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes.html
---

# Brokers
<a name="clusters-clusterarn-nodes"></a>

The broker nodes in the cluster.

## URI
<a name="clusters-clusterarn-nodes-url"></a>

`/v1/clusters/{{clusterArn}}/nodes`

## HTTP methods
<a name="clusters-clusterarn-nodes-http-methods"></a>

### GET
<a name="clusters-clusterarn-nodesget"></a>

**Operation ID:** `ListNodes`

Returns a list of the broker nodes in the cluster. The following Python 3.6 example first lists one node of a cluster. Because the cluster has more nodes, the response contains a token that the script then uses to list the remaining nodes.

```
import boto3

client = boto3.client('kafka')

list_nodes_response = client.list_nodes(
    ClusterArn='arn:aws:kafka:us-east-1:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4',
    MaxResults=1
)

print('\n')
print('Here is the first node in the list:')
print('\n')
print(list_nodes_response['NodeInfoList'])

next_token = list_nodes_response['NextToken']

list_nodes_response = client.list_nodes(
    ClusterArn='arn:aws:kafka:us-east-1:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4',
    NextToken=next_token
)

print('\n')
print('Here are the remaining nodes in the list:')
print('\n')
print(list_nodes_response['NodeInfoList'])
```

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |
| maxResults | String | False | The maximum number of results to return in the response (default maximum 100 results per API call). If there are more results, the response includes a `NextToken` parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListNodesResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-nodesoptions"></a>

Enable CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-nodes-schemas"></a>

### Response bodies
<a name="clusters-clusterarn-nodes-response-examples"></a>

#### ListNodesResponse schema
<a name="clusters-clusterarn-nodes-response-body-listnodesresponse-example"></a>

```
{
  "nextToken": "string",
  "nodeInfoList": [
    {
      "zookeeperNodeInfo": {
        "zookeeperId": number,
        "clientVpcIpAddress": "string",
        "attachedENIId": "string",
        "endpoints": [
          "string"
        ],
        "zookeeperVersion": "string"
      },
      "instanceType": "string",
      "controllerNodeInfo": {
        "endpoints": [
          "string"
        ]
      },
      "nodeType": enum,
      "nodeARN": "string",
      "brokerNodeInfo": {
        "clientVpcIpAddress": "string",
        "attachedENIId": "string",
        "brokerId": number,
        "endpoints": [
          "string"
        ],
        "clientSubnet": "string",
        "currentBrokerSoftwareInfo": {
          "configurationRevision": integer,
          "kafkaVersion": "string",
          "configurationArn": "string"
        }
      },
      "addedToClusterTime": "string"
    }
  ]
}
```

#### Error schema
<a name="clusters-clusterarn-nodes-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-nodes-properties"></a>

### BrokerNodeInfo
<a name="clusters-clusterarn-nodes-model-brokernodeinfo"></a>

BrokerNodeInfo

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attachedENIId | string | False | The attached elastic network interface of the broker. |
| brokerId | number | False | The ID of the broker. |
| clientSubnet | string | False | The client subnet to which this broker node belongs. |
| clientVpcIpAddress | string | False | The virtual private cloud (VPC) of the client. |
| currentBrokerSoftwareInfo | [BrokerSoftwareInfo](#clusters-clusterarn-nodes-model-brokersoftwareinfo) | False | Information about the version of software currently deployed on the brokers in the cluster. |
| endpoints | Array of type string | False | Endpoints for accessing the broker. |

### BrokerSoftwareInfo
<a name="clusters-clusterarn-nodes-model-brokersoftwareinfo"></a>

Information about the current software installed on the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configurationArn | string | False | The Amazon Resource Name (ARN) of the configuration used for the cluster. This field isn't visible in this preview release. |
| configurationRevision | integer<br />Format: int64 | False | The revision of the configuration to use. This field isn't visible in this preview release. |
| kafkaVersion | string | False | The version of Apache Kafka. You can use Amazon MSK to create clusters that use Apache Kafka versions 1.1.1 and 2.2.1. See [Apache Kafka Versions](kafka-versions.md). |

### ControllerNodeInfo
<a name="clusters-clusterarn-nodes-model-controllernodeinfo"></a>

Controller Node Information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| endpoints | Array of type string | False | Endpoints for accessing the controller. |

### Error
<a name="clusters-clusterarn-nodes-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ListNodesResponse
<a name="clusters-clusterarn-nodes-model-listnodesresponse"></a>

Information about nodes in the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | The paginated results marker. When the result of a `ListNodes` operation is truncated, the call returns `NextToken` in the response. To get another batch of nodes, provide this token in your next request. |
| nodeInfoList | Array of type [NodeInfo](#clusters-clusterarn-nodes-model-nodeinfo) | False | List containing a `NodeInfo` object. Doesn't contain entries for brokers that have been deleted. |

### NodeInfo
<a name="clusters-clusterarn-nodes-model-nodeinfo"></a>

The node information object.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| addedToClusterTime | string | False | The start time. |
| brokerNodeInfo | [BrokerNodeInfo](#clusters-clusterarn-nodes-model-brokernodeinfo) | False | The broker node info. |
| controllerNodeInfo | [ControllerNodeInfo](#clusters-clusterarn-nodes-model-controllernodeinfo) | False | The controller node information. |
| instanceType | string | False | The instance type. |
| nodeARN | string | False | The Amazon Resource Name (ARN) of the node. |
| nodeType | [NodeType](#clusters-clusterarn-nodes-model-nodetype) | False | The node type. |
| zookeeperNodeInfo | [ZookeeperNodeInfo](#clusters-clusterarn-nodes-model-zookeepernodeinfo) | False | The ZookeeperNodeInfo. |

### NodeType
<a name="clusters-clusterarn-nodes-model-nodetype"></a>

The broker or Apache ZooKeeper node.
+ `BROKER`

### ZookeeperNodeInfo
<a name="clusters-clusterarn-nodes-model-zookeepernodeinfo"></a>

Apache ZooKeeper node information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attachedENIId | string | False | The attached elastic network interface of the broker. |
| clientVpcIpAddress | string | False | The virtual private cloud (VPC) IP address of the client. |
| endpoints | Array of type string | False | Endpoints for accessing the Apache ZooKeeper nodes. |
| zookeeperId | number | False | The role-specific ID for Apache ZooKeeper. |
| zookeeperVersion | string | False | The version of Apache ZooKeeper. |

## See also
<a name="clusters-clusterarn-nodes-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListNodes
<a name="ListNodes-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListNodes)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListNodes)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListNodes)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListNodes)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListNodes)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListNodes)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListNodes)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListNodes)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/ListNodes)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListNodes)
