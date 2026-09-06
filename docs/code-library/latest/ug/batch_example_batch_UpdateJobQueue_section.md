---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_UpdateJobQueue_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateJobQueue` with an AWS SDK or CLI
<a name="batch_example_batch_UpdateJobQueue_section"></a>

The following code examples show how to use `UpdateJobQueue`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Learn the basics](batch_example_batch_Scenario_section.md)
+  [Getting started with batch processing and serverless containers](batch_example_fargate_GettingStarted_section.md)

------
#### [ CLI ]

**AWS CLI**
**To update a job queue**
This example disables a job queue so that it can be deleted.
Command:

```
aws batch update-job-queue --job-queue {{GPGPU}} --state {{DISABLED}}
```
Output:

```
{
    "jobQueueArn": "arn:aws:batch:us-east-1:012345678910:job-queue/GPGPU",
    "jobQueueName": "GPGPU"
}
```
+  For API details, see [UpdateJobQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-job-queue.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/batch#code-examples).

```
    /**
     * Disables the specified job queue asynchronously.
     *
     * @param jobQueueArn the Amazon Resource Name (ARN) of the job queue to be disabled
     * @return a {@link CompletableFuture} that completes when the job queue update operation is complete,
     *         or completes exceptionally if an error occurs during the operation
     */
    public CompletableFuture<Void> disableJobQueueAsync(String jobQueueArn) {
        UpdateJobQueueRequest updateRequest = UpdateJobQueueRequest.builder()
            .jobQueue(jobQueueArn)
            .state(JQState.DISABLED)
            .build();

        CompletableFuture<UpdateJobQueueResponse> responseFuture = getAsyncClient().updateJobQueue(updateRequest);
        return responseFuture.whenComplete((updateResponse, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Failed to update job queue: " + ex.getMessage(), ex);
            }
        }).thenApply(updateResponse -> null);
    }
```
+  For API details, see [UpdateJobQueue](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateJobQueue) in *AWS SDK for Java 2.x API Reference*.

------
