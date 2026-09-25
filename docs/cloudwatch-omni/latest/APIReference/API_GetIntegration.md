---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetIntegration.html
---

# GetIntegration
<a name="API_GetIntegration"></a>

Returns the details of a single integration, identified by its identifier, Amazon Resource Name, or name.

## Request Parameters
<a name="API_GetIntegration_RequestParameters"></a>

 ** identifier **
Identifies the integration to return — exactly one of integrationId, integrationArn, or integrationName.
Type: [IntegrationIdentifier](API_IntegrationIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Elements
<a name="API_GetIntegration_ResponseElements"></a>

The following element is returned by the service.

 ** integration **
The details of the requested integration.
Type: [Integration](API_Integration.md) object

## Errors
<a name="API_GetIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

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
<a name="API_GetIntegration_Examples"></a>

### Get an integration by id
<a name="API_GetIntegration_Example_1"></a>

The following example returns the integration with the given id. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetIntegration_Example_1_Request"></a>

```
{
  "identifier": {
    "integrationId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
  }
}
```

#### Sample Response
<a name="API_GetIntegration_Example_1_Response"></a>

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
<a name="API_GetIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetIntegration)
