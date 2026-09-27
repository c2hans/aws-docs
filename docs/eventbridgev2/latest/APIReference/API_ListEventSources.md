---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_ListEventSources.html
---

# ListEventSources
<a name="API_ListEventSources"></a>

Lists EventSources as summaries. By default the list spans the EventSources the caller account owns; set EventBusArn to scope it to one bus. Use DescribeEventSource to retrieve full configuration.

## Request Parameters
<a name="API_ListEventSources_RequestParameters"></a>

 ** EventBusArn **
The Amazon Resource Name (ARN) that uniquely identifies an event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`
Required: No

 ** MaxResults **
Maximum number of results to return in one page of a List operation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** NamePrefix **
EventSource name. First character alphanumeric; the rest may add '.', '-', '\_'. Names may not begin with the reserved "aws." prefix. The grammar matches the ARN local-name segment in EventSourceArn (event-sourcev2/<type>/<name>/<id>), mirroring EventBusName, so a name the ARN cannot represent cannot be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(?!aws\.)[A-Za-z0-9][\.\-_A-Za-z0-9]*`
Required: No

 ** NextToken **
Opaque pagination token returned by a List operation. Pass it back in the next request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## Response Elements
<a name="API_ListEventSources_ResponseElements"></a>

The following elements are returned by the service.

 ** EventSources **
List of EventSource summaries.
Type: Array of [EventSourceSummary](API_EventSourceSummary.md) objects

 ** NextToken **
Opaque pagination token returned by a List operation. Pass it back in the next request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_ListEventSources_Errors"></a>

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
<a name="API_ListEventSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridgev2-2025-05-15/ListEventSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridgev2-2025-05-15/ListEventSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/ListEventSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridgev2-2025-05-15/ListEventSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/ListEventSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridgev2-2025-05-15/ListEventSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridgev2-2025-05-15/ListEventSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridgev2-2025-05-15/ListEventSources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridgev2-2025-05-15/ListEventSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/ListEventSources)
