---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-listquickconnects.html
---

# Get the list of Quick Connect endpoints associated with a given queue in Connect Customer agent workspace
<a name="3P-apps-agent-requests-listquickconnects"></a>

 Get the list of Quick Connect endpoints associated with the given queue(s). Optionally you can pass in a parameter to override the default max-results value of 500.

 **Signature**

```
listQuickConnects(
    queueARNs: QueueARN | QueueARN[],
    options?: ListQuickConnectsOptions,
  ): Promise<ListQuickConnectsResult>
```

 **Usage**

```
const routingProfile: AgentRoutingProfile = await agentClient.getRoutingProfile();
const quickConnects: ListQuickConnectsResult = await agentClient.listQuickConnects(routingProfile.queues[0].queueARN);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  queueARNs Required  |  string \| string[]  |  One or more Queue ARNs for which the Queue Connects need to be retrieved  |
|  options.maxResults  |  number  |  The maximum number of results to return per page. The default value is 500  |
|  options.nextToken  |  string  |  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  |

 **Output - ListQuickConnectsResult**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  quickConnects  |  QuickConnect[]  |  Its either AgentQuickConnect or QueueQuickConnect or PhoneNumberQuickConnect which contains endpointARN and name. Additionally PhoneNumberQuickConnect contains phoneNumber  |
|  nextToken  |  string  |  If there are additional results, this is the token for the next set of results.  |

 **Permissions required:**

```
User.Configuration.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
