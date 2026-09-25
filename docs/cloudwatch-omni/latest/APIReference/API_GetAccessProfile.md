---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetAccessProfile.html
---

# GetAccessProfile
<a name="API_GetAccessProfile"></a>

Retrieves an access profile by ID.

The response indicates whether the calling principal is currently allowed to assume the profile.

## Request Parameters
<a name="API_GetAccessProfile_RequestParameters"></a>

 ** profileId **
The unique ID of the access profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** spaceId **
The unique ID of the space.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Elements
<a name="API_GetAccessProfile_ResponseElements"></a>

The following element is returned by the service.

 ** accessProfile **
The access profile.
Type: [AccessProfile](API_AccessProfile.md) object

## Errors
<a name="API_GetAccessProfile_Errors"></a>

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
<a name="API_GetAccessProfile_Examples"></a>

### Get an access profile
<a name="API_GetAccessProfile_Example_1"></a>

The following example retrieves an access profile by ID, including whether the calling principal is currently allowed to assume it. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetAccessProfile_Example_1_Request"></a>

```
{
  "profileId": "analyst-readonly",
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_GetAccessProfile_Example_1_Response"></a>

```
{
  "accessProfile": {
    "arn": "arn:aws:cloudwatch:us-east-1:123456789012:access-profile/analyst-readonly",
    "assumeStatus": "ALLOWED",
    "createdAt": "2026-09-16T14:22:31Z",
    "description": "Read-only access for analysts.",
    "name": "Analyst read-only profile",
    "profileId": "analyst-readonly",
    "profileType": "CUSTOMER_MANAGED",
    "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
    "updatedAt": "2026-09-16T14:22:31Z"
  }
}
```

## See Also
<a name="API_GetAccessProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetAccessProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetAccessProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetAccessProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetAccessProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetAccessProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetAccessProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetAccessProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetAccessProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetAccessProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetAccessProfile)
