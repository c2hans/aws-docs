---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_Span.html
---

# Span
<a name="API_amazon-q-connect_Span"></a>

A span represents a unit of work during AI agent execution, capturing timing, status, and contextual attributes.

## Contents
<a name="API_amazon-q-connect_Span_Contents"></a>

 ** assistantId **   <a name="connect-Type-amazon-q-connect_Span-assistantId"></a>
UUID of the Connect AI Assistant resource
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** attributes **   <a name="connect-Type-amazon-q-connect_Span-attributes"></a>
Span-specific contextual attributes
Type: [SpanAttributes](API_amazon-q-connect_SpanAttributes.md) object
Required: Yes

 ** endTimestamp **   <a name="connect-Type-amazon-q-connect_Span-endTimestamp"></a>
Operation end time in milliseconds since epoch
Type: Timestamp
Required: Yes

 ** requestId **   <a name="connect-Type-amazon-q-connect_Span-requestId"></a>
The service request ID that initiated the operation
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** sessionId **   <a name="connect-Type-amazon-q-connect_Span-sessionId"></a>
UUID of the Connect AI Session resource
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** spanId **   <a name="connect-Type-amazon-q-connect_Span-spanId"></a>
Unique span identifier
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** spanName **   <a name="connect-Type-amazon-q-connect_Span-spanName"></a>
Service-defined operation name
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** spanType **   <a name="connect-Type-amazon-q-connect_Span-spanType"></a>
Operation relationship type
Type: String
Valid Values: `CLIENT | SERVER | INTERNAL`
Required: Yes

 ** startTimestamp **   <a name="connect-Type-amazon-q-connect_Span-startTimestamp"></a>
Operation start time in milliseconds since epoch
Type: Timestamp
Required: Yes

 ** status **   <a name="connect-Type-amazon-q-connect_Span-status"></a>
Span completion status
Type: String
Valid Values: `OK | ERROR | TIMEOUT`
Required: Yes

 ** originRequestId **   <a name="connect-Type-amazon-q-connect_Span-originRequestId"></a>
The origin request identifier for end-to-end tracing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** parentSpanId **   <a name="connect-Type-amazon-q-connect_Span-parentSpanId"></a>
Parent span identifier for hierarchy. Null for root spans.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** statusDescription **   <a name="connect-Type-amazon-q-connect_Span-statusDescription"></a>
Human-readable error description when status is ERROR or TIMEOUT
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_amazon-q-connect_Span_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/Span)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/Span)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/Span)
