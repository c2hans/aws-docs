---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_STL_SSHCLIENT_ERROR.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# STL\_SSHCLIENT\_ERROR
<a name="r_STL_SSHCLIENT_ERROR"></a>

 Records all errors seen by the SSH client.

STL\_SSHCLIENT\_ERROR is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_STL_SSHCLIENT_ERROR-table-columns"></a>

| Column name  | Data type  | Description  |
| --- | --- | --- |
| userid | integer | ID of the user who generated the entry. |
| query  | integer | Query ID. The query column can be used to join other system tables and views. |
| slice  | integer  | Number that identifies the slice where the query was running. |
| recordtime | timestamp | Time that the error was logged. |
| pid | integer | Process that logged the error. |
| ssh\_username | character(1024) | The SSH user name. |
| endpoint | character(1024) | The SSH endpoint. |
| command | character(4096) | The complete SSH command. |
| error | character(1024) | The error message. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
