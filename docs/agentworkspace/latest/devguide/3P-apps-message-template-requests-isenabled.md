---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-message-template-requests-isenabled.html
---

# Determine if the Message Template feature is enabled in Connect Customer agent workspace
<a name="3P-apps-message-template-requests-isenabled"></a>

Returns the MessageTemplateEnabledState object, which indicates if the message template feature is enabled for the Connect instance. The Message Template feature is considered enabled if there is a knowledge base for message templates configured for the instance. The object contains the following fields:
+ `isEnabled`: A boolean indicating if the feature is enabled
+ `knowledgeBaseId`: The id of the Message Template Knowledge Base (if the feature is enabled)

 **Signature**

```
isEnabled(): Promise<MessageTemplateEnabledState>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
