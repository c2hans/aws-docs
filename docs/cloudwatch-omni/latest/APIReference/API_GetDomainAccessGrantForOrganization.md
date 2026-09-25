---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetDomainAccessGrantForOrganization.html
---

# GetDomainAccessGrantForOrganization
<a name="API_GetDomainAccessGrantForOrganization"></a>

Retrieves the full detail of a single organization access grant by ID.

## Request Parameters
<a name="API_GetDomainAccessGrantForOrganization_RequestParameters"></a>

 ** grantId **
The ID of the access grant to retrieve.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Elements
<a name="API_GetDomainAccessGrantForOrganization_ResponseElements"></a>

The following element is returned by the service.

 ** accessGrant **
The retrieved organization access grant.
Type: [OrganizationAccessGrant](API_OrganizationAccessGrant.md) object

## Errors
<a name="API_GetDomainAccessGrantForOrganization_Errors"></a>

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
<a name="API_GetDomainAccessGrantForOrganization_Examples"></a>

### Get an organization domain access grant
<a name="API_GetDomainAccessGrantForOrganization_Example_1"></a>

The following example retrieves the full detail of a single organization domain access grant by ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetDomainAccessGrantForOrganization_Example_1_Request"></a>

```
{
  "grantId": "7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d"
}
```

#### Sample Response
<a name="API_GetDomainAccessGrantForOrganization_Example_1_Response"></a>

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
<a name="API_GetDomainAccessGrantForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetDomainAccessGrantForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetDomainAccessGrantForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetDomainAccessGrantForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetDomainAccessGrantForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetDomainAccessGrantForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetDomainAccessGrantForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetDomainAccessGrantForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetDomainAccessGrantForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetDomainAccessGrantForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetDomainAccessGrantForOrganization)
