---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab.html
---

# Set up a CI/CD pipeline for hybrid workloads on Amazon ECS Anywhere by using AWS CDK and GitLab
<a name="set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab"></a>

*Rafael Ortiz, Amazon Web Services*

## Summary
<a name="set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab-summary"></a>

Amazon ECS Anywhere is an extension of the Amazon Elastic Container Service (Amazon ECS). It provides support for registering an *external instance*, such as an on-premises server or virtual machine (VM), to your Amazon ECS cluster. is feature helps reduce costs and mitigate complex local container orchestration and operations. You can use ECS Anywhere to deploy and run container applications in both on-premises and cloud environments. It removes the need for your team to learn multiple domains and skill sets, or to manage complex software on their own.

This pattern describes a step-by-step approach to provision an Amazon ECS cluster with Amazon ECS Anywhere instances by using Amazon Web Services (AWS) Cloud Development Kit (AWS CDK) stacks. You then use AWS CodePipeline to set up a continuous integration and continuous deployment (CI/CD) pipeline. Then, you replicate your GitLab code repository to AWS CodeCommit and deploy your containerized application on the Amazon ECS cluster.

This pattern is designed to help those who use on-premises infrastructure to run container applications and use GitLab to manage the application code base. You can manage those workloads by using AWS Cloud services, without disturbing your existing, on-premises infrastructure.

## Prerequisites and limitations
<a name="set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ A container application running on on-premises infrastructure.
+ A GitLab repository where you manage your application code base. For more information, see [Repository](https://docs.gitlab.com/ee/user/project/repository/) (GitLab).
+ AWS Command Line Interface (AWS CLI), installed and configured. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (AWS CLI documentation).
+ AWS CDK Toolkit, installed and configured globally. For more information, see [Install the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install) (AWS CDK documentation).
+ npm, installed and configured for the AWS CDK in TypeScript. For more information, see [Downloading and installing Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) (npm documentation).

**Limitations**
+ For limitations and considerations, see [External instances (Amazon ECS Anywhere)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html#ecs-anywhere-considerations) in the Amazon ECS documentation.

**Product versions**
+ AWS CDK Toolkit version 2.27.0 or later
+ npm version 7.20.3 or later
+ Node.js version 16.6.1 or later

## Architecture
<a name="set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab-architecture"></a>

**Target technology stack**
+ AWS CDK
+ AWS CloudFormation
+ AWS CodeBuild
+ AWS CodeCommit
+ AWS CodePipeline
+ Amazon ECS Anywhere
+ Amazon Elastic Container Registry (Amazon ECR)
+ AWS Identity and Access Management (IAM)
+ AWS System Manager
+ GitLab repository

**Target architecture**

![Architecture diagram of setting up the Amazon ECS cluster and CI/CD pipeline.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b0f35986-a839-4b01-8eb0-4748182ddafc/images/85b8d4d9-3591-4d69-a54b-64aa543498f1.png)

This diagram represents two primary workflows described in this pattern, provisioning the Amazon ECS cluster and setting up the CI/CD pipeline that sets up and deploys the CI/CD pipeline, as follows:

1. **Provisioning the Amazon ECS cluster**

   1. When you deploy the first AWS CDK stack, it creates a CloudFormation stack on AWS.

   1. This CloudFormation stack provisions an Amazon ECS cluster and related AWS resources.

   1. To register an external instance with an Amazon ECS cluster, you must install AWS Systems Manager Agent (SSM Agent) on your VM and register the VM as an AWS Systems Manager managed instance.

   1. You must also install the Amazon ECS container agent and Docker on your VM to register it as an external instance with the Amazon ECS cluster.

   1. When the external instance is registered and configured with the Amazon ECS cluster, it can run multiple containers on your VM, which is registered as an external instance.

   1. The Amazon ECS cluster is active and can run the application workloads through containers. The Amazon ECS Anywhere container instance runs in on-premises environment but is associated with the Amazon ECS cluster in the cloud.

1. **Setting up and deploying the CI/CD pipeline**

   1. When you deploy the second AWS CDK stack, it creates another CloudFormation stack on AWS.

   1. This CloudFormation stack provisions a pipeline in CodePipeline and related AWS resources.

   1. You push and merge application code changes to an on-premises GitLab repository.

   1. The GitLab repository is automatically replicated to the CodeCommit repository.

   1. The updates to the CodeCommit repo automatically starts CodePipeline.

   1. CodePipeline copies code from CodeCommit and creates the deployable application build in CodeBuild.

   1. CodePipeline creates a Docker image of the CodeBuild build environment and pushes it to the Amazon ECR repo.

   1. CodePipeline initiates CodeDeploy actions that pull the container image from the Amazon ECR repo.

   1. CodePipeline deploys the container image on the Amazon ECS cluster.

**Automation and scale**

This pattern uses the AWS CDK as an infrastructure as code (IaC) tool to configure and deploy this architecture. AWS CDK helps you orchestrate the AWS resources and set up Amazon ECS Anywhere and the CI/CD pipeline.

## Tools
<a name="set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a fast and scalable container management service that helps you run, stop, and manage containers on a cluster. This pattern also uses [Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html), which provides support for registering an on-premises server or VM to your Amazon ECS cluster.

**Other tools**
+ [Node.js](https://nodejs.org/en/docs/) is an event-driven JavaScript runtime environment designed for building scalable network applications.
+ [npm](https://docs.npmjs.com/about-npm) is a software registry that runs in a Node.js environment and is used to share or borrow packages and manage deployment of private packages.
+ [Vagrant](https://developer.hashicorp.com/vagrant/docs) is an open-source utility for building and maintaining portable virtual software development environments. For demonstration purposes, this pattern uses Vagrant to create an on-premises VM.

**Code repository**

The code for this pattern is available in the GitHub [CI/CD pipeline for Amazon ECS Anywhere using AWS CDK](https://github.com/aws-samples/amazon-ecs-anywhere-cicd-pipeline-cdk-sample) repository.

## Best practices
<a name="set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab-best-practices"></a>

Consider the following best practices when deploying this pattern:
+ [Best practices for developing and deploying cloud infrastructure with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/best-practices.html)
+ [Best practices for developing cloud applications with AWS CDK](https://aws.amazon.com/blogs/devops/best-practices-for-developing-cloud-applications-with-aws-cdk/) (AWS blog post)

## Epics
<a name="set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab-epics"></a>

### Verify the AWS CDK configuration
<a name="verify-the-aws-cdk-configuration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify the AWS CDK version. | Verify the version of the AWS CDK Toolkit by entering the following command.<pre>cdk --version</pre><br />This pattern requires version 2.27.0 or later. If you have an earlier version, follow the instructions in the [AWS CDK documentation](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) to update it. | DevOps engineer |
| Verify the npm version. | Verify the version of npm by entering the following command.<pre>npm --version</pre><br />This pattern requires version 7.20.3 or later. If you have an earlier version, follow the instructions in the [npm documentation](https://docs.npmjs.com/try-the-latest-stable-version-of-npm) to update it. | DevOps engineer |
| Set up AWS credentials. | Set up AWS credentials by entering the `aws configure` command and following the prompts.<pre>$aws configure<br />AWS Access Key ID [None]: <your-access-key-ID><br />AWS Secret Access Key [None]: <your-secret-access-key><br />Default region name [None]: <your-Region-name><br />Default output format [None]:</pre> | DevOps engineer |

### Bootstrap the AWS CDK environment
<a name="bootstrap-the-aws-cdk-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the AWS CDK code repository. | 1. Clone the [CI/CD pipeline for Amazon ECS Anywhere using AWS CDK](https://github.com/aws-samples/amazon-ecs-anywhere-cicd-pipeline-cdk-sample) repository for this pattern by entering the following command.<pre>git clone https://github.com/aws-samples/amazon-ecs-anywhere-cicd-pipeline-cdk-sample.git</pre><br />2. Navigate into the cloned directory by entering the following command.<pre>cd amazon-ecs-anywhere-cicd-pipeline-cdk-sample</pre> | DevOps engineer |
| Bootstrap the environment. | Deploy the CloudFormation template to the account and AWS Region that you want to use by entering the following command.<pre>cdk bootstrap <account-number>/<Region></pre><br />For more information, see [Bootstrapping](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html) in the AWS CDK documentation. | DevOps engineer |

### Build and deploy the infrastructure for Amazon ECS Anywhere
<a name="build-and-deploy-the-infrastructure-for-amazon-ecs-anywhere"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the package dependencies and compile the TypeScript files. | Install the package dependencies and compile the TypeScript files by entering the following commands.<pre>$cd EcsAnywhereCdk<br />$npm install<br />$npm fund </pre><br />These commands install all the packages from the sample repository. For more information, see [npm ci](https://docs.npmjs.com/cli/v7/commands/npm-ci) and [npm install](https://docs.npmjs.com/cli/v7/commands/npm-install) in the npm documentation. If you get any errors about missing packages when you enter these commands, see the [Troubleshooting](#set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab-troubleshooting) section of this pattern. | DevOps engineer |
| Build the project. | To build the project code, enter the following command.<pre>npm run build</pre><br />For more information about building and deploying the project, see [Your first AWS CDK app](https://docs.aws.amazon.com/cdk/latest/guide/hello_world.html#:~:text=the%20third%20parameter.-,Synthesize%20an%20AWS%20CloudFormation%20template,-Synthesize%20an%20AWS) in the AWS CDK documentation. | DevOps engineer |
| Deploy the Amazon ECS Anywhere infrastructure stack. | 1. List the stacks by entering the following command.<pre>$cdk list</pre><br />2. Confirm that the output returns the `EcsAnywhereInfraStack` and `ECSAnywherePipelineStack` stacks.<br />3. Deploy the `EcsAnywhereInfraStack` stack by entering the following command.<pre>$cdk  deploy EcsAnywhereInfraStack</pre> | DevOps engineer |
| Verify stack creation and output. | 1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation/](https://console.aws.amazon.com/cloudformation/).<br />2. On the **Stacks** page, select the `EcsAnywhereInfraStack` stack.<br />3. Confirm that the stack status is either `CREATE_IN_PROGRESS` or `CREATE_COMPLETE`. <br />Setting up the Amazon ECS cluster can take some time. Do not proceed until the stack creation is complete. | DevOps engineer |

### Set up an on-premises VM
<a name="set-up-an-on-premises-vm"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up your VM. | Create a Vagrant VM by entering the `vagrant up` command from the root directory where Vagrantfile is located. For more information, see the [Vagrant documentation](https://developer.hashicorp.com/vagrant/docs/cli/up). | DevOps engineer |
| Register your VM as an external instance. | 1. Log in to the Vagrant VM by using the `vagrant ssh` command. For more information, see the [Vagrant documentation](https://developer.hashicorp.com/vagrant/docs/cli/ssh).<br />2. Install AWS CLI on the VM by following [AWS CLI installation instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and entering the following commands. <pre>$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" \<br />> -o "awscliv2.zip"<br />$sudo apt install unzip<br />$unzip awscliv2.zip<br />$sudo ./aws/install<br />$aws configure<br />AWS Access Key ID [None]: <your-access-key-ID><br />AWS Secret Access Key [None]: <your-secret-access-key><br />Default region name [None]: <your-Region-name><br />Default output format [None]:</pre>1. Create an activation code and ID that you can use to register your VM with AWS Systems Manager and to activate your external instance. The output from this command includes the activation ID and activation code values.<pre>aws ssm create-activation \<br />> --iam-role EcsAnywhereInstanceRole \<br />> | tee ssm-activation.json</pre><br />If you receive an error when you run this command, see the [Troubleshooting](#set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab-troubleshooting) section.<br />2. Export the activation ID and code values.<pre>export ACTIVATION_ID=<activation-ID><br />export ACTIVATION_CODE=<activation-code></pre><br />3. Download the installation script to your VM.<pre>curl --proto "https" -o "ecs-anywhere-install.sh" \<br />> "https://amazon-ecs-agent.s3.amazonaws.com/ecs-anywhere-install-latest.sh"</pre><br />4. Run the installation script on your VM.<pre>sudo bash ecs-anywhere-install.sh \<br />--cluster EcsAnywhereCluster \<br />--activation-id $ACTIVATION_ID \<br />--activation-code $ACTIVATION_CODE \<br />--region <region-name></pre>This sets up your VM was an Amazon ECS Anywhere external instance and registers the instance in the Amazon ECS cluster. For more information, see [Registering an external instance to a cluster](https://docs.amazonaws.cn/en_us/AmazonECS/latest/developerguide/ecs-anywhere-registration.html) in the Amazon ECS documentation. If you experience any issues, see the [Troubleshooting](#set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab-troubleshooting) section. | DevOps engineer |
| Verify the status of Amazon ECS Anywhere and the external VM. | To verify whether your VM is connected to the Amazon ECS control plane and running, use the following commands.<pre>$aws ssm describe-instance-information<br />$aws ecs list-container-instances --cluster $CLUSTER_NAME</pre> | DevOps engineer |

### Deploy the CI/CD pipeline
<a name="deploy-the-ci-cd-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a branch in the CodeCommit repo. | Create a branch named `main` in the CodeCommit repo by creating the first commit for the repository. You can follow AWS documentation to [Create a commit in CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-commit.html#create-first-commit). The following command is an example.<pre>aws codecommit put-file \<br />  --repository-name EcsAnywhereRepo \<br />  --branch-name main \<br />  --file-path README.md \<br />  --file-content "Test" \<br />  --name "Dev Ops" \<br />  --email "devops@example.com" \<br />  --commit-message "Adding README."</pre> | DevOps engineer |
| Set up repo mirroring. | You can mirror a GitLab repository to and from external sources. You can select which repository serves as the source. Branches, tags, and commits are synced automatically. Set up a push mirror between the GitLab repository that hosts your application and the CodeCommit repository. For instructions, see [Set up a push mirror from GitLab to CodeCommit](https://docs.gitlab.com/ee/user/project/repository/mirror/push.html#set-up-a-push-mirror-from-gitlab-to-aws-codecommit) (GitLab documentation).By default, mirroring automatically syncs the repository. If you want to manually update the repositories, see [Update a mirror](https://docs.gitlab.com/ee/user/project/repository/mirror/#update-a-mirror) (GitLab documentation). | DevOps engineer |
| Deploy the CI/CD pipeline stack. | Deploy the `EcsAnywherePipelineStack` stack by entering the following command.<pre>$cdk  deploy EcsAnywherePipelineStack</pre> | DevOps engineer |
| Test the CI/CD pipeline. | 1. Make application code changes and push it to the source, on-premises GitLab repo. For example, edit the `../application/index.html` file to update the application version value.<br />2. When the code is replicated to the CodeCommit repo, this starts the CI/CD pipeline. Do one of the following:If you are using automatic mirroring to synchronize the GitLab repo with the CodeCommit repo, continue to the next step.If you are using manual mirroring, push the application code changes to the CodeCommit repo by following the instructions in [Update a mirror](https://docs.gitlab.com/ee/user/project/repository/mirror/#update-a-mirror) (GitLab documentation).<br />3. On your local machine, in a web browser, enter [http://localhost:80](http://localhost:80). This opens the NGINX web page because port 80 is forwarded to localhost in Vagrantfile. Confirm that you can view the updated application version value. This validates the pipeline and image deployment.<br />4. (Optional) If you want to verify the deployment in the AWS Management Console, do the following:Open the Amazon ECS console at [https://console.aws.amazon.com/ecs/](https://console.aws.amazon.com/ecs/).From the navigation bar, select the Region to use.In the navigation pane, choose **Clusters**.On the **Clusters** page, select the **EcsAnywhereCluster** cluster.Choose **Task Definitions**.Confirm the container is running. | DevOps engineer |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up and delete the resources. | After you walk through this pattern, you should remove the proof-of-concept resources you created. To clean up, enter the following commands.<pre>$cdk destroy EcsAnywherePipelineStack<br />$cdk destroy EcsAnywhereInfraStack</pre> | DevOps engineer |

## Troubleshooting
<a name="set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Errors about missing packages when installing package dependencies. | Enter one of the following commands to resolve missing packages.<pre>$npm ci</pre><br />or<pre>$npm install -g @aws-cdk/<package_name></pre> |
| When you run the `aws ssm create-activation` command on the VM, you receive the following error.<br />`An error occurred (ValidationException) when calling the CreateActivation operation: Nonexistent role or missing ssm service principal in trust policy: arn:aws:iam::000000000000:role/EcsAnywhereInstanceRole` | The `EcsAnywhereInfraStack` stack isn’t fully deployed, and the IAM role necessary to run this command hasn’t been created yet. Check the stack status in the CloudFormation console. Retry the command after the status changes to `CREATE_COMPLETE`. |
| An Amazon ECS health check returns `UNHEALTHY`, and you see the following error in the **Services** section of the cluster in the Amazon ECS console.<br />`service EcsAnywhereService was unable to place a task because no container instance met all of its requirements. Reason: No Container Instances were found in your cluster.` | Restart the Amazon ECS agent on your Vagrant VM by entering the following commands.<pre>$vagrant ssh<br />$sudo systemctl restart ecs<br />$sudo systemctl status ecs</pre> |

## Related resources
<a name="set-up-a-ci-cd-pipeline-for-hybrid-workloads-on-amazon-ecs-anywhere-by-using-aws-cdk-and-gitlab-resources"></a>
+ [Amazon ECS Anywhere marketing page](https://aws.amazon.com/ecs/anywhere/)
+ [Amazon ECS Anywhere documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html#ecs-anywhere-considerations)
+ [Amazon ECS Anywhere demo](https://www.youtube.com/watch?v=-eud6yUXsJM) (video)
+ [Amazon ECS Anywhere workshop samples](https://github.com/aws-samples/aws-ecs-anywhere-workshop-samples) (GitHub)
+ [Repository mirroring](https://docs.gitlab.com/ee/user/project/repository/mirror/) (GitLab documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
