---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/using-text-use-case.html
---

# Using the deployed Text use case
<a name="using-text-use-case"></a>

The built-in UI for the Text use case is intended to enable business users to quickly explore and experiment with the deployment created by the admin user. Configuration changes made by the business user only take effect for their session. The business user must share these changes with the admin user who can update the base deployment with those changes for all to use.

The chat UI consists of the following components:
+ Chat window
+ Chat input box
+ Settings
+ Clear conversation

## Chat window
<a name="chat-window"></a>

Holds different turns of the conversation. Messages starting on the right are from the business user, and messages starting on the left are from the configured LLM. A small clipboard icon exists on all LLM responses to enable easy copying of responses.

## Chat input box
<a name="chat-input-box"></a>

Pinned to the bottom of the chat window is the chat input box. This is where business users can enter their messages to be sent to the LLM. Just above the input box is the connection status. If the connection is lost (for example, due to inactivity), a new connection is automatically created the next time a chat message is sent. This request is expected to take a little longer due to the additional WebSocket connection time.

Based on the specific configuration, there might be a maximum length enforced on the input. If this limit is exceeded, users receive an alert and the message is not sent.

Note: If using RAG with Amazon Kendra, the [Retrieve API](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Retrieve.html) will truncate queries to 30 token words. If expecting longer user inputs, evaluate how this might affect search performance.

## Settings
<a name="settings"></a>

To enable business users to quickly experiment with different configurations, a settings panel is available, which enables on-the-fly editing of certain deployment configuration options

(example, prompt template). These changes can only be made at the start of a new session. Once a conversation is started, clearing the conversation re-enables the editing of the configuration settings.

Note: Admin users can choose to lock a deployment’s settings. They can prevent live edits at deployment time through the wizard during the prompt step.

## Clear conversation
<a name="clear-conversation"></a>

Over the course of the conversation, the solution maintains a chat history, which enables a conversational experience. This enables query disambiguation and follow-up questions. To reset a conversation and delete all chat history for this interaction, choose \*Clear conversation \*at the top of the chat window. Once the conversation has been cleared, a new session is created which re- enables editing of the settings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
