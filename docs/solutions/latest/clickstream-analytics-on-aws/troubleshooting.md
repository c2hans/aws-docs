---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides troubleshooting instructions for deploying and using the guidance.

## Problem: Deployment failure due to "Invalid Logging Configuration: The CloudWatch Logs Resource Policy size was exceeded"
<a name="problem-deployment-failure-due-to-invalid-logging-configuration-the-cloudwatch-logs-resource-policy-size-was-exceeded"></a>

 If you encounter a deployment failure due to creating CloudWatch log group with an error message like the one below,

 `Cannot enable logging. Policy document length breaking Cloudwatch Logs Constraints, either < 1 or > 5120 (Service: AmazonApiGatewayV2; Status Code: 400; Error Code: BadRequestException; Request ID: xxx-yyy-zzz; Proxy: null) `

 **Resolution:**

 [CloudWatch Logs resource policies are limited to 5120 characters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-CWL). The remediation is merging or removing useless policies, then updating the resource policies of CloudWatch logs to reduce the number of policies.

 Below is a sample command to reset resource policy of CloudWatch logs:

```
aws logs put-resource-policy --policy-name AWSLogDeliveryWrite20150319 \
--policy-document '
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AWSLogDeliveryWrite2",
      "Effect": "Allow",
      "Principal": {
        "Service": "delivery.logs.amazonaws.com"
      },
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": [
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<your AWS account id>"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:logs:<AWS region>:<your AWS account id>:*"
        }
      }
    }
  ]
}
'
```

## Problem: Cannot delete the CloudFormation stacks created for the Clickstream pipeline
<a name="problem-cannot-delete-the-cloudformation-stacks-created-for-the-clickstream-pipeline"></a>

 If you encounter a failure with an error message like the one below when deleting the CloudFormation stacks created for the Clickstream pipeline,

 `Role arn:aws:iam::<your AWS account id>:role/<stack nam>-ClickStreamApiStackActionSta-<random suffix> is invalid or cannot be assumed`

 **Resolution:**

 It results from deleting the web console stack for this guidance before the CloudFormation stacks are made for the Clickstream pipeline.

 Please create a new IAM role with the identical name mentioned in the above error message and trust the CloudFormation service with sufficient permission to delete those stacks.

**Note**
You can delete the IAM role after successfully removing those CloudFormation stacks.

## Problem: Reporting stack(Clickstream-Reporting-xxx) deployment fail
<a name="problem-reporting-stack-deployment-fail"></a>

Reporting stack deployment failed with message like

```
Connection attempt timed out
```

And it happened when creating DataSource(AWS::QuickSight::DataSource).

**Resolution:**

Login guidance web console and click "Retry" button in pipeline detail information page.

## Problem: Clickstream-DataModelingRedshift-xxxxx stack upgrade failed in UPDATE\_ROLLBACK\_FAILED
<a name="probem-clickstream-datamodelingredshift-stack-upgrade-failed"></a>

When upgrading from 1.0.x to the latest version, if the CloudFormation stack `Clickstream-DataModelingRedshift-xxxxx` is in the `UPDATE_ROLLBACK_FAILED` state, you need to manually fix it by following the steps below.

**Resolution:**

1. In the Cloudformation **Resource** tab, find the Lambda Function name with logical ID `CreateApplicationSchemasCreateSchemaForApplicationsFn`.

1. Update the `fn_name` and `aws_region` in below script and execute it in a shell terminal. Make sure you have AWS CLI installed and configured.

   ```
   aws_region=<us-east-1> # replace this with your AWS region, and remove '<', '>'
   fn_name=<fn_name_to_replace> # replace this with actual function name in step 1 and remove '<', '>'

   cat <<END | > ./index.mjs
   export const handler = async (event) => {
     console.log('No ops!')
     const response = {
       Status: 'SUCCESS',
       Data: {
         DatabaseName: '',
         RedshiftBIUsername: ''
       }
     };
     return response;
   };
   END

   rm ./noops-lambda.zip > /dev/null 2>&1
   zip ./noops-lambda.zip ./index.mjs

   aws lambda update-function-code --function-name ${fn_name} \
    --zip-file fileb://./noops-lambda.zip \
    --region ${aws_region} | tee /dev/null
   ```

1. In the Cloudformation web console, choose **Stack actions** and **Continue update rollback**.

1. Wait until the stack status is `UPDATE_ROLLBACK_COMPLETE`.

1. Retry the upgrade from the guidance web console.

## Problem: Can not sink data to MSK cluster, got "InvalidReplicationFactor (Broker: Invalid replication factor)" log in Ingestion Server
<a name="problem-can-not-sink-data-to-msk-cluster-got-invalidreplicationfactor-broker-invalid-replication-factor-log-in-ingestion-server"></a>

 If you notice that data can not be sunk into S3 through MSK cluster, and the error message in log of Ingestion Server (ECS) worker task is as below:

`Message production error: InvalidReplicationFactor (Broker: Invalid replication factor)`

 **Resolution:**

 This is caused by replication factor larger than available brokers, please edit the MSK cluster configuration, set `default.replication.factor` not larger than the total number of brokers.

## Problem: data processing job failure
<a name="problem-data-processing-job-failure"></a>

If the data processing job implemented by EMR serverless fails with the below errors:
+ IOException: No space left on device

  ```
  Job failed, please check complete logs in configured logging destination. ExitCode: 1. Last few exceptions: Caused by: java.io.IOException: No space left on device Exception in thread "main" org.apache.spark.SparkException:
  ```
+ ExecutorDeadException

  ```
  Job failed, please check complete logs in configured logging destination. ExitCode: 1. Last few exceptions: Caused by: org.apache.spark.ExecutorDeadException: The relative remote executor(Id: 34), which maintains the block data to fetch is dead. org.apache.spark.shuffle.FetchFailedException Caused by: org.apache.spark.SparkException: Job aborted due to stage failure: ShuffleMapStage
  ```
+ Could not find CoarseGrainedScheduler

  ```
  Job failed, please check complete logs in configured logging destination. ExitCode: 1. Last few exceptions: org.apache.spark.SparkException: Could not find CoarseGrainedScheduler.
  ```

You need to tune the EMR job default configuration. For more information, refer to [configure execution parameters](https://awslabs.github.io/clickstream-analytics-on-aws/en/1.2.x/pipeline-mgmt/data-processing/configure-execution-para/#config-spark-job-parameters).

## Problem: data loading workflow failure due to meeting the 25,000 events limit in a single execution history
<a name="problem-data-loading-workflow-failure"></a>

It's caused by the large volume of data to be loaded or the Redshift load being very high. You could mitigate this error by increasing the compute resources of Redshift (for example, RPUs for Redshift serverless) or reducing the [data processing interval](execution-parameters.md). Then [restart the data-loading workflow](frequently-asked-questions.md#data-pipeline-faq).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
