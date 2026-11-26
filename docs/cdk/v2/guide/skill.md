---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/skill.html
---

# AWS CDK Agent Skill

The * AWS CDK agent skill* teaches a coding agent how to work in a CDK codebase: bootstrapping and project setup, construct patterns, compliance, drift, importing and migrating existing resources, safe refactors, troubleshooting, and v1–v2 migration. It is published by AWS in the [Agent Toolkit for AWS on GitHub](https://github.com/aws/agent-toolkit-for-aws) under Apache-2.0.

## Installation
<a name="installation"></a>

The skill can be installed using the `skills` command:

```bash
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-cdk
```

For other install methods (plugin install, per-agent skills directories, and MCP runtime discovery), refer to the the [upstream skills README on GitHub](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills).
