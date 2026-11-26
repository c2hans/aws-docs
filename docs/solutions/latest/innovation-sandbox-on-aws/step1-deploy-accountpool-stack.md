---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/step1-deploy-accountpool-stack.html
---

# Step 1: Deploy the AccountPool stack

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
  <tr><td> <b>Account Pool OU Name (Optional)</b> </td><td> {{&lt;Empty&gt;}} </td><td>A custom name for the top-level account pool organizational unit (OU). If left empty, the OU is named <code>&lt;namespace&gt;_InnovationSandboxAccountPool</code>. Changing this value on an existing deployment renames the OU in AWS Organizations. The OU ID doesn’t change.</td></tr>
  <tr><td> <b>ISB Managed Regions</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Provide a comma-separated list of AWS Regions where sandbox accounts run workloads. Include <code>us-east-1</code> to enable global services. Complete the <a href="plan-your-deployment.md#managed-opt-in-regions">managed opt-in Region prerequisites</a> before adding an opt-in Region to this list or onboarding an account. If you change this parameter after deployment, follow <a href="#update-managed-regions">Change managed Regions after deployment</a>. Example: <code>us-east-1,eu-west-1</code> </td></tr>
  <tr><td> <b>Additional Allowed Services</b> </td><td> {{&lt;Empty&gt;}} </td><td>Optional comma-separated list of additional AWS service actions to allow in sandbox accounts. Format: <code>service:action</code> (for example, <code>sts:*,support:*,tag:*</code>). CloudFormation appends these actions to the solution’s default allowed services list, and they persist across upgrades. Actions that overlap with the default list appear as duplicates in the SCP, which has no effect. The parameter rejects bare wildcards (<code> : </code>). For the full list of services allowed by default, refer to <a href="allowed-services-reference.md">Allowed services in sandbox accounts</a>.</td></tr>
  <tr><td> <b>Additional Principal Exceptions</b> </td><td> {{&lt;Empty&gt;}} </td><td>Optional comma-separated list of IAM role ARN patterns to exclude from SCP restrictions in sandbox accounts. Supports wildcard (<code> </code>) at the end of role names (for example, <code>arn:aws:iam::</code>). CloudFormation appends these patterns to the principal exception list in the Allowed Services, Restrictions, and Region Limit SCPs. The Protect ISB Resources SCP is excluded from principal exceptions to prevent modification of solution infrastructure. The parameter rejects bare wildcards (<code>arn:aws:iam::*:role/*</code>).</td></tr>
  <tr><td> <b>Bedrock Inference Profile Patterns</b> </td><td> <code>arn:aws:bedrock:*:*:inference-profile/*</code> </td><td>Comma-separated list of Amazon Bedrock inference profile ARN patterns that the Region Limit SCP exempts. These patterns let cross-Region inference reach Regions outside your managed Regions. The default allows all inference profiles. To allow fewer profiles, list specific patterns, for example, <code>arn:aws:bedrock:*:*:inference-profile/global.*</code> for global profiles. If you leave this parameter empty, the Region Limit SCP blocks all cross-Region Amazon Bedrock inference, and Sandbox Spaces can’t run models that use cross-Region inference profiles.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, review and choose to acknowledge the messages under **Capabilities and transforms**, and choose **Next**.

1. On the **Review and create** page, review and confirm the settings.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation Console in the Status column. You should receive a **CREATE\_COMPLETE** status in approximately 60 minutes.

**Note**
Always include `us-east-1` as an ISB Managed Region to enable AWS global services. For example, if you want to enable `eu-west-1`, the parameter value should be `us-east-1,eu-west-1`.

## Change managed Regions after deployment
<a name="update-managed-regions"></a>

Before adding an opt-in managed Region, set its opt-in status to `ENABLED` in the Hub account and every existing pool account. A disabled Region in the Hub account causes the Compute stack update to fail. A disabled Region in a pool account causes that account’s observability link stack instance to fail while the Compute stack succeeds.

Use the Compute stack’s **Force configuration update (optional)** (`ForceConfigurationUpdate`) parameter after you change **ISB Managed Regions** in the Account Pool stack. Changing **ISB Managed Regions** does not automatically refresh the Compute stack. You don’t need to change **Force configuration update (optional)** when you update to a new solution version, because each new template makes the Compute stack re-read the configuration of the other stacks.

Before removing a Region, clean up all resources in that Region across every sandbox account. For more information about opt-in Regions, see [Managed opt-in Regions](plan-your-deployment.md#managed-opt-in-regions).

1. Sign in to the AWS Organizations management account. In the AWS CloudFormation console, update the Account Pool stack and choose **Use existing template**.

1. Change **ISB Managed Regions** to the complete comma-separated list of Regions that the solution should manage. Always include `us-east-1`.

1. Wait until the Account Pool stack reaches `UPDATE_COMPLETE`.

1. Sign in to the Hub account. Update the Compute stack and choose **Use existing template**. Preserve its other parameter values.

1. Set **Force configuration update (optional)** to any string different from its current value, such as `2026-11-16T21:00Z`. Reusing the current value does not trigger the refresh.

1. Wait until the Compute stack reaches `UPDATE_COMPLETE`.
**Note**
The shared-configuration resolver can cache the previous Account Pool configuration for up to five minutes. If `MissingSinkError` persists after the Compute update, wait until five minutes have passed since that update. Then update the Compute stack again with another new **Force configuration update (optional)** value.

1. In the Hub account, open the `Isb-<namespace>-ObservabilityLinks` StackSet. Confirm that it has a stack instance for every pool account in each managed Region, no stack instances in removed Regions, and that every expected instance is `CURRENT` with a `SUCCEEDED` detailed status.

The Compute update reconciles this namespace’s regional observability sink policies and makes the `Isb-<namespace>-ObservabilityLinks` StackSet target the current managed Regions. When you remove a managed Region, the solution removes this namespace’s statement from the shared regional sink policy. It leaves the sink in place because observability links can remain attached and other Innovation Sandbox namespaces in the Hub account can share it.
