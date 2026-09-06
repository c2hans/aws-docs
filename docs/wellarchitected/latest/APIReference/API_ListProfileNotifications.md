---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfileNotifications.html
---

# ListProfileNotifications
<a name="API_ListProfileNotifications"></a>

List profile notifications.

## Request Syntax
<a name="API_ListProfileNotifications_RequestSyntax"></a>

```
GET /profileNotifications/?MaxResults={{MaxResults}}&NextToken={{NextToken}}&WorkloadId={{WorkloadId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProfileNotifications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListProfileNotifications_RequestSyntax) **   <a name="wellarchitected-ListProfileNotifications-request-uri-MaxResults"></a>
The maximum number of results to return for this request.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListProfileNotifications_RequestSyntax) **   <a name="wellarchitected-ListProfileNotifications-request-uri-NextToken"></a>
The token to use to retrieve the next set of results.

 ** [WorkloadId](#API_ListProfileNotifications_RequestSyntax) **   <a name="wellarchitected-ListProfileNotifications-request-uri-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`

## Request Body
<a name="API_ListProfileNotifications_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProfileNotifications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "NotificationSummaries": [
      {
         "CurrentProfileVersion": "string",
         "LatestProfileVersion": "string",
         "ProfileArn": "string",
         "ProfileName": "string",
         "Type": "string",
         "WorkloadId": "string",
         "WorkloadName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProfileNotifications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListProfileNotifications_ResponseSyntax) **   <a name="wellarchitected-ListProfileNotifications-response-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String

 ** [NotificationSummaries](#API_ListProfileNotifications_ResponseSyntax) **   <a name="wellarchitected-ListProfileNotifications-response-NotificationSummaries"></a>
Notification summaries.
Type: Array of [ProfileNotificationSummary](API_ProfileNotificationSummary.md) objects

## Errors
<a name="API_ListProfileNotifications_Errors"></a>

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
<a name="API_ListProfileNotifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListProfileNotifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListProfileNotifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListProfileNotifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListProfileNotifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListProfileNotifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListProfileNotifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListProfileNotifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListProfileNotifications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListProfileNotifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListProfileNotifications)
