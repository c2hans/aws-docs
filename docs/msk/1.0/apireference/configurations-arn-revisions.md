---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn-revisions.html
---

# Configuration Revisions
<a name="configurations-arn-revisions"></a>

Represents the revisions of an MSK configuration.

## URI
<a name="configurations-arn-revisions-url"></a>

`/v1/configurations/{{arn}}/revisions`

## HTTP methods
<a name="configurations-arn-revisions-http-methods"></a>

### GET
<a name="configurations-arn-revisionsget"></a>

**Operation ID:** `ListConfigurationRevisions`

Returns a list of all the revisions of an MSK configuration.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |
| maxResults | String | False | The maximum number of results to return in the response (default maximum 100 results per API call). If there are more results, the response includes a `NextToken` parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListConfigurationRevisionsResponse | 200 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="configurations-arn-revisionsoptions"></a>

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
<a name="configurations-arn-revisions-schemas"></a>

### Response bodies
<a name="configurations-arn-revisions-response-examples"></a>

#### ListConfigurationRevisionsResponse schema
<a name="configurations-arn-revisions-response-body-listconfigurationrevisionsresponse-example"></a>

```
{
  "nextToken": "string",
  "revisions": [
    {
      "creationTime": "string",
      "description": "string",
      "revision": integer
    }
  ]
}
```

#### Error schema
<a name="configurations-arn-revisions-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="configurations-arn-revisions-properties"></a>

### ConfigurationRevision
<a name="configurations-arn-revisions-model-configurationrevision"></a>

Describes a configuration revision.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creationTime | string | True | The time when the configuration revision was created. |
| description | string | False | The description of the configuration revision. |
| revision | integer<br />Format: int64 | True | The revision number. |

### Error
<a name="configurations-arn-revisions-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ListConfigurationRevisionsResponse
<a name="configurations-arn-revisions-model-listconfigurationrevisionsresponse"></a>

Information about revisions of an MSK configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | Paginated results marker. |
| revisions | Array of type [ConfigurationRevision](#configurations-arn-revisions-model-configurationrevision) | False | List of ConfigurationRevision objects. |

## See also
<a name="configurations-arn-revisions-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListConfigurationRevisions
<a name="ListConfigurationRevisions-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListConfigurationRevisions)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListConfigurationRevisions)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListConfigurationRevisions)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListConfigurationRevisions)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListConfigurationRevisions)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListConfigurationRevisions)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListConfigurationRevisions)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListConfigurationRevisions)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/ListConfigurationRevisions)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListConfigurationRevisions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
