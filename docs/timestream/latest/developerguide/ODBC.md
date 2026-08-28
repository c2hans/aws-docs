---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/ODBC.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# ODBC
<a name="ODBC"></a>

The open-source [ODBC driver](https://github.com/awslabs/amazon-timestream-odbc-driver/tree/main) for Amazon Timestream for LiveAnalytics provides an SQL-relational interface to Timestream for LiveAnalytics for developers and enables connectivity from business intelligence (BI) tools such as Power BI Desktop and Microsoft Excel. The Timestream for LiveAnalytics ODBC driver is currently available on [Windows, macOS and Linux](https://github.com/awslabs/amazon-timestream-odbc-driver/releases), and also supports SSO with Okta and Microsoft Azure Active Directory (AD).

For more information, see [Amazon Timestream for LiveAnalytics ODBC driver documentation on GitHub](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/index.md).

**Topics**
+ [Setting up the Timestream for LiveAnalytics ODBC driver](ODBC-setup.md)
+ [Connection string syntax and options for the ODBC driver](ODBC-connecting.md)
+ [Connection string examples for the Timestream for LiveAnalytics ODBC driver](ODBC-connecting-examples.md)
+ [Troubleshooting connection with the ODBC driver](ODBC-connecting-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
