---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/inspector_example_inspector_BatchGetFindingDetails_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `BatchGetFindingDetails` with an AWS SDK
<a name="inspector_example_inspector_BatchGetFindingDetails_section"></a>

The following code example shows how to use `BatchGetFindingDetails`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](inspector_example_inspector_Scenario_section.md)

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/inspector#code-examples).

```
    /**
     * Retrieves detailed information about a specific AWS Inspector2 finding asynchronously.
     *
     * @param findingArn The ARN of the finding to look up.
     * @return A {@link CompletableFuture} that, when completed, provides a formatted string
     * containing all available details for the finding.
     * @throws RuntimeException if the async call to Inspector2 fails.
     */
    public CompletableFuture<String> getFindingDetailsAsync(String findingArn) {
        BatchGetFindingDetailsRequest request = BatchGetFindingDetailsRequest.builder()
                .findingArns(findingArn)
                .build();

        return getAsyncClient().batchGetFindingDetails(request)
                .thenApply(response -> {
                    if (response.findingDetails() == null || response.findingDetails().isEmpty()) {
                        return String.format("No details found for ARN: ", findingArn);
                    }

                    StringBuilder sb = new StringBuilder();
                    response.findingDetails().forEach(detail -> {
                        sb.append("Finding ARN: ").append(detail.findingArn()).append("\n")
                                .append("Risk Score: ").append(detail.riskScore()).append("\n");

                        // ExploitObserved timings
                        if (detail.exploitObserved() != null) {
                            sb.append("Exploit First Seen: ").append(detail.exploitObserved().firstSeen()).append("\n")
                                    .append("Exploit Last Seen: ").append(detail.exploitObserved().lastSeen()).append("\n");
                        }

                        // Reference URLs
                        if (detail.hasReferenceUrls()) {
                            sb.append("Reference URLs:\n");
                            detail.referenceUrls().forEach(url -> sb.append("  • ").append(url).append("\n"));
                        }

                        // Tools
                        if (detail.hasTools()) {
                            sb.append("Tools:\n");
                            detail.tools().forEach(tool -> sb.append("  • ").append(tool).append("\n"));
                        }

                        // TTPs
                        if (detail.hasTtps()) {
                            sb.append("TTPs:\n");
                            detail.ttps().forEach(ttp -> sb.append("  • ").append(ttp).append("\n"));
                        }

                        // CWEs
                        if (detail.hasCwes()) {
                            sb.append("CWEs:\n");
                            detail.cwes().forEach(cwe -> sb.append("  • ").append(cwe).append("\n"));
                        }

                        // Evidence
                        if (detail.hasEvidences()) {
                            sb.append("Evidence:\n");
                            detail.evidences().forEach(ev -> {
                                sb.append("  - Severity: ").append(ev.severity()).append("\n");

                            });
                        }

                        sb.append("\n");
                    });

                    return sb.toString();
                })
                .exceptionally(ex -> {
                    Throwable cause = ex.getCause() != null ? ex.getCause() : ex;

                    if (cause instanceof ResourceNotFoundException rnfe) {
                        return "Finding not found: %s".formatted(findingArn);
                    }

                    // Fallback for other exceptions
                    throw new RuntimeException("Failed to get finding details for ARN: " + findingArn, cause);
                });
    }
```
+  For API details, see [BatchGetFindingDetails](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/BatchGetFindingDetails) in *AWS SDK for Java 2.x API Reference*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
