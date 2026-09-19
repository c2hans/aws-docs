---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/step-1.-launch-the-stack.html
---

# Step 1. Launch the stack
<a name="step-1.-launch-the-stack"></a>

This automated AWS CloudFormation template deploys the Landing Zone Accelerator on AWS in the AWS Cloud. You must complete the applicable steps in [Prerequisites](prerequisites.md) before launching the stack.

1. Sign into [AWS Management Console](https://aws.amazon.com/console) and select the button to launch `AWSAccelerator-InstallerStack` CloudFormation template. [![Launch solution](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Flanding-zone-accelerator-on-aws%2Flatest%2FAWSAccelerator-InstallerStack.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution recommends using the AWS Control Tower service, which isn’t currently available in all AWS Regions. We recommend launching this solution in an AWS Region where AWS Control Tower is available. For the most current availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. We recommend you name your stack `AWSAccelerator-InstallerStack` to match the naming convention used by additional stacks that will be created by the Landing Zone Accelerator on AWS. For information about naming character limitations, refer to [IAM and STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Source</b> </td><td> <code>github</code> </td><td>Specify the git host.</td></tr>
  <tr><td> <b>Repository Owner</b> </td><td> <code>awslabs</code> </td><td>The owner of the git repository hosting the solution code.</td></tr>
  <tr><td> <b>Repository Name</b> </td><td> <code>landing-zone-accelerator-on-aws</code> </td><td>The name of the git repository hosting the solution code.</td></tr>
  <tr><td> <b>Branch Name</b> </td><td> <code> &lt;requires input&gt; </code> </td><td>The name of the git branch to use for installation. NOTE: The Branch Name parameter defaults to the latest release branch name. To determine the branch name, navigate to the Landing Zone Accelerator on AWS GitHub branches page and choose the release branch you want to deploy. Release branch names align with the semantic versioning of our GitHub releases. New release branches will be available as the open-source project is updated with new features.</td></tr>
  <tr><td> <b>Enable Approval Stage</b> </td><td> <code>Yes</code> </td><td>Select <code>Yes</code> to add a manual approval stage to accelerator pipeline.</td></tr>
  <tr><td> <b>Manual Approval Stage notification email list</b> </td><td> <i>optional input</i> </td><td>Provide comma separated list of email IDs to receive manual approval stage notification email.</td></tr>
  <tr><td> <b> Management Account Email </b> </td><td> <code> &lt;requires input&gt; </code> </td><td>The management (primary) account email. NOTE: Use a unique email address.</td></tr>
  <tr><td> <b>LogArchive Account Email</b> </td><td> <code> &lt;requires input&gt; </code> </td><td>The log archive account email. NOTE: Use a unique email address.</td></tr>
  <tr><td> <b>Audit Account Email</b> </td><td> <code> &lt;requires input&gt; </code> </td><td>The security audit account (also referred to as the audit account). NOTE: Use a unique email address.</td></tr>
  <tr><td> <b>Control Tower Environment</b> </td><td> <code>Yes</code> </td><td>Select <code>Yes</code> if you want to deploy to an AWS Control Tower environment. Select <code>No</code> if you’re not using AWS Control Tower.</td></tr>
  <tr><td> <b>Accelerator Resource name prefix</b> </td><td> <code>AWSAccelerator</code> </td><td>The prefix value for accelerator-deployed resources. Leave the default value if you’re using the solution-defined resource name prefix. IMPORTANT: Updating this value after initial installation will cause stack failure. Non-default value cannot start with keywords <code>aws</code> or <code>ssm</code> (case insensitive). Trailing dashes (for example, <code>input-</code>) in a non-default value will be ignored.</td></tr>
  <tr><td> <b>Use Existing Config Repository</b> </td><td> <code>No</code> </td><td>Select <code>Yes</code> to deploy the solution with an existing conﬁguration repository. Leave the default value if you’re using the solution-deployed repository. NOTE: Updating this value after initial installation may cause adverse effects such as unexpected failures and resource replacements.</td></tr>
  <tr><td> <b>Existing Config Repository Name</b> </td><td> <i>optional input</i> </td><td>The name of an existing CodeCommit repository hosting the solution configuration. When the <i>Use Existing Config Repository</i> parameter is set to <code>Yes</code>, the value for this parameter must be a valid name of an existing CodeCommit repository that holds the solution configuration. NOTE: When the <b>Use Existing Config Repository</b> parameter is set to <code>Yes</code> and this parameter is empty, then the Installer stack validation will fail, which will cause stack deployment failure.</td></tr>
  <tr><td> <b>Existing Config Repository Branch Name</b> </td><td> <i>optional input</i> </td><td>The name of an existing CodeCommit repository to pull the solution configuration from. When the <i>Use Existing Config Repository</i> parameter is set to <code>Yes</code>, the value for this parameter must be a valid name of an existing CodeCommit repository that holds the solution configuration. NOTE: When the <b>Use Existing Config Repository</b> parameter is set to <code>Yes</code> and this parameter is empty, then the Installer stack validation will fail, which will cause stack deployment failure.</td></tr>
  <tr><td> <b>Enable Diagnostics Pack</b> </td><td> <code>Yes</code> </td><td>Select <code>Yes</code> to deploy the diagnostics pack tool. For more information about the diagnostics pack tool deployed by the solution, refer to <a href="diagnostics-pack.md">Diagnostics pack</a> in the Troubleshooting section.</td></tr>
  <tr><td> <b>Configuration Repository Location</b> </td><td> <code> &lt;requires input&gt; </code> </td><td>Determines where to store the LZA configuration files used to customize your landing zone. In previous versions of the solution, files were stored in CodeCommit by default.IMPORTANT: Updating this value after initial installation will cause stack failures.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next.**

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template might create IAM resources.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a `CREATE_COMPLETE` status in approximately eight minutes.
