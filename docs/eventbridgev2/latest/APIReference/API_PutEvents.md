---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PutEvents.html
---

# PutEvents
<a name="API_PutEvents"></a>

Publishes events to an event bus.

## Request Parameters
<a name="API_PutEvents_RequestParameters"></a>

 ** DeduplicationConfiguration **
Request-level deduplication settings, applied to every entry in the batch.
Type: [DeduplicationConfiguration](API_DeduplicationConfiguration.md) object
Required: No

 ** Entries **
List of event entries to publish. Must contain at least one entry.
Type: Array of [PutEventsRequestEntry](API_PutEventsRequestEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** EventBusArn **
The Amazon Resource Name (ARN) that uniquely identifies an event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`
Required: Yes

## Response Elements
<a name="API_PutEvents_ResponseElements"></a>

The following elements are returned by the service.

 ** Entries **
List of per-entry publish results, in the same order as the request entries.
Type: Array of [PutEventsResultEntry](API_PutEventsResultEntry.md) objects

 ** FailedEntryCount **
The number of entries in the batch that failed to be published.
Type: Integer

## Errors
<a name="API_PutEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
HTTP Status Code: 403

 ** InternalException **
The request failed because of an internal service error. Retry the request.
HTTP Status Code: 500

 ** InvalidInputException **
A request parameter is missing or not valid.
HTTP Status Code: 400

 ** InvalidStateException **
The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
HTTP Status Code: 429

## See Also
<a name="API_PutEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridgev2-2025-05-15/PutEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridgev2-2025-05-15/PutEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/PutEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridgev2-2025-05-15/PutEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/PutEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridgev2-2025-05-15/PutEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridgev2-2025-05-15/PutEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridgev2-2025-05-15/PutEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridgev2-2025-05-15/PutEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/PutEvents)
