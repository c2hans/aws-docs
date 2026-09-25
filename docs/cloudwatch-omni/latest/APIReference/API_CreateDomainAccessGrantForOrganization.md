---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateDomainAccessGrantForOrganization.html
---

# CreateDomainAccessGrantForOrganization
<a name="API_CreateDomainAccessGrantForOrganization"></a>

Creates an AccessGrant that authorizes a principal to administer an organization domain.

## Request Parameters
<a name="API_CreateDomainAccessGrantForOrganization_RequestParameters"></a>

 ** clientToken **
Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** domainId **
The ID of the organization domain to create the grant on.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

 ** name **
A name that identifies the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** permission **
The permission to grant.
Type: String
Valid Values: `ADMIN`
Required: Yes

 ** principal **
The principal receiving the grant.
Type: [OrganizationAccessGrantPrincipal](API_OrganizationAccessGrantPrincipal.md) object
Required: Yes

 ** tags **
The tags to associate with the access grant.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Elements
<a name="API_CreateDomainAccessGrantForOrganization_ResponseElements"></a>

The following element is returned by the service.

 ** accessGrant **
The details of the created organization access grant.
Type: [OrganizationAccessGrant](API_OrganizationAccessGrant.md) object

## Errors
<a name="API_CreateDomainAccessGrantForOrganization_Errors"></a>

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
<a name="API_CreateDomainAccessGrantForOrganization_Examples"></a>

### Create an organization domain access grant
<a name="API_CreateDomainAccessGrantForOrganization_Example_1"></a>

The following example grants an Identity Center user administrative access to an organization domain. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_CreateDomainAccessGrantForOrganization_Example_1_Request"></a>

```
{
  "clientToken": "3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73",
  "domainId": "d-1a2b3c4d5e",
  "name": "org-domain-admin",
  "permission": "ADMIN",
  "principal": {
    "principalId": "94b6c7d8-1a2b-4c3d-9e4f-5a6b7c8d9e0f",
    "principalType": "IDC_USER"
  },
  "tags": {
    "Team": "observability"
  }
}
```

#### Sample Response
<a name="API_CreateDomainAccessGrantForOrganization_Example_1_Response"></a>

```
{
  "accessGrant": {
    "createdAt": "2026-09-16T14:22:31Z",
    "createdBy": "arn:aws:iam::123456789012:role/ObservabilityAdmin",
    "domainId": "d-1a2b3c4d5e",
    "grantArn": "arn:aws:cloudwatch:us-east-1:123456789012:organization-access-grant/7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d",
    "grantId": "7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d",
    "grantType": "CUSTOMER_MANAGED",
    "name": "org-domain-admin",
    "permission": "ADMIN",
    "principal": {
      "principalId": "94b6c7d8-1a2b-4c3d-9e4f-5a6b7c8d9e0f",
      "principalType": "IDC_USER"
    },
    "updatedAt": "2026-09-16T14:22:31Z"
  }
}
```

## See Also
<a name="API_CreateDomainAccessGrantForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/CreateDomainAccessGrantForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/CreateDomainAccessGrantForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/CreateDomainAccessGrantForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/CreateDomainAccessGrantForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/CreateDomainAccessGrantForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/CreateDomainAccessGrantForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/CreateDomainAccessGrantForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/CreateDomainAccessGrantForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/CreateDomainAccessGrantForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/CreateDomainAccessGrantForOrganization)
