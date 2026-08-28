---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/open-server.html
---

# open-servers
<a name="open-server"></a>

Opens one or more Amazon DCV servers. Before you can create sessions on a Amazon DCV server, you must change the server's state to open. After the Amazon DCV server is open, you can create Amazon DCV sessions on the server.

**Topics**
+ [Synopsis](#synopsis)
+ [Options](#options)
+ [Example](#example)

## Synopsis
<a name="synopsis"></a>

```
open-servers
--server-ids {{<value>}}
```

## Options
<a name="options"></a>

**`--server-ids`**
The comma-separated list of IDs of the Amazon DCV servers to open.
Type: String
Required: Yes

## Example
<a name="example"></a>

```
./dcvsm open-servers --server-ids "server123,server456"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
