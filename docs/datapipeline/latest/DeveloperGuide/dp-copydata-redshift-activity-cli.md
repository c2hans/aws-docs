---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-redshift-activity-cli.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Activity
<a name="dp-copydata-redshift-activity-cli"></a>

The last section in the JSON file is the definition of the activity that represents the work to perform. In this case, we use a `RedshiftCopyActivity` component to copy data from Amazon S3 to Amazon Redshift. For more information, see [RedshiftCopyActivity](dp-object-redshiftcopyactivity.md).

The `RedshiftCopyActivity` component is defined by the following fields:

```
{
  "id": "RedshiftCopyActivityId1",
  "input": {
    "ref": "S3DataNodeId1"
  },
  "schedule": {
    "ref": "ScheduleId1"
  },
  "insertMode": "KEEP_EXISTING",
  "name": "DefaultRedshiftCopyActivity1",
  "runsOn": {
    "ref": "Ec2ResourceId1"
  },
  "type": "RedshiftCopyActivity",
  "output": {
    "ref": "RedshiftDataNodeId1"
  }
},
```

`id`
The user-defined ID, which is a label for your reference only.

`input`
A reference to the Amazon S3 source file.

`schedule`
The schedule on which to run this activity.

`insertMode`
The insert type (`KEEP_EXISTING`, `OVERWRITE_EXISTING`, or `TRUNCATE`).

`name`
The user-defined name, which is a label for your reference only.

`runsOn`
The computational resource that performs the work that this activity defines.

`output`
A reference to the Amazon Redshift destination table.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
