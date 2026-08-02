---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateAcmeEndpoint.html
---

# UpdateAcmeEndpoint
<a name="API_UpdateAcmeEndpoint"></a>

Updates the configuration of an existing ACME endpoint. You can change the authorization behavior, contact requirement, or certificate authority settings.

## Request Syntax
<a name="API_UpdateAcmeEndpoint_RequestSyntax"></a>

```
{
   "AcmeEndpointArn": "{{string}}",
   "AuthorizationBehavior": "{{string}}",
   "CertificateAuthority": { ... },
   "Contact": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateAcmeEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AcmeEndpointArn](#API_UpdateAcmeEndpoint_RequestSyntax) **   <a name="ACM-UpdateAcmeEndpoint-request-AcmeEndpointArn"></a>
The Amazon Resource Name (ARN) of the ACME endpoint to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+`
Required: Yes

 ** [AuthorizationBehavior](#API_UpdateAcmeEndpoint_RequestSyntax) **   <a name="ACM-UpdateAcmeEndpoint-request-AuthorizationBehavior"></a>
The updated authorization behavior.
Type: String
Valid Values: `PRE_APPROVED`
Required: No

 ** [CertificateAuthority](#API_UpdateAcmeEndpoint_RequestSyntax) **   <a name="ACM-UpdateAcmeEndpoint-request-CertificateAuthority"></a>
The updated certificate authority configuration.
Type: [CertificateAuthority](API_CertificateAuthority.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [Contact](#API_UpdateAcmeEndpoint_RequestSyntax) **   <a name="ACM-UpdateAcmeEndpoint-request-Contact"></a>
The updated contact requirement.
Type: String
Valid Values: `REQUIRED | NOT_REQUIRED`
Required: No

## Response Elements
<a name="API_UpdateAcmeEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateAcmeEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have access required to perform this action.
HTTP Status Code: 400

 ** ConflictException **
You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because it exceeded a quota.
 ** throttlingReasons **
One or more reasons why the request was throttled.
HTTP Status Code: 400

 ** ValidationException **
The supplied input failed to satisfy constraints of an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAcmeEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/UpdateAcmeEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/UpdateAcmeEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/UpdateAcmeEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/UpdateAcmeEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/UpdateAcmeEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/UpdateAcmeEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/UpdateAcmeEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/UpdateAcmeEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/UpdateAcmeEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/UpdateAcmeEndpoint)
