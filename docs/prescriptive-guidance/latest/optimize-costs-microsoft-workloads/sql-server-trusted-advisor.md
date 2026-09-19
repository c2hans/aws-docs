---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-trusted-advisor.html
---

# Review Trusted Advisor recommendations for SQL Server workloads
<a name="sql-server-trusted-advisor"></a>

## Overview
<a name="sql-server-trusted-advisor-overview"></a>

[AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) provides recommendations that help you follow AWS best practices. By analyzing your usage, configuration, and spend, Trusted Advisor provides actionable recommendations to reduce your costs, improve system availability and performance, or help close security gaps. This section focuses on Trusted Advisor checks that can help you reduce the costs of operating SQL Server workloads in the AWS Cloud.

## Cost optimization recommendations
<a name="sql-server-trusted-advisor-recommendations"></a>

Trusted Advisor provides recommendations that help you optimize your SQL Server workloads on Amazon Elastic Compute Cloud (Amazon EC2). The checks inspect your SQL Server workloads and automatically list the instances that need optimization. Operationalizing Trusted Advisor recommendations can reduce costs and improve the security posture of your organization.

The following are Trusted Advisor checks that focus on Microsoft SQL Server:
+ [Amazon EC2 instances over-provisioned for Microsoft SQL Server](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#ec2-instance-over-provisioned-microsoft-sql-server) – This check analyzes your Amazon EC2 instances that are running SQL Server and alerts you if an instance exceeds the SQL Server software vCPU limit. For example, an instance with SQL Server Standard edition can use up to 48 vCPUs. An instance with SQL Server Web can use up to 32 vCPUs.

<table>
<tbody>
</tbody>
</table>

+ [Amazon EC2 instances consolidation for Microsoft SQL Server](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#ec2-instances-consolidation-sql-server) – This check analyzes your Amazon EC2 instances and alerts you if your instance has less than the minimum number of SQL Server licenses. You can consolidate smaller SQL Server instances to help lower costs. If you have many small, license-included SQL Server instances, then consider consolidating. According to the [Microsoft SQL Server 2019 licensing guide](https://download.microsoft.com/download/e/2/9/e29a9331-965d-4faa-bd2e-7c1db7cd8348/SQL_Server_2019_Licensing_guide.pdf), SQL Server requires a minimum of 4 vCPU licenses per instance. If you consolidate these databases, you can save on licensing costs. You can make your decision based on the number of databases on the instance, the maximum database size, and the total size of the databases. Consolidation is supported for Web, Standard, and Enterprise editions of SQL Server. For more information, see [Consolidating SQL Server Databases](https://learn.microsoft.com/en-us/archive/blogs/mvpawardprogram/consolidating-sql-server-databases) (Microsoft blog post).

  AWS does not recommend putting large production databases on only one server. However, you can consolidate smaller ones used for non-production environments, such as for development, testing, and staging. This depends on your current SQL Server usage; if you have low-usage databases, you can consolidate on one server.

## Configure Trusted Advisor
<a name="sql-server-trusted-advisor-configuration"></a>

Do the following to evaluate SQL Server focused checks in Trusted Advisor.

1. Sign in to the AWS Management Console.

1. Open the [AWS Trusted Advisor console](https://console.aws.amazon.com/trustedadvisor/home).

1. In the navigation pane, under **Recommendations**, choose **Cost optimization**.

1. In the **Cost optimization checks** list, review the status of the **Amazon EC2 instances consolidation for Microsoft SQL Server** and **Amazon EC2 instances over-provisioned for Microsoft SQL Server** checks.
   + Green check symbols indicate that your Amazon EC2 instances are optimally configured.
   + Orange alert symbols indicate that there are opportunities for improvement.

1. Choose a check to see its details and recommendations.

1. Follow the instructions provided by the check to optimize your Amazon EC2 instances that are running SQL Server workloads.

1. Monitor your instances regularly, and refresh the checks periodically.

## Additional resources
<a name="sql-server-trusted-advisor-resources"></a>
+ [Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html) (AWS documentation)
+ [Microsoft SQL Server on AWS](https://aws.amazon.com/sql/) (AWS)
+ [Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/) (AWS)
+ [SQL Server 2019 pricing](https://www.microsoft.com/en-us/sql-server/sql-server-2019-pricing) (Microsoft)
+ [AWS Launch Wizard for SQL Server](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sql.html) (AWS documentation)
