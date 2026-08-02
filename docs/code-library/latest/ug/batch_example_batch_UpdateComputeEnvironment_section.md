---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_UpdateComputeEnvironment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateComputeEnvironment` with an AWS SDK or CLI
<a name="batch_example_batch_UpdateComputeEnvironment_section"></a>

The following code examples show how to use `UpdateComputeEnvironment`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Learn the basics](batch_example_batch_Scenario_section.md)
+  [Getting started with batch processing and serverless containers](batch_example_fargate_GettingStarted_section.md)

------
#### [ CLI ]

**AWS CLI**
**To update a compute environment**
This example disables the P2OnDemand compute environment so it can be deleted.
Command:

```
aws batch update-compute-environment --compute-environment {{P2OnDemand}} --state {{DISABLED}}
```
Output:

```
{
    "computeEnvironmentName": "P2OnDemand",
    "computeEnvironmentArn": "arn:aws:batch:us-east-1:012345678910:compute-environment/P2OnDemand"
}
```
+  For API details, see [UpdateComputeEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-compute-environment.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/batch#code-examples).

```
    /**
     * Disables the specified compute environment asynchronously.
     *
     * @param computeEnvironmentName the name of the compute environment to disable
     * @return a CompletableFuture that completes when the compute environment is disabled
     */
    public CompletableFuture<UpdateComputeEnvironmentResponse> disableComputeEnvironmentAsync(String computeEnvironmentName) {
        UpdateComputeEnvironmentRequest updateRequest = UpdateComputeEnvironmentRequest.builder()
            .computeEnvironment(computeEnvironmentName)
            .state(CEState.DISABLED)
            .build();

        CompletableFuture<UpdateComputeEnvironmentResponse> responseFuture = getAsyncClient().updateComputeEnvironment(updateRequest);
        responseFuture.whenComplete((response, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Failed to disable compute environment: " + ex.getMessage(), ex);
            }
        });

        return responseFuture;
    }
```
+  For API details, see [UpdateComputeEnvironment](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateComputeEnvironment) in *AWS SDK for Java 2.x API Reference*.

------
