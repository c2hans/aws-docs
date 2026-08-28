---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/theme-1.html
---

# Theme 1: Use managed services
<a name="theme-1"></a>

**Essential Eight strategies covered**: Patch applications, restrict administrative privileges, patch operating systems

Managed services help you reduce your compliance obligations by allowing AWS to manage some security tasks, such as patching and vulnerability management.

As discussed in the [AWS shared responsibility model](australian-sec-compliance.md#shared-model) section, you share responsibility with AWS for cloud security and compliance. This can reduce your operational burden because AWS operates, manages, and controls components, from the host operating system and virtualisation layer to the physical security of the facilities in which the service operates.

Your responsibilities might include managing maintenance windows for managed services, such as Amazon Relational Database Service (Amazon RDS) or Amazon Redshift, and scanning for vulnerabilities in AWS Lambda code or container images. As with all themes in this guide, you also retain responsibility for monitoring and compliance reporting. You can use [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) to report vulnerabilities across all of your AWS accounts. You can use rules in AWS Config to make sure that services, such as Amazon RDS and Amazon Redshift, have minor updates and maintenance windows enabled.

For example, if you run an Amazon EC2 instance, your responsibilities include the following:
+ Application control
+ Patching applications
+ Restricting administrative privileges to the Amazon EC2 control plane and the operating system (OS)
+ Patching the OS
+ Enforcing multi-factor authentication (MFA) to access the AWS control plane and the OS
+ Backing up the data and configuration

Whereas if you run a Lambda function, then your responsibilities are reduced and include the following:
+ Application control
+ Confirming that libraries are up-to-date
+ Restricting administrative privileges to the Lambda control plane
+ Enforcing MFA to access the AWS control plane
+ Backing up the Lambda function code and configuration

## Related best practices in the AWS Well-Architected Framework
<a name="theme-1-best-practices"></a>
+ [SEC01-BP05 Reduce security management scope](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_securely_operate_reduce_management_scope.html)

## Implementing this theme
<a name="theme-1-implementation"></a>

### Enable patching
<a name="enable-patching.838ced04-b0de-57a5-8df1-73bc8cab1fc0"></a>
+ [Apply Amazon RDS updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html)
+ [Enable managed updates in AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-platform-update-managed.html)
+ [Be aware of Amazon Redshift cluster maintenance windows](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-cluster-maintenance)

### Scan for vulnerabilities
<a name="scan-for-vulnerabilities.2211743c-5bdf-586e-8de0-232d8d1e8a34"></a>
+ [Scan Amazon Elastic Container Registry (Amazon ECR) container images with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html)
+ [Scan Lambda functions with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html)

## Monitoring this theme
<a name="theme-1-monitoring"></a>

### Implement governance checks
<a name="implement-governance-checks.9d5e18cb-75da-5636-ab04-64f1c3751998"></a>
+ Enable the [Operational Best Practices for ACSC Essential 8](https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-acsc_essential_8.html) conformance pack in AWS Config

### Monitor Amazon Inspector
<a name="monitor-9999999999999999ins-.f46f106c-cfd2-5633-94be-a98971cde2f9"></a>
+ [Assess account-level coverage](https://docs.aws.amazon.com/inspector/latest/user/assessing-coverage.html#viewing-coverage-accounts)
+ [Manage multiple accounts](https://docs.aws.amazon.com/inspector/latest/user/managing-multiple-accounts.html)

### Implement the following AWS Config rules
<a name="implement-the-following-9999999999999999cc--rules.b69eb9cf-4ad6-5a6f-abcd-d7ddd48a319d"></a>
+ `RDS_AUTOMATIC_MINOR_VERSION_UPGRADE_ENABLED`
+ `ELASTIC_BEANSTALK_MANAGED_UPDATES_ENABLED`
+ `REDSHIFT_CLUSTER_MAINTENANCESETTINGS_CHECK`
+ `EC2_MANAGEDINSTANCE_PATCH_COMPLIANCE_STATUS_CHECK`
+ `EKS_CLUSTER_SUPPORTED_VERSION`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
