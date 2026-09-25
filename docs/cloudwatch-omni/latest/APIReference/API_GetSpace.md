---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetSpace.html
---

# GetSpace
<a name="API_GetSpace"></a>

Retrieves the details of a space by ID.

## Request Parameters
<a name="API_GetSpace_RequestParameters"></a>

 ** spaceId **
The unique ID of the space.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Elements
<a name="API_GetSpace_ResponseElements"></a>

The following element is returned by the service.

 ** space **
The details of the space.
Type: [Space](API_Space.md) object

## Errors
<a name="API_GetSpace_Errors"></a>

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
<a name="API_GetSpace_Examples"></a>

### Get a space
<a name="API_GetSpace_Example_1"></a>

The following example retrieves the details of a space by ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetSpace_Example_1_Request"></a>

```
{
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_GetSpace_Example_1_Response"></a>

```
{
  "space": {
    "agentCoreEvaluationRoleArn": "arn:aws:iam::123456789012:role/CloudWatchAgentCoreEvaluationRole",
    "createdAt": "2026-09-16T14:22:31Z",
    "dataAccessRoleArn": "arn:aws:iam::123456789012:role/CloudWatchSpaceDataAccessRole",
    "domainArn": "arn:aws:cloudwatch:us-east-1:123456789012:domain/d-1a2b3c4d5e",
    "encryptionConfiguration": {
      "encryptionStrategy": "CUSTOMER_MANAGED",
      "kmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/1a2b3c4d-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
    },
    "name": "prod-observability",
    "ownerAccountId": "123456789012",
    "region": "us-east-1",
    "spaceArn": "arn:aws:cloudwatch:us-east-1:123456789012:space/a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
    "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
    "status": "ACTIVE",
    "updatedAt": "2026-09-16T14:22:31Z"
  }
}
```

## See Also
<a name="API_GetSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetSpace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetSpace)
