---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetSecurityConfig.html
---

# GetSecurityConfig
<a name="API_GetSecurityConfig"></a>

Returns information about an OpenSearch Serverless security configuration. For more information, see [SAML authentication for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html).

## Request Syntax
<a name="API_GetSecurityConfig_RequestSyntax"></a>

```
{
   "id": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSecurityConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [id](#API_GetSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-GetSecurityConfig-request-id"></a>
The unique identifier of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_GetSecurityConfig_ResponseSyntax"></a>

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
<a name="API_GetSecurityConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [securityConfigDetail](#API_GetSecurityConfig_ResponseSyntax) **   <a name="opensearchserverless-GetSecurityConfig-response-securityConfigDetail"></a>
Details of the requested security configuration.
Type: [SecurityConfigDetail](API_SecurityConfigDetail.md) object

## Errors
<a name="API_GetSecurityConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetSecurityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/GetSecurityConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/GetSecurityConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/GetSecurityConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/GetSecurityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/GetSecurityConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/GetSecurityConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/GetSecurityConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/GetSecurityConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/GetSecurityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/GetSecurityConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
