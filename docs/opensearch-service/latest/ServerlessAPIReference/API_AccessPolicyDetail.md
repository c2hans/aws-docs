---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_AccessPolicyDetail.html
---

# AccessPolicyDetail
<a name="API_AccessPolicyDetail"></a>

Details about an OpenSearch Serverless access policy.

## Contents
<a name="API_AccessPolicyDetail_Contents"></a>

 ** createdDate **   <a name="opensearchserverless-Type-AccessPolicyDetail-createdDate"></a>
The date the policy was created.
Type: Long
Required: No

 ** description **   <a name="opensearchserverless-Type-AccessPolicyDetail-description"></a>
The description of the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** lastModifiedDate **   <a name="opensearchserverless-Type-AccessPolicyDetail-lastModifiedDate"></a>
The timestamp of when the policy was last modified.
Type: Long
Required: No

 ** name **   <a name="opensearchserverless-Type-AccessPolicyDetail-name"></a>
The name of the policy.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** policy **   <a name="opensearchserverless-Type-AccessPolicyDetail-policy"></a>
The JSON policy document without any whitespaces.
Type: JSON value
Required: No

 ** policyVersion **   <a name="opensearchserverless-Type-AccessPolicyDetail-policyVersion"></a>
The version of the policy.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 36.
Pattern: `([0-9a-zA-Z+/]{4})*(([0-9a-zA-Z+/]{2}==)|([0-9a-zA-Z+/]{3}=))?`
Required: No

 ** type **   <a name="opensearchserverless-Type-AccessPolicyDetail-type"></a>
The type of access policy.
Type: String
Valid Values: `data`
Required: No

## See Also
<a name="API_AccessPolicyDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/AccessPolicyDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/AccessPolicyDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/AccessPolicyDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
