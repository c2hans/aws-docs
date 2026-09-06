---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/entityresolution_example_entityresolution_Scenario_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Learn the basics of AWS Entity Resolution with an AWS SDK
<a name="entityresolution_example_entityresolution_Scenario_section"></a>

The following code examples show how to:
+ Create Schema Mapping.
+ Create an AWS Entity Resolution workflow.
+ Start the matching job for the workflow.
+ Get details for the matching job.
+ Get Schema Mapping.
+ List all Schema Mappings.
+ Tag the Schema Mapping resource.
+ Delete the AWS Entity Resolution Assets.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/entityresolution#code-examples).
Run an interactive scenario demonstrating AWS Entity Resolution features.

```
public class EntityResScenario {
    private static final Logger logger = LoggerFactory.getLogger(EntityResScenario.class);
    public static final String DASHES = new String(new char[80]).replace("\0", "-");
    private static final String STACK_NAME = "EntityResolutionCdkStack2";
    private static final String ENTITY_RESOLUTION_ROLE_ARN_KEY = "EntityResolutionRoleArn";
    private static final String GLUE_DATA_BUCKET_NAME_KEY = "GlueDataBucketName";
    private static final String JSON_GLUE_TABLE_ARN_KEY = "JsonErGlueTableArn";
    private static final String CSV_GLUE_TABLE_ARN_KEY = "CsvErGlueTableArn";
    private static String glueBucketName;
    private static String workflowName = "workflow-" + UUID.randomUUID();

    private static String jsonSchemaMappingName = "jsonschema-" + UUID.randomUUID();
    private static String jsonSchemaMappingArn = null;
    private static String csvSchemaMappingName = "csv-" + UUID.randomUUID();
    private static String roleARN;
    private static String csvGlueTableArn;
    private static String jsonGlueTableArn;
    private static Scanner scanner = new Scanner(System.in);

    private static EntityResActions actions = new EntityResActions();

    public static void main(String[] args) throws InterruptedException {

        logger.info("Welcome to the AWS Entity Resolution Scenario.");
        logger.info("""
            AWS Entity Resolution is a fully-managed machine learning service provided by
            Amazon Web Services (AWS) that helps organizations extract, link, and
            organize information from multiple data sources. It leverages natural
            language processing and deep learning models to identify and resolve
            entities, such as people, places, organizations, and products,
            across structured and unstructured data.

            With Entity Resolution, customers can build robust data integration
            pipelines to combine and reconcile data from multiple systems, databases,
            and documents. The service can handle ambiguous, incomplete, or conflicting
            information, and provide a unified view of entities and their relationships.
            This can be particularly valuable in applications such as customer 360,
            fraud detection, supply chain management, and knowledge management, where
            accurate entity identification is crucial.

            The `EntityResolutionAsyncClient` interface in the AWS SDK for Java 2.x
            provides a set of methods to programmatically interact with the AWS Entity
            Resolution service. This allows developers to automate the entity extraction,
            linking, and deduplication process as part of their data processing workflows.
            With Entity Resolution, organizations can unlock the value of their data,
            improve decision-making, and enhance customer experiences by having a reliable,
            comprehensive view of their key entities.
            """);

        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("""
            To prepare the AWS resources needed for this scenario application, the next step uploads
            a CloudFormation template whose resulting stack creates the following resources:
            - An AWS Glue Data Catalog table
            - An AWS IAM role
            - An AWS S3 bucket
            - An AWS Entity Resolution Schema

            It can take a couple minutes for the Stack to finish creating the resources.
            """);
        waitForInputToContinue(scanner);
        logger.info("Generating resources...");
        CloudFormationHelper.deployCloudFormationStack(STACK_NAME);
        Map<String, String> outputsMap = CloudFormationHelper.getStackOutputsAsync(STACK_NAME).join();
        roleARN = outputsMap.get(ENTITY_RESOLUTION_ROLE_ARN_KEY);
        glueBucketName = outputsMap.get(GLUE_DATA_BUCKET_NAME_KEY);
        csvGlueTableArn = outputsMap.get(CSV_GLUE_TABLE_ARN_KEY);
        jsonGlueTableArn = outputsMap.get(JSON_GLUE_TABLE_ARN_KEY);
        logger.info(DASHES);
        waitForInputToContinue(scanner);

        try {
            runScenario();

        } catch (Exception ce) {
            Throwable cause = ce.getCause();
            logger.error("An exception happened: " + (cause != null ? cause.getMessage() : ce.getMessage()));
        }
    }

    private static void runScenario() throws InterruptedException {
        /*
         This JSON is a valid input for the AWS Entity Resolution service.
         The JSON represents an array of three objects, each containing an "id", "name", and "email"
         property. This format aligns with the expected input structure for the
         Entity Resolution service.
         */
        String json = """
            {"id":"1","name":"Jane Doe","email":"jane.doe@example.com"}
            {"id":"2","name":"John Doe","email":"john.doe@example.com"}
            {"id":"3","name":"Jorge Souza","email":"jorge_souza@example.com"}
            """;
        logger.info("Upload the following JSON objects to the {} S3 bucket.", glueBucketName);
        logger.info(json);
        String csv = """
            id,name,email,phone
            1,Jane B.,Doe,jane.doe@example.com,555-876-9846
            2,John Doe Jr.,john.doe@example.com,555-654-3210
            3,María García,maría_garcia@company.com,555-567-1234
            4,Mary Major,mary_major@company.com,555-222-3333
            """;
        logger.info("Upload the following CSV data to the {} S3 bucket.", glueBucketName);
        logger.info(csv);
        waitForInputToContinue(scanner);
        try {
            actions.uploadInputData(glueBucketName, json, csv);
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();

            if (cause == null) {
                logger.error("Failed to upload input data: {}", ce.getMessage(), ce);
            }

            if (cause instanceof ResourceNotFoundException) {
                logger.error("Failed to upload input data as the resource was not found: {}", cause.getMessage(), cause);
            }
            return;
        }
        logger.info("The JSON and CSV objects have been uploaded to the S3 bucket.");
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("1. Create Schema Mapping");
        logger.info("""
            Entity Resolution schema mapping aligns and integrates data from
            multiple sources by identifying and matching corresponding entities
            like customers or products. It unifies schemas, resolves conflicts,
            and uses machine learning to link related entities, enabling a
            consolidated, accurate view for improved data quality and decision-making.

            In this example, the schema mapping lines up with the fields in the JSON and CSV objects. That is,
            it contains these fields: id, name, and email.
            """);
        try {
            CreateSchemaMappingResponse response = actions.createSchemaMappingAsync(jsonSchemaMappingName).join();
            jsonSchemaMappingName = response.schemaName();
            logger.info("The JSON schema mapping name is " + jsonSchemaMappingName);
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();

            if (cause == null) {
                logger.error("Failed to create JSON schema mapping: {}", ce.getMessage(), ce);
            }

            if (cause instanceof ConflictException) {
                logger.error("Schema mapping conflict detected: {}", cause.getMessage(), cause);
            } else {
                logger.error("Unexpected error while creating schema mapping: {}", cause.getMessage(), cause);
            }
            return;
        }

        try {
            CreateSchemaMappingResponse response = actions.createSchemaMappingAsync(csvSchemaMappingName).join();
            csvSchemaMappingName = response.schemaName();
            logger.info("The CSV schema mapping name is " + csvSchemaMappingName);
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();
            if (cause == null) {
                logger.error("Failed to create CSV schema mapping: {}", ce.getMessage(), ce);
            }

            if (cause instanceof ConflictException) {
                logger.error("Schema mapping conflict detected: {}", cause.getMessage(), cause);
            } else {
                logger.error("Unexpected error while creating CSV schema mapping: {}", cause.getMessage(), cause);
            }
            return;
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("2. Create an AWS Entity Resolution Workflow. ");
        logger.info("""
            An Entity Resolution matching workflow identifies and links records
            across datasets that represent the same real-world entity, such as
            customers or products. Using techniques like schema mapping,
            data profiling, and machine learning algorithms,
            it evaluates attributes like names or emails to detect duplicates
            or relationships, even with variations or inconsistencies.
            The workflow outputs consolidated, de-duplicated data.

            We will use the machine learning-based matching technique.
            """);
        waitForInputToContinue(scanner);
        try {
            String workflowArn = actions.createMatchingWorkflowAsync(
                roleARN, workflowName, glueBucketName, jsonGlueTableArn,
                jsonSchemaMappingName, csvGlueTableArn, csvSchemaMappingName).join();

            logger.info("The workflow ARN is: " + workflowArn);
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();

            if (cause == null) {
                logger.error("An unexpected error occurred: {}", ce.getMessage(), ce);
            }

            if (cause instanceof ValidationException) {
                logger.error("Validation error: {}", cause.getMessage(), cause);
            } else if (cause instanceof ConflictException) {
                logger.error("Workflow conflict detected: {}", cause.getMessage(), cause);
            } else {
                logger.error("Unexpected error: {}", cause.getMessage(), cause);
            }
            return;
        }

        waitForInputToContinue(scanner);
        logger.info(DASHES);
        logger.info("3. Start the matching job of the " + workflowName + " workflow.");
        waitForInputToContinue(scanner);
        String jobId = null;
        try {
            jobId = actions.startMatchingJobAsync(workflowName).join();
            logger.info("The matching job was successfully started.");
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();
            if (cause instanceof ConflictException) {
                logger.error("Job conflict detected: {}", cause.getMessage(), cause);
            } else {
                logger.error("Unexpected error while starting the job: {}", ce.getMessage(), ce);
            }
            return;
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("4. While the matching job is running, let's look at other API methods. First, let's get details for job " + jobId);
        waitForInputToContinue(scanner);
        try {
            actions.getMatchingJobAsync(jobId, workflowName).join();
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();
            if (cause instanceof ResourceNotFoundException) {
                logger.error("The matching job not found: {}", cause.getMessage(), cause);
            } else {
                logger.error("Failed to start matching job: " + (cause != null ? cause.getMessage() : ce.getMessage()));
            }
            return;
        }
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("5. Get the schema mapping for the JSON data.");
        waitForInputToContinue(scanner);
        try {
            GetSchemaMappingResponse response = actions.getSchemaMappingAsync(jsonSchemaMappingName).join();
            jsonSchemaMappingArn = response.schemaArn();
            logger.info("Schema mapping ARN is " + jsonSchemaMappingArn);
        } catch (CompletionException ce) {
            Throwable cause = ce.getCause();
            if (cause instanceof ResourceNotFoundException) {
                logger.error("Schema mapping not found: {}", cause.getMessage(), cause);
            } else {
                logger.error("Error retrieving the specific schema mapping: " + ce.getCause().getMessage());
            }
            return;
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("6. List Schema Mappings.");
        try {
            actions.ListSchemaMappings();
        } catch (CompletionException ce) {
            logger.error("Error retrieving schema mappings: " + ce.getCause().getMessage());
            return;
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("7. Tag the {} resource.", jsonSchemaMappingName);
        logger.info("""
            Tags can help you organize and categorize your Entity Resolution resources.
            You can also use them to scope user permissions by granting a user permission
            to access or change only resources with certain tag values.
            In Entity Resolution, SchemaMapping and MatchingWorkflow can be tagged. For this example,
            the SchemaMapping is tagged.
                """);
        try {
            actions.tagEntityResource(jsonSchemaMappingArn).join();
        } catch (CompletionException ce) {
            logger.error("Error tagging the resource: " + ce.getCause().getMessage());
            return;
        }

        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("8. View the results of the AWS Entity Resolution Workflow.");
        logger.info("""
            You cannot view the result of the workflow that is in a running state.
            In order to view the results, you need to wait for the workflow that we started in step 3 to complete.

            If you choose not to wait, you cannot view the results. You can perform
            this task manually in the AWS Management Console.

            This can take up to 30 mins (y/n).
            """);
        String viewAns = scanner.nextLine().trim();
        boolean isComplete = false;
        if (viewAns.equalsIgnoreCase("y")) {
            logger.info("You selected to view the Entity Resolution Workflow results.");
            countdownWithWorkflowCheck(actions, 1800, jobId, workflowName);
            isComplete = true;
            try {
                JobMetrics metrics = actions.getJobInfo(workflowName, jobId).join();
                logger.info("Number of input records: {}", metrics.inputRecords());
                logger.info("Number of match ids: {}", metrics.matchIDs());
                logger.info("Number of records not processed: {}", metrics.recordsNotProcessed());
                logger.info("Number of total records processed: {}", metrics.totalRecordsProcessed());
                logger.info("The following represents the output data generated by the Entity Resolution workflow based on the JSON and CSV input data. The output data is stored in the {} bucket.", glueBucketName);
                actions.printData(glueBucketName);

                logger.info("""

                    Note that each of the last 2 records are considered a match even though the 'name' differs between the records;
                    For example 'John Doe Jr.' compared to 'John Doe'.
                    The confidence level is a value between 0 and 1, where 1 indicates a perfect match.

                    """);

            } catch (CompletionException ce) {
                Throwable cause = ce.getCause();
                if (cause instanceof ResourceNotFoundException) {
                    logger.error("The job not found: {}", cause.getMessage(), cause);
                } else {
                    logger.error("Error retrieving job information: " + ce.getCause().getMessage());
                }
                return;
            }
        }

        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("9. Do you want to delete the resources, including the workflow? (y/n)");
        logger.info("""
            You cannot delete the workflow that is in a running state.
            In order to delete the workflow, you need to wait for the workflow to complete.

            You can delete the workflow manually in the AWS Management Console at a later time.

            If you already waited for the workflow to complete in the previous step,
            the workflow is completed and you can delete it.

            If the workflow is not completed, this can take up to 30 mins (y/n).
            """);
        String delAns = scanner.nextLine().trim();
        if (delAns.equalsIgnoreCase("y")) {
            try {
                if (!isComplete) {
                    countdownWithWorkflowCheck(actions, 1800, jobId, workflowName);
                }
                actions.deleteMatchingWorkflowAsync(workflowName).join();
                logger.info("Workflow deleted successfully!");
            } catch (CompletionException ce) {
                logger.info("Error deleting the workflow: {} ", ce.getMessage());
                return;
            }

            try {
                // Delete both schema mappings.
                actions.deleteSchemaMappingAsync(jsonSchemaMappingName).join();
                actions.deleteSchemaMappingAsync(csvSchemaMappingName).join();
                logger.info("Both schema mappings were deleted successfully!");
            } catch (CompletionException ce) {
                logger.error("Error deleting schema mapping: {}", ce.getMessage());
                return;
            }

            waitForInputToContinue(scanner);
            logger.info(DASHES);
            logger.info("""
                Now we delete the CloudFormation stack, which deletes
                the resources that were created at the beginning of this scenario.
                """);
            waitForInputToContinue(scanner);
            logger.info(DASHES);
            try {
                deleteCloudFormationStack();
            } catch (RuntimeException e) {
                logger.error("Failed to delete the stack: {}", e.getMessage());
                return;
            }

        } else {
            logger.info("You can delete the AWS resources in the AWS Management Console.");
        }

        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("This concludes the AWS Entity Resolution scenario.");
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
                // Handle invalid input.
                logger.info("Invalid input. Please try again.");
            }
        }
    }

    public static void countdownWithWorkflowCheck(EntityResActions actions, int totalSeconds, String jobId, String workflowName) throws InterruptedException {
        int secondsElapsed = 0;

        while (true) {
            // Calculate display minutes and seconds.
            int remainingTime = totalSeconds - secondsElapsed;
            int displayMinutes = remainingTime / 60;
            int displaySeconds = remainingTime % 60;

            // Print the countdown.
            System.out.printf("\r%02d:%02d", displayMinutes, displaySeconds);
            Thread.sleep(1000); // Wait for 1 second
            secondsElapsed++;

            // Check workflow status every 60 seconds.
            if (secondsElapsed % 60 == 0 || remainingTime <= 0) {
                GetMatchingJobResponse response = actions.checkWorkflowStatusCompleteAsync(jobId, workflowName).join();
                if (response != null && "SUCCEEDED".equalsIgnoreCase(String.valueOf(response.status()))) {
                    logger.info(""); // Move to the next line after countdown.
                    logger.info("Countdown complete: Workflow is in Completed state!");
                    break; // Break out of the loop if the status is "SUCCEEDED"
                }
            }

            // If countdown reaches zero, reset it for continuous countdown.
            if (remainingTime <= 0) {
                secondsElapsed = 0;
            }
        }
    }

    private static void deleteCloudFormationStack() {
        try {
            CloudFormationHelper.emptyS3Bucket(glueBucketName);
            CloudFormationHelper.destroyCloudFormationStack(STACK_NAME);
            logger.info("Resources deleted successfully!");
        } catch (CloudFormationException e) {
            throw new RuntimeException("Failed to delete CloudFormation stack: " + e.getMessage(), e);
        } catch (S3Exception e) {
            throw new RuntimeException("Failed to empty S3 bucket: " + e.getMessage(), e);
        }
    }
}
```
A wrapper class for AWS Entity Resolution SDK methods.

```
public class EntityResActions {

    private static final String PREFIX = "eroutput/";
    private static final Logger logger = LoggerFactory.getLogger(EntityResActions.class);

    private static EntityResolutionAsyncClient entityResolutionAsyncClient;

    private static S3AsyncClient s3AsyncClient;

    public static EntityResolutionAsyncClient getResolutionAsyncClient() {
        if (entityResolutionAsyncClient == null) {
            /*
            The `NettyNioAsyncHttpClient` class is part of the AWS SDK for Java, version 2,
            and it is designed to provide a high-performance, asynchronous HTTP client for interacting with AWS services.
             It uses the Netty framework to handle the underlying network communication and the Java NIO API to
             provide a non-blocking, event-driven approach to HTTP requests and responses.
             */

            SdkAsyncHttpClient httpClient = NettyNioAsyncHttpClient.builder()
                .maxConcurrency(50)  // Adjust as needed.
                .connectionTimeout(Duration.ofSeconds(60))  // Set the connection timeout.
                .readTimeout(Duration.ofSeconds(60))  // Set the read timeout.
                .writeTimeout(Duration.ofSeconds(60))  // Set the write timeout.
                .build();

            ClientOverrideConfiguration overrideConfig = ClientOverrideConfiguration.builder()
                .apiCallTimeout(Duration.ofMinutes(2))  // Set the overall API call timeout.
                .apiCallAttemptTimeout(Duration.ofSeconds(90))  // Set the individual call attempt timeout.
                .retryStrategy(RetryMode.STANDARD)
                .build();

            entityResolutionAsyncClient = EntityResolutionAsyncClient.builder()
                .httpClient(httpClient)
                .overrideConfiguration(overrideConfig)
                .build();
        }
        return entityResolutionAsyncClient;
    }

    public static S3AsyncClient getS3AsyncClient() {
        if (s3AsyncClient == null) {
            /*
            The `NettyNioAsyncHttpClient` class is part of the AWS SDK for Java, version 2,
            and it is designed to provide a high-performance, asynchronous HTTP client for interacting with AWS services.
             It uses the Netty framework to handle the underlying network communication and the Java NIO API to
             provide a non-blocking, event-driven approach to HTTP requests and responses.
             */

            SdkAsyncHttpClient httpClient = NettyNioAsyncHttpClient.builder()
                .maxConcurrency(50)  // Adjust as needed.
                .connectionTimeout(Duration.ofSeconds(60))  // Set the connection timeout.
                .readTimeout(Duration.ofSeconds(60))  // Set the read timeout.
                .writeTimeout(Duration.ofSeconds(60))  // Set the write timeout.
                .build();

            ClientOverrideConfiguration overrideConfig = ClientOverrideConfiguration.builder()
                .apiCallTimeout(Duration.ofMinutes(2))  // Set the overall API call timeout.
                .apiCallAttemptTimeout(Duration.ofSeconds(90))  // Set the individual call attempt timeout.
                .retryStrategy(RetryMode.STANDARD)
                .build();

            s3AsyncClient = S3AsyncClient.builder()
                .httpClient(httpClient)
                .overrideConfiguration(overrideConfig)
                .build();
        }
        return s3AsyncClient;
    }

    /**
     * Deletes the schema mapping asynchronously.
     *
     * @param schemaName the name of the schema to delete
     * @return a {@link CompletableFuture} that completes when the schema mapping is deleted successfully,
     * or throws a {@link RuntimeException} if the deletion fails
     */
    public CompletableFuture<DeleteSchemaMappingResponse> deleteSchemaMappingAsync(String schemaName) {
        DeleteSchemaMappingRequest request = DeleteSchemaMappingRequest.builder()
            .schemaName(schemaName)
            .build();

        return getResolutionAsyncClient().deleteSchemaMapping(request)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    // Successfully deleted the schema mapping, log the success message.
                    logger.info("Schema mapping '{}' deleted successfully.", schemaName);
                } else {
                    // Ensure exception is not null before accessing its cause.
                    if (exception == null) {
                        throw new CompletionException("An unknown error occurred while deleting the schema mapping.", null);
                    }

                    Throwable cause = exception.getCause();
                    if (cause instanceof ResourceNotFoundException) {
                        throw new CompletionException("The schema mapping was not found to delete: " + schemaName, cause);
                    }

                    // Wrap other AWS exceptions in a CompletionException.
                    throw new CompletionException("Failed to delete schema mapping: " + schemaName, exception);
                }
            });
    }

    /**
     * Lists the schema mappings associated with the current AWS account. This method uses an asynchronous paginator to
     * retrieve the schema mappings, and prints the name of each schema mapping to the console.
     */
    public void ListSchemaMappings() {
        ListSchemaMappingsRequest mappingsRequest = ListSchemaMappingsRequest.builder()
            .build();

        ListSchemaMappingsPublisher paginator = getResolutionAsyncClient().listSchemaMappingsPaginator(mappingsRequest);

        // Iterate through the pages of results
        CompletableFuture<Void> future = paginator.subscribe(response -> {
            response.schemaList().forEach(schemaMapping ->
                logger.info("Schema Mapping Name: " + schemaMapping.schemaName())
            );
        });

        // Wait for the asynchronous operation to complete
        future.join();
    }

    /**
     * Asynchronously deletes a workflow with the specified name.
     *
     * @param workflowName the name of the workflow to be deleted
     * @return a {@link CompletableFuture} that completes when the workflow has been deleted
     * @throws RuntimeException if the deletion of the workflow fails
     */
    public CompletableFuture<DeleteMatchingWorkflowResponse> deleteMatchingWorkflowAsync(String workflowName) {
        DeleteMatchingWorkflowRequest request = DeleteMatchingWorkflowRequest.builder()
            .workflowName(workflowName)
            .build();

        return getResolutionAsyncClient().deleteMatchingWorkflow(request)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    logger.info("{} was deleted", workflowName );
                } else {
                    if (exception == null) {
                        throw new CompletionException("An unknown error occurred while deleting the workflow.", null);
                    }

                    Throwable cause = exception.getCause();
                    if (cause instanceof ResourceNotFoundException) {
                        throw new CompletionException("The workflow to delete was not found.", cause);
                    }

                    // Wrap other AWS exceptions in a CompletionException.
                    throw new CompletionException("Failed to delete workflow: " + exception.getMessage(), exception);
                }
            });
    }

    /**
     * Creates a schema mapping asynchronously.
     *
     * @param schemaName the name of the schema to create
     * @return a {@link CompletableFuture} that represents the asynchronous creation of the schema mapping
     */
    public CompletableFuture<CreateSchemaMappingResponse> createSchemaMappingAsync(String schemaName) {
        List<SchemaInputAttribute> schemaAttributes = null;
        if (schemaName.startsWith("json")) {
            schemaAttributes = List.of(
                SchemaInputAttribute.builder().matchKey("id").fieldName("id").type(SchemaAttributeType.UNIQUE_ID).build(),
                SchemaInputAttribute.builder().matchKey("name").fieldName("name").type(SchemaAttributeType.NAME).build(),
                SchemaInputAttribute.builder().matchKey("email").fieldName("email").type(SchemaAttributeType.EMAIL_ADDRESS).build()
            );
        } else {
            schemaAttributes = List.of(
                SchemaInputAttribute.builder().matchKey("id").fieldName("id").type(SchemaAttributeType.UNIQUE_ID).build(),
                SchemaInputAttribute.builder().matchKey("name").fieldName("name").type(SchemaAttributeType.NAME).build(),
                SchemaInputAttribute.builder().matchKey("email").fieldName("email").type(SchemaAttributeType.EMAIL_ADDRESS).build(),
                SchemaInputAttribute.builder().fieldName("phone").type(SchemaAttributeType.PROVIDER_ID).subType("STRING").build()
            );
        }

        CreateSchemaMappingRequest request = CreateSchemaMappingRequest.builder()
            .schemaName(schemaName)
            .mappedInputFields(schemaAttributes)
            .build();

        return getResolutionAsyncClient().createSchemaMapping(request)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    logger.info("[{}] schema mapping Created Successfully!", schemaName);
                } else {
                    if (exception == null) {
                        throw new CompletionException("An unknown error occurred while creating the schema mapping.", null);
                    }

                    Throwable cause = exception.getCause();
                    if (cause instanceof ConflictException) {
                        throw new CompletionException("A conflicting schema mapping already exists. Resolve conflicts before proceeding.", cause);
                    }

                    // Wrap other AWS exceptions in a CompletionException.
                    throw new CompletionException("Failed to create schema mapping: " + exception.getMessage(), exception);
                }
            });
    }

    /**
     * Retrieves the schema mapping asynchronously.
     *
     * @param schemaName the name of the schema to retrieve the mapping for
     * @return a {@link CompletableFuture} that completes with the {@link GetSchemaMappingResponse} when the operation
     * is complete
     * @throws RuntimeException if the schema mapping retrieval fails
     */
    public CompletableFuture<GetSchemaMappingResponse> getSchemaMappingAsync(String schemaName) {
        GetSchemaMappingRequest mappingRequest = GetSchemaMappingRequest.builder()
            .schemaName(schemaName)
            .build();

        return getResolutionAsyncClient().getSchemaMapping(mappingRequest)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    response.mappedInputFields().forEach(attribute ->
                        logger.info("Attribute Name: " + attribute.fieldName() +
                            ", Attribute Type: " + attribute.type().toString()));
                } else {
                    if (exception == null) {
                        throw new CompletionException("An unknown error occurred while getting schema mapping.", null);
                    }

                    Throwable cause = exception.getCause();
                    if (cause instanceof ResourceNotFoundException) {
                        throw new CompletionException("The requested schema mapping was not found.", cause);
                    }

                    // Wrap other exceptions in a CompletionException with the message.
                    throw new CompletionException("Failed to get schema mapping: " + exception.getMessage(), exception);
                }
            });
    }

    /**
     * Asynchronously retrieves a matching job based on the provided job ID and workflow name.
     *
     * @param jobId        the ID of the job to retrieve
     * @param workflowName the name of the workflow associated with the job
     * @return a {@link CompletableFuture} that completes when the job information is available or an exception occurs
     */
    public CompletableFuture<GetMatchingJobResponse> getMatchingJobAsync(String jobId, String workflowName) {
        GetMatchingJobRequest request = GetMatchingJobRequest.builder()
            .jobId(jobId)
            .workflowName(workflowName)
            .build();

        return getResolutionAsyncClient().getMatchingJob(request)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    // Successfully fetched the matching job details, log the job status.
                    logger.info("Job status: " + response.status());
                    logger.info("Job details: " + response.toString());
                } else {
                    if (exception == null) {
                        throw new CompletionException("An unknown error occurred while fetching the matching job.", null);
                    }

                    Throwable cause = exception.getCause();
                    if (cause instanceof ResourceNotFoundException) {
                        throw new CompletionException("The requested job could not be found.", cause);
                    }

                    // Wrap other exceptions in a CompletionException with the message.
                    throw new CompletionException("Error fetching matching job: " + exception.getMessage(), exception);
                }
            });
    }

    /**
     * Starts a matching job asynchronously for the specified workflow name.
     *
     * @param workflowName the name of the workflow for which to start the matching job
     * @return a {@link CompletableFuture} that completes with the job ID of the started matching job, or an empty
     * string if the operation fails
     */
    public CompletableFuture<String> startMatchingJobAsync(String workflowName) {
        StartMatchingJobRequest jobRequest = StartMatchingJobRequest.builder()
            .workflowName(workflowName)
            .build();

        return getResolutionAsyncClient().startMatchingJob(jobRequest)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    String jobId = response.jobId();
                    logger.info("Job ID: " + jobId);
                } else {
                    if (exception == null) {
                        throw new CompletionException("An unknown error occurred while starting the job.", null);
                    }

                    Throwable cause = exception.getCause();
                    if (cause instanceof ConflictException) {
                        throw new CompletionException("The job is already running. Resolve conflicts before starting a new job.", cause);
                    }

                    // Wrap other AWS exceptions in a CompletionException.
                    throw new CompletionException("Failed to start the job: " + exception.getMessage(), exception);
                }
            })
            .thenApply(response -> response != null ? response.jobId() : "");
    }

    /**
     * Checks the status of a workflow asynchronously.
     *
     * @param jobId        the ID of the job to check
     * @param workflowName the name of the workflow to check
     * @return a CompletableFuture that resolves to a boolean value indicating whether the workflow has completed
     * successfully
     */
    public CompletableFuture<GetMatchingJobResponse> checkWorkflowStatusCompleteAsync(String jobId, String workflowName) {
        GetMatchingJobRequest request = GetMatchingJobRequest.builder()
            .jobId(jobId)
            .workflowName(workflowName)
            .build();

        return getResolutionAsyncClient().getMatchingJob(request)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    // Process the response and log the job status.
                    logger.info("Job status: " + response.status());
                } else {
                    // Ensure exception is not null before accessing its cause.
                    if (exception == null) {
                        throw new CompletionException("An unknown error occurred while checking job status.", null);
                    }

                    Throwable cause = exception.getCause();
                    if (cause instanceof ResourceNotFoundException) {
                        throw new CompletionException("The requested resource was not found while checking the job status.", cause);
                    }

                    // Wrap other AWS exceptions in a CompletionException.
                    throw new CompletionException("Failed to check job status: " + exception.getMessage(), exception);
                }
            });
    }

    /**
     * Creates an asynchronous CompletableFuture to manage the creation of a matching workflow.
     *
     * @param roleARN                 the AWS IAM role ARN to be used for the workflow execution
     * @param workflowName            the name of the workflow to be created
     * @param outputBucket            the S3 bucket path where the workflow output will be stored
     * @param jsonGlueTableArn        the ARN of the Glue Data Catalog table to be used as the input source
     * @param jsonErSchemaMappingName the name of the schema to be used for the input source
     * @return a CompletableFuture that, when completed, will return the ARN of the created workflow
     */
    public CompletableFuture<String> createMatchingWorkflowAsync(
        String roleARN
        , String workflowName
        , String outputBucket
        , String jsonGlueTableArn
        , String jsonErSchemaMappingName
        , String csvGlueTableArn
        , String csvErSchemaMappingName) {

        InputSource jsonInputSource = InputSource.builder()
            .inputSourceARN(jsonGlueTableArn)
            .schemaName(jsonErSchemaMappingName)
            .applyNormalization(false)
            .build();

        InputSource csvInputSource = InputSource.builder()
            .inputSourceARN(csvGlueTableArn)
            .schemaName(csvErSchemaMappingName)
            .applyNormalization(false)
            .build();

        OutputAttribute idOutputAttribute = OutputAttribute.builder()
            .name("id")
            .build();

        OutputAttribute nameOutputAttribute = OutputAttribute.builder()
            .name("name")
            .build();

        OutputAttribute emailOutputAttribute = OutputAttribute.builder()
            .name("email")
            .build();

        OutputAttribute phoneOutputAttribute = OutputAttribute.builder()
            .name("phone")
            .build();

        OutputSource outputSource = OutputSource.builder()
            .outputS3Path("s3://" + outputBucket + "/eroutput")
            .output(idOutputAttribute, nameOutputAttribute, emailOutputAttribute, phoneOutputAttribute)
            .applyNormalization(false)
            .build();

        ResolutionTechniques resolutionType = ResolutionTechniques.builder()
            .resolutionType(ResolutionType.ML_MATCHING)
            .build();

        CreateMatchingWorkflowRequest workflowRequest = CreateMatchingWorkflowRequest.builder()
            .roleArn(roleARN)
            .description("Created by using the AWS SDK for Java")
            .workflowName(workflowName)
            .inputSourceConfig(List.of(jsonInputSource, csvInputSource))
            .outputSourceConfig(List.of(outputSource))
            .resolutionTechniques(resolutionType)
            .build();

        return getResolutionAsyncClient().createMatchingWorkflow(workflowRequest)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    logger.info("Workflow created successfully.");
                } else {
                    Throwable cause = exception.getCause();
                    if (cause instanceof ValidationException) {
                        throw new CompletionException("Invalid request: Please check input parameters.", cause);
                    }

                    if (cause instanceof ConflictException) {
                        throw new CompletionException("A conflicting workflow already exists. Resolve conflicts before proceeding.", cause);
                    }
                    throw new CompletionException("Failed to create workflow: " + exception.getMessage(), exception);
                }
            })
            .thenApply(CreateMatchingWorkflowResponse::workflowArn);
    }

    /**
     * Tags the specified schema mapping ARN.
     *
     * @param schemaMappingARN the ARN of the schema mapping to tag
     */
    public CompletableFuture<TagResourceResponse> tagEntityResource(String schemaMappingARN) {
        Map<String, String> tags = new HashMap<>();
        tags.put("tag1", "tag1Value");
        tags.put("tag2", "tag2Value");

        TagResourceRequest request = TagResourceRequest.builder()
            .resourceArn(schemaMappingARN)
            .tags(tags)
            .build();

        return getResolutionAsyncClient().tagResource(request)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    // Successfully tagged the resource, log the success message.
                    logger.info("Successfully tagged the resource.");
                } else {
                    if (exception == null) {
                        throw new CompletionException("An unknown error occurred while tagging the resource.", null);
                    }

                    Throwable cause = exception.getCause();
                    if (cause instanceof ResourceNotFoundException) {
                        throw new CompletionException("The resource to tag was not found.", cause);
                    }
                    throw new CompletionException("Failed to tag the resource: " + exception.getMessage(), exception);
                }
            });
    }

    public CompletableFuture<JobMetrics> getJobInfo(String workflowName, String jobId) {
        return getResolutionAsyncClient().getMatchingJob(b -> b
                .workflowName(workflowName)
                .jobId(jobId))
            .whenComplete((response, exception) -> {
                if (response != null) {
                    logger.info("Job metrics fetched successfully for jobId: " + jobId);
                } else {
                    Throwable cause = exception.getCause();
                    if (cause instanceof ResourceNotFoundException) {
                        throw new CompletionException("Invalid request: Job id was not found.", cause);
                    }
                    throw new CompletionException("Failed to fetch job info: " + exception.getMessage(), exception);
                }
            })
            .thenApply(response -> response.metrics()); // Extract job metrics
    }

    /**
     * Uploads data to an Amazon S3 bucket asynchronously.
     *
     * @param bucketName the name of the S3 bucket to upload the data to
     * @param jsonData   the JSON data to be uploaded
     * @param csvData    the CSV data to be uploaded
     * @return a {@link CompletableFuture} representing both asynchronous operation of uploading the data
     * @throws RuntimeException if an error occurs during the file upload
     */

    public void uploadInputData(String bucketName, String jsonData, String csvData) {
        // Upload JSON data.
        String jsonKey = "jsonData/data.json";
        PutObjectRequest jsonUploadRequest = PutObjectRequest.builder()
            .bucket(bucketName)
            .key(jsonKey)
            .contentType("application/json")
            .build();

        CompletableFuture<PutObjectResponse> jsonUploadResponse = getS3AsyncClient().putObject(jsonUploadRequest, AsyncRequestBody.fromString(jsonData));

        // Upload CSV data.
        String csvKey = "csvData/data.csv";
        PutObjectRequest csvUploadRequest = PutObjectRequest.builder()
            .bucket(bucketName)
            .key(csvKey)
            .contentType("text/csv")
            .build();
        CompletableFuture<PutObjectResponse> csvUploadResponse = getS3AsyncClient().putObject(csvUploadRequest, AsyncRequestBody.fromString(csvData));

        CompletableFuture.allOf(jsonUploadResponse, csvUploadResponse)
            .whenComplete((result, ex) -> {
                if (ex != null) {
                    // Wrap an AWS exception.
                    throw new CompletionException("Failed to upload files", ex);
                }
            }).join();

    }

    /**
     * Finds the latest file in the S3 bucket that starts with "run-" in any depth of subfolders
     */
    private CompletableFuture<String> findLatestMatchingFile(String bucketName) {
        ListObjectsV2Request request = ListObjectsV2Request.builder()
            .bucket(bucketName)
            .prefix(PREFIX) // Searches within the given folder
            .build();

        return getS3AsyncClient().listObjectsV2(request)
            .thenApply(response -> response.contents().stream()
                .map(S3Object::key)
                .filter(key -> key.matches(".*?/run-[0-9a-zA-Z\\-]+")) // Matches files like run-XXXXX in any subfolder
                .max(String::compareTo) // Gets the latest file
                .orElse(null))
            .whenComplete((result, exception) -> {
                if (exception == null) {
                    if (result != null) {
                        logger.info("Latest matching file found: " + result);
                    } else {
                        logger.info("No matching files found.");
                    }
                } else {
                    throw new CompletionException("Failed to find latest matching file: " + exception.getMessage(), exception);
                }
            });
    }

    /**
     * Prints the data located in the file in the S3 bucket that starts with "run-" in any depth of subfolders
     */
    public void printData(String bucketName) {
        try {
            // Find the latest file with "run-" prefix in any depth of subfolders.
            String s3Key = findLatestMatchingFile(bucketName).join();
            if (s3Key == null) {
                logger.error("No matching files found in S3.");
                return;
            }

            logger.info("Downloading file: " + s3Key);

            // Read CSV file as String.
            String csvContent = readCSVFromS3Async(bucketName, s3Key).join();
            if (csvContent.isEmpty()) {
                logger.error("File is empty.");
                return;
            }

            // Process CSV content.
            List<String[]> records = parseCSV(csvContent);
            printTable(records);

        } catch (RuntimeException | IOException | CsvException e) {
            logger.error("Error processing CSV file from S3: " + e.getMessage());
            e.printStackTrace();
        }
    }

    /**
     * Reads a CSV file from S3 and returns it as a String.
     */
    private static CompletableFuture<String> readCSVFromS3Async(String bucketName, String s3Key) {
        GetObjectRequest getObjectRequest = GetObjectRequest.builder()
            .bucket(bucketName)
            .key(s3Key)
            .build();

        // Initiating the asynchronous request to get the file as bytes
        return getS3AsyncClient().getObject(getObjectRequest, AsyncResponseTransformer.toBytes())
            .thenApply(responseBytes -> responseBytes.asUtf8String()) // Convert bytes to UTF-8 string
            .whenComplete((result, exception) -> {
                if (exception != null) {
                    throw new CompletionException("Failed to read CSV from S3: " + exception.getMessage(), exception);
                } else {
                    logger.info("Successfully fetched CSV file content from S3.");
                }
            });
    }

    /**
     * Parses CSV content from a String into a list of records.
     */
    private static List<String[]> parseCSV(String csvContent) throws IOException, CsvException {
        try (CSVReader csvReader = new CSVReader(new StringReader(csvContent))) {
            return csvReader.readAll();
        }
    }

    /**
     * Prints the given CSV data in a formatted table
     */
    private static void printTable(List<String[]> records) {
        if (records.isEmpty()) {
            System.out.println("No records found.");
            return;
        }

        String[] headers = records.get(0);
        List<String[]> rows = records.subList(1, records.size());

        // Determine column widths dynamically based on longest content
        int[] columnWidths = new int[headers.length];
        for (int i = 0; i < headers.length; i++) {
            final int columnIndex = i;
            int maxWidth = Math.max(headers[i].length(), rows.stream()
                .map(row -> row.length > columnIndex ? row[columnIndex].length() : 0)
                .max(Integer::compareTo)
                .orElse(0));
            columnWidths[i] = Math.min(maxWidth, 25); // Limit max width for better readability
        }

        // Enable ANSI Console for colored output
        AnsiConsole.systemInstall();

        // Print table header
        System.out.println(ansi().fgYellow().a("=== CSV Data from S3 ===").reset());
        printRow(headers, columnWidths, true);

        // Print rows
        rows.forEach(row -> printRow(row, columnWidths, false));

        // Restore console to normal
        AnsiConsole.systemUninstall();
    }

    private static void printRow(String[] row, int[] columnWidths, boolean isHeader) {
        String border = IntStream.range(0, columnWidths.length)
            .mapToObj(i -> "-".repeat(columnWidths[i] + 2))
            .collect(Collectors.joining("+", "+", "+"));

        if (isHeader) {
            System.out.println(border);
        }

        System.out.print("|");
        for (int i = 0; i < columnWidths.length; i++) {
            String cell = (i < row.length && row[i] != null) ? row[i] : "";
            System.out.printf(" %-" + columnWidths[i] + "s |", isHeader ? ansi().fgBrightBlue().a(cell).reset() : cell);
        }
        System.out.println();

        if (isHeader) {
            System.out.println(border);
        }
    }
}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [CreateMatchingWorkflow](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/CreateMatchingWorkflow)
  + [CreateSchemaMapping](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/CreateSchemaMapping)
  + [DeleteMatchingWorkflow](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/DeleteMatchingWorkflow)
  + [DeleteSchemaMapping](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/DeleteSchemaMapping)
  + [GetMatchingJob](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/GetMatchingJob)
  + [GetSchemaMapping](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/GetSchemaMapping)
  + [ListMatchingWorkflows](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/ListMatchingWorkflows)
  + [ListSchemaMappings](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/ListSchemaMappings)
  + [StartMatchingJob](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/StartMatchingJob)
  + [TagResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/TagResource)

------
#### [ JavaScript ]

**SDK for JavaScript (v2)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/entityresolution#code-examples).
Run an interactive scenario demonstrating AWS Entity Resolution features.

```
import {
  Scenario,
  ScenarioAction,
  ScenarioInput,
  ScenarioOutput,
} from "@aws-doc-sdk-examples/lib/scenario/index.js";
import {
  CloudFormationClient,
  CreateStackCommand,
  DeleteStackCommand,
  DescribeStacksCommand,
  waitUntilStackExists,
  waitUntilStackCreateComplete,
} from "@aws-sdk/client-cloudformation";
import {
  EntityResolutionClient,
  CreateSchemaMappingCommand,
  CreateMatchingWorkflowCommand,
  GetMatchingJobCommand,
  StartMatchingJobCommand,
  GetSchemaMappingCommand,
  ListSchemaMappingsCommand,
  TagResourceCommand,
  DeleteMatchingWorkflowCommand,
  DeleteSchemaMappingCommand,
  ConflictException,
  ValidationException,
} from "@aws-sdk/client-entityresolution";
import {
  DeleteObjectsCommand,
  DeleteBucketCommand,
  PutObjectCommand,
  S3Client,
  ListObjectsCommand,
} from "@aws-sdk/client-s3";
import { wait } from "@aws-doc-sdk-examples/lib/utils/util-timers.js";

import { readFile } from "node:fs/promises";
import { parseArgs } from "node:util";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname } from "node:path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const stackName = `${data.inputs.entityResolutionStack}`;

/*The inputs for this example can be edited in the ../input.json.*/
import data from "../inputs.json" with { type: "json" };
const skipWhenErrors = (state) => state.errors.length > 0;
/**
 * Used repeatedly to have the user press enter.
 * @type {ScenarioInput}
 */
/* v8 ignore next 3 */
const pressEnter = new ScenarioInput("continue", "Press Enter to continue", {
  type: "input",
  verbose: "false",
  skipWhen: skipWhenErrors,
});

const region = "eu-west-1";

const entityResolutionClient = new EntityResolutionClient({ region: region });
const cloudFormationClient = new CloudFormationClient({ region: region });
const s3Client = new S3Client({ region: region });

const greet = new ScenarioOutput(
  "greet",
  "AWS Entity Resolution is a fully-managed machine learning service provided by " +
    "Amazon Web Services (AWS) that helps organizations extract, link, and " +
    "organize information from multiple data sources. It leverages natural " +
    "language processing and deep learning models to identify and resolve " +
    "entities, such as people, places, organizations, and products, " +
    "across structured and unstructured data.\n" +
    "\n" +
    "With Entity Resolution, customers can build robust data integration " +
    "pipelines to combine and reconcile data from multiple systems, databases, " +
    "and documents. The service can handle ambiguous, incomplete, or conflicting " +
    "information, and provide a unified view of entities and their relationships. " +
    "This can be particularly valuable in applications such as customer 360, " +
    "fraud detection, supply chain management, and knowledge management, where " +
    "accurate entity identification is crucial.\n" +
    "\n" +
    "The `EntityResolutionAsyncClient` interface in the AWS SDK for Java 2.x " +
    "provides a set of methods to programmatically interact with the AWS Entity " +
    "Resolution service. This allows developers to automate the entity extraction, " +
    "linking, and deduplication process as part of their data processing workflows. " +
    "With Entity Resolution, organizations can unlock the value of their data, " +
    "improve decision-making, and enhance customer experiences by having a reliable, " +
    "comprehensive view of their key entities.",

  { header: true },
);
const displayBuildCloudFormationStack = new ScenarioOutput(
  "displayBuildCloudFormationStack",
  "To prepare the AWS resources needed for this scenario application, the next step uploads " +
    "a CloudFormation template whose resulting stack creates the following resources:\n" +
    "- An AWS Glue Data Catalog table \n" +
    "- An AWS IAM role \n" +
    "- An AWS S3 bucket \n" +
    "- An AWS Entity Resolution Schema \n" +
    "It can take a couple minutes for the Stack to finish creating the resources.",
);

const sdkBuildCloudFormationStack = new ScenarioAction(
  "sdkBuildCloudFormationStack",
  async (/** @type {State} */ state) => {
    try {
      const data = readFileSync(
        `${__dirname}/../../../../resources/cfn/entity-resolution-basics/entity-resolution-basics-template.yml`,
        "utf8",
      );
      await cloudFormationClient.send(
        new CreateStackCommand({
          StackName: stackName,
          TemplateBody: data,
          Capabilities: ["CAPABILITY_IAM"],
        }),
      );
      await waitUntilStackExists(
        { client: cloudFormationClient },
        { StackName: stackName },
      );
      await waitUntilStackCreateComplete(
        { client: cloudFormationClient },
        { StackName: stackName },
      );
      const stack = await cloudFormationClient.send(
        new DescribeStacksCommand({
          StackName: stackName,
        }),
      );

      state.entityResolutionRole = stack.Stacks[0].Outputs[1];
      state.jsonGlueTable = stack.Stacks[0].Outputs[2];
      state.CSVGlueTable = stack.Stacks[0].Outputs[3];
      state.glueDataBucket = stack.Stacks[0].Outputs[0];
      state.stackName = stack.StackName;
      console.log(state.glueDataBucket);
      console.log(
        `The  ARN of the EntityResolution Role is ${state.entityResolutionRole.OutputValue}`,
      );
      console.log(
        `The ARN of the Json Glue Table is ${state.jsonGlueTable.OutputValue}`,
      );
      console.log(
        `The ARN of the CSV Glue Table is ${state.CSVGlueTable.OutputValue}`,
      );
      console.log(
        `The name of the Glue Data Bucket is ${state.glueDataBucket.OutputValue}\n`,
      );
    } catch (caught) {
      console.error(caught.message);
      throw caught;
    }
    try {
      console.log(
        `Uploading the following JSON in ../data.json to the ${state.glueDataBucket.OutputValue} S3 bucket...`,
      );
      const bucketName = state.glueDataBucket.OutputValue;

      const putObjectParams = {
        Bucket: bucketName,
        Key: "jsonData/data.json",
        Body: await readFileSync(
          `${__dirname}/../../../../javascriptv3/example_code/entityresolution/data.json`,
        ),
      };
      const command = new PutObjectCommand(putObjectParams);
      const response = await s3Client.send(command);
      console.log(
        `../data.json file data uploaded to the ${state.glueDataBucket.OutputValue} S3 bucket.\n`,
      );
    } catch (caught) {
      console.error(caught.message);
      throw caught;
    }
    try {
      console.log(
        `Uploading the CSV data in ../data.csv to the ${state.glueDataBucket.OutputValue} S3 bucket...`,
      );

      const bucketName = state.glueDataBucket.OutputValue;
      const putObjectParams = {
        Bucket: bucketName,
        Key: "csvData/data.csv",
        Body: await readFileSync(
          `${__dirname}/../../../../javascriptv3/example_code/entityresolution/data.csv`,
        ),
      };
      const command = new PutObjectCommand(putObjectParams);
      const response = await s3Client.send(command);
      console.log(
        `../data.csv file data uploaded to the ${state.glueDataBucket.OutputValue} S3 bucket.`,
      );
    } catch (caught) {
      console.error(caught.message);
      throw caught;
    }
  },
);

const displayCreateSchemaMapping = new ScenarioOutput(
  "displayCreateSchemaMapping",
  "1. Create Schema Mapping" +
    "Entity Resolution schema mapping aligns and integrates data from " +
    "multiple sources by identifying and matching corresponding entities " +
    "like customers or products. It unifies schemas, resolves conflicts, " +
    "and uses machine learning to link related entities, enabling a " +
    "consolidated, accurate view for improved data quality and decision-making." +
    "\n" +
    "In this example, the schema mapping lines up with the fields in the JSON and CSV objects. That is, " +
    " it contains these fields: id, name, and email. ",
);

const sdkCreateSchemaMapping = new ScenarioAction(
  "sdkCreateSchemaMapping",
  async (/** @type {State} */ state) => {
    const createSchemaMappingParamsJson = {
      schemaName: `${data.inputs.schemaNameJson}`,
      mappedInputFields: [
        {
          fieldName: "id",
          type: "UNIQUE_ID",
        },
        {
          fieldName: "name",
          type: "NAME",
        },
        {
          fieldName: "email",
          type: "EMAIL_ADDRESS",
        },
      ],
    };
    const createSchemaMappingParamsCSV = {
      schemaName: `${data.inputs.schemaNameCSV}`,
      mappedInputFields: [
        {
          fieldName: "id",
          type: "UNIQUE_ID",
        },
        {
          fieldName: "name",
          type: "NAME",
        },
        {
          fieldName: "email",
          type: "EMAIL_ADDRESS",
        },
        {
          fieldName: "phone",
          type: "PROVIDER_ID",
          subType: "STRING",
        },
      ],
    };
    try {
      const command = new CreateSchemaMappingCommand(
        createSchemaMappingParamsJson,
      );
      const response = await entityResolutionClient.send(command);
      state.schemaNameJson = response.schemaName;
      state.schemaArn = response.schemaArn;
      state.idOutputAttribute = response.mappedInputFields[0].fieldName;
      state.nameOutputAttribute = response.mappedInputFields[1].fieldName;
      state.emailOutputAttribute = response.mappedInputFields[2].fieldName;

      console.log("The JSON schema mapping name is ", state.schemaNameJson);
    } catch (caught) {
      if (caught instanceof ConflictException) {
        console.error(
          `The schema mapping already exists: ${caught.message} \n Exiting program.`,
        );
        return;
      }
    }
    try {
      const command = new CreateSchemaMappingCommand(
        createSchemaMappingParamsCSV,
      );
      const response = await entityResolutionClient.send(command);
      state.schemaNameCSV = response.schemaName;
      state.phoneOutputAttribute = response.mappedInputFields[3].fieldName;
      console.log("The CSV schema mapping name is ", state.schemaNameCSV);
    } catch (caught) {
      if (caught instanceof ConflictException) {
        console.error(
          `An unexpected error occurred while creating the geofence collection: ${caught.message} \n Exiting program.`,
        );
        return;
      }
    }
  },
);
const displayCreateMatchingWorkflow = new ScenarioOutput(
  "displayCreateMatchingWorkflow",
  "2. Create an AWS Entity Resolution Workflow. " +
    "An Entity Resolution matching workflow identifies and links records " +
    "across datasets that represent the same real-world entity, such as " +
    "customers or products. Using techniques like schema mapping, " +
    "data profiling, and machine learning algorithms, " +
    "it evaluates attributes like names or emails to detect duplicates " +
    "or relationships, even with variations or inconsistencies. " +
    "The workflow outputs consolidated, de-duplicated data." +
    "\n" +
    "We will use the machine learning-based matching technique.",
);

const sdkCreateMatchingWorkflow = new ScenarioAction(
  "sdkCreateMatchingWorkflow",
  async (/** @type {State} */ state) => {
    const createMatchingWorkflowParams = {
      roleArn: `${state.entityResolutionRole.OutputValue}`,
      workflowName: `${data.inputs.workflowName}`,
      description: "Created by using the AWS SDK for JavaScript (v3).",
      inputSourceConfig: [
        {
          inputSourceARN: `${state.jsonGlueTable.OutputValue}`,
          schemaName: `${data.inputs.schemaNameJson}`,
          applyNormalization: false,
        },
        {
          inputSourceARN: `${state.CSVGlueTable.OutputValue}`,
          schemaName: `${data.inputs.schemaNameCSV}`,
          applyNormalization: false,
        },
      ],
      outputSourceConfig: [
        {
          outputS3Path: `s3://${state.glueDataBucket.OutputValue}/eroutput`,
          output: [
            {
              name: state.idOutputAttribute,
            },
            {
              name: state.nameOutputAttribute,
            },
            {
              name: state.emailOutputAttribute,
            },
            {
              name: state.phoneOutputAttribute,
            },
          ],
          applyNormalization: false,
        },
      ],
      resolutionTechniques: { resolutionType: "ML_MATCHING" },
    };
    try {
      const command = new CreateMatchingWorkflowCommand(
        createMatchingWorkflowParams,
      );
      const response = await entityResolutionClient.send(command);
      state.workflowArn = response.workflowArn;
      console.log(
        `Workflow created successfully.\n The workflow ARN is: ${response.workflowArn}`,
      );
    } catch (caught) {
      if (caught instanceof ConflictException) {
        console.error(
          `The matching workflow already exists: ${caught.message} \n Exiting program.`,
        );
        return;
      }
      if (caught instanceof ValidationException) {
        console.error(
          `There was a validation exception: ${caught.message} \n Exiting program.`,
        );
        return;
      }
    }
  },
);
const displayMatchingJobOfWorkflow = new ScenarioOutput(
  "displayMatchingJobOfWorkflow",
  "3. Start the matching job of the workflow",
);

const sdkMatchingJobOfWorkflow = new ScenarioAction(
  "sdk",
  async (/** @type {State} */ state) => {
    const matchingJobOfWorkflowParams = {
      workflowName: `${data.inputs.workflowName}`,
    };
    try {
      const command = new StartMatchingJobCommand(matchingJobOfWorkflowParams);
      const response = await entityResolutionClient.send(command);
      state.jobID = response.jobId;
      console.log(`Job ID: ${state.jobID} \n
The matching job was successfully started.`);
    } catch (caught) {
      if (caught instanceof ConflictException) {
        console.error(
          `The matching workflow already exists: ${caught.message} \n Exiting program.`,
        );
        return;
      }
    }
  },
);

const displayGetDetailsforJob = new ScenarioOutput(
  "displayGetDetailsforJob",
  `4. While the matching job is running, let's look at other API methods. First, let's get details for the job `,
);

const sdkGetDetailsforJob = new ScenarioAction(
  "sdkGetDetailsforJob",
  async (/** @type {State} */ state) => {
    const getDetailsforJobParams = {
      workflowName: `${data.inputs.workflowName}`,
      jobId: `${state.jobID}`,
    };
    try {
      const command = new GetMatchingJobCommand(getDetailsforJobParams);
      const response = await entityResolutionClient.send(command);
      state.Status = response.status;
      state.response = response;
      console.log(`Job status: ${state.Status} `);
    } catch (caught) {
      console.error(caught.message);
      throw caught;
    }
  },
);

const displayGetSchemaMappingJson = new ScenarioOutput(
  "displayGetSchemaMappingJson",
  "5. Get the schema mapping for the JSON data.",
);

const sdkGetSchemaMappingJson = new ScenarioAction(
  "sdkGetSchemaMappingJson",
  async (/** @type {State} */ state) => {
    const getSchemaMappingJsonParams = {
      schemaName: `${data.inputs.schemaNameJson}`,
    };
    try {
      const command = new GetSchemaMappingCommand(getSchemaMappingJsonParams);
      const response = await entityResolutionClient.send(command);
      console.log("Schema·mapping·ARN·is:·", response.schemaArn);
      const resultMappings = response.mappedInputFields;
      const noOfResultMappings = resultMappings.length;
      for (let i = 0; i < noOfResultMappings; i++) {
        console.log(
          `Attribute name: ${resultMappings[i].fieldName} `,
          `Attribute type: ${resultMappings[i].type}`,
        );
      }
    } catch (caught) {
      console.error(caught.message);
      throw caught;
    }
  },
);

const displayListSchemaMappings = new ScenarioOutput(
  "displayListSchemaMappings",
  "6. List Schema Mappings.",
);

const sdkListSchemaMappings = new ScenarioAction(
  "sdkListSchemaMappings",
  async (/** @type {State} */ state) => {
    try {
      const command = new ListSchemaMappingsCommand({});
      const response = await entityResolutionClient.send(command);
      const noOfSchemas = response.schemaList.length;
      for (let i = 0; i < noOfSchemas; i++) {
        console.log(
          `Schema Mapping Name: ${response.schemaList[i].schemaName} `,
        );
      }
    } catch (caught) {
      console.error(caught.message);
      throw caught;
    }
  },
);

const displayTagTheJsonSchema = new ScenarioOutput(
  "display",
  "7. Tag the resource. \n" +
    "Tags can help you organize and categorize your Entity Resolution resources. " +
    "You can also use them to scope user permissions by granting a user permission " +
    "to access or change only resources with certain tag values. " +
    "In Entity Resolution, SchemaMapping and MatchingWorkflow can be tagged. For this example, " +
    "the SchemaMapping is tagged.",
);

const sdkTagTheJsonSchema = new ScenarioAction(
  "sdkGetSchemaMappingJson",
  async (/** @type {State} */ state) => {
    const tagResourceCommandParams = {
      resourceArn: state.schemaArn,
      tags: {
        tag1: "tag1Value",
        tag2: "tag2Value",
      },
    };
    try {
      const command = new TagResourceCommand(tagResourceCommandParams);
      const response = await entityResolutionClient.send(command);
      console.log("Successfully tagged the resource.");
    } catch (caught) {
      console.error(caught.message);
      throw caught;
    }
  },
);

const displayGetJobInfo = new ScenarioOutput(
  "displayGetJobInfo",
  "8. View the results of the AWS Entity Resolution Workflow.\n " +
    "Please perform this task manually in the AWS Management Console. ",
);

const displayDeleteResources = new ScenarioOutput(
  "displayDeleteResources",
  "9. Delete the resources \n" +
    "You cannot delete a workflow that is in a running state. So this will take ~30 minutes.\n" +
    "If you don't want to delete the resources, simply exit this application.",
);

const sdkDeleteResources = new ScenarioAction(
  "sdkDeleteResources",
  async (/** @type {State} */ state) => {
    console.log(
      "You selected to delete the resources. This will take about 30 minutes.",
    );
    await wait(1800);
    const bucketName = state.glueDataBucket.OutputValue;
    try {
      const emptyBucket = async ({ bucketName }) => {
        const listObjectsCommand = new ListObjectsCommand({
          Bucket: bucketName,
        });
        const { Contents } = await s3Client.send(listObjectsCommand);
        const keys = Contents.map((c) => c.Key);

        const deleteObjectsCommand = new DeleteObjectsCommand({
          Bucket: bucketName,
          Delete: { Objects: keys.map((key) => ({ Key: key })) },
        });
        await s3Client.send(deleteObjectsCommand);
        console.log(`Bucket ${bucketName} emptied successfully.\n`);
      };
      await emptyBucket({ bucketName });
    } catch (error) {
      console.log("error ", error);
    }
    try {
      const deleteBucket = async ({ bucketName }) => {
        const command = new DeleteBucketCommand({ Bucket: bucketName });
        await s3Client.send(command);
        console.log(`Bucket ${bucketName} deleted successfully.\n`);
      };
      await deleteBucket({ bucketName });
    } catch (error) {
      console.log("error ", error);
    }
    try {
      console.log(
        "Now we will delete the CloudFormation stack, which deletes the resources that were created at the beginning of the scenario.",
      );
      const deleteStackParams = { StackName: `${state.stackName}` };
      const command = new DeleteStackCommand(deleteStackParams);
      const response = await cloudFormationClient.send(command);
      console.log("CloudFormation stack deleted successfully.");
    } catch (error) {
      console.log("error ", error);
    }
    try {
      const deleteWorkflowParams = {
        workflowName: `${data.inputs.workflowName}`,
      };
      const command = new DeleteMatchingWorkflowCommand(deleteWorkflowParams);
      const response = await entityResolutionClient.send(command);
      console.log("Workflow deleted successfully!");
    } catch (caught) {
      if (caught instanceof ConflictException) {
        console.error(
          `Job associated with workflow ${data.inputs.workflowName} is still running, so can't be deleted.
          Neither can schemas ${data.inputs.schemaNameJson} and ${data.inputs.schemaNameCSV} associated with it. Please confirm this workflow is finished in the AWS Management Console, then delete it manually.`,
        );
        throw caught;
      }
    }
    try {
      const deleteJSONschemaMapping = {
        schemaName: `${data.inputs.schemaNameJson}`,
      };
      const command = new DeleteSchemaMappingCommand(deleteJSONschemaMapping);
      const response = await entityResolutionClient.send(command);
      console.log("Schema mapping deleted successfully. ");
    } catch (caught) {
      if (caught instanceof ConflictException) {
        console.error(
          `The schema ${data.inputs.schemaNameJson} can't be deleted because it is associated with workflow
           ${data.inputs.workflowName}, which is still running. Please confirm this workflow is finished in the AWS Management Console, then delete it manually.`,
        );
        throw caught;
      }
    }
    try {
      const deleteCSVschemaMapping = {
        schemaName: `${data.inputs.schemaNameCSV}`,
      };
      const command = new DeleteSchemaMappingCommand(deleteCSVschemaMapping);
      const response = await entityResolutionClient.send(command);
      console.log("Schema mapping deleted successfully.");
    } catch (caught) {
      if (caught instanceof ConflictException) {
        console.error(
          `The schema ${data.inputs.schemaNameCSV} can't be deleted because it is associated with workflow ${data.inputs.workflowName}, which is still running. Please confirm this workflow is finished in the AWS Management Console, then delete it manually.`,
        );
        throw caught;
      }
    }
  },
  {
    skipWhen: (/** @type {State} */ state) =>
      state.confirmDeleteResources === "",
  },
);

const goodbye = new ScenarioOutput(
  "goodbye",
  "Thank you for checking out the Amazon Location Service Use demo. We hope you " +
    "learned something new, or got some inspiration for your own apps today!" +
    " For more Amazon Location Services examples in different programming languages, have a look at: " +
    "https://docs.aws.amazon.com/code-library/latest/ug/location_code_examples.html",
);

const myScenario = new Scenario("Entity Resolution Basics Scenario", [
  greet,
  pressEnter,
  displayBuildCloudFormationStack,
  sdkBuildCloudFormationStack,
  pressEnter,
  displayCreateSchemaMapping,
  sdkCreateSchemaMapping,
  pressEnter,
  displayCreateMatchingWorkflow,
  sdkCreateMatchingWorkflow,
  pressEnter,
  displayMatchingJobOfWorkflow,
  sdkMatchingJobOfWorkflow,
  pressEnter,
  displayGetDetailsforJob,
  sdkGetDetailsforJob,
  pressEnter,
  displayGetSchemaMappingJson,
  sdkGetSchemaMappingJson,
  pressEnter,
  displayListSchemaMappings,
  sdkListSchemaMappings,
  pressEnter,
  displayTagTheJsonSchema,
  sdkTagTheJsonSchema,
  pressEnter,
  displayGetJobInfo,
  pressEnter,
  displayDeleteResources,
  pressEnter,
  sdkDeleteResources,
  pressEnter,
  goodbye,
]);

/** @type {{ stepHandlerOptions: StepHandlerOptions }} */
export const main = async (stepHandlerOptions) => {
  await myScenario.run(stepHandlerOptions);
};

// Invoke main function if this file was run directly.
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const { values } = parseArgs({
    options: {
      yes: {
        type: "boolean",
        short: "y",
      },
    },
  });
  main({ confirmAll: values.yes });
}
```
+ For API details, see the following topics in *AWS SDK for JavaScript API Reference*.
  + [CreateMatchingWorkflow](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/entityresolution-2018-05-10/CreateMatchingWorkflow)
  + [CreateSchemaMapping](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/entityresolution-2018-05-10/CreateSchemaMapping)
  + [DeleteMatchingWorkflow](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/entityresolution-2018-05-10/DeleteMatchingWorkflow)
  + [DeleteSchemaMapping](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/entityresolution-2018-05-10/DeleteSchemaMapping)
  + [GetMatchingJob](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/entityresolution-2018-05-10/GetMatchingJob)
  + [GetSchemaMapping](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/entityresolution-2018-05-10/GetSchemaMapping)
  + [ListMatchingWorkflows](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/entityresolution-2018-05-10/ListMatchingWorkflows)
  + [ListSchemaMappings](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/entityresolution-2018-05-10/ListSchemaMappings)
  + [StartMatchingJob](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/entityresolution-2018-05-10/StartMatchingJob)
  + [TagResource](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/entityresolution-2018-05-10/TagResource)

------
