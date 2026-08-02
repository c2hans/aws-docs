---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-on-premises-container-applications-by-setting-up-amazon-ecs-anywhere-with-the-aws-cdk.html
---

# Manage on-premises container applications by setting up Amazon ECS Anywhere with the AWS CDK
<a name="manage-on-premises-container-applications-by-setting-up-amazon-ecs-anywhere-with-the-aws-cdk"></a>

*Dr. Rahul Sharad Gaikwad, Amazon Web Services*

## Summary
<a name="manage-on-premises-container-applications-by-setting-up-amazon-ecs-anywhere-with-the-aws-cdk-summary"></a>

[Amazon ECS Anywhere](https://aws.amazon.com/ecs/anywhere/) is an extension of the Amazon Elastic Container Service (Amazon ECS). You can use ECS Anywhere to deploy native Amazon ECS tasks in an on-premises or customer-managed environment. This feature helps reduce costs and mitigate complex local container orchestration and operations. You can use ECS Anywhere to deploy and run container applications in both on-premises and cloud environments. It removes the need for your team to learn multiple domains and skill sets, or to manage complex software on their own.

This pattern demonstrates the steps to set up ECS Anywhere by using [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) stacks.

## Prerequisites and limitations
<a name="manage-on-premises-container-applications-by-setting-up-amazon-ecs-anywhere-with-the-aws-cdk-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI), installed and configured. (See [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the AWS CLI documentation.)
+ AWS CDK Toolkit, installed and configured. (See [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) in the AWS CDK documentation, and follow the instructions to install version 2 globally.)
+ Node package manager (npm), installed and configured for the AWS CDK in TypeScript. (See [Downloading and installing Node.js and npm ](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)in the npm documentation.)

**Limitations **
+ For limitations and considerations, see [External instances (Amazon ECS Anywhere)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html#ecs-anywhere-considerations) in the Amazon ECS documentation.

**Product versions**
+ AWS CDK Toolkit version 2
+ npm version 7.20.3 or later
+ Node.js version 16.6.1 or later

## Architecture
<a name="manage-on-premises-container-applications-by-setting-up-amazon-ecs-anywhere-with-the-aws-cdk-architecture"></a>

**Target technology stack  **
+ AWS CloudFormation
+ AWS CDK
+ Amazon ECS Anywhere
+ AWS Identity and Access Management (IAM)

**Target architecture **

The following diagram illustrates a high-level system architecture of ECS Anywhere setup using the AWS CDK with TypeScript, as implemented by this pattern.

1. When you deploy the AWS CDK stack, it creates a CloudFormation stack on AWS.

1. The CloudFormation stack provisions an Amazon ECS cluster and related AWS resources.

1. To register an external instance with an Amazon ECS cluster, you must install AWS Systems Manager Agent (SSM Agent) on your virtual machine (VM) and register the VM as an AWS Systems Manager managed instance.

1. You must also install the Amazon ECS container agent and Docker on your VM to register it as an external instance with the Amazon ECS cluster.

1. When the external instance is registered and configured with the Amazon ECS cluster, it can run multiple containers on your VM, which is registered as an external instance.

![ECS Anywhere setup using the AWS CDK with TypeScript.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/3ed63c00-40e7-4831-bb9d-63049c3490aa/images/ff7dc774-830d-4b9f-8262-7314afe7a033.png)

**Automation and scale**

The [GitHub repository](https://github.com/aws-samples/amazon-ecs-anywhere-cdk-samples/) that is provided with this pattern uses the AWS CDK as an infrastructure as code (IaC) tool to create the configuration for this architecture. AWS CDK helps you orchestrate resources and set up ECS Anywhere.

## Tools
<a name="manage-on-premises-container-applications-by-setting-up-amazon-ecs-anywhere-with-the-aws-cdk-tools"></a>
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.

**Code**

The source code for this pattern is available on GitHub, in the [Amazon ECS Anywhere CDK Samples](https://github.com/aws-samples/amazon-ecs-anywhere-cdk-samples) repository. To clone and use the repository, follow the instructions in the next section.

## Epics
<a name="manage-on-premises-container-applications-by-setting-up-amazon-ecs-anywhere-with-the-aws-cdk-epics"></a>

### Verify AWS CDK configuration
<a name="verify-aws-cdk-configuration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify the AWS CDK version. | Verify the version of the AWS CDK Toolkit by running the following command:<pre>cdk --version</pre><br />This pattern requires AWS CDK version 2. If you have an earlier version of the AWS CDK, follow the instructions in the [AWS CDK documentation](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) to update it. | DevOps engineer |
| Set up AWS credentials. | To set up credentials, run the `aws configure` command and follow the prompts:<pre>$aws configure<br />AWS Access Key ID [None]: <your-access-key-ID><br />AWS Secret Access Key [None]: <your-secret-access-key><br />Default region name [None]: <your-Region-name><br />Default output format [None]:</pre> | DevOps engineer |

### Bootstrap the AWS CDK environment
<a name="bootstrap-the-aws-cdk-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the AWS CDK code repository. | Clone the GitHub code repository for this pattern by using the command:<pre>git clone https://github.com/aws-samples/amazon-ecs-anywhere-cdk-samples.git</pre> | DevOps engineer |
| Bootstrap the environment. | To deploy the AWS CloudFormation template to the account and AWS Region that you want to use, run the following command:<pre>cdk bootstrap <account-number>/<Region></pre><br />For more information, see [Bootstrapping](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html) in the AWS CDK documentation. | DevOps engineer |

### Build and deploy the project
<a name="build-and-deploy-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install package dependencies and compile TypeScript files. | Install the package dependencies and compile the TypeScript files by running the following commands:<pre>$cd amazon-ecs-anywhere-cdk-samples<br />$npm install<br />$npm fund </pre><br />These commands install all the packages from the sample repository. If you get any errors about missing packages, use one of the following commands:<pre>$npm ci   </pre><br />—or—<pre>$npm install -g @aws-cdk/<package_name></pre><br />For more information, see [npm ci](https://docs.npmjs.com/cli/v7/commands/npm-ci) and  [npm install](https://docs.npmjs.com/cli/v7/commands/npm-install) in the npm documentation. | DevOps engineer |
| Build the project. | To build the project code, run the command:<pre>npm run build</pre><br />For more information about building and deploying the project, see [Your first AWS CDK app](https://docs.aws.amazon.com/cdk/latest/guide/hello_world.html#:~:text=the%20third%20parameter.-,Synthesize%20an%20AWS%20CloudFormation%20template,-Synthesize%20an%20AWS) in the AWS CDK documentation. | DevOps engineer |
| Deploy the project. | To deploy the project code, run the command:<pre>cdk deploy</pre> | DevOps engineer |
| Verify stack creation and output. | Open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/),** **and choose the `EcsAnywhereStack` stack. The **Outputs** tab shows the commands to run on your external VM. | DevOps engineer |

### Set up an on-premises machine
<a name="set-up-an-on-premises-machine"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up your VM by using Vagrant. | For demonstration purposes, you can use [HashiCorp Vagrant](https://www.vagrantup.com/) to create a VM. Vagrant is an open-source utility for building and maintaining portable virtual software development environments. Create a Vagrant VM by running the `vagrant up` command from the root directory where Vagrantfile is placed. For more information, see the [Vagrant documentation](https://www.vagrantup.com/docs/cli/up). | DevOps engineer |
| Register your VM as an external instance. | 1. Log in to the Vagrant VM by using the `vagrant ssh` command. For more information, see the [Vagrant documentation](https://www.vagrantup.com/docs/cli/ssh).<br />2. Create an activation code and ID that you can use to register your VM with AWS Systems Manager and to activate your external instance. The output from this command includes `ActivationId` and `ActivationCode` values: <pre>aws ssm create-activation --iam-role EcsAnywhereInstanceRole | tee ssm-activation.json</pre><br />3. Export the activation ID and code values:<pre>export ACTIVATION_ID=<activation-ID><br />export ACTIVATION_CODE=<activation-code></pre><br />4. Download the installation script to your on-premises server or VM:<pre>curl -o "ecs-anywhere-install.sh" "https://amazon-ecs-agent.s3.amazonaws.com/ecs-anywhere-install-latest.sh" && sudo chmod +x ecs-anywhere-install.sh</pre><br />5. Run the installation script on your on-premises server or VM:<pre>sudo ./ecs-anywhere-install.sh \<br />    --cluster test-ecs-anywhere \<br />     --activation-id $ACTIVATION_ID \<br />     --activation-code $ACTIVATION_CODE \<br />    --region <Region></pre><br />For more information about setting up and registering your VM, see [Registering an external instance to a cluster](https://docs.amazonaws.cn/en_us/AmazonECS/latest/developerguide/ecs-anywhere-registration.html) in the Amazon ECS documentation. | DevOps engineer |
| Verify the status of ECS Anywhere and the external VM. | To verify whether your virtual box is connected to the Amazon ECS control plane and running, use the following commands:<pre>aws ssm describe-instance-information<br />aws ecs list-container-instances --cluster $CLUSTER_NAME</pre> | DevOps engineer |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up and delete resources. | After you walk through this pattern, you should remove the resources you created to avoid incurring any further charges. To clean up, run the command:<pre>cdk destroy</pre> | DevOps engineer |

## Related resources
<a name="manage-on-premises-container-applications-by-setting-up-amazon-ecs-anywhere-with-the-aws-cdk-resources"></a>
+ [Amazon ECS Anywhere Documentation](https://aws.amazon.com/ecs/anywhere/)
+ [Amazon ECS Anywhere Demo](https://www.youtube.com/watch?v=-eud6yUXsJM)
+ [Amazon ECS Anywhere Workshop Samples](https://github.com/aws-samples/aws-ecs-anywhere-workshop-samples)
