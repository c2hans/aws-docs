---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.aliasupdate.html
---

# FT.ALIASUPDATE
<a name="vector-search-commands-ft.aliasupdate"></a>

Update an existing alias to point to a different physical index. This command only affects future references to the alias. Currently in-progress operations (FT.SEARCH, FT.AGGREGATE) are unaffected by this command.

**Syntax**

```
FT.ALIASUPDATE <alias> <index>
```

**Return**

Returns a simple string OK message or an error reply.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
