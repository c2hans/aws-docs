---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework.html
---

# Deploy agentic systems on Amazon Bedrock with the CrewAI framework by using Terraform
<a name="deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework"></a>

*Vanitha Dontireddy, Amazon Web Services*

## Summary
<a name="deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework-summary"></a>

This pattern demonstrates how to implement scalable multi-agent AI systems by using the [CrewAI](https://www.crewai.com/) framework integrated with [Amazon Bedrock](https://aws.amazon.com/bedrock/?nc1=h_ls) and [Terraform](https://registry.terraform.io/). The solution enables organizations to create, deploy, and manage sophisticated AI agent workflows through infrastructure as code (IaC). In this pattern, CrewAI multi-agent orchestration capabilities combine with Amazon Bedrock foundation models and Terraform infrastructure automation. As a result, teams can build production-ready AI systems that tackle complex tasks with minimal human oversight. The pattern implements enterprise-grade security, scalability, and operational best practices.

## Prerequisites and limitations
<a name="deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework-prereqs"></a>

**Prerequisites**
+ An active AWS account with appropriate permissions to [access Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
+ Terraform version 1.5 or later [installed](https://developer.hashicorp.com/terraform/install)
+ Python version 3.9 or later [installed](https://www.python.org/downloads/)
+ CrewAI framework [installed](https://docs.crewai.com/installation)

**Limitations**
+ Agent interactions are limited by model context windows.
+ Terraform state management considerations for large-scale deployments apply to this pattern.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework-architecture"></a>

In this pattern, the following interactions occur:
+ Amazon Bedrock provides the foundation for agent intelligence through its suite of foundation models (FMs). It enables natural language processing (NLP), reasoning, and decision-making capabilities for the AI agents while maintaining high availability and scalability.
+ The CrewAI framework serves as the core orchestration layer for creating and managing AI agents. It handles agent communication protocols, task delegation, and workflow management while integrating with Amazon Bedrock.
+ Terraform manages the entire infrastructure stack through code, including compute resources, networking, security groups, and AWS Identity and Access Management (IAM) roles. It ensures consistent, version-controlled deployments across environments. The Terraform deployment creates the following:
  + AWS Lambda function to run the CrewAI application
  + Amazon Simple Storage Service (Amazon S3) buckets for code and reports
  + IAM roles with appropriate permissions
  + Amazon CloudWatch logging
  + Scheduled execution by Amazon EventBridge

The following diagram illustrates the architecture for deploying CrewAI multi-agent systems by using Amazon Bedrock and Terraform.

![Workflow to deploy CrewAI multi-agent systems using Terraform and Amazon Bedrock.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b46069e9-4c38-405f-b0f0-310eabb06b06/images/b3296b17-e388-46ba-8d71-2ec7ce3ed3e0.png)

The diagram shows the following workflow:

1. The user clones the repository.

1. The user runs the command `terraform apply` to deploy the AWS resources.

1. Amazon Bedrock model configuration includes specifying the foundation model (FM) to use for configuring the CrewAI agents.

1. An EventBridge rule is established to trigger the Lambda function according to the defined schedule.

1. When triggered (either by schedule or manually), the Lambda function initializes and assumes the IAM role with permissions to access AWS services and Amazon Bedrock.

1. The CrewAI framework loads agent configurations from YAML files and creates specialized AI agents (the *AWS infrastructure security audit* crew). The Lambda function sequentially executes these agents to scan AWS resources, analyze security vulnerabilities, and generate comprehensive audit reports.

1. CloudWatch Logs captures detailed execution information from the Lambda function with a 365-day retention period and AWS Key Management Service (AWS KMS) encryption for compliance requirements. The logs provide visibility into agent activities, error tracking, and performance metrics, enabling effective monitoring and troubleshooting of the security audit process.

1. The security audit report is automatically generated and stored in the designated Amazon S3 bucket. The automated setup helps maintain consistent security monitoring with minimal operational overhead.

After the initial deployment, the workflow provides ongoing security auditing and reporting for your AWS infrastructure without manual intervention.

**Overview of AI agents**

This pattern creates multiple AI agents, each with unique roles, goals, and tools:
+ The **security analyst agent** collects and analyzes AWS resource information.
+ The **penetration tester agent **identifies vulnerabilities in AWS resources.
+ The **compliance expert agent **checks configurations against compliance standards.
+ The **report writer agent** compiles findings into comprehensive reports.

These agents collaborate on a series of tasks, leveraging their collective skills to perform security audits and generate comprehensive reports. (The `config/agents.yaml` file outlines the capabilities and configurations of each agent in this crew.)

Security analysis processing consists of the following actions:

1. The security analyst agent examines the collected data about AWS resources such as the following:
   + Amazon Elastic Compute Cloud (Amazon EC2) instances and security groups
   + Amazon S3 buckets and configurations
   + IAM roles, policies, and permissions
   + Virtual private cloud (VPC) configurations and network settings
   + Amazon RDS databases and security settings
   + Lambda functions and configurations
   + Other AWS services within audit scope

1. The penetration tester agent identifies potential vulnerabilities.

1. The agents collaborate through the CrewAI framework to share findings.

Report generation consists of the following actions:

1. The report writer agent compiles findings from all other agents.

1. Security issues are organized by service, severity, and compliance impact.

1. Remediation recommendations are generated for each identified issue.

1. A comprehensive security audit report is created in markdown format and uploaded to the designated Amazon S3 bucket. Historical reports are preserved for compliance tracking and security posture improvement.

Logging and monitoring activities include:
+ CloudWatch logs capture execution details and any errors.
+ Lambda execution metrics are recorded for monitoring.

**Note**
The code for `aws-security-auditor-crew` is sourced from the GitHub [3P-Agentic\_frameworks](https://github.com/aws-samples/3P-Agentic-Frameworks/blob/main/crewai/aws-security-auditor-crew/README.md) repository, available in the AWS Samples collection.

**Availability and scale**

You can expand the available agents to more than the four core agents. To scale with additional specialized agents, consider the following new agent types:
+ A *threat intelligence specialist* agent can do the following:
  + Monitors external threat feeds and correlates with internal findings
  + Provides context on emerging threats relevant to your infrastructure
  + Prioritizes vulnerabilities based on active exploitation in the wild
+ *Compliance framework* agents can focus on specific regulatory areas such as the following:
  + Payment Card Industry Data Security Standard (PCI DSS) compliance agent
  + Health Insurance Portability and Accountability Act of 1996 (HIPAA) compliance agent
  + System and Organization Controls 2 (SOC 2) compliance agent
  + General Data Protection Regulation (GDPR) compliance agent

By thoughtfully expanding the available agents, this solution can provide deeper, more specialized security insights while maintaining scalability across large AWS environments. For more information about an implementation approach, tool development, and scaling considerations, see [Additional information](#deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework-additional).

## Tools
<a name="deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework-tools"></a>

**AWS services**
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed AI service that makes high-performing foundation models (FMs) available for use through a unified API.
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts. In this pattern, it’s used for scheduling and orchestrating agent workflows.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data. In this pattern, it provides object storage for agent artifacts and state management.

**Other tools**
+ [CrewAI](https://www.crewai.com/open-source) is an open source Python-based framework for building multi-agent AI systems.
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

The code for this pattern is available in the GitHub [deploy-crewai-agents-terraform](https://github.com/aws-samples/deploy-crewai-agents-terraform.git) repository.

## Best practices
<a name="deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework-best-practices"></a>
+ Implement proper state management for Terraform by using an Amazon S3 backend with Amazon DynamoDB locking. For more information, see [Backend best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/backend.html) in *Best practices for using the Terraform AWS Provider*.
+ Use workspaces to separate development, staging, and production environments.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.
+ Enable detailed logging and monitoring through CloudWatch Logs.
+ Implement retry mechanisms and error handling for agent operations.

## Epics
<a name="deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework-epics"></a>

### Deploy CrewAI framework
<a name="deploy-crewai-framework"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone this pattern’s repository on your local machine, run the following command:<pre>git clone "git@github.com:aws-samples/deploy-crewai-agents-terraform.git"<br />cd deploy-crewai-agents-terraform</pre> | DevOps engineer |
| Edit the environment variables. | To edit the environment variables, do the following:1. Create a `terraform.tfvars` file from the example `terraform.tfvars.example` in the [terraform](https://github.com/aws-samples/deploy-crewai-agents-terraform/blob/main/terraform/terraform.tfvars.example) directory.<br />2. Edit the environment variables to use your own information. | DevOps engineer |
| Create the infrastructure. | To create the infrastructure, run the following commands:<pre>cd terraform</pre><pre>terraform init</pre><pre>terraform plan</pre><br />Review the execution plan carefully. If the planned changes are acceptable, then run the following command:<pre>terraform apply --auto-approve</pre> | DevOps engineer |

### Access CrewAI agents
<a name="access-crewai-agents"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Access the agents. | The agents in the AWS Infrastructure Security Audit and Reporting crew are deployed as a Lambda function. To access the agents, use the following steps:1. Sign in to the AWS Management Console and open the AWS Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/).<br />2. On the **Functions** page, find and then select the function named `{project_name}`\\function (as defined in your Terraform variables).<br />3. From the function’s page, you can take the following actions: <br />• View configuration details. <br />• Monitor execution metrics.<br />• View CloudWatch logs.<br />• Test the function manually. | DevOps engineer |
| (Optional) Configure manual execution of the agents. | The agents are configured to run automatically on a daily schedule (midnight UTC). However, you can trigger them manually by using the following steps:1. In the Lambda console, select the function named `{project_name}`.<br />2. On the function’s page, choose the **Test** tab.<br />3. Create a new test event with an empty JSON object `{}`.<br />4. To execute the event, choose **Test**.<br />For more details, see [Testing Lambda functions in the console](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html) in the Lambda documentation. | DevOps engineer |
| Access agent logs for debugging. | The CrewAI agents are running in a Lambda environment with the necessary permissions to perform security audits and store reports in Amazon S3. The output is a markdown report that provides a comprehensive security analysis of your AWS infrastructure.<br />To assist with detailed debugging of agent behavior, do the following:1. In the AWS Management Console, navigate to CloudWatch Logs.<br />2. Find the log group for your Lambda function.<br />3. Look for log entries with agent names (for example, *Infrastructure mapping specialist* and *Exploratory security analyst*).<br />4. Review the logs for insights into the actions of each agent. | DevOps engineer |
| View results of agent execution. | To view the results of an agent execution, do the following:1. In the AWS Management Console, navigate to Amazon S3.<br />2. Open the Amazon S3 bucket named `{project_name}-reports-{random_suffix}` (as defined in your Terraform variables).<br />Reports are stored with timestamp-based filenames as follows: `security-audit-report-YYYY-MM-DD-HH-MM-SS.md)` | DevOps engineer |
| Monitor agent execution. | To monitor the agents' execution through CloudWatch logs, do the following:1. In the AWS Management Console, navigate to CloudWatch.<br />2. Go to **Log groups**.<br />3. Select the log group named `/aws/lambda/{project_name}-function`.<br />4. In **Log streams**, choose the most recent log stream to see detailed execution information. | DevOps engineer |
|  Customize agent behavior. | To modify the agents or their tasks, do the following:1. Update the configuration files in your local repository: <br />• The following file defines each agent's role, capabilities, and settings: `src/aws_infrastructure_security_audit_and_reporting/config/agents.yaml` <br />• The following dile defines the tasks and workflows for the agents:<br />`src/aws_infrastructure_security_audit_and_reporting/config/tasks.yaml`<br />2. To repackage and update the Lambda function, use the following commands: <pre>cd terraform </pre><pre>terraform apply</pre> | DevOps engineer |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the created resources. | To delete all infrastructure created by this pattern, run the following command:<pre>terraform plan -destroy </pre>The following command will permanently delete all resources created by this pattern. The command will prompt for confirmation before removing any resources.<br />Review the destruction plan carefully. If the planned deletions are acceptable, then run the following command:<pre>terraform destroy</pre> | DevOps engineer |

## Troubleshooting
<a name="deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Agent behavior | For information about this issue, see [Test and troubleshoot agent behavior](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-networking.html) in the Amazon Bedrock documentation. |
| Lambda network issues | For information about these issues, see [Troubleshoot networking issues in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-networking.html) in the Lambda documentation. |
| IAM permissions | For information about these issues, see [Troubleshoot IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html) in the IAM documentation. |

## Related resources
<a name="deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework-resources"></a>

**AWS Blogs**
+ [Build agentic systems with CrewAI and Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/build-agentic-systems-with-crewai-and-amazon-bedrock/)

**AWS documentation**
+ [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/)
+ [How Amazon Bedrock Agents works](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-how.html)
+ [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)

**Other resources**
+ [CrewAI documentation](https://docs.crewai.com/introduction)
+ [Terraform AWS Provider documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

## Additional information
<a name="deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework-additional"></a>

This section contains information about an implementation approach, tool development, and scaling considerations related to the earlier discussion in [Automation and scale](#deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework-architecture).

**Implementation approach**

Consider the following approach to adding agents:

1. Agent configuration:
   + Add new agent definitions to the `config/agents.yaml` file.
   + Define specialized backstories, goals, and tools for each agent.
   + Configure memory and analysis capabilities based on agent specialty.

1. Task orchestration:
   + Update the `config/tasks.yaml` file to include new agent-specific tasks.
   + Create dependencies between tasks to help ensure proper information flow.
   + Implement parallel task execution where appropriate.

**Technical implementation**

Following is an addition to the `agents.yaml` file for a proposed Threat Intelligence Specialist agent:

```
Example new agent configuration in agents.yaml
threat_intelligence_agent:
 name: "Threat Intelligence Specialist"
 role: "Cybersecurity Threat Intelligence Analyst"
 goal: "Correlate AWS security findings with external threat intelligence"
 backstory: "Expert in threat intelligence with experience in identifying emerging threats and attack patterns relevant to cloud infrastructure."
verbose: true
allow_delegation: true
tools:
- "ThreatIntelligenceTool"
- "AWSResourceAnalyzer"
```

**Tool development**

With the CrewAI framework, you can take the following actions to enhance your security audit crew's effectiveness:
+ Create custom tools for new agents.
+ Integrate with external APIs for threat intelligence.
+ Develop specialized analyzers for different AWS services.

**Scaling considerations**

When expanding your AWS Infrastructure Security Audit and Reporting system to handle larger environments or more comprehensive audits, address the following scaling factors:
+ **Computational resources**
  + Increase Lambda memory allocation to handle additional agents.
  + Consider splitting agent workloads across multiple Lambda functions.
+ **Cost management**
  + Monitor Amazon Bedrock API usage as agent count increases.
  + Implement selective agent activation based on audit scope.
+ **Collaboration efficiency**
  + Optimize information sharing between agents.
  + Implement hierarchical agent structures for complex environments.
+ **Knowledge base enhancement**
  + Provide agents with specialized knowledge bases for their domains.
  + Regularly update agent knowledge with new security best practices.
