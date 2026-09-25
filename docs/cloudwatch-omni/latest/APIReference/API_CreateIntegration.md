---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateIntegration.html
---

# CreateIntegration
<a name="API_CreateIntegration"></a>

Creates an integration with a third-party provider. Returns the integration identifier and its initial status; when the provider requires interactive consent, an authorization URL is returned for the user to complete setup.

## Request Parameters
<a name="API_CreateIntegration_RequestParameters"></a>

 ** clientToken **
Idempotency token for safe retries. Retrying with the same token returns the original integration instead of creating a duplicate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** credential **
The credential used to authenticate with the third-party provider.
Type: [IntegrationCredential](API_IntegrationCredential.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** integrationAttributes **
Provider-specific attributes to associate with the integration.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** integrationType **
The type of third-party provider to integrate with.
Type: String
Valid Values: `AWS_CONFIG_SLREC | SLACK | EXTERNAL_AGENT | AWS_INTEGRATION`
Required: Yes

 ** name **
The name for the new integration; unique within the account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** roleArn **
The Amazon Resource Name of the IAM role assumed to access the integration.
Type: String
Required: No

 ** tags **
Tags to apply to the integration at creation time (Tagris tag-on-create).
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Elements
<a name="API_CreateIntegration_ResponseElements"></a>

The following element is returned by the service.

 ** integration **
The details of the created integration. This is the same object returned by GetIntegration and UpdateIntegration.
Type: [Integration](API_Integration.md) object

## Errors
<a name="API_CreateIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The operation could not be completed because of a conflict with the current state of the resource.
 ** conflictType **
The type of conflict that caused the request to fail. Not always present.
 ** errorCode **
The error code associated with the conflict. Not always present.
 ** message **
A human-readable description of the conflict.
 ** resourceId **
The identifier of the resource that is in conflict. Not always present.
 ** resourceType **
The type of the resource that is in conflict. Not always present.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** errorCode **
The error code associated with the failure.
 ** resourceId **
The identifier of the resource that could not be found. Not always present.
 ** resourceType **
The type of the resource that could not be found. Not always present.
HTTP Status Code: 404

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
<a name="API_CreateIntegration_Examples"></a>

### Create an AWS integration
<a name="API_CreateIntegration_Example_1"></a>

The following example creates an AWS\_INTEGRATION named my-aws-integration, authorized by an IAM role. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_CreateIntegration_Example_1_Request"></a>

```
{
  "clientToken": "b3f8c7d6-5b4a-4c3d-9e2f-1a0b2c3d4e5f",
  "integrationType": "AWS_INTEGRATION",
  "name": "my-aws-integration",
  "roleArn": "arn:aws:iam::123456789012:role/service-role/CloudWatchIntegrationRole"
}
```

#### Sample Response
<a name="API_CreateIntegration_Example_1_Response"></a>

```
{
  "integration": {
    "createdAt": "2026-09-16T00:03:00Z",
    "integrationArn": "arn:aws:cloudwatch:us-east-1:123456789012:integration/a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
    "integrationId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
    "integrationType": "AWS_INTEGRATION",
    "name": "my-aws-integration",
    "roleArn": "arn:aws:iam::123456789012:role/service-role/CloudWatchIntegrationRole",
    "status": "ACTIVE",
    "updatedAt": "2026-09-16T00:03:00Z"
  }
}
```

## See Also
<a name="API_CreateIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/CreateIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/CreateIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/CreateIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/CreateIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/CreateIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/CreateIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/CreateIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/CreateIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/CreateIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/CreateIntegration)
