---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-cli-reference.html
---

# AgentCore CLI reference
<a name="agentcore-cli-reference"></a>

This reference documents the public Amazon Bedrock AgentCore CLI releases.

**Topics**
+ [Project Lifecycle](#cli-project-lifecycle)
+ [Resource Management](#cli-resources)
+ [Optimization & Config Bundles](#cli-optimization)

## Project Lifecycle
<a name="cli-project-lifecycle"></a>

 *Auto-generated from `@aws/agentcore` v0.24.2 — do not edit by hand.*

### agentcore create
<a name="_agentcore_create"></a>

```
agentcore create [options]
```

Create a new AgentCore project

 **Parameters**

 `--name <name>` *(optional)*
Resource name [non-interactive]

 `--project-name <name>` *(optional)*
Project name (start with letter, alphanumeric only, max 23 chars) [non-interactive]

 `--no-agent` *(optional)*
Skip agent creation [non-interactive]

 `--defaults` *(optional)*
Create a harness project with default settings (this is the default) [non-interactive]

 `--build <type>` *(optional)*
Build type: CodeZip or Container (default: CodeZip) [non-interactive]

 `--language <language>` *(optional)*
Target language: Python or TypeScript (default: Python) [non-interactive]

 `--framework <framework>` *(optional)*
Agent framework (Strands, LangChain\_LangGraph, GoogleADK, OpenAIAgents, VercelAI) [non-interactive]

 `--model-provider <provider>` *(optional)*
Model provider (Bedrock, Anthropic, OpenAI, Gemini) [non-interactive]

 `--api-key <key>` *(optional)*
API key for non-Bedrock providers [non-interactive]

 `--memory <option>` *(optional)*
Memory option (none, shortTerm, longAndShortTerm) [non-interactive]

 `--protocol <protocol>` *(optional)*
Protocol: HTTP, MCP, A2A, AGUI (default: HTTP) [non-interactive]

 `--type <type>` *(optional)*
Agent type: create or import (default: create) [non-interactive]

 `--agent-id <id>` *(optional)*
Bedrock Agent ID (required for --type import) [non-interactive]

 `--agent-alias-id <id>` *(optional)*
Bedrock Agent Alias ID (required for --type import) [non-interactive]

 `--region <region>` *(optional)*
The AWS Region for Bedrock Agent (required for --type import) [non-interactive]

 `--network-mode <mode>` *(optional)*
Network mode (PUBLIC, VPC) [non-interactive]

 `--subnets <ids>` *(optional)*
Comma-separated subnet IDs (required for VPC mode) [non-interactive]

 `--security-groups <ids>` *(optional)*
Comma-separated security group IDs (required for VPC mode) [non-interactive]

 `--vpc-id <id>` *(optional)*
VPC ID (required for Container builds with VPC mode) [non-interactive]

 `--idle-timeout <seconds>` *(optional)*
Idle session timeout in seconds (60-28800) [non-interactive]

 `--max-lifetime <seconds>` *(optional)*
Max instance lifetime in seconds (60-28800) [non-interactive]

 `--session-storage-mount-path <path>` *(optional)*
Absolute mount path for session filesystem storage under /mnt (for example, /mnt/data) [non-interactive]

 `--efs-access-point-arn <arn>` *(optional)*
EFS access point ARN (repeatable, paired with --efs-mount-path) [non-interactive] (default: [])

 `--efs-mount-path <path>` *(optional)*
EFS mount path (for example, /mnt/tools, paired with --efs-access-point-arn) [non-interactive] (default: [])

 `--s3-access-point-arn <arn>` *(optional)*
S3 Files access point ARN (repeatable, paired with --s3-mount-path) [non-interactive] (default: [])

 `--s3-mount-path <path>` *(optional)*
S3 Files mount path (for example, /mnt/datasets, paired with --s3-access-point-arn) [non-interactive] (default: [])

 `--with-config-bundle` *(optional)*
Create a config bundle wired into the agent template [non-interactive]

 `--output-dir <dir>` *(optional)*
Output directory (default: current directory) [non-interactive]

 `--skip-git` *(optional)*
Skip git repository initialization [non-interactive]

 `--skip-python-setup` *(optional)*
Skip Python virtual environment setup [non-interactive]

 `--skip-install` *(optional)*
Skip all dependency installation (npm install, uv sync) [non-interactive]

 `--dry-run` *(optional)*
Preview what would be created without making changes [non-interactive]

 `--json` *(optional)*
Output as JSON [non-interactive]

 `--model-id <id>` *(optional)*
Model ID for harness [non-interactive]

 `--api-key-arn <arn>` *(optional)*
API key ARN for non-Bedrock harness providers [non-interactive]

 `--api-base <url>` *(optional)*
Base URL for the harness model provider API endpoint (lite\_llm) [non-interactive]

 `--additional-params <json>` *(optional)*
Provider-specific harness params as a JSON object (lite\_llm) [non-interactive]

 `--no-harness-memory` *(optional)*
Disable memory for the harness (this is the default) [non-interactive]

 `--max-iterations <n>` *(optional)*
Max agent loop iterations (harness) [non-interactive]

 `--max-tokens <n>` *(optional)*
Max tokens per iteration (harness) [non-interactive]

 `--timeout <seconds>` *(optional)*
Max execution duration in seconds (harness) [non-interactive]

 `--truncation-strategy <strategy>` *(optional)*
Truncation strategy: sliding\_window or summarization (harness) [non-interactive]

 `--container <uri-or-path>` *(optional)*
Container image URI or Dockerfile path (harness) [non-interactive]

### agentcore deploy
<a name="_agentcore_deploy"></a>

```
agentcore deploy|dp [options]
```

Deploy project infrastructure to AWS via CDK.

 **Parameters**

 `--target <target>` *(optional)*
Deployment target name (default: "default") [non-interactive]

 `-y, --yes` *(optional)*
Auto-confirm prompts, read credentials from env [non-interactive]

 `-v, --verbose` *(optional)*
Show resource-level deployment events [non-interactive]

 `--json` *(optional)*
Output as JSON [non-interactive]

 `--dry-run` *(optional)*
Preview deployment without deploying [non-interactive]

 `--diff` *(optional)*
Show CDK diff without deploying [non-interactive]

### agentcore dev
<a name="_agentcore_dev"></a>

```
agentcore dev|d [options] [prompt]
```

Launch local dev server, or invoke an agent locally.

 **Parameters**

 `prompt`
Send a prompt to a running dev server [non-interactive]

 `-p, --port <port>` *(optional)*
Port for development server. Used as-is when set explicitly; the default is offset by the runtime index in multi-runtime projects. (default: "8080")

 `-r, --runtime <name>` *(optional)*
Runtime to run or invoke (required if multiple runtimes)

 `-s, --stream` *(optional)*
Stream response when invoking [non-interactive]

 `-l, --logs` *(optional)*
Run dev server with logs to stdout [non-interactive]

 `--exec` *(optional)*
Execute a shell command in the running dev container (Container agents only) [non-interactive]

 `--tool <name>` *(optional)*
MCP tool name (used with "call-tool" prompt) [non-interactive]

 `--input <json>` *(optional)*
MCP tool arguments as JSON (used with --tool) [non-interactive]

 `--skip-deploy` *(optional)*
Skip automatic resource deployment before starting dev server

 `-H, --header <header>` *(optional)*
Custom header to forward to the agent (format: "Name: Value", repeatable) [non-interactive] (default: [])

 `-b, --no-browser` *(optional)*
Use terminal TUI instead of web-based chat UI

 `--no-traces` *(optional)*
Disable local OTEL trace collection

### agentcore package
<a name="_agentcore_package"></a>

```
agentcore package|pkg [options]
```

Package agent artifacts without deploying.

 **Parameters**

 `-d, --directory <path>` *(optional)*
Project directory containing agentcore config

 `-r, --runtime <name>` *(optional)*
Package only the specified runtime

### agentcore export
<a name="_agentcore_export"></a>

```
agentcore export [options] [command]
```

Export a harness to a Strands runtime agent.

### agentcore update
<a name="_agentcore_update"></a>

```
agentcore update [options] [command]
```

Check for and install CLI updates

 **Parameters**

 `-c, --check` *(optional)*
Check for updates without installing

### agentcore validate
<a name="_agentcore_validate"></a>

```
agentcore validate [options]
```

Validate agentcore/ config files.

 **Parameters**

 `-d, --directory <path>` *(optional)*
Project directory containing agentcore config

 `--json` *(optional)*
Output as JSON [non-interactive]

## Resource Management
<a name="cli-resources"></a>

 *Auto-generated from `@aws/agentcore` v0.24.2 — do not edit by hand.*

### agentcore add
<a name="_agentcore_add"></a>

```
agentcore add [options] [command] [subcommand]
```

Add resources to project config.

### agentcore remove
<a name="_agentcore_remove"></a>

```
agentcore remove [options] [command] [subcommand]
```

Remove resources from project config.

### agentcore import
<a name="_agentcore_import"></a>

```
agentcore import [options] [command]
```

Import a runtime, memory, or starter toolkit into this project.

 **Parameters**

 `--source <path>` *(optional)*
Path to the .bedrock\_agentcore.yaml configuration file

 `--target <target>` *(optional)*
Deployment target name (only needed if project has multiple targets)

 `-y, --yes` *(optional)*
Auto-confirm prompts

## Optimization & Config Bundles
<a name="cli-optimization"></a>

 *Auto-generated from `@aws/agentcore` v0.24.2 — do not edit by hand.*

### agentcore config-bundle
<a name="_agentcore_config_bundle"></a>

```
agentcore config-bundle|cb [options] [command]
```

Manage configuration bundles (use bundle name from agentcore.json, not the ID)

### agentcore promote
<a name="_agentcore_promote"></a>

```
agentcore promote [options] [command]
```

Promote resources

### agentcore archive
<a name="_agentcore_archive"></a>

```
agentcore archive [options] [command]
```

Archive (delete) a batch evaluation or recommendation on the service and clear local history.
