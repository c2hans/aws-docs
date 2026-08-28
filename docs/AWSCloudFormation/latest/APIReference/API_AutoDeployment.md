---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_AutoDeployment.html
---

# AutoDeployment
<a name="API_AutoDeployment"></a>

Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organization or organizational unit (OU). For more information, see [Enable or disable automatic deployments for StackSets in AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-auto-deployment.html) in the * AWS CloudFormation User Guide*.

## Contents
<a name="API_AutoDeployment_Contents"></a>

 ** DependsOn.member.N **
A list of StackSet ARNs that this StackSet depends on for auto-deployment operations. When auto-deployment is triggered, operations will be sequenced to ensure all dependencies complete successfully before this StackSet's operation begins.
Type: Array of strings
Required: No

 ** Enabled **
If set to `true`, StackSets automatically deploys additional stack instances to AWS Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.
Type: Boolean
Required: No

 ** RetainStacksOnAccountRemoval **
If set to `true`, stack resources are retained when an account is removed from a target organization or OU. If set to `false`, stack resources are deleted. Specify only if `Enabled` is set to `True`.
Type: Boolean
Required: No

## See Also
<a name="API_AutoDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/AutoDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/AutoDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/AutoDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
