---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/entityresolution_example_entityresolution_CreateSchemaMapping_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateSchemaMapping` with an AWS SDK
<a name="entityresolution_example_entityresolution_CreateSchemaMapping_section"></a>

The following code examples show how to use `CreateSchemaMapping`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](entityresolution_example_entityresolution_Scenario_section.md)

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/entityresolution#code-examples).

```
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
```
+  For API details, see [CreateSchemaMapping](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/CreateSchemaMapping) in *AWS SDK for Java 2.x API Reference*.

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/entityresolution#code-examples).

```
//The default inputs for this demo are read from the ../inputs.json.

import { fileURLToPath } from "node:url";

import {
  CreateSchemaMappingCommand,
  EntityResolutionClient,
} from "@aws-sdk/client-entityresolution";
import data from "../inputs.json" with { type: "json" };

const region = "eu-west-1";
const erClient = new EntityResolutionClient({ region: region });

export const main = async () => {
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
    const response = await erClient.send(command);
    console.log("The JSON schema mapping name is ", response.schemaName);
  } catch (error) {
    console.log("error ", error.message);
  }
};
```
+  For API details, see [CreateSchemaMapping](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/entityresolution/command/CreateSchemaMappingCommand) in *AWS SDK for JavaScript API Reference*.

------
