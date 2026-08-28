---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-modify-spts-program-example.html
---

# Example
<a name="working-with-members-of-mpts-modify-spts-program-example"></a>

This example changes the MPTS member with the ID 6 in the MPTS that has the ID 2. The request changes one of the PID values.

```
PUT http://198.51.100.0/mpts/2/mpts_members/6
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<mpts_member>
  <pid_map>
    <pmt_pid>600</pmt_pid>
  </pid_map>
</mpts_member>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
