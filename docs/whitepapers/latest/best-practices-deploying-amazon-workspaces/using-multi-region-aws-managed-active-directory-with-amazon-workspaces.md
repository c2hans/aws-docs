---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/using-multi-region-aws-managed-active-directory-with-amazon-workspaces.html
---

# Using multi-Region AWS Managed Active Directory with Amazon WorkSpaces
<a name="using-multi-region-aws-managed-active-directory-with-amazon-workspaces"></a>

[AWS Directory Service for Microsoft Active Directory](https://aws.amazon.com/directoryservice/active-directory/) (MAD) is a fully managed Microsoft Active Directory (AD) that can be paired with Amazon WorkSpaces. Customers choose AWS Managed Microsoft AD because it has built-in high availability, monitoring, and backups. AWS Managed Microsoft AD Enterprise edition adds the ability to configure [Multi-Region Replication](https://aws.amazon.com/blogs/aws/multi-region-replication-now-enabled-for-aws-managed-microsoft-active-directory/). This feature automatically configures inter-region networking connectivity, deploys domain controllers, and replicates all the Active Directory data across multiple regions, ensuring that Windows and Linux workloads residing in those regions can connect to and use AWS MAD with low latency and high performance. Replicated MAD regions cannot be [directly registered with WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/register-deregister-directory.html), however a replicated MAD directory can be registered with WorkSpaces by configuring an AD Connector (ADC) to point to your replicated Domain Controllers.

 The best practice when deploying AD Connectors with MAD is to create an AD Connector for each business unit within your WorkSpaces environment. This will allow you to align each business unit with a specific Organizational Unit within Active Directory. You can then assign AD Group Policy Objects at the Organization Unit level that directly align with the business unit in question.

## Architecture
<a name="architecture"></a>

![Sample architecture showing AD Connectors with MAD is to create an AD Connector for each business unit within your WorkSpaces environment.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/registering-replicated-mad-region.png)

## Implementation
<a name="implementation"></a>

 To register your replicated MAD region to WorkSpaces, you will need to create an AD Connector pointed to your MAD Domain Controller IPs. You can find your MAD Domain Controller IP addresses by going to the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/) navigation pane, selecting Directories and then choosing the correct directory ID. To create these AD Connectors, follow this [guide](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_getting_started.html). Once they are created, you can [register them for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/register-deregister-directory.html). Before you deploy WorkSpaces in your new region, ensure you have updated your VPCs [DHCP options set.](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/dhcp_options_set.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
