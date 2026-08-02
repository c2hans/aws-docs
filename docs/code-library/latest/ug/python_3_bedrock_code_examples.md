---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_bedrock_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Bedrock examples using SDK for Python (Boto3)
<a name="python_3_bedrock_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with Amazon Bedrock.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Actions](#actions)
+ [Scenarios](#scenarios)

## Get started
<a name="get_started"></a>

### Hello Amazon Bedrock
<a name="bedrock_Hello_python_3_topic"></a>

The following code example shows how to get started using Amazon Bedrock.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock#code-examples).

```
"""
Lists the available Amazon Bedrock models.
"""
import logging
import json
import boto3

from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def list_foundation_models(bedrock_client):
    """
    Gets a list of available Amazon Bedrock foundation models.

    :return: The list of available bedrock foundation models.
    """

    try:
        response = bedrock_client.list_foundation_models()
        models = response["modelSummaries"]
        logger.info("Got %s foundation models.", len(models))
        return models

    except ClientError:
        logger.error("Couldn't list foundation models.")
        raise

def main():
    """Entry point for the example. Uses the AWS SDK for Python (Boto3)
    to create an Amazon Bedrock client. Then lists the available Bedrock models
    in the region set in the callers profile and credentials.
    """

    bedrock_client = boto3.client(service_name="bedrock")

    fm_models = list_foundation_models(bedrock_client)
    for model in fm_models:
        print(f"Model: {model['modelName']}")
        print(json.dumps(model, indent=2))
        print("---------------------------\n")

    logger.info("Done.")

if __name__ == "__main__":
    main()
```
+  For API details, see [ListFoundationModels](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListFoundationModels) in *AWS SDK for Python (Boto3) API Reference*.

## Actions
<a name="actions"></a>

### `GetFoundationModel`
<a name="bedrock_GetFoundationModel_python_3_topic"></a>

The following code example shows how to use `GetFoundationModel`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock#code-examples).
Get details about a foundation model.

```
    def get_foundation_model(self, model_identifier):
        """
        Get details about an Amazon Bedrock foundation model.

        :return: The foundation model's details.
        """

        try:
            return self.bedrock_client.get_foundation_model(
                modelIdentifier=model_identifier
            )["modelDetails"]
        except ClientError:
            logger.error(
                f"Couldn't get foundation models details for {model_identifier}"
            )
            raise
```
+  For API details, see [GetFoundationModel](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetFoundationModel) in *AWS SDK for Python (Boto3) API Reference*.

### `ListFoundationModels`
<a name="bedrock_ListFoundationModels_python_3_topic"></a>

The following code example shows how to use `ListFoundationModels`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock#code-examples).
List the available Amazon Bedrock foundation models.

```
    def list_foundation_models(self):
        """
        List the available Amazon Bedrock foundation models.

        :return: The list of available bedrock foundation models.
        """

        try:
            response = self.bedrock_client.list_foundation_models()
            models = response["modelSummaries"]
            logger.info("Got %s foundation models.", len(models))
            return models

        except ClientError:
            logger.error("Couldn't list foundation models.")
            raise
```
+  For API details, see [ListFoundationModels](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListFoundationModels) in *AWS SDK for Python (Boto3) API Reference*.

## Scenarios
<a name="scenarios"></a>

### Orchestrate generative AI applications with Step Functions
<a name="cross_ServerlessPromptChaining_python_3_topic"></a>

The following code example shows how to build and orchestrate generative AI applications with Amazon Bedrock and Step Functions.

**SDK for Python (Boto3)**
 The Amazon Bedrock Serverless Prompt Chaining scenario demonstrates how [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), and [https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) can be used to build and orchestrate complex, serverless, and highly scalable generative AI applications. It contains the following working examples:
+  Write an analysis of a given novel for a literature blog. This example illustrates a simple, sequential chain of prompts.
+  Generate a short story about a given topic. This example illustrates how the AI can iteratively process a list of items that it previously generated.
+  Create an itinerary for a weekend vacation to a given destination. This example illustrates how to parallelize multiple distinct prompts.
+  Pitch movie ideas to a human user acting as a movie producer. This example illustrates how to parallelize the same prompt with different inference parameters, how to backtrack to a previous step in the chain, and how to include human input as part of the workflow.
+  Plan a meal based on ingredients the user has at hand. This example illustrates how prompt chains can incorporate two distinct AI conversations, with two AI personas engaging in a debate with each other to improve the final outcome.
+  Find and summarize today's highest trending GitHub repository. This example illustrates chaining multiple AI agents that interact with external APIs.
 For complete source code and instructions to set up and run, see the full project on [GitHub](https://github.com/aws-samples/amazon-bedrock-serverless-prompt-chaining).

**Services used in this example**
+ Amazon Bedrock
+ Amazon Bedrock Runtime
+ Amazon Bedrock Agents
+ Amazon Bedrock Agents Runtime
+ Step Functions
