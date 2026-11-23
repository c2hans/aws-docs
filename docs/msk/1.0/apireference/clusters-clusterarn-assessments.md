---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-assessments.html
---

# Assessments

Assessments scan a cluster for readiness before you change it. An assessment of type `UPDATE_BROKER_TYPE` reports every condition that would block or complicate an in-place upgrade from Standard brokers to Express brokers, so that you can resolve the conditions before you call `UpdateBrokerType`.

## URI
<a name="clusters-clusterarn-assessments-url"></a>

`/v1/clusters/{{clusterArn}}/assessments`

## HTTP methods
<a name="clusters-clusterarn-assessments-http-methods"></a>

### GET
<a name="clusters-clusterarn-assessmentsget"></a>

**Operation ID:** `ListAssessments`

Returns the assessments for a cluster, newest first. Filter by `assessmentType` to narrow the list.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| assessmentType | String | False | Optional filter. The type of assessment to filter by. |
| maxResults | String | False | The maximum number of assessments to return in the response. The default is 25 and the maximum is 100. If there are more results, the response includes a `NextToken` parameter. |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListAssessmentsResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### POST
<a name="clusters-clusterarn-assessmentspost"></a>

**Operation ID:** `CreateAssessment`

Creates an assessment for a cluster and starts an asynchronous, read-only scan. The operation returns as soon as the scan starts; poll `DescribeAssessment` for the result and call `ListAssessmentFindings` once the status is `COMPLETE`.

A cluster can have only one assessment of a given type in progress at a time. If one is already in progress, this operation returns that assessment rather than creating another. When the cluster has reached its assessment quota, the operation fails; delete a completed or failed assessment to free a slot.

The scan does not lock the cluster and does not change it.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateAssessmentResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 409 | Error | An assessment of the same type is already in progress for this cluster. Wait for it to complete, or read it with `DescribeAssessment`. |
| 429 | Error | The cluster has reached its assessment quota. Delete a completed or failed assessment for this cluster, then retry your request. |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-assessmentsoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-assessments-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-assessments-request-examples"></a>

#### POST schema
<a name="clusters-clusterarn-assessments-request-body-post-example"></a>

```json
{
  "assessmentType": enum,
  "assessmentParameters": {
    "targetBrokerType": "string",
    "targetInstanceType": "string"
  },
  "tags": {
  }
}
```

### Response bodies
<a name="clusters-clusterarn-assessments-response-examples"></a>

#### ListAssessmentsResponse schema
<a name="clusters-clusterarn-assessments-response-body-listassessmentsresponse-example"></a>

```json
{
  "assessments": [
    {
      "assessmentArn": "string",
      "clusterArn": "string",
      "assessmentType": enum,
      "status": enum,
      "creationTime": "string",
      "tags": {
      }
    }
  ],
  "nextToken": "string"
}
```

#### CreateAssessmentResponse schema
<a name="clusters-clusterarn-assessments-response-body-createassessmentresponse-example"></a>

```json
{
  "assessmentArn": "string",
  "clusterArn": "string",
  "assessmentType": enum,
  "status": enum,
  "creationTime": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-assessments-response-body-error-example"></a>

```json
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-assessments-properties"></a>

### AssessmentInfo
<a name="clusters-clusterarn-assessments-model-assessmentinfo"></a>

Summary information about an assessment, returned by ListAssessments.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| assessmentArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the assessment. |
| assessmentType | [AssessmentType](#clusters-clusterarn-assessments-model-assessmenttype) | False | The type of assessment. |
| clusterArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the cluster that was assessed. |
| creationTime | string | False | The time when the assessment was created. |
| status | [AssessmentStatus](#clusters-clusterarn-assessments-model-assessmentstatus) | False | The current status of the assessment. |
| tags | object | False | The tags attached to the assessment. |

### AssessmentParameters
<a name="clusters-clusterarn-assessments-model-assessmentparameters"></a>

Type-specific parameters for the assessment. The required fields depend on the assessmentType.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| targetBrokerType | string<br />MaxLength: 64 | False | The broker type to assess readiness for. Specify `EXPRESS` to assess an upgrade from Standard brokers to Express brokers. This parameter is required when `assessmentType` is `UPDATE_BROKER_TYPE`. |
| targetInstanceType | string<br />MaxLength: 256 | False | The specific instance type to assess readiness for, for example `express.m7g.large`. Omit it to have the assessment recommend an instance type instead, which it reports as a `CAPACITY` finding. |

### AssessmentStatus
<a name="clusters-clusterarn-assessments-model-assessmentstatus"></a>

The lifecycle status of the assessment. While the status is `IN_PROGRESS` the scan is running and no findings are available. When it reaches `COMPLETE`, read `summary` here and the individual findings through `ListAssessmentFindings`. `FAILED` means that the scan did not finish, and `statusMessage` explains why. `DELETING` means that the assessment is being deleted and its findings are being removed.
+ `IN_PROGRESS`
+ `COMPLETE`
+ `FAILED`
+ `DELETING`

### AssessmentType
<a name="clusters-clusterarn-assessments-model-assessmenttype"></a>

The type of assessment to perform.
+ `UPDATE_BROKER_TYPE`

### CreateAssessmentRequest
<a name="clusters-clusterarn-assessments-model-createassessmentrequest"></a>

Creates a new assessment for a cluster. Kicks off an asynchronous scan and returns immediately with an assessment ARN and status.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| assessmentParameters | [AssessmentParameters](#clusters-clusterarn-assessments-model-assessmentparameters) | False | Type-specific parameters for the assessment. Required parameters depend on the assessmentType. |
| assessmentType | [AssessmentType](#clusters-clusterarn-assessments-model-assessmenttype) | True | The type of assessment to perform. |
| tags | object | False | The tags to attach to the assessment. |

### CreateAssessmentResponse
<a name="clusters-clusterarn-assessments-model-createassessmentresponse"></a>

Returns information about the created assessment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| assessmentArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the assessment. |
| assessmentType | [AssessmentType](#clusters-clusterarn-assessments-model-assessmenttype) | False | The type of assessment. |
| clusterArn | string<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN) of the cluster being assessed. |
| creationTime | string | False | The time when the assessment was created. |
| status | [AssessmentStatus](#clusters-clusterarn-assessments-model-assessmentstatus) | False | The current status of the assessment. |

### Error
<a name="clusters-clusterarn-assessments-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ListAssessmentsResponse
<a name="clusters-clusterarn-assessments-model-listassessmentsresponse"></a>

Returns a list of assessments.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| assessments | Array of type [AssessmentInfo](#clusters-clusterarn-assessments-model-assessmentinfo) | False | A list of assessment summaries. |
| nextToken | string | False | If the response is truncated, it returns a nextToken. Send this in the subsequent request to get the remaining results. |

## See also
<a name="clusters-clusterarn-assessments-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListAssessments
<a name="ListAssessments-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListAssessments)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListAssessments)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListAssessments)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListAssessments)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListAssessments)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListAssessments)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListAssessments)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListAssessments)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/ListAssessments)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListAssessments)

### CreateAssessment
<a name="CreateAssessment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/CreateAssessment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/CreateAssessment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/CreateAssessment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/CreateAssessment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/CreateAssessment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/CreateAssessment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/CreateAssessment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/CreateAssessment)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/CreateAssessment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/CreateAssessment)
