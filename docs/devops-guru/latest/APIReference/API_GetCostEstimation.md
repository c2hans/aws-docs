---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_GetCostEstimation.html
---

# GetCostEstimation
<a name="API_GetCostEstimation"></a>

Returns an estimate of the monthly cost for DevOps Guru to analyze your AWS resources. For more information, see [Estimate your Amazon DevOps Guru costs](https://docs.aws.amazon.com/devops-guru/latest/userguide/cost-estimate.html) and [Amazon DevOps Guru pricing](http://aws.amazon.com/devops-guru/pricing/).

## Request Syntax
<a name="API_GetCostEstimation_RequestSyntax"></a>

```
GET /cost-estimation?NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCostEstimation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [NextToken](#API_GetCostEstimation_RequestSyntax) **   <a name="DevOpsGuru-GetCostEstimation-request-uri-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

## Request Body
<a name="API_GetCostEstimation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCostEstimation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Costs": [
      {
         "Cost": number,
         "Count": number,
         "State": "string",
         "Type": "string",
         "UnitCost": number
      }
   ],
   "NextToken": "string",
   "ResourceCollection": {
      "CloudFormation": {
         "StackNames": [ "string" ]
      },
      "Tags": [
         {
            "AppBoundaryKey": "string",
            "TagValues": [ "string" ]
         }
      ]
   },
   "Status": "string",
   "TimeRange": {
      "EndTime": number,
      "StartTime": number
   },
   "TotalCost": number
}
```

## Response Elements
<a name="API_GetCostEstimation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Costs](#API_GetCostEstimation_ResponseSyntax) **   <a name="DevOpsGuru-GetCostEstimation-response-Costs"></a>
An array of `ResourceCost` objects that each contains details about the monthly cost estimate to analyze one of your AWS resources.
Type: Array of [ServiceResourceCost](API_ServiceResourceCost.md) objects

 ** [NextToken](#API_GetCostEstimation_ResponseSyntax) **   <a name="DevOpsGuru-GetCostEstimation-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [ResourceCollection](#API_GetCostEstimation_ResponseSyntax) **   <a name="DevOpsGuru-GetCostEstimation-response-ResourceCollection"></a>
The collection of the AWS resources used to create your monthly DevOps Guru cost estimate.
Type: [CostEstimationResourceCollectionFilter](API_CostEstimationResourceCollectionFilter.md) object

 ** [Status](#API_GetCostEstimation_ResponseSyntax) **   <a name="DevOpsGuru-GetCostEstimation-response-Status"></a>
The status of creating this cost estimate. If it's still in progress, the status `ONGOING` is returned. If it is finished, the status `COMPLETED` is returned.
Type: String
Valid Values: `ONGOING | COMPLETED`

 ** [TimeRange](#API_GetCostEstimation_ResponseSyntax) **   <a name="DevOpsGuru-GetCostEstimation-response-TimeRange"></a>
The start and end time of the cost estimation.
Type: [CostEstimationTimeRange](API_CostEstimationTimeRange.md) object

 ** [TotalCost](#API_GetCostEstimation_ResponseSyntax) **   <a name="DevOpsGuru-GetCostEstimation-response-TotalCost"></a>
The estimated monthly cost to analyze the AWS resources. This value is the sum of the estimated costs to analyze each resource in the `Costs` object in this response.
Type: Double

## Errors
<a name="API_GetCostEstimation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource could not be found
 ** ResourceId **
 The ID of the AWS resource that could not be found.
 ** ResourceType **
 The type of the AWS resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_GetCostEstimation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/GetCostEstimation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/GetCostEstimation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/GetCostEstimation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/GetCostEstimation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/GetCostEstimation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/GetCostEstimation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/GetCostEstimation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/GetCostEstimation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/GetCostEstimation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/GetCostEstimation)
