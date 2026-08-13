---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/experimental-ous.html
---

# Experimental OUs
<a name="experimental-ous"></a>

## Sandbox OU
<a name="sandbox-ou"></a>

 The Sandbox OU contains accounts in which your builders are generally free to explore and experiment with AWS services and other tools and services subject to your acceptable use policies. These environments are typically disconnected from your internal networks and internal services. Sandbox accounts should not be promoted to any other type of account or environment within the Workloads OU.

### Sandbox per builder or team with spend limits
<a name="sandbox-per-builder-or-team-with-spend-limits"></a>

 A common practice is to provide a sandbox account to either each builder or each small team of builders, along with cloud spend budgets to ensure that their AWS spending aligns within your policies. In more advanced scenarios, you might provide your builders and teams with the option to have multiple sandbox accounts so that they can experiment more freely with configurations that entail use of multiple accounts (for example, experimenting with cross-account IAM roles).

 There is a maximum number of accounts in an organization. If you have thousands of builders and expect to allocate a sandbox environment for each builder, you might encounter the maximum quota for accounts. Refer to [Quotas for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) for more details on the maximum number of accounts in an organization.

 In cases where you need more than several thousand sandbox accounts, you might consider either creating one or more separate organizations to contain the sandbox accounts or establishing a process to recycle sandboxes when they are no longer in use.

### Temporary resources and environments
<a name="temporary-resources-and-environments"></a>

 Unlike more persistent development environments, it's common to set expectations with your builders that the resources they create in sandbox environments are temporary in nature. As a cost control measure and to reinforce the temporary nature of sandbox resources, you can put automated procedures in place to periodically purge the resources created in these environments.

 As a further measure to reduce costs, you can use the [Instance Scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/) solution to automate the starting and stopping of Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) instances based on provided schedules

### Wide-ranging access
<a name="wide-ranging-access"></a>

 Wide-ranging access is typically provided in sandbox-oriented accounts including administrative-like access within each account, full access to most AWS services, and possibly outbound and inbound access to the internet. Access to the internet might be required to connect to AWS service APIs, download externally accessible software packages, and integrate with publicly available services.

### No access to corporate resources and non-public data
<a name="no-access-to-corporate-resources-and-non-public-data"></a>

 Given the extent of access provided in sandbox environments, businesses typically employ a combination of controls and internal usage agreements to limit builders from accessing corporate resources and data from their sandbox accounts. Use of non-public data and intellectual property, including proprietary source code and binaries, is typically not allowed in sandbox environments.

### Sandbox and development environments
<a name="sandbox-and-development-environments"></a>

 Due to use of non-public data and the more formal nature of the work being performed in development environments, we recommend that you make a high-level distinction between sandbox environments and development environments. For example, in development environments your teams are performing more formal experiments, day-to-day development, and early testing work that requires access to your intellectual property and to enterprise services, such as source code and artifact management.

### Additional services and functionalities
<a name="additional-services-and-functionalities-6"></a>

 Common examples of monitoring capabilities that can be centrally accessed and managed using a Shared Services account include:
+  [**Instance Scheduler on AWS**](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/) solution to automate the starting and stopping of Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) instances based on provided schedules.

### Sandbox per builder or team
<a name="sandbox-per-builder-or-team"></a>

 In the following example, sandbox accounts are represented for individual builders and teams. One user has two sandbox accounts so that they can perform experiments that require multiple accounts.

 In support of hackathons and other events, you might also find value in creating transient sandbox accounts for temporary teams of people.

![Diagram showing example structure of Sandbox OU](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/example-sandbox-ou.png)
