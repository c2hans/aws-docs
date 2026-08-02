---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_EventLogEntry.html
---

# EventLogEntry
<a name="API_EventLogEntry"></a>

Information about an entry in an event log of Amazon CodeCatalyst activity.

## Contents
<a name="API_EventLogEntry_Contents"></a>

 ** eventCategory **   <a name="codecatalyst-Type-EventLogEntry-eventCategory"></a>
The category for the event.
Type: String
Required: Yes

 ** eventName **   <a name="codecatalyst-Type-EventLogEntry-eventName"></a>
The name of the event.
Type: String
Required: Yes

 ** eventSource **   <a name="codecatalyst-Type-EventLogEntry-eventSource"></a>
The source of the event.
Type: String
Required: Yes

 ** eventTime **   <a name="codecatalyst-Type-EventLogEntry-eventTime"></a>
The time the event took place, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp
Required: Yes

 ** eventType **   <a name="codecatalyst-Type-EventLogEntry-eventType"></a>
The type of the event.
Type: String
Required: Yes

 ** id **   <a name="codecatalyst-Type-EventLogEntry-id"></a>
The system-generated unique ID of the event.
Type: String
Required: Yes

 ** operationType **   <a name="codecatalyst-Type-EventLogEntry-operationType"></a>
The type of the event.
Type: String
Valid Values: `READONLY | MUTATION`
Required: Yes

 ** userIdentity **   <a name="codecatalyst-Type-EventLogEntry-userIdentity"></a>
The system-generated unique ID of the user whose actions are recorded in the event.
Type: [UserIdentity](API_UserIdentity.md) object
Required: Yes

 ** errorCode **   <a name="codecatalyst-Type-EventLogEntry-errorCode"></a>
The code of the error, if any.
Type: String
Required: No

 ** projectInformation **   <a name="codecatalyst-Type-EventLogEntry-projectInformation"></a>
Information about the project where the event occurred.
Type: [ProjectInformation](API_ProjectInformation.md) object
Required: No

 ** requestId **   <a name="codecatalyst-Type-EventLogEntry-requestId"></a>
The system-generated unique ID of the request.
Type: String
Required: No

 ** requestPayload **   <a name="codecatalyst-Type-EventLogEntry-requestPayload"></a>
Information about the payload of the request.
Type: [EventPayload](API_EventPayload.md) object
Required: No

 ** responsePayload **   <a name="codecatalyst-Type-EventLogEntry-responsePayload"></a>
Information about the payload of the response, if any.
Type: [EventPayload](API_EventPayload.md) object
Required: No

 ** sourceIpAddress **   <a name="codecatalyst-Type-EventLogEntry-sourceIpAddress"></a>
The IP address of the user whose actions are recorded in the event.
Type: String
Required: No

 ** userAgent **   <a name="codecatalyst-Type-EventLogEntry-userAgent"></a>
The user agent whose actions are recorded in the event.
Type: String
Required: No

## See Also
<a name="API_EventLogEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/EventLogEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/EventLogEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/EventLogEntry)
