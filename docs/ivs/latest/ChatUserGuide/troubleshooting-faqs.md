---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/troubleshooting-faqs.html
---

# Troubleshooting IVS Chat
<a name="troubleshooting-faqs"></a>

This document describes best practices and troubleshooting tips for Amazon Interactive Video Service (IVS) Chat. Behaviors related to IVS Chat often are distinct from behaviors related to IVS video. For more information, see [Getting Started with Amazon IVS Chat](getting-started-chat.md).

Topics:
+ [Why were IVS chat connections not disconnected when the room was deleted?](#chat-connections-not-disconnected)

## Why were IVS chat connections not disconnected when the room was deleted?
<a name="chat-connections-not-disconnected"></a>

When a chat-room resource is deleted, if the room is actively being used, the chat clients that are connected to the room are not automatically disconnected. The connection is dropped if/when the chat application refreshes the chat token. Alternately, a manual disconnect of all users must be done to remove all users from the chat room.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
