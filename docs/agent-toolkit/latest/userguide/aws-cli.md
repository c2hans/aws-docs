---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html
---

# AWS CLI
<a name="aws-cli"></a>

The AWS CLI provides commands to set up AI coding agents with the Agent Toolkit for AWS. You can manage installed AWS skills from the command line. The CLI works with any AI coding agent that the toolkit detects on your system, including Kiro, Cursor, and Claude Code.

Use the CLI when you want to install skills and configure the AWS MCP Server in a single step.

The CLI provides two command groups:
+ `aws configure agent-toolkit` - An interactive setup wizard that detects installed agents, installs default AWS skills, and configures the AWS MCP Server.
+ `aws agent-toolkit` - A set of commands to install, update, remove, list, and search for individual AWS skills.

**Topics**
+ [Prerequisites](#aws-cli-prerequisites)
+ [Setting up with the AWS CLI](#aws-cli-setup)
+ [Managing skills with the AWS CLI](#aws-cli-managing-skills)

## Prerequisites
<a name="aws-cli-prerequisites"></a>
+ AWS CLI version `2.35.0` or later. To install or update the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.
+ One or more supported AI coding agents installed on your system. The CLI detects supported agents by the presence of their configuration directories (for example, `~/.kiro` for Kiro). Skills are installed globally in those configuration directories, not per project.

## Setting up with the AWS CLI
<a name="aws-cli-setup"></a>

The `aws configure agent-toolkit` command runs an interactive setup wizard. It detects installed AI coding agents, installs default AWS skills, and configures the AWS MCP Server connection.

```
aws configure agent-toolkit
```

After the wizard completes, your selected agents can use the AWS MCP Server and the installed skills. Restart your agent client to load the new configuration.

## Managing skills with the AWS CLI
<a name="aws-cli-managing-skills"></a>

The `aws agent-toolkit` command group provides operations to install, update, remove, list, and search for individual skills. By default, install, update, and remove operations apply to all detected agents. Use the `--agent` option to target a specific tool.

The value for `--agent` is the stable agent identifier (for example, `kiro`). Run any command with `--help` to see valid values.

**Topics**
+ [Install a skill](#aws-cli-add-skill)
+ [Update an installed skill](#aws-cli-update-skill)
+ [Remove an installed skill](#aws-cli-remove-skill)
+ [List installed skills](#aws-cli-list-installed-skills)
+ [List available skills](#aws-cli-list-available-skills)
+ [Search for skills](#aws-cli-search-skills)
+ [Get skill metadata](#aws-cli-get-skill-metadata)
+ [Get a file from a skill](#aws-cli-get-skill-file)

### Install a skill
<a name="aws-cli-add-skill"></a>

The `add-skill` command downloads and installs an AWS skill to detected AI coding agents. By default, it installs the latest version globally to all detected agents. Use `--agent` to target a specific tool, or `--skill-version` to pin a specific version.

**Example 1: Install a skill**

The following `add-skill` example downloads and installs the `aws-serverless` skill to all detected AI coding agents.

```
aws agent-toolkit add-skill \
    --skill-name aws-serverless
```

**Example 2: Install a skill to a specific agent**

The following `add-skill` example installs the `aws-cdk` skill only to Kiro.

```
aws agent-toolkit add-skill \
    --skill-name aws-cdk \
    --agent kiro
```

**Example 3: Install a specific version of a skill**

The following `add-skill` example installs version `v1` of the `aws-serverless` skill.

```
aws agent-toolkit add-skill \
    --skill-name aws-serverless \
    --skill-version v1
```

### Update an installed skill
<a name="aws-cli-update-skill"></a>

The `update-skill` command updates an installed AWS skill to the latest version. It compares the local version against the catalog and downloads a newer version if one is available. By default, the command updates the skill for all detected agents. Use `--agent` to update only for a specific tool.

**Example 1: Update an installed skill**

The following `update-skill` example updates the `aws-serverless` skill to the latest version across all agents.

```
aws agent-toolkit update-skill \
    --skill-name aws-serverless
```

**Example 2: Update a skill for a specific agent**

The following `update-skill` example updates the `aws-serverless` skill only for Kiro.

```
aws agent-toolkit update-skill \
    --skill-name aws-serverless \
    --agent kiro
```

### Remove an installed skill
<a name="aws-cli-remove-skill"></a>

The `remove-skill` command removes a previously installed AWS skill from detected agents. By default, it removes the skill from all detected agents. Use `--agent` to remove the skill from a specific tool only.

**Example 1: Remove an installed skill**

The following `remove-skill` example removes the `aws-serverless` skill from all detected agents.

```
aws agent-toolkit remove-skill \
    --skill-name aws-serverless
```

**Example 2: Remove a skill from a specific agent**

The following `remove-skill` example removes the `aws-cdk` skill only from Kiro.

```
aws agent-toolkit remove-skill \
    --skill-name aws-cdk \
    --agent kiro
```

### List installed skills
<a name="aws-cli-list-installed-skills"></a>

The `list-installed-skills` command lists AWS skills that you previously installed with the `aws agent-toolkit` commands. It shows the skill name, agent, and file path for each installation. By default, it lists skills from all detected agents. Use `--agent` to filter results to a specific tool.

**Example 1: List installed skills**

The following `list-installed-skills` example lists all AWS skills installed on detected agents.

```
aws agent-toolkit list-installed-skills
```

**Example 2: List installed skills for a specific agent**

The following `list-installed-skills` example lists skills installed only in Kiro.

```
aws agent-toolkit list-installed-skills \
    --agent kiro
```

### List available skills
<a name="aws-cli-list-available-skills"></a>

The `list-available-skills` command lists skills available in the remote catalog.

**Example 1: List all available skills**

The following `list-available-skills` example lists all skills available in the remote catalog.

```
aws agent-toolkit list-available-skills
```

**Example 2: List available skills filtered by category**

The following `list-available-skills` example lists only skills in the `aws-core` category.

```
aws agent-toolkit list-available-skills \
    --category-filter aws-core
```

### Search for skills
<a name="aws-cli-search-skills"></a>

The `search-skills` command searches the remote catalog for skills matching a query.

**Example: Search for available skills**

The following `search-skills` example searches for skills related to serverless development.

```
aws agent-toolkit search-skills \
    --search-query serverless
```

### Get skill metadata
<a name="aws-cli-get-skill-metadata"></a>

The `get-skill-metadata` command retrieves metadata for a skill. This includes the version, description, categories, and file list.

**Example 1: Get metadata for a skill**

The following `get-skill-metadata` example retrieves metadata for the `aws-serverless` skill.

```
aws agent-toolkit get-skill-metadata \
    --skill-name aws-serverless
```

**Example 2: Get metadata for a specific skill version**

The following `get-skill-metadata` example retrieves metadata for version `v1` of the `aws-serverless` skill.

```
aws agent-toolkit get-skill-metadata \
    --skill-name aws-serverless \
    --skill-version v1
```

### Get a file from a skill
<a name="aws-cli-get-skill-file"></a>

The `get-skill-file` command retrieves the contents of a single file from a skill. Use `aws agent-toolkit get-skill-metadata` to discover available file names for each skill. By default, the command retrieves the latest version. Use `--skill-version` to fetch a specific version.

**Example 1: Fetch a file from a skill**

The following `get-skill-file` example retrieves the `SKILL.md` file from the `aws-serverless` skill.

```
aws agent-toolkit get-skill-file \
    --skill-name aws-serverless \
    --file-path SKILL.md
```

**Example 2: Fetch a specific version of a skill file**

The following `get-skill-file` example retrieves a reference file from a specific version of the `aws-serverless` skill.

```
aws agent-toolkit get-skill-file \
    --skill-name aws-serverless \
    --file-path references/architecture.md \
    --skill-version v1
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Agent Toolkit for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-toolkit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
