---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-thinking-block-binding.html
---

# Thinking block binding (beta)
<a name="claude-messages-thinking-block-binding"></a>

## Overview
<a name="claude-messages-thinking-block-binding-overview"></a>

Thinking-capable Claude models can bind a `thinking` or `redacted_thinking` block to the context that created it: the model that produced it, the AWS account that made the request, the end user (if one was identified), and the conversation content that came before the block. When you replay a thinking block in a later request, Claude honors it only if that context still matches. This protects the integrity of Claude's reasoning across multi-turn and agentic conversations.

Two things determine how binding applies to a given request:
+ The request object `thinking.block_binding` and the response array `input_transformations` are available on thinking-capable Claude models and require the `thinking-binding-controls-2026-08-01` beta value.
+ The account, end-user, and conversation-prefix checks are enforced on Claude Fable 5.1 and Claude Mythos 5.1. Other thinking-capable models accept the same fields and return `input_transformations`, but do not run the account, end-user, or conversation-prefix checks at this time. The model-compatibility check applies whenever a bound block is replayed, on any thinking-capable model.

**What is checked on replay**

| **Check** | **Description** |
| --- | --- |
| Model | The model reading the block is allowed to read the producer's thinking. A model cannot read another model's thinking unless the two are explicitly compatible. This check applies on any thinking-capable model. |
| Account | The replaying request comes from the same AWS account that produced the block, or from one of the accounts listed in bind\_to\_additional\_organizations. |
| End user | The replaying request carries the same end-user identifier the producing request carried — unless the producer set bind\_to\_end\_user to false. |
| Conversation prefix | The top-level system prompt, tools, and all message content before the block are unchanged from the request that produced it. |

**Note**
A thinking block whose signature has been altered or cannot be decrypted always returns a 400, regardless of these checks or the beta value.

## The block\_binding request object
<a name="claude-messages-thinking-block-binding-request-object"></a>

Add `block_binding` to the `thinking` object and include the beta value in `anthropic_beta`:

```
{
    "anthropic_version": "bedrock-2023-05-31",
    "anthropic_beta": ["thinking-binding-controls-2026-08-01"],
    "max_tokens": 16000,
    "thinking": {
        "type": "adaptive",
        "block_binding": {
            "bind_to_additional_organizations": [
                {"type": "aws", "account_id": "123456789012"}
            ],
            "bind_to_end_user": false,
            "mismatch_behavior": "drop_block"
        }
    },
    "messages": [{ "role": "user", "content": "Your prompt here" }]
}
```

| **Field** | **Description** |
| --- | --- |
| bind\_to\_additional\_organizations | Up to 6 additional accounts (besides the caller) allowed to replay this request's thinking blocks. Each entry is {"type":"aws","account\_id":"<12 digits>"}, {"type":"anthropic","organization\_id":"<uuid>"}, or {"type":"gcp","project\_number":"<digits>"}. Duplicate entries and your own account are ignored. |
| bind\_to\_end\_user | Boolean, default true. When true, a replayed block is honored only if the same end-user identifier is present. Set false to record the end user without enforcing the check. |
| mismatch\_behavior | "drop\_block" or "error". Controls what happens when a check fails. |

**Note**
The compared account is the calling AWS account; you can't set it in the body. To identify the end user, pass `metadata.user_id` (or `user_profile_id`) unchanged on each request; don't change it mid-conversation. `CountTokens` doesn't accept end-user identifiers.

Without the beta value, sending `block_binding` returns `400 thinking.adaptive.block_binding: Extra inputs are not permitted`. Malformed values return a standard 400 naming the field.

## Controlling mismatch behavior
<a name="claude-messages-thinking-block-binding-mismatch-behavior"></a>

| **Value** | **Behavior on a failed check** |
| --- | --- |
| "drop\_block" | Request succeeds with 200. The failing block is removed before the model (for a prefix failure, later thinking blocks in that turn are also removed), and listed in input\_transformations. |
| "error" | Request fails with 400 invalid\_request\_error naming the failed block. Not retryable; returned before any streaming events. |

**Note**
If `mismatch_behavior` is omitted with the beta value, it behaves like `"drop_block"`.

## The input\_transformations response array
<a name="claude-messages-thinking-block-binding-input-transformations"></a>

When the beta value is sent, the response may include a top-level `input_transformations` array describing any blocks that were removed:

```
{
    "type": "message", "role": "assistant", "content": [ ... ],
    "stop_reason": "end_turn",
    "usage": {"input_tokens": 18234, "output_tokens": 911},
    "input_transformations": [
        {"type": "thinking_dropped", "path": "messages.3.content.0", "reason": "prefix_binding_mismatch"}
    ]
}
```

This is a top-level array (a sibling of `usage`), present only with the beta value; `[]` when no blocks were removed and absent otherwise. Each entry contains a `path` identifying the removed block and a `reason` — one of `model_binding_mismatch`, `prefix_binding_mismatch`, `organization_binding_mismatch`, or `end_user_binding_mismatch`. In streaming responses, the array appears within the message object inside the `message_start` event and is not repeated in `message_delta`. Removed blocks do not count toward `input_tokens`, and the array is not returned by `CountTokens`.

## Error responses
<a name="claude-messages-thinking-block-binding-error-responses"></a>

When `mismatch_behavior` is `"error"`, a failed check returns:

```
{
    "type": "error",
    "error": {
        "type": "invalid_request_error",
        "message": "messages.3.content.0: Invalid `signature` in `thinking` block. The block is bound to a different conversation. Remove the block, or set `thinking.block_binding.mismatch_behavior` to \"drop_block\"."
    }
}
```

Match on the leading clause `Invalid `signature` in `thinking` block` (or `redacted_thinking`), not the full message.

## Guidance for multi-turn and agentic applications
<a name="claude-messages-thinking-block-binding-guidance"></a>
+ Replay assistant turns exactly as they were returned, and keep the system prompt and tools stable within a conversation.
+ Avoid one-off content injected into earlier turns (for example, a transient system message or reminder text appended to the last user turn). These change the conversation prefix and invalidate later thinking blocks.
+ If your application rewrites conversation history, drop thinking blocks from the rewritten point onward, or set `mismatch_behavior` to `"drop_block"`.
+ Keep the end-user identifier constant within a conversation, or set `bind_to_end_user` to `false`.
+ Applications that operate across multiple accounts should list those accounts in `bind_to_additional_organizations`.
+ When using the Converse API with a model that supports it, pass the beta value and `thinking.block_binding` through `additionalModelRequestFields`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
