---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListCheckSummaries.html
---

# ListCheckSummaries
<a name="API_ListCheckSummaries"></a>

List of Trusted Advisor checks summarized for all accounts related to the workload.

## Request Syntax
<a name="API_ListCheckSummaries_RequestSyntax"></a>

```
POST /workloads/{{WorkloadId}}/checkSummaries HTTP/1.1
Content-type: application/json

{
   "ChoiceId": "{{string}}",
   "LensArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PillarId": "{{string}}",
   "QuestionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCheckSummaries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [WorkloadId](#API_ListCheckSummaries_RequestSyntax) **   <a name="wellarchitected-ListCheckSummaries-request-uri-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_ListCheckSummaries_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChoiceId](#API_ListCheckSummaries_RequestSyntax) **   <a name="wellarchitected-ListCheckSummaries-request-ChoiceId"></a>
The ID of a choice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [LensArn](#API_ListCheckSummaries_RequestSyntax) **   <a name="wellarchitected-ListCheckSummaries-request-LensArn"></a>
Well-Architected Lens ARN.
Type: String
Required: Yes

 ** [MaxResults](#API_ListCheckSummaries_RequestSyntax) **   <a name="wellarchitected-ListCheckSummaries-request-MaxResults"></a>
The maximum number of results to return for this request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListCheckSummaries_RequestSyntax) **   <a name="wellarchitected-ListCheckSummaries-request-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String
Pattern: `[A-Za-z0-9+\/=_-]+`
Required: No

 ** [PillarId](#API_ListCheckSummaries_RequestSyntax) **   <a name="wellarchitected-ListCheckSummaries-request-PillarId"></a>
The ID used to identify a pillar, for example, `security`.
A pillar is identified by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [QuestionId](#API_ListCheckSummaries_RequestSyntax) **   <a name="wellarchitected-ListCheckSummaries-request-QuestionId"></a>
The ID of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Syntax
<a name="API_ListCheckSummaries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CheckSummaries": [
      {
         "AccountSummary": {
            "string" : number
         },
         "ChoiceId": "string",
         "Description": "string",
         "Id": "string",
         "LensArn": "string",
         "Name": "string",
         "PillarId": "string",
         "Provider": "string",
         "QuestionId": "string",
         "Status": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCheckSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CheckSummaries](#API_ListCheckSummaries_ResponseSyntax) **   <a name="wellarchitected-ListCheckSummaries-response-CheckSummaries"></a>
List of Trusted Advisor summaries related to the Well-Architected best practice.
Type: Array of [CheckSummary](API_CheckSummary.md) objects

 ** [NextToken](#API_ListCheckSummaries_ResponseSyntax) **   <a name="wellarchitected-ListCheckSummaries-response-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String
Pattern: `[A-Za-z0-9+\/=_-]+`

## Errors
<a name="API_ListCheckSummaries_Errors"></a>

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

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

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
<a name="API_ListCheckSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListCheckSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListCheckSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListCheckSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListCheckSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListCheckSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListCheckSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListCheckSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListCheckSummaries)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListCheckSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListCheckSummaries)
