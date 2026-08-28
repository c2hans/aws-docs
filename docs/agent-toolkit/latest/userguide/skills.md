---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/skills.html
---

# Skills
<a name="skills"></a>

Agent skills are curated packages of instructions, code scripts, and reference materials that help AI coding agents complete specific AWS tasks. Skills bridge the gap between what AI models know from training data and what they need to work effectively with AWS. This is especially important for newer services, complex multi-service workflows, and tasks where best practices matter.

**Topics**
+ [What is a skill?](#what-is-a-skill)
+ [How agents discover and use skills](#how-agents-use-skills)
+ [Types of skills](#types-of-skills)
+ [Available skills](#available-skills)
+ [Using skills with and without the AWS MCP Server](#skills-with-without-mcp)
+ [AWS CLI](aws-cli.md)

## What is a skill?
<a name="what-is-a-skill"></a>

A skill is a directory containing a `SKILL.md` file and optional supporting files. The `SKILL.md` file includes a brief description and instructions that tell your agent how to complete a task. These instructions specify which steps to follow, which AWS APIs to call, which mistakes to avoid, and how to verify the result. Skills can also include reference files with deeper guidance on specific subtasks, code scripts for deterministic operations, and slash commands that let you invoke the skill directly.

Skills are lightweight and modular. Each skill focuses on a single task or domain, and your agent loads only the skills it needs for the current task. A skill typically consumes a few thousand tokens when loaded. This is far less than the equivalent documentation, because a skill contains only the information your agent needs to act, not background context it already has.

## How agents discover and use skills
<a name="how-agents-use-skills"></a>

There are four ways agents get access to skills:

Bundled with a plugin
Each plugin includes a curated set of skills that are available to your agent immediately after installation. Your agent can use these skills without any network calls or additional setup.

Installed locally
You can download individual skills from the [Agent Toolkit for AWS repository on GitHub](https://github.com/aws/agent-toolkit-for-aws) and add them to your agent's skills directory.

Installed with the AWS CLI
You can install skills with the AWS CLI through the interactive setup wizard (`aws configure agent-toolkit`) or with the individual `aws agent-toolkit` commands. The CLI detects supported agents on your system and installs skills into each agent's configuration directory. For more information, see [AWS CLI](aws-cli.md).

Discovered at runtime through the AWS MCP Server
Agents can search for and retrieve skills on demand through the AWS MCP Server, without any local installation. Your agent uses the `search_documentation` tool to find relevant skills and the `retrieve_skill` tool to load them into context.

Regardless of how a skill was installed, your agent uses it the same way:

1. Your agent reads the skill's description to determine if it is relevant to the current task.

1. If relevant, your agent loads the full instructions from `SKILL.md`.

1. Your agent follows the skill's procedures, loading reference files only as needed.

1. After the task is complete, your agent releases the skill content from context.

This progressive disclosure means that many available skills do not slow your agent down or consume unnecessary context. Your agent loads only the skills relevant to the current task.

## Types of skills
<a name="types-of-skills"></a>

The Agent Toolkit for AWS includes several types of skills:

Service decision guides
These skills help your agent choose the right AWS service for a use case. For example, a database decision guide helps your agent recommend Amazon DynamoDB, Amazon Aurora, or Amazon DSQL based on the workload requirements.

Step-by-step procedures
These skills provide tested workflows for common tasks like creating Amazon S3 Tables, setting up AWS Glue ETL pipelines, configuring IAM policies, and deploying serverless applications.

Troubleshooting guides
These skills provide diagnostic procedures for common errors, with steps to identify the cause and resolve the issue. For example, a CloudFormation deployment troubleshooting skill covers the top failure patterns and how to fix them.

SDK usage guides
These skills provide language-specific best practices for the AWS SDKs. They cover common mistakes that models consistently get wrong, like Amazon DynamoDB marshalling in JavaScript or pagination patterns in Python.

## Available skills
<a name="available-skills"></a>

Each plugin includes a curated set of skills covering the most common workflows for that domain. The full set of skills, including domain-specific skills for individual AWS services, is available on [GitHub](https://github.com/aws/agent-toolkit-for-aws) and discoverable at runtime through the AWS MCP Server.

To see what skills are available from within your agent, ask: *"What AWS skills do you have available?"* or *"Search for AWS skills related to databases."*

You can also browse and install skills from the command line:

```
npx skills add aws/agent-toolkit-for-aws/skills
```

## Using skills with and without the AWS MCP Server
<a name="skills-with-without-mcp"></a>

Skills work best with the AWS MCP Server, which provides authenticated API access, sandboxed script execution, and enterprise controls like CloudWatch metrics and IAM context keys. For production workflows, use the AWS MCP Server.

Skills also work without the AWS MCP Server. When your agent does not have access to the AWS MCP Server, it can run the same AWS operations using the AWS CLI directly. Each skill includes instructions that work with both approaches.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Agent Toolkit for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-toolkit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
