---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListInstrumentationConfigurations.html
---

# ListInstrumentationConfigurations
<a name="API_ListInstrumentationConfigurations"></a>

Returns all active instrumentation configurations for a service and environment. SDKs use this operation to sync configurations and apply client-side filters locally.

Include the previous `SyncedAt` value to perform incremental syncs. When no changes are detected, the response sets `Changed` to `false` and omits configuration details.

## Request Syntax
<a name="API_ListInstrumentationConfigurations_RequestSyntax"></a>

```
POST /list-instrumentation-configurations HTTP/1.1
Content-type: application/json

{
   "Environment": "{{string}}",
   "InstrumentationType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Service": "{{string}}",
   "SyncedAt": {{number}}
}
```

## URI Request Parameters
<a name="API_ListInstrumentationConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListInstrumentationConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Environment](#API_ListInstrumentationConfigurations_RequestSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-request-Environment"></a>
The environment that the service is running in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9:/+=,.@_-]+`
Required: Yes

 ** [InstrumentationType](#API_ListInstrumentationConfigurations_RequestSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-request-InstrumentationType"></a>
The type of instrumentation configuration (`BREAKPOINT` or `PROBE`). Required to determine which backing store to query.
Type: String
Valid Values: `BREAKPOINT | PROBE`
Required: Yes

 ** [MaxResults](#API_ListInstrumentationConfigurations_RequestSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-request-MaxResults"></a>
The maximum number of configurations to return in one call. The default is 50 and the maximum is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListInstrumentationConfigurations_RequestSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-request-NextToken"></a>
Use the token returned by a previous call to retrieve the next page of configurations.
Type: String
Required: No

 ** [Service](#API_ListInstrumentationConfigurations_RequestSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-request-Service"></a>
The name of the service to retrieve instrumentation configurations for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9:/+=,.@_-]+`
Required: Yes

 ** [SyncedAt](#API_ListInstrumentationConfigurations_RequestSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-request-SyncedAt"></a>
The timestamp from the last successful sync. When provided, the response returns `Changed` as `false` if nothing is new since this time, or returns the latest configurations when changes exist.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_ListInstrumentationConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Changed": boolean,
   "Environment": "string",
   "LatestConfigurations": [
      {
         "ARN": "string",
         "AttributeFilters": [
            {
               "string" : "string"
            }
         ],
         "CaptureConfiguration": { ... },
         "CreatedAt": number,
         "Description": "string",
         "ExpiresAt": number,
         "InstrumentationType": "string",
         "Location": { ... },
         "LocationHash": "string",
         "SignalType": "string"
      }
   ],
   "NextToken": "string",
   "Service": "string",
   "SyncedAt": number,
   "SyncInterval": number
}
```

## Response Elements
<a name="API_ListInstrumentationConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Changed](#API_ListInstrumentationConfigurations_ResponseSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-response-Changed"></a>
Indicates whether there are configuration changes since the provided `SyncedAt` timestamp.
Type: Boolean

 ** [Environment](#API_ListInstrumentationConfigurations_ResponseSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-response-Environment"></a>
The environment associated with the returned configurations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [LatestConfigurations](#API_ListInstrumentationConfigurations_ResponseSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-response-LatestConfigurations"></a>
The current set of active instrumentation configurations for the service and environment. Items omit service and environment because they are provided in the request.
Type: Array of [InstrumentationConfigurationWithoutServiceEnv](API_InstrumentationConfigurationWithoutServiceEnv.md) objects

 ** [NextToken](#API_ListInstrumentationConfigurations_ResponseSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-response-NextToken"></a>
Pagination token to continue listing configurations when more results are available.
Type: String

 ** [Service](#API_ListInstrumentationConfigurations_ResponseSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-response-Service"></a>
The service name associated with the returned configurations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [SyncedAt](#API_ListInstrumentationConfigurations_ResponseSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-response-SyncedAt"></a>
The server timestamp to supply on the next sync call.
Type: Timestamp

 ** [SyncInterval](#API_ListInstrumentationConfigurations_ResponseSyntax) **   <a name="applicationsignals-ListInstrumentationConfigurations-response-SyncInterval"></a>
The suggested number of seconds to wait before the next sync request. This is at least 60 seconds to prevent excessive polling.
Type: Integer
Valid Range: Minimum value of 60.

## Errors
<a name="API_ListInstrumentationConfigurations_Errors"></a>

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
<a name="API_ListInstrumentationConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/ListInstrumentationConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/ListInstrumentationConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ListInstrumentationConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/ListInstrumentationConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ListInstrumentationConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/ListInstrumentationConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/ListInstrumentationConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/ListInstrumentationConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/ListInstrumentationConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ListInstrumentationConfigurations)
