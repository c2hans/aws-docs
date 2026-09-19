---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/step1-deploy-accountpool-stack.html
---

# Step 1: Deploy the AccountPool stack
<a name="step1-deploy-accountpool-stack"></a>

In this step, you deploy the resources required to set up Organizational Units (OUs), Service Control Policies (SCPs), roles, and Regions.

**Important**
Ensure that you log into the **Org Management** account for deploying the AccountPool stack.

**Note**
Refer to [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions) for a list of supported AWS Regions.

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and choose the button to launch the `AccountPool` stack CloudFormation template.

 [![Launch Stack](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-AccountPool.template&redirectId=ImplementationGuide)

The template launches in the US East (N.Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box, and choose **Next**.

1. On the **Specify stack** details page, enter a stack name for your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the AWS Identity and Access Management User Guide.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Namespace</b> </td><td> {{myisb}} </td><td>The namespace for this deployment of Innovation Sandbox (must be the same for all member stacks). For example, <b>myisb</b>.</td></tr>
  <tr><td> <b>Hub Account Id</b> </td><td> {{&lt;Requires input&gt;}} </td><td>The AWS Account Id where the Innovation Sandbox Hub application (Data and Compute stacks) is (to be) deployed. This refers to the Hub account you have identified in the Prerequisites section.</td></tr>
  <tr><td> <b>Parent OU Id</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Provide the Root id or organization unit id where Innovation Sandbox OUs will be created. To find the OU Id, navigate to AWS Organizations to view the details of the OU that you would like to use.</td></tr>
  <tr><td> <b>ISB Managed Regions</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Provide a comma-separated list of AWS Regions to limit sandbox usage to specific regions. Always include <code>us-east-1</code> to enable global services. Example: <code>us-east-1,eu-west-1</code> </td></tr>
  <tr><td> <b>Additional Allowed Services</b> </td><td> {{&lt;Empty&gt;}} </td><td>Optional comma-separated list of additional AWS service actions to allow in sandbox accounts. Format: <code>service:action</code> (for example, <code>sts:*,support:*,tag:*</code>). CloudFormation appends these actions to the solution’s default allowed services list, and they persist across upgrades. Actions that overlap with the default list appear as duplicates in the SCP, which has no effect. The parameter rejects bare wildcards (<code> : </code>). For the full list of services allowed by default, refer to <a href="allowed-services-reference.md">Allowed services in sandbox accounts</a>.</td></tr>
  <tr><td> <b>Additional Principal Exceptions</b> </td><td> {{&lt;Empty&gt;}} </td><td>Optional comma-separated list of IAM role ARN patterns to exclude from SCP restrictions in sandbox accounts. Supports wildcard (<code> </code>) at the end of role names (for example, <code>arn:aws:iam::</code>). CloudFormation appends these patterns to the principal exception list in the Allowed Services, Restrictions, and Region Limit SCPs. The Protect ISB Resources SCP is excluded from principal exceptions to prevent modification of solution infrastructure. The parameter rejects bare wildcards (<code>arn:aws:iam::*:role/*</code>).</td></tr>
  <tr><td> <b>Bedrock Inference Profile Patterns</b> </td><td> {{&lt;Empty&gt;}} </td><td>Optional comma-separated list of Bedrock inference profile ARN patterns to exempt from the region deny SCP. By default (empty), the region restriction SCP blocks all cross-region Bedrock calls. To allow cross-region inference, provide one or more patterns — for example, <code>arn:aws:bedrock:*:*:inference-profile/ </code> for all profiles or <code>arn:aws:bedrock:</code> for US profiles only.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, review and choose to acknowledge the messages under **Capabilities and transforms**, and choose **Next**.

1. On the **Review and create** page, review and confirm the settings.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation Console in the Status column. You should receive a **CREATE\_COMPLETE** status in approximately 60 minutes.

**Note**
Always include `us-east-1` as an ISB Managed Region to enable AWS global services. For example, if you want to enable `eu-west-1`, the parameter value should be `us-east-1,eu-west-1`.
