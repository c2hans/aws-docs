---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/neptune_example_neptune_Scenario_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Learn the basics of Neptune with an AWS SDK
<a name="neptune_example_neptune_Scenario_section"></a>

The following code examples show how to:
+ Create an Amazon Neptune Subnet Group.
+ Create an Neptune Cluster.
+ Create an Neptune Instance.
+ Check the status of the Neptune Instance.
+ Show Neptune cluster details.
+ Stop the Neptune cluster.
+ Start the Neptune cluster.
+ Delete the Neptune Assets.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).
Run an interactive scenario demonstrating Neptune features.

```
public class NeptuneScenario {
    public static final String DASHES = new String(new char[80]).replace("\0", "-");
    private static final Logger logger = LoggerFactory.getLogger(NeptuneScenario.class);
    static Scanner scanner = new Scanner(System.in);
    static NeptuneActions neptuneActions = new NeptuneActions();

    public static void main(String[] args) {
        final String usage =
                """
                Usage:
                    <subnetGroupName> <clusterName> <dbInstanceId>

                Where:
                    subnetGroupName - The name of an existing Neptune DB subnet group that includes subnets in at least two Availability Zones.
                    clusterName     - The unique identifier for the Neptune DB cluster.
                    dbInstanceId    - The identifier for a specific Neptune DB instance within the cluster.
                """;
        String subnetGroupName = "neptuneSubnetGroup65";
        String clusterName = "neptuneCluster65";
        String dbInstanceId = "neptuneDB65";

        logger.info("""
                   Amazon Neptune is a fully managed graph
                   database service by AWS, designed specifically
                   for handling complex relationships and connected
                   datasets at scale. It supports two popular graph models:
                   property graphs (via openCypher and Gremlin) and RDF
                   graphs (via SPARQL). This makes Neptune ideal for
                   use cases such as knowledge graphs, fraud detection,
                   social networking, recommendation engines, and
                   network management, where relationships between
                   entities are central to the data.

                   Being fully managed, Neptune handles database
                   provisioning, patching, backups, and replication,
                   while also offering high availability and durability
                   within AWS's infrastructure.

                   For developers, programming with Neptune allows
                   for building intelligent, relationship-aware
                   applications that go beyond traditional tabular
                   databases. Developers can use the AWS SDK for Java
                   to automate infrastructure operations (via NeptuneClient).

                    Let's get started...
                    """);
        waitForInputToContinue(scanner);
        runScenario(subnetGroupName, dbInstanceId, clusterName);
    }

    public static void runScenario(String subnetGroupName, String dbInstanceId, String clusterName) {
        logger.info(DASHES);
        logger.info("1. Create a Neptune DB Subnet Group");
        logger.info("The Neptune DB subnet group is used when launching a Neptune cluster");
        waitForInputToContinue(scanner);
        try {
            neptuneActions.createSubnetGroupAsync(subnetGroupName).join();

        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();
            if (cause instanceof ServiceQuotaExceededException) {
                logger.error("The request failed due to service quota exceeded: {}", cause.getMessage());
            } else {
                logger.error("An unexpected error occurred.", cause);
            }
            return;
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("2. Create a Neptune Cluster");
        logger.info("A Neptune Cluster allows you to store and query highly connected datasets with low latency.");
        waitForInputToContinue(scanner);
        String dbClusterId;
        try {
            dbClusterId = neptuneActions.createDBClusterAsync(clusterName).join();
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();
            if (cause instanceof ServiceQuotaExceededException) {
                logger.error("The request failed due to service quota exceeded: {}", cause.getMessage());
            } else {
                logger.error("An unexpected error occurred.", cause);
            }
            return;
        }

        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("3. Create a Neptune DB Instance");
        logger.info("In this step, we add a new database instance to the Neptune cluster");
        waitForInputToContinue(scanner);
        try {
        neptuneActions.createDBInstanceAsync(dbInstanceId, dbClusterId).join();
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();
            if (cause instanceof ServiceQuotaExceededException) {
                logger.error("The request failed due to service quota exceeded: {}", cause.getMessage());
            } else {
                logger.error("An unexpected error occurred.", cause);
            }
            return;
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("4. Check the status of the Neptune DB Instance");
        logger.info("""
                    In this step, we will wait until the DB instance
                    becomes available. This may take around 10 minutes.
                    """);
        waitForInputToContinue(scanner);
        try {
            neptuneActions.checkInstanceStatus(dbInstanceId, "available").join();
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();
            logger.error("An unexpected error occurred.", cause);
            return;
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("5.Show Neptune Cluster details");
        waitForInputToContinue(scanner);
        try {
            neptuneActions.describeDBClustersAsync(clusterName).join();
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();
            if (cause instanceof ResourceNotFoundException) {
                logger.error("The request failed due to the resource not found: {}", cause.getMessage());
            } else {
                logger.error("An unexpected error occurred.", cause);
            }
            return;
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("6. Stop the Amazon Neptune cluster");
        logger.info("""
                    Once stopped, this step polls the status
                    until the cluster is in a stopped state.
                    """);
        waitForInputToContinue(scanner);
        try {
            neptuneActions.stopDBClusterAsync(dbClusterId);
            neptuneActions.waitForClusterStatus(dbClusterId, "stopped");
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();
            if (cause instanceof ResourceNotFoundException) {
                logger.error("The request failed due to the resource not found: {}", cause.getMessage());
            } else {
                logger.error("An unexpected error occurred.", cause);
            }
            return;
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("7. Start the Amazon Neptune cluster");
        logger.info("""
                    Once started, this step polls the clusters
                    status until it's in an available state.
                    We will also poll the instance status.
                    """);
        waitForInputToContinue(scanner);
        try {
            neptuneActions.startDBClusterAsync(dbClusterId);
            neptuneActions.waitForClusterStatus(dbClusterId, "available");
            neptuneActions.checkInstanceStatus(dbInstanceId, "available").join();
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();
            if (cause instanceof ResourceNotFoundException) {
                logger.error("The request failed due to the resource not found: {}", cause.getMessage());
            } else {
                logger.error("An unexpected error occurred.", cause);
            }
            return;
        }
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("8. Delete the Neptune Assets");
        logger.info("Would you like to delete the Neptune Assets? (y/n)");
        String delAns = scanner.nextLine().trim();
        if (delAns.equalsIgnoreCase("y")) {
            logger.info("You selected to delete the Neptune assets.");
            try {
                neptuneActions.deleteNeptuneResourcesAsync(dbInstanceId, clusterName, subnetGroupName);
            } catch (CompletionException ce) {
                Throwable cause = ce.getCause();
                if (cause instanceof ResourceNotFoundException) {
                    logger.error("The request failed due to the resource not found: {}", cause.getMessage());
                } else {
                    logger.error("An unexpected error occurred.", cause);
                }
                return;
            }
        } else {
            logger.info("You selected not to delete Neptune assets.");
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info(
                """
                Thank you for checking out the Amazon Neptune Service Use demo. We hope you
                learned something new, or got some inspiration for your own apps today.
                For more AWS code examples, have a look at:
                https://docs.aws.amazon.com/code-library/latest/ug/what-is-code-library.html
                """);
        logger.info(DASHES);
    }

    private static void waitForInputToContinue(Scanner scanner) {
        while (true) {
            logger.info("");
            logger.info("Enter 'c' followed by <ENTER> to continue:");
            String input = scanner.nextLine();

            if (input.trim().equalsIgnoreCase("c")) {
                logger.info("Continuing with the program...");
                logger.info("");
                break;
            } else {
                logger.info("Invalid input. Please try again.");
            }
        }
    }
}
```
A wrapper class for Neptune SDK methods.

```
public class NeptuneActions {
    private CompletableFuture<Void> instanceCheckFuture;
    private static NeptuneAsyncClient neptuneAsyncClient;
    private final Region region = Region.US_EAST_1;
    private static final Logger logger = LoggerFactory.getLogger(NeptuneActions.class);
    private final NeptuneClient neptuneClient = NeptuneClient.builder().region(region).build();

    /**
     * Retrieves an instance of the NeptuneAsyncClient.
     * <p>
     * This method initializes and returns a singleton instance of the NeptuneAsyncClient. The client
     * is configured with the following settings:
     * <ul>
     *     <li>Maximum concurrency: 100</li>
     *     <li>Connection timeout: 60 seconds</li>
     *     <li>Read timeout: 60 seconds</li>
     *     <li>Write timeout: 60 seconds</li>
     *     <li>API call timeout: 2 minutes</li>
     *     <li>API call attempt timeout: 90 seconds</li>
     *     <li>Retry strategy: STANDARD</li>
     * </ul>
     * The client is built using the NettyNioAsyncHttpClient.
     *
     * @return the singleton instance of the NeptuneAsyncClient
     */
    private static NeptuneAsyncClient getAsyncClient() {
        if (neptuneAsyncClient == null) {
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

            neptuneAsyncClient = NeptuneAsyncClient.builder()
                    .httpClient(httpClient)
                    .overrideConfiguration(overrideConfig)
                    .build();
        }
        return neptuneAsyncClient;
    }

    /**
     * Asynchronously deletes a set of Amazon Neptune resources in a defined order.
     * <p>
     * The method performs the following operations in sequence:
     * <ol>
     *     <li>Deletes the Neptune DB instance identified by {@code dbInstanceId}.</li>
     *     <li>Waits until the DB instance is fully deleted.</li>
     *     <li>Deletes the Neptune DB cluster identified by {@code dbClusterId}.</li>
     *     <li>Deletes the Neptune DB subnet group identified by {@code subnetGroupName}.</li>
     * </ol>
     * <p>
     * If any step fails, the subsequent operations are not performed, and the exception
     * is logged. This method blocks the calling thread until all operations complete.
     *
     * @param dbInstanceId      the ID of the Neptune DB instance to delete
     * @param dbClusterId       the ID of the Neptune DB cluster to delete
     * @param subnetGroupName   the name of the Neptune DB subnet group to delete
     */
    public void deleteNeptuneResourcesAsync(String dbInstanceId, String dbClusterId, String subnetGroupName) {
        deleteDBInstanceAsync(dbInstanceId)
                .thenCompose(v -> waitUntilInstanceDeletedAsync(dbInstanceId))
                .thenCompose(v -> deleteDBClusterAsync(dbClusterId))
                .thenCompose(v -> deleteDBSubnetGroupAsync(subnetGroupName))
                .whenComplete((v, ex) -> {
                    if (ex != null) {
                        logger.info("Failed to delete Neptune resources: " + ex.getMessage());
                    } else {
                        logger.info("Neptune resources deleted successfully.");
                    }
                })
                .join(); // Waits for the entire async chain to complete
    }

    /**
     * Deletes a subnet group.
     *
     * @param subnetGroupName the identifier of the subnet group to delete
     * @return a {@link CompletableFuture} that completes when the cluster has been deleted
     */
    public CompletableFuture<Void> deleteDBSubnetGroupAsync(String subnetGroupName) {
        DeleteDbSubnetGroupRequest request = DeleteDbSubnetGroupRequest.builder()
                .dbSubnetGroupName(subnetGroupName)
                .build();

        return getAsyncClient().deleteDBSubnetGroup(request)
                .thenAccept(response -> logger.info("🗑️ Deleting Subnet Group: " + subnetGroupName));
    }

    /**
     * Deletes a DB instance asynchronously.
     *
     * @param clusterId the identifier of the cluster to delete
     * @return a {@link CompletableFuture} that completes when the cluster has been deleted
     */
    public CompletableFuture<Void> deleteDBClusterAsync(String clusterId) {
        DeleteDbClusterRequest request = DeleteDbClusterRequest.builder()
                .dbClusterIdentifier(clusterId)
                .skipFinalSnapshot(true)
                .build();

        return getAsyncClient().deleteDBCluster(request)
                .thenAccept(response -> System.out.println("🗑️ Deleting DB Cluster: " + clusterId));
    }

    public CompletableFuture<Void> waitUntilInstanceDeletedAsync(String instanceId) {
        CompletableFuture<Void> future = new CompletableFuture<>();
        long startTime = System.currentTimeMillis();
        checkInstanceDeletedRecursive(instanceId, startTime, future);
        return future;
    }

    /**
     * Deletes a DB instance asynchronously.
     *
     * @param instanceId the identifier of the DB instance to be deleted
     * @return a {@link CompletableFuture} that completes when the DB instance has been deleted
     */
    public CompletableFuture<Void> deleteDBInstanceAsync(String instanceId) {
        DeleteDbInstanceRequest request = DeleteDbInstanceRequest.builder()
                .dbInstanceIdentifier(instanceId)
                .skipFinalSnapshot(true)
                .build();

        return getAsyncClient().deleteDBInstance(request)
                .thenAccept(response -> System.out.println("🗑️ Deleting DB Instance: " + instanceId));
    }

    private void checkInstanceDeletedRecursive(String instanceId, long startTime, CompletableFuture<Void> future) {
        DescribeDbInstancesRequest request = DescribeDbInstancesRequest.builder()
                .dbInstanceIdentifier(instanceId)
                .build();

        getAsyncClient().describeDBInstances(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();
                        if (cause instanceof NeptuneException &&
                                ((NeptuneException) cause).awsErrorDetails().errorCode().equals("DBInstanceNotFound")) {
                            long elapsed = (System.currentTimeMillis() - startTime) / 1000;
                            logger.info("\r Instance %s deleted after %ds%n", instanceId, elapsed);
                            future.complete(null);
                            return;
                        }
                        future.completeExceptionally(new CompletionException("Error polling DB instance", cause));
                        return;
                    }

                    String status = response.dbInstances().get(0).dbInstanceStatus();
                    long elapsed = (System.currentTimeMillis() - startTime) / 1000;
                    System.out.printf("\r  Waiting: Instance %s status: %-10s (%ds elapsed)", instanceId, status, elapsed);
                    System.out.flush();

                    CompletableFuture.delayedExecutor(20, TimeUnit.SECONDS)
                            .execute(() -> checkInstanceDeletedRecursive(instanceId, startTime, future));
                });
    }

    public void waitForClusterStatus(String clusterId, String desiredStatus) {
        System.out.printf("Waiting for cluster '%s' to reach status '%s'...\n", clusterId, desiredStatus);
        CompletableFuture<Void> future = new CompletableFuture<>();
        checkClusterStatusRecursive(clusterId, desiredStatus, System.currentTimeMillis(), future);
        future.join();
    }

    private void checkClusterStatusRecursive(String clusterId, String desiredStatus, long startTime, CompletableFuture<Void> future) {
        DescribeDbClustersRequest request = DescribeDbClustersRequest.builder()
                .dbClusterIdentifier(clusterId)
                .build();

        getAsyncClient().describeDBClusters(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();
                        future.completeExceptionally(
                                new CompletionException("Error checking Neptune cluster status", cause)
                        );
                        return;
                    }

                    List<DBCluster> clusters = response.dbClusters();
                    if (clusters.isEmpty()) {
                        future.completeExceptionally(new RuntimeException("Cluster not found: " + clusterId));
                        return;
                    }

                    String currentStatus = clusters.get(0).status();
                    long elapsedSeconds = (System.currentTimeMillis() - startTime) / 1000;
                    System.out.printf("\r Elapsed: %-20s  Cluster status: %-20s", formatElapsedTime((int) elapsedSeconds), currentStatus);
                    System.out.flush();

                    if (desiredStatus.equalsIgnoreCase(currentStatus)) {
                        System.out.printf("\r Neptune cluster reached desired status '%s' after %s.\n", desiredStatus, formatElapsedTime((int) elapsedSeconds));
                        future.complete(null);
                    } else {
                        CompletableFuture.delayedExecutor(20, TimeUnit.SECONDS)
                                .execute(() -> checkClusterStatusRecursive(clusterId, desiredStatus, startTime, future));
                    }
                });
    }

    /**
     * Starts an Amazon Neptune DB cluster.
     *
     * @param clusterIdentifier the unique identifier of the DB cluster to be stopped
     */
    public CompletableFuture<StartDbClusterResponse> startDBClusterAsync(String clusterIdentifier) {
        StartDbClusterRequest clusterRequest = StartDbClusterRequest.builder()
                .dbClusterIdentifier(clusterIdentifier)
                .build();

        return getAsyncClient().startDBCluster(clusterRequest)
                .whenComplete((response, error) -> {
                    if (error != null) {
                        Throwable cause = error.getCause() != null ? error.getCause() : error;

                        if (cause instanceof ResourceNotFoundException) {
                            throw (ResourceNotFoundException) cause;
                        }

                        throw new RuntimeException("Failed to start DB cluster: " + cause.getMessage(), cause);
                    } else {
                        logger.info("DB Cluster starting: " + clusterIdentifier);
                    }
                });
    }

    /**
     * Stops an Amazon Neptune DB cluster.
     *
     * @param clusterIdentifier the unique identifier of the DB cluster to be stopped
     */
    public CompletableFuture<StopDbClusterResponse> stopDBClusterAsync(String clusterIdentifier) {
        StopDbClusterRequest clusterRequest = StopDbClusterRequest.builder()
                .dbClusterIdentifier(clusterIdentifier)
                .build();

        return getAsyncClient().stopDBCluster(clusterRequest)
                .whenComplete((response, error) -> {
                    if (error != null) {
                        Throwable cause = error.getCause() != null ? error.getCause() : error;

                        if (cause instanceof ResourceNotFoundException) {
                            throw (ResourceNotFoundException) cause;
                        }

                        throw new RuntimeException("Failed to stop DB cluster: " + cause.getMessage(), cause);
                    } else {
                        logger.info("DB Cluster stopped: " + clusterIdentifier);
                    }
                });
    }

    /**
     * Asynchronously describes the specified Amazon RDS DB cluster.
     *
     * @param clusterId the identifier of the DB cluster to describe
     * @return a {@link CompletableFuture} that completes when the operation is done, or throws a {@link RuntimeException}
     * if an error occurs
     */
    public CompletableFuture<Void> describeDBClustersAsync(String clusterId) {
        DescribeDbClustersRequest request = DescribeDbClustersRequest.builder()
                .dbClusterIdentifier(clusterId)
                .build();

        return getAsyncClient().describeDBClusters(request)
                .thenAccept(response -> {
                    for (DBCluster cluster : response.dbClusters()) {
                        logger.info("Cluster Identifier: " + cluster.dbClusterIdentifier());
                        logger.info("Status: " + cluster.status());
                        logger.info("Engine: " + cluster.engine());
                        logger.info("Engine Version: " + cluster.engineVersion());
                        logger.info("Endpoint: " + cluster.endpoint());
                        logger.info("Reader Endpoint: " + cluster.readerEndpoint());
                        logger.info("Availability Zones: " + cluster.availabilityZones());
                        logger.info("Subnet Group: " + cluster.dbSubnetGroup());
                        logger.info("VPC Security Groups:");
                        cluster.vpcSecurityGroups().forEach(vpcGroup ->
                                logger.info("  - " + vpcGroup.vpcSecurityGroupId()));
                        logger.info("Storage Encrypted: " + cluster.storageEncrypted());
                        logger.info("IAM DB Auth Enabled: " + cluster.iamDatabaseAuthenticationEnabled());
                        logger.info("Backup Retention Period: " + cluster.backupRetentionPeriod() + " days");
                        logger.info("Preferred Backup Window: " + cluster.preferredBackupWindow());
                        logger.info("Preferred Maintenance Window: " + cluster.preferredMaintenanceWindow());
                        logger.info("------");
                    }
                })
                .exceptionally(ex -> {
                    Throwable cause = ex.getCause() != null ? ex.getCause() : ex;

                    if (cause instanceof ResourceNotFoundException) {
                        throw (ResourceNotFoundException) cause;
                    }

                    throw new RuntimeException("Failed to describe the DB cluster: " + cause.getMessage(), cause);
                });
    }

    public CompletableFuture<Void> checkInstanceStatus(String instanceId, String desiredStatus) {
        CompletableFuture<Void> future = new CompletableFuture<>();
        long startTime = System.currentTimeMillis();
        checkStatusRecursive(instanceId, desiredStatus.toLowerCase(), startTime, future);
        return future;
    }

    /**
     * Checks the status of a Neptune instance recursively until the desired status is reached or a timeout occurs.
     *
     * @param instanceId     the ID of the Neptune instance to check
     * @param desiredStatus  the desired status of the Neptune instance
     * @param startTime      the start time of the operation, used to calculate the elapsed time
     * @param future         a {@link CompletableFuture} that will be completed when the desired status is reached
     */
    private void checkStatusRecursive(String instanceId, String desiredStatus, long startTime, CompletableFuture<Void> future) {
        DescribeDbInstancesRequest request = DescribeDbInstancesRequest.builder()
                .dbInstanceIdentifier(instanceId)
                .build();

        getAsyncClient().describeDBInstances(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();
                        future.completeExceptionally(
                                new CompletionException("Error checking Neptune instance status", cause)
                        );
                        return;
                    }

                    List<DBInstance> instances = response.dbInstances();
                    if (instances.isEmpty()) {
                        future.completeExceptionally(new RuntimeException("Instance not found: " + instanceId));
                        return;
                    }

                    String currentStatus = instances.get(0).dbInstanceStatus();
                    long elapsedSeconds = (System.currentTimeMillis() - startTime) / 1000;
                    System.out.printf("\r Elapsed: %-20s  Status: %-20s", formatElapsedTime((int) elapsedSeconds), currentStatus);
                    System.out.flush();

                    if (desiredStatus.equalsIgnoreCase(currentStatus)) {
                        System.out.printf("\r Neptune instance reached desired status '%s' after %s.\n", desiredStatus, formatElapsedTime((int) elapsedSeconds));
                        future.complete(null);
                    } else {
                        CompletableFuture.delayedExecutor(20, TimeUnit.SECONDS)
                                .execute(() -> checkStatusRecursive(instanceId, desiredStatus, startTime, future));
                    }
                });
    }

    private String formatElapsedTime(int seconds) {
        int minutes = seconds / 60;
        int remainingSeconds = seconds % 60;

        if (minutes > 0) {
            return minutes + (minutes == 1 ? " min" : " mins") + ", " +
                    remainingSeconds + (remainingSeconds == 1 ? " sec" : " secs");
        } else {
            return remainingSeconds + (remainingSeconds == 1 ? " sec" : " secs");
        }
    }

    /**
     * Creates a new Amazon Neptune DB instance asynchronously.
     *
     * @param dbInstanceId the identifier for the new DB instance
     * @param dbClusterId  the identifier for the DB cluster that the new instance will be a part of
     * @return a {@link CompletableFuture} that completes with the identifier of the newly created DB instance
     * @throws CompletionException if the operation fails, with a cause of either:
     *                             - {@link ServiceQuotaExceededException} if the request would exceed the maximum quota, or
     *                             - a general exception with the failure message
     */
    public CompletableFuture<String> createDBInstanceAsync(String dbInstanceId, String dbClusterId) {
        CreateDbInstanceRequest request = CreateDbInstanceRequest.builder()
                .dbInstanceIdentifier(dbInstanceId)
                .dbInstanceClass("db.r5.large")
                .engine("neptune")
                .dbClusterIdentifier(dbClusterId)
                .build();

        return getAsyncClient().createDBInstance(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();
                        if (cause instanceof ServiceQuotaExceededException) {
                            throw new CompletionException("The operation was denied because the request would exceed the maximum quota.", cause);
                        }
                        throw new CompletionException("Failed to create Neptune DB instance: " + exception.getMessage(), exception);
                    }
                })
                .thenApply(response -> {
                    String instanceId = response.dbInstance().dbInstanceIdentifier();
                    logger.info("Created Neptune DB Instance: " + instanceId);
                    return instanceId;
                });
    }

    /**
     * Creates a new Amazon Neptune DB cluster asynchronously.
     *
     * @param dbName the name of the DB cluster to be created
     * @return a CompletableFuture that, when completed, provides the ID of the created DB cluster
     * @throws CompletionException if the operation fails for any reason, including if the request would exceed the maximum quota
     */
    public CompletableFuture<String> createDBClusterAsync(String dbName) {
        CreateDbClusterRequest request = CreateDbClusterRequest.builder()
                .dbClusterIdentifier(dbName)
                .engine("neptune")
                .deletionProtection(false)
                .backupRetentionPeriod(1)
                .build();

        return getAsyncClient().createDBCluster(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();
                        if (cause instanceof ServiceQuotaExceededException) {
                            throw new CompletionException("The operation was denied because the request would exceed the maximum quota.", cause);
                        }
                        throw new CompletionException("Failed to create Neptune DB cluster: " + exception.getMessage(), exception);
                    }
                })
                .thenApply(response -> {
                    String clusterId = response.dbCluster().dbClusterIdentifier();
                    logger.info("DB Cluster created: " + clusterId);
                    return clusterId;
                });
    }

    /**
     * Creates a new DB subnet group asynchronously.
     *
     * @param groupName the name of the subnet group to create
     * @return a CompletableFuture that, when completed, returns the Amazon Resource Name (ARN) of the created subnet group
     * @throws CompletionException if the operation fails, with a cause that may be a ServiceQuotaExceededException if the request would exceed the maximum quota
     */
    public CompletableFuture<String> createSubnetGroupAsync(String groupName) {

        // Get the Amazon Virtual Private Cloud (VPC) where the Neptune cluster and resources will be created
        String vpcId = getDefaultVpcId();
        logger.info("VPC is : " + vpcId);

        List<String> subnetList = getSubnetIds(vpcId);
        for (String subnetId : subnetList) {
            System.out.println("Subnet group:" +subnetId);
        }

        CreateDbSubnetGroupRequest request = CreateDbSubnetGroupRequest.builder()
                .dbSubnetGroupName(groupName)
                .dbSubnetGroupDescription("Subnet group for Neptune cluster")
                .subnetIds(subnetList)
                .build();

        return getAsyncClient().createDBSubnetGroup(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();
                        if (cause instanceof ServiceQuotaExceededException) {
                            throw new CompletionException("The operation was denied because the request would exceed the maximum quota.", cause);
                        }
                        throw new CompletionException("Failed to create subnet group: " + exception.getMessage(), exception);
                    }
                })
                .thenApply(response -> {
                    String name = response.dbSubnetGroup().dbSubnetGroupName();
                    String arn = response.dbSubnetGroup().dbSubnetGroupArn();
                    logger.info("Subnet group created: " + name);
                    return arn;
                });
    }

    private List<String> getSubnetIds(String vpcId) {
        try (Ec2Client ec2 = Ec2Client.builder().region(region).build()) {
            DescribeSubnetsRequest request = DescribeSubnetsRequest.builder()
                    .filters(builder -> builder.name("vpc-id").values(vpcId))
                    .build();

            DescribeSubnetsResponse response = ec2.describeSubnets(request);
            return response.subnets().stream()
                    .map(Subnet::subnetId)
                    .collect(Collectors.toList());
        }
    }

    public static String getDefaultVpcId() {
        Ec2Client ec2 = Ec2Client.builder()
                .region(Region.US_EAST_1)
                .build();

        Filter myFilter = Filter.builder()
                .name("isDefault")
                .values("true")
                .build();

        List<Filter> filterList = new ArrayList<>();
        filterList.add(myFilter);

        DescribeVpcsRequest request = DescribeVpcsRequest.builder()
                .filters(filterList)
                .build();

        DescribeVpcsResponse response = ec2.describeVpcs(request);
        if (!response.vpcs().isEmpty()) {
            Vpc defaultVpc = response.vpcs().get(0);
            return defaultVpc.vpcId();
        } else {
            throw new RuntimeException("No default VPC found in this region.");
        }
    }
}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [CreateDBCluster](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateDBCluster)
  + [CreateDBInstance](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateDBInstance)
  + [CreateDBSubnetGroup](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateDBSubnetGroup)
  + [CreateGraph](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateGraph)
  + [DeleteDBCluster](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBCluster)
  + [DeleteDBInstance](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBInstance)
  + [DeleteDBSubnetGroup](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBSubnetGroup)
  + [DescribeDBClusters](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeDBClusters)
  + [DescribeDBInstances](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeDBInstances)
  + [ExecuteGremlinProfileQuery](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ExecuteGremlinProfileQuery)
  + [ExecuteGremlinQuery](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ExecuteGremlinQuery)
  + [ExecuteOpenCypherExplainQuery](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ExecuteOpenCypherExplainQuery)
  + [ExecuteQuery](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ExecuteQuery)
  + [StartDBCluster](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/StartDBCluster)
  + [StopDBCluster](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/StopDBCluster)

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
import boto3
import time
from botocore.exceptions import ClientError

# Constants used in this scenario
POLL_INTERVAL_SECONDS = 10
TIMEOUT_SECONDS = 1200  # 20 minutes

def delete_db_cluster(neptune_client, cluster_id: str):
    """
    Deletes a Neptune DB cluster and throws exceptions to the caller.

    Args:
        neptune_client (boto3.client): The Neptune client object.
        cluster_id (str): The ID of the Neptune DB cluster to be deleted.

    Raises:
        ClientError: If the delete operation fails.
    """
    request = {
        'DBClusterIdentifier': cluster_id,
        'SkipFinalSnapshot': True
    }

    try:
        print(f"Deleting DB Cluster: {cluster_id}")
        neptune_client.delete_db_cluster(**request)

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "DBClusterNotFoundFault":
            print(f"Cluster '{cluster_id}' not found or already deleted.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't delete DB cluster. {code}: {message}")
        raise

def format_elapsed_time(seconds: int) -> str:
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"

def delete_db_instance(neptune_client, instance_id: str):
    """
    Deletes a Neptune DB instance and waits for its deletion to complete.
    Raises exception to be handled by calling code.
    """
    print(f"Initiating deletion of DB Instance: {instance_id}")
    try:
        neptune_client.delete_db_instance(
            DBInstanceIdentifier=instance_id,
            SkipFinalSnapshot=True
        )

        print(f"Waiting for DB Instance '{instance_id}' to be deleted...")
        waiter = neptune_client.get_waiter('db_instance_deleted')
        waiter.wait(
            DBInstanceIdentifier=instance_id,
            WaiterConfig={
                'Delay': 30,
                'MaxAttempts': 40
            }
        )

        print(f"DB Instance '{instance_id}' successfully deleted.")

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "DBInstanceNotFoundFault":
            print(f"Instance '{instance_id}' not found or already deleted.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't delete DB instance. {code}: {message}")
        raise

def delete_db_subnet_group(neptune_client, subnet_group_name):
    """
    Deletes a Neptune DB subnet group synchronously using Boto3.

    Args:
        neptune_client (boto3.client): The Neptune client.
        subnet_group_name (str): The name of the DB subnet group to delete.

    Raises:
        ClientError: If the delete operation fails.
    """
    delete_group_request = {
        'DBSubnetGroupName': subnet_group_name
    }

    try:
        neptune_client.delete_db_subnet_group(**delete_group_request)
        print(f"️ Deleting Subnet Group: {subnet_group_name}")

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "DBSubnetGroupNotFoundFault":
            print(f"Subnet group '{subnet_group_name}' not found or already deleted.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't delete subnet group. {code}: {message}")
        raise

def wait_for_cluster_status(
        neptune_client,
        cluster_id: str,
        desired_status: str,
        timeout_seconds: int = TIMEOUT_SECONDS,
        poll_interval_seconds: int = POLL_INTERVAL_SECONDS
):
    """
    Waits for a Neptune DB cluster to reach a desired status.

    Args:
        neptune_client (boto3.client): The Amazon Neptune client.
        cluster_id (str): The identifier of the Neptune DB cluster.
        desired_status (str): The target status (e.g., "available", "stopped").
        timeout_seconds (int): Max time to wait in seconds (default: 1200).
        poll_interval_seconds (int): Polling interval in seconds (default: 10).

    Raises:
        RuntimeError: If the desired status is not reached before timeout.
    """
    print(f"Waiting for cluster '{cluster_id}' to reach status '{desired_status}'...")
    start_time = time.time()

    while True:
        # Prepare request object
        describe_cluster_request = {
            'DBClusterIdentifier': cluster_id
        }

        # Call the Neptune API
        response = neptune_client.describe_db_clusters(**describe_cluster_request)
        clusters = response.get('DBClusters', [])
        current_status = clusters[0].get('Status') if clusters else None
        elapsed_seconds = int(time.time() - start_time)

        status_str = current_status if current_status else "Unknown"
        print(
            f"\r Elapsed: {format_elapsed_time(elapsed_seconds):<20}  Cluster status: {status_str:<20}",
            end="", flush=True
        )

        if current_status and current_status.lower() == desired_status.lower():
            print(
                f"\nNeptune cluster reached desired status '{desired_status}' after {format_elapsed_time(elapsed_seconds)}."
            )
            return

        if elapsed_seconds > timeout_seconds:
            raise RuntimeError(f"Timeout waiting for Neptune cluster to reach status: {desired_status}")

        time.sleep(poll_interval_seconds)

def start_db_cluster(neptune_client, cluster_identifier: str):
    """
    Starts an Amazon Neptune DB cluster and waits until it reaches 'available'.

    Args:
        neptune_client (boto3.client): The Neptune client.
        cluster_identifier (str): The DB cluster identifier.

    Raises:
        ClientError: Propagates AWS API issues like resource not found.
        RuntimeError: If cluster doesn't reach 'available' within timeout.
    """
    try:
        # Initial wait in case the cluster was just stopped
        time.sleep(30)
        neptune_client.start_db_cluster(DBClusterIdentifier=cluster_identifier)
    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't start DB cluster. Here's why: {code}: {message}")
        raise

    start_time = time.time()
    paginator = neptune_client.get_paginator('describe_db_clusters')

    while True:
        try:
            pages = paginator.paginate(DBClusterIdentifier=cluster_identifier)
            clusters = []
            for page in pages:
                clusters.extend(page.get('DBClusters', []))
        except ClientError as err:
            code = err.response["Error"]["Code"]
            message = err.response["Error"]["Message"]

            if code == "DBClusterNotFound":
                print(f"Cluster '{cluster_identifier}' not found while polling. It may have been deleted.")
            else:
                print(f"Couldn't describe DB cluster. Here's why: {code}: {message}")
            raise

        status = clusters[0].get('Status') if clusters else None
        elapsed = time.time() - start_time

        print(f"\rElapsed: {int(elapsed)}s – Cluster status: {status}", end="", flush=True)

        if status and status.lower() == 'available':
            print(f"\n🎉 Cluster '{cluster_identifier}' is available.")
            return

        if elapsed > TIMEOUT_SECONDS:
            raise RuntimeError(f"Timeout waiting for cluster '{cluster_identifier}' to become available.")

        time.sleep(POLL_INTERVAL_SECONDS)

def stop_db_cluster(neptune_client, cluster_identifier: str):
    """
    Stops an Amazon Neptune DB cluster and waits until it's fully stopped.

    Args:
        neptune_client (boto3.client): The Neptune client.
        cluster_identifier (str): The DB cluster identifier.

    Raises:
        ClientError: For AWS API errors (e.g., resource not found).
        RuntimeError: If the cluster doesn't stop within the timeout.
    """
    try:
        neptune_client.stop_db_cluster(DBClusterIdentifier=cluster_identifier)
    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't stop DB cluster. Here's why: {code}: {message}")
        raise

    start_time = time.time()
    paginator = neptune_client.get_paginator('describe_db_clusters')

    while True:
        try:
            pages = paginator.paginate(DBClusterIdentifier=cluster_identifier)
            clusters = []
            for page in pages:
                clusters.extend(page.get('DBClusters', []))
        except ClientError as err:
            code = err.response["Error"]["Code"]
            message = err.response["Error"]["Message"]

            if code == "DBClusterNotFound":
                print(f"Cluster '{cluster_identifier}' not found while polling. It may have been deleted.")
            else:
                print(f"Couldn't describe DB cluster. Here's why: {code}: {message}")
            raise

        status = clusters[0].get('Status') if clusters else None
        elapsed = time.time() - start_time

        print(f"\rElapsed: {int(elapsed)}s – Cluster status: {status}", end="", flush=True)

        if status and status.lower() == 'stopped':
            print(f"\nCluster '{cluster_identifier}' is now stopped.")
            return

        if elapsed > TIMEOUT_SECONDS:
            raise RuntimeError(f"Timeout waiting for cluster '{cluster_identifier}' to stop.")

        time.sleep(POLL_INTERVAL_SECONDS)

def describe_db_clusters(neptune_client, cluster_id: str):
    """
    Describes details of a Neptune DB cluster, paginating if needed.

    Args:
        neptune_client (boto3.client): The Neptune client.
        cluster_id (str): The ID of the cluster to describe.

    Raises:
        ClientError: If there's an AWS API error (e.g., cluster not found).
    """
    paginator = neptune_client.get_paginator('describe_db_clusters')

    try:
        pages = paginator.paginate(DBClusterIdentifier=cluster_id)

        found = False
        for page in pages:
            for cluster in page.get('DBClusters', []):
                found = True
                print(f"Cluster Identifier: {cluster.get('DBClusterIdentifier')}")
                print(f"Status: {cluster.get('Status')}")
                print(f"Engine: {cluster.get('Engine')}")
                print(f"Engine Version: {cluster.get('EngineVersion')}")
                print(f"Endpoint: {cluster.get('Endpoint')}")
                print(f"Reader Endpoint: {cluster.get('ReaderEndpoint')}")
                print(f"Availability Zones: {cluster.get('AvailabilityZones')}")
                print(f"Subnet Group: {cluster.get('DBSubnetGroup')}")
                print("VPC Security Groups:")
                for vpc_group in cluster.get('VpcSecurityGroups', []):
                    print(f"  - {vpc_group.get('VpcSecurityGroupId')}")
                print(f"Storage Encrypted: {cluster.get('StorageEncrypted')}")
                print(f"IAM Auth Enabled: {cluster.get('IAMDatabaseAuthenticationEnabled')}")
                print(f"Backup Retention Period: {cluster.get('BackupRetentionPeriod')} days")
                print(f"Preferred Backup Window: {cluster.get('PreferredBackupWindow')}")
                print(f"Preferred Maintenance Window: {cluster.get('PreferredMaintenanceWindow')}")
                print("------")

        if not found:
            # Treat empty response as cluster not found
            raise ClientError(
                {"Error": {"Code": "DBClusterNotFound", "Message": f"No cluster found with ID '{cluster_id}'"}},
                "DescribeDBClusters"
            )

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        elif code == "DBClusterNotFound":
            print(f"Cluster '{cluster_id}' not found. Please verify the cluster ID.")
        else:
            print(f"Couldn't describe DB cluster. Here's why: {code}: {message}")
        raise

def check_instance_status(neptune_client, instance_id: str, desired_status: str):
    """
    Polls the status of a Neptune DB instance until it reaches desired_status.
    Uses pagination via describe_db_instances — even for a single instance.

    Raises:
      ClientError: If describe_db_instances fails (e.g., instance not found).
      RuntimeError: If timeout expires before reaching desired status.
    """
    paginator = neptune_client.get_paginator('describe_db_instances')
    start_time = time.time()

    while True:
        try:
            pages = paginator.paginate(DBInstanceIdentifier=instance_id)
            instances = []
            for page in pages:
                instances.extend(page.get('DBInstances', []))

        except ClientError as err:
            code = err.response["Error"]["Code"]
            message = err.response["Error"]["Message"]

            if code == "DBInstanceNotFound":
                print(f"Instance '{instance_id}' not found. Please verify the instance ID.")
            else:
                print(f"Failed to describe DB instance. {code}: {message}")
            raise

        current_status = instances[0].get('DBInstanceStatus') if instances else None
        elapsed = int(time.time() - start_time)

        print(f"\rElapsed: {format_elapsed_time(elapsed)}  Status: {current_status}", end="", flush=True)

        if current_status and current_status.lower() == desired_status.lower():
            print(f"\nInstance '{instance_id}' reached '{desired_status}' in {format_elapsed_time(elapsed)}.")
            return

        if elapsed > TIMEOUT_SECONDS:
            raise RuntimeError(f"Timeout waiting for '{instance_id}' to reach '{desired_status}'")

        time.sleep(POLL_INTERVAL_SECONDS)

def create_db_instance(neptune_client, db_instance_id: str, db_cluster_id: str) -> str:
    try:
        request = {
            'DBInstanceIdentifier': db_instance_id,
            'DBInstanceClass': 'db.r5.large',
            'Engine': 'neptune',
            'DBClusterIdentifier': db_cluster_id
        }

        print(f"Creating Neptune DB Instance: {db_instance_id}")
        response = neptune_client.create_db_instance(**request)

        instance = response.get('DBInstance')
        if not instance or 'DBInstanceIdentifier' not in instance:
            raise RuntimeError("Instance creation succeeded but no ID returned.")

        print(f"Waiting for DB Instance '{db_instance_id}' to become available...")
        waiter = neptune_client.get_waiter('db_instance_available')
        waiter.wait(
            DBInstanceIdentifier=db_instance_id,
            WaiterConfig={'Delay': 30, 'MaxAttempts': 40}
        )

        print(f"DB Instance '{db_instance_id}' is now available.")
        return instance['DBInstanceIdentifier']

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't create DB instance. Here's why: {code}: {message}")
        raise

    except Exception as e:
        print(f"Unexpected error creating DB instance '{db_instance_id}': {e}")
        raise RuntimeError(f"Unexpected error creating DB instance '{db_instance_id}': {e}") from e

def create_db_cluster(neptune_client, db_name: str) -> str:
    """
    Creates a Neptune DB cluster and returns its identifier.

    Args:
        neptune_client (boto3.client): The Neptune client object.
        db_name (str): The desired cluster identifier.

    Returns:
        str: The DB cluster identifier.

    Raises:
        RuntimeError: For any failure or AWS error, with a user-friendly message.
    """
    request = {
        'DBClusterIdentifier': db_name,
        'Engine': 'neptune',
        'DeletionProtection': False,
        'BackupRetentionPeriod': 1
    }

    try:
        response = neptune_client.create_db_cluster(**request)
        cluster = response.get('DBCluster') or {}

        cluster_id = cluster.get('DBClusterIdentifier')
        if not cluster_id:
            raise RuntimeError("Cluster created but no ID returned.")

        print(f"DB Cluster created: {cluster_id}")
        return cluster_id

    except ClientError as e:
        code = e.response["Error"]["Code"]
        message = e.response["Error"]["Message"]

        if code in ("ServiceQuotaExceededException", "DBClusterQuotaExceededFault"):
            raise RuntimeError("You have exceeded the quota for Neptune DB clusters.") from e
        else:
            raise RuntimeError(f"AWS error [{code}]: {message}") from e

    except Exception as e:
        raise RuntimeError(f"Unexpected error creating DB cluster '{db_name}': {e}") from e

def get_subnet_ids(vpc_id: str) -> list[str]:
    ec2_client = boto3.client('ec2')

    describe_subnets_request = {
        'Filters': [{'Name': 'vpc-id', 'Values': [vpc_id]}]
    }

    response = ec2_client.describe_subnets(**describe_subnets_request)
    subnets = response.get('Subnets', [])
    subnet_ids = [subnet['SubnetId'] for subnet in subnets if 'SubnetId' in subnet]
    return subnet_ids

def get_default_vpc_id() -> str:
    ec2_client = boto3.client('ec2')
    describe_vpcs_request = {
        'Filters': [{'Name': 'isDefault', 'Values': ['true']}]
    }

    response = ec2_client.describe_vpcs(**describe_vpcs_request)
    vpcs = response.get('Vpcs', [])
    if not vpcs:
        raise RuntimeError("No default VPC found in this region.")

    default_vpc_id = vpcs[0]['VpcId']
    print(f"Default VPC ID: {default_vpc_id}")
    return default_vpc_id

def create_subnet_group(neptune_client, group_name: str):
    """
    Creates a Neptune DB subnet group and returns its name and ARN.

    Args:
        neptune_client (boto3.client): The Neptune client object.
        group_name (str): The desired name of the subnet group.

    Returns:
        tuple(str, str): (subnet_group_name, subnet_group_arn)

    Raises:
        RuntimeError: For quota errors or other AWS-related failures.
    """
    vpc_id = get_default_vpc_id()
    subnet_ids = get_subnet_ids(vpc_id)

    request = {
        'DBSubnetGroupName': group_name,
        'DBSubnetGroupDescription': 'My Neptune subnet group',
        'SubnetIds': subnet_ids,
        'Tags': [{'Key': 'Environment', 'Value': 'Dev'}]
    }

    try:
        response = neptune_client.create_db_subnet_group(**request)
        sg = response.get("DBSubnetGroup", {})
        name = sg.get("DBSubnetGroupName")
        arn = sg.get("DBSubnetGroupArn")

        if not name or not arn:
            raise RuntimeError("Response missing subnet group name or ARN.")

        print(f"Subnet group created: {name}")
        print(f"ARN: {arn}")
        return name, arn

    except ClientError as e:
        code = e.response["Error"]["Code"]
        msg = e.response["Error"]["Message"]

        if code == "ServiceQuotaExceededException":
            print("Subnet group quota exceeded.")
            raise RuntimeError("Subnet group quota exceeded.") from e
        else:
            print(f"AWS error [{code}]: {msg}")
            raise RuntimeError(f"AWS error [{code}]: {msg}") from e

    except Exception as e:
        print(f"Unexpected error creating subnet group '{group_name}': {e}")
        raise RuntimeError(f"Unexpected error creating subnet group '{group_name}': {e}") from e

def wait_for_input_to_continue():
    input("\nPress <ENTER> to continue...")
    print("Continuing with the program...\n")

def run_scenario(neptune_client, subnet_group_name: str, db_instance_id: str, cluster_name: str):
    print("-" * 88)
    print("1. Create a Neptune DB Subnet Group")
    wait_for_input_to_continue()

    try:
        name, arn = create_subnet_group(neptune_client, subnet_group_name)
        print(f"Subnet group successfully created: {name}")

        print("-" * 88)
        print("2. Create a Neptune Cluster")
        wait_for_input_to_continue()
        db_cluster_id = create_db_cluster(neptune_client, cluster_name)

        print("-" * 88)
        print("3. Create a Neptune DB Instance")
        wait_for_input_to_continue()
        create_db_instance(neptune_client, db_instance_id, cluster_name)

        print("-" * 88)
        print("4. Check the status of the Neptune DB Instance")
        print("""
        Even though you're targeting a single DB instance,
        describe_db_instances supports pagination and can return multiple pages.

        Handling paginated responses ensures your method continues to work reliably
        even if AWS returns large or paged results.
        """)
        wait_for_input_to_continue()
        check_instance_status(neptune_client, db_instance_id, "available")

        print("-" * 88)
        print("5. Show Neptune Cluster details")
        wait_for_input_to_continue()
        describe_db_clusters(neptune_client, db_cluster_id)

        print("-" * 88)
        print("6. Stop the Amazon Neptune cluster")
        print("""
            Boto3 doesn't currently offer a
            built-in waiter for stop_db_cluster,
            This example implements a custom polling
            strategy until the cluster is in a stopped state.
        """)
        wait_for_input_to_continue()
        stop_db_cluster(neptune_client, db_cluster_id)
        check_instance_status(neptune_client, db_instance_id, "stopped")

        print("-" * 88)
        print("7. Start the Amazon Neptune cluster")
        print("""
            Boto3 doesn't currently offer a
            built-in waiter for start_db_cluster,
            This example implements a custom polling
            strategy until the cluster is in an available state.
        """)
        wait_for_input_to_continue()
        start_db_cluster(neptune_client, db_cluster_id)
        wait_for_cluster_status(neptune_client, db_cluster_id, "available")
        check_instance_status(neptune_client, db_instance_id, "available")

        print("All Neptune resources are now available.")
        print("-" * 88)

        print("-" * 88)
        print("8. Delete the Neptune Assets")
        print("Would you like to delete the Neptune Assets? (y/n)")
        del_ans = input().strip().lower()

        if del_ans == "y":
            print("You selected to delete the Neptune assets.")

            delete_db_instance(neptune_client, db_instance_id)
            delete_db_cluster(neptune_client, db_cluster_id)
            delete_db_subnet_group(neptune_client, subnet_group_name)

            print("Neptune resources deleted successfully")

    except ClientError as ce:
        code = ce.response["Error"]["Code"]

        if code in ("DBInstanceNotFound", "DBInstanceNotFoundFault", "ResourceNotFound"):
            print(f"Instance '{db_instance_id}' not found.")
        elif code in ("DBClusterNotFound", "DBClusterNotFoundFault", "ResourceNotFoundFault"):
            print(f"Cluster '{cluster_name}' not found.")
        elif code == "DBSubnetGroupNotFoundFault":
            print(f"Subnet group '{subnet_group_name}' not found.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"AWS error [{code}]: {ce.response['Error']['Message']}")
            raise  # re-raise unexpected errors

    except RuntimeError as re:
        print(f"Runtime error or timeout: {re}")

def main():
    neptune_client = boto3.client('neptune')

    # Customize the following names to match your Neptune setup
    # (You must change these to unique values for your environment)
    subnet_group_name = "neptuneSubnetGroup111"
    cluster_name = "neptuneCluster111"
    db_instance_id = "neptuneDB111"

    print("""
    Amazon Neptune is a fully managed graph database service by AWS...
    Let's get started!
    """)
    wait_for_input_to_continue()
    run_scenario(neptune_client, subnet_group_name, db_instance_id, cluster_name)

    print("""
    Thank you for checking out the Amazon Neptune Service Use demo.
    For more AWS code examples, visit:
    https://docs.aws.amazon.com/code-library/latest/ug/what-is-code-library.html
    """)

if __name__ == "__main__":
    main()
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CreateDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBCluster)
  + [CreateDBInstance](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBInstance)
  + [CreateDBSubnetGroup](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBSubnetGroup)
  + [CreateGraph](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateGraph)
  + [DeleteDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBCluster)
  + [DeleteDBInstance](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBInstance)
  + [DeleteDBSubnetGroup](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBSubnetGroup)
  + [DescribeDBClusters](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBClusters)
  + [DescribeDBInstances](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBInstances)
  + [ExecuteGremlinProfileQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteGremlinProfileQuery)
  + [ExecuteGremlinQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteGremlinQuery)
  + [ExecuteOpenCypherExplainQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteOpenCypherExplainQuery)
  + [ExecuteQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteQuery)
  + [StartDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/StartDBCluster)
  + [StopDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/StopDBCluster)

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
