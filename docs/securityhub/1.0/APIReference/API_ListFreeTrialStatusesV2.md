---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListFreeTrialStatusesV2.html
---

# ListFreeTrialStatusesV2
<a name="API_ListFreeTrialStatusesV2"></a>

Lists the free trial status of Security Hub features. A delegated Security Hub administrator can list the status for accounts in its organization. Any other account can list the status only for itself. Free trial status remains available after a feature is disabled.

## Request Syntax
<a name="API_ListFreeTrialStatusesV2_RequestSyntax"></a>

```
POST /freetrial/statusv2/list HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Statuses": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListFreeTrialStatusesV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListFreeTrialStatusesV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_ListFreeTrialStatusesV2_RequestSyntax) **   <a name="securityhub-ListFreeTrialStatusesV2-request-AccountIds"></a>
The AWS account identifiers to list free trial status for. You can specify accounts other than your own only if you are a delegated Security Hub administrator.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `^[0-9]{12}$`
Required: No

 ** [MaxResults](#API_ListFreeTrialStatusesV2_RequestSyntax) **   <a name="securityhub-ListFreeTrialStatusesV2-request-MaxResults"></a>
The maximum number of results to return. If you don't specify a value, Security Hub returns up to 100 results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListFreeTrialStatusesV2_RequestSyntax) **   <a name="securityhub-ListFreeTrialStatusesV2-request-NextToken"></a>
The pagination token to request the next page of results.
Type: String
Required: No

 ** [Statuses](#API_ListFreeTrialStatusesV2_RequestSyntax) **   <a name="securityhub-ListFreeTrialStatusesV2-request-Statuses"></a>
The free trial statuses to filter the results by. Valid values:
+  `ACTIVE` returns only features with an ongoing free trial period.
+  `INACTIVE` returns only features whose free trial period has ended, or that never started.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `ACTIVE | INACTIVE`
Required: No

## Response Syntax
<a name="API_ListFreeTrialStatusesV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountFreeTrialStatuses": [
      {
         "AccountId": "string",
         "EvaluatedAt": "string",
         "FreeTrialStatuses": [
            {
               "ExpiresAt": "string",
               "FeatureType": "string",
               "StartedAt": "string",
               "Status": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFreeTrialStatusesV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountFreeTrialStatuses](#API_ListFreeTrialStatusesV2_ResponseSyntax) **   <a name="securityhub-ListFreeTrialStatusesV2-response-AccountFreeTrialStatuses"></a>
An array of free trial statuses, one for each account in scope.
Type: Array of  objects
Array Members: Maximum number of 100 items.

 ** [NextToken](#API_ListFreeTrialStatusesV2_ResponseSyntax) **   <a name="securityhub-ListFreeTrialStatusesV2-response-NextToken"></a>
The pagination token to use to request the next page of results. If there are no additional results, this value is null.
Type: String

## Errors
<a name="API_ListFreeTrialStatusesV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_ListFreeTrialStatusesV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListFreeTrialStatusesV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListFreeTrialStatusesV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListFreeTrialStatusesV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListFreeTrialStatusesV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListFreeTrialStatusesV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListFreeTrialStatusesV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListFreeTrialStatusesV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListFreeTrialStatusesV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListFreeTrialStatusesV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListFreeTrialStatusesV2)
