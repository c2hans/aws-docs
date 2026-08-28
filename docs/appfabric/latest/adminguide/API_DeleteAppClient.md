---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/API_DeleteAppClient.html
---

# DeleteAppClient
<a name="API_DeleteAppClient"></a>

|  |
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Deletes an application client.

**Topics**
+ [Request body](#API_DeleteAppClient_request)
+ [Response elements](#API_DeleteAppClient_response)

## Request body
<a name="API_DeleteAppClient_request"></a>

The request accepts the following data in JSON format.

| Parameter | Description |
| --- | --- |
| **appClientIdentifier** | The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the AppClient to use for the request.<br />Length Constraints: Minimum length of 1. Maximum length of 1011.<br />Pattern: `arn:.+$\|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`<br />Required: Yes |

## Response elements
<a name="API_DeleteAppClient_response"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
