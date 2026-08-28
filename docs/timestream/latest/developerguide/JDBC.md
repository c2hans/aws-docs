---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/JDBC.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# JDBC
<a name="JDBC"></a>

 You can use a Java Database Connectivity (JDBC) connection to connect Timestream for LiveAnalytics to your business intelligence tools and other applications, such as [SQL Workbench](https://www.sql-workbench.eu/). The Timestream for LiveAnalytics JDBC driver currently supports SSO with Okta and Microsoft Azure AD.

**Topics**
+ [Configuring the JDBC driver for Timestream for LiveAnalytics](JDBC.configuring.md)
+ [Connection properties](JDBC.connection-properties.md)
+ [JDBC URL examples](JDBC.url-examples.md)
+ [Setting up Timestream for LiveAnalytics JDBC single sign-on authentication with Okta](JDBC.SSOwithOkta.md)
+ [Setting up Timestream for LiveAnalytics JDBC single sign-on authentication with Microsoft Azure AD](JDBC.withAzureAD.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
