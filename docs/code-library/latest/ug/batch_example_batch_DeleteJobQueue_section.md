---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_DeleteJobQueue_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteJobQueue` with an AWS SDK or CLI
<a name="batch_example_batch_DeleteJobQueue_section"></a>

The following code examples show how to use `DeleteJobQueue`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Learn the basics](batch_example_batch_Scenario_section.md)
+  [Getting started with batch processing and serverless containers](batch_example_fargate_GettingStarted_section.md)

------
#### [ CLI ]

**AWS CLI**
**To delete a job queue**
This example deletes the GPGPU job queue.
Command:

```
aws batch delete-job-queue --job-queue {{GPGPU}}
```
+  For API details, see [DeleteJobQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-job-queue.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/batch#code-examples).

```
    /**
     * Deletes a Batch job queue asynchronously.
     *
     * @param jobQueueArn The Amazon Resource Name (ARN) of the job queue to delete.
     * @return A CompletableFuture that represents the asynchronous deletion of the job queue.
     *         The future completes when the job queue has been successfully deleted or if an error occurs.
     *         If successful, the future will be completed with a {@code Void} value.
     *         If an error occurs, the future will be completed exceptionally with the thrown exception.
     */
    public CompletableFuture<Void> deleteJobQueueAsync(String jobQueueArn) {
        DeleteJobQueueRequest deleteRequest = DeleteJobQueueRequest.builder()
            .jobQueue(jobQueueArn)
            .build();

        CompletableFuture<DeleteJobQueueResponse> responseFuture = getAsyncClient().deleteJobQueue(deleteRequest);
        return responseFuture.whenComplete((deleteResponse, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Failed to delete job queue: " + ex.getMessage(), ex);
            }
        }).thenApply(deleteResponse -> null);
    }
```
+  For API details, see [DeleteJobQueue](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DeleteJobQueue) in *AWS SDK for Java 2.x API Reference*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
