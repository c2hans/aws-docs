---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListNotifications.html
---

# ListNotifications
<a name="API_ListNotifications"></a>

List lens notifications.

## Request Syntax
<a name="API_ListNotifications_RequestSyntax"></a>

```
POST /notifications HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceArn": "{{string}}",
   "WorkloadId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListNotifications_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListNotifications_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListNotifications_RequestSyntax) **   <a name="wellarchitected-ListNotifications-request-MaxResults"></a>
The maximum number of results to return for this request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListNotifications_RequestSyntax) **   <a name="wellarchitected-ListNotifications-request-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String
Required: No

 ** [ResourceArn](#API_ListNotifications_RequestSyntax) **   <a name="wellarchitected-ListNotifications-request-ResourceArn"></a>
The ARN for the related resource for the notification.
Only one of `WorkloadID` or `ResourceARN` should be specified.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: No

 ** [WorkloadId](#API_ListNotifications_RequestSyntax) **   <a name="wellarchitected-ListNotifications-request-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

## Response Syntax
<a name="API_ListNotifications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "NotificationSummaries": [
      {
         "LensUpgradeSummary": {
            "CurrentLensVersion": "string",
            "LatestLensVersion": "string",
            "LensAlias": "string",
            "LensArn": "string",
            "ResourceArn": "string",
            "ResourceName": "string",
            "WorkloadId": "string",
            "WorkloadName": "string"
         },
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNotifications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListNotifications_ResponseSyntax) **   <a name="wellarchitected-ListNotifications-response-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String

 ** [NotificationSummaries](#API_ListNotifications_ResponseSyntax) **   <a name="wellarchitected-ListNotifications-response-NotificationSummaries"></a>
List of lens notification summaries in a workload.
Type: Array of [NotificationSummary](API_NotificationSummary.md) objects

## Errors
<a name="API_ListNotifications_Errors"></a>

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
<a name="API_ListNotifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListNotifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListNotifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListNotifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListNotifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListNotifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListNotifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListNotifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListNotifications)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListNotifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListNotifications)
