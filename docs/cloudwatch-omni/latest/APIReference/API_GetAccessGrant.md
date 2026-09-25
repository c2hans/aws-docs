---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetAccessGrant.html
---

# GetAccessGrant
<a name="API_GetAccessGrant"></a>

Retrieves the full detail of a single AccessGrant by ID.

## Request Parameters
<a name="API_GetAccessGrant_RequestParameters"></a>

 ** grantId **
The ID of the access grant to retrieve.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Elements
<a name="API_GetAccessGrant_ResponseElements"></a>

The following element is returned by the service.

 ** accessGrant **
The full details of the access grant.
Type: [AccessGrant](API_AccessGrant.md) object

## Errors
<a name="API_GetAccessGrant_Errors"></a>

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
<a name="API_GetAccessGrant_Examples"></a>

### Get an access grant
<a name="API_GetAccessGrant_Example_1"></a>

The following example retrieves the full detail of a single access grant by ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetAccessGrant_Example_1_Request"></a>

```
{
  "grantId": "7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d"
}
```

#### Sample Response
<a name="API_GetAccessGrant_Example_1_Response"></a>

```
{
  "accessGrant": {
    "accountId": "123456789012",
    "createdAt": "2026-09-16T14:22:31Z",
    "createdBy": "arn:aws:iam::123456789012:role/ObservabilityAdmin",
    "domainId": "d-1a2b3c4d5e",
    "grantArn": "arn:aws:cloudwatch:us-east-1:123456789012:access-grant/7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d",
    "grantId": "7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d",
    "grantType": "CUSTOMER_MANAGED",
    "name": "analyst-read-access",
    "permission": "CUSTOM",
    "principal": {
      "principalId": "94b6c7d8-1a2b-4c3d-9e4f-5a6b7c8d9e0f",
      "principalType": "IDC_USER"
    },
    "scopedActions": [
      {
        "actions": [
          "cloudwatch:GetOmniDashboard",
          "cloudwatch:UpdateOmniDashboard"
        ],
        "resources": [
          {
            "resourceArns": [
              "arn:aws:cloudwatch:us-east-1:123456789012:omni-dashboard/c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f"
            ],
            "resourceType": "OmniDashboard"
          }
        ]
      }
    ],
    "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
    "updatedAt": "2026-09-16T14:22:31Z"
  }
}
```

## See Also
<a name="API_GetAccessGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetAccessGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetAccessGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetAccessGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetAccessGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetAccessGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetAccessGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetAccessGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetAccessGrant)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetAccessGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetAccessGrant)
