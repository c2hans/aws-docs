---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-sensitive-data-redaction-mask-mode.html
---

# Redaction mask mode
<a name="bda-sensitive-data-redaction-mask-mode"></a>

Use this setting to control how BDA masks detected PII entities in redacted output files.

Set the value to `PII` to replace all detected entities with a generic [PII] marker. Set the value to `ENTITY_TYPE` to replace each entity with its specific type marker, such as [NAME], [EMAIL], or [ADDRESS].

This setting applies only when you set `detectionMode` to `DETECTION_AND_REDACTION`. If you do not specify a value, BDA defaults to ENTITY\_TYPE.

**Redaction mask mode values**

| Mask mode | Description |
| --- | --- |
| PII | Replace sensitive data with [PII] in the redacted output files. |
| ENTITY\_TYPE | Replace sensitive data with [ENTITY\_TYPE] in the redacted output files. For example, [ADDRESS], [EMAIL]. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
