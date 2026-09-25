---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListIntegrations.html
---

# ListIntegrations
<a name="API_ListIntegrations"></a>

Lists the integrations in the account, optionally filtered by type, status, or name. Results are paginated.

## Request Parameters
<a name="API_ListIntegrations_RequestParameters"></a>

 ** integrationType **
Returns only integrations of this provider type.
Type: String
Valid Values: `AWS_CONFIG_SLREC | SLACK | EXTERNAL_AGENT | AWS_INTEGRATION`
Required: No

 ** maxResults **
Maximum number of integrations to return in one page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** name **
Returns only the integration with this exact name.
Type: String
Required: No

 ** nextToken **
Pagination token from a previous response; omit for the first page.
Type: String
Required: No

 ** status **
Returns only integrations in this status.
Type: String
Valid Values: `ACTIVE | DELETED | PENDING | PENDING_OAUTH | ERROR | FAILED`
Required: No

## Response Elements
<a name="API_ListIntegrations_ResponseElements"></a>

The following elements are returned by the service.

 ** items **
The page of integrations.
Type: Array of [Integration](API_Integration.md) objects

 ** nextToken **
Pagination token for the next page; absent when there are no more results.
Type: String

## Errors
<a name="API_ListIntegrations_Errors"></a>

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
<a name="API_ListIntegrations_Examples"></a>

### List integrations of a type
<a name="API_ListIntegrations_Example_1"></a>

The following example lists up to 20 AWS\_INTEGRATION integrations in the account. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_ListIntegrations_Example_1_Request"></a>

```
{
  "integrationType": "AWS_INTEGRATION",
  "maxResults": 20
}
```

#### Sample Response
<a name="API_ListIntegrations_Example_1_Response"></a>

```
{
  "items": [
    {
      "createdAt": "2026-09-16T00:03:00Z",
      "integrationArn": "arn:aws:cloudwatch:us-east-1:123456789012:integration/a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
      "integrationId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
      "integrationType": "AWS_INTEGRATION",
      "name": "my-aws-integration",
      "status": "ACTIVE",
      "updatedAt": "2026-09-16T00:03:00Z"
    }
  ],
  "nextToken": "eyJvZmZzZXQiOjIwfQ=="
}
```

## See Also
<a name="API_ListIntegrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/ListIntegrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/ListIntegrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ListIntegrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/ListIntegrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ListIntegrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/ListIntegrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/ListIntegrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/ListIntegrations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/ListIntegrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ListIntegrations)
