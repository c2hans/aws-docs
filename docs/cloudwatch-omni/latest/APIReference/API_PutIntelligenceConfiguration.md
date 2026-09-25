---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_PutIntelligenceConfiguration.html
---

# PutIntelligenceConfiguration
<a name="API_PutIntelligenceConfiguration"></a>

Creates or updates the intelligence configuration for the calling account. Account is identified via FAS (caller identity).

## Request Parameters
<a name="API_PutIntelligenceConfiguration_RequestParameters"></a>

 ** clientToken **
Idempotency token for safe retries. Repeating a request with the same token applies the update at most once instead of reprocessing it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** kmsKeyArn **
Optional KMS key ARN to configure customer-managed encryption for anomaly data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):kms:[a-z0-9-]+:[0-9]{12}:key/(?:mrk-)?[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** removeKmsKey **
Set to true to disassociate the configured KMS key. Mutually exclusive with kmsKeyArn; the service returns ValidationException if both are provided.
Type: Boolean
Required: No

## Response Elements
<a name="API_PutIntelligenceConfiguration_ResponseElements"></a>

The following elements are returned by the service.

 ** accountId **
The AWS account ID this configuration applies to.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** createdAt **
ISO-8601 timestamp of initial creation.
Type: Timestamp

 ** kmsKeyArn **
The currently active KMS key ARN for customer-managed encryption, if configured.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):kms:[a-z0-9-]+:[0-9]{12}:key/(?:mrk-)?[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** updatedAt **
ISO-8601 timestamp of the last update.
Type: Timestamp

## Errors
<a name="API_PutIntelligenceConfiguration_Errors"></a>

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
<a name="API_PutIntelligenceConfiguration_Examples"></a>

### Configure a customer-managed KMS key
<a name="API_PutIntelligenceConfiguration_Example_1"></a>

The following example sets the customer-managed KMS key used to encrypt the account's intelligence data. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_PutIntelligenceConfiguration_Example_1_Request"></a>

```
{
  "clientToken": "b3f8c7d6-5b4a-4c3d-9e2f-1a0b2c3d4e5f",
  "kmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/1a2b3c4d-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_PutIntelligenceConfiguration_Example_1_Response"></a>

```
{
  "accountId": "123456789012",
  "createdAt": "2026-01-15T08:30:00Z",
  "kmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/1a2b3c4d-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
  "updatedAt": "2026-09-16T12:00:00Z"
}
```

## See Also
<a name="API_PutIntelligenceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/PutIntelligenceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/PutIntelligenceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/PutIntelligenceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/PutIntelligenceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/PutIntelligenceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/PutIntelligenceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/PutIntelligenceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/PutIntelligenceConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/PutIntelligenceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/PutIntelligenceConfiguration)
