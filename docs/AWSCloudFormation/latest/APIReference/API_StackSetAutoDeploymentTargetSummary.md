---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_StackSetAutoDeploymentTargetSummary.html
---

# StackSetAutoDeploymentTargetSummary
<a name="API_StackSetAutoDeploymentTargetSummary"></a>

One of the targets for the StackSet. Returned by the [ListStackSetAutoDeploymentTargets](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackSetAutoDeploymentTargets.html) API operation.

## Contents
<a name="API_StackSetAutoDeploymentTargetSummary_Contents"></a>

 ** OrganizationalUnitId **
The organization root ID or organizational unit (OU) IDs where the StackSet is targeted.
Type: String
Pattern: `^(ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}|r-[a-z0-9]{4,32})$`
Required: No

 ** Regions.member.N **
The list of Regions targeted for this organization or OU.
Type: Array of strings
Pattern: `^[a-zA-Z0-9-]{1,128}$`
Required: No

## See Also
<a name="API_StackSetAutoDeploymentTargetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetAutoDeploymentTargetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetAutoDeploymentTargetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetAutoDeploymentTargetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
