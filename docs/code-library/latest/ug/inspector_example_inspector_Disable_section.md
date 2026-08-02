---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/inspector_example_inspector_Disable_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `Disable` with an AWS SDK
<a name="inspector_example_inspector_Disable_section"></a>

The following code example shows how to use `Disable`.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/inspector#code-examples).

```
    /**
     * Asynchronously disables AWS Inspector for the specified accounts and resource types.
     *
     * @param accountIds a {@link List} of AWS account IDs for which to disable Inspector;
     *                   may be {@code null} or empty to target the current account
     * @return a {@link CompletableFuture} that, when completed, returns a {@link String}
     *         summarizing the disable results for each account
     * @throws CompletionException if the disable operation fails due to validation errors,
     *                             service errors, or other exceptions
     * @see <a href="https://docs.aws.amazon.com/inspector/latest/APIReference/API_Disable.html">
     *      AWS Inspector2 Disable API</a>
     */
    public CompletableFuture<String> disableInspectorAsync(List<String> accountIds) {

        // The resource types to disable.
        List<ResourceScanType> resourceTypes = List.of(
                ResourceScanType.EC2,
                ResourceScanType.ECR,
                ResourceScanType.LAMBDA,
                ResourceScanType.LAMBDA_CODE
        );

        // Build the request.
        DisableRequest.Builder requestBuilder = DisableRequest.builder()
                .resourceTypes(resourceTypes);

        if (accountIds != null && !accountIds.isEmpty()) {
            requestBuilder.accountIds(accountIds);
        }

        DisableRequest request = requestBuilder.build();

        return getAsyncClient().disable(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();
                        if (cause instanceof ValidationException) {
                            throw new CompletionException(
                                    "Inspector may already be disabled for this account: %s".formatted(cause.getMessage()),
                                    cause
                            );
                        }

                        if (cause instanceof Inspector2Exception) {
                            Inspector2Exception e = (Inspector2Exception) cause;
                            throw new CompletionException(
                                    "AWS Inspector2 service error: %s".formatted(e.awsErrorDetails().errorMessage()),
                                    cause
                            );
                        }

                        throw new CompletionException(
                                "Failed to disable Inspector: %s".formatted(exception.getMessage()),
                                exception
                        );
                    }
                })
                .thenApply(response -> {
                    StringBuilder summary = new StringBuilder("Disable results:\n");

                    if (response.accounts() == null || response.accounts().isEmpty()) {
                        summary.append("Inspector may already be disabled for all target accounts.");
                        return summary.toString();
                    }

                    for (Account account : response.accounts()) {
                        String accountId = account.accountId() != null ? account.accountId() : "Unknown";
                        String status = account.status() != null ? account.statusAsString() : "Unknown";
                        summary.append(" • Account: ").append(accountId)
                                .append(" → Status: ").append(status).append("\n");
                    }

                    return summary.toString();
                });
    }
```
+  For API details, see [Disable](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/Disable) in *AWS SDK for Java 2.x API Reference*.

------
