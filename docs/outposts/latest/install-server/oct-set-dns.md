---
source_url: https://docs.aws.amazon.com/outposts/latest/install-server/oct-set-dns.html
---

# set-dns
<a name="oct-set-dns"></a>

The **set-dns** command sets the DNS (Domain Name Server) IP address.

**Syntax**

```
Outpost>set-dns {{dns}}
```
For example: `set-dns {{8.8.8.8}}`

**Parameters**
This command requires the DNS address.

**Example output: Success**

```
Outpost> set-dns
---
success: True
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
