---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/close-server.html
---

# close-servers
<a name="close-server"></a>

Closes one or more Amazon DCV servers. When you close a Amazon DCV server, you make it unavailable for Amazon DCV session placement. You can't create Amazon DCV sessions on closed servers. Closing a server ensures that no sessions are running on it and that users can't create new sessions on it.

**Topics**
+ [Synopsis](#synopsis)
+ [Options](#options)
+ [Example](#example)

## Synopsis
<a name="synopsis"></a>

```
close-servers
--server-ids {{<value>}}
[--force]
```

## Options
<a name="options"></a>

**`--server-ids`**
The comma-separated list of IDs of the Amazon DCV servers to close.
Type: String
Required: Yes

**`--force`**
Operation that forces the server to close. By default, this is disabled.
Type: Boolean
Required: No

## Example
<a name="example"></a>

```
dcvsm close-servers --server-ids "server123,server456"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
