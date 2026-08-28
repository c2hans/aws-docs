---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RedactionConfiguration.html
---

# RedactionConfiguration
<a name="API_RedactionConfiguration"></a>

The redaction configuration for conversational analytics.

## Contents
<a name="API_RedactionConfiguration_Contents"></a>

 ** Behavior **   <a name="connect-Type-RedactionConfiguration-Behavior"></a>
Controls whether redaction is applied to the analytics output. Valid values: `Enable` \| `Disable`.
Type: String
Valid Values: `Enable | Disable`
Required: Yes

 ** Policy **   <a name="connect-Type-RedactionConfiguration-Policy"></a>
The redaction output policy that determines which versions of the transcript are stored. Valid values: `None` \| `RedactedOnly` \| `RedactedAndOriginal`.
Type: String
Valid Values: `None | RedactedOnly | RedactedAndOriginal`
Required: Yes

 ** Entities **   <a name="connect-Type-RedactionConfiguration-Entities"></a>
The list of PII entity types to redact from the transcript (for example, `NAME`, `ADDRESS`, `CREDIT_DEBIT_NUMBER`).
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** MaskMode **   <a name="connect-Type-RedactionConfiguration-MaskMode"></a>
The masking mode that determines how redacted content is replaced in the output. Valid values: `PII` (replaces with the literal string [PII]) \| `EntityType` (replaces with the entity type name, for example [NAME]).
Type: String
Valid Values: `PII | EntityType`
Required: No

## See Also
<a name="API_RedactionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RedactionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RedactionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RedactionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
