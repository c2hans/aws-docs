---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/API_Authorize.html
---

# Authorize
<a name="API_Authorize"></a>

|  |
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Authorizes an AppClient.

**Topics**
+ [Request body](#API_Authorize_request)

## Request body
<a name="API_Authorize_request"></a>

The request accepts the following data in JSON format.

| Parameter | Description |
| --- | --- |
| **app\_client\_id** | The ID of the AppClient to authorize. |
| **redirect\_uri** | The URI to redirect end users to after authorization. |
| **state** | A unique value to maintain the state between the request and callback. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
