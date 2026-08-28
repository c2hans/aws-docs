---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/steps-to-build-mcp-server-docker-image.html
---

# Steps to build MCP server Docker Image
<a name="steps-to-build-mcp-server-docker-image"></a>

To use MCP (Model Context Protocol) servers with Generative AI Application Builder on AWS, you need a Docker image built and stored in a private Amazon ECR repository as the first step.

**Note**
As of now, existing deployed MCP servers in Amazon Bedrock AgentCore runtime cannot be exported into GAAB. For MCP servers to be attached to Agents created through GAAB, they need to be created through GAAB.

## Step 1: Create your MCP server
<a name="step-1-create-your-mcp-server"></a>

First, you need to have your MCP server implementation ready. For detailed instructions on creating an MCP server, refer to the [Amazon Bedrock AgentCore Developer Guide - Create an MCP server](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html#runtime-mcp-create-server).

We recommend the following project structure:

```
.
├── __init__.py
├── extras/
│   ├── extra_dependencies.py
│   ├── Dockerfile
├── requirements.txt
└── server.py <-- Server Entry point
```

For the Dockerfile structure, we recommend using a format similar to the following example:

```
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim
WORKDIR /app

# All environment variables in one layer
ENV UV_SYSTEM_PYTHON=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_NO_PROGRESS=1 \
    PYTHONUNBUFFERED=1 \
    DOCKER_CONTAINER=1 \
    AWS_REGION=us-east-1 \
    AWS_DEFAULT_REGION=us-east-1

COPY requirements.txt requirements.txt
# Install from requirements file
RUN uv pip install -r requirements.txt

RUN uv pip install aws-opentelemetry-distro>=0.10.1

# Signal that this is running in Docker for host binding logic
ENV DOCKER_CONTAINER=1

# Create non-root user
RUN useradd -m -u 1000 bedrock_agentcore
USER bedrock_agentcore

EXPOSE 9000
EXPOSE 8000
EXPOSE 8080

# Copy entire project (respecting .dockerignore)
COPY . .

# Use the full module path
CMD ["opentelemetry-instrument", "python", "-m", "server"]
```

## Step 2: Test your MCP server locally
<a name="step-2-test-your-mcp-server-locally"></a>

Before deploying to AWS, it’s important to test your MCP server locally to ensure it works as expected. For detailed instructions on local testing, refer to the [Amazon Bedrock AgentCore Developer Guide - Test your MCP server locally](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html#runtime-mcp-test-locally).

## Step 3: Deploy to Amazon ECR
<a name="step-3-deploy-to-amazon-ecr"></a>

Once your MCP server is created and tested locally, follow these steps to deploy it to Amazon ECR:

1. Make sure that you have the latest version of the AWS CLI and Docker installed. For more information, see [Getting Started with Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html).

1. Retrieve an authentication token and authenticate your Docker client to your registry. Use the AWS CLI:

   ```
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
   ```

1. Build your Docker image using the following command. For information on building a Docker file from scratch, see the [Docker documentation](https://docs.docker.com/engine/reference/builder/). You can skip this step if your image is already built:

   ```
   docker build -t <repository-name> .
   ```

1. After the build completes, tag your image so you can push the image to this repository:

   ```
   docker tag <repository-name>:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/<repository-name>:latest
   ```

1. Run the following command to push this image to your newly created AWS repository:

   ```
   docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/<repository-name>:latest
   ```

For complete deployment instructions, refer to the [Amazon Bedrock AgentCore Developer Guide - Deploy your MCP server to AWS](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html#runtime-mcp-deploy-aws).

## Step 4: Use the ECR URI in GAAB
<a name="step-4-use-the-ecr-uri-in-gaab"></a>

After successfully pushing your Docker image to Amazon ECR, copy the image URI from the ECR console. You will use this URI when deploying your MCP server through the Generative AI Application Builder on AWS deployment wizard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
