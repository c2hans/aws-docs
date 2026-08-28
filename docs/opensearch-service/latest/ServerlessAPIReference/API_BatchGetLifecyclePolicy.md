---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetLifecyclePolicy.html
---

# BatchGetLifecyclePolicy
<a name="API_BatchGetLifecyclePolicy"></a>

Returns one or more configured OpenSearch Serverless lifecycle policies. For more information, see [Viewing data lifecycle policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list).

## Request Syntax
<a name="API_BatchGetLifecyclePolicy_RequestSyntax"></a>

```
{
   "identifiers": [
      {
         "name": "{{string}}",
         "type": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_BatchGetLifecyclePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identifiers](#API_BatchGetLifecyclePolicy_RequestSyntax) **   <a name="opensearchserverless-BatchGetLifecyclePolicy-request-identifiers"></a>
The unique identifiers of policy types and policy names.
Type: Array of [LifecyclePolicyIdentifier](API_LifecyclePolicyIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 40 items.
Required: Yes

## Response Syntax
<a name="API_BatchGetLifecyclePolicy_ResponseSyntax"></a>

```
{
   "lifecyclePolicyDetails": [
      {
         "createdDate": number,
         "description": "string",
         "lastModifiedDate": number,
         "name": "string",
         "policy": JSON value,
         "policyVersion": "string",
         "type": "string"
      }
   ],
   "lifecyclePolicyErrorDetails": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "name": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetLifecyclePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecyclePolicyDetails](#API_BatchGetLifecyclePolicy_ResponseSyntax) **   <a name="opensearchserverless-BatchGetLifecyclePolicy-response-lifecyclePolicyDetails"></a>
A list of lifecycle policies matched to the input policy name and policy type.
Type: Array of [LifecyclePolicyDetail](API_LifecyclePolicyDetail.md) objects

 ** [lifecyclePolicyErrorDetails](#API_BatchGetLifecyclePolicy_ResponseSyntax) **   <a name="opensearchserverless-BatchGetLifecyclePolicy-response-lifecyclePolicyErrorDetails"></a>
A list of lifecycle policy names and policy types for which retrieval failed.
Type: Array of [LifecyclePolicyErrorDetail](API_LifecyclePolicyErrorDetail.md) objects

## Errors
<a name="API_BatchGetLifecyclePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/BatchGetLifecyclePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/BatchGetLifecyclePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/BatchGetLifecyclePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/BatchGetLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/BatchGetLifecyclePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/BatchGetLifecyclePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/BatchGetLifecyclePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/BatchGetLifecyclePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/BatchGetLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/BatchGetLifecyclePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
