---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname-architecturerecommendations.html
---

# GetArchitectureRecommendations
<a name="recoverygroups-recoverygroupname-architecturerecommendations"></a>

## URI
<a name="recoverygroups-recoverygroupname-architecturerecommendations-url"></a>

`/recoverygroups/{{recoveryGroupName}}/architectureRecommendations`

## HTTP methods
<a name="recoverygroups-recoverygroupname-architecturerecommendations-http-methods"></a>

### GET
<a name="recoverygroups-recoverygroupname-architecturerecommendationsget"></a>

**Operation ID:** `GetArchitectureRecommendations`

Gets recommendations about architecture designs for improving resiliency for an application, based on a recovery group.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recoveryGroupName}} | String | True | The name of a recovery group. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that identifies which batch of results you want to see. |
| maxResults | String | False | The number of objects that you want to return with this call. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetArchitectureRecommendationsOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="recoverygroups-recoverygroupname-architecturerecommendationsoptions"></a>

Enables CORS by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recoveryGroupName}} | String | True | The name of a recovery group. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="recoverygroups-recoverygroupname-architecturerecommendations-schemas"></a>

### Response bodies
<a name="recoverygroups-recoverygroupname-architecturerecommendations-response-examples"></a>

#### GetArchitectureRecommendationsOutput schema
<a name="recoverygroups-recoverygroupname-architecturerecommendations-response-body-getarchitecturerecommendationsoutput-example"></a>

```
{
  "lastAuditTimestamp": "string",
  "nextToken": "string",
  "recommendations": [
    {
      "recommendationText": "string"
    }
  ]
}
```

## Properties
<a name="recoverygroups-recoverygroupname-architecturerecommendations-properties"></a>

### GetArchitectureRecommendationsOutput
<a name="recoverygroups-recoverygroupname-architecturerecommendations-model-getarchitecturerecommendationsoutput"></a>

Result from `GetArchitectureRecommendations` call.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| lastAuditTimestamp | string | True | The time that a recovery group was last assessed for recommendations, in UTC ISO-8601 format. |
| nextToken | string | False | The token that identifies which batch of results you want to see. |
| recommendations | Array of type [Recommendation](#recoverygroups-recoverygroupname-architecturerecommendations-model-recommendation) | True | A list of the recommendations for the customer's application. |

### Recommendation
<a name="recoverygroups-recoverygroupname-architecturerecommendations-model-recommendation"></a>

Recommendations that are provided to make an application more recovery resilient.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| recommendationText | string | True | Text of the recommendations that are provided to make an application more recovery resilient. |

## See also
<a name="recoverygroups-recoverygroupname-architecturerecommendations-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetArchitectureRecommendations
<a name="GetArchitectureRecommendations-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/GetArchitectureRecommendations)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/GetArchitectureRecommendations)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/GetArchitectureRecommendations)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/GetArchitectureRecommendations)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/GetArchitectureRecommendations)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/GetArchitectureRecommendations)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/GetArchitectureRecommendations)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/GetArchitectureRecommendations)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/GetArchitectureRecommendations)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/GetArchitectureRecommendations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
