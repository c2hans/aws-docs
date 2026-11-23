---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-assessments-assessmentarn.html
---

# Assessment

## URI
<a name="clusters-clusterarn-assessments-assessmentarn-url"></a>

`/v1/clusters/{{clusterArn}}/assessments/{{assessmentArn}}`

## HTTP methods
<a name="clusters-clusterarn-assessments-assessmentarn-http-methods"></a>

### GET
<a name="clusters-clusterarn-assessments-assessmentarnget"></a>

**Operation ID:** `DescribeAssessment`

Returns the status of an assessment and, once the assessment is complete, a summary of its findings by category and severity. The individual findings are returned by `ListAssessmentFindings`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{assessmentArn}} | String | True | The Amazon Resource Name (ARN) of the assessment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DescribeAssessmentResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### DELETE
<a name="clusters-clusterarn-assessments-assessmentarndelete"></a>

**Operation ID:** `DeleteAssessment`

Deletes an assessment and its findings, and frees one slot against the cluster's assessment quota. The assessment moves to `DELETING` and its findings are removed asynchronously.

An assessment that is still in progress cannot be deleted. Deleting an assessment that is already being deleted succeeds.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| {{assessmentArn}} | String | True | The Amazon Resource Name (ARN) of the assessment to delete. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DeleteAssessmentResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 409 | Error | The assessment is still in progress. Wait for it to complete, then retry your request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-assessments-assessmentarnoptions"></a>

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
<a name="clusters-clusterarn-assessments-assessmentarn-schemas"></a>

### Response bodies
<a name="clusters-clusterarn-assessments-assessmentarn-response-examples"></a>

#### DescribeAssessmentResponse schema
<a name="clusters-clusterarn-assessments-assessmentarn-response-body-describeassessmentresponse-example"></a>

```json
{
  "assessmentArn": "string",
  "clusterArn": "string",
  "assessmentType": enum,
  "status": enum,
  "statusMessage": "string",
  "creationTime": "string",
  "completionTime": "string",
  "assessmentParameters": {
    "targetBrokerType": "string",
    "targetInstanceType": "string"
  },
  "summary": {
    "totalFindings": integer,
    "hasBlockingFindings": boolean,
    "findingsCapped": boolean,
    "byCategory": {
    },
    "bySeverity": {
    }
  },
  "tags": {
  }
}
```

#### DeleteAssessmentResponse schema
<a name="clusters-clusterarn-assessments-assessmentarn-response-body-deleteassessmentresponse-example"></a>

```json
{
  "assessmentArn": "string",
  "status": enum
}
```

#### Error schema
<a name="clusters-clusterarn-assessments-assessmentarn-response-body-error-example"></a>

```json
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-assessments-assessmentarn-properties"></a>

### AssessmentParameters
<a name="clusters-clusterarn-assessments-assessmentarn-model-assessmentparameters"></a>

Type-specific parameters for the assessment. The required fields depend on the assessmentType.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| targetBrokerType | string<br />MaxLength: 64 | False | The broker type to assess readiness for. Specify `EXPRESS` to assess an upgrade from Standard brokers to Express brokers. This parameter is required when `assessmentType` is `UPDATE_BROKER_TYPE`. |
| targetInstanceType | string<br />MaxLength: 256 | False | The specific instance type to assess readiness for, for example `express.m7g.large`. Omit it to have the assessment recommend an instance type instead, which it reports as a `CAPACITY` finding. |

### AssessmentStatus
<a name="clusters-clusterarn-assessments-assessmentarn-model-assessmentstatus"></a>

The lifecycle status of the assessment. While the status is `IN_PROGRESS` the scan is running and no findings are available. When it reaches `COMPLETE`, read `summary` here and the individual findings through `ListAssessmentFindings`. `FAILED` means that the scan did not finish, and `statusMessage` explains why. `DELETING` means that the assessment is being deleted and its findings are being removed.
+ `IN_PROGRESS`
+ `COMPLETE`
+ `FAILED`
+ `DELETING`

### AssessmentSummary
<a name="clusters-clusterarn-assessments-assessmentarn-model-assessmentsummary"></a>

Summary of assessment findings broken down by category and severity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| byCategory | object | False | Count of findings grouped by category. |
| bySeverity | object | False | Count of findings grouped by severity. |
| findingsCapped | boolean | False | `true` when the assessment found more findings than it stores, so `ListAssessmentFindings` returns fewer findings than `totalFindings`. Resolve the findings you can see and run the assessment again to surface the rest. |
| hasBlockingFindings | boolean | False | `true` when the assessment found at least one `ERROR`-severity finding. The upgrade is blocked until every one of them is resolved. Check this field rather than counting findings yourself. |
| totalFindings | integer | False | How many findings the assessment detected in total. When `findingsCapped` is `true`, this count is higher than the number of findings `ListAssessmentFindings` returns. |

### AssessmentType
<a name="clusters-clusterarn-assessments-assessmentarn-model-assessmenttype"></a>

The type of assessment to perform.
+ `UPDATE_BROKER_TYPE`

### DeleteAssessmentResponse
<a name="clusters-clusterarn-assessments-assessmentarn-model-deleteassessmentresponse"></a>

Returns the result of deleting an assessment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| assessmentArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the assessment being deleted. |
| status | [AssessmentStatus](#clusters-clusterarn-assessments-assessmentarn-model-assessmentstatus) | False | The current status of the assessment. Will be DELETING. |

### DescribeAssessmentResponse
<a name="clusters-clusterarn-assessments-assessmentarn-model-describeassessmentresponse"></a>

Returns the status and summary of an assessment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| assessmentArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the assessment. |
| assessmentParameters | [AssessmentParameters](#clusters-clusterarn-assessments-assessmentarn-model-assessmentparameters) | False | The parameters that were provided when creating the assessment. |
| assessmentType | [AssessmentType](#clusters-clusterarn-assessments-assessmentarn-model-assessmenttype) | False | The type of assessment. |
| clusterArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the cluster that was assessed. |
| completionTime | string | False | The time when the assessment completed. Present only when status is COMPLETE or FAILED. |
| creationTime | string | False | The time when the assessment was created. |
| status | [AssessmentStatus](#clusters-clusterarn-assessments-assessmentarn-model-assessmentstatus) | False | The current status of the assessment. |
| statusMessage | string | False | Additional information about the current status. Present when status is FAILED. |
| summary | [AssessmentSummary](#clusters-clusterarn-assessments-assessmentarn-model-assessmentsummary) | False | Summary of findings by category and severity. Present only when status is COMPLETE. |
| tags | object | False | The tags attached to the assessment. |

### Error
<a name="clusters-clusterarn-assessments-assessmentarn-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

## See also
<a name="clusters-clusterarn-assessments-assessmentarn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeAssessment
<a name="DescribeAssessment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DescribeAssessment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DescribeAssessment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DescribeAssessment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DescribeAssessment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DescribeAssessment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DescribeAssessment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DescribeAssessment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DescribeAssessment)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/DescribeAssessment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DescribeAssessment)

### DeleteAssessment
<a name="DeleteAssessment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DeleteAssessment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DeleteAssessment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DeleteAssessment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DeleteAssessment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DeleteAssessment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DeleteAssessment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DeleteAssessment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DeleteAssessment)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/DeleteAssessment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DeleteAssessment)
