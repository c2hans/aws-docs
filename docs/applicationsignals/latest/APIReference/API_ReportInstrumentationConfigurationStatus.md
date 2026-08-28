---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ReportInstrumentationConfigurationStatus.html
---

# ReportInstrumentationConfigurationStatus
<a name="API_ReportInstrumentationConfigurationStatus"></a>

Reports the status of one or more instrumentation configurations from SDK instances. Use this to record when configurations become ready, hit errors, become active, or are disabled by limits.

Report `READY`, `ERROR`, and `DISABLED` when the status changes. Report `ACTIVE` periodically (for example, every minute) while instrumentation is running.

## Request Syntax
<a name="API_ReportInstrumentationConfigurationStatus_RequestSyntax"></a>

```
POST /report-instrumentation-configuration-status HTTP/1.1
Content-type: application/json

{
   "Configurations": [
      {
         "ErrorCause": "{{string}}",
         "InstrumentationType": "{{string}}",
         "LocationHash": "{{string}}",
         "SignalType": "{{string}}",
         "Status": "{{string}}",
         "Time": {{number}}
      }
   ],
   "Environment": "{{string}}",
   "Service": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ReportInstrumentationConfigurationStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ReportInstrumentationConfigurationStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Configurations](#API_ReportInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-ReportInstrumentationConfigurationStatus-request-Configurations"></a>
An array of configuration status reports (up to 100) that include the instrumentation type, signal type, location hash, status, timestamp, and optional error cause.
Type: Array of [InstrumentationConfigurationStatusReport](API_InstrumentationConfigurationStatusReport.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [Environment](#API_ReportInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-ReportInstrumentationConfigurationStatus-request-Environment"></a>
The environment that the service is running in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Service](#API_ReportInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-ReportInstrumentationConfigurationStatus-request-Service"></a>
The service that the reported configurations belong to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_ReportInstrumentationConfigurationStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Environment": "string",
   "Service": "string",
   "UnprocessedStatusEvents": [
      {
         "FailedReason": "string",
         "InstrumentationType": "string",
         "LocationHash": "string",
         "SignalType": "string",
         "Status": "string",
         "Time": number
      }
   ]
}
```

## Response Elements
<a name="API_ReportInstrumentationConfigurationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Environment](#API_ReportInstrumentationConfigurationStatus_ResponseSyntax) **   <a name="applicationsignals-ReportInstrumentationConfigurationStatus-response-Environment"></a>
The environment echoed from the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Service](#API_ReportInstrumentationConfigurationStatus_ResponseSyntax) **   <a name="applicationsignals-ReportInstrumentationConfigurationStatus-response-Service"></a>
The service name echoed from the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [UnprocessedStatusEvents](#API_ReportInstrumentationConfigurationStatus_ResponseSyntax) **   <a name="applicationsignals-ReportInstrumentationConfigurationStatus-response-UnprocessedStatusEvents"></a>
Status events that failed to be processed. Each entry includes the configuration identifiers, status, timestamp, and a reason for the failure.
Type: Array of [UnprocessedStatusEvent](API_UnprocessedStatusEvent.md) objects

## Errors
<a name="API_ReportInstrumentationConfigurationStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ReportInstrumentationConfigurationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/ReportInstrumentationConfigurationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/ReportInstrumentationConfigurationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ReportInstrumentationConfigurationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/ReportInstrumentationConfigurationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ReportInstrumentationConfigurationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/ReportInstrumentationConfigurationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/ReportInstrumentationConfigurationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/ReportInstrumentationConfigurationStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/ReportInstrumentationConfigurationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ReportInstrumentationConfigurationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
