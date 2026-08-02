---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingHistory.html
---

# GetFindingHistory
<a name="API_GetFindingHistory"></a>

 Returns the history of a Security Hub CSPM finding. The history includes changes made to any fields in the AWS Security Finding Format (ASFF) except top-level timestamp fields, such as the `CreatedAt` and `UpdatedAt` fields.

This operation might return fewer results than the maximum number of results (`MaxResults`) specified in a request, even when more results are available. If this occurs, the response includes a `NextToken` value, which you should use to retrieve the next set of results in the response. The presence of a `NextToken` value in a response doesn't necessarily indicate that the results are incomplete. However, you should continue to specify a `NextToken` value until you receive a response that doesn't include this value.

## Request Syntax
<a name="API_GetFindingHistory_RequestSyntax"></a>

```
POST /findingHistory/get HTTP/1.1
Content-type: application/json

{
   "EndTime": "{{string}}",
   "FindingIdentifier": {
      "Id": "{{string}}",
      "ProductArn": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StartTime": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetFindingHistory_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetFindingHistory_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetFindingHistory_RequestSyntax) **   <a name="securityhub-GetFindingHistory-request-EndTime"></a>
 An ISO 8601-formatted timestamp that indicates the end time of the requested finding history.
If you provide values for both `StartTime` and `EndTime`, Security Hub CSPM returns finding history for the specified time period. If you provide a value for `StartTime` but not for `EndTime`, Security Hub CSPM returns finding history from the `StartTime` to the time at which the API is called. If you provide a value for `EndTime` but not for `StartTime`, Security Hub CSPM returns finding history from the [CreatedAt](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html#securityhub-Type-AwsSecurityFindingFilters-CreatedAt) timestamp of the finding to the `EndTime`. If you provide neither `StartTime` nor `EndTime`, Security Hub CSPM returns finding history from the `CreatedAt` timestamp of the finding to the time at which the API is called. In all of these scenarios, the response is limited to 100 results.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp
Required: No

 ** [FindingIdentifier](#API_GetFindingHistory_RequestSyntax) **   <a name="securityhub-GetFindingHistory-request-FindingIdentifier"></a>
Identifies which finding to get the finding history for.
Type: [AwsSecurityFindingIdentifier](API_AwsSecurityFindingIdentifier.md) object
Required: Yes

 ** [MaxResults](#API_GetFindingHistory_RequestSyntax) **   <a name="securityhub-GetFindingHistory-request-MaxResults"></a>
 The maximum number of results to be returned. If you don’t provide it, Security Hub CSPM returns up to 100 results of finding history.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetFindingHistory_RequestSyntax) **   <a name="securityhub-GetFindingHistory-request-NextToken"></a>
 A token for pagination purposes. Provide `NULL` as the initial value. In subsequent requests, provide the token included in the response to get up to an additional 100 results of finding history. If you don’t provide `NextToken`, Security Hub CSPM returns up to 100 results of finding history for each request.
Type: String
Required: No

 ** [StartTime](#API_GetFindingHistory_RequestSyntax) **   <a name="securityhub-GetFindingHistory-request-StartTime"></a>
A timestamp that indicates the start time of the requested finding history.
If you provide values for both `StartTime` and `EndTime`, AWS Security Hub CSPM returns finding history for the specified time period. If you provide a value for `StartTime` but not for `EndTime`, Security Hub CSPM returns finding history from the `StartTime` to the time at which the API is called. If you provide a value for `EndTime` but not for `StartTime`, Security Hub CSPM returns finding history from the [CreatedAt](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html#securityhub-Type-AwsSecurityFindingFilters-CreatedAt) timestamp of the finding to the `EndTime`. If you provide neither `StartTime` nor `EndTime`, Security Hub CSPM returns finding history from the `CreatedAt` timestamp of the finding to the time at which the API is called. In all of these scenarios, the response is limited to 100 results.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp
Required: No

## Response Syntax
<a name="API_GetFindingHistory_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Records": [
      {
         "FindingCreated": boolean,
         "FindingIdentifier": {
            "Id": "string",
            "ProductArn": "string"
         },
         "NextToken": "string",
         "Updates": [
            {
               "NewValue": "string",
               "OldValue": "string",
               "UpdatedField": "string"
            }
         ],
         "UpdateSource": {
            "Identity": "string",
            "Type": "string"
         },
         "UpdateTime": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetFindingHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetFindingHistory_ResponseSyntax) **   <a name="securityhub-GetFindingHistory-response-NextToken"></a>
 A token for pagination purposes. Provide this token in the subsequent request to `GetFindingsHistory` to get up to an additional 100 results of history for the same finding that you specified in your initial request.
Type: String

 ** [Records](#API_GetFindingHistory_ResponseSyntax) **   <a name="securityhub-GetFindingHistory-response-Records"></a>
 A list of events that altered the specified finding during the specified time period.
Type: Array of [FindingHistoryRecord](API_FindingHistoryRecord.md) objects

## Errors
<a name="API_GetFindingHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_GetFindingHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetFindingHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetFindingHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetFindingHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetFindingHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetFindingHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetFindingHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetFindingHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetFindingHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetFindingHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetFindingHistory)
