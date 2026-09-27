---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_UpdateSubscriber.html
---

# UpdateSubscriber
<a name="API_UpdateSubscriber"></a>

Updates a subscriber. Fields omitted from the request are left unchanged.

## Request Parameters
<a name="API_UpdateSubscriber_RequestParameters"></a>

 ** BatchConfiguration **
Batching configuration for a subscriber.
Type: [BatchConfiguration](API_BatchConfiguration.md) object
Required: No

 ** Description **
Free-text description. Used by every resource type that has one: event buses, subscribers, and event sources.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[^\u0000-\u001F\u007F-\u009F\u2028\u2029]*(?![\s\S]).*`
Required: No

 ** FilterConfiguration **
Configuration for filtering events delivered to a subscriber. On CreateSubscriber, Filters is required and must contain at least one Filter with a non-empty Pattern. On UpdateSubscriber, an empty `FilterConfiguration:{}` clears the existing filter. Any non-empty shape (including `{Language:X}` without Filters) must contain a valid Filters list — same contract as CreateSubscriber. A non-empty Filters list overwrites; an omitted FilterConfiguration preserves existing state. All Filters are implicitly ANDed — an event must match every Filter to be delivered.
Type: [FilterConfiguration](API_FilterConfiguration.md) object
Required: No

 ** InvokeConfiguration **
Update-able configuration for how the subscriber invokes its target.
Type: [UpdateInvokeConfiguration](API_UpdateInvokeConfiguration.md) object
Required: No

 ** LogConfiguration **
Log configuration for a subscriber.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: No

 ** OnFailureConfiguration **
On-failure configuration: where a failed delivery is sent. Shared by the subscriber and the EventSource.
Type: [OnFailureConfiguration](API_OnFailureConfiguration.md) object
Required: No

 ** ResumePosition **
Position from which delivery resumes when a subscriber is unpaused. Honored only on an UpdateSubscriber call that transitions State from STOPPED to RUNNING (unpause); ignored on any other call and not accepted on Create. Defaults to LAST\_PROCESSED when omitted.
Type: String
Valid Values: `LAST_PROCESSED | LATEST`
Required: No

 ** RetryPolicy **
Retry policy for a subscriber.
Type: [RetryPolicy](API_RetryPolicy.md) object
Required: No

 ** State **
Customer-controlled run state of a subscriber, set on create or update. Distinct from the bus lifecycle vocabulary, where ACTIVE means "provisioned and healthy". Delivery requires State RUNNING on a subscriber that is not revoked.
Type: String
Valid Values: `RUNNING | STOPPED`
Required: No

 ** SubscriberArn **
The Amazon Resource Name (ARN) that uniquely identifies a subscriber.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):subscriber\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`
Required: Yes

 ** Transformer **
Transformer configuration for a subscriber.
Type: [Transformer](API_Transformer.md) object
Required: No

## Response Elements
<a name="API_UpdateSubscriber_ResponseElements"></a>

The following elements are returned by the service.

 ** EventBusArn **
The Amazon Resource Name (ARN) that uniquely identifies an event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`

 ** LastModifiedTime **
The time the subscriber was last modified.
Type: Timestamp

 ** Name **
Name of a subscriber. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '\_'.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][\.\-_A-Za-z0-9]*`

 ** PointInTimeConfiguration **
Point-in-time configuration for a subscriber. Only applicable when StartingPosition is POINT\_IN\_TIME.
Type: [PointInTimeConfiguration](API_PointInTimeConfiguration.md) object

 ** StartingPosition **
Starting position for a subscriber.
Type: String
Valid Values: `LATEST | POINT_IN_TIME`

 ** State **
Customer-controlled run state of a subscriber, set on create or update. Distinct from the bus lifecycle vocabulary, where ACTIVE means "provisioned and healthy". Delivery requires State RUNNING on a subscriber that is not revoked.
Type: String
Valid Values: `RUNNING | STOPPED`

 ** SubscriberArn **
The Amazon Resource Name (ARN) that uniquely identifies a subscriber.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):subscriber\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`

 ** Type **
Delivery ordering mode of a subscriber: FIFO delivers events in order within an event group; UNORDERED delivers without an ordering guarantee.
Type: String
Valid Values: `FIFO | UNORDERED`

## Errors
<a name="API_UpdateSubscriber_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
HTTP Status Code: 403

 ** ConcurrentModificationException **
Another change to the resource is already in progress. Retry the request.
HTTP Status Code: 409

 ** InternalException **
The request failed because of an internal service error. Retry the request.
HTTP Status Code: 500

 ** InvalidInputException **
A request parameter is missing or not valid.
HTTP Status Code: 400

 ** InvalidStateException **
The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
HTTP Status Code: 409

 ** LimitExceededException **
The request would exceed a service quota for the account.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
HTTP Status Code: 429

## See Also
<a name="API_UpdateSubscriber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridgev2-2025-05-15/UpdateSubscriber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridgev2-2025-05-15/UpdateSubscriber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/UpdateSubscriber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridgev2-2025-05-15/UpdateSubscriber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/UpdateSubscriber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridgev2-2025-05-15/UpdateSubscriber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridgev2-2025-05-15/UpdateSubscriber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridgev2-2025-05-15/UpdateSubscriber)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridgev2-2025-05-15/UpdateSubscriber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/UpdateSubscriber)
