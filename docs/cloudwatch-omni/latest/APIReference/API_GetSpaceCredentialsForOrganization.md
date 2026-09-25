---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetSpaceCredentialsForOrganization.html
---

# GetSpaceCredentialsForOrganization
<a name="API_GetSpaceCredentialsForOrganization"></a>

Returns temporary credentials for a space in an organization member account. The credentials are valid for one hour.

The caller must be the organization's management account or a delegated administrator with access to the target space. The target account must be an active member of the same organization as the domain, and the space must already exist.

## Request Parameters
<a name="API_GetSpaceCredentialsForOrganization_RequestParameters"></a>

 ** context **
Context for credential resolution.
Type: [SpaceCredentialRequestContext](API_SpaceCredentialRequestContext.md) object
Required: Yes

 ** credentialType **
Selects which member-account credential to return. Set this to SPACE\_OPERATION.
Type: String
Valid Values: `SPACE_OPERATION`
Required: Yes

## Response Elements
<a name="API_GetSpaceCredentialsForOrganization_ResponseElements"></a>

The following element is returned by the service.

 ** credentials **
The temporary AWS credentials for the space.
Type: [AwsCredentials](API_AwsCredentials.md) object

## Errors
<a name="API_GetSpaceCredentialsForOrganization_Errors"></a>

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
<a name="API_GetSpaceCredentialsForOrganization_Examples"></a>

### Get space credentials for an organization member account
<a name="API_GetSpaceCredentialsForOrganization_Example_1"></a>

The following example returns temporary, space-scoped AWS credentials for an existing space in an organization member account, selected by spaceId. The credentials are valid for one hour, as reflected by the expiration timestamp. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetSpaceCredentialsForOrganization_Example_1_Request"></a>

```
{
  "context": {
    "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
  },
  "credentialType": "SPACE_OPERATION"
}
```

#### Sample Response
<a name="API_GetSpaceCredentialsForOrganization_Example_1_Response"></a>

```
{
  "credentials": {
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "expiration": "2026-09-16T15:22:31Z",
    "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "sessionToken": "IQoJb3JpZ2luX2VjEXAMPLESESSIONTOKEN1234567890"
  }
}
```

## See Also
<a name="API_GetSpaceCredentialsForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetSpaceCredentialsForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetSpaceCredentialsForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetSpaceCredentialsForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetSpaceCredentialsForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetSpaceCredentialsForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetSpaceCredentialsForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetSpaceCredentialsForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetSpaceCredentialsForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetSpaceCredentialsForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetSpaceCredentialsForOrganization)
