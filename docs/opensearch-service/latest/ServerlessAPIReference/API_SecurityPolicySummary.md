---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_SecurityPolicySummary.html
---

# SecurityPolicySummary
<a name="API_SecurityPolicySummary"></a>

A summary of a security policy for OpenSearch Serverless.

## Contents
<a name="API_SecurityPolicySummary_Contents"></a>

 ** createdDate **   <a name="opensearchserverless-Type-SecurityPolicySummary-createdDate"></a>
The date the policy was created.
Type: Long
Required: No

 ** description **   <a name="opensearchserverless-Type-SecurityPolicySummary-description"></a>
The description of the security policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** lastModifiedDate **   <a name="opensearchserverless-Type-SecurityPolicySummary-lastModifiedDate"></a>
The timestamp of when the policy was last modified.
Type: Long
Required: No

 ** name **   <a name="opensearchserverless-Type-SecurityPolicySummary-name"></a>
The name of the policy.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** policyVersion **   <a name="opensearchserverless-Type-SecurityPolicySummary-policyVersion"></a>
The version of the policy.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 36.
Pattern: `([0-9a-zA-Z+/]{4})*(([0-9a-zA-Z+/]{2}==)|([0-9a-zA-Z+/]{3}=))?`
Required: No

 ** type **   <a name="opensearchserverless-Type-SecurityPolicySummary-type"></a>
The type of security policy.
Type: String
Valid Values: `encryption | network`
Required: No

## See Also
<a name="API_SecurityPolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/SecurityPolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/SecurityPolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/SecurityPolicySummary)
