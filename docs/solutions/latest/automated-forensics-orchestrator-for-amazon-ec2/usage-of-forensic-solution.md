---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/usage-of-forensic-solution.html
---

# Usage of Forensic Guidance
<a name="usage-of-forensic-solution"></a>

## Step 1. Sign in to the Security Hub AWS Account AWS Management Console and initiate forensic analysis
<a name="step-1.-sign-in-to-the-security-hub-aws-account-aws-console-and-initiate-forensic-analysis"></a>

After the Guidance CloudFormation stack has been deployed and launched, you can sign in to the web interface.

1. Sign in to the [AWS Security Hub console](https://console.aws.amazon.com/securityhub/).

1. To display a finding list, do one of the following:

   1. In the Security Hub navigation pane, choose **Findings**.

   1. In the Security Hub navigation pane, choose **Insights**. Select an insight, and then on the results list, select an insight result.

   1. In the Security Hub navigation pane, choose **Integrations**. Choose **See findings** for an integration.

1. Select the finding title.

1. Select the instance findings to trigger forensics.

1. In **Actions** , you can select:

   1.  **Forensic Isolation** to initiate forensic analysis and perform isolation of instance.

   1.  **Forensic Triage** to initiate forensic analysis.

       **Forensic analysis - Actions**
![initiate forensic analysis](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/initiate-forensic-analysis.png)

## Step 2. Sign in to the Forensic AWS Account AWS Management Console and view step functions flow
<a name="step-2.-sign-in-to-the-forensic-aws-account-aws-console-and-view-step-functions-flow"></a>

1. Sign in to the [AWS Step Functions console](https://console.aws.amazon.com/states/).

1. After completion of triaging, an acquisition and investigation flow email will be sent to subscribed SNS topic.

**Acquisition and investigation flow notification**
image::images/investigation-flow-sns.png[scaledwidth=100%]. Check email for details of the forensic results.

   Example Disk Analysis result:

**Example - Disk Analysis result**
image::images/disk-analysis-result.png[scaledwidth=100%]\+

Example Memory Analysis result:

\+ .Example - Memory Analysis result image::images/memory-analysis-result.png[scaledwidth=100%]
