---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-bma.html
---

# Get started with Amazon Bedrock Managed Agents (with OpenAI) on AgentCore Runtime
<a name="runtime-get-started-bma"></a>

**Note**
Amazon Bedrock Managed Agents (with OpenAI) is in preview. Features and APIs may change before general availability.

Amazon Bedrock Managed Agents runs the OpenAI Codex harness on AWS. The harness runs the loop between the model and the tools, keeps the session, and compacts context as the conversation grows. When the agent must run a command or work with files, Bedrock Managed Agents sends the work to an environment. You decide where that environment runs.

You can run the Codex exec-server on your own computer for local development. For other workloads, Bedrock Managed Agents invokes an AgentCore Runtime in your account. The Runtime gives each session its own microVM. The session runs under an execution role that you control, and the Runtime can connect to your VPC so that the agent can reach private resources. The model calls stay in Bedrock Managed Agents, so the container runs only the commands that the agent sends.

In this tutorial, you do these tasks:
+ Create and deploy the Runtime with the AgentCore CLI.
+ Start a session with the OpenAI SDK. The agent uses a sample skill in your Runtime.
+ (Optional) Add your own skills.

Steps 1 to 4 take about 15 minutes.

The AWS resources that you create in this tutorial might result in charges to your AWS account. These resources include the Runtime, the AWS CodeBuild image builds, and the Bedrock Managed Agents model calls. For more information, see [AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/). To stop the charges, remove the resources in [Step 8: Clean up](#runtime-get-started-bma-clean-up).

## Prerequisites
<a name="runtime-get-started-bma-prerequisites"></a>
+  **Node.js 20 or later.** The AgentCore CLI is distributed as an npm package. Check with `node --version`.
+  **uv.** The sample client uses [uv](https://docs.astral.sh/uv/) to install its Python dependencies.
+  **An AWS account with credentials configured.** To create an account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). To configure credentials, see [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
+  **IAM permissions.** Your identity needs permissions to make AgentCore API calls and to assume the CDK bootstrap roles used during deployment. See [Use the AgentCore CLI](runtime-permissions.md#runtime-permissions-cli).
+  **Model access.** Your account needs access to the Bedrock Managed Agents model `openai.gpt-5.6-luna`.

The CLI builds the container image with AWS CodeBuild in your account.

## Step 1: Create the project
<a name="runtime-get-started-bma-create"></a>

Install the AgentCore CLI, and set your credentials and Region:

```
npm install -g @aws/agentcore
agentcore --version

export AWS_PROFILE=your-profile
export AWS_REGION=us-east-1
```

Create the project with the `BedrockManagedAgents` framework. You can also run `agentcore create` with no flags. Select **Agent**, and then select **Bedrock Managed Agents** as the framework.

```
agentcore create --name MyManagedAgent --framework BedrockManagedAgents
cd MyManagedAgent
```

The project has the Runtime configuration in `agentcore/agentcore.json` and the container source in `app/MyManagedAgent/`. The container runs `codex exec-server`, which connects out to Bedrock Managed Agents and runs the commands of the agent.

The project configures the Runtime with these defaults:
+ A 30 minute idle timeout and an 8 hour maximum lifetime. See [Configure lifecycle settings](runtime-lifecycle-settings.md).
+ An execution role with the permissions in `bma-acr-policy.json`.

### Project structure
<a name="runtime-get-started-bma-project-structure"></a>

```
MyManagedAgent/
├── agentcore/
│   ├── agentcore.json
│   └── cdk/
└── app/MyManagedAgent/
    ├── Dockerfile
    ├── lifecycle/server.py
    ├── otel/collector.yaml
    ├── plugins/acr-report/
    ├── bma-acr-policy.json
    ├── pyproject.toml
    ├── client.py
    └── README.md
```

Key files:
+  `lifecycle/server.py` - The lifecycle server. Bedrock Managed Agents calls it to start `codex exec-server` in your Runtime session. Do not change this file.
+  `Dockerfile` - Installs Codex, the CloudWatch agent, and Python, and copies `lifecycle/`, `otel/`, and `plugins/` to `/opt/bma`.
+  `otel/collector.yaml` - Sends the spans and logs of the exec-server to CloudWatch.
+  `plugins/acr-report/` - A sample plugin with one skill. The skill saves `acr-report.txt` in the workspace.
+  `bma-acr-policy.json` - Allows `bedrock-mantle:RegisterEnvironment` and `bedrock-mantle:ConnectEnvironment`. To limit it to one project, change `Resource` to `arn:aws:bedrock-mantle:<region>:<account-id>:project/<project-id>`.
+  `pyproject.toml` - The Python dependencies. The `dev` group is for `client.py` only.
+  `client.py` - A sample client that starts a session. You run it in Step 3.

### Deploy the Runtime in a VPC
<a name="runtime-get-started-bma-vpc"></a>

Add the network options to `agentcore create`:

```
agentcore create --name MyManagedAgent --framework BedrockManagedAgents \
  --network-mode VPC --vpc-id <vpc-id> --subnets <subnet-ids> \
  --security-groups <security-group-ids>
```

The VPC must have a route to the Bedrock Managed Agents endpoint, because the exec-server connects out to it. The image build downloads Codex and Python, so it also needs a route to the internet. See [Configure AgentCore for VPC](agentcore-vpc.md).

### Run the Runtime on Instances
<a name="runtime-get-started-bma-instances"></a>

The same project runs on the **Instances** compute type. Add a capacity provider to the project, and then add the agent with the capacity provider:

```
agentcore create --name MyManagedAgent --no-agent
cd MyManagedAgent
agentcore add capacity-provider --name MyCapacityProvider \
  --subnets <subnet-ids> --security-groups <security-group-ids> \
  --os LINUX_ARM64 --instance-types c7g.large
agentcore add agent --name MyManagedAgent --framework BedrockManagedAgents \
  --capacity-provider MyCapacityProvider
```

Then continue with [Step 2: Deploy](#runtime-get-started-bma-deploy). `agentcore deploy` also creates the capacity provider and its operator role.
+ Use `LINUX_ARM64` and Graviton instance types, because the image build makes an ARM64 image.
+ The capacity provider gives the network. The subnets must have a route to the Bedrock Managed Agents endpoint.

To attach a capacity provider that is not in the project, give its ARN to `agentcore create --framework BedrockManagedAgents --capacity-provider <capacity-provider-arn>`. See [Runtime Instances and capacity providers](runtime-instances.md).

## Step 2: Deploy
<a name="runtime-get-started-bma-deploy"></a>

```
agentcore deploy
agentcore status
```

The CLI builds the image with AWS CodeBuild in your account, and deploys the Runtime and its execution role. Bedrock Managed Agents invokes the Runtime for you.

Save the Runtime ARN from the output of `agentcore status`:

```
arn:aws:bedrock-agentcore:us-east-1:<account-id>:runtime/<runtime-id>
```

## Step 3: Run a session
<a name="runtime-get-started-bma-client"></a>

Bedrock Managed Agents must have permission to invoke your Runtime. This permission is separate from the Runtime execution role.

Run the client from the agent directory:

```
cd app/MyManagedAgent
uv run client.py --runtime <runtime-arn>
```

The client creates a session and prints the session ID, each command with its output, and the answer of the agent. By default, the agent uses the `acr-report` skill to save `acr-report.txt` in the workspace.

### How the client works
<a name="runtime-get-started-bma-client-code"></a>

The client uses the `client.beta.agents` resources of the `openai` package. Bedrock Managed Agents runs the agent loop.

When the client creates the session, it sets these values in `environment`:
+  `type` - `aws_bedrock_agentcore`, which tells Bedrock Managed Agents to use an AgentCore Runtime.
+  `runtime_arn` - Your Runtime. The session runs in the Region of the Runtime.
+  `workspace_directory` - The directory where the agent runs its commands. The client uses `/home/app/workspace`. The lifecycle server creates the directory.
+  `runtime_qualifier` - The endpoint of the Runtime. The client uses `DEFAULT`.
+  `capability_directories` - The directories where Bedrock Managed Agents finds skills. The client uses `/opt/bma/plugins`.

The `provide_token` helper uses your AWS credentials to get a short-lived Amazon Bedrock bearer token for each request.

```
"""Send an input to a Bedrock Managed Agents session that uses this project's ACR."""

import argparse
import json
from typing import Any

from aws_bedrock_token_generator import provide_token
from openai import NotFoundError, OpenAI

BMA_MODEL_ID = "openai.gpt-5.6-luna"
# The agent runs its commands in this directory. The lifecycle server creates it.
WORKSPACE_DIRECTORY = "/home/app/workspace"
# Plugins and skills that the agent can use. The image has the acr-report plugin
# at this path. Add the path of an S3 Files mount to use the skills in a bucket.
CAPABILITY_DIRECTORIES = ["/opt/bma/plugins"]
TURN_END = ("completed", "failed", "cancelled")
TOOL_CALLS = ("mcp_call", "function_call", "web_search_call")

def show(data: dict[str, Any]) -> None:
    """Prints the session ID, the commands, the tool calls, and the answer."""
    kind = data["type"].removeprefix("agent.session.")
    item = data.get("item") or {}
    if kind == "created":
        print(f"Session {data['session']['id']}")
    elif kind == "turn.output_text.delta":
        print(data["delta"], end="", flush=True)
    elif kind == "turn.item.done" and item.get("type") == "command_execution":
        print(f"\n$ {item['command']}\n{item.get('output') or ''}".rstrip())
    elif kind == "turn.item.done" and item.get("type") in TOOL_CALLS:
        print(f"\nTool {item.get('name') or item['type']} {item.get('status')}")
    elif kind == "error" or kind.split(".")[-1] in TURN_END:
        source = data.get("turn") or data.get("environment") or data.get("session")
        print(f"\n{kind} {(source or data).get('error') or ''}".rstrip())

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", required=True, help="The ACR ARN.")
    parser.add_argument(
        "--session-id",
        help="The BMA session ID. If it does not exist, the client creates a session.",
    )
    parser.add_argument(
        "--input",
        default="Use the acr-report skill to save an ACR report in the workspace.",
    )
    parser.add_argument(
        "--gateway",
        help="The Gateway URL from the output of `agentcore deploy`.",
    )
    parser.add_argument("--delete", action="store_true", help="Delete the session.")
    parser.add_argument("--raw", action="store_true", help="Print events as JSON.")
    args = parser.parse_args()
    # BMA must run in the Region of the ACR.
    region = args.runtime.split(":")[3]

    with OpenAI(
        api_key=lambda: provide_token(region=region),
        base_url=f"https://bedrock-mantle.{region}.api.aws/openai/v1",
    ) as client:
        sessions = client.beta.agents.sessions
        session_id = args.session_id
        if session_id:
            try:
                session = sessions.retrieve(session_id).model_dump(warnings=False)
            except NotFoundError:
                print(f"Session {session_id} does not exist.")
                session_id = None
            else:
                if session["environment"].get("runtime_arn") != args.runtime:
                    raise ValueError(f"Session {session_id} uses another ACR.")

        if session_id:
            # BMA opens the stream only with stream=true, and the SDK does not send it.
            events = sessions.events.stream(session_id, extra_query={"stream": "true"})
            message = {
                "role": "user",
                "content": [{"type": "input_text", "text": args.input}],
            }
            sessions.events.create(
                session_id,
                events=[{"type": "agent.session.input.message", "input": [message]}],
            )
        else:
            agent: dict[str, Any] = {
                "model": BMA_MODEL_ID,
                "instructions": "Use the available tools to complete the task.",
            }
            if args.gateway:
                # Bedrock Managed Agents calls Gateway with IAM from the service side.
                agent["tools"] = [
                    {
                        "type": "mcp",
                        "server_label": "team_tools",
                        "required": True,
                        "connection_origin": "service",
                        "transport": {"type": "http", "server_url": args.gateway},
                    }
                ]
                args.input += (
                    " Then use the Gateway's documentation and runbook tools to explain"
                    " how to investigate an MCP connection failure. Cite your sources."
                )
            events = sessions.create(
                agent=agent,
                environment={
                    "type": "aws_bedrock_agentcore",
                    "runtime_arn": args.runtime,
                    "runtime_qualifier": "DEFAULT",
                    "workspace_directory": WORKSPACE_DIRECTORY,
                    "capability_directories": CAPABILITY_DIRECTORIES,
                },
                input=args.input,
                stream=True,
            )

        with events:
            for event in events:
                data = event.model_dump(mode="json", warnings=False)
                session_id = session_id or (data.get("session") or {}).get("id")
                if args.raw:
                    print(json.dumps(data), flush=True)
                else:
                    show(data)
                if data["type"].removeprefix("agent.session.turn.") in TURN_END:
                    break

        if args.delete:
            sessions.delete(session_id)
            print(f"\nDeleted session {session_id}")

if __name__ == "__main__":
    main()
```

## Step 4: Continue the session
<a name="runtime-get-started-bma-continue"></a>

To send another input to the same session, add the session ID. The turn uses the same workspace. To keep the workspace after an idle stop, add session storage as in [Keep files after an idle stop](#runtime-get-started-bma-keep-files).

```
uv run client.py --runtime <runtime-arn> --session-id <session-id> \
  --input "Run cat acr-report.txt and show the output."
```

If the session does not exist, the client creates a new session. Add `--delete` to delete the session after the turn, or `--raw` to print each event as JSON.

### Keep files after an idle stop
<a name="runtime-get-started-bma-keep-files"></a>

On a microVM Runtime, put the home directory of the exec-server on session storage. Then the workspace, the connection state, and `CODEX_HOME` stay after an idle stop.

1. Instead of the command in Step 1, create the project with session storage:

   ```
   agentcore create --name MyManagedAgent --framework BedrockManagedAgents \
     --session-storage-mount-path /mnt/home
   cd MyManagedAgent
   ```

1. In `agentcore/agentcore.json`, add this variable to the entry for the Runtime:

   ```
   "envVars": [{ "name": "BMA_HOME_DIR", "value": "/mnt/home" }]
   ```

1. In `client.py`, set `WORKSPACE_DIRECTORY = "/mnt/home/workspace"`.

1. Deploy, and run the client.

For more information about session storage, see [File system configurations for AgentCore Runtime](runtime-filesystem-configurations.md).

## Step 5: (Optional) Add skills
<a name="runtime-get-started-bma-skills"></a>

To add a skill to the image, add a plugin under `plugins/` and deploy. A plugin has a `.codex-plugin/plugin.json` file and a `skills/` directory. The `skills/` directory has one subdirectory for each skill, with a `SKILL.md` file in it. The image copies it to `/opt/bma/plugins`, which the client already gives to Bedrock Managed Agents.

To start, copy `plugins/acr-report/`, and rename the plugin directory and `skills/acr-report/` to the name of your plugin and your skill. In `plugin.json`, set `name`, `version`, `description`, and `"skills": "./skills/"`. Each `SKILL.md` starts with front matter that has `name` and `description`. After the deploy, start a new session with `--input "Use the <skill-name> skill to …​"`.

### Share skills from an Amazon S3 bucket
<a name="runtime-get-started-bma-skills-s3"></a>

Mount an S3 Files access point in the Runtime. Then the skills change when the bucket changes, and the image stays the same. For the S3 Files file system, the access point, and the security group rules, see [File system configurations for AgentCore Runtime](runtime-filesystem-configurations.md).

An S3 Files mount needs a Runtime in VPC network mode. Create the project with the network options in [Deploy the Runtime in a VPC](#runtime-get-started-bma-vpc).

In the bucket, put each plugin in its own directory under the root directory of the access point. Use the same layout as `plugins/acr-report/`: `<plugin>/.codex-plugin/plugin.json` and `<plugin>/skills/<skill>/SKILL.md`.

Add the mount to the entry for the Runtime in `agentcore/agentcore.json`:

```
{
  "filesystemConfigurations": [
    {
      "s3FilesAccessPoint": {
        "accessPointArn": "arn:aws:s3files:us-east-1:111122223333:file-system/fs-0123456789abcdef0/access-point/fsap-0123456789abcdef0",
        "mountPath": "/mnt/skills"
      }
    }
  ]
}
```

Then set `CAPABILITY_DIRECTORIES` in `client.py` to `["/opt/bma/plugins", "/mnt/skills"]`, and deploy.

## Step 6: View logs and traces
<a name="runtime-get-started-bma-observe"></a>

```
agentcore logs --since 15m
```

The first deploy turns on CloudWatch Transaction Search in your account. The traces show after about 10 minutes. To see the traces, open the CloudWatch console and choose **GenAI Observability**. Each call from Bedrock Managed Agents to the lifecycle server has one `bma.invocation` span. For more information, see [View observability data for your Amazon Bedrock AgentCore agents](observability-view.md).

**Transaction Search settings apply to the entire account**
Transaction Search and its span indexing apply to the entire account in the Region, and additional charges might apply. To keep your current settings, add `"disableTransactionSearch": true` to `~/.agentcore/config.json` before you deploy.

## Step 7: Update and redeploy
<a name="runtime-get-started-bma-update"></a>

Change the Runtime settings in `agentcore/agentcore.json`, or the files of the image, and deploy again. For example, this setting stops an idle session after 10 minutes. The values are in seconds.

```
{
  "lifecycleConfiguration": {
    "idleRuntimeSessionTimeout": 600,
    "maxLifetime": 28800
  }
}
```

```
agentcore deploy
```

The changes apply to new sessions.

### Environment variables of the lifecycle server
<a name="runtime-get-started-bma-env-vars"></a>

Add a variable to `envVars` in the entry for the Runtime, for example `{ "name": "DISABLE_ADOT_OBSERVABILITY", "value": "true" }`.

| Variable | Default | Description |
| --- | --- | --- |
|  `DISABLE_ADOT_OBSERVABILITY`  | Not set | Set to `true` to turn off the traces and the exec-server logs. The lifecycle server still writes its own logs to the log group of the Runtime. |
|  `BMA_HOME_DIR`  |  `/home/app`  |  `HOME` of the exec-server. |
|  `BMA_STATE_DIR`  |  `.bma` in `BMA_HOME_DIR`  | The directory of `state.json`, which keeps the connection state of the session. |
|  `BMA_CODEX_HOME`  |  `.codex` in `BMA_HOME_DIR`  |  `CODEX_HOME` of the exec-server. |
|  `BMA_CODEX_BINARY`  |  `/opt/bma/bin/codex`  | The Codex binary. |
|  `BMA_MAX_TURN_LEASE`  |  `300`  | The longest turn lease, in seconds. |

Each image build installs the latest Codex release. The lifecycle server needs Codex 0.154.0 or later. To pin a release, add `CODEX_RELEASE=<version>` next to `CODEX_NON_INTERACTIVE=1` in the `Dockerfile`.

## Step 8: Clean up
<a name="runtime-get-started-bma-clean-up"></a>

To delete a session, add `--delete` to the last run of the client for that session. Then remove the resources of the project, and deploy to delete the Runtime, its execution role, and the stack.

```
agentcore remove all
agentcore deploy
```

The deploy does not delete these resources:
+ The CloudWatch Logs log groups of the Runtime, of the CodeBuild project that builds the image, and of the Lambda function that starts the build.
+ The AWS KMS key of the Amazon ECR repository. The key stays in the **Pending deletion** state for 30 days, and then AWS KMS deletes it.
+ The `CDKToolkit` stack, if the first deploy bootstrapped the account and Region. Other AWS CDK apps can use this stack. Delete it only if no other app uses it.
+ The Transaction Search settings from Step 6.

To find the log groups, run these commands. Then delete each log group.

```
aws logs describe-log-groups --log-group-name-prefix /aws/bedrock-agentcore/runtimes/<project-name>_<agent-name>- --query 'logGroups[].logGroupName'
aws logs describe-log-groups --log-group-name-prefix /aws/codebuild/AgentCore-<project-name>-<target-name>- --query 'logGroups[].logGroupName'
aws logs describe-log-groups --log-group-name-prefix /aws/lambda/AgentCore-<project-name>-<target-name>- --query 'logGroups[].logGroupName'
aws logs delete-log-group --log-group-name <log-group-name>
```

Replace these values:
+  `<project-name>` - The name of the project. In Step 1, it is `MyManagedAgent`.
+  `<agent-name>` - The name of the agent. In Step 1, it is also `MyManagedAgent`.
+  `<target-name>` - The name of the deploy target in `agentcore/aws-targets.json`. The default is `default`. In the CodeBuild and Lambda names, each underscore (`_`) in the project name and the target name changes to a hyphen (`-`).

If you added other resources to the project, such as a gateway or a memory, check that the deploy deleted them.

## Related resources
<a name="runtime-get-started-bma-related"></a>
+  [Use the AgentCore CLI](runtime-permissions.md#runtime-permissions-cli)
+  [Configure lifecycle settings](runtime-lifecycle-settings.md)
+  [File system configurations for AgentCore Runtime](runtime-filesystem-configurations.md)
+  [Configure AgentCore for VPC](agentcore-vpc.md)
+  [Runtime Instances and capacity providers](runtime-instances.md)
+  [View observability data for your Amazon Bedrock AgentCore agents](observability-view.md)
