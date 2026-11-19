---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/guardrails.html
---

# AI guardrails in AWS Quick

AWS Quick takes a defense-in-depth approach to help keep chat interactions safe and responsible in the AWS Quick web experience. Multiple safety layers work together, each addressing different risks at different points in an interaction. No single layer is designed to catch every risk on its own.

Usage of AWS Quick AI features is subject to the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/) on the AWS website.

The following topics describe how these controls work and how to configure them.

**Topics**
+ [How AI safety controls work together](#guardrails-how-controls-work-together)
+ [Blocked words and phrases](#guardrails-blocked-phrases)

## How AI safety controls work together
<a name="guardrails-how-controls-work-together"></a>

AWS Quick uses the following controls together:

Model safety controls
With Quick, the models that you use have their own safety controls, which are designed to refuse requests for harmful content.

Prompt-level safety instructions
Quick instructs the model to promote responsible behavior, resist attempts to override safety settings, and avoid exposing internal system information.

External content marking
When connectors and remote Model Context Protocol (MCP) servers return content, Quick is designed to mark it as external data. It's also designed to instruct the model not to follow instructions in that content. The marking is an instruction to the model, not a filter. For more information, see [Two-condition model for adversarial content risk](sec-agentic-security.md#sec-agentic-security-two-condition-model).

Response rendering
Quick is designed to remove disallowed HTML from chat responses and to limit the types of links and images that a response can include. You can also choose whether links in responses are clickable. For more information, see [Configure clickable external links in chat responses](manage-agent.md#configure-clickable-links).

Access and permission controls
Identity, data-access, and action-permission controls limit what data and operations are available during an interaction. These limits match the signed-in person's permissions. For more information about identity and permissions, see [Identity and access management in Quick](identity.md) and [Custom permissions](custom-permissions.md).

Administrator-configured controls
You can set up blocked words and phrases for chat interactions in the AWS Quick web experience.

These controls help reduce risk. However, they do not replace your responsibility to configure access, permissions, agents, flows, and data sources for your use case.

## Blocked words and phrases
<a name="guardrails-blocked-phrases"></a>

You can block up to 50 words or phrases in chat interactions in the AWS Quick web experience. This applies to chat agents and flows. Each entry can contain up to 36 characters. Quick checks both user requests and generated responses for these phrases. These checks match whole words and phrases, regardless of capitalization. They aren't designed to catch misspellings, character substitutions, or encoded text. Quick doesn't block any words or phrases by default.

### Add blocked words and phrases
<a name="guardrails-add-blocked-phrases"></a>

Use the following procedure to add blocked words and phrases for chat agents and flows in the AWS Quick web experience.

**To add blocked words and phrases**

1. Sign in to Quick and choose **Manage Quick**.

1. From the navigation pane, choose **Customization**, and then choose **Chat agent customization**.

1. In **Chat agent customization**, under **Guardrails and safety controls**, choose **Add** to add blocked words and phrases. You can add up to 50 words and phrases. Each entry can contain up to 36 characters.

### Edit blocked words and phrases
<a name="guardrails-edit-blocked-phrases"></a>

Use the following procedure to add or remove blocked words and phrases for chat agents and flows in the AWS Quick web experience.

**To edit blocked words and phrases**

1. Sign in to Quick and choose **Manage Quick**.

1. From the navigation pane, choose **Customization**, and then choose **Chat agent customization**.

1. In **Chat agent customization**, under **Guardrails and safety controls**, choose **Remove** to remove existing entries, or choose **Add** to add entries. You can add up to 50 words and phrases. Each entry can contain up to 36 characters.
