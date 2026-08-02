---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html
---

# Automatically build and deploy a Java application to Amazon EKS using a CI/CD pipeline
<a name="automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline"></a>

*MAHESH RAGHUNANDANAN, Jomcy Pappachen, and James Radtke, Amazon Web Services*

## Summary
<a name="automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline-summary"></a>

This pattern describes how to create a continuous integration and continuous delivery (CI/CD) pipeline that automatically builds and deploys a Java application with recommended DevSecOps practices to an Amazon Elastic Kubernetes Service (Amazon EKS) cluster on the AWS Cloud. This pattern uses a greeting application developed with a Spring Boot Java framework and that uses Apache Maven.

You can use this pattern’s approach to build the code for a Java application, package the application artifacts as a Docker image, security scan the image, and upload the image as a workload container on Amazon EKS. This pattern's approach is useful if you want to migrate from a tightly coupled monolithic architecture to a microservices architecture. The approach also helps you to monitor and manage the entire lifecycle of a Java application, which ensures a higher level of automation and helps avoid errors or bugs.

## Prerequisites and limitations
<a name="automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI) version 2, installed and configured. For more information about this, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) in the AWS CLI documentation.

  AWS CLI version 2 must be configured with the same AWS Identity and Access Management (IAM) role that creates the Amazon EKS cluster, because only that role is authorized to add other IAM roles to the `aws-auth` `ConfigMap`. For information and steps to configure AWS CLI, see [Configuring settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) in the AWS CLI documentation.
+ IAM roles and permissions with full access to AWS CloudFormation. For more information about this, see [Controlling access with IAM](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) in the CloudFormation documentation.
+ An existing Amazon EKS cluster, with details of the IAM role name and the Amazon Resource Name (ARN) of the IAM role for worker nodes in the EKS cluster.
+ Kubernetes Cluster Autoscaler, installed and configured in your Amazon EKS cluster. For more information, see [Scale cluster compute with Karpenter and Cluster Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/cluster-autoscaler.html) in the Amazon EKS documentation.
+ Access to code in the GitHub repository.

**Important**
AWS Security Hub CSPM is enabled as part of the CloudFormation templates that are included in the code for this pattern. By default, after Security Hub CSPM is enabled, it comes with a 30–day free trial. After the trial, there is a cost associated with this AWS service. For more information about pricing, see [AWS Security Hub CSPM pricing](https://aws.amazon.com/security-hub/pricing/).

**Product versions**
+ Helm version 3.4.2 or later
+ Apache Maven version 3.6.3 or later
+ BridgeCrew Checkov version 2.2 or later
+ Aqua Security Trivy version 0.37 or later

## Architecture
<a name="automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline-architecture"></a>

**Technology stack**
+ AWS CodeBuild
+ AWS CodeCommit
+ Amazon CodeGuru
+ AWS CodePipeline
+ Amazon Elastic Container Registry (Amazon ECR)
+ Amazon EKS
+ Amazon EventBridge
+ AWS Security Hub CSPM
+ Amazon Simple Notification Service (Amazon SNS)

**Target architecture**

![Workflow for deploying a Java application to Amazon EKS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/95a5b5c2-d7fb-41eb-9089-455318c0d585/images/4f5fd8c2-2b6d-4945-aa64-fcf317521711.png)

The diagram shows the following workflow:

1. The developer updates the Java application code in the base branch of the CodeCommit repository, which creates a pull request (PR).

1. As soon as the PR is submitted, Amazon CodeGuru Reviewer automatically reviews the code, analyzes it based on best practices for Java, and gives recommendations to the developer.

1. After the PR is merged to the base branch, an Amazon EventBridge event is created.

1. The EventBridge event initiates the CodePipeline pipeline, which starts.

1. CodePipeline runs the CodeSecurity Scan stage (continuous security).

1. AWS CodeBuild starts the security scan process in which the Dockerfile and Kubernetes deployment Helm files are scanned by using Checkov, and application source code is scanned based on incremental code changes. The application source code scan is performed by the [CodeGuru Reviewer Command Line Interface (CLI) wrapper](https://github.com/aws/aws-codeguru-cli).
**Note**
As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html) in the CodeGuru Reviewer documentation.

1. If the security scan stage is successful, the Build stage (continuous integration) is initiated.

1. In the Build stage, CodeBuild builds the artifact, packages the artifact to a Docker image, scans the image for security vulnerabilities by using Aqua Security Trivy, and stores the image in Amazon ECR.

1. The vulnerabilities detected from step 8 are uploaded to Security Hub CSPM for further analysis by developers or engineers. Security Hub CSPM provides an overview and recommendations for remediating the vulnerabilities.

1. Email notifications of sequential phases within the CodePipeline pipeline are sent through Amazon SNS.

1. After the continuous integration phases are complete, CodePipeline enters the Deploy stage (continuous delivery).

1. The Docker image is deployed to Amazon EKS as a container workload (pod) by using Helm charts.

1. The application pod is configured with Amazon CodeGuru Profiler agent, which sends the profiling data of the application (CPU, heap usage, and latency) to CodeGuru Profiler, which helps developers understand the behavior of the application.

## Tools
<a name="automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline-tools"></a>

**AWS services**
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+  [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [Amazon CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html) collects runtime performance data from your live applications, and provides recommendations that can help you fine-tune your application performance.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources, including AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state on AWS. It also helps you check your AWS environment against security industry standards and best practices.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other services**
+ [Helm](https://helm.sh/docs/) is an open-source package manager for Kubernetes.
+ [Apache Maven](https://maven.apache.org/) is a software project management and comprehension tool.
+ [BridgeCrew Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) is a static code analysis tool for scanning infrastructure as code (IaC) files for misconfigurations that might lead to security or compliance problems.
+ [Aqua Security Trivy](https://github.com/aquasecurity/trivy) is a comprehensive scanner for vulnerabilities in container images, file systems, and Git repositories, in addition to configuration issues.

**Code **

The code for this pattern is available in the GitHub [aws-codepipeline-devsecops-amazoneks](https://github.com/aws-samples/aws-codepipeline-devsecops-amazoneks) repository.

## Best practices
<a name="automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline-best-practices"></a>
+ This pattern follows [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) to apply the principle of least privilege for IAM entities across all phases of the solution. If you want to extend the solution with additional AWS services or third-party tools, we recommend that you review the section on [applying least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the IAM documentation.
+ If you have multiple Java applications, we recommend that you create separate CI/CD pipelines for each application.
+ If you have a monolith application, we recommend that you break the application into microservices where possible. Microservices are more flexible, they make it easier to deploy applications as containers, and they provide better visibility into the overall build and deployment of the application.

## Epics
<a name="automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline-epics"></a>

### Set up the environment
<a name="set-up-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the GitHub repository. | To clone the repository, run the following command.<pre>git clone https://github.com/aws-samples/aws-codepipeline-devsecops-amazoneks</pre> | App developer, DevOps engineer |
| Create an S3 bucket and upload the code. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html) | AWS DevOps, Cloud administrator, DevOps engineer |
| Create an CloudFormation stack. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html) | AWS DevOps, DevOps engineer |
| Validate the CloudFormation stack deployment. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html) | AWS DevOps, DevOps engineer |
| Delete the S3 bucket. | Empty and delete the S3 bucket that you created earlier. For more information, see [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) in the Amazon S3 documentation. | AWS DevOps, DevOps engineer |

### Configure the Helm charts
<a name="configure-the-helm-charts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the Helm charts of your Java application. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html) | DevOps engineer |
| Validate Helm charts for syntax errors. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html) | DevOps engineer |

### Set up the Java CI/CD pipeline
<a name="set-up-the-java-ci-cd-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the CI/CD pipeline. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html) | AWS DevOps |

### Activate integration between Security Hub CSPM and Aqua Security
<a name="activate-integration-between-ash-and-aqua-security"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Turn on Aqua Security integration. | This step is required for uploading the Docker image vulnerability findings reported by Trivy to Security Hub CSPM. Because CloudFormation doesn’t support Security Hub CSPM integrations, this process must be done manually.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html) | AWS administrator, DevOps engineer |

### Configure CodeBuild to run Helm or kubectl commands
<a name="configure-acb-to-run-helm-or-kubectl-commands"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Allow CodeBuild to run Helm or kubectl commands in the Amazon EKS cluster. | For CodeBuild to be authenticated to use Helm or `kubectl` commands with the Amazon EKS cluster, you must add the IAM roles to the `aws-auth` `ConfigMap`. In this case, add the ARN of the IAM role `EksCodeBuildkubeRoleARN`, which is the IAM role created for the CodeBuild service to access the Amazon EKS cluster and deploy workloads on it. This is a one-time activity.The following procedure must be completed before the deployment approval stage in CodePipeline.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html)<br />The `aws_auth` `ConfigMap` is configured, and access is granted.  | DevOps |

### Validate the CI/CD pipeline
<a name="validate-the-ci-cd-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify that the CI/CD pipeline automatically initiates. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html)For more information about starting the pipeline by using CodePipeline, see [Start a pipeline in ](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-about-starting.html)CodePipeline, [Start a pipeline manually](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-rerun-manually.html), and [Start a pipeline on a schedule](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-source-schedule.html) in the CodePipeline documentation. | DevOps |
| Approve the deployment. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline.html) | DevOps |
| Validate application profiling. | After the deployment is complete and the application pod is deployed in Amazon EKS, the Amazon CodeGuru Profiler agent that is configured in the application will try to send profiling data of the application (CPU, heap summary, latency, and bottlenecks) to CodeGuru Profiler.<br />For the initial deployment of an application, CodeGuru Profiler takes about 15 minutes to visualize the profiling data. | AWS DevOps |

## Related resources
<a name="automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline-resources"></a>
+ [AWS CodePipeline documentation](https://docs.aws.amazon.com/codepipeline/index.html)
+ [Scanning images with Trivy in an AWS CodePipeline](https://aws.amazon.com/blogs/containers/scanning-images-with-trivy-in-an-aws-codepipeline/) (AWS blog post)
+ [Improving your Java applications using Amazon CodeGuru Profiler](https://aws.amazon.com/blogs/devops/improving-your-java-applications-using-amazon-codeguru-profiler) (AWS blog post)
+ [AWS Security Finding Format (ASFF) syntax](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format-syntax.html)
+ [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html)
+ [Helm upgrade](https://helm.sh/docs/helm/helm_upgrade/)

## Additional information
<a name="automatically-build-and-deploy-a-java-application-to-amazon-eks-using-a-ci-cd-pipeline-additional"></a>
+ CodeGuru Profiler should not be confused with the AWS X-Ray service in terms of functionality. We recommend that you use CodeGuru Profiler to identify the most expensive lines of codes that might cause bottlenecks or security issues, and fix them before they become a potential risk. The X-Ray service is for application performance monitoring.
+ In this pattern, event rules are associated with the default event bus. If needed, you can extend the pattern to use a custom event bus.
+ This pattern uses CodeGuru Reviewer as a static application security testing (SAST) tool for application code. You can also use this pipeline for other tools, such as SonarQube or Checkmarx. You can add the scan setup instructions for any of these tools to `buildspec/buildspec_secscan.yaml` to replace the CodeGuru scan instructions.
**Note**
As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html) in the CodeGuru Reviewer documentation.
