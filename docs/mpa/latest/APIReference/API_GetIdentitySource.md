---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetIdentitySource.html
---

# GetIdentitySource
<a name="API_GetIdentitySource"></a>

Returns details for an identity source. For more information, see [Identity Source](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html) in the *Multi-party approval User Guide*.

## Request Syntax
<a name="API_GetIdentitySource_RequestSyntax"></a>

```
GET /identity-sources/{{IdentitySourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIdentitySource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IdentitySourceArn](#API_GetIdentitySource_RequestSyntax) **   <a name="mpa-GetIdentitySource-request-uri-IdentitySourceArn"></a>
Amazon Resource Name (ARN) for the identity source.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_GetIdentitySource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIdentitySource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": "string",
   "IdentitySourceArn": "string",
   "IdentitySourceParameters": { ... },
   "IdentitySourceType": "string",
   "Status": "string",
   "StatusCode": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_GetIdentitySource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_GetIdentitySource_ResponseSyntax) **   <a name="mpa-GetIdentitySource-response-CreationTime"></a>
Timestamp when the identity source was created.
Type: Timestamp

 ** [IdentitySourceArn](#API_GetIdentitySource_ResponseSyntax) **   <a name="mpa-GetIdentitySource-response-IdentitySourceArn"></a>
Amazon Resource Name (ARN) for the identity source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [IdentitySourceParameters](#API_GetIdentitySource_ResponseSyntax) **   <a name="mpa-GetIdentitySource-response-IdentitySourceParameters"></a>
A ` IdentitySourceParameters` object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.
Type: [IdentitySourceParametersForGet](API_IdentitySourceParametersForGet.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [IdentitySourceType](#API_GetIdentitySource_ResponseSyntax) **   <a name="mpa-GetIdentitySource-response-IdentitySourceType"></a>
The type of resource that provided identities to the identity source. For example, an IAM Identity Center instance.
Type: String
Valid Values: `IAM_IDENTITY_CENTER`

 ** [Status](#API_GetIdentitySource_ResponseSyntax) **   <a name="mpa-GetIdentitySource-response-Status"></a>
Status for the identity source. For example, if the identity source is `ACTIVE`.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | ERROR`

 ** [StatusCode](#API_GetIdentitySource_ResponseSyntax) **   <a name="mpa-GetIdentitySource-response-StatusCode"></a>
Status code of the identity source.
Type: String
Valid Values: `ACCESS_DENIED | DELETION_FAILED | IDC_INSTANCE_NOT_FOUND | IDC_INSTANCE_NOT_VALID`

 ** [StatusMessage](#API_GetIdentitySource_ResponseSyntax) **   <a name="mpa-GetIdentitySource-response-StatusMessage"></a>
Message describing the status for the identity source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Errors
<a name="API_GetIdentitySource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You do not have sufficient access to perform this action. Check your permissions, and try again.
 ** Message **
Message for the `AccessDeniedException` error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error. Try your request again. If the problem persists, contact AWS Support.
 ** Message **
Message for the `InternalServerException` error.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The specified resource doesn't exist. Check the resource ID, and try again.
 ** Message **
Message for the `ResourceNotFoundException` error.
HTTP Status Code: 404

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling.
 ** Message **
Message for the `ThrottlingException` error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the constraints specified by an AWS service.
 ** Message **
Message for the `ValidationException` error.
HTTP Status Code: 400

## See Also
<a name="API_GetIdentitySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/GetIdentitySource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/GetIdentitySource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/GetIdentitySource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/GetIdentitySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/GetIdentitySource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/GetIdentitySource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/GetIdentitySource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/GetIdentitySource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/GetIdentitySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/GetIdentitySource)
