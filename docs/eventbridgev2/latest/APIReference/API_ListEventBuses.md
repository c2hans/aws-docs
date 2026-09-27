---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_ListEventBuses.html
---

# ListEventBuses
<a name="API_ListEventBuses"></a>

Lists the event buses visible to the caller: buses the account owns and buses shared with it through AWS RAM. Shared entries carry identity fields only (Name, EventBusArn, EventBusAccountId); owned entries carry every summary field. Set EventBusAccountId to scope the list to one owner account.

## Request Parameters
<a name="API_ListEventBuses_RequestParameters"></a>

 ** EventBusAccountId **
AWS Account Id.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** MaxResults **
Maximum number of results to return in one page of a List operation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** NamePrefix **
Name of an event bus. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '\_'. The grammar matches the name segment of EventBusArn (event-busv2/<name>/<id>), so every valid name can be represented in the bus's ARN. The same type is used everywhere a bus name appears.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][\.\-_A-Za-z0-9]*`
Required: No

 ** NextToken **
Opaque pagination token returned by a List operation. Pass it back in the next request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## Response Elements
<a name="API_ListEventBuses_ResponseElements"></a>

The following elements are returned by the service.

 ** EventBuses **
List of event bus summaries.
Type: Array of [EventBusSummary](API_EventBusSummary.md) objects

 ** NextToken **
Opaque pagination token returned by a List operation. Pass it back in the next request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_ListEventBuses_Errors"></a>

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

 ** ThrottlingException **
The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
HTTP Status Code: 429

## See Also
<a name="API_ListEventBuses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridgev2-2025-05-15/ListEventBuses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridgev2-2025-05-15/ListEventBuses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/ListEventBuses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridgev2-2025-05-15/ListEventBuses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/ListEventBuses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridgev2-2025-05-15/ListEventBuses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridgev2-2025-05-15/ListEventBuses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridgev2-2025-05-15/ListEventBuses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridgev2-2025-05-15/ListEventBuses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/ListEventBuses)
