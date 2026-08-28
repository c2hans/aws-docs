---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-messages-example2.html
---

# Example 2
<a name="monitoring-query-alerts-messages-get-a-list-of-messages-example2"></a>

The following example requests all *active code 30 *(node activated) messages from *node 13*, limiting the responses to *20**per page.*

```
GET http://10.4.138.230/messages?status=active&code=30&node=13&per_page=20
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
