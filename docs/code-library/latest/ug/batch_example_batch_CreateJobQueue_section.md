---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_CreateJobQueue_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateJobQueue` with an AWS SDK or CLI
<a name="batch_example_batch_CreateJobQueue_section"></a>

The following code examples show how to use `CreateJobQueue`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Learn the basics](batch_example_batch_Scenario_section.md)
+  [Getting started with batch processing and serverless containers](batch_example_fargate_GettingStarted_section.md)

------
#### [ CLI ]

**AWS CLI**
**To create a low priority job queue with a single compute environment**
This example creates a job queue called LowPriority that uses the M4Spot compute environment.
Command:

```
aws batch create-job-queue --cli-input-json {{file://<path_to_json_file>/LowPriority.json}}
```
JSON file format:

```
{
  "jobQueueName": "LowPriority",
  "state": "ENABLED",
  "priority": 10,
  "computeEnvironmentOrder": [
    {
      "order": 1,
      "computeEnvironment": "M4Spot"
    }
  ]
}
```
Output:

```
{
    "jobQueueArn": "arn:aws:batch:us-east-1:012345678910:job-queue/LowPriority",
    "jobQueueName": "LowPriority"
}
```
**To create a high priority job queue with two compute environments**
This example creates a job queue called HighPriority that uses the C4OnDemand compute environment with an order of 1 and the M4Spot compute environment with an order of 2. The scheduler will attempt to place jobs on the C4OnDemand compute environment first.
Command:

```
aws batch create-job-queue --cli-input-json {{file://<path_to_json_file>/HighPriority.json}}
```
JSON file format:

```
{
  "jobQueueName": "HighPriority",
  "state": "ENABLED",
  "priority": 1,
  "computeEnvironmentOrder": [
    {
      "order": 1,
      "computeEnvironment": "C4OnDemand"
    },
    {
      "order": 2,
      "computeEnvironment": "M4Spot"
    }
  ]
}
```
Output:

```
{
    "jobQueueArn": "arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority",
    "jobQueueName": "HighPriority"
}
```
+  For API details, see [CreateJobQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-job-queue.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/batch#code-examples).

```
    /**
     * Creates a job queue asynchronously.
     *
     * @param jobQueueName the name of the job queue to create
     * @param computeEnvironmentName the name of the compute environment to associate with the job queue
     * @return a CompletableFuture that completes with the Amazon Resource Name (ARN) of the job queue
     */
    public CompletableFuture<String> createJobQueueAsync(String jobQueueName, String computeEnvironmentName) {
        if (jobQueueName == null || jobQueueName.isEmpty()) {
            throw new IllegalArgumentException("Job queue name cannot be null or empty");
        }
        if (computeEnvironmentName == null || computeEnvironmentName.isEmpty()) {
            throw new IllegalArgumentException("Compute environment name cannot be null or empty");
        }

        CreateJobQueueRequest request = CreateJobQueueRequest.builder()
            .jobQueueName(jobQueueName)
            .priority(1)
            .computeEnvironmentOrder(ComputeEnvironmentOrder.builder()
                .computeEnvironment(computeEnvironmentName)
                .order(1)
                .build())
            .build();

        CompletableFuture<CreateJobQueueResponse> response = getAsyncClient().createJobQueue(request);
        response.whenComplete((resp, ex) -> {
            if (ex != null) {
                String errorMessage = "Unexpected error occurred: " + ex.getMessage();
                throw new RuntimeException(errorMessage, ex);
            }
        });

        return response.thenApply(CreateJobQueueResponse::jobQueueArn);
    }
```
+  For API details, see [CreateJobQueue](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CreateJobQueue) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def create_job_queue(
        self,
        job_queue_name: str,
        compute_environment_name: str,
        priority: int = 1,
    ) -> dict:
        """
        Creates a job queue associated with a compute environment.

        :param job_queue_name: The name for the job queue.
        :param compute_environment_name: The compute environment to associate.
        :param priority: The priority of the job queue (default 1).
        :return: A dictionary with the job queue name and ARN.
        """
        try:
            response = self.batch_client.create_job_queue(
                jobQueueName=job_queue_name,
                state="ENABLED",
                priority=priority,
                computeEnvironmentOrder=[
                    {
                        "order": 1,
                        "computeEnvironment": compute_environment_name,
                    }
                ],
            )
            logger.info(
                "Created job queue %s: %s",
                response["jobQueueName"],
                response["jobQueueArn"],
            )
            return response
        except ClientError as err:
            logger.error(
                "Error creating job queue %s: %s",
                job_queue_name,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [CreateJobQueue](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateJobQueue) in *AWS SDK for Python (Boto3) API Reference*.

------
