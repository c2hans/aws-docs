---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/arrays.html
---

# Arrays
<a name="arrays"></a>

In a POST or PUT, an array must include the property **type="array"**. For example:

```
<?xml version="1.0" encoding="UTF-8"?>
<hosts type="array">
  <host>10.4.136.15</host>
  <host>10.4.136.[90-92]</host>
</hosts>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
