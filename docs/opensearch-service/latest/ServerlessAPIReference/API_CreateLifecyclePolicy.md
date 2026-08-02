---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateLifecyclePolicy.html
---

# CreateLifecyclePolicy
<a name="API_CreateLifecyclePolicy"></a>

Creates a lifecyle policy to be applied to OpenSearch Serverless indexes. Lifecycle policies define the number of days or hours to retain the data on an OpenSearch Serverless index. For more information, see [Creating data lifecycle policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-create).

## Request Syntax
<a name="API_CreateLifecyclePolicy_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "policy": "{{string}}",
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateLifecyclePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="opensearchserverless-CreateLifecyclePolicy-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [description](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="opensearchserverless-CreateLifecyclePolicy-request-description"></a>
A description of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [name](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="opensearchserverless-CreateLifecyclePolicy-request-name"></a>
The name of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: Yes

 ** [policy](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="opensearchserverless-CreateLifecyclePolicy-request-policy"></a>
The JSON policy document to use as the content for the lifecycle policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Pattern: `.*[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+.*`
Required: Yes

 ** [type](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="opensearchserverless-CreateLifecyclePolicy-request-type"></a>
The type of lifecycle policy.
Type: String
Valid Values: `retention`
Required: Yes

## Response Syntax
<a name="API_CreateLifecyclePolicy_ResponseSyntax"></a>

```
{
   "lifecyclePolicyDetail": {
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
<a name="API_CreateLifecyclePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecyclePolicyDetail](#API_CreateLifecyclePolicy_ResponseSyntax) **   <a name="opensearchserverless-CreateLifecyclePolicy-response-lifecyclePolicyDetail"></a>
Details about the created lifecycle policy.
Type: [LifecyclePolicyDetail](API_LifecyclePolicyDetail.md) object

## Errors
<a name="API_CreateLifecyclePolicy_Errors"></a>

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
<a name="API_CreateLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/CreateLifecyclePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/CreateLifecyclePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CreateLifecyclePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/CreateLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CreateLifecyclePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/CreateLifecyclePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/CreateLifecyclePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/CreateLifecyclePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/CreateLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CreateLifecyclePolicy)
