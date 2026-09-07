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

![Workflow for deploying a Java application to Amazon EKS.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/95a5b5c2-d7fb-41eb-9089-455318c0d585/images/4f5fd8c2-2b6d-4945-aa64-fcf317521711.png)

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
| Create an S3 bucket and upload the code. | 1. Sign in to the AWS Management Console, open the [Amazon S3 console](https://console.aws.amazon.com/s3/), and then create an S3 bucket in the AWS Region where you plan to deploy this solution. For more information, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 documentation.<br />2. In the S3 bucket, create a folder named `code`.<br />3. Navigate to where you cloned the repository. To create a compressed version of the entire code with the .zip extension (`cicdstack.zip`) and validate the .zip file, run the following commands in order.<pre>cd aws-codepipeline-devsecops-amazoneks<br />python -m zipfile -c cicdstack.zip *<br />python -m zipfile -t cicdstack.zip</pre>If the `python` command fails and states that Python was not found, use `python3` instead.<br />4. Upload the `cicdstack.zip` file to the code folder that you previously created in the S3 bucket. | AWS DevOps, Cloud administrator, DevOps engineer |
| Create an CloudFormation stack. | 1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/) and choose **Create stack**.<br />2. In **Specify template**, choose **Upload a template file**, upload the `cf_templates/codecommit_ecr.yaml` file, and then choose **Next**.<br />3. In **Specify stack details**, enter the stack name, and then provide the following input parameter values:`CodeCommitRepositoryBranchName`: The name of the branch where your code will reside (the default is `main`)`CodeCommitRepositoryName`: The name of the CodeCommitrepository to create`CodeCommitRepositoryS3Bucket`: The name of the S3 bucket where you created the code folder`CodeCommitRepositoryS3BucketObjKey`: `code/cicdstack.zip``ECRRepositoryName`: The name of the Amazon ECR repository to create<br />4. Choose **Next**, use the default settings for the **Configure stack options**, and then choose **Next**.<br />5. In the **Review** section, verify the template and stack details, and then choose **Create stack**. The stack is then created, including the CodeCommit and Amazon ECR repositories.<br />6. Note the names of the CodeCommit and Amazon ECR repositories, which will be required to set up the Java CI/CD pipeline. | AWS DevOps, DevOps engineer |
| Validate the CloudFormation stack deployment. | 1. Under **Stacks** on the CloudFormation console, verify the status of the CloudFormation stack that you deployed. The status of the stack should be **CREATE COMPLETE**.<br />2. From the console, validate that the CloudFormation and Amazon ECR repositories have been provisioned and are ready. | AWS DevOps, DevOps engineer |
| Delete the S3 bucket. | Empty and delete the S3 bucket that you created earlier. For more information, see [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) in the Amazon S3 documentation. | AWS DevOps, DevOps engineer |

### Configure the Helm charts
<a name="configure-the-helm-charts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the Helm charts of your Java application. | 1. In the location where you cloned the GitHub repository, navigate to the folder `helm_charts/aws-proserve-java-greeting`. In this folder, the `values.dev.yaml`** **file contains information about Kubernetes resources configuration that you can modify for your container deployments to Amazon EKS. Update the Docker repository parameter by providing your AWS account ID, AWS Region, and Amazon ECR repository name.<pre>image:<br />  repository: <account-id>.dkr.ecr.<region>.amazonaws.com/<app-ecr-repo-name></pre><br />2. The Java pod's service type is set to `LoadBalancer`.<pre>service:<br />  type: LoadBalancer<br />  port: 80<br />  targetPort: 8080<br />  path: /hello<br />  initialDelaySeconds: 60<br />  periodSeconds: 30</pre><br />To use a different service (for example, `NodePort`), you can change this parameter. For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types).<br />3. You can activate the [Kubernetes Horizontal Pod Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html) by changing the `autoscaling` parameter to `enabled: true`.<pre>autoscaling:<br />  enabled: true<br />  minReplicas: 1<br />  maxReplicas: 100<br />  targetCPUUtilizationPercentage: 80<br />  # targetMemoryUtilizationPercentage: 80</pre><br />4. You can enable different features for the Kubernetes workloads by changing the values in the `values.<ENV>.yaml` file, where `<ENV>` is your development, production, UAT, or QA environment. | DevOps engineer |
| Validate Helm charts for syntax errors. | 1. From the terminal, verify that Helm v3 is installed in your local workstation by running the following command.<pre>helm --version</pre><br />If Helm v3 isn’t installed, [install it](https://helm.sh/docs/intro/install/).<br />2. In the terminal, navigate to the Helm charts directory (`helm_charts/aws-proserve-java-greeting`), and run the following command.<pre>helm lint . -f values.dev.yaml</pre><br />This will check the Helm charts for any syntax errors. | DevOps engineer |

### Set up the Java CI/CD pipeline
<a name="set-up-the-java-ci-cd-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the CI/CD pipeline. | 1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), and choose **Create stack**.<br />2. In **Specify template**, choose **Upload a template file**, upload the `cf_templates/build_deployment.yaml` template, and then choose **Next**.<br />3. In **Specify stack details**, specify the **Stack name**, and then provide the following values for the input parameters:`CodeBranchName`: Branch name of the CodeCommit repository where your code resides`EKSClusterName`: Name of your EKS cluster (not the `EKSCluster` ID)`EKSCodeBuildAppName`: Name of the app Helm chart (`aws-proserve-java-greeting`)`EKSWorkerNodeRoleARN`: ARN of the IAM role assigned to the Amazon EKS worker nodes`EKSWorkerNodeRoleName`: Name of the IAM role assigned to the Amazon EKS worker nodes`EcrDockerRepository`: Name of the Amazon ECR repository where the Docker images of your code will be stored`EmailRecipient`: Email address where build notifications should be sent`EnvType`: Environment (for example, dev, test, or prod)`SourceRepoName`: Name of the CodeCommit repository where your code resides<br />4. Choose **Next**. Use the default settings in **Configure stack options**, and then choose **Next**.<br />5. In the **Review** section, verify the CloudFormation template and stack details, and then choose **Next**.<br />6. Choose **Create stack**. <br />7. During the CloudFormation stack deployment, the owner of the email address that you provided in the parameters will receive a message to subscribe to an SNS topic. To subscribe to Amazon SNS, the owner must choose the link in the message.<br />8. After the stack is created, open the **Outputs** tab of the stack, and then record the ARN value for the `EksCodeBuildkubeRoleARN` output key. This IAM ARN value will be required later when you provide permissions for the CodeBuild IAM role to deploy workloads in the Amazon EKS cluster. | AWS DevOps |

### Activate integration between Security Hub CSPM and Aqua Security
<a name="activate-integration-between-ash-and-aqua-security"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Turn on Aqua Security integration. | This step is required for uploading the Docker image vulnerability findings reported by Trivy to Security Hub CSPM. Because CloudFormation doesn’t support Security Hub CSPM integrations, this process must be done manually.1. Open the [AWS Security Hub CSPM console](https://console.aws.amazon.com/securityhub/), and navigate to **Integrations**.<br />2. Search for Aqua Security, and select **Aqua Security: Aqua Security**.<br />3. Choose **Accept findings**. | AWS administrator, DevOps engineer |

### Configure CodeBuild to run Helm or kubectl commands
<a name="configure-acb-to-run-helm-or-kubectl-commands"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Allow CodeBuild to run Helm or kubectl commands in the Amazon EKS cluster. | For CodeBuild to be authenticated to use Helm or `kubectl` commands with the Amazon EKS cluster, you must add the IAM roles to the `aws-auth` `ConfigMap`. In this case, add the ARN of the IAM role `EksCodeBuildkubeRoleARN`, which is the IAM role created for the CodeBuild service to access the Amazon EKS cluster and deploy workloads on it. This is a one-time activity.The following procedure must be completed before the deployment approval stage in CodePipeline.1. Open the `cf_templates/kube_aws_auth_configmap_patch.sh` shell script in your Amazon Linux or macOS environment.<br />2. Authenticate to the Amazon EKS cluster by running the following command.<pre>aws eks --region <aws-region> update-kubeconfig --name <eks-cluster-name></pre><br />3. Run the shell script by using the following command, replacing `<rolearn-eks-codebuild-kubectl>` with the ARN value of `EksCodeBuildkubeRoleARN` that you recorded earlier.<pre>bash cf_templates/kube_aws_auth_configmap_patch.sh <rolearn-eks-codebuild-kubectl> </pre><br />The `aws_auth` `ConfigMap` is configured, and access is granted.  | DevOps |

### Validate the CI/CD pipeline
<a name="validate-the-ci-cd-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify that the CI/CD pipeline automatically initiates. | 1. The CodeSecurity Scan stage in the pipeline will usually fail if Checkov detects vulnerabilities in the Dockerfile or Helm charts. However, the purpose of this example is to establish a process of identifying potential security vulnerabilities rather than fixing it through the CI/CD pipeline, typically a DevSecOps process. In the file `buildspec/buildspec_secscan.yaml`, the `checkov` command uses the `--soft-fail` flag to avoid pipeline failure.<pre>- echo -e "\n Running Dockerfile Scan"<br />- checkov -f code/app/Dockerfile --framework dockerfile --soft-fail --summary-position bottom<br />- echo -e "\n Running Scan of Helm Chart files"<br />- cp -pv helm_charts/$EKS_CODEBUILD_APP_NAME/values.dev.yaml helm_charts/$EKS_CODEBUILD_APP_NAME/values.yaml<br />- checkov -d helm_charts/$EKS_CODEBUILD_APP_NAME --framework helm --soft-fail --summary-position bottom<br />- rm -rfv helm_charts/$EKS_CODEBUILD_APP_NAME/values.yaml</pre><br />For the pipeline to fail when vulnerabilities are reported for the Dockerfile and Helm charts, the `--soft-fail` option must be removed from the `checkov` command. Developers or engineers can then fix the vulnerabilities and commit the changes to the CodeCommit source code repository.<br />2. Similar to CodeSecurity Scan, the Build stage uses Aqua Security Trivy to identify `HIGH` and `CRITICAL` Docker image vulnerabilities before pushing the application to Amazon ECR.<pre>- AWS_REGION=$AWS_DEFAULT_REGION AWS_ACCOUNT_ID=$AWS_ACCOUNT_ID trivy -d image --no-progress --ignore-unfixed --exit-code 0 --severity HIGH,CRITICAL --format template --template "@securityhub/asff.tpl" -o securityhub/report.asff $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$CODEBUILD_RESOLVED_SOURCE_VERSION</pre><br />In this example, the pipeline doesn’t fail when Docker image vulnerabilities are reported, because the `trivy` command in the `buildspec/buildspec.yml` file includes the flag** **`--exit-code`** **with a value** **of`0`. For the pipeline to fail when `HIGH` and `CRTICAL` vulnerabilities are reported, change the value of `--exit-code` to `1`. Developers or engineers can then fix the vulnerabilities and commit the changes to the CodeCommit source code repository.<br />3. Docker image vulnerabilities reported by Aqua Security Trivy are uploaded to Security Hub CSPM. On the Security Hub CSPM console, navigate to **Findings**. Filter the findings with **Record** **State = Active** and **Product = Aqua Security**. This lists the Docker image vulnerabilities in Security Hub CSPM. It can take 15 minutes to an hour for vulnerabilities to appear in Security Hub CSPM.For more information about starting the pipeline by using CodePipeline, see [Start a pipeline in ](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-about-starting.html)CodePipeline, [Start a pipeline manually](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-rerun-manually.html), and [Start a pipeline on a schedule](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-source-schedule.html) in the CodePipeline documentation. | DevOps |
| Approve the deployment. | 1. After the build phase is complete, there is a deployment approval gate. The reviewer or a release manager should inspect the build, and, if all requirements are met, approve it. This is the recommended approach for teams that use continuous delivery for application deployment.<br />2. After approval, the pipeline initiates the Deploy stage.<br />3. After the Deploy stage is successful, the CodeBuild log for this stage provides the URL of the application. Use the URL to validate the readiness of the application. | DevOps |
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
