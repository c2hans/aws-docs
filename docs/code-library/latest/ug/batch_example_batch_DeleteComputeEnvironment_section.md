---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_DeleteComputeEnvironment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteComputeEnvironment` with an AWS SDK or CLI
<a name="batch_example_batch_DeleteComputeEnvironment_section"></a>

The following code examples show how to use `DeleteComputeEnvironment`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Learn the basics](batch_example_batch_Scenario_section.md)
+  [Getting started with batch processing and serverless containers](batch_example_fargate_GettingStarted_section.md)

------
#### [ CLI ]

**AWS CLI**
**To delete a compute environment**
This example deletes the P2OnDemand compute environment.
Command:

```
aws batch delete-compute-environment --compute-environment {{P2OnDemand}}
```
+  For API details, see [DeleteComputeEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-compute-environment.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/batch#code-examples).

```
    public CompletableFuture<DeleteComputeEnvironmentResponse> deleteComputeEnvironmentAsync(String computeEnvironmentName) {
        DeleteComputeEnvironmentRequest deleteComputeEnvironment = DeleteComputeEnvironmentRequest.builder()
            .computeEnvironment(computeEnvironmentName)
            .build();

        return getAsyncClient().deleteComputeEnvironment(deleteComputeEnvironment)
            .whenComplete((response, ex) -> {
                if (ex != null) {
                    Throwable cause = ex.getCause();
                    if (cause instanceof BatchException) {
                        throw new RuntimeException(cause);
                    } else {
                        throw new RuntimeException("Unexpected error: " + cause.getMessage(), cause);
                    }
                }
            });
    }
```
+  For API details, see [DeleteComputeEnvironment](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DeleteComputeEnvironment) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def delete_compute_environment(self, compute_environment: str) -> None:
        """
        Deletes a compute environment.

        :param compute_environment: The compute environment name or ARN to delete.
        """
        try:
            self.batch_client.delete_compute_environment(
                computeEnvironment=compute_environment
            )
            logger.info("Deleted compute environment %s.", compute_environment)
        except ClientError as err:
            logger.error(
                "Error deleting compute environment %s: %s",
                compute_environment,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DeleteComputeEnvironment](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DeleteComputeEnvironment) in *AWS SDK for Python (Boto3) API Reference*.

------
