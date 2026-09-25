---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateDomainForOrganization.html
---

# CreateDomainForOrganization
<a name="API_CreateDomainForOrganization"></a>

Creates an organization-scoped domain for the caller's AWS Organization. Only the organization's management account can call this operation.

## Request Parameters
<a name="API_CreateDomainForOrganization_RequestParameters"></a>

 ** clientToken **
Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** domainAccessRoleArn **
The ARN of an IAM role in the management account used for domain access. You must create this role, and its trust policy must allow the service principal to assume it.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:iam::[0-9]{12}:role/.+`
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
Required: Yes

 ** name **
A name that identifies the organization domain. Must be 3-63 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

 ** tags **
The tags to associate with the domain.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Elements
<a name="API_CreateDomainForOrganization_ResponseElements"></a>

The following element is returned by the service.

 ** organizationDomain **
The details of the created organization domain.
Type: [OrganizationDomain](API_OrganizationDomain.md) object

## Errors
<a name="API_CreateDomainForOrganization_Errors"></a>

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
<a name="API_CreateDomainForOrganization_Examples"></a>

### Create an organization domain
<a name="API_CreateDomainForOrganization_Example_1"></a>

The following example creates an organization-scoped domain from the organization's management account, configures it with an Identity Center instance, and supplies an IAM role in the management account for domain access. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_CreateDomainForOrganization_Example_1_Request"></a>

```
{
  "clientToken": "3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73",
  "domainAccessRoleArn": "arn:aws:iam::123456789012:role/CloudWatchOrganizationDomainAccessRole",
  "identityProviderConfiguration": {
    "identityCenterConfiguration": {
      "identityCenterInstanceArn": "arn:aws:sso:::instance/ssoins-1234567890abcdef"
    }
  },
  "identityProviders": [
    "IDC"
  ],
  "name": "prod-observability-org",
  "tags": {
    "Team": "observability"
  }
}
```

#### Sample Response
<a name="API_CreateDomainForOrganization_Example_1_Response"></a>

```
{
  "organizationDomain": {
    "createdAt": "2026-09-16T14:22:31Z",
    "customEndpointUrls": [
      "https://prod-observability-org.cloudwatch-omni.global.app.aws"
    ],
    "domainAccessRoleArn": "arn:aws:iam::123456789012:role/CloudWatchOrganizationDomainAccessRole",
    "domainArn": "arn:aws:cloudwatch:us-east-1:123456789012:organization-domain/d-9z8y7x6w5v",
    "domainEndpointUrl": "https://d-9z8y7x6w5v.cloudwatch-omni.global.app.aws",
    "domainId": "d-9z8y7x6w5v",
    "identityCenterApplicationArn": "arn:aws:sso::123456789012:application/ssoins-1234567890abcdef/apl-0f9e8d7c6b5a4938",
    "identityProviderConfiguration": {
      "identityCenterConfiguration": {
        "identityCenterInstanceArn": "arn:aws:sso:::instance/ssoins-1234567890abcdef"
      }
    },
    "identityProviders": [
      "IDC"
    ],
    "name": "prod-observability-org",
    "organizationId": "o-a1b2c3d4e5",
    "ownerAccountId": "123456789012",
    "region": "us-east-1",
    "status": "ACTIVE",
    "updatedAt": "2026-09-16T14:22:31Z"
  }
}
```

## See Also
<a name="API_CreateDomainForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/CreateDomainForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/CreateDomainForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/CreateDomainForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/CreateDomainForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/CreateDomainForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/CreateDomainForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/CreateDomainForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/CreateDomainForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/CreateDomainForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/CreateDomainForOrganization)
