---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetPoliciesStats.html
---

# GetPoliciesStats
<a name="API_GetPoliciesStats"></a>

Returns statistical information about your OpenSearch Serverless access policies, security configurations, and security policies.

## Response Syntax
<a name="API_GetPoliciesStats_ResponseSyntax"></a>

```
{
   "AccessPolicyStats": {
      "DataPolicyCount": number
   },
   "LifecyclePolicyStats": {
      "RetentionPolicyCount": number
   },
   "SecurityConfigStats": {
      "SamlConfigCount": number
   },
   "SecurityPolicyStats": {
      "EncryptionPolicyCount": number,
      "NetworkPolicyCount": number
   },
   "TotalPolicyCount": number
}
```

## Response Elements
<a name="API_GetPoliciesStats_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessPolicyStats](#API_GetPoliciesStats_ResponseSyntax) **   <a name="opensearchserverless-GetPoliciesStats-response-AccessPolicyStats"></a>
Information about the data access policies in your account.
Type: [AccessPolicyStats](API_AccessPolicyStats.md) object

 ** [LifecyclePolicyStats](#API_GetPoliciesStats_ResponseSyntax) **   <a name="opensearchserverless-GetPoliciesStats-response-LifecyclePolicyStats"></a>
Information about the lifecycle policies in your account.
Type: [LifecyclePolicyStats](API_LifecyclePolicyStats.md) object

 ** [SecurityConfigStats](#API_GetPoliciesStats_ResponseSyntax) **   <a name="opensearchserverless-GetPoliciesStats-response-SecurityConfigStats"></a>
Information about the security configurations in your account.
Type: [SecurityConfigStats](API_SecurityConfigStats.md) object

 ** [SecurityPolicyStats](#API_GetPoliciesStats_ResponseSyntax) **   <a name="opensearchserverless-GetPoliciesStats-response-SecurityPolicyStats"></a>
Information about the security policies in your account.
Type: [SecurityPolicyStats](API_SecurityPolicyStats.md) object

 ** [TotalPolicyCount](#API_GetPoliciesStats_ResponseSyntax) **   <a name="opensearchserverless-GetPoliciesStats-response-TotalPolicyCount"></a>
The total number of OpenSearch Serverless security policies and configurations in your account.
Type: Long

## Errors
<a name="API_GetPoliciesStats_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

## See Also
<a name="API_GetPoliciesStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/GetPoliciesStats)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/GetPoliciesStats)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/GetPoliciesStats)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/GetPoliciesStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/GetPoliciesStats)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/GetPoliciesStats)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/GetPoliciesStats)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/GetPoliciesStats)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/GetPoliciesStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/GetPoliciesStats)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
