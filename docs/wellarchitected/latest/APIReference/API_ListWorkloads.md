---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListWorkloads.html
---

# ListWorkloads
<a name="API_ListWorkloads"></a>

Paginated list of workloads.

## Request Syntax
<a name="API_ListWorkloads_RequestSyntax"></a>

```
POST /workloadsSummaries HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "WorkloadNamePrefix": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWorkloads_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWorkloads_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListWorkloads_RequestSyntax) **   <a name="wellarchitected-ListWorkloads-request-MaxResults"></a>
The maximum number of results to return for this request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListWorkloads_RequestSyntax) **   <a name="wellarchitected-ListWorkloads-request-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String
Required: No

 ** [WorkloadNamePrefix](#API_ListWorkloads_RequestSyntax) **   <a name="wellarchitected-ListWorkloads-request-WorkloadNamePrefix"></a>
An optional string added to the beginning of each workload name returned in the results.
Type: String
Length Constraints: Maximum length of 100.
Required: No

## Response Syntax
<a name="API_ListWorkloads_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "WorkloadSummaries": [
      {
         "ImprovementStatus": "string",
         "Lenses": [ "string" ],
         "Owner": "string",
         "PrioritizedRiskCounts": {
            "string" : number
         },
         "Profiles": [
            {
               "ProfileArn": "string",
               "ProfileVersion": "string"
            }
         ],
         "RiskCounts": {
            "string" : number
         },
         "UpdatedAt": number,
         "WorkloadArn": "string",
         "WorkloadId": "string",
         "WorkloadName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkloads_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListWorkloads_ResponseSyntax) **   <a name="wellarchitected-ListWorkloads-response-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String

 ** [WorkloadSummaries](#API_ListWorkloads_ResponseSyntax) **   <a name="wellarchitected-ListWorkloads-response-WorkloadSummaries"></a>
A list of workload summaries.
Type: Array of [WorkloadSummary](API_WorkloadSummary.md) objects

## Errors
<a name="API_ListWorkloads_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListWorkloads_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListWorkloads)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListWorkloads)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListWorkloads)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListWorkloads)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListWorkloads)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListWorkloads)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListWorkloads)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListWorkloads)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListWorkloads)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListWorkloads)
