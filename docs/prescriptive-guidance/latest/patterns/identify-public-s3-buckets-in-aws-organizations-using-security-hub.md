---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-public-s3-buckets-in-aws-organizations-using-security-hub.html
---

# Identify public Amazon S3 buckets in AWS Organizations by using Security Hub CSPM
<a name="identify-public-s3-buckets-in-aws-organizations-using-security-hub"></a>

*Mourad Cherfaoui, Arun Chandapillai, and Parag Nagwekar, Amazon Web Services*

## Summary
<a name="identify-public-s3-buckets-in-aws-organizations-using-security-hub-summary"></a>

This pattern shows you how to build a mechanism for identifying public Amazon Simple Storage Service (Amazon S3) buckets in your AWS Organizations accounts. The mechanism works by using controls from the [AWS Foundational Security Best Practices (FSBP) standard](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html) in AWS Security Hub CSPM to monitor Amazon S3 buckets. You can use Amazon EventBridge to process Security Hub CSPM [findings](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings.html), and then post these findings to an Amazon Simple Notification Service (Amazon SNS) topic. Stakeholders in your organization can subscribe to the topic and get immediate email notifications about the findings.

New Amazon S3 buckets and their objects don't allow public access by default. You can use this pattern in scenarios where you must modify default Amazon S3 configurations based on your organization's requirements. For example, this could be a scenario where you have an Amazon S3 bucket that hosts a public-facing website or files that everyone on the internet must be able to read from your Amazon S3 bucket.

Security Hub CSPM is often deployed as a central service to consolidate all security findings, including those related to security standards and compliance requirements. There are other AWS services that you can use to detect public Amazon S3 buckets, but this pattern uses an existing Security Hub CSPM deployment with minimal configuration.

## Prerequisites and limitations
<a name="identify-public-s3-buckets-in-aws-organizations-using-security-hub-prereqs"></a>

**Prerequisites**
+ An AWS multi-account setup with a dedicated [Security Hub CSPM administrator account](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html)
+ Security Hub CSPM and AWS Config, enabled in the AWS Region that you want to monitor
**Note**
You must enable [cross-Region aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation-enable.html) in Security Hub CSPM if you want to monitor multiple Regions from a single aggregation Region.
+ User permissions for accessing and updating the Security Hub CSPM administrator account, read access to all the Amazon S3 buckets in the organization, and permissions for turning off public access (if required)

## Architecture
<a name="identify-public-s3-buckets-in-aws-organizations-using-security-hub-architecture"></a>

The following diagram shows an architecture for using Security Hub CSPM to identify public Amazon S3 buckets.

![Diagram showing cross-account replication workflow](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7e365290-e3e9-460a-b69f-669ba459cf4c/images/381d66ac-ec03-4458-9793-9d125cebdba6.png)

The diagram show the following workflow:

1. Security Hub CSPM monitors the configuration of Amazon S3 buckets in all AWS Organizations accounts (including the administrator account) by using the S3.2 and S3.3 controls from the FSBP security standard, and detects a finding if a bucket is configured as public.

1. The Security Hub CSPM administrator account accesses the findings (including those for S3.2 and S3.3) from all member accounts.

1. Security Hub CSPM automatically sends all new findings and all updates to existing findings to EventBridge as **Security Hub CSPM Findings - Imported** events. This includes events for findings from both the administrator and member accounts.

1. An EventBridge rule filters on findings from S3.2 and S3.3 that have a `ComplianceStatus` of `FAILED`, a workflow status of `NEW`, and a `RecordState` of `ACTIVE`.

1. Rules use the event patterns to identify events and send them to an Amazon SNS topic once matched.

1. An Amazon SNS topic sends the events to its subscribers (through email, for example).

1. Security analysts designated to receive the email notifications review the Amazon S3 bucket in question.

1. If the bucket is approved for public access, the security analyst sets the workflow status of the corresponding finding in Security Hub CSPM to `SUPPRESSED`. Otherwise, the analyst sets the status to `NOTIFIED`. This eliminates future notifications for the Amazon S3 bucket and reduces notification noise.

1. If the workflow status is set to `NOTIFIED`, the security analyst reviews the finding with the bucket owner to determine if public access is justified and complies with privacy and data protection requirements. The investigation results in either removing public access to the bucket or approving public access. In the latter case, the security analyst sets the workflow status to `SUPPRESSED`.

**Note**
The architecture diagram applies to both single Region and cross-Region aggregation deployments. In accounts A, B, and C in the diagram, Security Hub CSPM can belong to the same Region as the administrator account or belong to different Regions if cross-Region aggregation is enabled.

## Tools
<a name="identify-public-s3-buckets-in-aws-organizations-using-security-hub-tools"></a>
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. EventBridge delivers a stream of real-time data from your own applications, software as a service (SaaS) applications, and AWS services. EventBridge routes that data to targets such as Amazon SNS topics and AWS Lambda functions if the data matches user-defined rules.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses. Subscribers receive all messages published to the topics to which they subscribe, and all subscribers to a topic receive the same messages.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS. Security Hub CSPM also helps you check your AWS environment against security industry standards and best practices. Security Hub CSPM collects security data from across AWS accounts, services, and supported third-party partner products, and then helps to analyze security trends and identify the highest priority security issues.

## Epics
<a name="identify-public-s3-buckets-in-aws-organizations-using-security-hub-epics"></a>

### Configure Security Hub CSPM accounts
<a name="configure-ash-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable Security Hub CSPM in AWS Organizations accounts. | To enable Security Hub CSPM in the organization accounts where you want to monitor Amazon S3 buckets, see the guidelines from [Designating a Security Hub CSPM administrator account (console)](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html#:~:text=AWSSecurityHubOrganizationsAccess-,Designating%20a%20Security%20Hub%20administrator%20account%20(console),-The%20organization%20management) and [Managing member accounts that belong to an organization](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html) in the Security Hub CSPM documentation. | AWS administrator |
| (Optional) Enable cross-Region aggregation. | If you want to monitor Amazon S3 buckets in multiple Regions from a single Region, set up [cross-Region aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html). | AWS administrator |
| Enable the S3.2 and S3.3 controls for the FSBP security standard. | You must enable S3.2 and S3.3 controls for the FSBP security standard.1. To enable S3.2 controls, follow the instructions from [[S3.2] S3 buckets should prohibit public read access](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-2) in the Security Hub CSPM documentation.<br />2. To enable S3.3 controls, follow the instructions from [[3] S3 buckets should prohibit public write access](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-3) in the Security Hub CSPM documentation. | AWS administrator |

### Set up the environment
<a name="set-up-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the Amazon SNS topic and email subscription. | 1. Sign in to the AWS Management Console and open the [Amazon SNS console](https://console.aws.amazon.com/sns/home).<br />2. In the navigation pane, choose **Topics**, and then choose **Create topic**.<br />3. For **Type**, choose **Standard**.<br />4. For **Name**, enter a name for your topic (for example, **public-s3-buckets**).<br />5. Choose **Create topic**.<br />6. On the** Subscriptions** tab for your topic, choose **Create subscription**.<br />7. For **Protocol**, select **Email**.<br />8. For **Endpoint**, enter the email address that will receive the notifications. You can use the email address of an AWS administrator, IT professional, or Infosec professional.<br />9. Choose **Create subscription**. To create additional email subscriptions, repeat steps 6–8 as needed. | AWS administrator |
| Configure the EventBridge rule. | 1. Open the [EventBridge console](https://console.aws.amazon.com/events/).<br />2. In the **Get started** section, select **EventBridge Rule**, and then choose **Create rule**.<br />3. On the **Define rule detail** page, for **Name**, enter a name for your rule (for example, **public-s3-buckets**). Choose **Next**.<br />4. In the **Event pattern** section, choose **Edit pattern**.<br />5. Copy the following code, paste it into the **Event pattern** code editor, and then choose **Next**.<pre>{<br />  "source": ["aws.securityhub"],<br />  "detail-type": ["Security Hub Findings - Imported"],<br />  "detail": {<br />    "findings": {<br />      "Compliance": {<br />        "Status": ["FAILED"]<br />      },<br />      "RecordState": ["ACTIVE"],<br />      "Workflow": {<br />        "Status": ["NEW"]<br />      },<br />      "ProductFields": {<br />        "ControlId": ["S3.2", "S3.3"]<br />      }<br />    }<br />  }<br />}</pre><br />6. On the **Select target(s)** page, for **Select a target**, select **SNS topic** as the target, and then select the topic that you created earlier.<br />7. Choose **Next**, choose **Next** again, and then choose **Create rule**. | AWS administrator |

## Troubleshooting
<a name="identify-public-s3-buckets-in-aws-organizations-using-security-hub-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| I have an Amazon S3 bucket with public access enabled, but I'm not getting email notifications for it. | This could be because the bucket was created in another Region and cross-Region aggregation is not enabled in the Security Hub CSPM administrator account. To resolve this issue, enable cross-Region aggregation or implement this pattern's solution in the Region where your Amazon S3 bucket currently resides. |

## Related resources
<a name="identify-public-s3-buckets-in-aws-organizations-using-security-hub-resources"></a>
+ [What is AWS Security Hub CSPM?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) (Security Hub CSPM documentation)
+ [AWS Foundational Security Best Practices (FSBP) standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp.html) (Security Hub CSPM documentation)
+ [AWS Security Hub CSPM multi-account enable scripts](https://github.com/awslabs/aws-securityhub-multiaccount-scripts/tree/master/multiaccount-enable) (AWS Labs)
+ [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) (Amazon S3 documentation)

## Additional information
<a name="identify-public-s3-buckets-in-aws-organizations-using-security-hub-additional"></a>

*Workflow for monitoring public Amazon S3 buckets*

The following workflow illustrates how you can monitor the public Amazon S3 buckets in your organization. The workflow assumes that you completed the steps in the *Configure the Amazon SNS topic and email subscription *story of this pattern*.*

1. You receive an email notification when an Amazon S3 bucket is configured with public access.
   + If the bucket is approved for public access, set the workflow status of the corresponding finding to `SUPPRESSED` in the Security Hub CSPM administrator account. This prevents Security Hub CSPM from issuing further notifications for this bucket and can eliminate duplicate alerts.
   + If the bucket isn't approved for public access, set the workflow status of the corresponding finding in the Security Hub CSPM administrator account to `NOTIFIED`. This prevents Security Hub CSPM from issuing further notifications for this bucket from Security Hub CSPM and can eliminate noise.

1. If the bucket might contain sensitive data, turn off public access immediately until the review is completed. If you turn off public access, then Security Hub CSPM changes the workflow status to `RESOLVED`. Then, email notifications for the bucket stop.

1. Find the user who configured the bucket as public (for example, by using AWS CloudTrail) and start a review. The review results in either removing public access to the bucket or approving public access. If public access is approved, then set the workflow status of the corresponding finding to `SUPPRESSED`.
