---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_SubmitJob_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `SubmitJob` with an AWS SDK or CLI
<a name="batch_example_batch_SubmitJob_section"></a>

The following code examples show how to use `SubmitJob`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Learn the basics](batch_example_batch_Scenario_section.md)
+  [Getting started with batch processing and serverless containers](batch_example_fargate_GettingStarted_section.md)

------
#### [ CLI ]

**AWS CLI**
**To submit a job**
This example submits a simple container job called example to the HighPriority job queue.
Command:

```
aws batch submit-job --job-name {{example}} --job-queue {{HighPriority}}  --job-definition {{sleep60}}
```
Output:

```
{
    "jobName": "example",
    "jobId": "876da822-4198-45f2-a252-6cea32512ea8"
}
```
+  For API details, see [SubmitJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/submit-job.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/batch#code-examples).

```
    /**
     * Submits a job asynchronously to the AWS Batch service.
     *
     * @param jobDefinitionName the name of the job definition to use
     * @param jobQueueName the name of the job queue to submit the job to
     * @param jobARN the Amazon Resource Name (ARN) of the job definition
     * @return a CompletableFuture that, when completed, contains the job ID of the submitted job
     */
    public CompletableFuture<String> submitJobAsync(String jobDefinitionName, String jobQueueName, String jobARN) {
        SubmitJobRequest jobRequest = SubmitJobRequest.builder()
            .jobDefinition(jobARN)
            .jobName(jobDefinitionName)
            .jobQueue(jobQueueName)
            .build();

        CompletableFuture<SubmitJobResponse> responseFuture = getAsyncClient().submitJob(jobRequest);
        responseFuture.whenComplete((response, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Unexpected error occurred: " + ex.getMessage(), ex);
            }
        });

        return responseFuture.thenApply(SubmitJobResponse::jobId);
    }
```
+  For API details, see [SubmitJob](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/SubmitJob) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def submit_job(self, job_name: str, job_queue: str, job_definition: str) -> dict:
        """
        Submits a job to a job queue.

        :param job_name: A descriptive name for the job.
        :param job_queue: The job queue name or ARN.
        :param job_definition: The job definition name:revision or ARN.
        :return: A dictionary with the job name, ID, and ARN.
        """
        try:
            response = self.batch_client.submit_job(
                jobName=job_name,
                jobQueue=job_queue,
                jobDefinition=job_definition,
            )
            logger.info(
                "Submitted job %s (ID: %s): %s",
                response["jobName"],
                response["jobId"],
                response.get("jobArn", ""),
            )
            return response
        except ClientError as err:
            logger.error(
                "Error submitting job %s: %s",
                job_name,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [SubmitJob](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/SubmitJob) in *AWS SDK for Python (Boto3) API Reference*.

------
