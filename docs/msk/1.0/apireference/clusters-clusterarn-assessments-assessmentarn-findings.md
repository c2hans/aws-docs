---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-assessments-assessmentarn-findings.html
---

# Assessment Findings

## URI
<a name="clusters-clusterarn-assessments-assessmentarn-findings-url"></a>

`/v1/clusters/{{clusterArn}}/assessments/{{assessmentArn}}/findings`

## HTTP methods
<a name="clusters-clusterarn-assessments-assessmentarn-findings-http-methods"></a>

### GET
<a name="clusters-clusterarn-assessments-assessmentarn-findingsget"></a>

**Operation ID:** `ListAssessmentFindings`

Returns the findings of a completed assessment. Each finding names the affected resource, what is wrong with it, and how to resolve it. Filter by `category`, by `severity`, or by both.

Findings are available only while the assessment status is `COMPLETE`. An assessment that is still in progress returns a conflict error.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{assessmentArn}} | String | True | The Amazon Resource Name (ARN) of the assessment. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| category | String | False | Optional filter. Only return findings matching this category. |
| severity | String | False | Optional filter. Only return findings matching this severity. |
| maxResults | String | False | The maximum number of findings to return in the response. The default is 100 and the maximum is 500. If there are more results, the response includes a `NextToken` parameter. |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListAssessmentFindingsResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 409 | Error | The assessment is not yet complete. Findings are available only while the assessment status is `COMPLETE`. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-assessments-assessmentarn-findingsoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{assessmentArn}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-assessments-assessmentarn-findings-schemas"></a>

### Response bodies
<a name="clusters-clusterarn-assessments-assessmentarn-findings-response-examples"></a>

#### ListAssessmentFindingsResponse schema
<a name="clusters-clusterarn-assessments-assessmentarn-findings-response-body-listassessmentfindingsresponse-example"></a>

```json
{
  "findings": [
    {
      "findingId": "string",
      "category": enum,
      "severity": enum,
      "resource": "string",
      "message": "string",
      "remediation": {
        "action": "string",
        "documentationUrl": "string"
      }
    }
  ],
  "nextToken": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-assessments-assessmentarn-findings-response-body-error-example"></a>

```json
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-assessments-assessmentarn-findings-properties"></a>

### AssessmentFinding
<a name="clusters-clusterarn-assessments-assessmentarn-findings-model-assessmentfinding"></a>

A single finding from an assessment, describing a specific issue or observation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| category | [FindingCategory](#clusters-clusterarn-assessments-assessmentarn-findings-model-findingcategory) | True | The category of this finding. |
| findingId | string | True | An identifier derived from the content of the finding, not from the assessment run. The same problem on the same resource produces the same `findingId` every time, so you can compare runs to see which findings you have resolved and which are new. |
| message | string | True | Human-readable description of what is wrong, why it matters, and what to do. |
| remediation | [FindingRemediation](#clusters-clusterarn-assessments-assessmentarn-findings-model-findingremediation) | False | Guidance for resolving this finding. Absent when no specific remediation applies. |
| resource | string | False | The specific resource affected (for example, topic name). Absent for cluster-level findings. |
| severity | [FindingSeverity](#clusters-clusterarn-assessments-assessmentarn-findings-model-findingseverity) | True | The severity of this finding. |

### Error
<a name="clusters-clusterarn-assessments-assessmentarn-findings-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### FindingCategory
<a name="clusters-clusterarn-assessments-assessmentarn-findings-model-findingcategory"></a>

The category of an assessment finding.
+ `INFRASTRUCTURE`
+ `BROKER_CONFIGURATION`
+ `TOPIC_CONFIGURATION`
+ `CAPACITY`
+ `HEALTH`

### FindingRemediation
<a name="clusters-clusterarn-assessments-assessmentarn-findings-model-findingremediation"></a>

Guidance for resolving a finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| action | string | False | The recommended action to resolve this finding. |
| documentationUrl | string<br />MaxLength: 2048 | False | A link to documentation with more detail about this finding and how to resolve it. |

### FindingSeverity
<a name="clusters-clusterarn-assessments-assessmentarn-findings-model-findingseverity"></a>

How much attention the finding needs. `ERROR` means that the upgrade cannot proceed until you resolve the condition. `WARNING` means that the upgrade can proceed, but that the condition is likely to cause problems afterwards. `INFO` is reported so that you know about the condition and needs no action.
+ `ERROR`
+ `WARNING`
+ `INFO`

### ListAssessmentFindingsResponse
<a name="clusters-clusterarn-assessments-assessmentarn-findings-model-listassessmentfindingsresponse"></a>

Returns the findings for a completed assessment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| findings | Array of type [AssessmentFinding](#clusters-clusterarn-assessments-assessmentarn-findings-model-assessmentfinding) | False | A list of findings from the assessment. |
| nextToken | string | False | If the response is truncated, it returns a nextToken. Send this in the subsequent request to get the remaining results. |

## See also
<a name="clusters-clusterarn-assessments-assessmentarn-findings-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListAssessmentFindings
<a name="ListAssessmentFindings-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListAssessmentFindings)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListAssessmentFindings)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListAssessmentFindings)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListAssessmentFindings)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListAssessmentFindings)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListAssessmentFindings)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListAssessmentFindings)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListAssessmentFindings)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/ListAssessmentFindings)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListAssessmentFindings)
