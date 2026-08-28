---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/rules-files.html
---

# Rules files
<a name="rules-files"></a>

Most AI coding agents support project-level configuration files, often called rules files. These files provide persistent instructions that your agent follows in every session. For example, you might have a rules file that tells your agent to always write TypeScript in strict mode, or to use a specific testing framework.

The Agent Toolkit for AWS includes a recommended rules file that tells your agent how to work with AWS. For example, the rules file instructs your agent to use the AWS MCP Server for API calls, to search for available skills before starting a task, and to prefer infrastructure-as-code over direct CLI commands.

**Topics**
+ [Recommended AWS rules file](#recommended-rules-file)
+ [Where to put the rules file](#rules-file-location)
+ [Customization](#rules-customization)

## Recommended AWS rules file
<a name="recommended-rules-file"></a>

The Agent Toolkit for AWS includes a recommended rules file that covers using the AWS MCP Server, discovering skills, verifying against documentation, and following infrastructure-as-code best practices. You can find the latest version of this file in the [Agent Toolkit for AWS repository on GitHub](https://github.com/aws/agent-toolkit-for-aws/blob/main/rules/aws-agent-rules.md). Copy the content into the appropriate file for your agent.

## Where to put the rules file
<a name="rules-file-location"></a>

The file name and location depend on your agent:

**Rules file locations by agent**

| Agent | Project rules | Location |
| --- | --- | --- |
| Claude Code | CLAUDE.md | Project root |
| Codex | AGENTS.md | Project root |
| Cursor | .cursor/rules/\*.mdc | .cursor/rules/ directory |
| Kiro | .kiro/steering/\*.md | .kiro/steering/ directory |

For Claude Code and Codex, add the recommended rules file content to your existing `CLAUDE.md` or `AGENTS.md` file, or create a new one in your project root. For Cursor, create a new `.mdc` file in the `.cursor/rules/` directory. For example, name it `.cursor/rules/aws.mdc`. Your agent still supports the legacy `.cursorrules` file, but it is deprecated.

## Customization
<a name="rules-customization"></a>

The recommended rules file is a starting point. Customize it for your project. For example, you can specify which AWS Region to use, which VPC to deploy into, or which naming conventions to follow for resources.

The following example shows project-specific rules you might add:

```
# Project-specific AWS rules

- Default region is eu-west-1. Do not create resources in other regions
  unless explicitly asked.
- All infrastructure must be deployed into VPC vpc-0abc1234567890def in the
  shared-services account.
- Resource naming convention: {team}-{service}-{environment}-{purpose}
  (e.g., payments-lambda-prod-processor).
- Always tag resources with Team=payments, CostCenter=CC-4521, and
  Environment=(dev|staging|prod).
- Use Python 3.12 for all Lambda functions. Do not use Node.js unless
  the project already uses it.
- Never provision resources larger than t3.medium without confirmation.
```

Add these rules alongside the recommended AWS rules in your agent's rules file. Your agent follows both sets of instructions in every session.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Agent Toolkit for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-toolkit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
