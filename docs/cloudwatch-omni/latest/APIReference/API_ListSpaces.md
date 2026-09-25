---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListSpaces.html
---

# ListSpaces
<a name="API_ListSpaces"></a>

Returns the spaces in the account, optionally filtered by domain.

## Request Parameters
<a name="API_ListSpaces_RequestParameters"></a>

 ** domainId **
Filter by domain ID.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: No

 ** maxResults **
The maximum number of spaces to return per page. Defaults to 100. A page can contain fewer results than this value even when more results remain; continue while nextToken is present.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
A token to retrieve the next page of results. Supply the same filters used on the request that returned it. Tokens expire after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Elements
<a name="API_ListSpaces_ResponseElements"></a>

The following elements are returned by the service.

 ** items **
The list of space summaries.
Type: Array of [SpaceSummary](API_SpaceSummary.md) objects

 ** nextToken **
A token to retrieve the next page of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListSpaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

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
<a name="API_ListSpaces_Examples"></a>

### List spaces in a domain
<a name="API_ListSpaces_Example_1"></a>

The following example lists the first page of spaces in a domain and returns a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_ListSpaces_Example_1_Request"></a>

```
{
  "domainId": "d-1a2b3c4d5e",
  "maxResults": 50
}
```

#### Sample Response
<a name="API_ListSpaces_Example_1_Response"></a>

```
{
  "items": [
    {
      "createdAt": "2026-09-16T14:22:31Z",
      "domainArn": "arn:aws:cloudwatch:us-east-1:123456789012:domain/d-1a2b3c4d5e",
      "name": "prod-observability",
      "ownerAccountId": "123456789012",
      "region": "us-east-1",
      "spaceArn": "arn:aws:cloudwatch:us-east-1:123456789012:space/a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
      "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
      "status": "ACTIVE",
      "updatedAt": "2026-09-16T14:22:31Z"
    },
    {
      "createdAt": "2026-09-16T14:22:31Z",
      "domainArn": "arn:aws:cloudwatch:us-east-1:123456789012:domain/d-1a2b3c4d5e",
      "name": "staging-observability",
      "ownerAccountId": "123456789012",
      "region": "us-east-1",
      "spaceArn": "arn:aws:cloudwatch:us-east-1:123456789012:space/b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
      "spaceId": "b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
      "status": "ACTIVE",
      "updatedAt": "2026-09-16T14:22:31Z"
    }
  ],
  "nextToken": "eyJvZmZzZXQiOjIwfQ=="
}
```

## See Also
<a name="API_ListSpaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/ListSpaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/ListSpaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ListSpaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/ListSpaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ListSpaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/ListSpaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/ListSpaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/ListSpaces)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/ListSpaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ListSpaces)
