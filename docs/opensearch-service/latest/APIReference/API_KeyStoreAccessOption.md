---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_KeyStoreAccessOption.html
---

# KeyStoreAccessOption
<a name="API_KeyStoreAccessOption"></a>

The configuration parameters to enable access to the key store required by the package.

## Contents
<a name="API_KeyStoreAccessOption_Contents"></a>

 ** KeyStoreAccessEnabled **   <a name="opensearchservice-Type-KeyStoreAccessOption-KeyStoreAccessEnabled"></a>
This indicates whether Key Store access is enabled
Type: Boolean
Required: Yes

 ** KeyAccessRoleArn **   <a name="opensearchservice-Type-KeyStoreAccessOption-KeyAccessRoleArn"></a>
Role ARN to access the KeyStore Key
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):iam::[0-9]+:role\/.*`
Required: No

## See Also
<a name="API_KeyStoreAccessOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/KeyStoreAccessOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/KeyStoreAccessOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/KeyStoreAccessOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
