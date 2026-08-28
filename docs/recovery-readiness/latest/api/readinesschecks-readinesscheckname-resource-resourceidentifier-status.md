---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname-resource-resourceidentifier-status.html
---

# GetReadinessCheckResourceStatus
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status"></a>

## URI
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status-url"></a>

`/readinesschecks/{{readinessCheckName}}/resource/{{resourceIdentifier}}/status`

## HTTP methods
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status-http-methods"></a>

### GET
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-statusget"></a>

**Operation ID:** `GetReadinessCheckResourceStatus`

Gets individual readiness status for a readiness check. To see the overall readiness status for a recovery group, that considers the readiness status for all the readiness checks in the recovery group, use `GetRecoveryGroupReadinessSummary`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{readinessCheckName}} | String | True | Name of a readiness check. |
| {{resourceIdentifier}} | String | True | The resource identifier, which is the Amazon Resource Name (ARN) or the identifier generated for the resource by Application Recovery Controller (for example, for a DNS target resource). |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that identifies which batch of results you want to see. |
| maxResults | String | False | The number of objects that you want to return with this call. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetReadinessCheckResourceStatusOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-statusoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{readinessCheckName}} | String | True | Name of a readiness check. |
| {{resourceIdentifier}} | String | True | The resource identifier, which is the Amazon Resource Name (ARN) or the identifier generated for the resource by Application Recovery Controller (for example, for a DNS target resource). |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status-schemas"></a>

### Response bodies
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status-response-examples"></a>

#### GetReadinessCheckResourceStatusOutput schema
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status-response-body-getreadinesscheckresourcestatusoutput-example"></a>

```
{
  "nextToken": "string",
  "readiness": enum,
  "rules": [
    {
      "readiness": enum,
      "messages": [
        {
          "messageText": "string"
        }
      ],
      "lastCheckedTimestamp": "string",
      "ruleId": "string"
    }
  ]
}
```

## Properties
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status-properties"></a>

### GetReadinessCheckResourceStatusOutput
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status-model-getreadinesscheckresourcestatusoutput"></a>

Result of a `GetReadinessCheckResourceStatus` operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | True | The token that identifies which batch of results you want to see. |
| readiness | [Readiness](#readinesschecks-readinesscheckname-resource-resourceidentifier-status-model-readiness) | True | The readiness at a rule level. |
| rules | Array of type [RuleResult](#readinesschecks-readinesscheckname-resource-resourceidentifier-status-model-ruleresult) | True | Details of the rule's results. |

### Message
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status-model-message"></a>

Information relating to readiness check status.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| messageText | string | False | The text of a readiness check message. |

### Readiness
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status-model-readiness"></a>

The readiness status.
+ `READY`
+ `NOT_READY`
+ `UNKNOWN`
+ `NOT_AUTHORIZED`

### RuleResult
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status-model-ruleresult"></a>

The result of a successful `Rule` request, with status for an individual rule.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| lastCheckedTimestamp | string | True | The time the resource was last checked for readiness, in ISO-8601 format, UTC. |
| messages | Array of type [Message](#readinesschecks-readinesscheckname-resource-resourceidentifier-status-model-message) | True | Details about the resource's readiness. |
| readiness | [Readiness](#readinesschecks-readinesscheckname-resource-resourceidentifier-status-model-readiness) | True | The readiness at rule level. |
| ruleId | string | True | The identifier of the rule. |

## See also
<a name="readinesschecks-readinesscheckname-resource-resourceidentifier-status-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetReadinessCheckResourceStatus
<a name="GetReadinessCheckResourceStatus-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/GetReadinessCheckResourceStatus)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/GetReadinessCheckResourceStatus)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/GetReadinessCheckResourceStatus)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/GetReadinessCheckResourceStatus)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/GetReadinessCheckResourceStatus)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/GetReadinessCheckResourceStatus)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/GetReadinessCheckResourceStatus)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/GetReadinessCheckResourceStatus)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/GetReadinessCheckResourceStatus)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/GetReadinessCheckResourceStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
