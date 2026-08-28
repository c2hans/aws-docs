---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/API_UpdateAppClient.html
---

# UpdateAppClient
<a name="API_UpdateAppClient"></a>

|  |
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Updates an AppClient.

**Topics**
+ [Request body](#API_UpdateAppClient_request)
+ [Response elements](#API_UpdateAppClient_response)

## Request body
<a name="API_UpdateAppClient_request"></a>

The request accepts the following data in JSON format.

| Parameter | Description |
| --- | --- |
| **appClientIdentifier** | The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the AppClient to use for the request.<br />Length Constraints: Minimum length of 1. Maximum length of 1011.<br />Pattern: `arn:.+$\|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`<br />Required: Yes |
| **redirectUrls** | The URI to redirect end users to after authorization. You can add up to 5 redirectUrls. For example, `https://localhost:8080`.<br />Type: Array of strings<br />Array Members: Minimum number of 1 item. Maximum number of 5 items.<br />Length Constraints: Minimum length of 1. Maximum length of 2048.<br />Pattern: `(http\|https):\/\/[-a-zA-Z0-9_:.\/]+`<br /> |

## Response elements
<a name="API_UpdateAppClient_response"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

| Parameter | Description |
| --- | --- |
| **appClient** | Contains information about an AppClient.<br />Type: [AppClient](API_AppClient.md) object |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
