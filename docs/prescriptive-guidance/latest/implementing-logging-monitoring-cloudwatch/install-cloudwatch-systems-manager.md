---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/install-cloudwatch-systems-manager.html
---

# Installing the CloudWatch agent using Systems Manager
<a name="install-cloudwatch-systems-manager"></a>

You can use Systems Manager State Manager with Systems Manager Distributor to automatically install and update the CloudWatch agent on servers and EC2 instances. Distributor includes the `AmazonCloudWatchAgent` AWS managed package that installs the most recent CloudWatch agent version.

This installation approach has the following prerequisites:
+ The Systems Manager agent must be installed and running on your servers or EC2 instances. The Systems Manager agent is preinstalled on Amazon Linux, Amazon Linux 2, and some AMIs. The agent must also be installed and configured on other images or on-premises VMs and servers.
**Note**
Amazon Linux 2 is nearing end of support. For more information, see the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/).
+ An IAM role or credentials that have the [required CloudWatch and Systems Manager permissions ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent.html)must be attached to the EC2 instance or defined in the credentials file for an on-premises server. For example, you can create an IAM role that includes the AWS managed policies: AmazonSSMManagedInstanceCore for Systems Manager and CloudWatchAgentServerPolicy for CloudWatch.

You can use the [ssm-cloudwatch-instance-role.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/ssm-cloudwatch-instance-role.yaml) AWS CloudFormation template to deploy an IAM role and instance profile that includes both of these policies. This template can also be modified to include other standard IAM permissions for your EC2 instances. For on-premises servers or VMs, should configure the CloudWatch agent to use the [Systems Manager service role](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-service-role.html) that was configured for the on-premises server. For more information about this, see [How can I configure on-premises servers that use Systems Manager Agent and the unified CloudWatch agent to use only temporary credentials?](https://aws.amazon.com/premiumsupport/knowledge-center/cloudwatch-on-premises-temp-credentials/) in the AWS Knowledge Center.

The following list provides several advantages for using the Systems Manager Distributor and State Manager approach to install and maintain the CloudWatch agent:
+ **Automated installation for multiple OSs** – You don't need to write and maintain a script for each OS to download and install the CloudWatch agent.
+ **Automatic update checks** – State Manager automatically and regularly checks that each EC2 instance has the most recent CloudWatch version.
+ **Compliance reporting** – The Systems Manager compliance dashboard shows which EC2 instances failed to successfully install the Distributor package.
+ **Automated installation for newly launched EC2 instances** – New EC2 instances that are launched into your account automatically receive the CloudWatch agent.

However, you should also consider the following three areas before you choose this approach:
+ **Collision with an existing association** – If another association already installs or configures the CloudWatch agent, then the two associations might interfere with each other and potentially cause issues. When using this approach, you should remove any existing associations that install or update the CloudWatch agent and configuration.
+ **Updating custom agent configuration files** – Distributor performs an installation by using the default configuration file. If you use a custom configuration file or multiple CloudWatch configuration files, you must update the configuration after the installation.
+ **Multi-Region or multi-account setup** – The State Manager association must be set up in each account and Region. New accounts in a multi-account environment must be updated to include the State Manager association. You need to centralize or synchronize the CloudWatch configuration so that multiple accounts and Regions can retrieve and apply your required standards.

## Set up State Manager and Distributor for CloudWatch agent deployment and configuration
<a name="set-up-state-manager-and-distributor-for-cloud-watch-agent-deployment-and-configuration"></a>

You can use [Systems Manager Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html) to quickly configure Systems Manager features, including automatically installing and updating the CloudWatch agent on your EC2 instances. The Quick Setup deploys an AWS CloudFormation stack that deploys and configures Systems Manager resources based on your choices.

The following list provides two important actions that are performed by Quick Setup for automated CloudWatch agent installation and update:

1. **Create Systems Manager custom documents** – Quick Setup creates the following Systems Manager documents for use with State Manager. The document names might vary but the content remains the same:
   + CreateAndAttachIAMToInstance – Creates the AmazonSSMRoleForInstancesQuickSetup role and instance profile if they don't exist and attaches the AmazonSSMManagedInstanceCore policy to the role. This doesn't include the required CloudWatchAgentServerPolicy IAM policy. You must update this policy and update this Systems Manager document to include this policy as described in the following section.
   + InstallAndManageCloudWatchDocument – Installs the CloudWatch agent with Distributor and configures each EC2 instance one time with a default CloudWatch agent configuration using the AWS-ConfigureAWSPackage Systems Manager document.
   + UpdateCloudWatchDocument – Updates the CloudWatch agent by installing the latest CloudWatch agent using the AWS-ConfigureAWSPackage Systems Manager document. Updating or uninstalling the agent doesn't remove the existing CloudWatch configuration files from the EC2 instance.

1. **Create State Manager associations** – State Manager associations are created and configured to use the custom created Systems Manager documents. The State Manager association names might vary but the configuration remains the same:
   + ManageCloudWatchAgent – Runs the InstallAndManageCloudWatchDocument Systems Manager document one time for each EC2 instance.
   + UpdateCloudWatchAgent – Runs the UpdateCloudWatchDocument Systems Manager document every 30 days for each EC2 instance.
   + Runs the CreateAndAttachIAMToInstance Systems Manager document one time for each EC2 instance.

You must augment and customize the completed Quick Setup configuration to include

CloudWatch permissions and support custom CloudWatch configurations. In particular, the

CreateAndAttachIAMToInstance and the InstallAndManageCloudWatchDocument document will need to be updated. You can manually update the Systems Manager documents created by Quick Setup. Alternatively, you can use your own CloudFormation template to provision the same resources with the necessary updates as well as configure and deploy other Systems Manager resources and not use Quick Setup.

### Important: Quick Setup creates an AWS CloudFormation stack to deploy and configure Systems Manager resources based on your choices. If you update your Quick Setup choices, you might need to manually re-update the Systems Manager documents.
<a name="important--quick-setup-creates-an-aws-cloudformation-stack-to-deploy-and-configure-systems-manager-resources-based-on-your-choices.-if-you-update-your-quick-setup-choices--you-might-need-to-manually-re-update-the-systems-manager-documents..bf357038-3f20-5422-858b-0b125c7f9226"></a>

The following sections describe how to manually update the Systems Manager resources created by Quick Setup, as well as use your own AWS CloudFormation template to perform an updated Quick Setup. We recommend that you use your own AWS CloudFormation template to avoid manually updating resources created by Quick Setup and AWS CloudFormation.

## Use Systems Manager Quick Setup and manually update the created Systems Manager resources
<a name="use-systems-manager-quick-setup-and-manually-update-the-created-systems-manager-resources"></a>

This Systems Manager document created by Quick Setup checks whether an EC2 instance has an existing IAM instance profile attached to it. If it does, it attaches the AmazonSSMManagedInstanceCore policy to the existing role. This protects your existing EC2 instances from losing AWS permissions that might be assigned through existing instance profiles. You need to add a step in this document to attach the CloudWatchAgentServerPolicy IAM policy to EC2 instances that already have an instance profile attached. The Systems Manager document also creates the IAM role if it doesn't exist and an EC2 instance doesn't have an instance profile attached to it. You must update this section of the document to also include the CloudWatchAgentServerPolicy IAM policy.

Review the completed [CreateAndAttachIAMToInstance.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/tree/main/custom_ssm_setup) sample document and compare it to the document created by Quick Setup. Edit the existing document to include the required steps and changes. Based on your Quick Setup choices the document created by Quick Setup might be different than the provided sample document, so ensure that you make the required adjustments. The sample document includes the Quick Setup option choice to scan instances for missing patches daily and therefore includes a policy for Systems Manager Patch Manager.

### Update the InstallAndManageCloudWatchDocument Systems Manager document
<a name="update-the-installandmanagecloudwatchdocument-systems-manager-document.52c39f21-f93b-5b76-8f59-6847769148f0"></a>

This Systems Manager document created by Quick Setup installs the CloudWatch agent and configures it with the default CloudWatch agent configuration. The default CloudWatch configuration aligns to the basic, predefined metric set. You must replace the default configuration step and add steps to download your CloudWatch configuration files from your CloudWatch configuration S3 bucket.

Review the completed [InstallAndManageCloudWatchDocument.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/tree/main/custom_ssm_setup) updated document and compare it to the document created by Quick Setup. The document created by your Quick Setup might be different, so make sure that you have made the required adjustments. Edit your existing document to include the necessary steps and changes.

## Use AWS CloudFormation instead of Quick Setup
<a name="use-aws-cloud-formation-instead-of-quick-setup"></a>

Instead of using Quick Setup, you can use AWS CloudFormation to configure Systems Manager. This approach allows you to customize your Systems Manager configuration according to your specific requirements. This approach also avoids manual updates to the configured Systems Manager resources created by Quick Setup to support custom CloudWatch configurations.

The Quick Setup feature also uses AWS CloudFormation and creates a AWS CloudFormation stack set to deploy and configure Systems Manager resources based on your choices. Before you can use AWS CloudFormation stack sets, you must create the IAM roles used by AWS CloudFormation StackSets to support deployments across multiple accounts or Regions. Quick Setup creates the roles it requires to support multi-Region or multi-account deployments with AWS CloudFormation StackSets. You must complete the prerequisites for AWS CloudFormation StackSets if you want to configure and deploy Systems Manager resources in multiple Regions or multiple accounts from a single account and Region. For more information about this, see [Prerequisites for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html) in the AWS CloudFormation documentation.

Review the [AWS-QuickSetup-SSMHostMgmt.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/tree/main/custom_ssm_setup) AWS CloudFormation template for customized Quick Setup.

You should review the resources and capabilities in the AWS CloudFormation template and make adjustments according to your requirements. You should version control the AWS CloudFormation template that you use and incrementally test changes to confirm the required result. Additionally, you should perform cloud security reviews to determine if there are any policy adjustments that are required based on your organization's requirements.

You should deploy the AWS CloudFormation stack in a single test account and Region, and perform any necessary test cases to customize and confirm the desired result. You can then graduate your deployment to multiple Regions in a single account, and then to multiple accounts and multiple regions.

## Customized Quick Setup in a single account and Region with an AWS CloudFormation stack
<a name="customized-quick-setup-in-a-single-account-and-region-with-an-aws-cloud-formation-stack"></a>

If you are only use a single account and Region, you can deploy the complete example as a AWS CloudFormation stack instead of an AWS CloudFormation stack set. However if possible, we recommend that you use the multi-account, multi-Region stack set approach even if only use a single account and Region. Using AWS CloudFormation StackSets makes it easier to expand to additional accounts and Regions in the future.

Use the following steps to deploy the [AWS-QuickSetup-SSMHostMgmt.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/tree/main/custom_ssm_setup) AWS CloudFormation template as an AWS CloudFormation stack in a single account and Region:

1. Download the template and check it into your preferred version control system (for example, GitHub).

1. Customize the default AWS CloudFormation parameter values based on your organization's requirements.

1. Customize the State Manager association schedules.

1. Customize the Systems Manager document with the InstallAndManageCloudWatchDocument

logical ID. Confirm that the S3 bucket prefixes align to the prefixes for the S3 bucket containing your CloudWatch configuration.

1. Retrieve and record the Amazon Resource Name (ARN) for the S3 bucket containing your CloudWatch configurations. For more information about this, see the Storing CloudWatch configuration files in an S3 bucket  (p. 9) section of this guide. A sample [cloudwatch-config-s3-bucket.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/cloudwatch-config-s3-bucket.yaml) AWS CloudFormation template is available that includes a bucket policy to provide read access to AWS Organizations accounts.

1. Deploy the customized Quick Setup AWS CloudFormation template to the same account as your S3 bucket:
   + For the CloudWatchConfigBucketARN parameter, enter the S3 bucket's ARN.
   + Make adjustments to the parameter options depending on the capabilities that you want to enable for Systems Manager.

1. Deploy a test EC2 instance with and without an IAM role to confirm that the EC2 instance works withCloudWatch.
+ Apply the AttachIAMToInstance State Manager association. This is a Systems Manager runbook that is configured to run on a schedule. State Manager associations that use runbooks are not automatically applied to new EC2 instances and can be configured to run on a scheduled basis. For more information, see [Running automations with triggers using State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-sm-target.html) in the Systems Manager documentation.
+ Confirm that the EC2 instance has the required IAM role attached.
+ Confirm that the Systems Manager agent is working correctly by confirming that the EC2 instance is visible in Systems Manager.
+ Confirm that the CloudWatch agent is working correctly by viewing CloudWatch logs and metrics based on the CloudWatch configurations from your S3 bucket.

## Customized Quick Setup in multiple Regions and multiple accounts with AWS CloudFormation StackSets
<a name="customized-quick-setup-in-multiple-regions-and-multiple-accounts-with-aws-cloud-formation-stack-sets"></a>

If you are using multiple accounts and Regions, then you can deploy the [AWS-QuickSetupSSMHostMgmt.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/tree/main/custom_ssm_setup) AWS CloudFormation template as a stack set. You must complete the [AWS CloudFormation StackSet prerequisites](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html) before using stack sets. The requirements vary depending on whether you are deploying stack sets with [**self-managed** or **service-managed **permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html).

We recommend that you deploy stack sets with service-managed permissions so that new accounts automatically receive the customized Quick Setup. You must deploy a service-managed stack set from the AWS Organizations management account or delegated administrator account. You should deploy the stack set from a centralized account used for automation that has delegated administrator privileges, rather than the AWS Organizations management account. We also recommend that you test your stack set deployment by targeting a test organizational unit (OU) with a single or small number of accounts in one Region.

1. Complete steps 1 to 5 from the Customized Quick Setup in a single account and Region with an AWS CloudFormation stack  section of this guide.

1. Sign in to the AWS Management Console, open the AWS CloudFormation consoler and choose **Create StackSet**:
   + Choose **Template is ready** and **Upload a template file**. Upload the AWS CloudFormation template that you customized to your requirements.
   + Specify the stack set details:
   + Enter a stack set name, for example, StackSet-SSM-QuickSetup.
   + Make adjustments to the parameter options depending on the capabilities that you want to enable for Systems Manager.
   + For the CloudWatchConfigBucketARN parameter, enter the ARN for your CloudWatch configuration's S3 bucket.
   + Specify the stack set options, choose whether you will use service-managed permissions with AWS Organizations or self-managed permissions.
   + If you choose self-managed permissions, enter the

**AWSCloudFormationStackSetAdministrationRole** and

**AWSCloudFormationStackSetExecutionRole** IAM role details. The administrator role must exist in the account and the execution role must exist in each target account
+ For **service-managed** permissions with AWS Organizations, we recommend that you first deploy to a test OU instead of the entire organization.
+ Choose whether you want to enable automatic deployments. We recommend that you choose **Enabled**. For account removal behavior, the recommended setting is **Delete stacks**.
+ For **self-managed** permissions, enter the AWS account IDs for the accounts that you want to set up. You must repeat this process for each new account if you use self-managed permissions.
+ Enter the Regions where you will be using CloudWatch and Systems Manager.
+ Confirm that the deployment is successful by viewing the status in the **Operations** **and Stack instances** tab for the stack set.
+ Test that Systems Manager and CloudWatch are correctly working in the deployed accounts by following step 7 from the Customized Quick Setup in a single account and Region with an AWS CloudFormation stack (p. 23) section of this guide.

## Considerations for configuring on-premises servers
<a name="considerations-for-configuring-on-premises-servers"></a>

The CloudWatch agent for on-premises servers and VMs is installed and configured by using a similar approach to that for EC2 instances. However, the following table provides considerations that you must evaluate when installing and configuring the CloudWatch agent on on-premises servers and VMs.

|  |
| --- |
| Point the CloudWatch agent to the same temporary credentials used for Systems Manager. | When you set up Systems Manager in a hybrid environment that includes on-premises servers, you can activate Systems Manager with an IAM role. You should use the role created for your EC2 instances that includes the CloudWatchAgentServerPolicy and AmazonSSMManagedInstanceCore policies.This results in the Systems Manager agent retrieving and writing temporary credentials |
| --- |--- |
|  | to a local credentials file. You can point your CloudWatch agent configuration to the same file. You can use the process from [Configure onpremises servers that use Systems Manager agent and the unified CloudWatch agent to use only temporary credentials](https://aws.amazon.com/premiumsupport/knowledge-center/cloudwatch-on-premises-temp-credentials/) in the AWS Knowledge Center.<br />You can also automate this process by defining a separate Systems Manager Automation runbook and State Manager association, and targeting your on-premises instances with tags. When you create an [Systems Manager activation](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-activation-managed-nodes.html) for your on-premises instances, you should include a tag that identifies the instances as on-premises instances. |
| **Consider using accounts and Regions that have VPN or AWS Direct Connect access and AWS PrivateLink.** | You can use AWS Direct Connect or AWS Virtual Private Network (AWS VPN) to establish private connections between on-premises networks and your virtual private cloud (VPC). AWS PrivateLink establishes a private connection to CloudWatch Logs with an interface VPC endpoint. This approach is useful if you have restrictions that prevent data being sent over the public internet to a public service endpoint. |
| **All metrics must be included in the CloudWatch configuration file.** | Amazon EC2 includes standard metrics (for example, CPU utilization) but these metrics must be defined for on-premises instances. You can use a separate platform configuration file to define these metrics for on-premises servers and then append the configuration to the standard CloudWatch metrics configuration for the platform. |

## Considerations for ephemeral EC2 instances
<a name="considerations-for-ephemeral-ec2-instances"></a>

EC2 instances are temporary, or *ephemeral*, if they are provisioned by Amazon EC2 Auto Scaling, Amazon EMR, [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), or AWS Batch. Ephemeral EC2 instances can cause a very large number of CloudWatch streams under a common log group without additional information on their runtime origin.

If you use ephemeral EC2 instances, consider adding additional dynamic contextual information in the log group and log stream names. For example, you can include the Spot Instance request ID, Amazon EMR cluster name, or Auto Scaling group name. This information can vary for newly launched EC2 instances and you might have to retrieve and configure it at runtime. You can do this by writing a CloudWatch agent configuration file at boot and restarting the agent to include the updated configuration file. This enables delivery of logs and metrics to CloudWatch using dynamic runtime information.

You should also make sure that your metrics and logs are sent by the CloudWatch agent before your ephemeral EC2 instances are terminated. The CloudWatch agent includes a flush\_interval parameter that can be configured to define the time interval for flushing log and metric buffers. You can lower this value based on your workload and stop the CloudWatch agent and force the buffers to flush before the EC2 instance is terminated.

## Using an automated solution to deploy the CloudWatch agent
<a name="using-an-automated-solution-to-deploy-the-cloud-watch-agent"></a>

If you use an automation solution (for example, Ansible or Chef), you can leverage it to automatically install and update the CloudWatch agent. If you use this approach, you must evaluate the following considerations:
+ **Validate that the automation covers the OSs and the OS versions that you support.** If the automation script doesn't support all your organization's OSs, you should define alternative solutions for the unsupported OSs.
+ **Validate that the automation solution regularly checks for CloudWatch agent updates and upgrades**. Your automation solution should regularly check for updates to the CloudWatch agent, or regularly uninstall and reinstall the agent. You can use a scheduler or automation solution functionality to regularly check and update the agent.
+ **Validate that you can confirm agent installation and configuration compliance**. Your automation solution should enable you to determine when a system doesn't have the agent installed or when the agent isn't working. You can implement a notification or alarm into your automation solution so that failed installations and configurations are tracked.
