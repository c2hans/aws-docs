---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/inspector_example_inspector_DeleteFilter_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteFilter` with an AWS SDK
<a name="inspector_example_inspector_DeleteFilter_section"></a>

The following code example shows how to use `DeleteFilter`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](inspector_example_inspector_Scenario_section.md)

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/inspector#code-examples).

```
    /**
     * Deletes an AWS Inspector2 filter.
     *
     * @param filterARN The ARN of the filter to delete.
     */
    public CompletableFuture<Void> deleteFilterAsync(String filterARN) {
        return getAsyncClient().deleteFilter(
                        DeleteFilterRequest.builder()
                                .arn(filterARN)
                                .build()
                )
                .handle((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause() != null ? exception.getCause() : exception;

                        if (cause instanceof ResourceNotFoundException rnfe) {
                            String msg = "Filter not found for ARN: %s".formatted(filterARN);
                            logger.warn(msg, rnfe);
                            throw new CompletionException(msg, rnfe);
                        }

                        throw new RuntimeException("Failed to delete the filter: " + cause, cause);
                    }
                    return null;
                });
    }
```
+  For API details, see [DeleteFilter](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/DeleteFilter) in *AWS SDK for Java 2.x API Reference*.

------
