---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/workspaces.html
---

# Projects and workspaces on the bedrock-mantle endpoint

On the bedrock-mantle endpoint, projects and workspaces provide application-level isolation for your generative AI workloads. Projects work with the OpenAI-compatible APIs (Responses and Chat Completions), and workspaces work with the Anthropic-compatible Messages API. They enable you to segment your AI applications for cost tracking, observability, and access control.

**Tip**
For new applications, we recommend the bedrock-runtime endpoint. To organize workloads on bedrock-runtime, see [Projects](projects.md).

## What are projects and workspaces?
<a name="workspaces-what-is"></a>

A project is a logical boundary used to isolate workloads such as applications, environments, or experiments within Amazon Bedrock. A workspace is the same underlying resource: you manage both with the Projects API, and they provide the same capabilities:
+ **Access isolation**: Control who can access specific project resources using IAM policies for Amazon Bedrock Projects.
+ **Cost monitoring**: Track spending at the project level using AWS tags and AWS Cost Explorer.
+ **Observability**: Track usage metrics and patterns per project for monitoring and optimization.

Projects allow you to manage multiple generative AI workloads in production without creating separate AWS accounts or organizations, reducing operational complexity while maintaining security and governance.

Each AWS account has a default project. Requests that don't name a project are associated with it. You can create more projects using the Projects API, and reference them with the `OpenAI-Project` header or the `anthropic-workspace-id` header. Specify the ID of a project that you created with the Projects API. The bedrock-mantle endpoint doesn't accept OpenAI project IDs or project IDs from the bedrock-runtime endpoint.

## When to use projects and workspaces
<a name="workspaces-when-to-use"></a>

You should use projects and workspaces when you need to:
+ **Organize by business structure**: Manage Amazon Bedrock usage based on your organizational taxonomy such as business units, teams, applications, or cost centers.
+ **Track costs accurately**: Monitor and allocate AI spending to specific teams, projects, or environments.
+ **Enforce access policies**: Apply granular IAM permissions to control who can access specific AI workloads.
+ **Scale production workloads**: Run multiple production applications with clear operational boundaries and monitoring.

## Projects vs. workspaces
<a name="workspaces-vs-projects"></a>

Projects and workspaces are the same underlying resource. The difference is how you reference them in your inference requests, depending on which API you use:

| Feature | Projects | Workspaces |
| --- | --- | --- |
| Supported APIs | OpenAI-compatible APIs (Responses, Chat Completions) | Anthropic Messages API |
| Endpoint | bedrock-mantle.{region}.api.aws/v1 | bedrock-mantle.{region}.api.aws/anthropic/v1/messages |
| Header | OpenAI-Project: {project-id} | anthropic-workspace-id: {project-id} |
| Management API | Projects API | Projects API |
| Access control | Project as a resource in IAM policies | Project as a resource in IAM policies |
| Cost tracking | AWS tags on projects | AWS tags on projects |

## Getting started
<a name="workspaces-getting-started"></a>

This section walks you through creating a project, associating it with inference requests, and verifying your setup.

### Prerequisites
<a name="workspaces-prerequisites"></a>
+ An AWS account with Amazon Bedrock access
+ IAM permissions to create and manage Amazon Bedrock projects
+ An API key for Amazon Bedrock authentication
+ For workspaces, access to Claude models (see [Request access to models](model-access.md))

**Note**
Amazon Bedrock offers short-term and long-term API keys. We recommend short-term keys for applications with greater security requirements. The default policy attached to long-term keys only allows you to get and list projects. To create, update, or archive projects with a long-term key, assign additional IAM policies to the key.

### Step 1: Set up your environment
<a name="workspaces-setup-environment"></a>

```bash
export OPENAI_API_KEY="<your-bedrock-key>"
export OPENAI_BASE_URL="https://bedrock-mantle.<your-region>.api.aws/v1"
```

Replace `<your-region>` with your AWS Region, such as `us-east-1`.

### Step 2: Create a project
<a name="workspaces-create"></a>

Create a project with tags for cost monitoring. You use the same project as a workspace for Messages API requests.

```bash
curl -X POST $OPENAI_BASE_URL/organization/projects \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Project ABC",
    "tags": {
      "Project": "CustomerChatbot",
      "Environment": "Production",
      "Owner": "TeamAlpha",
      "CostCenter": "21524"
    }
  }'
```

Response:

```json
{
  "arn": "arn:aws:bedrock-mantle:us-east-1:111122223333:project/proj_5d5ykleja6cwpirysbb7",
  "created_at": 1772135628,
  "id": "proj_5d5ykleja6cwpirysbb7",
  "name": "Project ABC",
  "object": "organization.project",
  "status": "active",
  "tags": {
    "Project": "CustomerChatbot",
    "Environment": "Production",
    "Owner": "TeamAlpha",
    "CostCenter": "21524"
  }
}
```

The `id` field is the value that you pass in the `OpenAI-Project` or `anthropic-workspace-id` header. The `arn` field is specific to Amazon Bedrock and is the ARN for IAM policies. The `geography` parameter in the OpenAI API specification is ignored; the Region comes from your endpoint.

### Step 3: Associate requests with your project
<a name="workspaces-associate-requests"></a>

------
#### [ Responses (cURL) ]

```bash
curl -X POST $OPENAI_BASE_URL/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "OpenAI-Project: proj_5d5ykleja6cwpirysbb7" \
  -d '{
    "model": "openai.gpt-oss-120b",
    "input": "Explain the benefits of using projects in Amazon Bedrock"
  }'
```

------
#### [ OpenAI SDK (Python) ]

```python
from openai import OpenAI

client = OpenAI(project="proj_5d5ykleja6cwpirysbb7")

response = client.chat.completions.create(
    model="openai.gpt-oss-120b",
    messages=[{"role": "user", "content": "Explain how projects improve security"}],
)
print(response.choices[0].message.content)
```

------
#### [ Messages (cURL) ]

```bash
curl -X POST "https://bedrock-mantle.us-east-1.api.aws/anthropic/v1/messages" \
  -H "x-api-key: $OPENAI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-workspace-id: proj_5d5ykleja6cwpirysbb7" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic.claude-sonnet-4-6-v1",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello, how can you help me today?"}]
  }'
```

------
#### [ Anthropic SDK (Python) ]

```python
import os
import anthropic

client = anthropic.Anthropic(
    base_url="https://bedrock-mantle.us-east-1.api.aws/anthropic",
    api_key=os.environ["OPENAI_API_KEY"],
)
response = client.messages.create(
    model="anthropic.claude-sonnet-4-6-v1",
    max_tokens=1024,
    extra_headers={"anthropic-workspace-id": "proj_5d5ykleja6cwpirysbb7"},
    messages=[{"role": "user", "content": "Hello, how can you help me today?"}],
)
print(response.content[0].text)
```

------

All inference requests made with the same project ID are grouped together, enabling per-project cost tracking, access control, and observability.

### Step 4: Verify your setup
<a name="workspaces-verify"></a>

List your active projects to verify that your project was created:

```bash
curl -X GET $OPENAI_BASE_URL/organization/projects \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

## Working with projects and workspaces
<a name="workspaces-managing"></a>

You can have up to 1,000 projects per account. The following requests use the project from Getting started.

```bash
# Retrieve project details
curl -X GET $OPENAI_BASE_URL/organization/projects/proj_5d5ykleja6cwpirysbb7 \
  -H "Authorization: Bearer $OPENAI_API_KEY"

# Update the project name
curl -X POST $OPENAI_BASE_URL/organization/projects/proj_5d5ykleja6cwpirysbb7 \
  -H "Authorization: Bearer $OPENAI_API_KEY" -H "Content-Type: application/json" \
  -d '{"name": "Production Chatbot v2"}'

# Add or update tags
curl -X POST $OPENAI_BASE_URL/organization/projects/proj_5d5ykleja6cwpirysbb7 \
  -H "Authorization: Bearer $OPENAI_API_KEY" -H "Content-Type: application/json" \
  -d '{"add_tags": {"Application": "WebApp", "Version": "2.0", "Team": "Engineering"}}'

# Remove tags
curl -X POST $OPENAI_BASE_URL/organization/projects/proj_5d5ykleja6cwpirysbb7 \
  -H "Authorization: Bearer $OPENAI_API_KEY" -H "Content-Type: application/json" \
  -d '{"remove_tag_keys": ["Version", "OldTagKey"]}'

# Archive the project
curl -X POST $OPENAI_BASE_URL/organization/projects/proj_5d5ykleja6cwpirysbb7/archive \
  -H "Authorization: Bearer $OPENAI_API_KEY" -H "Content-Type: application/json"
```
+ **No full tag replacement**: There is no operation to replace the entire tag set at once. Specify which tags to add and which to remove.
+ **Tags in responses**: Tags that you specify are returned in all project responses.

**Important**
Archived projects cannot be used for new inference requests. You can still retrieve an archived project for 30 days after you archive it.

For IAM policies, see [IAM policies for Amazon Bedrock Projects](security-iam-projects.md). For AWS CloudFormation, see [Managing Projects with AWS CloudFormation](cloudformation-projects.md). For cost allocation, see [Projects](cost-mgmt-projects.md) in Track usage and costs.

## Best practices
<a name="workspaces-best-practices"></a>

**One project per application**: Create separate projects or workspaces for each distinct application or service.

```
├── CustomerChatbot-Production
├── CustomerChatbot-Staging
├── CustomerChatbot-Development
├── InternalSearch-Production
└── InternalSearch-Development
```
+ **Separate environments**: Use different projects for development, staging, and production environments.
+ **Experiment isolation**: Create dedicated projects for experiments and proofs of concept.
+ **Use clear names**: Use names that reflect your organization, such as CustomerChatbot-Prod or CostCenter-2152-Production.
+ **Tag for cost allocation**: Always include cost center and team tags.
+ **Regular audits**: Periodically review and archive unused projects.
