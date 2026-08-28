---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html
---

# How Amazon Bedrock Flows works
<a name="flows-how-it-works"></a>

Amazon Bedrock Flows lets you build generative AI workflows by connecting nodes, each of which correspond to a step in the flow that invokes an Amazon Bedrock or related resource. To define inputs into and outputs from nodes, you use expressions to specify how the input is interpreted. To better understand these concepts, review the following topics:

**Topics**
+ [Key definitions for Amazon Bedrock Flows](key-definitions-flow.md)
+ [Use expressions to define inputs by extracting the relevant part of a whole input in Amazon Bedrock Flows](flows-expressions.md)
+ [Node types for your flow](flows-nodes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
