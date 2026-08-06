---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-meeting-intelligence-strands-agents-fargate.html
---

# Deploy Multi-Agent Meeting Intelligence Platform Using Strands Agents SDK and AWS Fargate
<a name="deploy-meeting-intelligence-strands-agents-fargate"></a>

*Aishita Batra and Muskan ., Amazon Web Services*

## Summary
<a name="deploy-meeting-intelligence-strands-agents-fargate-summary"></a>

This pattern deploys a multi-agent meeting intelligence platform on AWS Fargate that automatically generates structured minutes, executive summaries, audio narrations, and formatted PDF reports from meeting transcripts. The solution uses the Strands Agents SDK to orchestrate four specialized AI agents, Amazon Bedrock for language model inference, and Amazon Polly for text-to-speech conversion.

Users upload meeting transcripts through a Streamlit web interface, and the system processes them asynchronously through a coordinated agent pipeline. The infrastructure deploys automatically through GitHub Actions with AWS AWS Cloud Development Kit (AWS CDK) and includes built-in monitoring, auto-scaling, and high availability.

## Prerequisites and limitations
<a name="deploy-meeting-intelligence-strands-agents-fargate-prereqs"></a>

*Prerequisites*
+ An active AWS account with administrative permissions
+ AWS CDK version 2.114.1 or later installed
+ AWS CLI installed and configured with appropriate AWS Identity and Access Management (IAM) permissions
+ Node.js 18 or later
+ Python 3.12 or later
+ Git installed
+ Docker installed (optional, for local testing)
+ A GitHub account with repository secrets configured: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
+ Amazon Bedrock with access to the Anthropic Claude 3 Sonnet model enabled in your Region
+ Amazon Polly access enabled (enabled by default in most Regions)
+ IAM permissions for Amazon Simple Storage Service (Amazon S3), Amazon Elastic Container Service (Amazon ECS), Fargate, Elastic Load Balancing, Amazon Virtual Private Cloud (Amazon VPC)
+ Amazon VPC, IAM, Amazon CloudWatch, and Amazon Simple Notification Service (Amazon SNS)

*Limitations*
+ Processing time is 2–7 minutes per meeting, depending on transcript complexity.
+ Maximum transcript length is 50,000 characters per request.
+ Audio summaries are automatically condensed to 3,000 characters (Amazon Polly character limit).
+ Amazon Bedrock Claude 3 Sonnet availability varies by AWS Region.
+ Job status is stored in memory and is not persistent across container restarts unless you configure S3-based persistence.
+ Direct upload supports `.txt` files only.
+ The Application Load Balancer enforces a 15-minute timeout for processing requests.
+ Some AWS services aren't available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="deploy-meeting-intelligence-strands-agents-fargate-architecture"></a>

**Target architecture **

The solution deploys a multi-agent AI system using Strands Agents SDK on AWS Fargate with the following architecture :

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/dfd870ca-7a7d-48cc-a62a-b14c8c3c7bb6/images/8f9c0497-153f-4361-80cd-791dc0fec8c5.png)

1. Users upload meeting transcripts through a Streamlit web application hosted locally or on a remote server.

1. An Application Load Balancer in public subnets distributes traffic to the Fargate service across two Availability Zones.

1. Fargate tasks run in private subnets with NAT Gateway access and host the FastAPI backend and Strands agent orchestration logic.

1. The Strands multi-agent system processes transcripts through four sequential agents: structured minutes generation, concise summary generation, audio narration, and PDF report creation.

1. Amazon Bedrock provides language model inference (Claude 3 Sonnet) for the minutes and summary generation agents.

1. Amazon Polly converts the concise summary to an MP3 audio narration.

1. Amazon S3 stores uploaded transcripts, generated output files, and job status with lifecycle management policies.

1. Amazon CloudWatch provides centralized logging, CPU and memory alarms, and service health monitoring with Amazon SNS notifications.

1. GitHub Actions provides automated CI/CD deployment through AWS CDK with health validation testing.

*Automation and scale*
+ **ECS **Fargate** auto-scaling** – Automatic container scaling from 1 to 3 instances based on 70% CPU and memory utilization thresholds.
+ CloudWatch** monitoring** – CPU (65%), memory (80%), and service health alarms integrated with Amazon SNS notifications.
+ **Application Load Balancer** – Traffic distribution with health checks every 60 seconds and 15-minute idle timeout for long-running AI processing tasks.
+ **Background task processing** – Asynchronous meeting analysis using FastAPI BackgroundTasks for concurrent job execution.
+ **S3-based job persistence** – Persistent job status storage in Amazon S3 that ensures job continuity across container restarts and scaling events.
+ **GitHub Actions CI/CD** – Automated deployment pipeline with CDK infrastructure provisioning and health validation testing.

## Tools
<a name="deploy-meeting-intelligence-strands-agents-fargate-tools"></a>

*AWS services*
+ Amazon Bedrock – Provides language model inference (Claude 3 Sonnet) for meeting analysis and summarization agents. See [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/).
+ Amazon CloudWatch – Monitors container performance, captures application logs, and triggers alarms for CPU, memory, and service health thresholds. See [Amazon CloudWatch CloudWatch documentation](https://docs.aws.amazon.com/cloudwatch/).
+ Amazon Elastic Container Service (Amazon ECS) – Orchestrates Fargate container tasks with health checks and service discovery. See[ Amazon ECS documentation](https://docs.aws.amazon.com/ecs/).
+ Amazon Polly – Converts concise meeting summaries to MP3 audio narrations. See [Amazon Polly documentation](https://docs.aws.amazon.com/polly/).
+ Amazon Simple Notification Service (Amazon SNS)– Delivers alarm notifications from CloudWatch monitoring. See [Amazon SNS documentation](https://docs.aws.amazon.com/sns/).
+ Amazon Simple Storage Service (Amazon S3) – Stores uploaded transcripts, generated output files, and job status with lifecycle management. See [Amazon S3 documentation](https://docs.aws.amazon.com/s3/).
+ AWS CDK – Defines and deploys all infrastructure as code. See [AWS CDK documentation](https://docs.aws.amazon.com/cdk/).
+ AWS Fargate – Runs containerized application workloads without managing servers, with auto-scaling from 1 to 3 instances. See [AWS Fargate documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html).
+ Elastic Load Balancing – Distributes incoming traffic to Fargate tasks across Availability Zones. See [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/).

*Other tools*
+ **Docker** – Builds container images for local testing. See [Docker documentation](https://docs.docker.com/).
+ **FastAPI** – Provides the REST API backend for job submission, status checking, and file operations. See [FastAPI documentation](https://fastapi.tiangolo.com/).
+ **GitHub Actions** – Automates the CI/CD deployment pipeline. See [GitHub Actions documentation](https://docs.github.com/en/actions).
+ **ReportLab** – Generates formatted PDF reports from structured meeting minutes. See [ReportLab documentation](https://docs.reportlab.com/).
+ **Strands Agents SDK** – Orchestrates multi-agent workflows with minimal code using the `@tool` decorator pattern. See [Strands SDK documentation](https://strandsagents.com/).
+ **Streamlit** – Provides the web-based user interface for transcript upload and output download. See [Streamlit documentation](https://docs.streamlit.io/).

*Code repository*

The code for this pattern is available in the GitHub [sample-ai-meeting-minutes-generator](https://github.com/aws-samples/sample-ai-meeting-minutes-generator) repository.

## Best practices
<a name="deploy-meeting-intelligence-strands-agents-fargate-best-practices"></a>
+ Use clear, focused system prompts for each agent to ensure consistent output formatting and professional meeting documentation.
+ Implement Amazon S3 lifecycle management with 90-day retention for cost optimization and automated file cleanup.
+ Use Amazon S3-based job tracking to maintain state across container restarts and scaling events for reliable processing.
+ Configure CloudWatch alarms for CPU, memory, and service health with Amazon SNS notifications for proactive monitoring.
+ Validate and sanitize file uploads and content format before processing to prevent system errors and security issues.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.
+ Consider AWS AgentCore for production deployments that require managed orchestration and simplified operational overhead. Strands SDK is preferred when you need greater customization of agent interactions and specialized workflow control.
+ Implement systematic evaluation of agent outputs against human-generated meeting minutes to improve system prompts and agent performance continuously.

## Epics
<a name="deploy-meeting-intelligence-strands-agents-fargate-epics"></a>

### Deploy the infrastructure
<a name="deploy-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository | 1. To clone the pattern's repository, run the following command:<pre>git clone https://github.com/aws-samples/sample-ai-meeting-minutes-generator.git<br /></pre>1. Navigate to the project directory:<pre>cd meeting-minutes-app<br /></pre> | AWS DevOps |
| Create your own Git repository | 1. Create a new repository on your preferred Git platform (GitHub, GitLab, or Bitbucket).<br />2. Update the remote origin to point to your repository:<pre>git remote set-url origin https://<your-git-platform>.com/<your-username>/<your-repo-name>.git<br /></pre>1. Push the code to your repository:<pre>git push -u origin main<br /></pre> | App developer |
| Configure repository secrets for CI/CD. | 1. Navigate to your repository's **Settings** page.<br />2. Choose **Secrets and variables**, and then choose **Actions** (for GitHub) or the equivalent section for your Git platform.<br />3. Add the following repository secrets:Name: `AWS_ACCESS_KEY_ID`, Value: `<your-aws-access-key-id>`Name: `AWS_SECRET_ACCESS_KEY`, Value: `<your-aws-secret-access-key>` | DevOps engineer |
| Deploy the infrastructure by using the CI/CD workflow. | 1. Trigger the deployment by pushing code to your main branch:<pre>git add .<br />git commit -m "Deploy multi-agent meeting intelligence platform"<br />git push origin main<br /></pre>1. The GitHub Actions workflow automatically provisions the infrastructure by using AWS CDK. | DevOps engineer |
| Verify the infrastructure deployment. | 1. Navigate to your repository's CI/CD section (for example, `https://github.com/<your-username>/<your-repo-name>/actions`).<br />2. Choose the running workflow to view real-time logs and progress.<br />3. Open the AWS Management Console and navigate to the AWS CloudFormation service.<br />4. Select the **MeetingMinutesFargateStack** stack from the list.<br />5. Verify that the stack status shows **CREATE\_COMPLETE**.<br />6. Choose the **Outputs** tab and note the **ServiceURL** value for use in the next epic. | DevOps engineer, Cloud administrator |

### Configure and launch the application
<a name="configure-and-launch-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the local development environment | 1. Navigate to the application directory:<pre>cd meeting_minutes_agent/app<br /></pre>1. Create and activate a Python virtual environment:<pre>python -m venv venv<br />source venv/bin/activate  # Linux/Mac<br /># Or on Windows: venv\Scripts\activate<br /></pre>1. Install the required dependencies:<pre>pip install -r requirements.txt<br />pip install streamlit<br /></pre> | App developer |
| Retrieve the backend service URL. | 1. Open the AWS Management Console and navigate to the AWS CloudFormation service.<br />2. Select the **MeetingMinutesFargateStack** stack.<br />3. Choose the **Outputs** tab.<br />4. Locate the **ServiceURL** key and copy its corresponding URL value. | Cloud administrator |
| Launch the application and verify connectivity. | 1. Start the Streamlit application with the backend URL:<pre>BACKEND_URL="http://<your-service-url>.us-east-1.elb.amazonaws.com" streamlit run meeting_minutes_agent/app/streamlit_app.py<br /></pre>1. Open a web browser and navigate to `http://localhost:8501`.<br />2. Verify that the interface displays **Backend connected** status in the sidebar. | App developer |

### Verify the Solution
<a name="verify-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Process a meeting transcript and verify outputs. | 1. Upload a meeting transcript by using one of these methods:Use the provided `sample_meeting.txt` file from the repository.Upload your own meeting transcript (`.txt` file).Paste meeting transcript content directly in the text input area.<br />2. Choose **Generate Minutes** to start the multi-agent processing workflow.<br />3. Monitor the real-time processing progress through the interface.<br />4. Download and verify the generated outputs:`meeting_minutes_*.txt` – Structured meeting minutes`meeting_audio_*.mp3` – Audio summary narration`meeting_report_*.pdf` – Comprehensive PDF report<br />5. Verify that all four output files are present and contain expected content. | App developer |

## Troubleshooting
<a name="deploy-meeting-intelligence-strands-agents-fargate-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Amazon Bedrock model access error | Verify that the Anthropic Claude 3 Sonnet model is enabled in your Region. Open the Amazon Bedrock console, choose **Model access**, and confirm that Claude 3 Sonnet shows **Access granted**. |
| CDK bootstrap fails |  Run `cdk bootstrap aws://<account-id>/<region>` manually before deployment. Verify that your AWS CLI credentials have permissions for CloudFormation, Amazon S3, and IAM. |
| + Fargate task fails to start |  Check the Amazon ECS console for stopped task details. Common causes include incorrect IAM role permissions, missing Amazon Bedrock access, or VPC configuration issues. Review CloudWatch logs for the task. |
| Processing times out (15-minute ALB timeout) | The Application Load Balancer has a 15-minute idle timeout. For very long transcripts, reduce the input size to under 50,000 characters, or increase the ALB timeout in the CDK configuration. |
| Audio generation fails | Amazon Polly has a 3,000-character limit. The concise summary agent condenses content to under this limit automatically. If audio generation still fails, verify that Amazon Polly access is enabled in your Region. |
| GitHub Actions deployment fails | Verify that `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` repository secrets are configured correctly. Check that the IAM user has permissions for CDK deployment (CloudFormation, Amazon ECS, Amazon S3, IAM). |
| Backend not connected (Streamlit shows disconnected) | Verify that the `BACKEND_URL` environment variable matches the ServiceURL from the CloudFormation Outputs tab. Confirm that the Fargate service is running and healthy in the Amazon ECS console. |
| Job status lost after container restart | Enable Amazon S3-based job persistence by configuring the `S3_JOB_TRACKING` environment variable. Without this, job status is stored in memory only and lost on container restarts. |

## Related resources
<a name="deploy-meeting-intelligence-strands-agents-fargate-resources"></a>

*References*
+ [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/)
+ [Amazon Polly Developer Guide](https://docs.aws.amazon.com/polly/latest/dg/)
+ [Amazon ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/)
+ [AWS Fargate User Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
+ [AWS CDK CDK Developer Guide](https://docs.aws.amazon.com/cdk/v2/guide/)
+ [Elastic Load Balancing User Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/)

*Tools*
+ [Strands Agents SDK documentation](https://strandsagents.com/)
+ [FastAPI documentation](https://fastapi.tiangolo.com/)
+ [Streamlit documentation](https://docs.streamlit.io/)
+ [GitHub Actions documentation](https://docs.github.com/en/actions)

## Additional information
<a name="deploy-meeting-intelligence-strands-agents-fargate-additional-information"></a>

*Multi-agent processing workflow*

The solution orchestrates meeting processing through four specialized agents that run sequentially within Fargate tasks. Each job is assigned a unique job ID and is executed asynchronously for scalability and fault isolation.

1. **Structured Minutes Generator** (`generate_structured_minutes`) – Takes the raw meeting transcript and title as input. Uses Amazon Bedrock Claude 3 Sonnet to produce comprehensive meeting minutes, including meeting information, agenda items, discussion summary, action items with assignees and deadlines, and next steps. Saves output as a plain text file.

1. **Concise Summary Generator** (`concise_minutes_agent`) – Takes the full structured minutes from Agent 1 as input. Uses Amazon Bedrock Claude 3 Sonnet to create an executive summary of under 3,000 characters for audio generation and quick reading.

1. **Audio Generator** (`audio_generator_agent`) – Takes the concise minutes from Agent 2 as input. Uses the Strands `speak` tool with Amazon Polly to generate an MP3 audio file narrating the concise summary.

1. **PDF Report Generator** (`create_comprehensive_pdf`) – Takes the full structured minutes from Agent 1 as input. Uses the ReportLab library to produce a professional PDF report with custom title styling, section headers, readable text layout, and metadata.

*Data flow*

1. **User upload** – Meeting transcript uploaded through the Streamlit UI or direct API call.

1. **Job initialization** – FastAPI creates a unique job ID and returns immediately for asynchronous processing.

1. **Background processing** – The four-step Strands agent workflow executes sequentially.

1. **File management** – Generated files are uploaded to Amazon S3 with presigned download URLs.

1. **Job completion** – Status is updated with download links for all generated outputs.

*Future enhancement considerations*
+ Persistent job tracking with Amazon DynamoDB for cross-container reliability
+ Multi-format input support (`.docx`, `.pdf`, audio transcription files)
+ Real-time WebSocket progress updates

**End-to-End Processing Flow**
+ The solution orchestrates meeting processing through a coordinated sequence of specialized agents running within Fargate tasks.
+ Each job is assigned a **unique job ID** and executed asynchronously to ensure scalability and fault isolation.
+ The workflow includes **transcript ingestion → structured minutes generation → executive summarization → audio narration → PDF report creation**, with each step **validated and logged in real time**.

**Four-Step Agent Processing**

1. **Structured Minutes Generator** – produces detailed meeting minutes.

1. **Concise Summary Generator** – creates executive summary for quick review and audio narration.

1. **Audio Generator** – generates MP3 narration of the summary.

1. **PDF Report Generator** – produces polished, formatted PDF reports.

**Automated File Management and Cloud Integration**
+ **Automatic Output Upload: **Structured text, audio, and PDF reports are automatically uploaded to **Amazon S3** with proper **partitioning by job IDs.**
+ **Integrity Checks & Lifecycle Management:** Upload confirmations, file validation, and cleanup are logged ensuring operational transparency and reliability.
+ **FastAPI **background tasks manage asynchronous job execution.

**UI Integration & Outputs**
+ Streamlit UI shows backend connection, transcript input area, and Generate Minutes after uploading meeting transcript through** S3 Pre-signed URL** to initiate jobs.
![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/dfd870ca-7a7d-48cc-a62a-b14c8c3c7bb6/images/f608a187-91bf-4524-a849-907eb5efb182.png)
+ Once processing completes, the structured text, audio, and PDF outputs are made available for download via **Pre-signed S3 URL**s, accessible through clickable buttons in the UI.
![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/dfd870ca-7a7d-48cc-a62a-b14c8c3c7bb6/images/b4fa32f4-32c3-43ae-b140-0f6a58ebe245.png)
![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/dfd870ca-7a7d-48cc-a62a-b14c8c3c7bb6/images/eb878259-f90e-4d9f-8a4d-42627d04bdd1.png)
