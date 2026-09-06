---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.html
---

# BootstrapBrokers
<a name="clusters-clusterarn-bootstrap-brokers"></a>

A list of brokers that a client application can use to bootstrap.

## URI
<a name="clusters-clusterarn-bootstrap-brokers-url"></a>

`/v1/clusters/{{clusterArn}}/bootstrap-brokers`

## HTTP methods
<a name="clusters-clusterarn-bootstrap-brokers-http-methods"></a>

### GET
<a name="clusters-clusterarn-bootstrap-brokersget"></a>

**Operation ID:** `GetBootstrapBrokers`

A list of brokers that a client can use to bootstrap. This list doesn't necessarily include all of the brokers in the cluster. The following Python 3.6 example shows how you can use the Amazon Resource Name (ARN) of a cluster to get its bootstrap brokers. If you don't know the ARN of your cluster, you can use the `ListClusters` operation to get the ARNs of all the clusters in this account and Region.

```
import boto3

client = boto3.client('kafka')

response = client.get_bootstrap_brokers(
    ClusterArn='arn:aws:kafka:us-east-1:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4',
)

print(response['BootstrapBrokerString'])
```

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  GetBootstrapBrokersResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-bootstrap-brokersoptions"></a>

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
<a name="clusters-clusterarn-bootstrap-brokers-schemas"></a>

### Response bodies
<a name="clusters-clusterarn-bootstrap-brokers-response-examples"></a>

#### GetBootstrapBrokersResponse schema
<a name="clusters-clusterarn-bootstrap-brokers-response-body-getbootstrapbrokersresponse-example"></a>

```
{
  "bootstrapBrokerStringPublicSaslIam": "string",
  "bootstrapBrokerStringIpv6": "string",
  "bootstrapBrokerStringPublicSaslScram": "string",
  "bootstrapBrokerString": "string",
  "bootstrapBrokerStringTls": "string",
  "bootstrapBrokerStringVpcConnectivitySaslIam": "string",
  "bootstrapBrokerStringPublicTls": "string",
  "bootstrapBrokerStringVpcConnectivityTls": "string",
  "bootstrapBrokerStringVpcConnectivitySaslScram": "string",
  "bootstrapBrokerStringSaslIam": "string",
  "bootstrapBrokerStringTlsIpv6": "string",
  "bootstrapBrokerStringSaslScramIpv6": "string",
  "bootstrapBrokerStringSaslScram": "string",
  "bootstrapBrokerStringSaslIamIpv6": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-bootstrap-brokers-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-bootstrap-brokers-properties"></a>

### Error
<a name="clusters-clusterarn-bootstrap-brokers-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### GetBootstrapBrokersResponse
<a name="clusters-clusterarn-bootstrap-brokers-model-getbootstrapbrokersresponse"></a>

Returns a string containing one or more hostname:port pairs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bootstrapBrokerString | string | False | A string containing one or more hostname:port pairs. |
| bootstrapBrokerStringIpv6 | string | False | A string that contains one or more host name (or IP) and port pairs for IPV6 connectivity. |
| bootstrapBrokerStringPublicSaslIam | string | False | A string that is one or more pairs of DNS names (or IP addresses) and SASL IAM ports for public access. |
| bootstrapBrokerStringPublicSaslScram | string | False | A string that is one or more pairs of DNS names (or IP addresses) and SASL IAM ports for public access. |
| bootstrapBrokerStringPublicTls | string | False | A string that is one or more pairs of DNS names (or IP addresses) and SASL IAM ports for public access. |
| bootstrapBrokerStringSaslIam | string | False | A string containing one or more dns name (or IP) and SASL IAM port pairs. |
| bootstrapBrokerStringSaslIamIpv6 | string | False | A string that contains one or more DNS name (or IP) and SASL IAM port for IPV6 connectivity. |
| bootstrapBrokerStringSaslScram | string | False | A string containing one or more dns name (or IP) and SASL SCRAM port pairs. |
| bootstrapBrokerStringSaslScramIpv6 | string | False | A string that contains one or more DNS name (or IP) and SASL SCRAM port pairs for IPV6 connectivity. |
| bootstrapBrokerStringTls | string | False | A string containing one or more DNS names (or IP) and TLS port pairs. The following is an example.<pre>{<br />    "BootstrapBrokerStringTls": "b-3.exampleClusterName.abcde.c2.kafka.us-east-1.amazonaws.com:9094,b-1.exampleClusterName.abcde.c2.kafka.us-east-1.amazonaws.com:9094,b-2.exampleClusterName.abcde.c2.kafka.us-east-1.amazonaws.com:9094"<br />}</pre> |
| bootstrapBrokerStringTlsIpv6 | string | False | A string that contains one or more DNS name (or IP) and TLS port pairs for IPV6 connectivity. |
| bootstrapBrokerStringVpcConnectivitySaslIam | string | False | A string containing one or more dns name (or IP) and SASL IAM port pairs for VPC connectivity. |
| bootstrapBrokerStringVpcConnectivitySaslScram | string | False | A string containing one or more dns name (or IP) and SASL SCRAM port pairs for VPC connectivity. |
| bootstrapBrokerStringVpcConnectivityTls | string | False | A string containing one or more dns name (or IP) and Tls port pairs for VPC connectivity. |

## See also
<a name="clusters-clusterarn-bootstrap-brokers-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetBootstrapBrokers
<a name="GetBootstrapBrokers-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/GetBootstrapBrokers)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/GetBootstrapBrokers)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/GetBootstrapBrokers)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/GetBootstrapBrokers)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/GetBootstrapBrokers)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/GetBootstrapBrokers)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/GetBootstrapBrokers)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/GetBootstrapBrokers)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/GetBootstrapBrokers)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/GetBootstrapBrokers)
