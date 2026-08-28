---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/how-the-generative-ai-application-builder-on-aws-solution-works.html
---

# How the Generative AI Application Builder on AWS solution works
<a name="how-the-generative-ai-application-builder-on-aws-solution-works"></a>

The admin user primarily interfaces with the Deployment dashboard to view, create, and manage new and existing use case deployments. Through this dashboard, the admin user has access to the following actions:
+ View list of deployments
+ Create new deployments
+ Edit existing deployments
+ Clone a deployment’s configuration to create a new deployment
+ Delete a deployment (deprovision the resources through a CloudFormation delete)
+ Permanently delete the configuration details of a deployment

 **Depicts Use case diagram for the admin user of the Deployment dashboard**

![image4](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/image4.png)

**Note**
The admin user might not have direct access to the AWS console. In that case, the admin user must work with the DevOps user to support actions such as ingesting data into a Kendra knowledge base.

For the Text use case, the business user gets access to a user interface enabling them to chat with the LLM. The specifics of this configuration are controlled by the deployment settings configured by the admin user. In the Text use case, the business user has access to the following actions:
+ Send messages through the chat interface
+ View conversation history
+ Clear the conversation history
+ View prompt
+ Edit prompt

 **Depicts Use case diagram for the business user of the Text use case**

![image5](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/image5.png)

With the Bedrock Agent use case, the business user can access a UI for chatting with the configured Amazon Bedrock Agent. The admin user can configure these speciﬁcs in the deployment settings. In the Bedrock Agent use case, the business user has access to the following actions:
+ Send messages through the chat interface
+ View conversation history
+ Clear the conversation history

 **Depicts Use case diagram for the business user of the Bedrock Agent use case**

![agent use case user diagram](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/agent-use-case-user-diagram.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
