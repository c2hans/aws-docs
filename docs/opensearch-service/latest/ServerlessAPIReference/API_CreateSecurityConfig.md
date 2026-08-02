---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateSecurityConfig.html
---

# CreateSecurityConfig
<a name="API_CreateSecurityConfig"></a>

Specifies a security configuration for OpenSearch Serverless. For more information, see [SAML authentication for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html).

## Request Syntax
<a name="API_CreateSecurityConfig_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "iamFederationOptions": {
      "groupAttribute": "{{string}}",
      "userAttribute": "{{string}}"
   },
   "iamIdentityCenterOptions": {
      "groupAttribute": "{{string}}",
      "instanceArn": "{{string}}",
      "userAttribute": "{{string}}"
   },
   "name": "{{string}}",
   "samlOptions": {
      "groupAttribute": "{{string}}",
      "metadata": "{{string}}",
      "openSearchServerlessEntityId": "{{string}}",
      "sessionTimeout": {{number}},
      "userAttribute": "{{string}}"
   },
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateSecurityConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-CreateSecurityConfig-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [description](#API_CreateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-CreateSecurityConfig-request-description"></a>
A description of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [iamFederationOptions](#API_CreateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-CreateSecurityConfig-request-iamFederationOptions"></a>
Describes IAM federation options in the form of a key-value map. This field is required if you specify `iamFederation` for the `type` parameter.
Type: [IamFederationConfigOptions](API_IamFederationConfigOptions.md) object
Required: No

 ** [iamIdentityCenterOptions](#API_CreateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-CreateSecurityConfig-request-iamIdentityCenterOptions"></a>
Describes IAM Identity Center options in the form of a key-value map. This field is required if you specify `iamidentitycenter` for the `type` parameter.
Type: [CreateIamIdentityCenterConfigOptions](API_CreateIamIdentityCenterConfigOptions.md) object
Required: No

 ** [name](#API_CreateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-CreateSecurityConfig-request-name"></a>
The name of the security configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: Yes

 ** [samlOptions](#API_CreateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-CreateSecurityConfig-request-samlOptions"></a>
Describes SAML options in the form of a key-value map. This field is required if you specify `SAML` for the `type` parameter.
Type: [SamlConfigOptions](API_SamlConfigOptions.md) object
Required: No

 ** [type](#API_CreateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-CreateSecurityConfig-request-type"></a>
The type of security configuration.
Type: String
Valid Values: `saml | iamidentitycenter | iamfederation`
Required: Yes

## Response Syntax
<a name="API_CreateSecurityConfig_ResponseSyntax"></a>

```
{
   "securityConfigDetail": {
      "configVersion": "string",
      "createdDate": number,
      "description": "string",
      "iamFederationOptions": {
         "groupAttribute": "string",
         "userAttribute": "string"
      },
      "iamIdentityCenterOptions": {
         "applicationArn": "string",
         "applicationDescription": "string",
         "applicationName": "string",
         "groupAttribute": "string",
         "instanceArn": "string",
         "userAttribute": "string"
      },
      "id": "string",
      "lastModifiedDate": number,
      "samlOptions": {
         "groupAttribute": "string",
         "metadata": "string",
         "openSearchServerlessEntityId": "string",
         "sessionTimeout": number,
         "userAttribute": "string"
      },
      "type": "string"
   }
}
```

## Response Elements
<a name="API_CreateSecurityConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [securityConfigDetail](#API_CreateSecurityConfig_ResponseSyntax) **   <a name="opensearchserverless-CreateSecurityConfig-response-securityConfigDetail"></a>
Details about the created security configuration.
Type: [SecurityConfigDetail](API_SecurityConfigDetail.md) object

## Errors
<a name="API_CreateSecurityConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE\_FAILED state.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Thrown when you attempt to create more resources than the service allows based on service quotas.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_CreateSecurityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/CreateSecurityConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/CreateSecurityConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CreateSecurityConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/CreateSecurityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CreateSecurityConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/CreateSecurityConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/CreateSecurityConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/CreateSecurityConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/CreateSecurityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CreateSecurityConfig)
