---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-get-list-of-task-reports-example.html
---

# Example
<a name="performing-bulk-tasks-get-list-of-task-reports-example"></a>

The response to this request provides information on two bulk tasks. One task\_report has the ID 4; all of its 10 actions have completed. The other task\_report has the ID 5; three of its seven actions have completed.

```
GET http://198.51.100.0/task_reports
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<task_reports>
  <task_report>
   <created_at>2015-04-09T04:12:12-07:00</created_at>
   <description>Channel Start</description>
   <failed_count>1</failed_count>
   <id>4</id>
   <successful_count>9</successful_count>
   <task_count>10</task_count>
   <updated_at>2015-04-09T04:12:13-07:00</updated_at>
  </task_report>
  <task_report>
   <created_at>2015-04-09T04:14:12-07:00</created_at>
   <description>Channel Start</description>
   <failed_count>0</failed_count>
   <id>5</id>
   <successful_count>3</successful_count>
   <task_count>7</task_count>
   <updated_at>2015-04-09T04:16:12-07:00</updated_at>
  </task_report>
</task_reports>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
