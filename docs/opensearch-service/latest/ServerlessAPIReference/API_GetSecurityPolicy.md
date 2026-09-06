---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetSecurityPolicy.html
---

# GetSecurityPolicy
<a name="API_GetSecurityPolicy"></a>

Returns information about a configured OpenSearch Serverless security policy. For more information, see [Network access for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html) and [Encryption at rest for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html).

## Request Syntax
<a name="API_GetSecurityPolicy_RequestSyntax"></a>

```
{
   "name": "{{string}}",
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSecurityPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_GetSecurityPolicy_RequestSyntax) **   <a name="opensearchserverless-GetSecurityPolicy-request-name"></a>
The name of the security policy.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: Yes

 ** [type](#API_GetSecurityPolicy_RequestSyntax) **   <a name="opensearchserverless-GetSecurityPolicy-request-type"></a>
The type of security policy.
Type: String
Valid Values: `encryption | network`
Required: Yes

## Response Syntax
<a name="API_GetSecurityPolicy_ResponseSyntax"></a>

```
{
   "securityPolicyDetail": {
      "createdDate": number,
      "description": "string",
      "lastModifiedDate": number,
      "name": "string",
      "policy": JSON value,
      "policyVersion": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_GetSecurityPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [securityPolicyDetail](#API_GetSecurityPolicy_ResponseSyntax) **   <a name="opensearchserverless-GetSecurityPolicy-response-securityPolicyDetail"></a>
Details about the requested security policy.
Type: [SecurityPolicyDetail](API_SecurityPolicyDetail.md) object

## Errors
<a name="API_GetSecurityPolicy_Errors"></a>

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
<a name="API_GetSecurityPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/GetSecurityPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/GetSecurityPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/GetSecurityPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/GetSecurityPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/GetSecurityPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/GetSecurityPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/GetSecurityPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/GetSecurityPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/GetSecurityPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/GetSecurityPolicy)
