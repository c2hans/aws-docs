---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateIntegrationDetail.html
---

# CreateIntegrationDetail
<a name="API_CreateIntegrationDetail"></a>

Contains details required to create a code security integration with a specific repository provider.

## Contents
<a name="API_CreateIntegrationDetail_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** gitlabSelfManaged **   <a name="inspector2-Type-CreateIntegrationDetail-gitlabSelfManaged"></a>
Details specific to creating an integration with a self-managed GitLab instance.
Type: [CreateGitLabSelfManagedIntegrationDetail](API_CreateGitLabSelfManagedIntegrationDetail.md) object
Required: No

## See Also
<a name="API_CreateIntegrationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CreateIntegrationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CreateIntegrationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CreateIntegrationDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
