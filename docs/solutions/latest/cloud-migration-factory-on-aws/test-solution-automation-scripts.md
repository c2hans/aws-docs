---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/test-solution-automation-scripts.html
---

# Step 8: Test the solution using the automation scripts
<a name="test-solution-automation-scripts"></a>

## Import migration metadata into the factory
<a name="import-migration-metadata-into-the-factory"></a>

To start the migration process, download the [server-list.csv](https://github.com/aws-solutions/cloud-migration-factory-on-aws/blob/master/source/integrations/mgn/MGN-automation-scripts/server-list.csv) file from the GitHub repository. The `server-list.csv` file is an example AWS MGN Service migration intake form to import the attributes for the in-scope source servers.

**Note**
The .csv file and the sample automation scripts were part of the package from the same GitHub repository.

You can customize the form for your migration by replacing the sample data with your specific server and application data. The following table details the data to replace to customize this solution for your migration needs.

| Field name | Required? | Description |
| --- | --- | --- |
| wave\_name | Yes | The wave name is based on priority and application server dependencies. Obtain this identifier from your migration plan. |
| app\_name | Yes | The names of the applications that are in-scope for migration. Confirm that your application grouping includes all the applications sharing the same servers. |
| aws\_accountid | Yes | A 12-digit identifier for your AWS account located in your account profile. To access, select your account profile from the upper-right corner of the AWS Management Console and select **My Account** from the drop-down menu. |
| aws\_region | Yes | AWS Region code. For example, `us-east-1`. Refer to the [full Region code list](https://docs.aws.amazon.com/general/latest/gr/rande.html). |
| server\_name | Yes | The name of the on-premises servers that are in-scope for migration. |
| server\_os\_family | Yes | The operating system (OS) that is running on the in-scope source servers. Use either **windows** or **linux** since this solution supports only these operating systems. |
| server\_os\_version | Yes | The version of the OS running on the in-scope source servers. Use the OS version, not the Kernel version, for example, use RHEL 7.1, Windows Server 2019, or CentOS 7.5, 7.6. Do not use Linux 3.xx, 4.xx, or Windows 8.1.x.  |
| server\_fqdn | Yes | The source server’s fully qualified domain name, which is the server name followed by the domain name. For example, server123.company.com. |
| server\_tier | Yes | A label to identify whether the source server is a **web**, **app**, or a **database** server. We recommend designating the source server as **app** if the server functions as more than one tier, for example, if the server runs web, app, and database tiers together. |
| server\_environment | Yes | A label to identify the server’s environment. For example, **dev**, **test**, **prod**, **QA**, or **pre-prod**. |
| r\_type | Yes | A label to identify the migration strategy. For example, **Retire, Retain, Relocate, Rehost, Repurchase, Replatform, Rearchitect, TBC.**  |
| subnet\_IDs | Yes | The subnet ID for the target Amazon EC2 instance for the migration post-cutover. |
| securitygroup\_IDs | Yes | The security group ID for the target Amazon EC2 instance for the migration post-cutover. |
| subnet\_IDs\_test | Yes | The target subnet ID for the source server that will be tested. |
| securitygroup\_IDs\_test | Yes | The target security group ID for the source server that will be tested. |
| instanceType | Yes | The Amazon EC2 instance type identified in the discovery and planning effort. For information about EC2 instance types, refer to [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types). |
| tenancy | Yes | The tenancy type, which is identified during the discovery and planning efforts. Use one of the following values to identify the tenancy: **Shared**, **Dedicated**, or **Dedicated Host**. You can use **Shared** as the default value unless an application’s license requires a specified type. |
| Tags | No | The tags for the server resources, such as `CostCenter=123;BU=IT;Location=US`. |
| private\_ip | No | The private IP for the target instance. If not included, instance will get an IP from DHCP. |
| iamRole | No | IAM role for the target instance. If not included, no IAM role will be attached to the target instance. |

1. Log in to the Cloud Migration Factory web console.

1. Under **Migration Management**, select **Import** and choose **Select file**. Select the intake form you completed previously and choose **Next**.

1. Review the changes and make sure that you do not see any errors (information message is normal), and choose **Next.**

1. Choose **Upload** to upload servers.

## Access the domains
<a name="access-the-domains"></a>

The sample automation scripts included with this solution connect to the in-scope source servers to automate migration tasks, such as the installation of the replication agent, and shutting down the source servers. In order to conduct a test run of the solution, a domain user with local admin permissions to the source servers is required, for Windows and Linux (sudo permissions) servers. If Linux is not in the domain, other users such as LDAP user with sudo permissions or a local sudo user may be used. For more information about automated migration tasks, refer to Automated migration activities using Migration Factory web console and [Automated migration activities using command prompt](list-of-automated-migration-activities-using-command-prompt.md).

## Conduct a test run of the migration automation
<a name="conduct-a-test-run-of-the-migration-automation"></a>

This solution lets you conduct a test run of the migration automation. Using automation scripts, the migration process imports the data from the migration CSV file into the solution. Prerequisite checks are conducted for the source servers, the replication agent is pushed to the source servers, replication status is verified, and the target server is launched from the Migration Factory web interface. For step-by-step instructions on running a test, refer to Automated migration activities using Migration Factory web console and [Automated migration activities using command prompt](list-of-automated-migration-activities-using-command-prompt.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
