---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetDomainForOrganization.html
---

# GetDomainForOrganization
<a name="API_GetDomainForOrganization"></a>

Retrieves the details of an organization domain by ID.

## Request Parameters
<a name="API_GetDomainForOrganization_RequestParameters"></a>

 ** domainId **
The ID of the organization domain.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

## Response Elements
<a name="API_GetDomainForOrganization_ResponseElements"></a>

The following element is returned by the service.

 ** organizationDomain **
The details of the organization domain.
Type: [OrganizationDomain](API_OrganizationDomain.md) object

## Errors
<a name="API_GetDomainForOrganization_Errors"></a>

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
<a name="API_GetDomainForOrganization_Examples"></a>

### Get an organization domain
<a name="API_GetDomainForOrganization_Example_1"></a>

The following example retrieves the configuration and status of an organization-scoped domain by its ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetDomainForOrganization_Example_1_Request"></a>

```
{
  "domainId": "d-9z8y7x6w5v"
}
```

#### Sample Response
<a name="API_GetDomainForOrganization_Example_1_Response"></a>

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
<a name="API_GetDomainForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetDomainForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetDomainForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetDomainForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetDomainForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetDomainForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetDomainForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetDomainForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetDomainForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetDomainForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetDomainForOrganization)
