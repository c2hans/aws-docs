---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/flows-view.html
---

# View information about flows in Amazon Bedrock
<a name="flows-view"></a>

To learn how to view information about a flow, choose the tab for your preferred method, and then follow the steps:

------
#### [ Console ]

**To view the details of a flow**

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock).

1. Select **Amazon Bedrock Flows** from the left navigation pane. Then, in the **Amazon Bedrock Flows** section, select a flow.

1. View the details of the flow in the **Flow details** pane.

------
#### [ API ]

To get information about a flow, send a [GetFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlow.html) request with an [Agents for Amazon Bedrock build-time endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bra-bt) and specify the ARN or ID of the flow as the `flowIdentifier`.

To list information about your flows, send a [ListFlows](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListFlows.html) request with an [Agents for Amazon Bedrock build-time endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bra-bt). You can specify the following optional parameters:

| Field | Short description |
| --- | --- |
| maxResults | The maximum number of results to return in a response. |
| nextToken | If there are more results than the number you specified in the maxResults field, the response returns a nextToken value. To see the next batch of results, send the nextToken value in another request. |

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
