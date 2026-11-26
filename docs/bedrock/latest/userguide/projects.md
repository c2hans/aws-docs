---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/projects.html
---

# Projects

Amazon Bedrock projects give each of your generative AI workloads its own boundary within an AWS account. Projects enable you to organize and manage your AI applications with improved access control, cost tracking, and observability across your organization.

**Note**
Support for projects on the bedrock-runtime endpoint is in preview release and is subject to change. The preview is available in all commercial AWS Regions where Amazon Bedrock is available.

## What is a project?
<a name="projects-what-is"></a>

A project is a logical boundary used to isolate workloads such as applications, environments, or experiments within Amazon Bedrock. Projects provide:
+ **Access isolation:** Control who can run inference in each project with IAM policies on the project's Amazon Resource Name (ARN).
+ **Cost monitoring:** Track spending at the project level with AWS tags, AWS Cost Explorer, and AWS Data Exports (CUR 2.0).
+ **Observability:** Monitor each project's invocations, tokens, latency, and errors in Amazon CloudWatch, and find the project in each model invocation log record.

A project works with every foundation model and with the InvokeModel, Converse, Messages, Responses, and Chat Completions APIs on the bedrock-runtime endpoint. A project belongs to one AWS Region, and each inference request runs in one project.

Each AWS account has a default project in each Region. Requests that don't name a project run in the default project and are billed as before. You can create more projects in your account with the `CreateProject` API. You can't rename or archive the default project.

### Projects vs. AWS accounts
<a name="projects-vs-aws-accounts"></a>

AWS accounts and AWS Organizations are billing and ownership boundaries at the infrastructure level. Projects are workload and application boundaries within a single account. You can create a project in seconds with an API call, so you can run many workloads in one account instead of creating an account for each. You manage all of them in one place, with no cross-account IAM roles or resource sharing.

## When to use projects
<a name="projects-when-to-use"></a>

Use projects when you need to:
+ **Organize by business structure:** Manage Amazon Bedrock usage based on your organizational taxonomy, such as business units, teams, applications, or cost centers.
+ **Track costs accurately:** Monitor and allocate AI spending to specific teams, projects, or environments.
+ **Enforce access policies:** Apply granular IAM permissions to control who can run inference for specific AI workloads.
+ **Set data handling per workload:** Give one workload a different data retention mode than the rest of your account, or enroll one workload in a trusted access program.

## Projects vs. application inference profiles
<a name="projects-vs-inference-profiles"></a>

We recommend projects to control access and track cost for each workload, because one project covers every model and API that the workload calls. A request can use a project or an application inference profile, not both. Features that take a model ARN instead of a project, such as knowledge bases, model evaluation, Prompt management, and flows, use application inference profiles to track cost.

## Getting started with projects
<a name="projects-getting-started"></a>

This section walks you through creating your first project, allowing a role to use it, and running inference in it.

### Prerequisites
<a name="projects-prerequisites"></a>

Before you begin, you need an AWS account with access to Amazon Bedrock models, and IAM permissions to create projects and run inference. You also need AWS CLI version 2.42.0 or later, or the AWS SDK for Python (Boto3) version 1.44.10 or later.

### Step 1: Create a project
<a name="projects-create-first"></a>

Create the project in the AWS Region where your workload runs. Only a name is required. Add tags now to track the project's cost later.

------
#### [ AWS CLI ]

```bash
aws bedrock create-project \
    --name CustomerChatbot-Prod \
    --tags key=Project,value=CustomerChatbot key=Environment,value=Production key=CostCenter,value=21524
```

------
#### [ Python (Boto3) ]

```python
import boto3

bedrock = boto3.client("bedrock", region_name="us-east-1")
project = bedrock.create_project(
    name="CustomerChatbot-Prod",
    tags=[
        {"key": "Project", "value": "CustomerChatbot"},
        {"key": "Environment", "value": "Production"},
        {"key": "CostCenter", "value": "21524"},
    ],
)
print(project["id"], project["arn"])
```

------

The response includes the project's `id`, such as `proj_abcdefghijklmnopqrst`, which you add to inference requests, and its `arn`, which you use in IAM policies.

### Step 2: Allow a role to use the project
<a name="projects-allow-role"></a>

To run inference in a project, a role needs `bedrock:InvokeModel` on both the model and the project. For streaming, it also needs `bedrock:InvokeModelWithResponseStream`. The following policy lets a role call Amazon Nova models in one project.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"],
            "Resource": [
                "arn:aws:bedrock:*::foundation-model/amazon.nova-*",
                "arn:aws:bedrock:{{us-east-1}}:{{123456789012}}:inference-profile/us.amazon.nova-*",
                "arn:aws:bedrock:{{us-east-1}}:{{123456789012}}:project/proj_abcdefghijklmnopqrst"
            ]
        }
    ]
}
```

### Step 3: Run inference in the project
<a name="projects-associate-inference"></a>

To run inference in a project, add the project ID to your request. The following example uses the Converse API.

------
#### [ AWS CLI ]

```bash
aws bedrock-runtime converse \
    --model-id us.amazon.nova-micro-v1:0 \
    --project-identifier proj_abcdefghijklmnopqrst \
    --messages '[{"role": "user", "content": [{"text": "Explain the benefits of using projects in Amazon Bedrock"}]}]'
```

------
#### [ Python (Boto3) ]

```python
import boto3

runtime = boto3.client("bedrock-runtime", region_name="us-east-1")
response = runtime.converse(
    modelId="us.amazon.nova-micro-v1:0",
    projectIdentifier="proj_abcdefghijklmnopqrst",
    messages=[{"role": "user", "content": [{"text": "Explain the benefits of using projects in Amazon Bedrock"}]}],
)
print(response["output"]["message"]["content"][0]["text"])
```

------

The request runs in the project, and its cost, metrics, and logs carry the project. For the other APIs, see [Using projects with different APIs](#projects-using-apis).

### Step 4: Verify your project setup
<a name="projects-verify-setup"></a>

To verify that the project was created, list your projects. The response includes the project's `id`, `name`, and `status`.

```bash
aws bedrock list-projects
```

## Working with projects
<a name="projects-working-with"></a>

This section describes how to manage projects throughout their lifecycle.

### Creating projects
<a name="projects-creating"></a>

You can have up to 10,000 active projects per account in each Region. Project names don't have to be unique, but names that reflect your organizational structure make projects easier to manage. For example, name projects by application (CustomerChatbot-Prod), team (TeamAlpha-Production), environment (Staging-MobileApp), or cost center (CostCenter-2152-Production).

### Listing and retrieving projects
<a name="projects-listing"></a>

```bash
# List active projects (omit --status-filter to list all)
aws bedrock list-projects --status-filter active

# Get one project
aws bedrock get-project --project-identifier proj_abcdefghijklmnopqrst
```

### Updating projects
<a name="projects-updating"></a>

Each `update-project` call changes one field: the name or the data retention mode.

```bash
aws bedrock update-project \
    --project-identifier proj_abcdefghijklmnopqrst \
    --name CustomerChatbot-Prod-v2
```

### Managing project tags
<a name="projects-managing-tags"></a>

Add, list, and remove tags with the Amazon Bedrock tagging operations. To see a project's tags, use `list-tags-for-resource`, because `get-project` and `list-projects` don't return tags.

```bash
aws bedrock tag-resource \
    --resource-arn arn:aws:bedrock:us-east-1:111122223333:project/proj_abcdefghijklmnopqrst \
    --tags key=Team,value=Engineering

aws bedrock list-tags-for-resource \
    --resource-arn arn:aws:bedrock:us-east-1:111122223333:project/proj_abcdefghijklmnopqrst

aws bedrock untag-resource \
    --resource-arn arn:aws:bedrock:us-east-1:111122223333:project/proj_abcdefghijklmnopqrst \
    --tag-keys Team
```

### Setting data retention mode
<a name="projects-data-retention"></a>

A project uses your account's data retention mode in its Region until you set one on the project. To set a mode, specify `dataRetention` when you create the project, or update it later:

```bash
aws bedrock update-project \
    --project-identifier proj_abcdefghijklmnopqrst \
    --data-retention mode=none
```

For the modes and how project and account settings combine, see [Data retention](data-retention.md). To enroll a single project in a trusted access program, see [Trusted access programs](trusted-access-programs.md).

### Tracking cost and usage
<a name="projects-cost-usage"></a>

To see each project's spend, activate your project tags as cost allocation tags in the AWS Billing and Cost Management console. Within 24 hours, AWS Cost Explorer and AWS Data Exports (CUR 2.0) show cost by project. In CUR 2.0, requests in a project carry the project ARN as their resource ID. Requests in the default project carry the model or inference profile ARN, as before.

Amazon CloudWatch metrics for Amazon Bedrock include a `ProjectId` dimension, so you can monitor invocations, tokens, latency, and errors for each project. If you turn on [model invocation logging](model-invocation-logging.md), each log record includes the project ARN.

### Archiving projects
<a name="projects-archiving"></a>

Archive projects that are no longer in use:

```bash
aws bedrock archive-project --project-identifier proj_abcdefghijklmnopqrst
```

**Important**
Archiving is permanent. Archived projects can't be used for new inference requests or updated. For 30 days after you archive a project, you can still get it and list it with `--status-filter archived`.

### Using projects with different APIs
<a name="projects-using-apis"></a>

To run inference in a project, add the project ID to your request. The following table shows where to add it for each API.

| API | Where to add the project ID |
| --- | --- |
| Converse, ConverseStream | projectIdentifier in the request body |
| InvokeModel, InvokeModelWithResponseStream | X-Amzn-Bedrock-ProjectIdentifier header |
| Responses, Chat Completions | OpenAI-Project header |
| Messages | anthropic-workspace-id header |

Specify the ID of a project that you created with the `CreateProject` API. The bedrock-runtime endpoint doesn't accept OpenAI project IDs or project IDs from the bedrock-mantle endpoint.

**Important**
Converse ignores the `X-Amzn-Bedrock-ProjectIdentifier` header. If you send the project in that header instead of the request body, the request runs in your default project.

------
#### [ InvokeModel ]

```python
import json
import boto3

runtime = boto3.client("bedrock-runtime", region_name="us-east-1")
response = runtime.invoke_model(
    modelId="us.amazon.nova-micro-v1:0",
    projectIdentifier="proj_abcdefghijklmnopqrst",
    body=json.dumps({"messages": [{"role": "user", "content": [{"text": "Hello"}]}]}),
)
```

------
#### [ Responses ]

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://bedrock-runtime.us-east-1.amazonaws.com/openai/v1",
    api_key=os.environ["AWS_BEARER_TOKEN_BEDROCK"],
    project="proj_abcdefghijklmnopqrst",
)
response = client.responses.create(
    model="global.openai.gpt-5.6-sol",
    input="What are the key features of Amazon Bedrock?",
)
print(response.output_text)
```

------
#### [ Chat Completions ]

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://bedrock-runtime.us-east-1.amazonaws.com/openai/v1",
    api_key=os.environ["AWS_BEARER_TOKEN_BEDROCK"],
    project="proj_abcdefghijklmnopqrst",
)
response = client.chat.completions.create(
    model="openai.gpt-oss-120b-1:0",
    messages=[{"role": "user", "content": "Explain how projects improve security"}],
)
print(response.choices[0].message.content)
```

------
#### [ Messages ]

```python
from anthropic import Anthropic
from aws_bedrock_token_generator import provide_token

client = Anthropic(
    base_url="https://bedrock-runtime.us-east-1.amazonaws.com/anthropic",
    api_key=provide_token(region="us-east-1"),
    default_headers={"anthropic-workspace-id": "proj_abcdefghijklmnopqrst"},
)
message = client.messages.create(
    model="global.anthropic.claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
)
print(message.content[0].text)
```

------

For Claude Code, set `ANTHROPIC_CUSTOM_HEADERS="X-Amzn-Bedrock-ProjectIdentifier: proj_abcdefghijklmnopqrst"`.

A project can run foundation models and cross-Region inference profiles. To use Provisioned Throughput or a custom or imported model, send the request without a project. If the project doesn't exist, is archived, or is in another Region, the request fails with `ValidationException`: "The provided project identifier is invalid."

### Best practices
<a name="projects-best-practices"></a>

Create a separate project for each application or service, and separate projects for development, staging, and production:

```
├── CustomerChatbot-Production
├── CustomerChatbot-Staging
├── CustomerChatbot-Development
├── InternalSearch-Production
└── InternalSearch-Development
```

Use dedicated projects for experiments and proofs of concept. Create projects before you deploy applications, and follow your organization's naming conventions. Periodically review and archive projects that you no longer use, and track project metrics to find optimization opportunities.

**Note**
To use projects and workspaces with the OpenAI-compatible and Anthropic-compatible APIs on the bedrock-mantle endpoint, see [Projects and workspaces on the bedrock-mantle endpoint](workspaces.md).
