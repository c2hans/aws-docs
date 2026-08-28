---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-connectivity.html
---

# Cluster Connectivity
<a name="clusters-clusterarn-connectivity"></a>

Use this resource to update the connectivity setting for an MSK cluster.

## URI
<a name="clusters-clusterarn-connectivity-url"></a>

`/v1/clusters/{{clusterArn}}/connectivity`

## HTTP methods
<a name="clusters-clusterarn-connectivity-http-methods"></a>

### PUT
<a name="clusters-clusterarn-connectivityput"></a>

**Operation ID:** `UpdateConnectivity`

Updates the connectivity setting for the cluster.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateConnectivityResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-connectivityoptions"></a>

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
<a name="clusters-clusterarn-connectivity-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-connectivity-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-connectivity-request-body-put-example"></a>

```
{
  "connectivityInfo": {
    "vpcConnectivity": {
      "clientAuthentication": {
        "sasl": {
          "iam": {
            "enabled": boolean
          },
          "scram": {
            "enabled": boolean
          }
        },
        "tls": {
          "enabled": boolean
        }
      }
    },
    "publicAccess": {
      "type": "string"
    },
    "networkType": "string"
  },
  "zookeeperAccess": {
    "enabled": boolean
  },
  "currentVersion": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-connectivity-response-examples"></a>

#### UpdateConnectivityResponse schema
<a name="clusters-clusterarn-connectivity-response-body-updateconnectivityresponse-example"></a>

```
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-connectivity-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-connectivity-properties"></a>

### ConnectivityInfo
<a name="clusters-clusterarn-connectivity-model-connectivityinfo"></a>

Broker access controls.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| networkType | string<br />MinLength: 4<br />MaxLength: 4 | False | The network type of the cluster, which is IPv4 or DUAL. The DUAL network type uses both IPv4 and IPv6 addresses for your cluster and its resources. By default, a cluster uses the IPv4 network type. |
| publicAccess | [PublicAccess](#clusters-clusterarn-connectivity-model-publicaccess) | False | Access control settings for the cluster's brokers. |
| vpcConnectivity | [VpcConnectivity](#clusters-clusterarn-connectivity-model-vpcconnectivity) | False | VPC connection control settings for brokers |

### Error
<a name="clusters-clusterarn-connectivity-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### PublicAccess
<a name="clusters-clusterarn-connectivity-model-publicaccess"></a>

Broker access controls

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| type | string | False | DISABLED means that public access is turned off. SERVICE\_PROVIDED\_EIPS means that public access is turned on. |

### UpdateConnectivityRequest
<a name="clusters-clusterarn-connectivity-model-updateconnectivityrequest"></a>

Request body for UpdateConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| connectivityInfo | [ConnectivityInfo](#clusters-clusterarn-connectivity-model-connectivityinfo) | False | The target connectivity setting for the cluster. |
| currentVersion | string | True | The current version of the cluster. |
| zookeeperAccess | [ZookeeperAccess](#clusters-clusterarn-connectivity-model-zookeeperaccess) | False | The target ZooKeeper access setting for the cluster. |

### UpdateConnectivityResponse
<a name="clusters-clusterarn-connectivity-model-updateconnectivityresponse"></a>

Response body for UpdateConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

### VpcConnectivity
<a name="clusters-clusterarn-connectivity-model-vpcconnectivity"></a>

VPC connection control settings for brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientAuthentication | [VpcConnectivityClientAuthentication](#clusters-clusterarn-connectivity-model-vpcconnectivityclientauthentication) | False | VPC connection control settings for brokers. |

### VpcConnectivityClientAuthentication
<a name="clusters-clusterarn-connectivity-model-vpcconnectivityclientauthentication"></a>

Includes all client authentication information for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sasl | [VpcConnectivitySasl](#clusters-clusterarn-connectivity-model-vpcconnectivitysasl) | False | Details for VpcConnectivity ClientAuthentication using SASL. |
| tls | [VpcConnectivityTls](#clusters-clusterarn-connectivity-model-vpcconnectivitytls) | False | Details for VpcConnectivity ClientAuthentication using TLS. |

### VpcConnectivityIAM
<a name="clusters-clusterarn-connectivity-model-vpcconnectivityiam"></a>

Details for SASL/IAM client authentication for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/IAM authentication is enabled or not. |

### VpcConnectivitySasl
<a name="clusters-clusterarn-connectivity-model-vpcconnectivitysasl"></a>

Details for client authentication using SASL for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| iam | [VpcConnectivityIAM](#clusters-clusterarn-connectivity-model-vpcconnectivityiam) | False | Details for ClientAuthentication using IAM for VpcConnectivity. |
| scram | [VpcConnectivityScram](#clusters-clusterarn-connectivity-model-vpcconnectivityscram) | False | Details for SASL/SCRAM client authentication for VpcConnectivity. |

### VpcConnectivityScram
<a name="clusters-clusterarn-connectivity-model-vpcconnectivityscram"></a>

Details for SASL/SCRAM client authentication for vpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/SCRAM authentication is enabled or not. |

### VpcConnectivityTls
<a name="clusters-clusterarn-connectivity-model-vpcconnectivitytls"></a>

Details for client authentication using TLS for vpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | TLS authentication is enabled or not. |

### ZookeeperAccess
<a name="clusters-clusterarn-connectivity-model-zookeeperaccess"></a>

ZooKeeper access control settings for the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Specifies whether direct Apache ZooKeeper client access is enabled or disabled for the cluster. |

## See also
<a name="clusters-clusterarn-connectivity-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateConnectivity
<a name="UpdateConnectivity-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateConnectivity)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateConnectivity)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateConnectivity)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateConnectivity)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateConnectivity)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateConnectivity)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateConnectivity)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateConnectivity)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/UpdateConnectivity)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateConnectivity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
