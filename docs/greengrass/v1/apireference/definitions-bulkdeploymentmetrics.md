---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-bulkdeploymentmetrics.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# BulkDeploymentMetrics
<a name="definitions-bulkdeploymentmetrics"></a>

```
{
"RecordsProcessed": 0,
"InvalidInputRecords": 0,
"RetryAttempts": 0
}
```

BulkDeploymentMetrics
Relevant metrics on input records processed during bulk deployment.
type: object

RecordsProcessed
The total number of group records from the input file that have been processed or attempted so far.
type: integer

InvalidInputRecords
The total number of records that returned a non-retryable error. For example, this can occur if a group record from the input file uses an invalid format or specifies a nonexistent group version, or if the execution role doesn't grant permission to deploy a group or group version.
type: integer

RetryAttempts
The total number of deployment attempts that returned a retryable error. For example, a retry is triggered if the attempt to deploy a group returns a throttling error. `StartBulkDeployment` retries a group deployment up to five times.
type: integer

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
