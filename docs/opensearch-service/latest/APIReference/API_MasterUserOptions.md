---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_MasterUserOptions.html
---

# MasterUserOptions
<a name="API_MasterUserOptions"></a>

Credentials for the master user for a domain.

## Contents
<a name="API_MasterUserOptions_Contents"></a>

 ** MasterUserARN **   <a name="opensearchservice-Type-MasterUserOptions-MasterUserARN"></a>
Amazon Resource Name (ARN) for the master user. Only specify if `InternalUserDatabaseEnabled` is `false`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** MasterUserName **   <a name="opensearchservice-Type-MasterUserOptions-MasterUserName"></a>
User name for the master user. Only specify if `InternalUserDatabaseEnabled` is `true`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** MasterUserPassword **   <a name="opensearchservice-Type-MasterUserOptions-MasterUserPassword"></a>
Password for the master user. Only specify if `InternalUserDatabaseEnabled` is `true`.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 128.
Pattern: `.*`
Required: No

## See Also
<a name="API_MasterUserOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/MasterUserOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/MasterUserOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/MasterUserOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
