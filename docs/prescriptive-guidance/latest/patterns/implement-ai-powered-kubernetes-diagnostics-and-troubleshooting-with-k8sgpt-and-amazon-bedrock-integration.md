---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-ai-powered-kubernetes-diagnostics-and-troubleshooting-with-k8sgpt-and-amazon-bedrock-integration.html
---

# Implement AI-powered Kubernetes diagnostics and troubleshooting with K8sGPT and Amazon Bedrock integration
<a name="implement-ai-powered-kubernetes-diagnostics-and-troubleshooting-with-k8sgpt-and-amazon-bedrock-integration"></a>

*Ishwar Chauthaiwale, Muskan ., and Prafful Gupta, Amazon Web Services*

## Summary
<a name="implement-ai-powered-kubernetes-diagnostics-and-troubleshooting-with-k8sgpt-and-amazon-bedrock-integration-summary"></a>

This pattern demonstrates how to implement AI-powered Kubernetes diagnostics and troubleshooting by integrating K8sGPT with the Anthropic Claude v2 model available on Amazon Bedrock. The solution provides natural language analysis and remediation steps for Kubernetes cluster issues through a secure bastion host architecture. By combining K8sGPT Kubernetes expertise with Amazon Bedrock advanced language capabilities, DevOps teams can quickly identify and resolve cluster problems. With these capabilities, it’s possible to reduce mean time to resolution (MTTR) by up to 50 percent.

This cloud-native pattern leverages Amazon Elastic Kubernetes Service (Amazon EKS) for Kubernetes management. The pattern implements security best practices through proper AWS Identity and Access Management (IAM) roles and network isolation. This solution is particularly valuable for organizations who want to streamline their Kubernetes operations and enhance their troubleshooting capabilities with AI assistance.

## Prerequisites and limitations
<a name="implement-ai-powered-kubernetes-diagnostics-and-troubleshooting-with-k8sgpt-and-amazon-bedrock-integration-prereqs"></a>

**Prerequisites**
+ An active AWS account with appropriate permissions
+ AWS Command Line Interface (AWS CLI) [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ An Amazon EKS cluster
+ Access to Anthropic Claude 2 model on [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
+ A bastion host with required security group settings
+ K8sGPT [installed](https://docs.k8sgpt.ai/getting-started/installation/)

**Limitations**
+ K8sGPT analysis is limited by the context window size of the Claude v2 model.
+ Amazon Bedrock API rate limits apply based on your account quotas.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ Amazon EKS [version 1.31 or later](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)
+ [Claude 2 model](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) on Amazon Bedrock
+ K8sGPT [v0.4.2 or later](https://github.com/k8sgpt-ai/k8sgpt/releases)

## Architecture
<a name="implement-ai-powered-kubernetes-diagnostics-and-troubleshooting-with-k8sgpt-and-amazon-bedrock-integration-architecture"></a>

The following diagram shows the architecture for AI-powered Kubernetes diagnostics using K8sGPT integrated with Amazon Bedrock in the AWS Cloud.

![Workflow for Kubernetes diagnostics using K8sGPT integrated with Amazon Bedrock.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/09bc08f6-e191-4cef-b26b-dcb6225b15cc/images/8789891d-4a90-44b0-a108-387f6d96496b.png)

The architecture shows the following workflow:

1. Developers access the environment through a secure connection to the bastion host. This Amazon EC2 instance serves as the secure entry point and contains the K8sGPT command line interface (CLI) installation and required configurations.

1. The bastion host, configured with specific IAM roles, establishes secure connections to both the Amazon EKS cluster and the Amazon Bedrock endpoints. K8sGPT is installed and configured on the bastion host to perform Kubernetes cluster analysis.

1. Amazon EKS manages the Kubernetes control plane and worker nodes, providing the target environment for K8sGPT analysis. The service runs across multiple Availability Zones within a virtual private cloud (VPC), which helps to provide high availability and resilience. Amazon EKS supplies operational data through the Kubernetes API, enabling comprehensive cluster analysis.

1. K8sGPT sends analysis data to Amazon Bedrock, which provides the Claude v2 foundation model (FM) for natural language processing. The service processes K8sGPT analysis to generate human-readable explanations and offers detailed remediation suggestions based on identified issues. Amazon Bedrock operates as a serverless AI service with high availability and scalability.

**Note**
Throughout this workflow, IAM controls access between components through roles and policies, managing authentication for the bastion host, Amazon EKS, and Amazon Bedrock interactions. IAM implements the principle of least privilege and enables secure cross-service communication throughout the architecture.

**Automation and scale**

K8sGPT operations can be automated and scaled across multiple Amazon EKS clusters through various AWS services and tools. This solution supports continuous integration and continuous deployment (CI/CD) integration using [Jenkins](https://www.jenkins.io/), [GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions), or [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) for scheduled analysis. The K8sGPT operator enables continuous in-cluster monitoring with automated issue detection and reporting capabilities. For enterprise-scale deployments, you can use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to schedule scans and trigger automated responses with custom scripts. AWS SDK integration enables programmatic control across large fleet of clusters.

## Tools
<a name="implement-ai-powered-kubernetes-diagnostics-and-troubleshooting-with-k8sgpt-and-amazon-bedrock-integration-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command line shell.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.

**Other tools**
+ [K8sGPT](https://k8sgpt.ai/) is an open source AI-powered tool that transforms Kubernetes management. It acts as a virtual site reliability engineering (SRE) expert, automatically scanning, diagnosing, and troubleshooting Kubernetes cluster issues. Administrators can interact with K8sGPT using natural language and get clear, actionable insights about cluster state, pod crashes, and service failures. The tool's built-in analyzers detect a wide range of issues, from misconfigured components to resource constraints, and provide easy-to-understand explanations and solutions.

## Best practices
<a name="implement-ai-powered-kubernetes-diagnostics-and-troubleshooting-with-k8sgpt-and-amazon-bedrock-integration-best-practices"></a>
+ Implement secure access controls by using AWS Systems Manager Session Manager for [bastion host access](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect.html).
+ Make sure that K8sGPT authentication uses dedicated IAM roles with least privilege permissions for Amazon Bedrock and Amazon EKS interactions . For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.
+ Configure [resource tagging](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html), enable Amazon CloudWatch [logging for audit trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html), and implement [data anonymization](https://aws.amazon.com/solutions/guidance/data-anonymization-on-aws/) for sensitive information.
+ Maintain regular backups of K8sGPT configurations while setting up automated scanning schedules during off-peak hours to minimize operational impact.

## Epics
<a name="implement-ai-powered-kubernetes-diagnostics-and-troubleshooting-with-k8sgpt-and-amazon-bedrock-integration-epics"></a>

### Add Amazon Bedrock to AI backend provider list.
<a name="add-br-to-ai-backend-provider-list"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set Amazon Bedrock as the AI backend provider for K8sGPT. | To set Amazon Bedrock as the AI [backend provide](https://docs.k8sgpt.ai/reference/providers/backend/)r for K8sGPT, use the following AWS CLI command:<pre>k8sgpt auth add -b amazonbedrock \<br /> -r us-west-2 \<br /> -m anthropic.claude-v2 \<br /> -n endpoint-name <br /></pre><br />The example command uses `us-west-2` for the AWS Region. However, you can select another Region, provided that both the Amazon EKS cluster and the corresponding Amazon Bedrock model are available and enabled in that selected Region.<br />To check that `amazonbedrock` is added to the AI backend provider list and is in the `Active` state, run the following command:<pre>k8sgpt auth list</pre><br />Following is an example of the expected output of this command:<pre>Default: <br />> openai<br />Active: <br />> amazonbedrock<br />Unused: <br />> openai<br />> localai<br />> ollama<br />> azureopenai<br />> cohere<br />> amazonsagemaker<br />> google<br />> noopai<br />> huggingface<br />> googlevertexai<br />> oci<br />> customrest<br />> ibmwatsonxai</pre> | AWS DevOps |

### Scan resources using a filter
<a name="scan-resources-using-a-filter"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| View a list of available filters. | To see the list of all available filters, use the following AWS CLI command:<pre>k8sgpt filters list</pre><br />Following is an example of the expected output of this command:<pre>Active: <br />> Deployment<br />> ReplicaSet<br />> PersistentVolumeClaim<br />> Service<br />> CronJob<br />> Node<br />> MutatingWebhookConfiguration<br />> Pod<br />> Ingress<br />> StatefulSet<br />> ValidatingWebhookConfiguration</pre> | AWS DevOps |
| Scan a pod in a specific namespace by using a filter. | This command is useful for targeted debugging of specific pod issues within a Kubernetes cluster, using Amazon Bedrock AI capabilities to analyze and explain the problems it finds.<br />To scan a pod in a specific namespace by using a filter, use the following AWS CLI command:<pre>k8sgpt analyze --backend amazonbedrock --explain --filter Pod -n default</pre><br />Following is an example of the expected output of this command:<pre>100% |████████████████████████████████████████████████████████| (1/1, 645 it/s)        <br />AI Provider: amazonbedrock<br /><br />0: Pod default/crashme()<br />- Error: the last termination reason is Error container=crashme pod=crashme<br />Error: The pod named crashme terminated because the container named crashme crashed.<br />Solution: Check logs for crashme pod to identify reason for crash. Restart pod or redeploy application to resolve crash.</pre> | AWS DevOps |
| Scan a deployment in a specific namespace by using a filter. | This command is useful for identifying and troubleshooting deployment-specific issues, particularly when the actual state doesn't match the desired state.<br />To scan a deployment in a specific namespace by using a filter, use the following AWS CLI command:<pre>k8sgpt analyze --backend amazonbedrock --explain --filter Deployment -n default</pre><br />Following is an example of the expected output of this command:<pre>100% |██████████████████████████████████████████████████████████| (1/1, 10 it/min)        <br />AI Provider: amazonbedrock<br /><br />0: Deployment default/nginx()<br />- Error: Deployment default/nginx has 1 replicas but 2 are available<br /> Error: The Deployment named nginx in the default namespace has 1 replica specified but 2 pod replicas are running.<br />Solution: Check if any other controllers like ReplicaSet or StatefulSet have created extra pods. Delete extra pods or adjust replica count to match available pods.</pre> | AWS DevOps |
| Scan a node in a specific namespace by using a filter. | To scan a node in a specific namespace by using a filter, use the following AWS CLI command:<pre>k8sgpt analyze --backend amazonbedrock --explain --filter Node -n default </pre><br />Following is an example of the expected output of this command:<pre>AI Provider: amazonbedrock<br /><br />No problems detected</pre> | AWS DevOps |

### Analyze detailed outputs
<a name="analyze-detailed-outputs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Get detailed outputs. |  To get detailed outputs, use the following AWS CLI command:<pre>k8sgpt analyze --backend amazonbedrock --explain --ouput json</pre><br />Following is an example of the expected output of this command:<pre>{<br />  "provider": "amazonbedrock",<br />  "errors": null,<br />  "status": "ProblemDetected",<br />  "problems": 1,<br />  "results": [<br />    {<br />      "kind": "Pod",<br />      "name": "default/crashme",<br />      "error": [<br />        {<br />          "Text": "the last termination reason is Error container=crashme pod=crashme",<br />          "KubernetesDoc": "",<br />          "Sensitive": []<br />        }<br />      ],<br />      "details": " Error: The pod named crashme terminated because the container named crashme crashed.\nSolution: Check logs for crashme pod to identify reason for crash. Restart pod or redeploy application to resolve crash.",<br />      "parentObject": ""<br />    }<br />  ]<br />}</pre> | AWS DevOps |
| Check problematic pods. | To check for specific problematic pods, use the following AWS CLI command:<pre>kubectl get pods --all-namespaces | grep -v Running</pre><br />Following is an example of the expected output of this command:<pre>NAMESPACE    NAME      READY    STATUS          RESTARTS      AGE                                       <br />default     crashme     0/1   CrashLoopBackOff   260(91s ago)   21h</pre> | AWS DevOps |
| Get application-specific insights. | This command is particularly useful when:+ You want to focus on a specific application in your cluster.<br />+ You use labels effectively to organize your Kubernetes resources.<br />+ You need to quickly check the health of a particular application component.<br />To get application-specific insights, use the following command:<pre>k8sgpt analyze --backend amazonbedrock --explain -L app=nginx -n default</pre><br />Following is an example of the expected output of this command:<pre>AI Provider: amazonbedrock<br /><br />No problems detected</pre> |  |

## Related resources
<a name="implement-ai-powered-kubernetes-diagnostics-and-troubleshooting-with-k8sgpt-and-amazon-bedrock-integration-resources"></a>

**AWS Blogs**
+ [Automate Amazon EKS troubleshooting using an Amazon Bedrock agentic workflow](https://aws.amazon.com/blogs/machine-learning/automate-amazon-eks-troubleshooting-using-an-amazon-bedrock-agentic-workflow/)
+ [Use K8sGPT and Amazon Bedrock for simplified Kubernetes cluster maintenance](https://aws.amazon.com/blogs/machine-learning/use-k8sgpt-and-amazon-bedrock-for-simplified-kubernetes-cluster-maintenance/)

**AWS documentation**
+ AWS CLI commands: [create-cluster](https://docs.aws.amazon.com/cli/latest/reference/eks/create-cluster.html) and [describe-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-cluster.html)
+ [Get started with Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) (Amazon EKS documentation)
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) (IAM documentation)

**Other resources**
+ [K8sGPT](https://k8sgpt.ai/)
