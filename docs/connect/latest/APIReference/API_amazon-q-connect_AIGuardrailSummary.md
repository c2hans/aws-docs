---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_AIGuardrailSummary.html
---

# AIGuardrailSummary
<a name="API_amazon-q-connect_AIGuardrailSummary"></a>

The summary of the AI Guardrail.

## Contents
<a name="API_amazon-q-connect_AIGuardrailSummary_Contents"></a>

 ** aiGuardrailArn **   <a name="connect-Type-amazon-q-connect_AIGuardrailSummary-aiGuardrailArn"></a>
The Amazon Resource Name (ARN) of the AI Guardrail.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** aiGuardrailId **   <a name="connect-Type-amazon-q-connect_AIGuardrailSummary-aiGuardrailId"></a>
The identifier of the Amazon Q in Connect AI Guardrail.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** assistantArn **   <a name="connect-Type-amazon-q-connect_AIGuardrailSummary-assistantArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** assistantId **   <a name="connect-Type-amazon-q-connect_AIGuardrailSummary-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_AIGuardrailSummary-name"></a>
The name of the AI Guardrail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** visibilityStatus **   <a name="connect-Type-amazon-q-connect_AIGuardrailSummary-visibilityStatus"></a>
The visibility status of the AI Guardrail.
Type: String
Valid Values: `SAVED | PUBLISHED`
Required: Yes

 ** description **   <a name="connect-Type-amazon-q-connect_AIGuardrailSummary-description"></a>
A description of the AI Guardrail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** modifiedTime **   <a name="connect-Type-amazon-q-connect_AIGuardrailSummary-modifiedTime"></a>
The time the AI Guardrail was last modified.
Type: Timestamp
Required: No

 ** status **   <a name="connect-Type-amazon-q-connect_AIGuardrailSummary-status"></a>
The status of the AI Guardrail.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED`
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_AIGuardrailSummary-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_AIGuardrailSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AIGuardrailSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AIGuardrailSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AIGuardrailSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
