---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/inspector_example_inspector_Scenario_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Learn the basics of Amazon Inspector with an AWS SDK
<a name="inspector_example_inspector_Scenario_section"></a>

The following code examples show how to:
+ Check Inspector account status.
+ Ensure Inspector is enabled.
+ Analyze security findings.
+ Check scan coverage.
+ Create a findings filter.
+ List existing filters.
+ Check usage and costs.
+ Get coverage statistics.
+ Delete a filter.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/inspector#code-examples).
Run an interactive scenario demonstrating features.

```
/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 * <p>
 * For more information, see the following documentation topic:
 * <p>
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class InspectorScenario {

    public static final String DASHES = new String(new char[80]).replace("\0", "-");
    private static final Logger logger = LoggerFactory.getLogger(InspectorScenario.class);
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        InspectorActions inspectorActions = new InspectorActions();
        logger.info("Amazon Inspector Basics Scenario");

        logger.info("""
                    Amazon Inspector is a security assessment service provided by Amazon Web Services (AWS) that helps
                    improve the security and compliance of applications deployed on AWS. It automatically assesses
                    applications for vulnerabilities or deviations from best practices. By leveraging Amazon Inspector,
                    users can gain insights into the overall security state of their application and identify potential
                    security risks.

                    This service operates by conducting both network and host-based assessments, allowing it to detect a
                    wide range of security issues, including those related to operating systems, network configurations,
                    and application dependencies.
                    """);

        waitForInputToContinue();

        try {
            runScenario(inspectorActions);

            logger.info("");
            logger.info("Scenario completed successfully!");
            logger.info("");
            logger.info("What you learned:");
            logger.info("  - How to check Inspector account status");
            logger.info("  - How to enable Inspector");
            logger.info("  - How to list and analyze findings");
            logger.info("  - How to check coverage information");
            logger.info("  - How to create and manage filters");
            logger.info("  - How to track usage and costs");
            logger.info("  - How to clean up resources");
            logger.info("");

        } catch (Exception ex) {
            logger.error("Scenario failed due to unexpected error: {}", ex.getMessage(), ex);

        } finally {
            scanner.close();
            logger.info("Exiting...");
        }
    }

    /**
     * Runs the Inspector scenario in a step-by-step sequence.
     *
     * All InspectorActions methods are asynchronous and return CompletableFutures.
     * Each step ends with .join(). Any async exception thrown during .join() will bubble up
     *
     */
    public static void runScenario(InspectorActions actions) {
        String filterArn = null;
        boolean inspectorEnabled = false;

        try {
            // Step 1
            logger.info(DASHES);
            logger.info("Step 1: Checking Inspector account status...");
            String status = actions.getAccountStatusAsync().join();
            logger.info(status);
            waitForInputToContinue();

            // Step 2
            logger.info(DASHES);
            logger.info("Step 2: Enabling Inspector...");
            String message = actions.enableInspectorAsync(null).join();
            logger.info(message);
            inspectorEnabled = true;  // track that Inspector was enabled
            waitForInputToContinue();

            // Step 3
            logger.info(DASHES);
            logger.info("Step 3: Listing LOW severity findings...");

            // Call the service method
            List<String> allFindings = actions.listLowSeverityFindingsAsync().join();

            if (!allFindings.isEmpty()) {
                // Only proceed if there are findings
                String lastArn = allFindings.get(allFindings.size() - 1);
                logger.info("Look up details on: {}", lastArn);
                waitForInputToContinue();
                String details = actions.getFindingDetailsAsync(lastArn).join();
                logger.info(details);
            } else {
                logger.info("No LOW severity findings found.");
            }

            waitForInputToContinue();

            // Step 4
            logger.info(DASHES);
            logger.info("Step 4: Listing coverage...");
            String coverage = actions.listCoverageAsync(5).join();
            logger.info(coverage);
            waitForInputToContinue();

            // Step 5
            logger.info(DASHES);
            logger.info("Step 5: Creating filter...");
            String filterName = "suppress-low-" + System.currentTimeMillis();
            filterArn = actions.createLowSeverityFilterAsync(filterName, "Suppress low severity findings").join();
            logger.info("Created filter: {}", filterArn);
            waitForInputToContinue();

            // Step 6
            logger.info(DASHES);
            logger.info("Step 6: Listing filters...");
            String filters = actions.listFiltersAsync(10).join();
            logger.info(filters);
            waitForInputToContinue();

            // Step 7
            logger.info(DASHES);
            logger.info("Step 7: Usage totals...");
            String usage = actions.listUsageTotalsAsync(null, 10).join();
            logger.info(usage);
            waitForInputToContinue();

            // Step 8
            logger.info(DASHES);
            logger.info("Step 8: Coverage statistics...");
            String stats = actions.listCoverageStatisticsAsync().join();
            logger.info(stats);
            waitForInputToContinue();

            // Step 9
            logger.info(DASHES);
            logger.info("Step 9: Delete filter?");
            logger.info("Filter ARN: {}", filterArn);
            logger.info("Delete the filter and disable Inspector? (y/n)");

            if (scanner.nextLine().trim().equalsIgnoreCase("y")) {
                actions.deleteFilterAsync(filterArn).join();
                logger.info("Filter deleted.");
                String disableMsg = actions.disableInspectorAsync(null).join();
                logger.info(disableMsg);
                inspectorEnabled = false; // track that Inspector was disabled
            }

            waitForInputToContinue();

        } catch (Exception ex) {
            logger.error("Scenario encountered an error: {}", ex.getMessage(), ex);
            // Rethrow the exception
            throw ex;

        } finally {
            // Cleanup in case of an exception
            if (filterArn != null) {
                try {
                    actions.deleteFilterAsync(filterArn).join();
                    logger.info("Cleanup: Filter deleted.");
                } catch (Exception e) {
                    logger.warn("Failed to delete filter during cleanup: {}", e.getMessage(), e);
                }
            }

            if (inspectorEnabled) {
                try {
                    actions.disableInspectorAsync(null).join();
                    logger.info("Cleanup: Inspector disabled.");
                } catch (Exception e) {
                    logger.warn("Failed to disable Inspector during cleanup: {}", e.getMessage(), e);
                }
            }
        }
    }

    // Utility Method
    private static void waitForInputToContinue() {
        while (true) {
            logger.info("");
            logger.info("Enter 'c' to continue:");
            String input = scanner.nextLine().trim();
            if (input.equalsIgnoreCase("c")) break;
            logger.info("Invalid input, try again.");
        }
    }
}
```
A wrapper class for SDK methods.

```
public class InspectorActions {
    private static Inspector2AsyncClient inspectorAsyncClient;
    private static final Logger logger = LoggerFactory.getLogger(InspectorActions.class);

    private static Inspector2AsyncClient getAsyncClient() {
        if (inspectorAsyncClient == null) {
            SdkAsyncHttpClient httpClient = NettyNioAsyncHttpClient.builder()
                    .maxConcurrency(100)
                    .connectionTimeout(Duration.ofSeconds(60))
                    .readTimeout(Duration.ofSeconds(60))
                    .writeTimeout(Duration.ofSeconds(60))
                    .build();

            ClientOverrideConfiguration overrideConfig = ClientOverrideConfiguration.builder()
                    .apiCallTimeout(Duration.ofMinutes(2))
                    .apiCallAttemptTimeout(Duration.ofSeconds(90))
                    .retryStrategy(RetryMode.STANDARD)
                    .build();

            inspectorAsyncClient = Inspector2AsyncClient.builder()
                    .httpClient(httpClient)
                    .overrideConfiguration(overrideConfig)
                    .build();
        }
        return inspectorAsyncClient;
    }

    /**
     * Enables AWS Inspector for the provided account(s) and default resource types.
     *
     * @param accountIds Optional list of AWS account IDs.
     */
    public CompletableFuture<String> enableInspectorAsync(List<String> accountIds) {

        // The resource types to enable.
        List<ResourceScanType> resourceTypes = List.of(
                ResourceScanType.EC2,
                ResourceScanType.ECR,
                ResourceScanType.LAMBDA,
                ResourceScanType.LAMBDA_CODE
        );

        // Build the request.
        EnableRequest.Builder requestBuilder = EnableRequest.builder()
                .resourceTypes(resourceTypes);

        if (accountIds != null && !accountIds.isEmpty()) {
            requestBuilder.accountIds(accountIds);
        }

        EnableRequest request = requestBuilder.build();
        return getAsyncClient().enable(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();
                        if (cause instanceof ValidationException) {
                            throw new CompletionException(
                                    "Inspector may already be enabled for this account: %s".formatted(cause.getMessage()),
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
                                "Failed to enable Inspector: %s".formatted(exception.getMessage()),
                                exception
                        );
                    }
                })
                .thenApply(response -> {
                    StringBuilder summary = new StringBuilder("Enable results:\n");

                    if (response.accounts() == null || response.accounts().isEmpty()) {
                        summary.append("Inspector may already be enabled for all target accounts.");
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

    /**
     * Asynchronously lists Inspector2 usage totals using a paginator.
     *
     * @param accountIds optional list of account IDs
     * @param maxResults maximum results per page
     * @return CompletableFuture completed with formatted summary text
     */
    public CompletableFuture<String> listUsageTotalsAsync(
            List<String> accountIds,
            int maxResults) {

        logger.info("Starting usage totals paginator…");

        ListUsageTotalsRequest.Builder builder = ListUsageTotalsRequest.builder()
                .maxResults(maxResults);

        if (accountIds != null && !accountIds.isEmpty()) {
            builder.accountIds(accountIds);
        }

        ListUsageTotalsRequest request = builder.build();
        ListUsageTotalsPublisher paginator = getAsyncClient().listUsageTotalsPaginator(request);
        StringBuilder summaryBuilder = new StringBuilder();

        return paginator.subscribe(response -> {
                    if (response.totals() != null && !response.totals().isEmpty()) {
                        response.totals().forEach(total -> {
                            if (total.usage() != null) {
                                total.usage().forEach(usage -> {
                                    logger.info("Usage: {} = {}", usage.typeAsString(), usage.total());
                                    summaryBuilder.append(usage.typeAsString())
                                            .append(": ")
                                            .append(usage.total())
                                            .append("\n");
                                });
                            }
                        });
                    } else {
                        logger.info("Page contained no usage totals.");
                    }
                }).thenRun(() -> logger.info("Successfully listed usage totals."))
                .thenApply(v -> {
                    String summary = summaryBuilder.toString();
                    return summary.isEmpty() ? "No usage totals found." : summary;
                }).exceptionally(ex -> {
                    Throwable cause = ex.getCause() != null ? ex.getCause() : ex;

                    if (cause instanceof ValidationException ve) {
                        throw new CompletionException(
                                "Validation error listing usage totals: %s".formatted(ve.getMessage()),
                                ve
                        );
                    }

                    throw new CompletionException("Failed to list usage totals", cause);
                });
    }

    /**
     * Retrieves the account status using the Inspector2Client.
     */
    public CompletableFuture<String> getAccountStatusAsync() {
        BatchGetAccountStatusRequest request = BatchGetAccountStatusRequest.builder()
                .accountIds(Collections.emptyList())
                .build();

        return getAsyncClient().batchGetAccountStatus(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();
                        if (cause instanceof AccessDeniedException) {
                            throw new CompletionException(
                                    "You do not have sufficient access: %s".formatted(cause.getMessage()),
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
                                "Unexpected error getting account status: %s".formatted(exception.getMessage()),
                                exception
                        );
                    }
                })
                .thenApply(response -> {

                    StringBuilder sb = new StringBuilder();
                    List<AccountState> accounts = response.accounts();

                    if (accounts == null || accounts.isEmpty()) {
                        sb.append("No account status returned.\n");
                        return sb.toString();
                    }

                    sb.append("Inspector Account Status:\n");
                    for (AccountState account : accounts) {

                        String accountId = account.accountId() != null
                                ? account.accountId()
                                : "Unknown";

                        sb.append("  Account ID: ").append(accountId).append("\n");

                        // Overall account state
                        if (account.state() != null && account.state().status() != null) {
                            sb.append("  Overall State: ")
                                    .append(account.state().status())
                                    .append("\n");
                        } else {
                            sb.append("  Overall State: Unknown\n");
                        }

                        // Resource state (only status available)
                        ResourceState resources = account.resourceState();
                        if (resources != null) {
                            sb.append("  Resource Status: available\n");
                        }

                        sb.append("\n");
                    }

                    return sb.toString();
                });
    }

    /**
     * Asynchronously lists Inspector2 filters using a paginator.
     *
     * @param maxResults maximum filters per page (nullable)
     * @return CompletableFuture completed with summary text
     */
    public CompletableFuture<String> listFiltersAsync(Integer maxResults) {
        logger.info("Starting async filters paginator…");

        ListFiltersRequest.Builder builder = ListFiltersRequest.builder();
        if (maxResults != null) {
            builder.maxResults(maxResults);
        }

        ListFiltersRequest request = builder.build();

        // Paginator from SDK
        ListFiltersPublisher paginator = getAsyncClient().listFiltersPaginator(request);
        StringBuilder collectedFilterIds = new StringBuilder();

        return paginator.subscribe(response -> {
            response.filters().forEach(filter -> {
                logger.info("Filter: " + filter.arn());
                collectedFilterIds.append(filter.arn()).append("\n");
            });
        }).thenApply(v -> {
            String result = collectedFilterIds.toString();
            logger.info("Successfully listed all filters.");
            return result.isEmpty() ? "No filters found." : result;
        }).exceptionally(ex -> {
            Throwable cause = ex.getCause() != null ? ex.getCause() : ex;

            if (cause instanceof ValidationException ve) {
                throw new CompletionException(
                        "Validation error listing filters: %s".formatted(ve.getMessage()),
                        ve
                );
            }

            throw new RuntimeException("Failed to list filters", ex);
        });
    }

    /**
     * Creates a new LOW severity filter in AWS Inspector2 to suppress findings.
     *
     * @param filterName  the name of the filter to create
     * @param description a descriptive string explaining the purpose of the filter
     * @return a CompletableFuture that completes with the ARN of the created filter
     * @throws CompletionException wraps any validation, Inspector2 service, or unexpected errors
     */
    public CompletableFuture<String> createLowSeverityFilterAsync(
            String filterName,
            String description) {

        // Define a filter to match LOW severity findings.
        StringFilter severityFilter = StringFilter.builder()
                .value(Severity.LOW.toString())
                .comparison(StringComparison.EQUALS)
                .build();

        // Create filter criteria.
        FilterCriteria filterCriteria = FilterCriteria.builder()
                .severity(Collections.singletonList(severityFilter))
                .build();

        // Build the filter creation request.
        CreateFilterRequest request = CreateFilterRequest.builder()
                .name(filterName)
                .filterCriteria(filterCriteria)
                .action(FilterAction.SUPPRESS)
                .description(description)
                .build();

        return getAsyncClient().createFilter(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause() != null ? exception.getCause() : exception;

                        if (cause instanceof ValidationException ve) {
                            throw new CompletionException(
                                    "Validation error creating filter: %s".formatted(ve.getMessage()),
                                    ve
                            );
                        }

                        if (cause instanceof Inspector2Exception e) {
                            throw new CompletionException(
                                    "Inspector2 service error: %s".formatted(e.awsErrorDetails().errorMessage()),
                                    e
                            );
                        }

                        // Unexpected async error
                        throw new CompletionException(
                                "Unexpected error creating filter: %s".formatted(exception.getMessage()),
                                exception
                        );
                    }
                })
                // Extract and return the ARN of the created filter.
                .thenApply(CreateFilterResponse::arn);
    }

    /**
     * Lists all AWS Inspector findings of LOW severity asynchronously.
     *
     * @return CompletableFuture containing a List of finding ARNs.
     * Returns an empty list if no LOW severity findings are found.
     */
    public CompletableFuture<ArrayList<String>> listLowSeverityFindingsAsync() {
        logger.info("Starting async LOW severity findings paginator…");

        // Build a filter criteria for LOW severity.
        StringFilter severityFilter = StringFilter.builder()
                .value(Severity.LOW.toString())
                .comparison(StringComparison.EQUALS)
                .build();

        FilterCriteria filterCriteria = FilterCriteria.builder()
                .severity(Collections.singletonList(severityFilter))
                .build();

        // Build the request.
        ListFindingsRequest request = ListFindingsRequest.builder()
                .filterCriteria(filterCriteria)
                .build();

        ListFindingsPublisher paginator = getAsyncClient().listFindingsPaginator(request);
        List<String> allArns = Collections.synchronizedList(new ArrayList<>());

        return paginator.subscribe(response -> {
                    if (response.findings() != null && !response.findings().isEmpty()) {
                        response.findings().forEach(finding -> {
                            logger.info("Finding ARN: {}", finding.findingArn());
                            allArns.add(finding.findingArn());
                        });
                    } else {
                        logger.info("Page contained no findings.");
                    }
                })
                .thenRun(() -> logger.info("Successfully listed all LOW severity findings."))
                .thenApply(v -> new ArrayList<>(allArns)) // Return list instead of a formatted string
                .exceptionally(ex -> {
                    Throwable cause = ex.getCause() != null ? ex.getCause() : ex;
                    if (cause instanceof ValidationException ve) {
                        throw new CompletionException(
                                "Validation error listing LOW severity findings: %s".formatted(ve.getMessage()),
                                ve
                        );
                    }
                    throw new RuntimeException("Failed to list LOW severity findings", ex);
                });
    }

    /**
     * Lists AWS Inspector2 coverage details for scanned resources using a paginator.
     *
     * @param maxResults Maximum number of resources to return.
     */
    public CompletableFuture<String> listCoverageAsync(int maxResults) {
        ListCoverageRequest initialRequest = ListCoverageRequest.builder()
                .maxResults(maxResults)
                .build();

        ListCoveragePublisher paginator = getAsyncClient().listCoveragePaginator(initialRequest);
        StringBuilder summary = new StringBuilder();

        return paginator.subscribe(response -> {
            List<CoveredResource> coveredResources = response.coveredResources();

            if (coveredResources == null || coveredResources.isEmpty()) {
                summary.append("No coverage information available for this page.\n");
                return;
            }

            Map<String, List<CoveredResource>> byType = coveredResources.stream()
                    .collect(Collectors.groupingBy(CoveredResource::resourceTypeAsString));

            byType.forEach((type, list) ->
                    summary.append("  ").append(type)
                            .append(": ").append(list.size())
                            .append(" resource(s)\n")
            );

            // Include up to 3 sample resources per page
            for (int i = 0; i < Math.min(coveredResources.size(), 3); i++) {
                CoveredResource r = coveredResources.get(i);
                summary.append("  - ").append(r.resourceTypeAsString())
                        .append(": ").append(r.resourceId()).append("\n");
                summary.append("    Scan Type: ").append(r.scanTypeAsString()).append("\n");
                if (r.scanStatus() != null) {
                    summary.append("    Status: ").append(r.scanStatus().statusCodeAsString()).append("\n");
                }
                if (r.accountId() != null) {
                    summary.append("    Account ID: ").append(r.accountId()).append("\n");
                }
                summary.append("\n");
            }

        }).thenApply(v -> {
            if (summary.length() == 0) {
                return "No coverage information found across all pages.";
            } else {
                return "Coverage Information:\n" + summary.toString();
            }
        }).exceptionally(ex -> {
            Throwable cause = ex.getCause();
            if (cause instanceof ValidationException) {
                throw new CompletionException(
                        "Validation error listing coverage: " + cause.getMessage(), cause);
            } else if (cause instanceof Inspector2Exception e) {
                throw new CompletionException(
                        "Inspector2 service error: " + e.awsErrorDetails().errorMessage(), e);
            }
            throw new CompletionException("Unexpected error listing coverage: " + ex.getMessage(), ex);
        });
    }

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
}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [BatchGetAccountStatus](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/BatchGetAccountStatus)
  + [BatchGetFindingDetails](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/BatchGetFindingDetails)
  + [CreateFilter](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/CreateFilter)
  + [DeleteFilter](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/DeleteFilter)
  + [Enable](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/Enable)
  + [ListCoverage](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ListCoverage)
  + [ListCoverageStatistics](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ListCoverageStatistics)
  + [ListFilters](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ListFilters)
  + [ListFindings](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ListFindings)
  + [ListUsageTotals](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ListUsageTotals)

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).
Run an interactive scenario demonstrating features.

```
class InspectorScenario:
    """Runs an interactive scenario that shows how to use Amazon Inspector."""

    def __init__(self, inspector_wrapper: Inspector2Wrapper) -> None:
        """
        :param inspector_wrapper: An object that wraps Amazon Inspector actions.
        """
        self.inspector_wrapper = inspector_wrapper
        self.filter_arn: Optional[str] = None
        # The resource types this scenario enabled, so cleanup can disable them.
        self.enabled_types: list[str] = list()

    @staticmethod
    def _wait_for_input() -> None:
        q.ask("\nPress Enter to continue...")
        print(DASHES)

    # ------------------------------------------------------------------
    # Setup
    # ------------------------------------------------------------------
    def setup(self) -> None:
        """
        Checks the account status, enables Inspector for any resource types
        that are not already enabled, and displays an account status summary.
        """
        print(DASHES)
        print("Setup: Checking Inspector account status...")
        accounts = self.inspector_wrapper.get_account_status()
        to_enable = list()
        for account in accounts:
            print(f"  Account ID: {account.get('accountId', 'Unknown')}")
            print(
                "  Overall State: "
                f"{account.get('state', dict()).get('status', 'Unknown')}"
            )
            resource_state = account.get("resourceState", dict())
            for key, resource_type in RESOURCE_STATE_KEYS.items():
                status = resource_state.get(key, dict()).get("status", "DISABLED")
                if status != "ENABLED" and resource_type not in to_enable:
                    to_enable.append(resource_type)

        if to_enable:
            print(f"\nEnabling Inspector for: {', '.join(to_enable)}...")
            results = self.inspector_wrapper.enable(to_enable)
            for result in results:
                print(
                    f"  Account: {result.get('accountId', 'Unknown')} -> "
                    f"Status: {result.get('status', 'Unknown')}"
                )
            if results:
                self.enabled_types = to_enable
        else:
            print("\nInspector is already enabled for all resource types.")

        print("\nAccount status summary:")
        for account in self.inspector_wrapper.get_account_status():
            print(f"  Account ID: {account.get('accountId', 'Unknown')}")
            resource_state = account.get("resourceState", dict())
            for key, resource_type in RESOURCE_STATE_KEYS.items():
                status = resource_state.get(key, dict()).get("status", "UNKNOWN")
                print(f"    {resource_type:12s}: {status}")

    # ------------------------------------------------------------------
    # Coverage Assessment
    # ------------------------------------------------------------------
    def assess_coverage(self) -> None:
        """
        Lists coverage details, displays overall coverage statistics, and
        reviews the scan status of covered resources.
        """
        print("Coverage Assessment: Listing coverage details (up to 5 resources)...")
        resources = self.inspector_wrapper.list_coverage(max_results=5)
        if not resources:
            print("  No coverage information found.")
        else:
            by_type = Counter(r.get("resourceType") for r in resources)
            for resource_type, count in by_type.items():
                print(f"  {resource_type}: {count} resource(s)")
            print("\n  Sample resources:")
            for resource in resources[:3]:
                print(
                    f"  - {resource.get('resourceType')}: {resource.get('resourceId')}"
                )
                print(f"    Scan Type : {resource.get('scanType')}")
                scan_status = resource.get("scanStatus", dict())
                if scan_status:
                    print(f"    Status    : {scan_status.get('statusCode')}")
                print(f"    Account ID: {resource.get('accountId')}")

        print("\nOverall coverage statistics:")
        stats = self.inspector_wrapper.list_coverage_statistics()
        print(f"  Total covered resources: {stats['totalCounts']}")

        print("\nScan status of resources:")
        if resources:
            by_status = Counter(
                r.get("scanStatus", dict()).get("statusCode", "UNKNOWN")
                for r in resources
            )
            for status_code, count in by_status.items():
                print(f"  {status_code}: {count} resource(s)")
        else:
            print("  No resources to review.")

    # ------------------------------------------------------------------
    # Findings Management
    # ------------------------------------------------------------------
    def manage_findings(self) -> None:
        """
        Lists findings across all resource types, analyzes one finding, creates
        a filter that suppresses low-severity findings, and lists filters.
        """
        print("Findings Management: Listing security findings...")
        findings = self.inspector_wrapper.list_findings(max_results=10)
        if not findings:
            print("  No findings found. This is common for new accounts.")
        else:
            for finding in findings:
                print(
                    f"  - [{finding.get('severity')}] {finding.get('title', 'Untitled')}"
                )
                print(f"    Type  : {finding.get('type')}")
                print(f"    Status: {finding.get('status')}")
                print(f"    ARN   : {finding.get('findingArn')}")

            finding_arn = findings[0]["findingArn"]
            print(f"\nAnalyzing finding details for: {finding_arn}")
            details = self.inspector_wrapper.batch_get_finding_details([finding_arn])
            if not details:
                print(f"  No details found for {finding_arn}.")
            for detail in details:
                print(f"  Risk Score: {detail.get('riskScore', 'N/A')}")
                exploit = detail.get("exploitObserved")
                if exploit:
                    print(f"  Exploit First Seen: {exploit.get('firstSeen')}")
                    print(f"  Exploit Last Seen : {exploit.get('lastSeen')}")
                for label, key in (
                    ("CWEs", "cwes"),
                    ("TTPs", "ttps"),
                    ("Tools", "tools"),
                    ("Reference URLs", "referenceUrls"),
                ):
                    values = detail.get(key, list())
                    if values:
                        print(f"  {label}: {', '.join(values)}")

        filter_name = f"suppress-low-{int(time.time())}"
        print(f"\nCreating filter '{filter_name}' to suppress LOW severity findings...")
        self.filter_arn = self.inspector_wrapper.create_low_severity_filter(
            filter_name, "Suppress low severity findings"
        )
        if self.filter_arn:
            print(f"  Created filter: {self.filter_arn}")
        else:
            print("  The filter was not created.")

        print("\nListing filters...")
        filters = self.inspector_wrapper.list_filters(max_results=10)
        if not filters:
            print("  No filters found.")
        for inspector_filter in filters:
            print(
                f"  - {inspector_filter.get('name')}: {inspector_filter.get('arn')} "
                f"({inspector_filter.get('action')})"
            )

    # ------------------------------------------------------------------
    # Usage and Costs
    # ------------------------------------------------------------------
    def check_usage_and_costs(self) -> None:
        """Lists usage totals and reviews coverage statistics by resource type."""
        print("Usage and Costs: Checking usage totals...")
        totals = self.inspector_wrapper.list_usage_totals(max_results=10)
        if not totals:
            print("  No usage totals found.")
        for total in totals:
            print(f"  Account ID: {total.get('accountId')}")
            for usage in total.get("usage", list()):
                cost = usage.get("estimatedMonthlyCost")
                cost_text = (
                    f" (est. {cost} {usage.get('currency', '')})" if cost else ""
                )
                print(f"    {usage.get('type')}: {usage.get('total')}{cost_text}")

        print("\nCoverage statistics by resource type:")
        stats = self.inspector_wrapper.list_coverage_statistics(
            group_by="RESOURCE_TYPE"
        )
        if not stats["countsByGroup"]:
            print("  No coverage statistics available.")
        for group in stats["countsByGroup"]:
            print(f"  {group.get('groupKey')}: {group.get('count')}")

    # ------------------------------------------------------------------
    # Cleanup
    # ------------------------------------------------------------------
    def cleanup(self) -> None:
        """Deletes the filter and disables Inspector, if the user agrees."""
        print("Cleanup")
        if self.filter_arn:
            print(f"  Filter ARN: {self.filter_arn}")
        if not q.ask("Delete the filter and disable Inspector? (y/n) ", q.is_yesno):
            print("  Leaving the filter and Inspector settings in place.")
            return

        if self.filter_arn:
            self.inspector_wrapper.delete_filter(self.filter_arn)
            print("  Filter deleted.")
            self.filter_arn = None

        disable_types = self.enabled_types
        if not disable_types and q.ask(
            "Inspector was already enabled before this scenario ran. "
            "Disable it anyway? (y/n) ",
            q.is_yesno,
        ):
            disable_types = RESOURCE_TYPES
        if disable_types:
            results = self.inspector_wrapper.disable(disable_types)
            for result in results:
                print(
                    f"  Account: {result.get('accountId', 'Unknown')} -> "
                    f"Status: {result.get('status', 'Unknown')}"
                )
            print(f"  Inspector disabled for: {', '.join(disable_types)}")
            self.enabled_types = list()
        else:
            print("  Inspector was left enabled.")

    def _cleanup_after_error(self) -> None:
        """Removes resources this scenario created when a step fails."""
        if self.filter_arn:
            try:
                self.inspector_wrapper.delete_filter(self.filter_arn)
                print("Cleanup: Filter deleted.")
                self.filter_arn = None
            except ClientError as err:
                logger.warning("Failed to delete filter during cleanup: %s", err)
        if self.enabled_types:
            try:
                self.inspector_wrapper.disable(self.enabled_types)
                print("Cleanup: Inspector disabled.")
                self.enabled_types = list()
            except ClientError as err:
                logger.warning("Failed to disable Inspector during cleanup: %s", err)

    # ------------------------------------------------------------------
    # Run the scenario
    # ------------------------------------------------------------------
    def run_scenario(self) -> None:
        """Runs the Amazon Inspector basics scenario."""
        print(DASHES)
        print("Amazon Inspector Basics Scenario")
        print(DASHES)
        print(
            "Amazon Inspector is a security assessment service that helps improve\n"
            "the security and compliance of applications deployed on AWS. It\n"
            "automatically assesses workloads for software vulnerabilities and\n"
            "unintended network exposure."
        )
        self._wait_for_input()

        try:
            self.setup()
            self._wait_for_input()
            self.assess_coverage()
            self._wait_for_input()
            self.manage_findings()
            self._wait_for_input()
            self.check_usage_and_costs()
            self._wait_for_input()
            self.cleanup()
        except ClientError:
            logger.exception("The scenario encountered an error.")
            self._cleanup_after_error()
            raise

        print(DASHES)
        print("Scenario completed successfully!")
        print("What you learned:")
        print("  - How to check Inspector account status")
        print("  - How to enable Inspector")
        print("  - How to list and analyze findings")
        print("  - How to check coverage information")
        print("  - How to create and manage filters")
        print("  - How to track usage and costs")
        print("  - How to clean up resources")
        print(DASHES)
```
A wrapper class for SDK methods.

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

    def enable(self, resource_types: list[str]) -> list[dict[str, Any]]:
        """
        Enables Amazon Inspector scans for the specified resource types.

        :param resource_types: The resource types to enable, such as EC2 or ECR.
        :return: The accounts that the request was applied to. If Inspector is
                 already enabled, a ValidationException is logged and an empty
                 list is returned.
        """
        try:
            response = self.inspector2_client.enable(resourceTypes=resource_types)
            return response.get("accounts", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Inspector may already be enabled for this account. "
                    "Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't enable Inspector for %s. Here's why: %s: %s",
                resource_types,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def disable(self, resource_types: list[str]) -> list[dict[str, Any]]:
        """
        Disables Amazon Inspector scans for the specified resource types.

        :param resource_types: The resource types to disable, such as EC2 or ECR.
        :return: The accounts that the request was applied to. If Inspector is
                 already disabled, a ValidationException is logged and an empty
                 list is returned.
        """
        try:
            response = self.inspector2_client.disable(resourceTypes=resource_types)
            return response.get("accounts", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Inspector may already be disabled for this account. "
                    "Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't disable Inspector for %s. Here's why: %s: %s",
                resource_types,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def get_account_status(self) -> list[dict[str, Any]]:
        """
        Gets the Amazon Inspector status of the current account.

        :return: A list of account states. Each includes the overall state and the
                 state of each resource type.
        """
        try:
            response = self.inspector2_client.batch_get_account_status()
            return response.get("accounts", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "AccessDeniedException":
                logger.error(
                    "You do not have sufficient access to get the Inspector "
                    "account status. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Couldn't get the Inspector account status. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise

    def list_findings(self, max_results: int = 10) -> list[dict[str, Any]]:
        """
        Lists Amazon Inspector findings across all resource types.

        :param max_results: The maximum number of findings to return.
        :return: The findings. If a ValidationException occurs, it is logged and
                 an empty list is returned.
        """
        try:
            findings = list()
            paginator = self.inspector2_client.get_paginator("list_findings")
            # This intentionally returns at most max_results findings. MaxItems
            # caps the total, and PageSize requests that many in a single call,
            # so only one request is made.
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                findings.extend(page.get("findings", list()))
            return findings
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing findings. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't list findings. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def list_coverage(self, max_results: int = 5) -> list[dict[str, Any]]:
        """
        Lists coverage details for the resources that Amazon Inspector scans.

        :param max_results: The maximum number of items to return.
        :return: The covered resources. If a ValidationException occurs, it is
                 logged and an empty list is returned.
        """
        try:
            covered_resources = list()
            paginator = self.inspector2_client.get_paginator("list_coverage")
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                covered_resources.extend(page.get("coveredResources", list()))
            return covered_resources
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing coverage. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't list coverage. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

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

    def list_usage_totals(self, max_results: int = 10) -> list[dict[str, Any]]:
        """
        Lists Amazon Inspector usage totals for the current account.

        :param max_results: The maximum number of items to return.
        :return: The usage totals. If a ValidationException occurs, it is logged
                 and an empty list is returned.
        """
        try:
            totals = list()
            paginator = self.inspector2_client.get_paginator("list_usage_totals")
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                totals.extend(page.get("totals", list()))
            return totals
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing usage totals. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't list usage totals. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def create_low_severity_filter(
        self, filter_name: str, description: str
    ) -> Optional[str]:
        """
        Creates a filter that suppresses LOW severity findings.

        :param filter_name: The name of the filter.
        :param description: A description of the filter.
        :return: The ARN of the new filter. If a ValidationException occurs, it is
                 logged and None is returned.
        """
        try:
            response = self.inspector2_client.create_filter(
                name=filter_name,
                description=description,
                action="SUPPRESS",
                filterCriteria={"severity": [{"comparison": "EQUALS", "value": "LOW"}]},
            )
            return response["arn"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error creating filter %s. Here's why: %s: %s",
                    filter_name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return None
            logger.error(
                "Couldn't create filter %s. Here's why: %s: %s",
                filter_name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def list_filters(self, max_results: int = 10) -> list[dict[str, Any]]:
        """
        Lists the findings filters in the current account.

        :param max_results: The maximum number of items to return.
        :return: The filters.
        """
        try:
            filters = list()
            paginator = self.inspector2_client.get_paginator("list_filters")
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                filters.extend(page.get("filters", list()))
            return filters
        except ClientError as err:
            logger.error(
                "Couldn't list filters. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

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

    def batch_get_finding_details(
        self, finding_arns: list[str]
    ) -> list[dict[str, Any]]:
        """
        Gets vulnerability intelligence details for the specified findings.

        :param finding_arns: The ARNs of the findings to look up.
        :return: The finding details.
        """
        try:
            response = self.inspector2_client.batch_get_finding_details(
                findingArns=finding_arns
            )
            return response.get("findingDetails", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Couldn't find details for findings %s. Here's why: %s: %s",
                    finding_arns,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Couldn't get finding details. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [BatchGetAccountStatus](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/BatchGetAccountStatus)
  + [BatchGetFindingDetails](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/BatchGetFindingDetails)
  + [CreateFilter](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/CreateFilter)
  + [DeleteFilter](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/DeleteFilter)
  + [Enable](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/Enable)
  + [ListCoverage](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListCoverage)
  + [ListCoverageStatistics](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListCoverageStatistics)
  + [ListFilters](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListFilters)
  + [ListFindings](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListFindings)
  + [ListUsageTotals](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListUsageTotals)

------
