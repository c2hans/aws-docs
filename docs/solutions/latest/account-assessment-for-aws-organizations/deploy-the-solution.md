---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution uses [CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation templates specify the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the templates.

**Important**
We designed this solution to aggregate scan findings for customers. This solution does not check the validity or correctness of your underlying resource-based policies. When changing policies that allow account migration to another AWS Organization, we recommend:
Verifying that your policies work as intended before making changes.
Using IAM [Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to verify that your policies achieve your desired permissions.
Reviewing and updating the `Condition` policy element to meet your security requirements. Do not delete the `Condition` without reviewing the underlying impact.
Engaging with AWS Solutions Architects, Technical Account Managers, and AWS Professional Services to review your AWS Organizations-based dependencies identified by the solution before initiating account migration.

**Note**
Dependencies outside the scope of this solution can impact the account migration between AWS Organizations (for example, [quotas](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) for AWS Organizations, resources shared by [AWS RAM](https://aws.amazon.com/ram/), and service-managed CloudFormation [StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)).

## Deployment process overview
<a name="deployment-process-overview"></a>

**Important**
This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
To opt out of this feature, download the template, modify the CloudFormation mapping section, and then use the CloudFormation console to upload your updated template and deploy the solution. For more information, see the [Anonymized data collection](reference.md#operational-metrics) section of this guide.

Before you launch the solution, review the [cost](cost.md), [architecture](architecture-overview.md), [security](security.md), and [other considerations](plan-your-deployment.md) discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 30-45 minutes

 [Step 1: Launch the Hub stack](step-1-launch-the-hub-stack.md)
+ Launch the AWS CloudFormation template in your Hub account.
+ Enter values for the required parameters.
+ Review the other template parameters and adjust, if necessary.

 [Step 2: Launch the Spoke stack](step-2-launch-the-spoke-stack.md)
+ Launch the AWS CloudFormation template in your Spoke accounts. Consider CloudFormation StackSets to deploy at scale.
+ Enter values for the required parameters.
+ Review the other template parameters and adjust, if necessary.

 [Step 3: Launch the Org-Management stack](step-3-launch-the-orgmanagement-stack.md)
+ Launch the AWS CloudFormation template in your Organizations management account.
+ Enter values for the required parameters.
+ Review the other template parameters and adjust, if necessary.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account Assessment for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
