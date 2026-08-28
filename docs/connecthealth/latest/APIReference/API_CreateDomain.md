---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CreateDomain.html
---

# CreateDomain
<a name="API_CreateDomain"></a>

Creates a new Domain for managing HealthAgent resources.

## Request Syntax
<a name="API_CreateDomain_RequestSyntax"></a>

```
POST /domain HTTP/1.1
Content-type: application/json

{
   "kmsKeyArn": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "webAppSetupConfiguration": {
      "ehrRole": "{{string}}",
      "idcInstanceId": "{{string}}",
      "idcRegion": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDomain_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [kmsKeyArn](#API_CreateDomain_RequestSyntax) **   <a name="connecthealth-CreateDomain-request-kmsKeyArn"></a>
The ARN of the KMS key to use for encrypting data in this Domain.
Type: String
Pattern: `arn:aws:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9-]+`
Required: No

 ** [name](#API_CreateDomain_RequestSyntax) **   <a name="connecthealth-CreateDomain-request-name"></a>
The name for the new Domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [tags](#API_CreateDomain_RequestSyntax) **   <a name="connecthealth-CreateDomain-request-tags"></a>
Tags to associate with the Domain.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [webAppSetupConfiguration](#API_CreateDomain_RequestSyntax) **   <a name="connecthealth-CreateDomain-request-webAppSetupConfiguration"></a>
Configuration for the Domain web application. Optional, but if provided all fields are required.
Type: [CreateWebAppConfiguration](API_CreateWebAppConfiguration.md) object
Required: No

## Response Syntax
<a name="API_CreateDomain_ResponseSyntax"></a>

```
HTTP/1.1 201
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
   "webAppConfiguration": {
      "ehrRole": "string",
      "idcApplicationId": "string",
      "idcRegion": "string"
   },
   "webAppUrl": "string"
}
```

## Response Elements
<a name="API_CreateDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateDomain_ResponseSyntax) **   <a name="connecthealth-CreateDomain-response-arn"></a>

Type: String
Pattern: `arn:aws:health-agent:[a-z0-9-]+:[0-9]{12}:domain/(hai-|dom-)[a-z0-9]+`

 ** [createdAt](#API_CreateDomain_ResponseSyntax) **   <a name="connecthealth-CreateDomain-response-createdAt"></a>

Type: Timestamp

 ** [domainId](#API_CreateDomain_ResponseSyntax) **   <a name="connecthealth-CreateDomain-response-domainId"></a>

Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`

 ** [encryptionContext](#API_CreateDomain_ResponseSyntax) **   <a name="connecthealth-CreateDomain-response-encryptionContext"></a>

Type: [EncryptionContext](API_EncryptionContext.md) object

 ** [kmsKeyArn](#API_CreateDomain_ResponseSyntax) **   <a name="connecthealth-CreateDomain-response-kmsKeyArn"></a>

Type: String
Pattern: `arn:aws:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9-]+`

 ** [name](#API_CreateDomain_ResponseSyntax) **   <a name="connecthealth-CreateDomain-response-name"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [status](#API_CreateDomain_ResponseSyntax) **   <a name="connecthealth-CreateDomain-response-status"></a>

Type: String
Valid Values: `ACTIVE | DELETING | DELETED`

 ** [webAppConfiguration](#API_CreateDomain_ResponseSyntax) **   <a name="connecthealth-CreateDomain-response-webAppConfiguration"></a>

Type: [WebAppConfiguration](API_WebAppConfiguration.md) object

 ** [webAppUrl](#API_CreateDomain_ResponseSyntax) **   <a name="connecthealth-CreateDomain-response-webAppUrl"></a>

Type: String

## Errors
<a name="API_CreateDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

## See Also
<a name="API_CreateDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/CreateDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/CreateDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/CreateDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/CreateDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/CreateDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/CreateDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/CreateDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/CreateDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/CreateDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/CreateDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
