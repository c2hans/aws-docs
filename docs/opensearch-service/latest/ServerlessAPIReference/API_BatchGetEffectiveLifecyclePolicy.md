---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetEffectiveLifecyclePolicy.html
---

# BatchGetEffectiveLifecyclePolicy
<a name="API_BatchGetEffectiveLifecyclePolicy"></a>

Returns a list of successful and failed retrievals for the OpenSearch Serverless indexes. For more information, see [Viewing data lifecycle policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list).

## Request Syntax
<a name="API_BatchGetEffectiveLifecyclePolicy_RequestSyntax"></a>

```
{
   "resourceIdentifiers": [
      {
         "resource": "{{string}}",
         "type": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_BatchGetEffectiveLifecyclePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceIdentifiers](#API_BatchGetEffectiveLifecyclePolicy_RequestSyntax) **   <a name="opensearchserverless-BatchGetEffectiveLifecyclePolicy-request-resourceIdentifiers"></a>
The unique identifiers of policy types and resource names.
Type: Array of [LifecyclePolicyResourceIdentifier](API_LifecyclePolicyResourceIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_BatchGetEffectiveLifecyclePolicy_ResponseSyntax"></a>

```
{
   "effectiveLifecyclePolicyDetails": [
      {
         "noMinRetentionPeriod": boolean,
         "policyName": "string",
         "resource": "string",
         "resourceType": "string",
         "retentionPeriod": "string",
         "type": "string"
      }
   ],
   "effectiveLifecyclePolicyErrorDetails": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "resource": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetEffectiveLifecyclePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [effectiveLifecyclePolicyDetails](#API_BatchGetEffectiveLifecyclePolicy_ResponseSyntax) **   <a name="opensearchserverless-BatchGetEffectiveLifecyclePolicy-response-effectiveLifecyclePolicyDetails"></a>
A list of lifecycle policies applied to the OpenSearch Serverless indexes.
Type: Array of [EffectiveLifecyclePolicyDetail](API_EffectiveLifecyclePolicyDetail.md) objects

 ** [effectiveLifecyclePolicyErrorDetails](#API_BatchGetEffectiveLifecyclePolicy_ResponseSyntax) **   <a name="opensearchserverless-BatchGetEffectiveLifecyclePolicy-response-effectiveLifecyclePolicyErrorDetails"></a>
A list of resources for which retrieval failed.
Type: Array of [EffectiveLifecyclePolicyErrorDetail](API_EffectiveLifecyclePolicyErrorDetail.md) objects

## Errors
<a name="API_BatchGetEffectiveLifecyclePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetEffectiveLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/BatchGetEffectiveLifecyclePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/BatchGetEffectiveLifecyclePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/BatchGetEffectiveLifecyclePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/BatchGetEffectiveLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/BatchGetEffectiveLifecyclePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/BatchGetEffectiveLifecyclePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/BatchGetEffectiveLifecyclePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/BatchGetEffectiveLifecyclePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/BatchGetEffectiveLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/BatchGetEffectiveLifecyclePolicy)
