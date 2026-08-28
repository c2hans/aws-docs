---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetMinuteUsage.html
---

# GetMinuteUsage
<a name="API_GetMinuteUsage"></a>

Returns the number of reserved minutes used by account.

## Request Syntax
<a name="API_GetMinuteUsage_RequestSyntax"></a>

```
POST /minute-usage HTTP/1.1
Content-type: application/json

{
   "month": {{number}},
   "year": {{number}}
}
```

## URI Request Parameters
<a name="API_GetMinuteUsage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetMinuteUsage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [month](#API_GetMinuteUsage_RequestSyntax) **   <a name="groundstation-GetMinuteUsage-request-month"></a>
The month being requested, with a value of 1-12.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 12.
Required: Yes

 ** [year](#API_GetMinuteUsage_RequestSyntax) **   <a name="groundstation-GetMinuteUsage-request-year"></a>
The year being requested, in the format of YYYY.
Type: Integer
Valid Range: Minimum value of 2018. Maximum value of 3000.
Required: Yes

## Response Syntax
<a name="API_GetMinuteUsage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "estimatedMinutesRemaining": number,
   "isReservedMinutesCustomer": boolean,
   "totalReservedMinuteAllocation": number,
   "totalScheduledMinutes": number,
   "upcomingMinutesScheduled": number
}
```

## Response Elements
<a name="API_GetMinuteUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [estimatedMinutesRemaining](#API_GetMinuteUsage_ResponseSyntax) **   <a name="groundstation-GetMinuteUsage-response-estimatedMinutesRemaining"></a>
Estimated number of minutes remaining for an account, specific to the month being requested.
Type: Integer

 ** [isReservedMinutesCustomer](#API_GetMinuteUsage_ResponseSyntax) **   <a name="groundstation-GetMinuteUsage-response-isReservedMinutesCustomer"></a>
Returns whether or not an account has signed up for the reserved minutes pricing plan, specific to the month being requested.
Type: Boolean

 ** [totalReservedMinuteAllocation](#API_GetMinuteUsage_ResponseSyntax) **   <a name="groundstation-GetMinuteUsage-response-totalReservedMinuteAllocation"></a>
Total number of reserved minutes allocated, specific to the month being requested.
Type: Integer

 ** [totalScheduledMinutes](#API_GetMinuteUsage_ResponseSyntax) **   <a name="groundstation-GetMinuteUsage-response-totalScheduledMinutes"></a>
Total scheduled minutes for an account, specific to the month being requested.
Type: Integer

 ** [upcomingMinutesScheduled](#API_GetMinuteUsage_ResponseSyntax) **   <a name="groundstation-GetMinuteUsage-response-upcomingMinutesScheduled"></a>
Upcoming minutes scheduled for an account, specific to the month being requested.
Type: Integer

## Errors
<a name="API_GetMinuteUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_GetMinuteUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/GetMinuteUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/GetMinuteUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/GetMinuteUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/GetMinuteUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/GetMinuteUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/GetMinuteUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/GetMinuteUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/GetMinuteUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/GetMinuteUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/GetMinuteUsage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
