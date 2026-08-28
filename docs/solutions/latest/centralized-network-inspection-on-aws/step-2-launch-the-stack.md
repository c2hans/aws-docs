---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/step-2-launch-the-stack.html
---

# Step 2: Launch the stack
<a name="step-2-launch-the-stack"></a>

 Follow the step-by-step instructions in this section to configure and deploy the guidance into your account.

 **Time to deploy:** Approximately 7–10 minutes.

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and upload the file created in previous step `./deployment/global-s3-assets/centralized-network-inspection-on-aws.template`

1.  The template launches in the US East (N. Virginia) Region by default. To launch the guidance in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
 This guidance uses Network Firewall, which is not currently available in all AWS Regions. You must launch this guidance in an AWS Region where AWS Network Firewall is available. For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).
 You can deploy this guidance multiple times in the same Region to allow users to set up a new network firewall and related resources for an existing transit gateway.

1.  On the **Specify stack details** page, assign a name to your guidance stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1.  Under **Parameters**, review the parameters for this guidance template and modify them as necessary. This guidance uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/step-2-launch-the-stack.html)

1.  Select **Next**.

1.  On the **Configure stack options** page, choose **Next**.

1.  On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1.  Choose **Submit** to deploy the stack.

    You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 7–10 minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Network Inspection on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
