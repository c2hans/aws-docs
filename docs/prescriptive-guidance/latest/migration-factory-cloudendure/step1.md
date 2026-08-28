---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/step1.html
---

# Step 1. Prepare the CSV file and import the data
<a name="step1"></a>

The first step in a large-scale migration is to prepare the application and server metadata. This metadata is usually collected from portfolio analysis and wave planning, and placed in a comma-separated values (CSV) file. You use the metadata to automate the migration process and to update the Amazon Elastic Compute Cloud (Amazon EC2) launch templates in order to launch target EC2 instances. The default CSV file that we'll provide includes the following attributes:
+ `wave_name` – Unique wave ID, based on priority and dependencies.
+ `app_name` – Application to be migrated.
+ `aws_region` – Target AWS Region for the source machines.
+ `aws_accountid` – 12-digit account ID of the destination AWS account.
+ `server_name` – On-premises server to be migrated.
+ `server_os_family` – Operating system (Windows or Linux) running on the on-premises server.
+ `server_os_version` – Version of the server operating system.
+ `server_fqdn` – Fully qualified domain name (FQDN) of the server.
+ `server_tier` – Type of server (web, application, or database).
+ `server_environment` – Host environment for server (development, test, production, QA, preproduction).
+ `r_type` – Migration strategy for the source server, such as rehost or replatform.
+ `subnet_IDs` – IDs of the AWS subnets to be used for the EC2 instances after cutover.
+ `securitygroup_IDs` – IDs of the AWS security groups to be used after cutover.
+ `subnet_IDs_test` – IDs of the AWS subnets to be used for testing.
+ `securitygroup_IDs_test` – IDs of the AWS security groups to be used for testing.
+ `instanceType` – [EC2 instance type](https://aws.amazon.com/ec2/instance-types/) to be used for the servers.
+ `tenancy` – Whether the instance runs on shared hardware, on single-tenant hardware (dedicated), or on an isolated server (Dedicated Host).
+ `tags` – AWS tags for target EC2 instances.

Cloud Migration Factory includes an automation script that you run on the migration execution server to import the metadata from the CSV file to Cloud Migration Factory.

For detailed instructions, see [Importing data](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/metadata-management.html#importing-data) in the *Cloud Migration Factory Implementation Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
