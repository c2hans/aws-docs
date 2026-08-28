---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-ODBC-connecting-troubleshooting.html
---

# Troubleshooting connection with the ODBC driver
<a name="query-ODBC-connecting-troubleshooting"></a>

**Note**
If the username and password is already specified in the DSN, do not specify them again when the ODBC driver manager asks for them.

An error code of `01S02` with a message, `Re-writing {{(connection string option)}} (have you specified it several times?)` occurs when a connection string option is passed more than once in the connection string. Specifying an option more than once raises an error. When making a connection with a DSN and a connection string, if a connection option is already specified in the DSN, do not specify it again in the connection string.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
