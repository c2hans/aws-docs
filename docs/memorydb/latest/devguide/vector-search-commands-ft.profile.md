---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.profile.html
---

# FT.PROFILE
<a name="vector-search-commands-ft.profile"></a>

Run a query and return profile information about that query.

**Syntax**

```
FT.PROFILE

<index>
SEARCH | AGGREGATE
[LIMITED]
QUERY <query ....>
```

**Return**

A two-element array. The first element is the result of the `FT.SEARCH` or `FT.AGGREGATE` command that was profiled. The second element is an array of performance and profiling information.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
