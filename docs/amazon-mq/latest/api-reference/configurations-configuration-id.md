---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/configurations-configuration-id.html
---

# Configuration
<a name="configurations-configuration-id"></a>

A configuration contains all of the settings for your broker. For more information, see [Amazon MQ for RabbitMQ broker configurations](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-broker-configuration-parameters.html) and [Amazon MQ for ActiveMQ broker configurations](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html) in the Amazon MQ Developer Guide.

You can create a configuration before creating any brokers. You can then apply the configuration to one or more brokers.

**Important**
Making changes to a configuration does not apply the changes to the broker immediately. To apply your changes, you must wait for the next maintenance window or reboot the broker.

## URI
<a name="configurations-configuration-id-url"></a>

`/v1/configurations/{{configuration-id}}`

## HTTP methods
<a name="configurations-configuration-id-http-methods"></a>

### GET
<a name="configurations-configuration-idget"></a>

**Operation ID:** `DescribeConfiguration`

Returns information about the specified configuration.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{configuration-id}} | String | True | The unique ID that Amazon MQ generates for the configuration. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  Configuration | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### PUT
<a name="configurations-configuration-idput"></a>

**Operation ID:** `UpdateConfiguration`

Updates the specified configuration.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{configuration-id}} | String | True | The unique ID that Amazon MQ generates for the configuration. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateConfigurationOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 409 | Error | HTTP Status Code 409: Configuration ID is already in use. Remove the configuration from all brokers and retry the request. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### DELETE
<a name="configurations-configuration-iddelete"></a>

**Operation ID:** `DeleteConfiguration`

Deletes the specified configuration.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{configuration-id}} | String | True | The unique ID that Amazon MQ generates for the configuration. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DeleteConfigurationOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 409 | Error | HTTP Status Code 409: Configuration ID is already in use. Remove the configuration from all brokers and retry the request. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="configurations-configuration-idoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{configuration-id}} | String | True | The unique ID that Amazon MQ generates for the configuration. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="configurations-configuration-id-schemas"></a>

### Request bodies
<a name="configurations-configuration-id-request-examples"></a>

#### PUT schema
<a name="configurations-configuration-id-request-body-put-example"></a>

```
{
  "data": "string",
  "description": "string"
}
```

### Response bodies
<a name="configurations-configuration-id-response-examples"></a>

#### Configuration schema
<a name="configurations-configuration-id-response-body-configuration-example"></a>

```
{
  "engineVersion": "string",
  "created": "string",
  "authenticationStrategy": enum,
  "name": "string",
  "description": "string",
  "engineType": enum,
  "id": "string",
  "arn": "string",
  "latestRevision": {
    "created": "string",
    "description": "string",
    "revision": integer
  },
  "tags": {
  }
}
```

#### UpdateConfigurationOutput schema
<a name="configurations-configuration-id-response-body-updateconfigurationoutput-example"></a>

```
{
  "created": "string",
  "warnings": [
    {
      "reason": enum,
      "attributeName": "string",
      "elementName": "string"
    }
  ],
  "name": "string",
  "id": "string",
  "arn": "string",
  "latestRevision": {
    "created": "string",
    "description": "string",
    "revision": integer
  }
}
```

#### DeleteConfigurationOutput schema
<a name="configurations-configuration-id-response-body-deleteconfigurationoutput-example"></a>

```
{
  "configurationId": "string"
}
```

#### Error schema
<a name="configurations-configuration-id-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="configurations-configuration-id-properties"></a>

### AuthenticationStrategy
<a name="configurations-configuration-id-model-authenticationstrategy"></a>

Optional. The authentication strategy used to secure the broker. The default is `SIMPLE`.
+ `SIMPLE`
+ `LDAP`
+ `CONFIG_MANAGED`

### Configuration
<a name="configurations-configuration-id-model-configuration"></a>

Returns information about all configurations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | Required. The ARN of the configuration. |
| authenticationStrategy | [AuthenticationStrategy](#configurations-configuration-id-model-authenticationstrategy) | True | Optional. The authentication strategy associated with the configuration. The default is `SIMPLE`. |
| created | string<br />Format: date-time | True | Required. The date and time of the configuration revision. |
| description | string | True | Required. The description of the configuration. |
| engineType | [EngineType](#configurations-configuration-id-model-enginetype) | True | Required. The type of broker engine. Currently, Amazon MQ supports `ACTIVEMQ` and `RABBITMQ`. |
| engineVersion | string | True | The broker engine version. Defaults to the latest available version for the specified broker engine type. For a list of supported engine versions, see the [ActiveMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide. |
| id | string | True | Required. The unique ID that Amazon MQ generates for the configuration. |
| latestRevision | [ConfigurationRevision](#configurations-configuration-id-model-configurationrevision) | True | Required. The latest revision of the configuration. |
| name | string | True | Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 1-150 characters long. |
| tags | object | False | The list of all tags associated with this configuration. |

### ConfigurationRevision
<a name="configurations-configuration-id-model-configurationrevision"></a>

Returns information about the specified configuration revision.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| created | string<br />Format: date-time | True | Required. The date and time of the configuration revision. |
| description | string | False | The description of the configuration revision. |
| revision | integer | True | Required. The revision number of the configuration. |

### DeleteConfigurationOutput
<a name="configurations-configuration-id-model-deleteconfigurationoutput"></a>

Returns information about the deleted configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configurationId | string | False | The unique ID that Amazon MQ generates for the configuration. |

### EngineType
<a name="configurations-configuration-id-model-enginetype"></a>

The type of broker engine. Amazon MQ supports ActiveMQ and RabbitMQ.
+ `ACTIVEMQ`
+ `RABBITMQ`

### Error
<a name="configurations-configuration-id-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

### SanitizationWarning
<a name="configurations-configuration-id-model-sanitizationwarning"></a>

Returns information about the configuration element or attribute that was sanitized in the configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attributeName | string | False | The name of the configuration attribute that has been sanitized. |
| elementName | string | False | The name of the configuration element that has been sanitized. |
| reason | [SanitizationWarningReason](#configurations-configuration-id-model-sanitizationwarningreason) | True | The reason for which the configuration elements or attributes were sanitized. |

### SanitizationWarningReason
<a name="configurations-configuration-id-model-sanitizationwarningreason"></a>

The reason for which the configuration elements or attributes were sanitized.
+ `DISALLOWED_ELEMENT_REMOVED`
+ `DISALLOWED_ATTRIBUTE_REMOVED`
+ `INVALID_ATTRIBUTE_VALUE_REMOVED`

### UpdateConfigurationInput
<a name="configurations-configuration-id-model-updateconfigurationinput"></a>

Updates the specified configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| data | string<br />Format: byte | True | Amazon MQ for Active MQ: The base64-encoded XML configuration. Amazon MQ for RabbitMQ: the base64-encoded Cuttlefish configuration. |
| description | string | False | The description of the configuration. |

### UpdateConfigurationOutput
<a name="configurations-configuration-id-model-updateconfigurationoutput"></a>

Returns information about the updated configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | The Amazon Resource Name (ARN) of the configuration. |
| created | string<br />Format: date-time | True | Required. The date and time of the configuration. |
| id | string | True | The unique ID that Amazon MQ generates for the configuration. |
| latestRevision | [ConfigurationRevision](#configurations-configuration-id-model-configurationrevision) | False | The latest revision of the configuration. |
| name | string | True | The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 1-150 characters long. |
| warnings | Array of type [SanitizationWarning](#configurations-configuration-id-model-sanitizationwarning) | False | The list of the first 20 warnings about the configuration elements or attributes that were sanitized. |

## See also
<a name="configurations-configuration-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeConfiguration
<a name="DescribeConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/DescribeConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/DescribeConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/DescribeConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/DescribeConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/DescribeConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/DescribeConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/DescribeConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/DescribeConfiguration)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/DescribeConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/DescribeConfiguration)

### UpdateConfiguration
<a name="UpdateConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/UpdateConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/UpdateConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/UpdateConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/UpdateConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/UpdateConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/UpdateConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/UpdateConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/UpdateConfiguration)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/UpdateConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/UpdateConfiguration)

### DeleteConfiguration
<a name="DeleteConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/DeleteConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/DeleteConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/DeleteConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/DeleteConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/DeleteConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/DeleteConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/DeleteConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/DeleteConfiguration)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/DeleteConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/DeleteConfiguration)
