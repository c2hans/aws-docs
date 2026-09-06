---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteSecurityConfig.html
---

# DeleteSecurityConfig
<a name="API_DeleteSecurityConfig"></a>

Deletes a security configuration for OpenSearch Serverless. For more information, see [SAML authentication for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html).

## Request Syntax
<a name="API_DeleteSecurityConfig_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "id": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSecurityConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_DeleteSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-DeleteSecurityConfig-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [id](#API_DeleteSecurityConfig_RequestSyntax) **   <a name="opensearchserverless-DeleteSecurityConfig-request-id"></a>
The security configuration identifier. For SAML the ID will be `saml/<accountId>/<idpProviderName>`. For example, `saml/123456789123/OKTADev`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Elements
<a name="API_DeleteSecurityConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteSecurityConfig_Errors"></a>

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
<a name="API_DeleteSecurityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/DeleteSecurityConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/DeleteSecurityConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/DeleteSecurityConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/DeleteSecurityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/DeleteSecurityConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/DeleteSecurityConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/DeleteSecurityConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/DeleteSecurityConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/DeleteSecurityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/DeleteSecurityConfig)
