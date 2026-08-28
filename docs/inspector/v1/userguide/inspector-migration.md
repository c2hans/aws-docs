---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Amazon Inspector Classic end of support
<a name="inspector-migration"></a>

After careful consideration, we decided to end support for Amazon Inspector Classic, effective May 20, 2026. Amazon Inspector Classic will no longer accept new customers beginning May 20, 2025. As an existing customer with an account signed up for the service before May 20, 2025, you can continue to use Amazon Inspector Classic features. After May 20, 2026, you will no longer be able to use Amazon Inspector Classic.

The new Amazon Inspector is now available globally in AWS Regions. The new Amazon Inspector is a completely rearchitected and redesigned version of the existing Amazon Inspector, now called Amazon Inspector Classic. The following capabilities are the key Amazon Inspector enhancements:
+ **Built for scale** – The new Amazon Inspector is built for scale and the dynamic cloud environment. There is no limit to the number of instances or images that can be scanned in an account.
+ **Support for container images** – The new Amazon Inspector also scans container images residing in Amazon Elastic Container Registry (Amazon ECR) for software vulnerabilities.
+ **Support for multi-account management** – The new Amazon Inspector is integrated with Organizations. This allows you to delegate an administrator account for Amazon Inspector from your organization. The delegated administrator account is a centralized account that consolidates all findings and can configure all member accounts.
+ **Uses AWS Systems Manager Agent (SSM Agent)** – With the new Amazon Inspector, you no longer need to install and maintain a stand-alone Amazon Inspector agent on all of your EC2 instances. The new Amazon Inspector leverages the widely-deployed SSM Agent.
+ **Automated and continual scanning** – With Amazon Inspector Classic, you manually set up assessment targets, assessment templates, and configure the frequency of the assessments. However, the new version of Amazon Inspector automatically detects all newly launched EC2 instances and eligible container images pushed to Amazon ECR and immediately scans them for software vulnerabilities and unintended network exposure. The resources are automatically re-scanned based on several triggers, including a new EC2 instance being launched, a container image being pushed to Amazon ECR, installation of a new package in an EC2 instance, installation of a patch, or publication of a new Common Vulnerabilities and Exposure (CVE) that impacts the resource.
+ **Amazon Inspector risk score** – The new Amazon Inspector calculates an Amazon Inspector risk score to help prioritize your findings. The risk score is calcuatled by correlating up-to-date CVE information with temporal and environmental factors like network accessibility and exploitability information.
+ **More integrations** – All findings are aggregated in a newly designed Amazon Inspector console and pushed to AWS Security Hub CSPM and Amazon EventBridge to automate workflows, such as ticketing. Container image related findings are also pushed to Amazon ECR.

To learn about all features and pricing for the new Amazon Inspector, see the [Amazon Inspector User Guide](https://docs.aws.amazon.com/inspector/latest/user).

While we will continue to support Amazon Inspector Classic for some time, and customers can use both the new Amazon Inspector and Amazon Inspector Classic in the same account, we highly encourage you to migrate to the new Amazon Inspector. The following sections walks you through the process of moving from Amazon Inspector Classic to the new Amazon Inspector.

**Topics**
+ [Step 1: (Optional) Export assessment reports and findings](#inspector-migration-step-1)
+ [Step 2: Delete all scheduled assessment runs in Amazon Inspector Classic](#inspector-migration-step-2)
+ [Step 3: Enable the new Amazon Inspector](#inspector-migration-step-3)

## Step 1: (Optional) Export assessment reports and findings
<a name="inspector-migration-step-1"></a>

To save the assessment reports and findings in Amazon Inspector Classic, generate an assessment report.

**To generate an assessment report**

1. On the **Assessment runs** page, locate the assessment run that you want to generate a report for. Make sure that its status is **Analysis complete**.

1. Under the **Reports** column for this assessment run, choose the reports icon.
**Important**
The reports icon is present in the **Reports** column only for those assessment runs that took place or will take place after April 25, 2017. That's when assessment reports in Amazon Inspector Classic became available.

1. In the **Assessment report** dialog box, choose the type of report that you want to view (either a **Findings** report or a **Full** report) and the report format (HTML or PDF). Then choose **Generate report**.

## Step 2: Delete all scheduled assessment runs in Amazon Inspector Classic
<a name="inspector-migration-step-2"></a>

To disable Amazon Inspector Classic, delete all the assessment templates in your account in all active AWS Regions. Deleting assessment templates stops all your scheduled future assessment runs.

**To delete an assessment template**
+ On the **Assessment Templates** page, choose the template that you want to delete, and then choose **Delete**. When prompted for confirmation, choose **Yes**.
**Important**
When you delete an assessment template, all assessment runs, findings, and versions of the reports associated with this template are also deleted.

## Step 3: Enable the new Amazon Inspector
<a name="inspector-migration-step-3"></a>

You can enable the new Amazon Inspector using the AWS Management Console or the new Amazon Inspector APIs. To get started with the new Amazon Inspector, see [Getting Started](https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html) in the *Amazon Inspector User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
