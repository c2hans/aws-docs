---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/automate.html
---

# Step 3. Automate backup operations
<a name="automate"></a>

Your organization's backup plans and resource assignments should be configured to reflect your enterprise data protection policies. By automating and deploying backup policies or organization-wide [backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html), you can standardize and scale your backup strategy. You can use [AWS Organizations](https://aws.amazon.com/organizations/) to centrally automate backup policies to implement, configure, manage, and govern backup activity across [supported AWS Backup resources](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-other-services.html) by scheduling backup operations.

To improve productivity and govern infrastructure operations across multiple-account environments, consider implementing infrastructure as code (IaC) and event-driven architecture as essential parts of your digital transformation and backup strategy. Automating backups provides the following benefits:
+ Reduces manual overhead from time-consuming configuration of your backups
+ Minimizes the risk for errors
+ Provides visibility on drift detection
+ Enhances backup policy compliance across multiple AWS workloads or accounts

Implementing backup policies as code can help you meet data protection regulations by doing the following:
+ Configuring different requirements for your resource types
+ Scaling your enterprise data protection strategy
+ Implementing [lifecycle rules](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Lifecycle.html) to specify how long before a recovery point either transitions to cold storage or is deleted, which can help optimize your costs

When automating your backup operations, you can scale resource assignment options by using AWS tags and resource IDs to automatically identify the AWS resources that store data for your business-critical applications and protect your data using immutable backups. This can help you prioritize security controls, such as access permissions and backup plans or policies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
