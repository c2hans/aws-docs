---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-list-mpts-output-statuses-example.html
---

# Example
<a name="working-with-mpts-get-list-mpts-output-statuses-example"></a>

This request returns information for the two MPTS outputs that exist in the cluster.

```
GET http://198.51.100.0/mpts/statuses
--------------------------------------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<mpts_statuses href="/mpts/statuses" product="AWS Elemental Conductor Live version="3.3.nnnnn">
  <mpts_status>
    <id type="integer">1</id>
    <status>running</status>
  </mpts_status>
  <mpts_status>
    <id type="integer">4</id>
    <status>running</status>
  </mpts_status>
</mpts_statuses>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
