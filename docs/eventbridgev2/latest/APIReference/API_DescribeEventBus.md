---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_DescribeEventBus.html
---

# DescribeEventBus
<a name="API_DescribeEventBus"></a>

Returns the full configuration and lifecycle state of an event bus.

## Request Parameters
<a name="API_DescribeEventBus_RequestParameters"></a>

 ** EventBusArn **
The Amazon Resource Name (ARN) that uniquely identifies an event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`
Required: Yes

## Response Elements
<a name="API_DescribeEventBus_ResponseElements"></a>

The following elements are returned by the service.

 ** CreationTime **
The time the event bus was created.
Type: Timestamp

 ** Description **
Free-text description. Used by every resource type that has one: event buses, subscribers, and event sources.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[^\u0000-\u001F\u007F-\u009F\u2028\u2029]*(?![\s\S]).*`

 ** EncryptionConfiguration **
Encryption configuration for an event bus.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** EventBusArn **
The Amazon Resource Name (ARN) that uniquely identifies an event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`

 ** LastModifiedTime **
The time the event bus was last modified.
Type: Timestamp

 ** Name **
Name of an event bus. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '\_'. The grammar matches the name segment of EventBusArn (event-busv2/<name>/<id>), so every valid name can be represented in the bus's ARN. The same type is used everywhere a bus name appears.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][\.\-_A-Za-z0-9]*`

 ** State **
Lifecycle state of an event bus.
+ CREATING: Bus creation is in progress.
+ CREATE\_FAILED: Bus creation failed; see StateReason. The bus cannot be recovered or recreated in place: delete it with DeleteEventBus, then create a new bus.
+ ACTIVE: Bus is fully operational and can accept events.
+ UPDATING: Bus update is in progress.
+ UPDATE\_FAILED: Bus update failed; the bus remains operational with its previous configuration.
+ DELETING: Bus deletion is actively in progress.
+ DELETE\_FAILED: Bus deletion failed; see StateReason. Retry DeleteEventBus after removing subscribers and event sources.
Type: String
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | ACTIVE | DELETE_FAILED`

 ** StateReason **
Human-readable explanation of why an event bus is in its current State. Omitted when the bus is in a normal operational state (ACTIVE). It stands in for the error response an asynchronous failure cannot return, so it applies only to resources with an asynchronous lifecycle: event buses. EventSources and subscribers are provisioned synchronously and report failures directly on the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** StorageConfiguration **
Event storage configuration of an event bus, as returned on reads.
Type: [StorageConfigurationOutput](API_StorageConfigurationOutput.md) object

## Errors
<a name="API_DescribeEventBus_Errors"></a>

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

 ** ResourceNotFoundException **
The resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
HTTP Status Code: 429

## See Also
<a name="API_DescribeEventBus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridgev2-2025-05-15/DescribeEventBus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridgev2-2025-05-15/DescribeEventBus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/DescribeEventBus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridgev2-2025-05-15/DescribeEventBus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/DescribeEventBus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridgev2-2025-05-15/DescribeEventBus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridgev2-2025-05-15/DescribeEventBus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridgev2-2025-05-15/DescribeEventBus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridgev2-2025-05-15/DescribeEventBus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/DescribeEventBus)
