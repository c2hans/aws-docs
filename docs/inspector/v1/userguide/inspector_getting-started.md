---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector_getting-started.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Getting started with Amazon Inspector Classic
<a name="inspector_getting-started"></a>

This tutorial shows you how to set up Amazon Inspector Classic and get started by creating and running your first assessment.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## One-click setup
<a name="inspector_basic-assessment"></a>

The following procedure shows you how to create and run an automatic assessment using a pre-built template and pre-defined scheduling parameters (once a week or one time only) on all available Amazon Elastic Compute Cloud (Amazon EC2) instances in the current AWS account and AWS Region.

1. Sign in to the AWS Management Console and open the Amazon Inspector Classic console at [https://console.aws.amazon.com/inspector/](https://console.aws.amazon.com/inspector/).

1. On the **Welcome** page, choose the type of assessment that you would like to run. **Network Assessments** analyze the network configurations of your AWS environment for vulnerabilities, and do not require an Amazon Inspector Classic agent. **Host Assessments** analyze the on-host software and configurations of your EC2 instances for vulnerabilities, and require an agent to be installed on the EC2 instances.

   Choose either **Run weekly (recommended)** or **Run once**. As soon as you make your choice, the service automatically creates the assessment for you. Specifically, the service does the following:

   1. Creates a [service-linked role](inspector_slr.md).
**Note**
To identify the EC2 instances that are specified in the assessment targets, Amazon Inspector Classic needs to enumerate your EC2 instances and tags. Amazon Inspector Classic gets access to these resources in your AWS account through a service-linked role called `AWSServiceRoleForAmazonInspector`. For more information about service-linked roles, see [Using service-linked roles for Amazon Inspector Classic](inspector_slr.md) and [Using Service-Linked Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html).

   1. If applicable, installs an [Amazon Inspector Classic agent](inspector_agents.md) on all available EC2 instances in your AWS account and Region.
**Note**
The service installs an Amazon Inspector Classic agent only on those EC2 instances that allow AWS Systems Manager Run Command. To use this option, make sure that all of your EC2 instances in the current AWS account and AWS Region have the SSM Agent installed and have an IAM role that allows Run Command. For more information, see [Installing the agent on multiple EC2 instances using the Systems Manager Run Command](inspector_installing-uninstalling-agents.md#install-run-command).

   1. Adds those instances to an [assessment target](inspector_applications.md).

   1. Includes that target in an [assessment template](inspector_assessments.md) with a standardized set of rules packages.

   1. Runs the assessment weekly or only once, depending on whether you chose **Run weekly (recommended)** or **Run once**.

1. In the **Confirmation** dialog box, choose **OK**. Amazon Inspector Classic automatically runs your assessment.

## Advanced setup
<a name="inspector_custom-assessment"></a>

The following procedure shows you how to choose specific Amazon EC2 instances, rules packages, and scheduling parameters to include in an assessment target and template.

1. On the **Welcome** page, choose **Advanced setup**.

1. On the **Define an assessment target** page, enter the name of your assessment target.

1. For **All Instances**, you can keep the check box selected to include all EC2 instances in your AWS account and Region in the assessment target. If you want to choose which EC2 instances to include, clear the **All Instances** check box, and enter the **Key** and **Value** tags that are associated with the target EC2 instances. For more information about tagging your EC2 instances, see [ Tagging Your Amazon EC2 Resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html).

1. For **Install Agents**, you can keep the check box selected by default if your instances allow [System Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html). The service installs an Amazon Inspector Classic agent on all EC2 instances in the assessment target that allow AWS Systems Manager. To use this option, make sure that all of your EC2 instances in the current AWS account and AWS Region have the SSM Agent installed and have an IAM role that allows Run Command. For more information, see [Installing the agent on multiple EC2 instances using the Systems Manager Run Command](inspector_installing-uninstalling-agents.md#install-run-command). If you want to manually install the agent, see [Installing Amazon Inspector Agents](inspector_installing-uninstalling-agents.md).

1. Choose **Next**.

1. On the **Define an assessment template** page, enter the name of your assessment template.

1. For **Rules packages**, choose the rules packages to include in the assessment template. For more information about rules packages, see [Amazon Inspector Rules Packages and Rules](inspector_rule-packages.md).

1. For **Duration**, choose the duration of your assessment run.

1. (Optional) For **Assessment Schedule**, set a schedule for recurring assessment runs.

1. Choose **Next**.

1. On the **Review** page, review your choices for the assessment target and template. If you're satisfied with the configuration, choose **Create**. If you set an assessment schedule for your assessment template, the assessment automatically runs after you choose **Create**.
**Note**
To identify the EC2 instances that are specified in the assessment targets, Amazon Inspector Classic needs to enumerate your EC2 instances and tags. Amazon Inspector Classic gets access to these resources in your AWS account through a service-linked role called `AWSServiceRoleForAmazonInspector`. For more information about using service-linked roles in Amazon Inspector Classic, see [Using service-linked roles for Amazon Inspector Classic](inspector_slr.md). For detailed information about using service-linked roles, see [Using service-linked roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) in the *AWS Identity and Access Management User Guide*.

1. If you didn't set up an assessment schedule, navigate to your assessment template through the console, and then choose **Run**.

1. To track the progress of the assessment run, in the navigation pane of the console, choose **Assessment runs**, and then choose **Findings**. For more information about findings, see [Amazon Inspector Classic findings](inspector_findings.md).
