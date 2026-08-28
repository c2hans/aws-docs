---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_GetPrompt_section.html
---

# Use `GetPrompt` with an AWS SDK
<a name="bedrock-agent_example_bedrock-agent_GetPrompt_section"></a>

The following code example shows how to use `GetPrompt`.

------
#### [ Python ]

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

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon Bedrock with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
