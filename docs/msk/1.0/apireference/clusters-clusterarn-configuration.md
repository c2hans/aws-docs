---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-configuration.html
---

# Cluster Configuration
<a name="clusters-clusterarn-configuration"></a>

Represents the configuration of a specific cluster.

## URI
<a name="clusters-clusterarn-configuration-url"></a>

`/v1/clusters/{{clusterArn}}/configuration`

## HTTP methods
<a name="clusters-clusterarn-configuration-http-methods"></a>

### PUT
<a name="clusters-clusterarn-configurationput"></a>

**Operation ID:** `UpdateClusterConfiguration`

Updates the cluster with the configuration that is specified in the request body. Before you invoke this operation, ensure that the number of partitions per broker on your MSK cluster is under the limits described in [Number of partitions per broker](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html#bestpractices-right-size-cluster). You can't update the configuration of an MSK cluster that exceeds these limits.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateClusterConfigurationResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-configurationoptions"></a>

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
<a name="clusters-clusterarn-configuration-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-configuration-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-configuration-request-body-put-example"></a>

```
{
  "configurationInfo": {
    "arn": "string",
    "revision": integer
  },
  "currentVersion": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-configuration-response-examples"></a>

#### UpdateClusterConfigurationResponse schema
<a name="clusters-clusterarn-configuration-response-body-updateclusterconfigurationresponse-example"></a>

```
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-configuration-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-configuration-properties"></a>

### ConfigurationInfo
<a name="clusters-clusterarn-configuration-model-configurationinfo"></a>

Specifies the configuration to use for the brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | ARN of the configuration to use. |
| revision | integer<br />Format: int64<br />Minimum: 1 | True | The revision of the configuration to use. |

### Error
<a name="clusters-clusterarn-configuration-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### UpdateClusterConfigurationRequest
<a name="clusters-clusterarn-configuration-model-updateclusterconfigurationrequest"></a>

Request body for UpdateClusterConfiguration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configurationInfo | [ConfigurationInfo](#clusters-clusterarn-configuration-model-configurationinfo) | True | Represents the configuration that you want MSK to use for the cluster. |
| currentVersion | string | True | The version of the cluster that you want to update. |

### UpdateClusterConfigurationResponse
<a name="clusters-clusterarn-configuration-model-updateclusterconfigurationresponse"></a>

Response body for UpdateClusterConfiguration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

## See also
<a name="clusters-clusterarn-configuration-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateClusterConfiguration
<a name="UpdateClusterConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateClusterConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateClusterConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateClusterConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateClusterConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateClusterConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateClusterConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateClusterConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateClusterConfiguration)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/UpdateClusterConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateClusterConfiguration)
