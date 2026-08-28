---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/resolve-connection-errors-after-migrating-microsoft-sql-server-to-the-aws-cloud.html
---

# Resolve connection errors after migrating Microsoft SQL Server to the AWS Cloud
<a name="resolve-connection-errors-after-migrating-microsoft-sql-server-to-the-aws-cloud"></a>

*Premkumar Chelladurai, Amazon Web Services*

## Summary
<a name="resolve-connection-errors-after-migrating-microsoft-sql-server-to-the-aws-cloud-summary"></a>

After you migrate Microsoft SQL Server running on Windows Server 2008 R2, 2012, or 2012 R2 to Amazon Elastic Compute Cloud (Amazon EC2) instances on the Amazon Web Services (AWS) Cloud, the connection to SQL Server fails and the following errors appear:
+ `[Microsoft][ODBC SQL Server Driver][DBNETLIB] General Network error`
+ `ERROR [08S01] [Microsoft][SQL Native Client]Communication link failure. System.Data.SqlClient.SqlException: A transport-level error has occurred when sending the request to the server. (provider: TCP Provider, error: 0 - An existing connection was forcibly closed by the remote host.)`
+ `TCP Provider: The semaphore timeout period has expired`

This pattern describes how you can resolve these errors by turning off the Windows Scalable Networking Pack (SNP) features at the operating system (OS) and network interface level for SQL Server running on Windows Server 2008 R2, 2012, or 2012 R2.

## Prerequisites and limitations
<a name="resolve-connection-errors-after-migrating-microsoft-sql-server-to-the-aws-cloud-prereqs"></a>

**Prerequisites**
+ Administrator privileges for Windows Server.
+ If you used AWS Application Migration Service as your migration tool, you require one of the following Windows Server versions:
  + Windows Server 2008 R2 Service Pack 1, 2012, or 2012 R2
+ If you used CloudEndure Migration as your migration tool, you require one of the following Windows Server versions:
  + Windows Server 2003 R2 Service Pack 3, 2008, 2008 R2 Service Pack 1, 2012, or 2012 R2

## Tools
<a name="resolve-connection-errors-after-migrating-microsoft-sql-server-to-the-aws-cloud-tools"></a>
+ [Amazon EC2](https://docs.aws.amazon.com/ec2/index.html) – Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the AWS Cloud. You can use Amazon EC2 to launch as many or as few virtual servers as you need, and you can scale out or scale in.
+ [Windows Server](https://docs.microsoft.com/en-us/windows-server/) – Windows Server is a platform for building an infrastructure of connected applications, networks, and web services.

## Epics
<a name="resolve-connection-errors-after-migrating-microsoft-sql-server-to-the-aws-cloud-epics"></a>

### Turn off SNP features at the OS and elastic network interface levels
<a name="turn-off-snp-features-at-the-os-and-elastic-network-interface-levels"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Turn off SNP features at the OS level. | 1. Sign in to Windows Server and open a command prompt as an administrator.<br />2. Run the `netsh int tcp show global` command.<br />3. In the output, check if either `Receive-Side Scaling` or `Chimney Offload` is in `enabled` mode. If either of them is `enabled`, run the following commands:`netsh int tcp set global chimney=disabled``netsh int tcp set global rss=disabled` | AWS administrator, AWS systems administrator, Migration engineer, Cloud administrator |
| Turn off SNP features at the elastic network interface level. | 1. Choose **Start**, enter `ncpa.cpl`, and then press **Enter**. <br />2. Right-click **Elastic Network Adapter**.<br />3. In the popup menu, choose **Properties**.<br />4. In the **Ethernet Adapter Properties** window, choose **Configure**.<br />5. In the **Amazon Elastic Network Adapter Properties** popup window, choose the **Advanced** tab.<br />6. In the **Property** section, turn off all offloads and RSS. | AWS administrator, Cloud administrator, AWS systems administrator |

## Related resources
<a name="resolve-connection-errors-after-migrating-microsoft-sql-server-to-the-aws-cloud-resources"></a>
+ [How to troubleshoot advanced network performance features such as RSS and NetDMA](https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-network-performance-features-rss-netdma)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
