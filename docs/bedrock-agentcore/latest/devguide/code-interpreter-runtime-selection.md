---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-runtime-selection.html
---

# Runtime selection
<a name="code-interpreter-runtime-selection"></a>

For a language, you can optionally specify a particular runtime. The following table shows the supported languages and their available runtimes.

| Language | Available runtimes |
| --- | --- |
| Python |  `python`  |
| JavaScript |  `nodejs` , `deno`  |
| TypeScript |  `nodejs` , `deno`  |

**Note**
For the `nodejs` runtime, we support CommonJS (CJS) modules for JavaScript and ECMAScript (ESM) modules for TypeScript.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
