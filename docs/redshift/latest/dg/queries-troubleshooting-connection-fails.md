---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/queries-troubleshooting-connection-fails.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Connection fails
<a name="queries-troubleshooting-connection-fails"></a>

Your query connection can fail because for the following reasons. We suggest the following troubleshooting approaches.

**Client cannot connect to server**
If you are using SSL or server certificates, first remove this complexity while you troubleshoot the connection issue. Then add SSL or server certificates back when you have found a solution. For more information, go to [Configure Security Options for Connections](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html) in the *Amazon Redshift Management Guide.*

**Connection is refused**
Generally, when you receive an error message indicating that there is a failure to establish a connection, it means that there is an issue with the permission to access the cluster. For more information, go to [The connection is refused or fails](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-refusal-failure-issues.html) in the *Amazon Redshift Management Guide.*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
