---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn.html
---

# Configuration
<a name="configurations-arn"></a>

Represents an MSK configuration. Use this path to describe the configuration.

## URI
<a name="configurations-arn-url"></a>

`/v1/configurations/{{arn}}`

## HTTP methods
<a name="configurations-arn-http-methods"></a>

### GET
<a name="configurations-arnget"></a>

**Operation ID:** `DescribeConfiguration`

Returns a description of this MSK configuration.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeConfigurationResponse | 200 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### PUT
<a name="configurations-arnput"></a>

**Operation ID:** `UpdateConfiguration`

Creates a new revision of the cluster configuration. The configuration must be in the `ACTIVE` state.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateConfigurationResponse | 200 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 409 | Error | This cluster name already exists. Retry your request using another name. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### DELETE
<a name="configurations-arndelete"></a>

**Operation ID:** `DeleteConfiguration`

Deletes a cluster configuration and all its revisions.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DeleteConfigurationResponse | 200 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="configurations-arnoptions"></a>

Enable CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="configurations-arn-schemas"></a>

### Request bodies
<a name="configurations-arn-request-examples"></a>

#### PUT schema
<a name="configurations-arn-request-body-put-example"></a>

```
{
  "description": "string",
  "serverProperties": "string"
}
```

### Response bodies
<a name="configurations-arn-response-examples"></a>

#### DescribeConfigurationResponse schema
<a name="configurations-arn-response-body-describeconfigurationresponse-example"></a>

```
{
  "creationTime": "string",
  "name": "string",
  "description": "string",
  "kafkaVersions": [
    "string"
  ],
  "state": enum,
  "arn": "string",
  "latestRevision": {
    "creationTime": "string",
    "description": "string",
    "revision": integer
  }
}
```

#### UpdateConfigurationResponse schema
<a name="configurations-arn-response-body-updateconfigurationresponse-example"></a>

```
{
  "arn": "string",
  "latestRevision": {
    "creationTime": "string",
    "description": "string",
    "revision": integer
  }
}
```

#### DeleteConfigurationResponse schema
<a name="configurations-arn-response-body-deleteconfigurationresponse-example"></a>

```
{
  "state": enum,
  "Arn": "string"
}
```

#### Error schema
<a name="configurations-arn-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="configurations-arn-properties"></a>

### ConfigurationRevision
<a name="configurations-arn-model-configurationrevision"></a>

Describes a configuration revision.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creationTime | string | True | The time when the configuration revision was created. |
| description | string | False | The description of the configuration revision. |
| revision | integer<br />Format: int64 | True | The revision number. |

### ConfigurationState
<a name="configurations-arn-model-configurationstate"></a>

State of a kafka configuration
+ `ACTIVE`
+ `DELETING`
+ `DELETE_FAILED`

### DeleteConfigurationResponse
<a name="configurations-arn-model-deleteconfigurationresponse"></a>

Returns information about the deleted configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Arn | string | False | The Amazon Resource Name (ARN) of the configuration. |
| state | [ConfigurationState](#configurations-arn-model-configurationstate) | False | State of the configuration. |

### DescribeConfigurationResponse
<a name="configurations-arn-model-describeconfigurationresponse"></a>

Response body for DescribeConfiguration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | The Amazon Resource Name (ARN) of the configuration. |
| creationTime | string | True | The time when the configuration was created. |
| description | string | True | The description of the configuration. |
| kafkaVersions | Array of type string | True | The versions of Apache Kafka with which you can use this MSK configuration. |
| latestRevision | [ConfigurationRevision](#configurations-arn-model-configurationrevision) | True | Latest revision of the configuration. |
| name | string | True | The name of the configuration. Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$". |
| state | [ConfigurationState](#configurations-arn-model-configurationstate) | False | State of the configuration. |

### Error
<a name="configurations-arn-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### UpdateConfigurationRequest
<a name="configurations-arn-model-updateconfigurationrequest"></a>

Update an MSK configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string | False | The description of the configuration. |
| serverProperties | string | True | Contents of the `server.properties` file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the console, the SDK, or the CLI, the contents of `server.properties` can be in plaintext. |

### UpdateConfigurationResponse
<a name="configurations-arn-model-updateconfigurationresponse"></a>

Response body for UpdateConfiguration

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) of the configuration. |
| latestRevision | [ConfigurationRevision](#configurations-arn-model-configurationrevision) | False | Latest revision of the configuration. |

## See also
<a name="configurations-arn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeConfiguration
<a name="DescribeConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DescribeConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DescribeConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DescribeConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DescribeConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DescribeConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DescribeConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DescribeConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DescribeConfiguration)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/DescribeConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DescribeConfiguration)

### UpdateConfiguration
<a name="UpdateConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateConfiguration)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/UpdateConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateConfiguration)

### DeleteConfiguration
<a name="DeleteConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DeleteConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DeleteConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DeleteConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DeleteConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DeleteConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DeleteConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DeleteConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DeleteConfiguration)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/DeleteConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DeleteConfiguration)
