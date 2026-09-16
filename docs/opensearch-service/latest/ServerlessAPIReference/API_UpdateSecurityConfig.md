---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateSecurityConfig.html
---

# UpdateSecurityConfig
<a name="API_UpdateSecurityConfig"></a>

Updates a security configuration for OpenSearch Serverless. For more information, see [SAML authentication for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html).

## Request Syntax
<a name="API_UpdateSecurityConfig_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "configVersion": "{{string}}",
   "description": "{{string}}",
   "iamFederationOptions": {
      "groupAttribute": "{{string}}",
      "userAttribute": "{{string}}"
   },
   "iamIdentityCenterOptionsUpdates": {
      "groupAttribute": "{{string}}",
      "userAttribute": "{{string}}"
   },
   "id": "{{string}}",
   "samlOptions": {
      "groupAttribute": "{{string}}",
      "metadata": "{{string}}",
      "openSearchServerlessEntityId": "{{string}}",
      "sessionTimeout": {{number}},
      "userAttribute": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateSecurityConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-UpdateSecurityConfig-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [configVersion](#API_UpdateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-UpdateSecurityConfig-request-configVersion"></a>
The version of the security configuration to be updated. You can find the most recent version of a security configuration using the `GetSecurityPolicy` command.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 36.
Pattern: `([0-9a-zA-Z+/]{4})*(([0-9a-zA-Z+/]{2}==)|([0-9a-zA-Z+/]{3}=))?`
Required: Yes

 ** [description](#API_UpdateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-UpdateSecurityConfig-request-description"></a>
A description of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [iamFederationOptions](#API_UpdateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-UpdateSecurityConfig-request-iamFederationOptions"></a>
Describes IAM federation options in the form of a key-value map for updating an existing security configuration. Use this field to modify IAM federation settings for the security configuration.
Type: [IamFederationConfigOptions](API_IamFederationConfigOptions.md) object
Required: No

 ** [iamIdentityCenterOptionsUpdates](#API_UpdateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-UpdateSecurityConfig-request-iamIdentityCenterOptionsUpdates"></a>
Describes IAM Identity Center options in the form of a key-value map.
Type: [UpdateIamIdentityCenterConfigOptions](API_UpdateIamIdentityCenterConfigOptions.md) object
Required: No

 ** [id](#API_UpdateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-UpdateSecurityConfig-request-id"></a>
The security configuration identifier. For SAML the ID will be `saml/<accountId>/<idpProviderName>`. For example, `saml/123456789123/OKTADev`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [samlOptions](#API_UpdateSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-UpdateSecurityConfig-request-samlOptions"></a>
SAML options in in the form of a key-value map.
Type: [SamlConfigOptions](API_SamlConfigOptions.md) object
Required: No

## Response Syntax
<a name="API_UpdateSecurityConfig_ResponseSyntax"></a>

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
<a name="API_UpdateSecurityConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [securityConfigDetail](#API_UpdateSecurityConfig_ResponseSyntax) **   <a name="opensearchserverless-UpdateSecurityConfig-response-securityConfigDetail"></a>
Details about the updated security configuration.
Type: [SecurityConfigDetail](API_SecurityConfigDetail.md) object

## Errors
<a name="API_UpdateSecurityConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE\_FAILED state.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Thrown when accessing or deleting a resource that does not exist.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSecurityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/UpdateSecurityConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/UpdateSecurityConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/UpdateSecurityConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/UpdateSecurityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/UpdateSecurityConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/UpdateSecurityConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/UpdateSecurityConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/UpdateSecurityConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/UpdateSecurityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/UpdateSecurityConfig)
