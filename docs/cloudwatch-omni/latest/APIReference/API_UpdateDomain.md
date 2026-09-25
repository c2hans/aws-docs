---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateDomain.html
---

# UpdateDomain
<a name="API_UpdateDomain"></a>

Updates a domain's name or identity provider configuration.

Only the provided fields are changed; omitted fields are left unchanged. Renaming a domain also changes the endpoint URLs derived from its name.

## Request Parameters
<a name="API_UpdateDomain_RequestParameters"></a>

 ** domainId **
The unique ID of the domain to update.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

 ** identityProviderConfiguration **
Identity provider configuration for the domain.
Type: [IdentityProviderConfiguration](API_IdentityProviderConfiguration.md) object
Required: No

 ** identityProviders **
The identity providers to configure for the domain.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `IAM | IDC`
Required: No

 ** name **
A new name for the domain. Omit to leave unchanged. Must be 3-63 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: No

## Response Elements
<a name="API_UpdateDomain_ResponseElements"></a>

The following element is returned by the service.

 ** domain **
The details of the updated domain.
Type: [Domain](API_Domain.md) object

## Errors
<a name="API_UpdateDomain_Errors"></a>

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

 ** ServiceQuotaExceededException **
A service quota was exceeded.
HTTP Status Code: 402

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
<a name="API_UpdateDomain_Examples"></a>

### Rename a domain
<a name="API_UpdateDomain_Example_1"></a>

The following example performs a partial update that changes only the domain name; the omitted fields are left unchanged. Renaming the domain also updates the endpoint URLs derived from its name, and updatedAt advances past createdAt. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_UpdateDomain_Example_1_Request"></a>

```
{
  "domainId": "d-1a2b3c4d5e",
  "name": "prod-observability-metrics"
}
```

#### Sample Response
<a name="API_UpdateDomain_Example_1_Response"></a>

```
{
  "domain": {
    "createdAt": "2026-09-16T14:22:31Z",
    "customEndpointUrls": [
      "https://prod-observability-metrics.cloudwatch-omni.global.app.aws"
    ],
    "domainArn": "arn:aws:cloudwatch:us-east-1:123456789012:domain/d-1a2b3c4d5e",
    "domainEndpointUrl": "https://d-1a2b3c4d5e.cloudwatch-omni.global.app.aws",
    "domainId": "d-1a2b3c4d5e",
    "identityCenterApplicationArn": "arn:aws:sso::123456789012:application/ssoins-1234567890abcdef/apl-0f9e8d7c6b5a4938",
    "identityProviderConfiguration": {
      "identityCenterConfiguration": {
        "identityCenterInstanceArn": "arn:aws:sso:::instance/ssoins-1234567890abcdef"
      }
    },
    "identityProviders": [
      "IDC"
    ],
    "name": "prod-observability-metrics",
    "region": "us-east-1",
    "status": "ACTIVE",
    "updatedAt": "2026-09-17T09:11:52Z"
  }
}
```

## See Also
<a name="API_UpdateDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/UpdateDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/UpdateDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/UpdateDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/UpdateDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/UpdateDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/UpdateDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/UpdateDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/UpdateDomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/UpdateDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/UpdateDomain)
