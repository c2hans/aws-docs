---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-chatops-solution-to-manage-sast-scan-results.html
---

# Deploy a ChatOps solution to manage SAST scan results by using Amazon Q Developer in chat applications custom actions and CloudFormation
<a name="deploy-chatops-solution-to-manage-sast-scan-results"></a>

*Anand Bukkapatnam Tirumala, Amazon Web Services*

## Summary
<a name="deploy-chatops-solution-to-manage-sast-scan-results-summary"></a>

This pattern presents a comprehensive solution that uses Amazon Q Developer in chat applications to streamline the management of static application security testing (SAST) scan failures reported through SonarQube. This innovative approach integrates custom actions and notifications into a conversational interface, enabling efficient collaboration and decision-making processes within development teams.

In today's fast-paced software development environment, managing SAST scan results efficiently is crucial for maintaining code quality and security. However, many organizations face the following significant challenges:
+ Delayed awareness of critical vulnerabilities because of inefficient notification systems
+ Slow decision-making processes caused by disconnected approval workflows
+ Lack of immediate, actionable responses to SAST scan failures
+ Fragmented communication and collaboration around security findings
+ Time-consuming and error-prone manual infrastructure setup for security tooling

These issues often lead to increased security risks, delayed releases, and reduced team productivity. To address these challenges effectively requires a solution that can streamline SAST result management, enhance team collaboration, and automate infrastructure provisioning.

Key features of the solution include:
+ **Customized notifications** – Real-time alerts and notifications are delivered directly to team chat channels, ensuring prompt awareness and action on SAST scan vulnerabilities or failures.
+ **Conversational approvals** – Stakeholders can initiate and complete approval workflows for SAST scan results seamlessly within the chat interface, accelerating decision-making processes.
+ **Custom actions** – Teams can define and execute custom actions based on SAST scan outcomes, such as automatically triggering email messages for quality gate failures, enhancing responsiveness to security issues.
+ **Centralized collaboration** – All SAST scan-related discussions, decisions, and actions are kept within a unified chat environment, fostering improved collaboration and knowledge-sharing among team members.
+ **Infrastructure as code (IaC)** – The entire solution is wrapped with AWS CloudFormation templates, enabling faster and more reliable infrastructure provisioning while reducing manual setup errors.

## Prerequisites and limitations
<a name="deploy-chatops-solution-to-manage-sast-scan-results-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An AWS Identity and Access Management (IAM) role with permissions to create and manage resources associated with the AWS services listed in [Tools](#deploy-chatops-solution-to-manage-sast-scan-results-tools).
+ A Slack workspace.
+ Amazon Q Developer in chat applications added to the required Slack workspace as a plugin. For more information, see [Add apps to your Slack workspace](https://slack.com/intl/en-in/help/articles/202035138-Add-apps-to-your-Slack-workspace) in the Slack documentation. Keep a note of the Slack workspace ID as shown on the AWS Management Console after successful registration.
+ A configured Amazon Q Developer in chat applications client, with the workspace ID readily available for input in the CloudFormation console. For instructions, see [Configure a Slack client](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html#slack-client-setup) in the *Amazon Q Developer in chat applications Administrator Guide*.
+ A source email account that is created and verified in Amazon Simple Email Service (Amazon SES) to send out approval email messages. For setup instructions, see [Creating and verifying email identities](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#verify-email-addresses-procedure) in the *Amazon Simple Email Service Developer Guide*.
+ A destination email address for receiving approval notifications. This address can be a shared inbox or a specific team distribution list.
+ An operational SonarQube instance that’s accessible from your AWS account. For more information, see the [SonarQube installation instructions](https://docs.sonarsource.com/sonarqube/latest/setup-and-upgrade/install-the-server/introduction/).
+ A SonarQube [user token](https://docs.sonarsource.com/sonarqube-server/latest/user-guide/managing-tokens/) with permissions to trigger and create projects through the pipeline.

**Limitations**
+ The creation of custom action buttons is a manual process in this solution.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="deploy-chatops-solution-to-manage-sast-scan-results-architecture"></a>

The following diagram shows the workflow and architecture components for this pattern.

![Workflow to deploy automated code quality assurance for release management using Amazon Q Developer.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/198312ed-e379-49a7-b706-8e79e2142f21/images/a977924c-957e-4f91-99d6-ed790e343ea6.png)

The diagram shows the automated code quality assurance workflow:

1. Code preparation and upload:
   + The developer compresses the codebase into a .zip file.
   + The developer manually uploads the .zip file to a designated Amazon Simple Storage Service (Amazon S3) bucket.

1. Amazon S3 event trigger and AWS Step Functions orchestration:
   + The Amazon S3 upload event triggers a Step Functions workflow.
   + Step Functions orchestrates a SAST scan using SonarQube.
   + The workflow monitors the AWS CodeBuild job status to determine next actions. If CodeBuild succeeds (quality gate pass), the workflow terminates. If CodeBuild fails, an AWS Lambda function is invoked for diagnostics. For more details, see **AWS Step Functions logic** later in this section.

1. AWS CodeBuild execution:
   + The CodeBuild job executes a SonarQube scan on the uploaded codebase.
   + Scan artifacts are stored in a separate Amazon S3 bucket for auditing and analysis.

1. Failure analysis (Lambda function):
   + On CodeBuild failure, the `CheckBuildStatus` Lambda function is triggered.
   + On CodeBuild success, the process is terminated and no further action is needed.

1. Lambda function analyzes failure cause (quality gate failure or other issues)
   + The `CheckBuildStatus` function creates a custom payload with detailed failure information.
   + The `CheckBuildStatus` function publishes the custom payload to an Amazon Simple Notification Service (Amazon SNS) topic.

1. Notification system:
   + Amazon SNS forwards the payload to Amazon Q Developer in chat applications for Slack integration.

1. Slack integration:
   + Amazon Q Developer in chat applications posts a notification in the designated Slack channel.

1. Approval process:
   + Approvers review the failure details in the Slack notification.
   + Approvers can initiate approval using the **Approve** button in Slack.

1. Approval handler:
   + An Approval Lambda function processes the approval action from Slack.
   + The Approval function publishes the custom message to Amazon SES.

1. Message generated:
   + The Approval function generates a custom message for developer notification.

1. Developer notification:
   + Amazon SES sends an email message to the developer with next steps or required actions.

This workflow combines manual code upload with automated quality checks, provides immediate feedback through Slack, and allows for human intervention when necessary, ensuring a robust and flexible code review process.

**AWS Step Functions logic**

As shown in the previous architecture diagram, if the quality gate pass on SonarQube fails, the workflow goes to the `CheckBuildStatus` Lambda function. The `CheckBuildStatus` function triggers a notification on the Slack channel. Each notification includes information with suggested next steps. Following are the types of notifications:
+ **Application has failed in code security scan** – The user receives this notification when the uploaded code did not pass the SonarQube security scan. The user can choose **APPROVE** to accept the build. However, the notification advises the user to beware of potential poor code quality and security risks. The notification includes the following details:
  + Next steps: Error: Quality gate status: FAILED – View details at the provided URL.
  + Triage the vulnerabilities as mentioned in the document at the provided URL.
  + CodeBuild details are available at the location at the provided URL.
+ **Application scan pipeline has failed because of some other reason** – The user receives this notification when the pipeline failed for some reason other than failing the code security scan. The notification includes the following details:
  + For next steps, go to the link provided for further troubleshooting.

To see screenshots of the notifications as they appear in a Slack channel, go to the [assets folder](https://github.com/aws-samples/chatops-slack/tree/main/assets) in the GitHub chatops-slack repository.

The following diagram shows an example of Step Functions step status after the quality gate pass fails.

![Workflow of AWS Step Functions step status after quality gate pass fails.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/198312ed-e379-49a7-b706-8e79e2142f21/images/40b7ebf0-2518-4413-9717-0bfb7559adde.png)

## Tools
<a name="deploy-chatops-solution-to-manage-sast-scan-results-tools"></a>

**AWS services**
+ [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) enables you to use Amazon Chime, Microsoft Teams, and Slack chat channels to monitor and respond to operational events in your AWS applications. *End of support notice:* On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [Amazon Simple Email Service (Amazon SES)](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html) helps you send and receive email messages by using your own email addresses and domains.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.

**Other tools**
+ [Slack](https://slack.com/help/articles/115004071768-What-is-Slack-), a Salesforce offering, is an AI-powered conversational platform that provides chat and video collaboration, automates processes with no code, and supports information sharing.
+ [SonarQube](https://docs.sonarsource.com/sonarqube/latest/user-guide/user-account/generating-and-using-tokens/) is an on-premises analysis tool designed to detect coding issues in over 30 languages, frameworks, and IaC platforms.

**Code repository**

The code for this pattern is available in the GitHub [chatops-slack](https://github.com/aws-samples/chatops-slack) repository.

## Best practices
<a name="deploy-chatops-solution-to-manage-sast-scan-results-best-practices"></a>
+ **CloudFormation stack management** – If you encounter any failures during CloudFormation stack execution, we recommend that you delete the failed stack. Then, re-create it with the correct parameter values. This approach supports a clean deployment and helps avoid potential conflicts or partial implementations.
+ **Shared inbox email configuration** – When you configure the `SharedInboxEmail` parameter, use a common distribution list that’s accessible to all relevant developers. This approach promotes transparency and helps important notifications reach the relevant team members.
+ **Production approval workflow** – For production environments, restrict access to the Slack channel that’s used for build approvals. Only designated approvers should be members of this channel. This practice maintains a clear chain of responsibility and enhances security by limiting who can approve critical changes.
+ **IAM permissions** – Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPracticesAndUseCases.html) in the IAM documentation.

## Epics
<a name="deploy-chatops-solution-to-manage-sast-scan-results-epics"></a>

### Perform initial setup
<a name="perform-initial-setup"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone the [chatops-slack](https://github.com/aws-samples/chatops-slack) repository for this pattern, use the following command.<br />`git clone "git@github.com:aws-samples/chatops-slack.git"` | AWS DevOps, Build lead, DevOps engineer, Cloud administrator |
| Create the .zip files that contain Lambda code. | Create the .zip files for the AWS Lambda function code for the `CheckBuildStatus` and `ApprovalEmail` functionality. To create `notification.zip` and `approval.zip`, use the following commands.<pre>cd chatops-slack/src</pre><pre>chmod -R 775 *</pre><pre>zip -r approval.zip approval</pre><pre>zip -r notification.zip notification</pre> | AWS DevOps, Build lead, DevOps engineer, Cloud administrator |

### Deploy the pre-requisite.yml stack file
<a name="deploy-the-pre-requisite-yml-stack-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Execute the `pre-requisite.yml` stack file. | The `pre-requisite.yml` CloudFormation stack file deploys the initial resources that are required before you execute the `app-security.yml` stack file. To execute the `pre-requisite.yml` file, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-chatops-solution-to-manage-sast-scan-results.html) | AWS administrator, AWS DevOps, Build lead, DevOps engineer |
| Upload the .zip files to the Amazon S3 bucket. | Upload the `notification.zip` and `approval.zip` files that you created earlier to the Amazon S3 bucket named `S3LambdaBucket`. The `app-security.yml` CloudFormation stack file uses `S3LambdaBucket` to provision the Lambda function. | AWS DevOps, Build lead, DevOps engineer, AWS systems administrator |

### Execute the app-security.yml stack file
<a name="execute-the-app-security-yml-stack-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Execute the `app-security.yml` stack file. | The `app-security.yml` stack files deploys the remaining infrastructure for the notification and the approval system. To execute the `app-security.yml` file, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-chatops-solution-to-manage-sast-scan-results.html) | AWS DevOps, AWS systems administrator, DevOps engineer, Build lead |
| Test the notification setup. | To test the notification setup, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-chatops-solution-to-manage-sast-scan-results.html)<br />After the test message is delivered successfully, you should see a notification on the Slack channel. For more information, see [Test notifications from AWS services to Slack](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html#test-notifications-slack) in the *Amazon Q Developer in chat applications Administrator Guide.* | AWS DevOps, AWS systems administrator, DevOps engineer, Build lead |

### Set up approval flow
<a name="set-up-approval-flow"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure custom Lambda action. | To set up the custom AWS Lambda action, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-chatops-solution-to-manage-sast-scan-results.html) | AWS administrator, AWS DevOps, Build lead, DevOps engineer, Slack Admin |
| Validate approval flow. | To validate that the approval flow works as expected, choose the **Approve** button in Slack.<br />Slackbot should send a notification on the message thread with the confirmation string **Approval Email sent successfully**. | AWS administrator, AWS DevOps, DevOps engineer, Slack Admin |

## Troubleshooting
<a name="deploy-chatops-solution-to-manage-sast-scan-results-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Slack misconfigurations | For information about troubleshooting issues related to Slack misconfigurations, see Troubleshooting Amazon Q Developer in the *Amazon Q Developer in chat applications Administrator Guide*. |
| Scan failed because of some other reason | This error means that the code build task has failed. To troubleshoot the issue, go to the link that’s in the message. The failure of the code build task might have the following possible causes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-chatops-solution-to-manage-sast-scan-results.html) |

## Related resources
<a name="deploy-chatops-solution-to-manage-sast-scan-results-resources"></a>

**AWS documentation**
+ [Configure a Slack client](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html#slack-client-setup)
+ [Creating a custom action](https://docs.aws.amazon.com/chatbot/latest/adminguide/custom-actions.html#creating-custom-actions)
+ [Creating an email address identity](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#verify-email-addresses-procedure) [procedure](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#verify-email-addresses-procedure)
+ [Tutorial: Get started with Slack](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html)

**Other resources**
+ [Add apps to your Slack workspace](https://slack.com/intl/en-in/help/articles/202035138-Add-apps-to-your-Slack-workspace) (Slack documentation)
+ [Generating and using tokens](https://docs.sonarsource.com/sonarqube/latest/user-guide/user-account/generating-and-using-tokens/) (SonarQube documentation)
+ [Introduction to the server installation](https://docs.sonarsource.com/sonarqube/latest/setup-and-upgrade/install-the-server/introduction/) (SonarQube documentation)

## Additional information
<a name="deploy-chatops-solution-to-manage-sast-scan-results-additional"></a>

This solution emphasizes Amazon Q Developer in chat applications custom actions for release management purposes. However, you can reuse the solution by modifying the Lambda code for your specific use case and build on top of it.

**Parameters of CloudFormation stack files**

The following table shows the parameters and their descriptions for the CloudFormation stack file `pre-requisite.yml`.

|
|
| **Key** | **Description** |
| --- |--- |
| `StackName` | The name of the CloudFormation stack. |
| `S3LambdaBucket` | The name of the Amazon S3 bucket where you upload the Lambda code. The name must be globally unique. |
| `SonarToken` | The SonarQube user token as described in [Prerequisites](#deploy-chatops-solution-to-manage-sast-scan-results-prereqs). |

The following table shows the parameters and their descriptions for the CloudFormation stack file `app-security.yml`.

|
|
| **Key** | **Description** |
| --- |--- |
| `CKMSKeyArn` | The AWS KMS key Amazon Resource Name (ARN) that is used in IAM roles and Lambda functions created in this stack. |
| `CKMSKeyId` | The AWS KMS key ID that is used in the Amazon SNS topic created in this stack. |
| `EnvironmentType` | The name of the client environment for deployment of the application scan pipeline. Select the environment name from the dropdown list of allowed values. |
| `S3LambdaBucket` | The name of the Amazon S3 bucket that contains the `approval.zip` and `notification.zip` files. |
| `SESEmail` | The name of the registered email identity in Amazon SES as described in [Prerequisites](#deploy-chatops-solution-to-manage-sast-scan-results-prereqs). This identity is the source email address. |
| `SharedInboxMail` | The destination email address to which the scan notifications are sent. |
| `SlackChannelId` | The channel ID of the Slack channel where you want the notifications sent. To find the channel ID, right-click the channel name in **Channel Details** on the Slack app. The channel ID is at the bottom. |
| `SlackWorkspaceId` | The Slack workspace ID as described in [Prerequisites](#deploy-chatops-solution-to-manage-sast-scan-results-prereqs). To find the Slack workspace ID, sign in to the AWS Management Console, open the Amazon Q Developer in chat applications console, and choose **Configured clients**, **Slack**, **WorkspaceID**. |
| `StackName` | The name of the CloudFormation stack. |
| `SonarFileDirectory` | The directory that contains the `sonar.project.<env>.properties` file. |
| `SonarFileName` | The name of the `sonar.project.<env>properties` file. |
| `SourceCodeZip` | The name of the .zip file that contains the `sonar.project.<env>properties` file and the source code. |
