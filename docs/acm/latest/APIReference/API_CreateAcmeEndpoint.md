---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeEndpoint.html
---

# CreateAcmeEndpoint
<a name="API_CreateAcmeEndpoint"></a>

Creates an ACME endpoint, which is a managed ACME server with a unique endpoint URL. After creation, ACME clients can use the endpoint URL to automate certificate issuance using the ACME protocol.

## Request Syntax
<a name="API_CreateAcmeEndpoint_RequestSyntax"></a>

```
{
   "AuthorizationBehavior": "{{string}}",
   "CertificateAuthority": { ... },
   "CertificateTags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Contact": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAcmeEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AuthorizationBehavior](#API_CreateAcmeEndpoint_RequestSyntax) **   <a name="ACM-CreateAcmeEndpoint-request-AuthorizationBehavior"></a>
The authorization behavior for the ACME endpoint.
Type: String
Valid Values: `PRE_APPROVED`
Required: Yes

 ** [CertificateAuthority](#API_CreateAcmeEndpoint_RequestSyntax) **   <a name="ACM-CreateAcmeEndpoint-request-CertificateAuthority"></a>
The type of certificate authority to use for issuing certificates through this ACME endpoint.
Type: [CertificateAuthority](API_CertificateAuthority.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [CertificateTags](#API_CreateAcmeEndpoint_RequestSyntax) **   <a name="ACM-CreateAcmeEndpoint-request-CertificateTags"></a>
Tags to apply to certificates issued through this ACME endpoint.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [Contact](#API_CreateAcmeEndpoint_RequestSyntax) **   <a name="ACM-CreateAcmeEndpoint-request-Contact"></a>
Specifies whether ACME clients must provide contact information during account registration.
Type: String
Valid Values: `REQUIRED | NOT_REQUIRED`
Required: No

 ** [IdempotencyToken](#API_CreateAcmeEndpoint_RequestSyntax) **   <a name="ACM-CreateAcmeEndpoint-request-IdempotencyToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Required: No

 ** [Tags](#API_CreateAcmeEndpoint_RequestSyntax) **   <a name="ACM-CreateAcmeEndpoint-request-Tags"></a>
One or more tags to associate with the ACME endpoint.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAcmeEndpoint_ResponseSyntax"></a>

```
{
   "AcmeEndpointArn": "string"
}
```

## Response Elements
<a name="API_CreateAcmeEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AcmeEndpointArn](#API_CreateAcmeEndpoint_ResponseSyntax) **   <a name="ACM-CreateAcmeEndpoint-response-AcmeEndpointArn"></a>
The Amazon Resource Name (ARN) of the created ACME endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+`

## Errors
<a name="API_CreateAcmeEndpoint_Errors"></a>

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

 ** ServiceQuotaExceededException **
A service quota has been exceeded.
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
<a name="API_CreateAcmeEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/CreateAcmeEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/CreateAcmeEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/CreateAcmeEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/CreateAcmeEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/CreateAcmeEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/CreateAcmeEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/CreateAcmeEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/CreateAcmeEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/CreateAcmeEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/CreateAcmeEndpoint)
