---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_bedrock-agent_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Bedrock Agents examples using SDK for Python (Boto3)
<a name="python_3_bedrock-agent_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with Amazon Bedrock Agents.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)
+ [Scenarios](#scenarios)

## Actions
<a name="actions"></a>

### `CreateAgent`
<a name="bedrock-agent_CreateAgent_python_3_topic"></a>

The following code example shows how to use `CreateAgent`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create an agent.

```
    def create_agent(self, agent_name, foundation_model, role_arn, instruction):
        """
        Creates an agent that orchestrates interactions between foundation models,
        data sources, software applications, user conversations, and APIs to carry
        out tasks to help customers.

        :param agent_name: A name for the agent.
        :param foundation_model: The foundation model to be used for orchestration by the agent.
        :param role_arn: The ARN of the IAM role with permissions needed by the agent.
        :param instruction: Instructions that tell the agent what it should do and how it should
                            interact with users.
        :return: The response from Amazon Bedrock Agents if successful, otherwise raises an exception.
        """
        try:
            response = self.client.create_agent(
                agentName=agent_name,
                foundationModel=foundation_model,
                agentResourceRoleArn=role_arn,
                instruction=instruction,
            )
        except ClientError as e:
            logger.error(f"Error: Couldn't create agent. Here's why: {e}")
            raise
        else:
            return response["agent"]
```
+  For API details, see [CreateAgent](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateAgent) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateAgentActionGroup`
<a name="bedrock-agent_CreateAgentActionGroup_python_3_topic"></a>

The following code example shows how to use `CreateAgentActionGroup`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create an agent action group.

```
    def create_agent_action_group(
            self, name, description, agent_id, agent_version, function_arn, api_schema
    ):
        """
        Creates an action group for an agent. An action group defines a set of actions that an
        agent should carry out for the customer.

        :param name: The name to give the action group.
        :param description: The description of the action group.
        :param agent_id: The unique identifier of the agent for which to create the action group.
        :param agent_version: The version of the agent for which to create the action group.
        :param function_arn: The ARN of the Lambda function containing the business logic that is
                             carried out upon invoking the action.
        :param api_schema: Contains the OpenAPI schema for the action group.
        :return: Details about the action group that was created.
        """
        try:
            response = self.client.create_agent_action_group(
                actionGroupName=name,
                description=description,
                agentId=agent_id,
                agentVersion=agent_version,
                actionGroupExecutor={"lambda": function_arn},
                apiSchema={"payload": api_schema},
            )
            agent_action_group = response["agentActionGroup"]
        except ClientError as e:
            logger.error(f"Error: Couldn't create agent action group. Here's why: {e}")
            raise
        else:
            return agent_action_group
```
+  For API details, see [CreateAgentActionGroup](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateAgentActionGroup) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateAgentAlias`
<a name="bedrock-agent_CreateAgentAlias_python_3_topic"></a>

The following code example shows how to use `CreateAgentAlias`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create an agent alias.

```
    def create_agent_alias(self, name, agent_id):
        """
        Creates an alias of an agent that can be used to deploy the agent.

        :param name: The name of the alias.
        :param agent_id: The unique identifier of the agent.
        :return: Details about the alias that was created.
        """
        try:
            response = self.client.create_agent_alias(
                agentAliasName=name, agentId=agent_id
            )
            agent_alias = response["agentAlias"]
        except ClientError as e:
            logger.error(f"Couldn't create agent alias. {e}")
            raise
        else:
            return agent_alias
```
+  For API details, see [CreateAgentAlias](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateAgentAlias) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateFlow`
<a name="bedrock-agent_CreateFlow_python_3_topic"></a>

The following code example shows how to use `CreateFlow`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create an Amazon Bedrock flow.

```
def create_flow(client, flow_name, flow_description, role_arn, flow_def):
    """
    Creates an Amazon Bedrock flow.

    Args:
    client: Amazon Bedrock agent boto3 client.
    flow_name (str): The name for the new flow.
    role_arn (str):  The ARN for the IAM role that use flow uses.
    flow_def (json): The JSON definition of the flow that you want to create.

    Returns:
        dict: The response from CreateFlow.
    """
    try:

        logger.info("Creating flow: %s.", flow_name)

        response = client.create_flow(
            name=flow_name,
            description=flow_description,
            executionRoleArn=role_arn,
            definition=flow_def
        )

        logger.info("Successfully created flow: %s. ID: %s",
                    flow_name,
                    {response['id']})

        return response

    except ClientError as e:
        logger.exception("Client error creating flow: %s", {str(e)})
        raise

    except Exception as e:
        logger.exception("Unexepcted error creating flow: %s", {str(e)})
        raise
```
+  For API details, see [CreateFlow](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateFlow) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateFlowAlias`
<a name="bedrock-agent_CreateFlowAlias_python_3_topic"></a>

The following code example shows how to use `CreateFlowAlias`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create an alias for an Amazon Bedrock flow.

```
def create_flow_alias(client, flow_id, flow_version, name, description):
    """
    Creates an alias for an Amazon Bedrock flow.

    Args:
        client: bedrock agent boto3 client.
        flow_id (str): The identifier of the flow.

    Returns:
        str: The ID for the flow alias.
    """

    try:
        logger.info("Creating flow alias for flow: %s.", flow_id)

        response = client.create_flow_alias(
            flowIdentifier=flow_id,
            name=name,
            description=description,
            routingConfiguration=[
                {
                    "flowVersion": flow_version
                }
            ]
        )
        logger.info("Successfully created flow alias for %s.", flow_id)

        return response['id']

    except ClientError as e:
        logging.exception("Client error creating alias for flow: %s - %s",
                flow_id, str(e))
        raise
    except Exception as e:
        logging.exception("Unexpected error creating alias for flow : %s - %s",
                flow_id, str(e))
        raise
```
+  For API details, see [CreateFlowAlias](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateFlowAlias) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateFlowVersion`
<a name="bedrock-agent_CreateFlowVersion_python_3_topic"></a>

The following code example shows how to use `CreateFlowVersion`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create a version of an Amazon Bedrock flow.

```
def create_flow_version(client, flow_id, description):
    """
    Creates a version of an Amazon Bedrock flow.

    Args:
        client: Amazon Bedrock agent boto3 client.
        flow_id (str): The identifier of the flow.
        description (str) : A description for the flow.

    Returns:
        str: The version for the flow.
    """
    try:

        logger.info("Creating flow version for flow: %s.", flow_id)

        # Call CreateFlowVersion operation
        response = client.create_flow_version(
            flowIdentifier=flow_id,
            description=description
        )

        logging.info("Successfully created flow version %s for flow %s.",
            response['version'], flow_id)

        return response['version']

    except ClientError as e:
        logging.exception("Client error creating flow: %s", str(e))
        raise
    except Exception as e:
        logging.exception("Unexpected error creating flow : %s", str(e))
        raise
```
+  For API details, see [CreateFlowVersion](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateFlowVersion) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateKnowledgeBase`
<a name="bedrock-agent_CreateKnowledgeBase_python_3_topic"></a>

The following code example shows how to use `CreateKnowledgeBase`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create an Amazon Bedrock knowledge base.

```
def create_knowledge_base(bedrock_agent_client, name, role_arn, description=None):
    """
    Creates a new knowledge base.

    Args:
        bedrock_agent_client: The Boto3 Bedrock Agent client.
        name (str): The name of the knowledge base.
        role_arn (str): The ARN of the IAM role that the knowledge base assumes to access resources.
        description (str, optional): A description of the knowledge base.

    Returns:
        dict: The details of the created knowledge base.
    """
    try:
        kwargs = {
            "name": name,
            "roleArn": role_arn,
            "knowledgeBaseConfiguration": {
                "type": "VECTOR",
                "vectorKnowledgeBaseConfiguration": {
                    "embeddingModelArn": "arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1"
                }
            },
            "storageConfiguration": {
                "type": "OPENSEARCH_SERVERLESS",
                # Note: You will need to create an OpenSearch Serverless collection first and replace this ARN
                # with your actual collection ARN from the OpenSearch console. If you use the console instead,
                # you can use the quick-create flow to have Knowledge Bases create the collection for you.
                "opensearchServerlessConfiguration": {
                    "collectionArn": "arn:aws:aoss:us-east-1::123456789012:collection/abcdefgh12345678defgh",
                        "fieldMapping": {
                        "metadataField": "metadata",
                        "textField": "text",
                        "vectorField": "vector"
                        },
                    "vectorIndexName": "test-uuid"
                    },
                },
            "clientToken": "test-client-token-" + str(uuid.uuid4())
        }

        if description:
            kwargs["description"] = description

        response = bedrock_agent_client.create_knowledge_base(**kwargs)

        logger.info("Created knowledge base with ID: %s", response["knowledgeBase"]["knowledgeBaseId"])
        return response["knowledgeBase"]

    except ClientError as err:
        logger.error(
            "Couldn't create knowledge base. Here's why: %s: %s",
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise
```
+  For API details, see [CreateKnowledgeBase](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateKnowledgeBase) in *AWS SDK for Python (Boto3) API Reference*.

### `CreatePrompt`
<a name="bedrock-agent_CreatePrompt_python_3_topic"></a>

The following code example shows how to use `CreatePrompt`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create an Amazon Bedrock managed prompt.

```
def create_prompt(client, prompt_name, prompt_description, prompt_template, model_id=None):
    """
    Creates an Amazon Bedrock managed prompt.

    Args:
    client: Amazon Bedrock Agent boto3 client.
    prompt_name (str): The name for the new prompt.
    prompt_description (str): The description for the new prompt.
    prompt_template (str): The template for the prompt.
    model_id (str, optional): The model ID to associate with the prompt.

    Returns:
        dict: The response from CreatePrompt.
    """
    try:
        logger.info("Creating prompt: %s.", prompt_name)

        # Create a variant with the template
        variant = {
            "name": "default",
            "templateType": "TEXT",
            "templateConfiguration": {
                "text": {
                    "text": prompt_template,
                    "inputVariables": []
                }
            }
        }

        # Extract input variables from the template
        # Look for patterns like {{variable_name}}

        variables = re.findall(r'{{(.*?)}}', prompt_template)
        for var in variables:
            variant["templateConfiguration"]["text"]["inputVariables"].append({"name": var.strip()})

        # Add model ID if provided
        if model_id:
            variant["modelId"] = model_id

        # Create the prompt with the variant
        create_params = {
            'name': prompt_name,
            'description': prompt_description,
            'variants': [variant]
        }

        response = client.create_prompt(**create_params)

        logger.info("Successfully created prompt: %s. ID: %s",
                    prompt_name,
                    response['id'])

        return response

    except ClientError as e:
        logger.exception("Client error creating prompt: %s", str(e))
        raise

    except Exception as e:
        logger.exception("Unexpected error creating prompt: %s", str(e))
        raise
```
+  For API details, see [CreatePrompt](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreatePrompt) in *AWS SDK for Python (Boto3) API Reference*.

### `CreatePromptVersion`
<a name="bedrock-agent_CreatePromptVersion_python_3_topic"></a>

The following code example shows how to use `CreatePromptVersion`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create a version of an Amazon Bedrock managed prompt.

```
def create_prompt_version(client, prompt_id, description=None):
    """
    Creates a version of an Amazon Bedrock managed prompt.

    Args:
    client: Amazon Bedrock Agent boto3 client.
    prompt_id (str): The identifier of the prompt to create a version for.
    description (str, optional): A description for the version.

    Returns:
        dict: The response from CreatePromptVersion.
    """
    try:
        logger.info("Creating version for prompt ID: %s.", prompt_id)

        create_params = {
            'promptIdentifier': prompt_id
        }

        if description:
            create_params['description'] = description

        response = client.create_prompt_version(**create_params)

        logger.info("Successfully created prompt version: %s", response['version'])
        logger.info("Prompt version ARN: %s", response['arn'])

        return response

    except ClientError as e:
        logger.exception("Client error creating prompt version: %s", str(e))
        raise

    except Exception as e:
        logger.exception("Unexpected error creating prompt version: %s", str(e))
        raise
```
+  For API details, see [CreatePromptVersion](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreatePromptVersion) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteAgent`
<a name="bedrock-agent_DeleteAgent_python_3_topic"></a>

The following code example shows how to use `DeleteAgent`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Delete an agent.

```
    def delete_agent(self, agent_id):
        """
        Deletes an Amazon Bedrock agent.

        :param agent_id: The unique identifier of the agent to delete.
        :return: The response from Amazon Bedrock Agents if successful, otherwise raises an exception.
        """

        try:
            response = self.client.delete_agent(
                agentId=agent_id, skipResourceInUseCheck=False
            )
        except ClientError as e:
            logger.error(f"Couldn't delete agent. {e}")
            raise
        else:
            return response
```
+  For API details, see [DeleteAgent](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeleteAgent) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteAgentAlias`
<a name="bedrock-agent_DeleteAgentAlias_python_3_topic"></a>

The following code example shows how to use `DeleteAgentAlias`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Delete an agent alias.

```
    def delete_agent_alias(self, agent_id, agent_alias_id):
        """
        Deletes an alias of an Amazon Bedrock agent.

        :param agent_id: The unique identifier of the agent that the alias belongs to.
        :param agent_alias_id: The unique identifier of the alias to delete.
        :return: The response from Amazon Bedrock Agents if successful, otherwise raises an exception.
        """

        try:
            response = self.client.delete_agent_alias(
                agentId=agent_id, agentAliasId=agent_alias_id
            )
        except ClientError as e:
            logger.error(f"Couldn't delete agent alias. {e}")
            raise
        else:
            return response
```
+  For API details, see [DeleteAgentAlias](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeleteAgentAlias) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteFlow`
<a name="bedrock-agent_DeleteFlow_python_3_topic"></a>

The following code example shows how to use `DeleteFlow`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Delete an Amazon Bedrock flow.

```
def delete_flow(client, flow_id):
    """
    Deletes an Amazon Bedrock flow.

    Args:
    client: Amazon Bedrock agent boto3 client.
    flow_id (str): The identifier of the flow that you want to delete.

    Returns:
        dict: The response from the DeleteFLow operation.
    """
    try:

        logger.info("Deleting flow ID: %s.",
                    flow_id)

        # Call DeleteFlow operation
        response = client.delete_flow(
            flowIdentifier=flow_id,
            skipResourceInUseCheck=True
        )

        logger.info("Finished deleting flow ID: %s", flow_id)

        return response

    except ClientError as e:
        logger.exception("Client error deleting flow: %s", {str(e)})
        raise

    except Exception as e:
        logger.exception("Unexepcted error deleting flow: %s", {str(e)})
        raise
```
+  For API details, see [DeleteFlow](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeleteFlow) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteFlowAlias`
<a name="bedrock-agent_DeleteFlowAlias_python_3_topic"></a>

The following code example shows how to use `DeleteFlowAlias`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Delete an alias for an Amazon Bedrock flow.

```
def delete_flow_alias(client, flow_id, flow_alias_id):
    """
    Deletes an Amazon Bedrock flow alias.

    Args:
        client: bedrock agent boto3 client.
        flow_id (str): The identifier of the flow.

    Returns:
        dict: The response from the call to DetectFLowAlias
    """
    try:

        logger.info("Deleting flow alias %s for flow: %s.", flow_alias_id, flow_id)

        # Delete the flow alias.
        response = client.delete_flow_alias(
            aliasIdentifier=flow_alias_id,
            flowIdentifier=flow_id
        )

        logging.info("Successfully deleted flow version for %s.", flow_id)
        return response

    except ClientError as e:
        logging.exception("Client error deleting flow version: %s", str(e))
        raise
    except Exception as e:
        logging.exception("Unexpected deleting flow version: %s", str(e))
        raise
```
+  For API details, see [DeleteFlowAlias](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeleteFlowAlias) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteFlowVersion`
<a name="bedrock-agent_DeleteFlowVersion_python_3_topic"></a>

The following code example shows how to use `DeleteFlowVersion`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Delete a version of an Amazon Bedrock flow.

```
def delete_flow_version(client, flow_id, flow_version):
    """
    Deletes a version of an Amazon Bedrock flow.

    Args:
        client: Amazon Bedrock agent boto3 client.
        flow_id (str): The identifier of the flow.

    Returns:
        dict: The response from DeleteFlowVersion.
    """
    try:

        logger.info("Deleting flow version %s for flow: %s.",flow_version, flow_id)

        # Call DeleteFlowVersion operation
        response = client.delete_flow_version(
            flowIdentifier=flow_id,
            flowVersion=flow_version
        )

        logging.info("Successfully deleted flow version %s for %s.",
                flow_version,
                flow_id)
        return response

    except ClientError as e:
        logging.exception("Client error deleting flow version: %s ", str(e))
        raise
    except Exception as e:
        logging.exception("Unexpected deleting flow version: %s", str(e))
        raise
```
+  For API details, see [DeleteFlowVersion](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeleteFlowVersion) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteKnowledgeBase`
<a name="bedrock-agent_DeleteKnowledgeBase_python_3_topic"></a>

The following code example shows how to use `DeleteKnowledgeBase`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Delete an Amazon Bedrock knowledge base.

```
def delete_knowledge_base(bedrock_agent_client, knowledge_base_id):
    """
    Deletes a knowledge base.

    Args:
        bedrock_agent_client: The Boto3 Bedrock Agent client.
        knowledge_base_id (str): The ID of the knowledge base to delete.

    Returns:
        bool: True if the deletion was successful.
    """
    try:
        bedrock_agent_client.delete_knowledge_base(
            knowledgeBaseId=knowledge_base_id
        )

        logger.info("Deleted knowledge base: %s", knowledge_base_id)
        return True
    except ClientError as err:
        logger.error(
            "Couldn't delete knowledge base %s. Here's why: %s: %s",
            knowledge_base_id,
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise
```
+  For API details, see [DeleteKnowledgeBase](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeleteKnowledgeBase) in *AWS SDK for Python (Boto3) API Reference*.

### `DeletePrompt`
<a name="bedrock-agent_DeletePrompt_python_3_topic"></a>

The following code example shows how to use `DeletePrompt`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Delete an Amazon Bedrock managed prompt.

```
def delete_prompt(client, prompt_id):
    """
    Deletes an Amazon Bedrock managed prompt.

    Args:
    client: Amazon Bedrock Agent boto3 client.
    prompt_id (str): The identifier of the prompt that you want to delete.

    Returns:
        dict: The response from the DeletePrompt operation.
    """
    try:
        logger.info("Deleting prompt ID: %s.", prompt_id)

        response = client.delete_prompt(
            promptIdentifier=prompt_id
        )

        logger.info("Finished deleting prompt ID: %s", prompt_id)

        return response

    except ClientError as e:
        logger.exception("Client error deleting prompt: %s", str(e))
        raise

    except Exception as e:
        logger.exception("Unexpected error deleting prompt: %s", str(e))
        raise
```
+  For API details, see [DeletePrompt](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeletePrompt) in *AWS SDK for Python (Boto3) API Reference*.

### `GetAgent`
<a name="bedrock-agent_GetAgent_python_3_topic"></a>

The following code example shows how to use `GetAgent`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Get an agent.

```
    def get_agent(self, agent_id, log_error=True):
        """
        Gets information about an agent.

        :param agent_id: The unique identifier of the agent.
        :param log_error: Whether to log any errors that occur when getting the agent.
                          If True, errors will be logged to the logger. If False, errors
                          will still be raised, but not logged.
        :return: The information about the requested agent.
        """

        try:
            response = self.client.get_agent(agentId=agent_id)
            agent = response["agent"]
        except ClientError as e:
            if log_error:
                logger.error(f"Couldn't get agent {agent_id}. {e}")
            raise
        else:
            return agent
```
+  For API details, see [GetAgent](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/GetAgent) in *AWS SDK for Python (Boto3) API Reference*.

### `GetFlow`
<a name="bedrock-agent_GetFlow_python_3_topic"></a>

The following code example shows how to use `GetFlow`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Get an Amazon Bedrock flow.

```
def get_flow(client, flow_id):
    """
    Gets an Amazon Bedrock flow.

    Args:
    client: bedrock agent boto3 client.
        flow_id (str): The identifier of the flow that you want to get.

    Returns:
        dict: The response from the GetFlow operation.
    """
    try:

        logger.info("Getting flow ID: %s.",
                    flow_id)

        # Call GetFlow operation.
        response = client.get_flow(
            flowIdentifier=flow_id
        )

        logger.info("Retrieved flow ID: %s. Name: %s", flow_id,
                    response['name'])

        return response

    except ClientError as e:
        logger.exception("Client error getting flow: %s", {str(e)})
        raise

    except Exception as e:
        logger.exception("Unexepcted error getting flow: %s", {str(e)})
        raise
```
+  For API details, see [GetFlow](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/GetFlow) in *AWS SDK for Python (Boto3) API Reference*.

### `GetFlowVersion`
<a name="bedrock-agent_GetFlowVersion_python_3_topic"></a>

The following code example shows how to use `GetFlowVersion`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Get a version of an Amazon Bedrock flow.

```
def get_flow_version(client, flow_id, flow_version):
    """
    Gets information about a version of an Amazon Bedrock flow.

    Args:
        client: Amazon Bedrock agent boto3 client.
        flow_id (str): The identifier of the flow.
        flow_version (str): The flow version of the flow.

    Returns:
        dict: The response from the call to GetFlowVersion.
    """
    try:

        logger.info("Deleting flow version for flow: %s.", flow_id)

        # Call GetFlowVersion operation
        response = client.get_flow_version(
            flowIdentifier=flow_id,
            flowVersion=flow_version
        )

        logging.info("Successfully got flow version %s information for flow %s.",
                    flow_version,
                    flow_id)

        return response

    except ClientError as e:
        logging.exception("Client error getting flow version: %s", str(e))
        raise
    except Exception as e:
        logging.exception("Unexpected error getting flow version: %s", str(e))
        raise
```
+  For API details, see [GetFlowVersion](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/GetFlowVersion) in *AWS SDK for Python (Boto3) API Reference*.

### `GetKnowledgeBase`
<a name="bedrock-agent_GetKnowledgeBase_python_3_topic"></a>

The following code example shows how to use `GetKnowledgeBase`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Get an Amazon Bedrock knowledge base.

```
def get_knowledge_base(bedrock_agent_client, knowledge_base_id):
    """
    Gets details about a specific knowledge base.

    Args:
        bedrock_agent_client: The Boto3 Bedrock Agent client.
        knowledge_base_id (str): The ID of the knowledge base.

    Returns:
        dict: The details of the knowledge base.
    """
    try:
        response = bedrock_agent_client.get_knowledge_base(
            knowledgeBaseId=knowledge_base_id
        )

        logger.info("Retrieved knowledge base: %s", knowledge_base_id)
        return response["knowledgeBase"]
    except ClientError as err:
        logger.error(
            "Couldn't get knowledge base %s. Here's why: %s: %s",
            knowledge_base_id,
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise
```
+  For API details, see [GetKnowledgeBase](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/GetKnowledgeBase) in *AWS SDK for Python (Boto3) API Reference*.

### `GetPrompt`
<a name="bedrock-agent_GetPrompt_python_3_topic"></a>

The following code example shows how to use `GetPrompt`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Get an Amazon Bedrock managed prompt.

```
def get_prompt(client, prompt_id):
    """
    Gets an Amazon Bedrock managed prompt.

    Args:
    client: Amazon Bedrock Agent boto3 client.
    prompt_id (str): The identifier of the prompt that you want to get.

    Returns:
        dict: The response from the GetPrompt operation.
    """
    try:
        logger.info("Getting prompt ID: %s.", prompt_id)

        response = client.get_prompt(
            promptIdentifier=prompt_id
        )

        logger.info("Retrieved prompt ID: %s. Name: %s",
                    prompt_id,
                    response['name'])

        return response

    except ClientError as e:
        logger.exception("Client error getting prompt: %s", str(e))
        raise

    except Exception as e:
        logger.exception("Unexpected error getting prompt: %s", str(e))
        raise
```
+  For API details, see [GetPrompt](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/GetPrompt) in *AWS SDK for Python (Boto3) API Reference*.

### `ListAgentActionGroups`
<a name="bedrock-agent_ListAgentActionGroups_python_3_topic"></a>

The following code example shows how to use `ListAgentActionGroups`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
List the action groups for an agent.

```
    def list_agent_action_groups(self, agent_id, agent_version):
        """
        List the action groups for a version of an Amazon Bedrock Agent.

        :param agent_id: The unique identifier of the agent.
        :param agent_version: The version of the agent.
        :return: The list of action group summaries for the version of the agent.
        """

        try:
            action_groups = []

            paginator = self.client.get_paginator("list_agent_action_groups")
            for page in paginator.paginate(
                    agentId=agent_id,
                    agentVersion=agent_version,
                    PaginationConfig={"PageSize": 10},
            ):
                action_groups.extend(page["actionGroupSummaries"])

        except ClientError as e:
            logger.error(f"Couldn't list action groups. {e}")
            raise
        else:
            return action_groups
```
+  For API details, see [ListAgentActionGroups](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/ListAgentActionGroups) in *AWS SDK for Python (Boto3) API Reference*.

### `ListAgentKnowledgeBases`
<a name="bedrock-agent_ListAgentKnowledgeBases_python_3_topic"></a>

The following code example shows how to use `ListAgentKnowledgeBases`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
List the knowledge bases associated with an agent.

```
    def list_agent_knowledge_bases(self, agent_id, agent_version):
        """
        List the knowledge bases associated with a version of an Amazon Bedrock Agent.

        :param agent_id: The unique identifier of the agent.
        :param agent_version: The version of the agent.
        :return: The list of knowledge base summaries for the version of the agent.
        """

        try:
            knowledge_bases = []

            paginator = self.client.get_paginator("list_agent_knowledge_bases")
            for page in paginator.paginate(
                    agentId=agent_id,
                    agentVersion=agent_version,
                    PaginationConfig={"PageSize": 10},
            ):
                knowledge_bases.extend(page["agentKnowledgeBaseSummaries"])

        except ClientError as e:
            logger.error(f"Couldn't list knowledge bases. {e}")
            raise
        else:
            return knowledge_bases
```
+  For API details, see [ListAgentKnowledgeBases](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/ListAgentKnowledgeBases) in *AWS SDK for Python (Boto3) API Reference*.

### `ListAgents`
<a name="bedrock-agent_ListAgents_python_3_topic"></a>

The following code example shows how to use `ListAgents`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
List the agents belonging to an account.

```
    def list_agents(self):
        """
        List the available Amazon Bedrock Agents.

        :return: The list of available bedrock agents.
        """

        try:
            all_agents = []

            paginator = self.client.get_paginator("list_agents")
            for page in paginator.paginate(PaginationConfig={"PageSize": 10}):
                all_agents.extend(page["agentSummaries"])

        except ClientError as e:
            logger.error(f"Couldn't list agents. {e}")
            raise
        else:
            return all_agents
```
+  For API details, see [ListAgents](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/ListAgents) in *AWS SDK for Python (Boto3) API Reference*.

### `ListFlowAliases`
<a name="bedrock-agent_ListFlowAliases_python_3_topic"></a>

The following code example shows how to use `ListFlowAliases`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
List the aliases for an Amazon Bedrock flow.

```
def list_flow_aliases(client, flow_id):
    """
    Lists the aliases of an Amazon Bedrock flow.

    Args:
        client: bedrock agent boto3 client.
        flow_id (str): The identifier of the flow.

    Returns:
        dict: The response from ListFlowAliases.
    """
    try:

        finished = False

        logger.info("Listing flow aliases for flow: %s.", flow_id)

        print(f"Aliases for flow: {flow_id}")

        response = client.list_flow_aliases(
            flowIdentifier=flow_id,
            maxResults=10)

        while finished is False:

            for alias in response['flowAliasSummaries']:
                print(f"Alias Name: {alias['name']}")
                print(f"ID: {alias['id']}")
                print(f"Description: {alias.get('description', 'No description')}\n")

                if 'nextToken' in response:
                    next_token = response['nextToken']
                    response = client.list_flow_aliases(maxResults=10,
                                                nextToken=next_token)
                else:
                    finished = True

        logging.info("Successfully listed flow aliases for flow %s.",
                flow_id)

        return response

    except ClientError as e:
        logging.exception("Client error listing flow aliases: %s", str(e))
        raise
    except Exception as e:
        logging.exception("Unexpected error listing flow aliases: %s", str(e))
        raise
```
+  For API details, see [ListFlowAliases](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/ListFlowAliases) in *AWS SDK for Python (Boto3) API Reference*.

### `ListFlowVersions`
<a name="bedrock-agent_ListFlowVersions_python_3_topic"></a>

The following code example shows how to use `ListFlowVersions`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
List the versions of an Amazon Bedrock flow.

```
def list_flow_versions(client, flow_id):
    """
    Lists the versions of an Amazon Bedrock flow.

    Args:
        client: Amazon bedrock agent boto3 client.
        flow_id (str): The identifier of the flow.

    Returns:
        dict: The response from ListFlowVersions.
    """
    try:

        finished = False

        logger.info("Listing flow versions for flow: %s.", flow_id)

        response = client.list_flow_versions(
            flowIdentifier=flow_id,
            maxResults=10)

        while finished is False:

            print(f"Versions for flow:{flow_id}")
            for version in response['flowVersionSummaries']:
                print(f"Version: {version['version']}")
                print(f"Status: {version['status']}\n")

                if 'nextToken' in response:
                    next_token = response['nextToken']
                    response = client.list_flow_versions(maxResults=10,
                                                nextToken=next_token)
                else:
                    finished = True

        logging.info("Successfully listed flow versions for flow %s.",
                flow_id)

        return response

    except ClientError as e:
        logging.exception("Client error listing flow versions: %s", str(e))
        raise
    except Exception as e:
        logging.exception("Unexpected error listing flow versions: %s", str(e))
        raise
```
+  For API details, see [ListFlowVersions](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/ListFlowVersions) in *AWS SDK for Python (Boto3) API Reference*.

### `ListFlows`
<a name="bedrock-agent_ListFlows_python_3_topic"></a>

The following code example shows how to use `ListFlows`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
List Amazon Bedrock flows.

```
def list_flows(client):
    """
    Lists versions of an Amazon Bedrock flow.

    Args:
        client: Amazon Bedrock agent boto3 client.
        flow_id (str): The identifier of the flow.

    Returns:
        Nothing.
    """
    try:
        finished = False

        logger.info("Listing flows:")

        response = client.list_flows(maxResults=10)

        while finished is False:

            for flow in response['flowSummaries']:
                print(f"ID: {flow['id']}")
                print(f"Name: {flow['name']}")
                print(
                    f"Description: {flow.get('description', 'No description')}")
                print(f"Latest version: {flow['version']}")
                print(f"Status: {flow['status']}\n")

            if 'nextToken' in response:
                next_token = response['nextToken']
                response = client.list_flows(maxResults=10,
                                             nextToken=next_token)
            else:
                finished = True

        logging.info("Successfully listed flows.")

    except ClientError as e:
        logging.exception("Client error listing flow versions: %s", str(e))
        raise
    except Exception as e:
        logging.exception("Unexpected error listing flow versions: %s", str(e))
        raise
```
+  For API details, see [ListFlows](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/ListFlows) in *AWS SDK for Python (Boto3) API Reference*.

### `ListKnowledgeBases`
<a name="bedrock-agent_ListKnowledgeBases_python_3_topic"></a>

The following code example shows how to use `ListKnowledgeBases`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
List Amazon Bedrock knowledge Bases.

```
def list_knowledge_bases(bedrock_agent_client, max_results=None):
    """
    Lists the knowledge bases in your AWS account.

    Args:
        bedrock_agent_client: The Boto3 Bedrock Agent client.
        max_results (int, optional): The maximum number of knowledge bases to return.

    Returns:
        list: A list of knowledge base details.
    """
    try:
        kwargs = {}
        if max_results is not None:
            kwargs["maxResults"] = max_results

        # Initialize an empty list to store all knowledge bases
        all_knowledge_bases = []

        # Use paginator to handle pagination automatically
        paginator = bedrock_agent_client.get_paginator('list_knowledge_bases')
        page_iterator = paginator.paginate(**kwargs)

        # Iterate through each page of results
        for page in page_iterator:
            all_knowledge_bases.extend(page.get('knowledgeBaseSummaries', []))

        logger.info("Found %s knowledge bases.", len(all_knowledge_bases))
        return all_knowledge_bases
    except ClientError as err:
        logger.error(
            "Couldn't list knowledge bases. Here's why: %s: %s",
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise
```
+  For API details, see [ListKnowledgeBases](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/ListKnowledgeBases) in *AWS SDK for Python (Boto3) API Reference*.

### `ListPrompts`
<a name="bedrock-agent_ListPrompts_python_3_topic"></a>

The following code example shows how to use `ListPrompts`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
List Amazon Bedrock managed prompts.

```
def list_prompts(client, max_results=10):
    """
    Lists Amazon Bedrock managed prompts.

    Args:
        client: Amazon Bedrock Agent boto3 client.
        max_results (int): Maximum number of results to return per page.

    Returns:
        list: A list of prompt summaries.
    """
    try:
        logger.info("Listing prompts:")

        # Create a paginator for the list_prompts operation
        paginator = client.get_paginator('list_prompts')

        # Create the pagination parameters
        pagination_config = {
            'maxResults': max_results
        }

        # Initialize an empty list to store all prompts
        all_prompts = []

        # Iterate through all pages
        for page in paginator.paginate(**pagination_config):
            all_prompts.extend(page.get('promptSummaries', []))

        logger.info("Successfully listed %s prompts.", len(all_prompts))
        return all_prompts

    except ClientError as e:
        logger.exception("Client error listing prompts: %s", str(e))
        raise
    except Exception as e:
        logger.exception("Unexpected error listing prompts: %s", str(e))
        raise
```
+  For API details, see [ListPrompts](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/ListPrompts) in *AWS SDK for Python (Boto3) API Reference*.

### `PrepareAgent`
<a name="bedrock-agent_PrepareAgent_python_3_topic"></a>

The following code example shows how to use `PrepareAgent`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Prepare an agent for internal testing.

```
    def prepare_agent(self, agent_id):
        """
        Creates a DRAFT version of the agent that can be used for internal testing.

        :param agent_id: The unique identifier of the agent to prepare.
        :return: The response from Amazon Bedrock Agents if successful, otherwise raises an exception.
        """
        try:
            prepared_agent_details = self.client.prepare_agent(agentId=agent_id)
        except ClientError as e:
            logger.error(f"Couldn't prepare agent. {e}")
            raise
        else:
            return prepared_agent_details
```
+  For API details, see [PrepareAgent](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/PrepareAgent) in *AWS SDK for Python (Boto3) API Reference*.

### `PrepareFlow`
<a name="bedrock-agent_PrepareFlow_python_3_topic"></a>

The following code example shows how to use `PrepareFlow`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Prepare an Amazon Bedrock flow.

```
def prepare_flow(client, flow_id):
    """
    Prepares an Amazon Bedrock Flow.

    Args:
        client: Amazon Bedrock agent boto3 client.
        flow_id (str): The identifier of the flow that you want to prepare.

    Returns:
        str: The status of the flow preparation
    """
    try:

        # Prepare the flow.
        logger.info("Preparing flow ID: %s",
                    flow_id)

        response = client.prepare_flow(
            flowIdentifier=flow_id
        )

        status = response.get('status')

        while status == "Preparing":
            logger.info("Preparing flow ID: %s. Status %s",
                        flow_id, status)

            sleep(5)
            response = client.get_flow(
                flowIdentifier=flow_id
            )
            status = response.get('status')
            print(f"Flow Status: {status}")

        if status == "Prepared":
            logger.info("Finished preparing flow ID: %s. Status %s",
                        flow_id, status)
        else:
            logger.warning("flow ID: %s not prepared. Status %s",
                           flow_id, status)

        return status

    except ClientError as e:
        logger.exception("Client error preparing flow: %s", {str(e)})
        raise

    except Exception as e:
        logger.exception("Unexepcted error preparing flow: %s", {str(e)})
        raise
```
+  For API details, see [PrepareFlow](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/PrepareFlow) in *AWS SDK for Python (Boto3) API Reference*.

### `UpdateFlow`
<a name="bedrock-agent_UpdateFlow_python_3_topic"></a>

The following code example shows how to use `UpdateFlow`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Update an Amazon Bedrock Flow.

```
def update_flow(client, flow_id, flow_name, flow_description, role_arn, flow_def):
    """
    Updates an Amazon Bedrock flow.

    Args:
    client: bedrock agent boto3 client.
    flow_id (str): The ID for the flow that you want to update.
    flow_name (str): The name for the flow.
    role_arn (str):  The ARN for the IAM role that use flow uses.
    flow_def (json): The JSON definition of the flow that you want to create.

    Returns:
        dict: Flow information if successful.
    """
    try:

        logger.info("Updating flow: %s.", flow_id)

        response = client.update_flow(
            flowIdentifier=flow_id,
            name=flow_name,
            description=flow_description,
            executionRoleArn=role_arn,
            definition=flow_def
        )

        logger.info("Successfully updated flow: %s. ID: %s",
                    flow_name,
                    {response['id']})

        return response

    except ClientError as e:
        logger.exception("Client error updating flow: %s", {str(e)})
        raise

    except Exception as e:
        logger.exception("Unexepcted error updating flow: %s", {str(e)})
        raise
```
+  For API details, see [UpdateFlow](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/UpdateFlow) in *AWS SDK for Python (Boto3) API Reference*.

### `UpdateFlowAlias`
<a name="bedrock-agent_UpdateFlowAlias_python_3_topic"></a>

The following code example shows how to use `UpdateFlowAlias`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Update an alias for an Amazon Bedrock flow.

```
def update_flow_alias(client, flow_id, alias_id, flow_version, name, description):
    """
    Updates an alias for an Amazon Bedrock flow.

    Args:
        client: bedrock agent boto3 client.
        flow_id (str): The identifier of the flow.

    Returns:
        str: The response from UpdateFlowAlias.
    """

    try:
        logger.info("Updating flow alias %s for flow: %s.", alias_id, flow_id)

        response = client.update_flow_alias(
            aliasIdentifier=alias_id,
            flowIdentifier=flow_id,
            name=name,
            description=description,
            routingConfiguration=[
                {
                    "flowVersion": flow_version
                }
            ]
        )
        logger.info("Successfully updated flow alias %s for %s.", alias_id, flow_id)

        return response

    except ClientError as e:
        logging.exception("Client error updating alias %s for flow: %s - %s",
                alias_id, flow_id, str(e))
        raise
    except Exception as e:
        logging.exception("Unexpected error updating alias %s for flow : %s - %s",
                alias_id, flow_id, str(e))
        raise
```
+  For API details, see [UpdateFlowAlias](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/UpdateFlowAlias) in *AWS SDK for Python (Boto3) API Reference*.

### `UpdateKnowledgeBase`
<a name="bedrock-agent_UpdateKnowledgeBase_python_3_topic"></a>

The following code example shows how to use `UpdateKnowledgeBase`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Update an Amazon Bedrock knowledge base.

```
def update_knowledge_base(bedrock_agent_client, knowledge_base_id, name=None, description=None, role_arn=None):
    """
    Updates an existing knowledge base.

    Args:
        bedrock_agent_client: The Boto3 Bedrock Agent client.
        knowledge_base_id (str): The ID of the knowledge base to update.
        name (str, optional): The new name for the knowledge base.
        description (str, optional): The new description for the knowledge base.
        role_arn (str, optional): The new IAM role ARN for the knowledge base.

    Returns:
        dict: The details of the updated knowledge base.
    """
    try:
        kwargs = {
            "knowledgeBaseId": knowledge_base_id,
            "knowledgeBaseConfiguration": {
                "type": "VECTOR",
                "vectorKnowledgeBaseConfiguration": {
                    "embeddingModelArn": "arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1"
                }
            }
        }

        if name:
            kwargs["name"] = name
        if description:
            kwargs["description"] = description
        if role_arn:
            kwargs["roleArn"] = role_arn

        response = bedrock_agent_client.update_knowledge_base(**kwargs)

        logger.info("Updated knowledge base: %s", knowledge_base_id)
        return response["knowledgeBase"]

    except ClientError as err:
        logger.error(
            "Couldn't update knowledge base %s. Here's why: %s: %s",
            knowledge_base_id,
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise
```
+  For API details, see [UpdateKnowledgeBase](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/UpdateKnowledgeBase) in *AWS SDK for Python (Boto3) API Reference*.

## Scenarios
<a name="scenarios"></a>

### Create and invoke a flow
<a name="bedrock-agent_GettingStartedWithBedrockFlows_python_3_topic"></a>

The following code example shows how to:
+ Create an execution role for the flow.
+ Create the flow.
+ Deploy the fully configured flow.
+ Invoke the flow with user-provided prompts.
+ Delete all created resources.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Generates a music playlist based on user-specified genre and number of songs.

```
from datetime import datetime
import logging
import boto3

from botocore.exceptions import ClientError

from roles import create_flow_role, delete_flow_role, update_role_policy
from flow import create_flow, prepare_flow, delete_flow
from run_flow import run_playlist_flow
from flow_version import create_flow_version, delete_flow_version
from flow_alias import create_flow_alias, delete_flow_alias

logging.basicConfig(
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def create_input_node(name):
    """
    Creates an input node configuration for an Amazon Bedrock flow.

    The input node serves as the entry point for the flow and defines
    the initial document structure that will be passed to subsequent nodes.

    Args:
        name (str): The name of the input node.

    Returns:
        dict: The input node configuration.

    """
    return {
        "type": "Input",
        "name": name,
        "outputs": [
            {
                "name": "document",
                "type": "Object"
            }
        ]
    }

def create_prompt_node(name, model_id):
    """
    Creates a prompt node configuration for a Bedrock flow that generates music playlists.

    The prompt node defines an inline prompt template that creates a music playlist based on
    a specified genre and number of songs. The prompt uses two variables that are mapped from
    the input JSON object:
    - {{genre}}: The genre of music to create a playlist for
    - {{number}}: The number of songs to include in the playlist

    Args:
        name (str): The name of the prompt node.
        model_id (str): The identifier of the foundation model to use for the prompt.

    Returns:
        dict: The prompt node.

    """

    return {
        "type": "Prompt",
        "name": name,
        "configuration": {
            "prompt": {
                "sourceConfiguration": {
                    "inline": {
                        "modelId": model_id,
                        "templateType": "TEXT",
                        "inferenceConfiguration": {
                            "text": {
                                "temperature": 0.8
                            }
                        },
                        "templateConfiguration": {
                            "text": {
                                "text": "Make me a {{genre}} playlist consisting of the following number of songs: {{number}}."
                            }
                        }
                    }
                }
            }
        },
        "inputs": [
            {
                "name": "genre",
                "type": "String",
                "expression": "$.data.genre"
            },
            {
                "name": "number",
                "type": "Number",
                "expression": "$.data.number"
            }
        ],
        "outputs": [
            {
                "name": "modelCompletion",
                "type": "String"
            }
        ]
    }

def create_output_node(name):
    """
    Creates an output node configuration for a Bedrock flow.

    The output node validates that the output from the last node is a string
    and returns it unmodified. The input name must be "document".

    Args:
        name (str): The name of the output node.

    Returns:
        dict: The output node configuration containing the output node:

    """

    return {
        "type": "Output",
        "name": name,
        "inputs": [
            {
                "name": "document",
                "type": "String",
                "expression": "$.data"
            }
        ]
    }

def create_playlist_flow(client, flow_name, flow_description, role_arn, prompt_model_id):
    """
    Creates the playlist generator flow.
    Args:
        client: bedrock agent boto3 client.
        role_arn (str): Name for the new IAM role.
        prompt_model_id (str): The id of the model to use in the prompt node.
    Returns:
        dict: The response from the create_flow operation.
    """

    input_node = create_input_node("FlowInput")
    prompt_node = create_prompt_node("MakePlaylist", prompt_model_id)
    output_node = create_output_node("FlowOutput")

    # Create connections between the nodes
    connections = []

    #  First, create connections between the output of the flow
    # input node and each input of the prompt node.
    for prompt_node_input in prompt_node["inputs"]:
        connections.append(
            {
                "name": "_".join([input_node["name"], prompt_node["name"],
                                   prompt_node_input["name"]]),
                "source": input_node["name"],
                "target": prompt_node["name"],
                "type": "Data",
                "configuration": {
                    "data": {
                        "sourceOutput": input_node["outputs"][0]["name"],
                        "targetInput": prompt_node_input["name"]
                    }
                }
            }
        )

    # Then, create a connection between the output of the prompt node and the input of the flow output node
    connections.append(
        {
            "name": "_".join([prompt_node["name"], output_node["name"]]),
            "source": prompt_node["name"],
            "target": output_node["name"],
            "type": "Data",
            "configuration": {
                "data": {
                    "sourceOutput": prompt_node["outputs"][0]["name"],
                    "targetInput": output_node["inputs"][0]["name"]
                }
            }
        }
    )

    flow_def = {
        "nodes": [input_node, prompt_node, output_node],
        "connections": connections
    }

    # Create the flow.

    response = create_flow(
        client, flow_name, flow_description, role_arn, flow_def)

    return response

def get_model_arn(client, model_id):
    """
    Gets the Amazon Resource Name (ARN) for a model.
    Args:
        client (str): Amazon Bedrock boto3 client.
        model_id (str): The id of the model.
    Returns:
        str: The ARN of the model.
    """

    try:
        # Call GetFoundationModelDetails operation
        response = client.get_foundation_model(modelIdentifier=model_id)

        # Extract model ARN from the response
        model_arn = response['modelDetails']['modelArn']

        return model_arn

    except ClientError as e:
        logger.exception("Client error getting model ARN: %s", {str(e)})
        raise

    except Exception as e:
        logger.exception("Unexpected error getting model ARN: %s", {str(e)})
        raise

def prepare_flow_version_and_alias(bedrock_agent_client,
                                   flow_id):
    """
    Prepares the flow and then creates a flow version and flow alias.
    Args:
        bedrock_agent_client: Amazon Bedrock Agent boto3 client.
        flowd_id (str): The ID of the flow that you want to prepare.
    Returns: The flow_version and flow_alias.

    """

    status = prepare_flow(bedrock_agent_client, flow_id)

    flow_version = None
    flow_alias = None

    if status == 'Prepared':

        # Create the flow version and alias.
        flow_version = create_flow_version(bedrock_agent_client,
                                           flow_id,
                                           f"flow version for flow {flow_id}.")

        flow_alias = create_flow_alias(bedrock_agent_client,
                                       flow_id,
                                       flow_version,
                                       "latest",
                                       f"Alias for flow {flow_id}, version {flow_version}")

    return flow_version, flow_alias

def delete_role_resources(bedrock_agent_client,
                          iam_client,
                          role_name,
                          flow_id,
                          flow_version,
                          flow_alias):
    """
    Deletes the flow, flow alias, flow version, and IAM roles.
    Args:
        bedrock_agent_client: Amazon Bedrock Agent boto3 client.
        iam_client: Amazon IAM boto3 client.
        role_name (str): The name of the IAM role.
        flow_id (str): The id of the flow.
        flow_version (str): The version of the flow.
        flow_alias (str): The alias of the flow.
    """

    if flow_id is not None:
        if flow_alias is not None:
            delete_flow_alias(bedrock_agent_client, flow_id, flow_alias)
        if flow_version is not None:
            delete_flow_version(bedrock_agent_client,
                        flow_id, flow_version)
        delete_flow(bedrock_agent_client, flow_id)

    if role_name is not None:
        delete_flow_role(iam_client, role_name)

def main():
    """
    Creates, runs, and optionally deletes a Bedrock flow for generating music playlists.

    Note:
        Requires valid AWS credentials in the default profile
    """

    delete_choice = "y"
    try:

        # Get various boto3 clients.
        session = boto3.Session(profile_name='default')
        bedrock_agent_runtime_client = session.client('bedrock-agent-runtime')
        bedrock_agent_client = session.client('bedrock-agent')
        bedrock_client = session.client('bedrock')
        iam_client = session.client('iam')

        role_name = None
        flow_id = None
        flow_version = None
        flow_alias = None

        #Change the model as needed.
        prompt_model_id = "amazon.nova-pro-v1:0"

        # Base the flow name on the current date and time
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d-%H-%M-%S")
        flow_name = f"FlowPlayList_{timestamp}"
        flow_description = "A flow to generate a music playlist."

        # Create a role for the flow.
        role_name = f"BedrockFlowRole-{flow_name}"
        role = create_flow_role(iam_client, role_name)
        role_arn = role['Arn']

        # Create the flow.
        response = create_playlist_flow(
            bedrock_agent_client, flow_name, flow_description, role_arn, prompt_model_id)
        flow_id = response.get('id')

        if flow_id:
            # Update accessible resources in the role.
            model_arn = get_model_arn(bedrock_client, prompt_model_id)
            update_role_policy(iam_client, role_name, [
                               response.get('arn'), model_arn])

            # Prepare the flow and flow version.
            flow_version, flow_alias = prepare_flow_version_and_alias(
                bedrock_agent_client, flow_id)

            # Run the flow.
            if flow_version and flow_alias:
                run_playlist_flow(bedrock_agent_runtime_client,
                                  flow_id, flow_alias)

                delete_choice = input("Delete flow? y or n : ").lower()

            else:
                print("Couldn't run. Deleting flow and role.")
                delete_flow(bedrock_agent_client, flow_id)
                delete_flow_role(iam_client, role_name)
        else:
            print("Couldn't create flow.")

    except Exception as e:
        print(f"Fatal error: {str(e)}")

    finally:
        if delete_choice == 'y':
                delete_role_resources(bedrock_agent_client,
                                          iam_client,
                                          role_name,
                                          flow_id,
                                          flow_version,
                                          flow_alias)
        else:
            print("Flow not deleted. ")
            print(f"\tFlow ID: {flow_id}")
            print(f"\tFlow version: {flow_version}")
            print(f"\tFlow alias: {flow_alias}")
            print(f"\tRole ARN: {role_arn}")

        print("Done!")

if __name__ == "__main__":
    main()

def invoke_flow(client, flow_id, flow_alias_id, input_data):
    """
    Invoke an Amazon Bedrock flow and handle the response stream.

    Args:
        client: Boto3 client for Amazon Bedrock agent runtime.
        flow_id: The ID of the flow to invoke.
        flow_alias_id: The alias ID of the flow.
        input_data: Input data for the flow.

    Returns:
        Dict containing flow status and flow output.
    """

    response = None
    request_params = None

    request_params = {
            "flowIdentifier": flow_id,
            "flowAliasIdentifier": flow_alias_id,
            "inputs": [input_data],
            "enableTrace": True
        }

    response = client.invoke_flow(**request_params)

    flow_status = ""
    output= ""

    # Process the streaming response
    for event in response['responseStream']:

        # Check if flow is complete.
        if 'flowCompletionEvent' in event:
            flow_status = event['flowCompletionEvent']['completionReason']

        # Save the model output.
        elif 'flowOutputEvent' in event:
            output = event['flowOutputEvent']['content']['document']
            logger.info("Output : %s", output)

        # Log trace events.
        elif 'flowTraceEvent' in event:
            logger.info("Flow trace:  %s", event['flowTraceEvent'])

    return {
        "flow_status": flow_status,
        "output": output

    }

def run_playlist_flow(bedrock_agent_client, flow_id, flow_alias_id):
    """
    Runs the playlist generator flow.

    Args:
        bedrock_agent_client: Boto3 client for Amazon Bedrock agent runtime.
        flow_id: The ID of the flow to run.
        flow_alias_id: The alias ID of the flow.

    """

    print ("Welcome to the playlist generator flow.")
    # Get the initial prompt from the user.
    genre = input("Enter genre: ")
    number_of_songs = int(input("Enter number of songs: "))

    # Use prompt to create input data for the input node.
    flow_input_data = {
        "content": {
            "document": {
                "genre" : genre,
                "number" : number_of_songs
            }
        },
        "nodeName": "FlowInput",
        "nodeOutputName": "document"
    }

    try:

        result = invoke_flow(
                bedrock_agent_client, flow_id, flow_alias_id, flow_input_data)

        status = result['flow_status']

        if status == "SUCCESS":
                # The flow completed successfully.
                logger.info("The flow %s successfully completed.", flow_id)
                print(result['output'])
        else:
            logger.warning("Flow status: %s",status)

    except ClientError as e:
        print(f"Client error: {str(e)}")
        logger.error("Client error: %s", {str(e)})
        raise

    except Exception as e:
        logger.error("An error occurred: %s", {str(e)})
        logger.error("Error type: %s", {type(e)})
        raise

def create_flow_role(client, role_name):
    """
    Creates an IAM role for Amazon Bedrock with permissions to run a flow.

    Args:
        role_name (str): Name for the new IAM role.
    Returns:
        str: The role Amazon Resource Name.
    """

    # Trust relationship policy - allows Amazon Bedrock service to assume this role.
    trust_policy = {
        "Version":"2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {
                "Service": "bedrock.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }]
    }

    # Basic inline policy for for running a flow.

    resources = "*"

    bedrock_policy = {
        "Version":"2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "bedrock:InvokeModel",
                    "bedrock:Retrieve",
                    "bedrock:RetrieveAndGenerate"
                ],
                # Using * as placeholder - Later you update with specific ARNs.
                "Resource": resources
            }
        ]
    }

    try:
        # Create the IAM role with trust policy
        logging.info("Creating role: %s",role_name)
        role = client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description="Role for Amazon Bedrock operations"
        )

        # Attach inline policy to the role
        print("Attaching inline policy")
        client.put_role_policy(
            RoleName=role_name,
            PolicyName=f"{role_name}-policy",
            PolicyDocument=json.dumps(bedrock_policy)
        )

        logging.info("Create Role ARN: %s", role['Role']['Arn'])
        return role['Role']

    except ClientError as e:
        logging.warning("Error creating role: %s", str(e))
        raise
    except Exception as e:
        logging.warning("Unexpected error: %s", str(e))
        raise

def update_role_policy(client, role_name, resource_arns):
    """
    Updates an IAM role's inline policy with specific resource ARNs.

    Args:
        role_name (str): Name of the existing role.
        resource_arns (list): List of resource ARNs to allow access to.
    """

    updated_policy = {
        "Version":"2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "bedrock:GetFlow",
                    "bedrock:InvokeModel",
                    "bedrock:Retrieve",
                    "bedrock:RetrieveAndGenerate"
                ],
                "Resource": resource_arns
            }
        ]
    }

    try:
        client.put_role_policy(
            RoleName=role_name,
            PolicyName=f"{role_name}-policy",
            PolicyDocument=json.dumps(updated_policy)
        )
        logging.info("Updated policy for role: %s",role_name)

    except ClientError as e:
        logging.warning("Error updating role policy: %s", str(e))
        raise

def delete_flow_role(client, role_name):
    """
    Deletes an IAM role.

    Args:
        role_name (str): Name of the role to delete.
    """

    try:
        # Detach and delete inline policies
        policies = client.list_role_policies(RoleName=role_name)['PolicyNames']
        for policy_name in policies:
            client.delete_role_policy(RoleName=role_name, PolicyName=policy_name)

        # Delete the role
        client.delete_role(RoleName=role_name)
        logging.info("Deleted role: %s", role_name)

    except ClientError as e:
        logging.info("Error Deleting role: %s", str(e))
        raise
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CreateFlow](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateFlow)
  + [CreateFlowAlias](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateFlowAlias)
  + [CreateFlowVersion](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateFlowVersion)
  + [DeleteFlow](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeleteFlow)
  + [DeleteFlowAlias](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeleteFlowAlias)
  + [DeleteFlowVersion](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeleteFlowVersion)
  + [GetFlow](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/GetFlow)
  + [GetFlowAlias](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/GetFlowAlias)
  + [GetFlowVersion](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/GetFlowVersion)
  + [InvokeFlow](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-12-12/InvokeFlow)
  + [PrepareFlow](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/PrepareFlow)

### Create and invoke a managed prompt
<a name="bedrock-agent_GettingStartedWithBedrockPrompts_python_3_topic"></a>

The following code example shows how to:
+ Create a managed prompt.
+ Create a version of the prompt.
+ Invoke the prompt using the version.
+ Clean up resources (optional).

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create and invoke a managed prompt.

```
import argparse
import boto3
import logging
import time

# Now import the modules
from prompt import create_prompt, create_prompt_version, delete_prompt
from run_prompt import invoke_prompt

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

def run_scenario(bedrock_client, bedrock_runtime_client, model_id, cleanup=True):
    """
    Runs the Amazon Bedrock managed prompt scenario.

    Args:
        bedrock_client: The Amazon Bedrock Agent client.
        bedrock_runtime_client: The Amazon Bedrock Runtime client.
        model_id (str): The model ID to use for the prompt.
        cleanup (bool): Whether to clean up resources at the end of the scenario.

    Returns:
        dict: A dictionary containing the created resources.
    """
    prompt_id = None

    try:
        # Step 1: Create a prompt
        print("\n=== Step 1: Creating a prompt ===")
        prompt_name = f"PlaylistGenerator-{int(time.time())}"
        prompt_description = "Playlist generator"
        prompt_template = """
          Make me a {{genre}} playlist consisting of the following number of songs: {{number}}."""

        create_response = create_prompt(
            bedrock_client,
            prompt_name,
            prompt_description,
            prompt_template,
            model_id
        )

        prompt_id = create_response['id']
        print(f"Created prompt: {prompt_name} with ID: {prompt_id}")

        # Create a version of the prompt
        print("\n=== Creating a version of the prompt ===")
        version_response = create_prompt_version(
            bedrock_client,
            prompt_id,
            description="Initial version of the product description generator"
        )

        prompt_version_arn = version_response['arn']
        prompt_version = version_response['version']

        print(f"Created prompt version: {prompt_version}")
        print(f"Prompt version ARN: {prompt_version_arn}")

        # Step 2: Invoke the prompt directly
        print("\n=== Step 2: Invoking the prompt ===")
        input_variables = {
            "genre": "pop",
            "number": "2",
           }

        # Use the ARN from the create_prompt_version response
        result = invoke_prompt(
            bedrock_runtime_client,
            prompt_version_arn,
            input_variables
        )
        # Display the playlist
        print(f"\n{result}")

        # Step 3: Clean up resources (optional)
        if cleanup:
            print("\n=== Step 3: Cleaning up resources ===")

            # Delete the prompt
            print(f"Deleting prompt {prompt_id}...")
            delete_prompt(bedrock_client, prompt_id)

            print("Cleanup complete")
        else:
            print("\n=== Resources were not cleaned up ===")
            print(f"Prompt ID: {prompt_id}")

    except Exception as e:
        logger.exception("Error in scenario: %s", str(e))

        # Attempt to clean up if an error occurred and cleanup was requested
        if cleanup and prompt_id:
            try:
                print("\nCleaning up resources after error...")

                # Delete the prompt
                try:
                    delete_prompt(bedrock_client, prompt_id)
                    print("Cleanup after error complete")
                except Exception as cleanup_error:
                    logger.error("Error during cleanup: %s", str(cleanup_error))
            except Exception as final_error:
                logger.error("Final error during cleanup: %s", str(final_error))

        # Re-raise the original exception
        raise

def main():
    """
    Entry point for the Amazon Bedrock managed prompt scenario.
    """
    parser = argparse.ArgumentParser(
        description="Run the Amazon Bedrock managed prompt scenario."
    )
    parser.add_argument(
        '--region',
        default='us-east-1',
        help="The AWS Region to use."
    )
    parser.add_argument(
        '--model-id',
        default='anthropic.claude-v2',
        help="The model ID to use for the prompt."
    )
    parser.add_argument(
        '--cleanup',
        action='store_true',
        default=True,
        help="Clean up resources at the end of the scenario."
    )
    parser.add_argument(
        '--no-cleanup',
        action='store_false',
        dest='cleanup',
        help="Don't clean up resources at the end of the scenario."
    )
    args = parser.parse_args()

    bedrock_client = boto3.client('bedrock-agent', region_name=args.region)
    bedrock_runtime_client = boto3.client('bedrock-runtime', region_name=args.region)

    print("=== Amazon Bedrock Managed Prompt Scenario ===")
    print(f"Region: {args.region}")
    print(f"Model ID: {args.model_id}")
    print(f"Cleanup resources: {args.cleanup}")

    try:
        run_scenario(
            bedrock_client,
            bedrock_runtime_client,
            args.model_id,
            args.cleanup
        )

    except Exception as e:
        logger.exception("Error running scenario: %s", str(e))

if __name__ == "__main__":
    main()
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse)
  + [CreatePrompt](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreatePrompt)
  + [CreatePromptVersion](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreatePromptVersion)
  + [DeletePrompt](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeletePrompt)

### Create and invoke an agent
<a name="bedrock-agent_GettingStartedWithBedrockAgents_python_3_topic"></a>

The following code example shows how to:
+ Create an execution role for the agent.
+ Create the agent and deploy a DRAFT version.
+ Create a Lambda function that implements the agent's capabilities.
+ Create an action group that connects the agent to the Lambda function.
+ Deploy the fully configured agent.
+ Invoke the agent with user-provided prompts.
+ Delete all created resources.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create and invoke an agent.

```
REGION = "us-east-1"
ROLE_POLICY_NAME = "agent_permissions"

class BedrockAgentScenarioWrapper:
    """Runs a scenario that shows how to get started using Amazon Bedrock Agents."""

    def __init__(
            self, bedrock_agent_client, runtime_client, lambda_client, iam_resource, postfix
    ):
        self.iam_resource = iam_resource
        self.lambda_client = lambda_client
        self.bedrock_agent_runtime_client = runtime_client
        self.postfix = postfix

        self.bedrock_wrapper = BedrockAgentWrapper(bedrock_agent_client)

        self.agent = None
        self.agent_alias = None
        self.agent_role = None
        self.prepared_agent_details = None
        self.lambda_role = None
        self.lambda_function = None

    def run_scenario(self):
        print("=" * 88)
        print("Welcome to the Amazon Bedrock Agents demo.")
        print("=" * 88)

        # Query input from user
        print("Let's start with creating an agent:")
        print("-" * 40)
        name, foundation_model = self._request_name_and_model_from_user()
        print("-" * 40)

        # Create an execution role for the agent
        self.agent_role = self._create_agent_role(foundation_model)

        # Create the agent
        self.agent = self._create_agent(name, foundation_model)

        # Prepare a DRAFT version of the agent
        self.prepared_agent_details = self._prepare_agent()

        # Create the agent's Lambda function
        self.lambda_function = self._create_lambda_function()

        # Configure permissions for the agent to invoke the Lambda function
        self._allow_agent_to_invoke_function()
        self._let_function_accept_invocations_from_agent()

        # Create an action group to connect the agent with the Lambda function
        self._create_agent_action_group()

        # If the agent has been modified or any components have been added, prepare the agent again
        components = [self._get_agent()]
        components += self._get_agent_action_groups()
        components += self._get_agent_knowledge_bases()

        latest_update = max(component["updatedAt"] for component in components)
        if latest_update > self.prepared_agent_details["preparedAt"]:
            self.prepared_agent_details = self._prepare_agent()

        # Create an agent alias
        self.agent_alias = self._create_agent_alias()

        # Test the agent
        self._chat_with_agent(self.agent_alias)

        print("=" * 88)
        print("Thanks for running the demo!\n")

        if q.ask("Do you want to delete the created resources? [y/N] ", q.is_yesno):
            self._delete_resources()
            print("=" * 88)
            print(
                "All demo resources have been deleted. Thanks again for running the demo!"
            )
        else:
            self._list_resources()
            print("=" * 88)
            print("Thanks again for running the demo!")

    def _request_name_and_model_from_user(self):
        existing_agent_names = [
            agent["agentName"] for agent in self.bedrock_wrapper.list_agents()
        ]

        while True:
            name = q.ask("Enter an agent name: ", self.is_valid_agent_name)
            if name.lower() not in [n.lower() for n in existing_agent_names]:
                break
            print(
                f"Agent {name} conflicts with an existing agent. Please use a different name."
            )

        models = ["anthropic.claude-instant-v1", "anthropic.claude-v2"]
        model_id = models[
            q.choose("Which foundation model would you like to use? ", models)
        ]

        return name, model_id

    def _create_agent_role(self, model_id):
        role_name = f"AmazonBedrockExecutionRoleForAgents_{self.postfix}"
        model_arn = f"arn:aws:bedrock:{REGION}::foundation-model/{model_id}*"

        print("Creating an an execution role for the agent...")

        try:
            role = self.iam_resource.create_role(
                RoleName=role_name,
                AssumeRolePolicyDocument=json.dumps(
                    {
                        "Version":"2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Principal": {"Service": "bedrock.amazonaws.com"},
                                "Action": "sts:AssumeRole",
                            }
                        ],
                    }
                ),
            )

            role.Policy(ROLE_POLICY_NAME).put(
                PolicyDocument=json.dumps(
                    {
                        "Version":"2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Action": "bedrock:InvokeModel",
                                "Resource": model_arn,
                            }
                        ],
                    }
                )
            )
        except ClientError as e:
            logger.error(f"Couldn't create role {role_name}. Here's why: {e}")
            raise

        return role

    def _create_agent(self, name, model_id):
        print("Creating the agent...")

        instruction = """
            You are a friendly chat bot. You have access to a function called that returns
            information about the current date and time. When responding with date or time,
            please make sure to add the timezone UTC.
            """
        agent = self.bedrock_wrapper.create_agent(
            agent_name=name,
            foundation_model=model_id,
            instruction=instruction,
            role_arn=self.agent_role.arn,
        )
        self._wait_for_agent_status(agent["agentId"], "NOT_PREPARED")

        return agent

    def _prepare_agent(self):
        print("Preparing the agent...")

        agent_id = self.agent["agentId"]
        prepared_agent_details = self.bedrock_wrapper.prepare_agent(agent_id)
        self._wait_for_agent_status(agent_id, "PREPARED")

        return prepared_agent_details

    def _create_lambda_function(self):
        print("Creating the Lambda function...")

        function_name = f"AmazonBedrockExampleFunction_{self.postfix}"

        self.lambda_role = self._create_lambda_role()

        try:
            deployment_package = self._create_deployment_package(function_name)

            lambda_function = self.lambda_client.create_function(
                FunctionName=function_name,
                Description="Lambda function for Amazon Bedrock example",
                Runtime="python3.11",
                Role=self.lambda_role.arn,
                Handler=f"{function_name}.lambda_handler",
                Code={"ZipFile": deployment_package},
                Publish=True,
            )

            waiter = self.lambda_client.get_waiter("function_active_v2")
            waiter.wait(FunctionName=function_name)

        except ClientError as e:
            logger.error(
                f"Couldn't create Lambda function {function_name}. Here's why: {e}"
            )
            raise

        return lambda_function

    def _create_lambda_role(self):
        print("Creating an execution role for the Lambda function...")

        role_name = f"AmazonBedrockExecutionRoleForLambda_{self.postfix}"

        try:
            role = self.iam_resource.create_role(
                RoleName=role_name,
                AssumeRolePolicyDocument=json.dumps(
                    {
                        "Version":"2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Principal": {"Service": "lambda.amazonaws.com"},
                                "Action": "sts:AssumeRole",
                            }
                        ],
                    }
                ),
            )
            role.attach_policy(
                PolicyArn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
            )
            print(f"Created role {role_name}")
        except ClientError as e:
            logger.error(f"Couldn't create role {role_name}. Here's why: {e}")
            raise

        print("Waiting for the execution role to be fully propagated...")
        wait(10)

        return role

    def _allow_agent_to_invoke_function(self):
        policy = self.iam_resource.RolePolicy(
            self.agent_role.role_name, ROLE_POLICY_NAME
        )
        doc = policy.policy_document
        doc["Statement"].append(
            {
                "Effect": "Allow",
                "Action": "lambda:InvokeFunction",
                "Resource": self.lambda_function["FunctionArn"],
            }
        )
        self.agent_role.Policy(ROLE_POLICY_NAME).put(PolicyDocument=json.dumps(doc))

    def _let_function_accept_invocations_from_agent(self):
        try:
            self.lambda_client.add_permission(
                FunctionName=self.lambda_function["FunctionName"],
                SourceArn=self.agent["agentArn"],
                StatementId="BedrockAccess",
                Action="lambda:InvokeFunction",
                Principal="bedrock.amazonaws.com",
            )
        except ClientError as e:
            logger.error(
                f"Couldn't grant Bedrock permission to invoke the Lambda function. Here's why: {e}"
            )
            raise

    def _create_agent_action_group(self):
        print("Creating an action group for the agent...")

        try:
            with open("./scenario_resources/api_schema.yaml") as file:
                self.bedrock_wrapper.create_agent_action_group(
                    name="current_date_and_time",
                    description="Gets the current date and time.",
                    agent_id=self.agent["agentId"],
                    agent_version=self.prepared_agent_details["agentVersion"],
                    function_arn=self.lambda_function["FunctionArn"],
                    api_schema=json.dumps(yaml.safe_load(file)),
                )
        except ClientError as e:
            logger.error(f"Couldn't create agent action group. Here's why: {e}")
            raise

    def _get_agent(self):
        return self.bedrock_wrapper.get_agent(self.agent["agentId"])

    def _get_agent_action_groups(self):
        return self.bedrock_wrapper.list_agent_action_groups(
            self.agent["agentId"], self.prepared_agent_details["agentVersion"]
        )

    def _get_agent_knowledge_bases(self):
        return self.bedrock_wrapper.list_agent_knowledge_bases(
            self.agent["agentId"], self.prepared_agent_details["agentVersion"]
        )

    def _create_agent_alias(self):
        print("Creating an agent alias...")

        agent_alias_name = "test_agent_alias"
        agent_alias = self.bedrock_wrapper.create_agent_alias(
            agent_alias_name, self.agent["agentId"]
        )

        self._wait_for_agent_status(self.agent["agentId"], "PREPARED")

        return agent_alias

    def _wait_for_agent_status(self, agent_id, status):
        while self.bedrock_wrapper.get_agent(agent_id)["agentStatus"] != status:
            wait(2)

    def _chat_with_agent(self, agent_alias):
        print("-" * 88)
        print("The agent is ready to chat.")
        print("Try asking for the date or time. Type 'exit' to quit.")

        # Create a unique session ID for the conversation
        session_id = uuid.uuid4().hex

        while True:
            prompt = q.ask("Prompt: ", q.non_empty)

            if prompt == "exit":
                break

            response = asyncio.run(self._invoke_agent(agent_alias, prompt, session_id))

            print(f"Agent: {response}")

    async def _invoke_agent(self, agent_alias, prompt, session_id):
        response = self.bedrock_agent_runtime_client.invoke_agent(
            agentId=self.agent["agentId"],
            agentAliasId=agent_alias["agentAliasId"],
            sessionId=session_id,
            inputText=prompt,
        )

        completion = ""

        for event in response.get("completion"):
            chunk = event["chunk"]
            completion += chunk["bytes"].decode()

        return completion

    def _delete_resources(self):
        if self.agent:
            agent_id = self.agent["agentId"]

            if self.agent_alias:
                agent_alias_id = self.agent_alias["agentAliasId"]
                print("Deleting agent alias...")
                self.bedrock_wrapper.delete_agent_alias(agent_id, agent_alias_id)

            print("Deleting agent...")
            agent_status = self.bedrock_wrapper.delete_agent(agent_id)["agentStatus"]
            while agent_status == "DELETING":
                wait(5)
                try:
                    agent_status = self.bedrock_wrapper.get_agent(
                        agent_id, log_error=False
                    )["agentStatus"]
                except ClientError as err:
                    if err.response["Error"]["Code"] == "ResourceNotFoundException":
                        agent_status = "DELETED"

        if self.lambda_function:
            name = self.lambda_function["FunctionName"]
            print(f"Deleting function '{name}'...")
            self.lambda_client.delete_function(FunctionName=name)

        if self.agent_role:
            print(f"Deleting role '{self.agent_role.role_name}'...")
            self.agent_role.Policy(ROLE_POLICY_NAME).delete()
            self.agent_role.delete()

        if self.lambda_role:
            print(f"Deleting role '{self.lambda_role.role_name}'...")
            for policy in self.lambda_role.attached_policies.all():
                policy.detach_role(RoleName=self.lambda_role.role_name)
            self.lambda_role.delete()

    def _list_resources(self):
        print("-" * 40)
        print(f"Here is the list of created resources in '{REGION}'.")
        print("Make sure you delete them once you're done to avoid unnecessary costs.")
        if self.agent:
            print(f"Bedrock Agent:   {self.agent['agentName']}")
        if self.lambda_function:
            print(f"Lambda function: {self.lambda_function['FunctionName']}")
        if self.agent_role:
            print(f"IAM role:        {self.agent_role.role_name}")
        if self.lambda_role:
            print(f"IAM role:        {self.lambda_role.role_name}")

    @staticmethod
    def is_valid_agent_name(answer):
        valid_regex = r"^[a-zA-Z0-9_-]{1,100}$"
        return (
            answer
            if answer and len(answer) <= 100 and re.match(valid_regex, answer)
            else None,
            "I need a name for the agent, please. Valid characters are a-z, A-Z, 0-9, _ (underscore) and - (hyphen).",
        )

    @staticmethod
    def _create_deployment_package(function_name):
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as zipped:
            zipped.write(
                "./scenario_resources/lambda_function.py", f"{function_name}.py"
            )
        buffer.seek(0)
        return buffer.read()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    postfix = "".join(
        random.choice(string.ascii_lowercase + "0123456789") for _ in range(8)
    )
    scenario = BedrockAgentScenarioWrapper(
        bedrock_agent_client=boto3.client(
            service_name="bedrock-agent", region_name=REGION
        ),
        runtime_client=boto3.client(
            service_name="bedrock-agent-runtime", region_name=REGION
        ),
        lambda_client=boto3.client(service_name="lambda", region_name=REGION),
        iam_resource=boto3.resource("iam"),
        postfix=postfix,
    )
    try:
        scenario.run_scenario()
    except Exception as e:
        logging.exception(f"Something went wrong with the demo. Here's what: {e}")
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CreateAgent](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateAgent)
  + [CreateAgentActionGroup](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateAgentActionGroup)
  + [CreateAgentAlias](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreateAgentAlias)
  + [DeleteAgent](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeleteAgent)
  + [DeleteAgentAlias](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeleteAgentAlias)
  + [GetAgent](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/GetAgent)
  + [ListAgentActionGroups](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/ListAgentActionGroups)
  + [ListAgentKnowledgeBases](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/ListAgentKnowledgeBases)
  + [ListAgents](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/ListAgents)
  + [PrepareAgent](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/PrepareAgent)

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
