---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/inspector_example_inspector_ListCoverageStatistics_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListCoverageStatistics` with an AWS SDK
<a name="inspector_example_inspector_ListCoverageStatistics_section"></a>

The following code examples show how to use `ListCoverageStatistics`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](inspector_example_inspector_Scenario_section.md)

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/inspector#code-examples).

```
    /**
     * Retrieves and prints the coverage statistics using a paginator.
     */
    public CompletableFuture<String> listCoverageStatisticsAsync() {
        ListCoverageStatisticsRequest request = ListCoverageStatisticsRequest.builder()
                .build();

        return getAsyncClient().listCoverageStatistics(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();

                        if (cause instanceof ValidationException) {
                            throw new CompletionException(
                                    "Validation error listing coverage statistics: %s".formatted(cause.getMessage()),
                                    cause
                            );
                        }

                        if (cause instanceof Inspector2Exception) {
                            Inspector2Exception e = (Inspector2Exception) cause;

                            throw new CompletionException(
                                    "Inspector2 service error: %s".formatted(e.awsErrorDetails().errorMessage()),
                                    e
                            );
                        }

                        throw new CompletionException(
                                "Unexpected error listing coverage statistics: %s".formatted(exception.getMessage()),
                                exception
                        );
                    }
                })
                .thenApply(response -> {
                    List<Counts> countsList = response.countsByGroup();
                    StringBuilder sb = new StringBuilder();

                    if (countsList == null || countsList.isEmpty()) {
                        sb.append("No coverage statistics available.\n");
                        return sb.toString();
                    }

                    sb.append("Coverage Statistics:\n");

                    for (Counts c : countsList) {
                        sb.append("  Group: ").append(c.groupKey()).append("\n")
                                .append("    Total Count: ").append(c.count()).append("\n\n");
                    }

                    return sb.toString();
                });
    }
```
+  For API details, see [ListCoverageStatistics](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ListCoverageStatistics) in *AWS SDK for Java 2.x API Reference*.

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

    def list_coverage_statistics(
        self, group_by: Optional[str] = None
    ) -> dict[str, Any]:
        """
        Lists coverage statistics for the resources that Amazon Inspector scans.

        :param group_by: Optional value to group the counts by, such as RESOURCE_TYPE.
        :return: A dict with 'totalCounts' and 'countsByGroup'. If a
                 ValidationException occurs, it is logged and empty statistics
                 are returned.
        """
        try:
            stats = {"totalCounts": 0, "countsByGroup": list()}
            params = dict()
            if group_by is not None:
                params["groupBy"] = group_by
            paginator = self.inspector2_client.get_paginator("list_coverage_statistics")
            for page in paginator.paginate(**params):
                # totalCounts is the service-wide total, repeated on every page,
                # so it is assigned rather than summed across pages.
                stats["totalCounts"] = page.get("totalCounts", 0)
                stats["countsByGroup"].extend(page.get("countsByGroup", list()))
            return stats
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing coverage statistics. "
                    "Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return {"totalCounts": 0, "countsByGroup": list()}
            logger.error(
                "Couldn't list coverage statistics. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [ListCoverageStatistics](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListCoverageStatistics) in *AWS SDK for Python (Boto3) API Reference*.

------
