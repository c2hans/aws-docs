---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/java_2_neptune_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Neptune examples using SDK for Java 2.x
<a name="java_2_neptune_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Java 2.x with Neptune.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)
+ [Scenarios](#scenarios)

## Get started
<a name="get_started"></a>

### Hello Neptune
<a name="neptune_Hello_java_2_topic"></a>

The following code example shows how to get started using Neptune.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class HelloNeptune {
    public static void main(String[] args) {
        NeptuneAsyncClient neptuneClient = NeptuneAsyncClient.create();
        describeDbCluster(neptuneClient).join(); // This ensures the async code runs to completion
    }

    /**
     * Describes the Amazon Neptune DB clusters.
     *
     * @param neptuneClient the Neptune asynchronous client used to make the request
     * @return a {@link CompletableFuture} that completes when the operation is finished
     */
    public static CompletableFuture<Void> describeDbCluster(NeptuneAsyncClient neptuneClient) {
        DescribeDbClustersRequest request = DescribeDbClustersRequest.builder()
                .maxRecords(20)
                .build();

        SdkPublisher<DescribeDbClustersResponse> paginator = neptuneClient.describeDBClustersPaginator(request);
        CompletableFuture<Void> future = new CompletableFuture<>();

        paginator.subscribe(new Subscriber<DescribeDbClustersResponse>() {
            private Subscription subscription;

            @Override
            public void onSubscribe(Subscription s) {
                this.subscription = s;
                s.request(Long.MAX_VALUE); // request all items
            }

            @Override
            public void onNext(DescribeDbClustersResponse response) {
                response.dbClusters().forEach(cluster -> {
                    System.out.println("Cluster Identifier: " + cluster.dbClusterIdentifier());
                    System.out.println("Status: " + cluster.status());
                });
            }

            @Override
            public void onError(Throwable t) {
                future.completeExceptionally(t);
            }

            @Override
            public void onComplete() {
                future.complete(null);
            }
        });

        return future.whenComplete((result, throwable) -> {
            neptuneClient.close();
            if (throwable != null) {
                System.err.println("Error describing DB clusters: " + throwable.getMessage());
            }
        });
    }
```
+  For API details, see [DescribeDBClustersPaginator](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeDBClustersPaginator) in *AWS SDK for Java 2.x API Reference*.

## Basics
<a name="basics"></a>

### Learn the basics
<a name="neptune_Scenario_java_2_topic"></a>

The following code example shows how to:
+ Create an Amazon Neptune Subnet Group.
+ Create an Neptune Cluster.
+ Create an Neptune Instance.
+ Check the status of the Neptune Instance.
+ Show Neptune cluster details.
+ Stop the Neptune cluster.
+ Start the Neptune cluster.
+ Delete the Neptune Assets.

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

## Actions
<a name="actions"></a>

### `CreateDBCluster`
<a name="neptune_CreateDBCluster_java_2_topic"></a>

The following code example shows how to use `CreateDBCluster`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
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
```
+  For API details, see [CreateDBCluster](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateDBCluster) in *AWS SDK for Java 2.x API Reference*.

### `CreateDBInstance`
<a name="neptune_CreateDBInstance_java_2_topic"></a>

The following code example shows how to use `CreateDBInstance`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
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
```
+  For API details, see [CreateDBInstance](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateDBInstance) in *AWS SDK for Java 2.x API Reference*.

### `CreateDBSubnetGroup`
<a name="neptune_CreateDBSubnetGroup_java_2_topic"></a>

The following code example shows how to use `CreateDBSubnetGroup`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
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
```
+  For API details, see [CreateDBSubnetGroup](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateDBSubnetGroup) in *AWS SDK for Java 2.x API Reference*.

### `CreateGraph`
<a name="neptune_CreateGraph_java_2_topic"></a>

The following code example shows how to use `CreateGraph`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
    /**
     * Executes the process of creating a new Neptune graph.
     *
     * @param client        the Neptune graph client used to interact with the Neptune service
     * @param graphName     the name of the graph to be created
     * @throws NeptuneGraphException if an error occurs while creating the graph
     */
    public static void executeCreateGraph(NeptuneGraphClient client, String graphName) {
        try {
            // Create the graph request
            CreateGraphRequest request = CreateGraphRequest.builder()
                    .graphName(graphName)
                    .provisionedMemory(16)
                    .build();

            // Create the graph
            CreateGraphResponse response = client.createGraph(request);

            // Extract the graph name and ARN
            String createdGraphName = response.name();
            String graphArn = response.arn();
            String graphEndpoint = response.endpoint();

            System.out.println("Graph created successfully!");
            System.out.println("Graph Name: " + createdGraphName);
            System.out.println("Graph ARN: " + graphArn);
            System.out.println("Graph Endpoint: " +graphEndpoint );

        } catch (NeptuneGraphException e) {
            System.err.println("Failed to create graph: " + e.awsErrorDetails().errorMessage());
        } finally {
            client.close();
        }
   }
```
+  For API details, see [CreateGraph](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateGraph) in *AWS SDK for Java 2.x API Reference*.

### `DeleteDBCluster`
<a name="neptune_DeleteDBCluster_java_2_topic"></a>

The following code example shows how to use `DeleteDBCluster`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
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
```
+  For API details, see [DeleteDBCluster](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBCluster) in *AWS SDK for Java 2.x API Reference*.

### `DeleteDBInstance`
<a name="neptune_DeleteDBInstance_java_2_topic"></a>

The following code example shows how to use `DeleteDBInstance`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
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
```
+  For API details, see [DeleteDBInstance](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBInstance) in *AWS SDK for Java 2.x API Reference*.

### `DeleteDBSubnetGroup`
<a name="neptune_DeleteDBSubnetGroup_java_2_topic"></a>

The following code example shows how to use `DeleteDBSubnetGroup`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
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
```
+  For API details, see [DeleteDBSubnetGroup](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBSubnetGroup) in *AWS SDK for Java 2.x API Reference*.

### `DescribeDBClusters`
<a name="neptune_DescribeDBClusters_java_2_topic"></a>

The following code example shows how to use `DescribeDBClusters`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
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
```
+  For API details, see [DescribeDBClusters](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeDBClusters) in *AWS SDK for Java 2.x API Reference*.

### `DescribeDBInstances`
<a name="neptune_DescribeDBInstances_java_2_topic"></a>

The following code example shows how to use `DescribeDBInstances`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
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
```
+  For API details, see [DescribeDBInstances](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeDBInstances) in *AWS SDK for Java 2.x API Reference*.

### `ExecuteGremlinProfileQuery`
<a name="neptune_ExecuteGremlinProfileQuery_java_2_topic"></a>

The following code example shows how to use `ExecuteGremlinProfileQuery`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
    /**
     * Executes a Gremlin query against an Amazon Neptune database using the provided {@link NeptunedataClient}.
     *
     * @param client the {@link NeptunedataClient} instance to use for executing the Gremlin query
     */
    public static void executeGremlinQuery(NeptunedataClient client) {
        try {
            System.out.println("Querying Neptune...");
            ExecuteGremlinQueryRequest request = ExecuteGremlinQueryRequest.builder()
                    .gremlinQuery("g.V().has('code', 'ANC')")
                    .build();

            ExecuteGremlinQueryResponse response = client.executeGremlinQuery(request);

            System.out.println("Full Response:");
            System.out.println(response);

            // Retrieve and print the result
            if (response.result() != null) {
                System.out.println("Query Result:");
                System.out.println(response.result().toString());
            } else {
                System.out.println("No result returned from the query.");
            }
        } catch (NeptunedataException e) {
            System.err.println("Error calling Neptune: " + e.awsErrorDetails().errorMessage());
        } catch (Exception e) {
            System.err.println("Unexpected error: " + e.getMessage());
        } finally {
            client.close();
        }
    }
```
+  For API details, see [ExecuteGremlinProfileQuery](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ExecuteGremlinProfileQuery) in *AWS SDK for Java 2.x API Reference*.

### `ExecuteGremlinQuery`
<a name="neptune_ExecuteGremlinQuery_java_2_topic"></a>

The following code example shows how to use `ExecuteGremlinQuery`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
    /**
     * Executes a Gremlin PROFILE query using the provided NeptunedataClient.
     *
     * @param client The NeptunedataClient instance to be used for executing the Gremlin PROFILE query.
     */
    private static void executeGremlinProfileQuery(NeptunedataClient client) {
        System.out.println("Executing Gremlin PROFILE query...");

        ExecuteGremlinProfileQueryRequest request = ExecuteGremlinProfileQueryRequest.builder()
                .gremlinQuery("g.V().has('code', 'ANC')")
                .build();

        ExecuteGremlinProfileQueryResponse response = client.executeGremlinProfileQuery(request);
        if (response.output() != null) {
            System.out.println("Query Profile Output:");
            System.out.println(response.output());
        } else {
            System.out.println("No output returned from the profile query.");
        }
    }
```
+  For API details, see [ExecuteGremlinQuery](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ExecuteGremlinQuery) in *AWS SDK for Java 2.x API Reference*.

### `ExecuteOpenCypherExplainQuery`
<a name="neptune_ExecuteOpenCypherExplainQuery_java_2_topic"></a>

The following code example shows how to use `ExecuteOpenCypherExplainQuery`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
    /**
     * Executes an OpenCypher EXPLAIN query using the provided Neptune data client.
     *
     * @param client The Neptune data client to use for the query execution.
     */
    public static void executeGremlinQuery(NeptunedataClient client) {
        try {
            System.out.println("Executing OpenCypher EXPLAIN query...");
            ExecuteOpenCypherExplainQueryRequest request = ExecuteOpenCypherExplainQueryRequest.builder()
                    .openCypherQuery("MATCH (n {code: 'ANC'}) RETURN n")
                    .explainMode("debug")
                    .build();

            ExecuteOpenCypherExplainQueryResponse response = client.executeOpenCypherExplainQuery(request);

            if (response.results() != null) {
                System.out.println("Explain Results:");
                System.out.println(response.results().asUtf8String());
            } else {
                System.out.println("No explain results returned.");
            }

        } catch (NeptunedataException e) {
            System.err.println("Neptune error: " + e.awsErrorDetails().errorMessage());
        } catch (Exception e) {
            System.err.println("Unexpected error: " + e.getMessage());
        } finally {
            client.close();
        }
    }
```
+  For API details, see [ExecuteOpenCypherExplainQuery](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ExecuteOpenCypherExplainQuery) in *AWS SDK for Java 2.x API Reference*.

### `ExecuteQuery`
<a name="neptune_ExecuteQuery_java_2_topic"></a>

The following code example shows how to use `ExecuteQuery`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
    /**
     * Executes a Gremlin profile query on the Neptune Analytics graph.
     *
     * @param client       the {@link NeptuneGraphClient} instance to use for the query
     * @param graphId      the identifier of the graph to execute the query on
     *
     * @throws NeptuneGraphException if an error occurs while executing the query on the Neptune Graph
     * @throws Exception if an unexpected error occurs
     */
    public static void executeGremlinProfileQuery(NeptuneGraphClient client, String graphId) {

        try {
            System.out.println("Running openCypher query on Neptune Analytics...");

            ExecuteQueryRequest request = ExecuteQueryRequest.builder()
                    .graphIdentifier(graphId)
                    .queryString("MATCH (n {code: 'ANC'}) RETURN n")
                    .language("OPEN_CYPHER")
                    .build();

            ResponseInputStream<ExecuteQueryResponse> response = client.executeQuery(request);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(response, StandardCharsets.UTF_8))) {
                String result = reader.lines().collect(Collectors.joining("\n"));
                System.out.println("Query Result:");
                System.out.println(result);
            } catch (Exception e) {
                System.err.println("Error reading response: " + e.getMessage());
            }

        } catch (NeptuneGraphException e) {
            System.err.println("NeptuneGraph error: " + e.awsErrorDetails().errorMessage());
        } catch (Exception e) {
            System.err.println("Unexpected error: " + e.getMessage());
        } finally {
            client.close();
        }
    }
```
+  For API details, see [ExecuteQuery](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ExecuteQuery) in *AWS SDK for Java 2.x API Reference*.

### `StartDBCluster`
<a name="neptune_StartDBCluster_java_2_topic"></a>

The following code example shows how to use `StartDBCluster`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
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
```
+  For API details, see [StartDBCluster](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/StartDBCluster) in *AWS SDK for Java 2.x API Reference*.

### `StopDBCluster`
<a name="neptune_StopDBCluster_java_2_topic"></a>

The following code example shows how to use `StopDBCluster`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
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
```
+  For API details, see [StopDBCluster](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/StopDBCluster) in *AWS SDK for Java 2.x API Reference*.

## Scenarios
<a name="scenarios"></a>

### Use the Neptune API to query graph data
<a name="cross_Neptune_Query_java_2_topic"></a>

The following code example shows how to use the Neptune API to query graph data.

**SDK for Java 2.x**
 Shows how to use Amazon Neptune Java API to create a Lambda function that queries graph data within the VPC.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/creating_neptune_lambda).

**Services used in this example**
+ Lambda
+ Neptune
