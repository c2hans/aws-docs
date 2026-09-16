---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/configurations-configuration-id-revisions-configuration-revision.html
---

# Configuration Revision
<a name="configurations-configuration-id-revisions-configuration-revision"></a>

To keep track of the changes you make to your configuration, you can create configuration revisions. For more information, see [Configuration](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configuration.html) in the Amazon MQ Developer Guide.

**Important**
Making changes to a configuration does not apply the changes to the broker immediately. To apply your changes, you must wait for the next maintenance window or reboot the broker.

## URI
<a name="configurations-configuration-id-revisions-configuration-revision-url"></a>

`/v1/configurations/{{configuration-id}}/revisions/{{configuration-revision}}`

## HTTP methods
<a name="configurations-configuration-id-revisions-configuration-revision-http-methods"></a>

### GET
<a name="configurations-configuration-id-revisions-configuration-revisionget"></a>

**Operation ID:** `DescribeConfigurationRevision`

Returns the specified configuration revision for the specified configuration.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{configuration-revision}} | String | True | The revision of the configuration. |
| {{configuration-id}} | String | True | The unique ID that Amazon MQ generates for the configuration. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeConfigurationRevisionOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="configurations-configuration-id-revisions-configuration-revisionoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{configuration-revision}} | String | True | The revision of the configuration. |
| {{configuration-id}} | String | True | The unique ID that Amazon MQ generates for the configuration. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="configurations-configuration-id-revisions-configuration-revision-schemas"></a>

### Response bodies
<a name="configurations-configuration-id-revisions-configuration-revision-response-examples"></a>

#### DescribeConfigurationRevisionOutput schema
<a name="configurations-configuration-id-revisions-configuration-revision-response-body-describeconfigurationrevisionoutput-example"></a>

```
{
  "data": "string",
  "created": "string",
  "description": "string",
  "configurationId": "string"
}
```

#### Error schema
<a name="configurations-configuration-id-revisions-configuration-revision-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="configurations-configuration-id-revisions-configuration-revision-properties"></a>

### DescribeConfigurationRevisionOutput
<a name="configurations-configuration-id-revisions-configuration-revision-model-describeconfigurationrevisionoutput"></a>

Returns the specified configuration revision for the specified configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configurationId | string | True | Required. The unique ID that Amazon MQ generates for the configuration. |
| created | string<br />Format: date-time | True | Required. The date and time of the configuration. |
| data | string<br />Format: byte | True | Amazon MQ for ActiveMQ: the base64-encoded XML configuration. Amazon MQ for RabbitMQ: base64-encoded Cuttlefish.  |
| description | string | False | The description of the configuration. |

### Error
<a name="configurations-configuration-id-revisions-configuration-revision-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

## See also
<a name="configurations-configuration-id-revisions-configuration-revision-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeConfigurationRevision
<a name="DescribeConfigurationRevision-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/DescribeConfigurationRevision)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/DescribeConfigurationRevision)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/DescribeConfigurationRevision)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/DescribeConfigurationRevision)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/DescribeConfigurationRevision)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/DescribeConfigurationRevision)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/DescribeConfigurationRevision)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/DescribeConfigurationRevision)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mq-2017-11-27/DescribeConfigurationRevision)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/DescribeConfigurationRevision)
