---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetInstrumentationConfigurationStatus.html
---

# GetInstrumentationConfigurationStatus
<a name="API_GetInstrumentationConfigurationStatus"></a>

Retrieves the status history for a single instrumentation configuration during a specified time range. The response lists when the configuration was ACTIVE, READY, ERROR, or DISABLED.

If no status or time window is provided, the operation defaults to ACTIVE events from the last hour.

## Request Syntax
<a name="API_GetInstrumentationConfigurationStatus_RequestSyntax"></a>

```
POST /get-instrumentation-configuration-status HTTP/1.1
Content-type: application/json

{
   "EndTime": {{number}},
   "Environment": "{{string}}",
   "InstrumentationType": "{{string}}",
   "LocationIdentifier": { ... },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Service": "{{string}}",
   "SignalType": "{{string}}",
   "StartTime": {{number}},
   "Status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetInstrumentationConfigurationStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetInstrumentationConfigurationStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-request-EndTime"></a>
The end of the time range to retrieve status events for. `StartTime` and `EndTime` must both be provided together or both be omitted. When both are omitted, the time range defaults to the last hour.
Type: Timestamp
Required: No

 ** [Environment](#API_GetInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-request-Environment"></a>
The environment name for the instrumentation configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [InstrumentationType](#API_GetInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-request-InstrumentationType"></a>
The type of instrumentation configuration (`BREAKPOINT` or `PROBE`). Required to identify the configuration to retrieve.
Type: String
Valid Values: `BREAKPOINT | PROBE`
Required: Yes

 ** [LocationIdentifier](#API_GetInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-request-LocationIdentifier"></a>
The location identifier - either the full code location or a pre-computed location hash.
Type: [LocationIdentifier](API_LocationIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [MaxResults](#API_GetInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-request-MaxResults"></a>
The maximum number of status events to return in one call. The default is 60.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-request-NextToken"></a>
Use the token returned by a previous call to retrieve the next page of status events.
Type: String
Required: No

 ** [Service](#API_GetInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-request-Service"></a>
The service name for the instrumentation configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [SignalType](#API_GetInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-request-SignalType"></a>
The telemetry signal type for instrumentation.
+  `SNAPSHOT` - Captures a snapshot of the instrumentation point.
Type: String
Valid Values: `SNAPSHOT`
Required: Yes

 ** [StartTime](#API_GetInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-request-StartTime"></a>
The start of the time range to retrieve status events for. `StartTime` and `EndTime` must both be provided together or both be omitted. When both are omitted, the time range defaults to the last hour.
Type: Timestamp
Required: No

 ** [Status](#API_GetInstrumentationConfigurationStatus_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-request-Status"></a>
The single status to query for. If omitted, only `ACTIVE` status events are returned.
Type: String
Valid Values: `READY | ERROR | ACTIVE | DISABLED`
Required: No

## Response Syntax
<a name="API_GetInstrumentationConfigurationStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Environment": "string",
   "Events": [
      {
         "ErrorCause": "string",
         "Time": number
      }
   ],
   "Location": { ... },
   "NextToken": "string",
   "Service": "string",
   "SignalType": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_GetInstrumentationConfigurationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Environment](#API_GetInstrumentationConfigurationStatus_ResponseSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-response-Environment"></a>
The environment echoed from the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Events](#API_GetInstrumentationConfigurationStatus_ResponseSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-response-Events"></a>
The list of status events within the requested time window, sorted with the most recent first. Error events include an error cause.
Type: Array of [InstrumentationStatusEvent](API_InstrumentationStatusEvent.md) objects

 ** [Location](#API_GetInstrumentationConfigurationStatus_ResponseSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-response-Location"></a>
The code location echoed from the request.
Type: [Location](API_Location.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [NextToken](#API_GetInstrumentationConfigurationStatus_ResponseSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-response-NextToken"></a>
Pagination token to continue retrieving status events.
Type: String

 ** [Service](#API_GetInstrumentationConfigurationStatus_ResponseSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-response-Service"></a>
The service name echoed from the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [SignalType](#API_GetInstrumentationConfigurationStatus_ResponseSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-response-SignalType"></a>
The telemetry signal type echoed from the request.
Type: String
Valid Values: `SNAPSHOT`

 ** [Status](#API_GetInstrumentationConfigurationStatus_ResponseSyntax) **   <a name="applicationsignals-GetInstrumentationConfigurationStatus-response-Status"></a>
The status that was queried. If not specified in the request, this is `ACTIVE`.
Type: String
Valid Values: `READY | ERROR | ACTIVE | DISABLED`

## Errors
<a name="API_GetInstrumentationConfigurationStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found.
 ** ResourceId **
Can't find the resource id.
 ** ResourceType **
The resource type is not valid.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetInstrumentationConfigurationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/GetInstrumentationConfigurationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/GetInstrumentationConfigurationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/GetInstrumentationConfigurationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/GetInstrumentationConfigurationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/GetInstrumentationConfigurationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/GetInstrumentationConfigurationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/GetInstrumentationConfigurationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/GetInstrumentationConfigurationStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/GetInstrumentationConfigurationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/GetInstrumentationConfigurationStatus)
