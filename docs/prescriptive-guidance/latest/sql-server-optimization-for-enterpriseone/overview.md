---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/overview.html
---

# Overview of JD Edwards EnterpriseOne behavior on SQL Server
<a name="overview"></a>

EnterpriseOne business logic is primarily handled within applications. Only basic data manipulation language (DML) statements are passed to the database from the application. In standard processing, the record set is opened on the database but is managed by the application. The application then typically performs multiple DML operations for each record in the record set. This approach generates a substantial volume of *chatty* DML operations against the database. The latency of each DML operation is one of the key drivers of performance. Because of this architecture, CPU usage of the database that supports EnterpriseOne tends to be minimal, whereas network and disk I/O characteristics are the primary drivers of process performance. EnterpriseOne database tuning focuses heavily on the minimization of DML latency.

To mitigate the latency impact of disk read I/O, a large buffer cache is often used. This can be combined with SQL Server data compression to make the buffer cache substantially more effective. Although using data compression affects CPU, the overhead is minimal when you use this approach with EnterpriseOne. When the buffer cache is adequately sized, disk read I/O latency isn't typically an area of concern.

The SQL Server buffer cache doesn't address the latency of write I/O. When an EnterpriseOne process generates a large number of chatty write operations, performance may be constrained by the latency of each write operation that commits to the transaction log. To minimize this latency, you can use `io2` and/or `io2` Block Express volumes for the LDF file. If `io2` and/or `io2` Block Express alone is insufficient to deliver the required performance or is otherwise cost-prohibitive, you can use a delayed durability configuration to improve performance.

Because many EnterpriseOne processes create record sets that might overlap with other open record sets, you should enable read committed snapshot isolation (RCSI) on each EnterpriseOne database to minimize blocking. When this feature is enabled, it can create a substantial I/O requirement for `tempdb`. `tempdb `is by nature ephemeral and doesn't require the durability of standard block storage. In most cases, local instance non-volatile memory express (NVMe) storage is the best choice for `tempdb`.

The following sections of this guide explore these and other best practices for optimizing SQL Server for JD Edwards EnterpriseOne.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
