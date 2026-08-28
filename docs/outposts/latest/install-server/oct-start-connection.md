---
source_url: https://docs.aws.amazon.com/outposts/latest/install-server/oct-start-connection.html
---

# start-connection
<a name="oct-start-connection"></a>

The **start-connection** command initiates a connection with the Outpost service in the Region for the Outposts server. This command sources the Signature Version 4 (SigV4) credentials from the environment variables you loaded with **export**. The connection runs asynchronously and returns immediately. To check the status of the connection, use [get-connection](oct-get-connection.md).

**Syntax**

```
Outpost>start-connection [{{index}}]
```

**Parameters**
This command takes an optional index. The valid values are 0 and 1.

**Example output: Connection is started**

```
is_started: True
asset_id: {{asset-id}}
connection_id: {{connection-id}}
timestamp: {{2021-10-01T23:30:26Z}}
checksum: {{checksum}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
