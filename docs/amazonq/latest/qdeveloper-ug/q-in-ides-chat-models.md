---
source_url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-ides-chat-models.html
---

# Selecting a model for Amazon Q chat in IDEs
<a name="q-in-ides-chat-models"></a>

You can select the model you want Amazon Q to use while chatting in the IDE. The model you select persists across all future chat sessions.

The following table describes the models that are available for Amazon Q chat in the IDE and their context windows.

| Model | Context window |
| --- | --- |
| Claude Sonnet 3.7 | 200k |
| Claude Sonnet 4 (default) | 200k |

## Select the model used for chatting in the IDE
<a name="select-model-ide-chat"></a>

To select the model Amazon Q uses when you chat in your IDE:

1. Open the Amazon Q chat panel in your IDE.

1. In the chat input area, choose the model menu dropdown. Select the model you want to use from the available options.

   The model you select persists until you change it.

## Context windows
<a name="context-window"></a>

The context window is the amount of context, including your conversation history and any explicit or automatic context, that Amazon Q can use to process and respond to your requests. Context is measured in tokens, which includes text and code.

For more information about context, see [Adding context to the chat](ide-chat-context.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
