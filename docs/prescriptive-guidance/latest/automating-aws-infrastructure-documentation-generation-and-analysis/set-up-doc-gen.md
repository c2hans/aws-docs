---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automating-aws-infrastructure-documentation-generation-and-analysis/set-up-doc-gen.html
---

# Set up the Infrastructure Documentation Generator
<a name="set-up-doc-gen"></a>

This section describes how to build and run the Infrastructure Documentation Generator tool. It provides a systematic approach to setting up both the backend service (FastAPI) and the frontend application (React UI) so that you can scan, analyze, and visualize AWS infrastructure. The backend is responsible for discovering resources, generating documentation, and mapping dependencies. The frontend presents results in an interactive UI. Together, these components form a complete approach for understanding and optimizing AWS environments.

## Set up the backend service
<a name="set-up-backend"></a>

These instructions guide you through setting up the backend service, which is responsible for scanning AWS accounts and generating structured infrastructure data. The backend API layer is built with FastAPI, a modern Python web framework. FastAPI provides endpoints for infrastructure scanning, documentation generation, dependency mapping, and cache operations. The backend interacts with various AWS services and provides an API for managing and retrieving cloud infrastructure details.

### Prerequisites
<a name="prerequisites.ab52d2d2-d03b-5f8d-86f1-ed3b2ebe3dd6"></a>

Before you begin the setup, make sure you meet the following prerequisites:
+ [Python](https://www.python.org/downloads/) 3.9 or a later version installed on your machine.
+ [AWS credentials configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)—this prerequisite is mandatory. The tool requires AWS credentials to interact with your AWS account. You must use the AWS Command Line Interface (AWS CLI) `aws configure` command to configure your credentials to allow the service to access AWS resources.
+ Amazon Bedrock with access to Claude 3.7 Sonnet [enabled](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).

### Set up and run the backend environment
<a name="set-up-and-run-the-backend-environment.614a2abd-8a63-5ce4-a982-08e9ab06f981"></a>

To set up the backend environment, use the following steps:

1. To clone the repository, run the following command:

   `git clone https://github.com/awslabs/InfraDocGen.git`

1. To create and activate a virtual environment, run the following command:

   `python3 -m venv venv source venv/bin/activate`

1. To install backend dependencies, run the following command:

   `pip install -r requirements.txt`

1. To start the API server, run the following command:

   `uvicorn main:app --reload`

## Set up the frontend application
<a name="set-up-frontend"></a>

These instructions guide you through setting up the frontend application, which visualizes AWS resources, analysis reports, and dependency graphs in an interactive web UI. The frontend uses a React Flow library to render interactive, zoomable, and searchable graphs of AWS resource dependencies. The frontend application interacts with the backend service to display infrastructure data in a user-friendly and insightful way.

### Prerequisites
<a name="prerequisites.bc471f2e-c1fb-5e9f-9040-1ebebf4a9974"></a>
+ [Node.js v20\+ ](https://nodejs.org/en/download/)or a later version installed.
+ A package manager to install frontend dependencies, for example, [npm](https://docs.npmjs.com/) or [Yarn](https://yarnpkg.com/getting-started).

### Set up and run the frontend application
<a name="set-up-and-run-the-frontend-application.afd2bf76-e954-5448-a108-522c4854a31d"></a>

To set up the frontend environment and run the application, use the following steps.

1. To move to the UI project, run the following command:

   `cd infra-ui`

1. To create an environment file to connect to the backend service, run the following command:

   `echo "VITE_API_BASE_URL=http://127.0.0.1:8000" > .env`

1. To install frontend dependencies, run the following command:

   `npm install`

1. To start the frontend development server, run the following command:

   `npm run dev`

## Run the backend and the frontend together
<a name="run-both-together"></a>

After the backend service and the frontend application are set up successfully, you can run the full system to experience the complete functionality. To use the system effectively, start both the backend API server and the frontend UI in parallel, each in its own terminal window or tab.

To run the backend and the frontend together, use the following steps:

1. Start the backend API (`uvicorn main:app --reload`) in one terminal.

1. Start the frontend UI (`npm run dev`) in another terminal.

1. Open the UI at **http://localhost:3000"**. The UI connects automatically to the backend at **http://127.0.0.1:8000**.

From the UI, you can trigger scans, view service-wise expandable infrastructure data, explore dependency graphs, and download Markdown documentation.
