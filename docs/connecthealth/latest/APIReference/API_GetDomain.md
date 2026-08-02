---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetDomain.html
---

# GetDomain
<a name="API_GetDomain"></a>

Retrieves information about a Domain.

## Request Syntax
<a name="API_GetDomain_RequestSyntax"></a>

```
GET /domain/{{domainId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDomain_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_GetDomain_RequestSyntax) **   <a name="connecthealth-GetDomain-request-uri-domainId"></a>
The id of the Domain to get
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetDomain_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": number,
   "domainId": "string",
   "encryptionContext": {
      "encryptionType": "string",
      "kmsKeyArn": "string"
   },
   "kmsKeyArn": "string",
   "name": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "webAppConfiguration": {
      "ehrRole": "string",
      "idcApplicationId": "string",
      "idcRegion": "string"
   },
   "webAppUrl": "string"
}
```

## Response Elements
<a name="API_GetDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetDomain_ResponseSyntax) **   <a name="connecthealth-GetDomain-response-arn"></a>

Type: String
Pattern: `arn:aws:health-agent:[a-z0-9-]+:[0-9]{12}:domain/(hai-|dom-)[a-z0-9]+`

 ** [createdAt](#API_GetDomain_ResponseSyntax) **   <a name="connecthealth-GetDomain-response-createdAt"></a>

Type: Timestamp

 ** [domainId](#API_GetDomain_ResponseSyntax) **   <a name="connecthealth-GetDomain-response-domainId"></a>

Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`

 ** [encryptionContext](#API_GetDomain_ResponseSyntax) **   <a name="connecthealth-GetDomain-response-encryptionContext"></a>

Type: [EncryptionContext](API_EncryptionContext.md) object

 ** [kmsKeyArn](#API_GetDomain_ResponseSyntax) **   <a name="connecthealth-GetDomain-response-kmsKeyArn"></a>

Type: String
Pattern: `arn:aws:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9-]+`

 ** [name](#API_GetDomain_ResponseSyntax) **   <a name="connecthealth-GetDomain-response-name"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [status](#API_GetDomain_ResponseSyntax) **   <a name="connecthealth-GetDomain-response-status"></a>

Type: String
Valid Values: `ACTIVE | DELETING | DELETED`

 ** [tags](#API_GetDomain_ResponseSyntax) **   <a name="connecthealth-GetDomain-response-tags"></a>
Tags associated with the Domain
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [webAppConfiguration](#API_GetDomain_ResponseSyntax) **   <a name="connecthealth-GetDomain-response-webAppConfiguration"></a>

Type: [WebAppConfiguration](API_WebAppConfiguration.md) object

 ** [webAppUrl](#API_GetDomain_ResponseSyntax) **   <a name="connecthealth-GetDomain-response-webAppUrl"></a>

Type: String

## Errors
<a name="API_GetDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
This error is thrown when the requested resource is not found.
HTTP Status Code: 404

## See Also
<a name="API_GetDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/GetDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/GetDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/GetDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/GetDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/GetDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/GetDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/GetDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/GetDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/GetDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/GetDomain)
