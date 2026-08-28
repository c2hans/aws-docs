---
source_url: https://docs.aws.amazon.com/dcv/latest/gw-admin/manage-start.html
---

# Starting the Connection Gateway
<a name="manage-start"></a>

Manually start the Connection Gateway service using the command line.

**To start the Connection Gateway service**
Use the following command:

```
$ sudo systemctl start dcv-connection-gateway
```

Configure the Connection Gateway service to start automatically.

**To configure the Connection Gateway service to start automatically**
Use the following command:

```
$ sudo systemctl enable dcv-connection-gateway
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
