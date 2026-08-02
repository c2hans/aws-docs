---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_DeregisterJobDefinition_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeregisterJobDefinition` with an AWS SDK or CLI
<a name="batch_example_batch_DeregisterJobDefinition_section"></a>

The following code examples show how to use `DeregisterJobDefinition`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](batch_example_batch_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To deregister a job definition**
This example deregisters a job definition called sleep10.
Command:

```
aws batch deregister-job-definition --job-definition {{sleep10}}
```
+  For API details, see [DeregisterJobDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/deregister-job-definition.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/batch#code-examples).

```
    /**
     * Deregisters a job definition asynchronously.
     *
     * @param jobDefinition the name of the job definition to be deregistered
     * @return a CompletableFuture that completes when the job definition has been deregistered
     * or an exception has occurred
     */
    public CompletableFuture<DeregisterJobDefinitionResponse> deregisterJobDefinitionAsync(String jobDefinition) {
        DeregisterJobDefinitionRequest jobDefinitionRequest = DeregisterJobDefinitionRequest.builder()
            .jobDefinition(jobDefinition)
            .build();

        CompletableFuture<DeregisterJobDefinitionResponse> responseFuture = getAsyncClient().deregisterJobDefinition(jobDefinitionRequest);
        responseFuture.whenComplete((response, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Unexpected error occurred: " + ex.getMessage(), ex);
            }
        });

        return responseFuture;
    }
```
+  For API details, see [DeregisterJobDefinition](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DeregisterJobDefinition) in *AWS SDK for Java 2.x API Reference*.

------
