---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_UpdateCloudFormationCollectionFilter.html
---

# UpdateCloudFormationCollectionFilter
<a name="API_UpdateCloudFormationCollectionFilter"></a>

 Contains the names of AWS CloudFormation stacks used to update a collection of stacks. You can specify up to 1000 AWS CloudFormation stacks.

## Contents
<a name="API_UpdateCloudFormationCollectionFilter_Contents"></a>

 ** StackNames **   <a name="DevOpsGuru-Type-UpdateCloudFormationCollectionFilter-StackNames"></a>
 An array of the names of the AWS CloudFormation stacks to update. You can specify up to 1000 AWS CloudFormation stacks.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z*]+[a-zA-Z0-9-]*$`
Required: No

## See Also
<a name="API_UpdateCloudFormationCollectionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/UpdateCloudFormationCollectionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/UpdateCloudFormationCollectionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/UpdateCloudFormationCollectionFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
