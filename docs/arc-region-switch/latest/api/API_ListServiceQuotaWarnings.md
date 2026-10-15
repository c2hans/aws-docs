---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListServiceQuotaWarnings.html
---

# ListServiceQuotaWarnings
<a name="API_ListServiceQuotaWarnings"></a>

Lists the service quota warnings for the plans that you can access. Region switch creates a warning when the applied quota value in one Region of a plan is lower than the value required for the matching resource in another Region or account in the plan.

Returns the warnings for the plans that you own and for plans that are shared with your account through AWS Resource Access Manager (AWS RAM). To return warnings for specific plans, provide a list of plan Amazon Resource Names (ARNs). Region switch ignores any plan ARN that you can't access. If you don't provide any plan ARNs, Region switch returns the warnings for all of your accessible plans.

## Request Syntax
<a name="API_ListServiceQuotaWarnings_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "planArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListServiceQuotaWarnings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListServiceQuotaWarnings_RequestSyntax) **   <a name="regionswitch-ListServiceQuotaWarnings-request-maxResults"></a>
The maximum number of results to return with this call. Valid values are `1` to `100`. If you don't specify a value, the operation returns up to the maximum number of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListServiceQuotaWarnings_RequestSyntax) **   <a name="regionswitch-ListServiceQuotaWarnings-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [planArns](#API_ListServiceQuotaWarnings_RequestSyntax) **   <a name="regionswitch-ListServiceQuotaWarnings-request-planArns"></a>
The Amazon Resource Names (ARNs) of the plans to return service quota warnings for. You can specify up to 100 plan ARNs. Region switch ignores any plan ARN that you can't access. If you omit this parameter, Region switch returns the warnings for all of your accessible plans.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: No

## Response Syntax
<a name="API_ListServiceQuotaWarnings_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "serviceQuotaWarningSummaries": [
      {
         "accountId": "string",
         "caseId": "string",
         "lastCheckedAt": number,
         "planArn": "string",
         "quotaCode": "string",
         "quotaName": "string",
         "quotaRegion": "string",
         "requestId": "string",
         "serviceCode": "string",
         "status": "string",
         "warningCreatedAt": number,
         "warningMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListServiceQuotaWarnings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListServiceQuotaWarnings_ResponseSyntax) **   <a name="regionswitch-ListServiceQuotaWarnings-response-nextToken"></a>
A pagination token. A response may contain no results while still including a `nextToken`. Continue paginating until `nextToken` is null to retrieve all results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [serviceQuotaWarningSummaries](#API_ListServiceQuotaWarnings_ResponseSyntax) **   <a name="regionswitch-ListServiceQuotaWarnings-response-serviceQuotaWarningSummaries"></a>
The service quota warnings for the plans that you can access.
Type: Array of [ServiceQuotaWarningSummary](API_ServiceQuotaWarningSummary.md) objects

## Errors
<a name="API_ListServiceQuotaWarnings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500
HTTP Status Code: 500

## See Also
<a name="API_ListServiceQuotaWarnings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/ListServiceQuotaWarnings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/ListServiceQuotaWarnings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ListServiceQuotaWarnings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/ListServiceQuotaWarnings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ListServiceQuotaWarnings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/ListServiceQuotaWarnings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/ListServiceQuotaWarnings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/ListServiceQuotaWarnings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/ListServiceQuotaWarnings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ListServiceQuotaWarnings)
