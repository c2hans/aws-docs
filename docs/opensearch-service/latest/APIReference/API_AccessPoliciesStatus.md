---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AccessPoliciesStatus.html
---

# AccessPoliciesStatus
<a name="API_AccessPoliciesStatus"></a>

The configured access rules for the domain's search endpoint, and the current status of those rules.

## Contents
<a name="API_AccessPoliciesStatus_Contents"></a>

 ** Options **   <a name="opensearchservice-Type-AccessPoliciesStatus-Options"></a>
The access policy configured for the domain. Access policies can be resource-based, IP-based, or IAM-based. For more information, see [Configuring access policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-access-policies).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 102400.
Pattern: `.*`
Required: Yes

 ** Status **   <a name="opensearchservice-Type-AccessPoliciesStatus-Status"></a>
The status of the access policy for the domain.
Type: [OptionStatus](API_OptionStatus.md) object
Required: Yes

## See Also
<a name="API_AccessPoliciesStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AccessPoliciesStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AccessPoliciesStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AccessPoliciesStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
