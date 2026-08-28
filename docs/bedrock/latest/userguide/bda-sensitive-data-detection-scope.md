---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-sensitive-data-detection-scope.html
---

# Detection scope
<a name="bda-sensitive-data-detection-scope"></a>

Use this setting to specify which BDA output types receive sensitive data detection. Specify `STANDARD` for standard output, `CUSTOM` for custom output (blueprint-based extraction), or both. If you do not specify a value, BDA defaults to both `STANDARD` and `CUSTOM`.

**Detection scope values**

| Scope | Description |
| --- | --- |
| STANDARD | Apply detection mode to standard outputs. |
| CUSTOM | Apply detection mode to custom outputs. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
