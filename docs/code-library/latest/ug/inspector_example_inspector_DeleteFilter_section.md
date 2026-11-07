---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/inspector_example_inspector_DeleteFilter_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteFilter` with an AWS SDK
<a name="inspector_example_inspector_DeleteFilter_section"></a>

The following code examples show how to use `DeleteFilter`.

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
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def delete_filter(self, filter_arn: str) -> None:
        """
        Deletes a findings filter.

        :param filter_arn: The ARN of the filter to delete.
        """
        try:
            self.inspector2_client.delete_filter(arn=filter_arn)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Filter %s was not found. Here's why: %s: %s",
                    filter_arn,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Couldn't delete filter %s. Here's why: %s: %s",
                    filter_arn,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeleteFilter](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/DeleteFilter) in *AWS SDK for Python (Boto3) API Reference*.

------
