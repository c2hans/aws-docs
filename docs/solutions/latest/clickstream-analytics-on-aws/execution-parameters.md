---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/execution-parameters.html
---

# Execution parameters
<a name="execution-parameters"></a>

 Execution parameters control how the transformation and enrichment jobs are orchestrated.

## Parameters
<a name="parameters"></a>

 You can configure the following **Execution parameters** after you turn on **Enable data processing**.

|  **Parameter**  |  **Description**  |  **Values**  |
| --- | --- | --- |
|  Data processing interval/Fixed Rate  |  Specify the interval to batch the data for data processing by fixed rate  | 1 hour<br />12 hours<br />1 day |
|  Data processing interval/Cron Expression  |  Specify the interval to batch the data for data processing by cron expression  | cron(0 \* \* ? \*) <br />cron(0 0,12 \* ? \*)<br />cron(0 0 \* ? \*)  |
|  Event freshness  |  Specify the days after which the guidance will ignore the event data. For example, if you specify 3 days for this parameter, the guidance will ignore any event which arrived more than 3 days after the events are triggered  | 3 days<br />5 days<br />30 days  |

## Cron expression syntax
<a name="cron-expression-syntax"></a>

 Syntax

 cron(minutes hours day-of-month month day-of-week year)

 For more information, refer to [Cron-based schedules](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html?icmpid=docs_console_unmapped#cron-based).

## Config Spark job parameters
<a name="config-spark-job-parameters"></a>

 By default, the Clickstream pipeline automatically adjusts EMR job parameters based on the dataset volume that requires processing. In most of time, you do not need to adjust the EMR job parameters, but if you want to override the EMR job parameters, you can put `spark-config.json` file in S3 bucket to set your job parameters.

 To add your customized the EMR job parameters, you can add a file `s3://{PipelineS3Bucket}/{PipelineS3Prefix}{ProjectId}/config/spark-config.json` in the S3 bucket.

 Please replace `{PipelineS3Bucket}`, `{PipelineS3Prefix}`, and `{ProjectId}` with the values of your data pipeline. These values are found in the `Clickstream-DataProcessing-<uuid>` stack's `Parameters`.

 Also, you can get these values by running the below commands,

```
stackNames=$(aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --no-paginate  | jq -r '.StackSummaries[].StackName' | grep  Clickstream-DataProcessing  | grep -v Nested)

echo -e "$stackNames" | while read stackName; do
    aws cloudformation describe-stacks --stack-name $stackName  | jq '.Stacks[].Parameters' | jq 'map(select(.ParameterKey == "PipelineS3Bucket" or .ParameterKey == "PipelineS3Prefix" or .ParameterKey == "ProjectId"))'
done
```

 Here is an example of the file `spark-config.json`:

```
{
   "sparkConfig": [
        "spark.emr-serverless.executor.disk=200g",
        "spark.executor.instances=16",
        "spark.dynamicAllocation.initialExecutors=16",
        "spark.executor.memory=100g",
        "spark.executor.cores=16",
        "spark.network.timeout=10000000",
        "spark.executor.heartbeatInterval=10000000",
        "spark.shuffle.registration.timeout=120000",
        "spark.shuffle.registration.maxAttempts=5",
        "spark.shuffle.file.buffer=2m",
        "spark.shuffle.unsafe.file.output.buffer=1m"
    ],
    "inputRePartitions": 2000
}
```

 Please make sure your account has enough emr-serverless quotas, you can view the quotas via emr-serverless-quotas in the Region us-east-1. For more configurations, please refer to [Spark job properties](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-spark.html#spark-defaults) and application [worker config](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/app-behavior.html#worker-configs).
