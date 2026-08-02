---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn-revisions-revision.html
---

# Configuration Revision
<a name="configurations-arn-revisions-revision"></a>

Represents a specific revision of an MSK configuration.

## URI
<a name="configurations-arn-revisions-revision-url"></a>

`/v1/configurations/{{arn}}/revisions/{{revision}}`

## HTTP methods
<a name="configurations-arn-revisions-revision-http-methods"></a>

### GET
<a name="configurations-arn-revisions-revisionget"></a>

**Operation ID:** `DescribeConfigurationRevision`

Returns a description of this revision of the configuration.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{revision}} | String | True | A string that uniquely identifies a revision of an MSK configuration. |
| {{arn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeConfigurationRevisionResponse | 200 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="configurations-arn-revisions-revisionoptions"></a>

Enable CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{revision}} | String | True | A string that uniquely identifies a revision of an MSK configuration. |
| {{arn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="configurations-arn-revisions-revision-schemas"></a>

### Response bodies
<a name="configurations-arn-revisions-revision-response-examples"></a>

#### DescribeConfigurationRevisionResponse schema
<a name="configurations-arn-revisions-revision-response-body-describeconfigurationrevisionresponse-example"></a>

```
{
  "creationTime": "string",
  "description": "string",
  "serverProperties": "string",
  "arn": "string",
  "revision": integer
}
```

#### Error schema
<a name="configurations-arn-revisions-revision-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="configurations-arn-revisions-revision-properties"></a>

### DescribeConfigurationRevisionResponse
<a name="configurations-arn-revisions-revision-model-describeconfigurationrevisionresponse"></a>

Response body for DescribeConfigurationRevision.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | The Amazon Resource Name (ARN) of the configuration. |
| creationTime | string | True | The time when the configuration was created. |
| description | string | True | The description of the configuration. |
| revision | integer<br />Format: int64 | True | The revision number. |
| serverProperties | string | True | Contents of the `server.properties` file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the console, the SDK, or the CLI, the contents of `server.properties` can be in plaintext. |

### Error
<a name="configurations-arn-revisions-revision-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

## See also
<a name="configurations-arn-revisions-revision-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeConfigurationRevision
<a name="DescribeConfigurationRevision-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DescribeConfigurationRevision)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DescribeConfigurationRevision)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DescribeConfigurationRevision)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DescribeConfigurationRevision)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DescribeConfigurationRevision)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DescribeConfigurationRevision)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DescribeConfigurationRevision)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DescribeConfigurationRevision)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/DescribeConfigurationRevision)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DescribeConfigurationRevision)
