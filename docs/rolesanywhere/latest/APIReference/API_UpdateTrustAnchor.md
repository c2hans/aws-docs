---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateTrustAnchor.html
---

# UpdateTrustAnchor

Updates a trust anchor. You establish trust between IAM Roles Anywhere and your certificate authority (CA) by configuring a trust anchor. You can define a trust anchor as a reference to an AWS Private Certificate Authority (AWS Private CA) or by uploading a CA certificate. Your AWS workloads can authenticate with the trust anchor using certificates issued by the CA in exchange for temporary AWS credentials.

 **Required permissions: ** `rolesanywhere:UpdateTrustAnchor`.

## Request Syntax
<a name="API_UpdateTrustAnchor_RequestSyntax"></a>

```
PATCH /trustanchor/{{trustAnchorId}} HTTP/1.1
Content-type: application/json

{
   "aliasName": "{{string}}",
   "crlDpRevocationEnabled": {{boolean}},
   "name": "{{string}}",
   "source": {
      "sourceData": { ... },
      "sourceType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateTrustAnchor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [trustAnchorId](#API_UpdateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-UpdateTrustAnchor-request-uri-trustAnchorId"></a>
The trust anchor to act on. You can specify one of the following:
+ The trust anchor ID.
+ The trust anchor ARN.
+ The alias ARN of the trust anchor.
An ARN must be for a trust anchor in your account and Region.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `([a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}|arn:aws(-[^:]+)?:rolesanywhere(:.*){2}:(trust-anchor|alias/trust-anchor)/.*)`
Required: Yes

## Request Body
<a name="API_UpdateTrustAnchor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aliasName](#API_UpdateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-UpdateTrustAnchor-request-aliasName"></a>
The alias for the trust anchor.
You can use this parameter in the following ways:
+ To set or change the alias, specify the new alias name. After the change, the previous alias ARN no longer identifies the resource. You can then assign the previous alias to another resource of the same type. A change can take a short time to take effect for requests that use an alias ARN.
+ To remove the alias, specify an empty string.
+ To keep the current alias, omit this parameter.
An alias name contains 1 to 256 characters. It must begin with a letter (A-Z or a-z). It can contain only letters (A-Z and a-z), numbers (0-9), underscores (\_), hyphens (-), and forward slashes (/). A forward slash can appear only between two other characters, so an alias name can't end with a forward slash or contain two in a row. Alias names that begin with `aws/`, in any combination of uppercase and lowercase letters, are reserved. Alias names are case sensitive.
The alias name must be unique among resources of the same type in your account and Region. If another resource of the same type already has the alias, the request fails with a `ValidationException`. An invalid or reserved alias name also causes a `ValidationException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?!.*//)([A-Za-z]([A-Za-z0-9_/-]*[A-Za-z0-9_-])?)?`
Required: No

 ** [crlDpRevocationEnabled](#API_UpdateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-UpdateTrustAnchor-request-crlDpRevocationEnabled"></a>
Specifies whether the trust anchor checks certificate revocation status against CRL distribution points.
Type: Boolean
Required: No

 ** [name](#API_UpdateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-UpdateTrustAnchor-request-name"></a>
The name of the trust anchor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[ a-zA-Z0-9-_]*`
Required: No

 ** [source](#API_UpdateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-UpdateTrustAnchor-request-source"></a>
The trust anchor type and its related certificate data.
Type: [Source](API_Source.md) object
Required: No

## Response Syntax
<a name="API_UpdateTrustAnchor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "trustAnchor": {
      "aliasArn": "string",
      "aliasName": "string",
      "createdAt": "string",
      "crlDpRevocationEnabled": boolean,
      "enabled": boolean,
      "name": "string",
      "notificationSettings": [
         {
            "channel": "string",
            "configuredBy": "string",
            "enabled": boolean,
            "event": "string",
            "threshold": number
         }
      ],
      "previousAliasName": "string",
      "source": {
         "sourceData": { ... },
         "sourceType": "string"
      },
      "trustAnchorArn": "string",
      "trustAnchorId": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_UpdateTrustAnchor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [trustAnchor](#API_UpdateTrustAnchor_ResponseSyntax) **   <a name="rolesanywhere-UpdateTrustAnchor-response-trustAnchor"></a>
The state of the trust anchor after a read or write operation.
Type: [TrustAnchorDetail](API_TrustAnchorDetail.md) object

## Errors
<a name="API_UpdateTrustAnchor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The resource could not be found.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The request has failed due to a temporary failure of the service.
 ** message **
The exception message.
 ** retryAfterSeconds **
The recommended number of seconds after which the client should retry the request.
HTTP Status Code: 503

 ** ValidationException **
Validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTrustAnchor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/UpdateTrustAnchor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/UpdateTrustAnchor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/UpdateTrustAnchor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/UpdateTrustAnchor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/UpdateTrustAnchor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/UpdateTrustAnchor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/UpdateTrustAnchor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/UpdateTrustAnchor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/UpdateTrustAnchor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/UpdateTrustAnchor)
