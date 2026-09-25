---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListViews.html
---

# ListViews
<a name="API_ListViews"></a>

Lists the views in the caller's account and region.

Returns a summary for each view, optionally filtered by view type. View definitions are not included — use GetView to retrieve them.

## Request Parameters
<a name="API_ListViews_RequestParameters"></a>

 ** maxResults **
The maximum number of views to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
A token to retrieve the next page of results.
Type: String
Required: No

 ** type **
Return only views of this ownership category.
Type: String
Valid Values: `USER | MANAGED`
Required: No

## Response Elements
<a name="API_ListViews_ResponseElements"></a>

The following elements are returned by the service.

 ** items **
The list of view summaries.
Type: Array of [ViewSummary](API_ViewSummary.md) objects

 ** nextToken **
A token to retrieve the next page of results, or null if there are no more results.
Type: String

## Errors
<a name="API_ListViews_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was throttled due to exceeding the allowed request rate.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request. Not always present.
HTTP Status Code: 429

 ** ValidationException **
A parameter is specified incorrectly.
 ** errorCode **
The error code associated with the validation failure.
HTTP Status Code: 400

## Examples
<a name="API_ListViews_Examples"></a>

### List the views in an account and Region
<a name="API_ListViews_Example_1"></a>

The following example returns a page of view summaries, filtered to user-created views. Definitions are not included — call GetView to retrieve them. A nextToken is returned when more results are available. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_ListViews_Example_1_Request"></a>

```
{
  "maxResults": 10,
  "type": "USER"
}
```

#### Sample Response
<a name="API_ListViews_Example_1_Response"></a>

```
{
  "items": [
    {
      "createdAt": "2026-09-16T14:22:31Z",
      "description": "Error counts by service",
      "name": "view.service_errors",
      "type": "USER",
      "updatedAt": "2026-09-16T14:22:31Z"
    }
  ],
  "nextToken": "eyJvZmZzZXQiOjEwfQ=="
}
```

## See Also
<a name="API_ListViews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/ListViews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/ListViews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ListViews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/ListViews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ListViews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/ListViews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/ListViews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/ListViews)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/ListViews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ListViews)
