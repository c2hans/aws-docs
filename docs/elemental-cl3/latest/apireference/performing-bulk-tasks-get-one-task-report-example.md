---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-get-one-task-report-example.html
---

# Example
<a name="performing-bulk-tasks-get-one-task-report-example"></a>

The response to this request provides information about the task\_report with the ID 5; three of its seven actions have completed. The bulk task with ID 3 belongs to Channel 13 and has succeeded, the bulk task with ID 4 belongs to Channel 15 and is pending, and so on.

```
GET http://198.51.100.0/task_reports
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<task_report>
 <created_at>2015-04-09T04:14:12-07:00</created_at>
 <description>Channel Start</description>
 <failed_count>0</failed_count>
 <id>5</id>
 <successful_count>3</successful_count>
 <task_count>7</task_count>
 <updated_at>2015-04-09T04:16:12-07:00</updated_at>
 <tasks type="array">
   <task>
     <id type="integer">3</id>
     <description>Channel Start for Channel 13</description>
     <state>successful</state>
     <message>Success</message>
   </task>
   <task>
     <id type="integer">4</id>
     <description>Channel Start for Channel 51</description>
     <state>pending</state>
     <message>Pending...</message>
   </task>
   <task>
.
.
.
   </task>
 </tasks>
</task_report>
```
