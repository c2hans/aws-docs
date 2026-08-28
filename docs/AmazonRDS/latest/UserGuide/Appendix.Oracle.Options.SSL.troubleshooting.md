---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.troubleshooting.html
---

# Troubleshooting SSL connections
<a name="Appendix.Oracle.Options.SSL.troubleshooting"></a>

You might query your database and receive the `ORA-28860` error.

```
ORA-28860: Fatal SSL error
28860. 00000 - "Fatal SSL error"
*Cause: An error occurred during the SSL connection to the peer. It is likely that this side sent data which the peer rejected.
*Action: Enable tracing to determine the exact cause of this error.
```

This error occurs when the client attempts to connect using a version of TLS that the server doesn't support. To avoid this error, edit the sqlnet.ora and set `SSL_VERSION` to the correct TLS version. For more information, see [Oracle Support Document 2748438.1](https://support.oracle.com/epmos/faces/DocumentDisplay?id=2748438.1) in My Oracle Support.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
