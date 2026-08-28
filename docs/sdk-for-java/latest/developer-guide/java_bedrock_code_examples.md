---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_bedrock_code_examples.html
---

# Amazon Bedrock examples using SDK for Java 2.x
<a name="java_bedrock_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Java 2.x with Amazon Bedrock.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `GetFoundationModel`
<a name="bedrock_GetFoundationModel_java_topic"></a>

The following code example shows how to use `GetFoundationModel`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/bedrock#code-examples).
Get details about a foundation model using the synchronous Amazon Bedrock client.

```
    /**
     * Get details about an Amazon Bedrock foundation model.
     *
     * @param bedrockClient   The service client for accessing Amazon Bedrock.
     * @param modelIdentifier The model identifier.
     * @return An object containing the foundation model's details.
     */
    public static FoundationModelDetails getFoundationModel(BedrockClient bedrockClient, String modelIdentifier) {
        try {
            GetFoundationModelResponse response = bedrockClient.getFoundationModel(
                    r -> r.modelIdentifier(modelIdentifier)
            );

            FoundationModelDetails model = response.modelDetails();

            System.out.println(" Model ID:                     " + model.modelId());
            System.out.println(" Model ARN:                    " + model.modelArn());
            System.out.println(" Model Name:                   " + model.modelName());
            System.out.println(" Provider Name:                " + model.providerName());
            System.out.println(" Lifecycle status:             " + model.modelLifecycle().statusAsString());
            System.out.println(" Input modalities:             " + model.inputModalities());
            System.out.println(" Output modalities:            " + model.outputModalities());
            System.out.println(" Supported customizations:     " + model.customizationsSupported());
            System.out.println(" Supported inference types:    " + model.inferenceTypesSupported());
            System.out.println(" Response streaming supported: " + model.responseStreamingSupported());

            return model;

        } catch (ValidationException e) {
            throw new IllegalArgumentException(e.getMessage());
        } catch (SdkException e) {
            System.err.println(e.getMessage());
            throw new RuntimeException(e);
        }
    }
```
Get details about a foundation model using the asynchronous Amazon Bedrock client.

```
    /**
     * Get details about an Amazon Bedrock foundation model.
     *
     * @param bedrockClient   The async service client for accessing Amazon Bedrock.
     * @param modelIdentifier The model identifier.
     * @return An object containing the foundation model's details.
     */
    public static FoundationModelDetails getFoundationModel(BedrockAsyncClient bedrockClient, String modelIdentifier) {
        try {
            CompletableFuture<GetFoundationModelResponse> future = bedrockClient.getFoundationModel(
                    r -> r.modelIdentifier(modelIdentifier)
            );

            FoundationModelDetails model = future.get().modelDetails();

            System.out.println(" Model ID:                     " + model.modelId());
            System.out.println(" Model ARN:                    " + model.modelArn());
            System.out.println(" Model Name:                   " + model.modelName());
            System.out.println(" Provider Name:                " + model.providerName());
            System.out.println(" Lifecycle status:             " + model.modelLifecycle().statusAsString());
            System.out.println(" Input modalities:             " + model.inputModalities());
            System.out.println(" Output modalities:            " + model.outputModalities());
            System.out.println(" Supported customizations:     " + model.customizationsSupported());
            System.out.println(" Supported inference types:    " + model.inferenceTypesSupported());
            System.out.println(" Response streaming supported: " + model.responseStreamingSupported());

            return model;

        } catch (ExecutionException e) {
            if (e.getMessage().contains("ValidationException")) {
                throw new IllegalArgumentException(e.getMessage());
            } else {
                System.err.println(e.getMessage());
                throw new RuntimeException(e);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.err.println(e.getMessage());
            throw new RuntimeException(e);
        }
    }
```
+  For API details, see [GetFoundationModel](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetFoundationModel) in *AWS SDK for Java 2.x API Reference*.

### `ListFoundationModels`
<a name="bedrock_ListFoundationModels_java_topic"></a>

The following code example shows how to use `ListFoundationModels`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/bedrock#code-examples).
List the available Amazon Bedrock foundation models using the synchronous Amazon Bedrock client.

```
    /**
     * Lists Amazon Bedrock foundation models that you can use.
     * You can filter the results with the request parameters.
     *
     * @param bedrockClient The service client for accessing Amazon Bedrock.
     * @return A list of objects containing the foundation models' details
     */
    public static List<FoundationModelSummary> listFoundationModels(BedrockClient bedrockClient) {

        try {
            ListFoundationModelsResponse response = bedrockClient.listFoundationModels(r -> {});

            List<FoundationModelSummary> models = response.modelSummaries();

            if (models.isEmpty()) {
                System.out.println("No available foundation models in " + region.toString());
            } else {
                for (FoundationModelSummary model : models) {
                    System.out.println("Model ID: " + model.modelId());
                    System.out.println("Provider: " + model.providerName());
                    System.out.println("Name:     " + model.modelName());
                    System.out.println();
                }
            }

            return models;

        } catch (SdkClientException e) {
            System.err.println(e.getMessage());
            throw new RuntimeException(e);
        }
    }
```
List the available Amazon Bedrock foundation models using the asynchronous Amazon Bedrock client.

```
    /**
     * Lists Amazon Bedrock foundation models that you can use.
     * You can filter the results with the request parameters.
     *
     * @param bedrockClient The async service client for accessing Amazon Bedrock.
     * @return A list of objects containing the foundation models' details
     */
    public static List<FoundationModelSummary> listFoundationModels(BedrockAsyncClient bedrockClient) {
        try {
            CompletableFuture<ListFoundationModelsResponse> future = bedrockClient.listFoundationModels(r -> {});

            List<FoundationModelSummary> models = future.get().modelSummaries();

            if (models.isEmpty()) {
                System.out.println("No available foundation models in " + region.toString());
            } else {
                for (FoundationModelSummary model : models) {
                    System.out.println("Model ID: " + model.modelId());
                    System.out.println("Provider: " + model.providerName());
                    System.out.println("Name:     " + model.modelName());
                    System.out.println();
                }
            }

            return models;

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.err.println(e.getMessage());
            throw new RuntimeException(e);
        } catch (ExecutionException e) {
            System.err.println(e.getMessage());
            throw new RuntimeException(e);
        }
    }
```
+  For API details, see [ListFoundationModels](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListFoundationModels) in *AWS SDK for Java 2.x API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
