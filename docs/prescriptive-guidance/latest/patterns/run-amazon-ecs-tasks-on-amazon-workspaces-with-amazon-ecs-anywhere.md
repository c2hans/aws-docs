---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-amazon-ecs-tasks-on-amazon-workspaces-with-amazon-ecs-anywhere.html
---

# Run Amazon ECS tasks on Amazon WorkSpaces with Amazon ECS Anywhere
<a name="run-amazon-ecs-tasks-on-amazon-workspaces-with-amazon-ecs-anywhere"></a>

*Akash Kumar, Amazon Web Services*

## Summary
<a name="run-amazon-ecs-tasks-on-amazon-workspaces-with-amazon-ecs-anywhere-summary"></a>

Amazon Elastic Container Service (Amazon ECS) Anywhere supports the deployment of Amazon ECS tasks in any environment, including Amazon Web Services (AWS) managed infrastructure and customer managed infrastructure. You can do this while using a fully AWS managed control plane that’s running in the cloud and always up to date.

Enterprises often use Amazon WorkSpaces for developing container-based applications. This has required Amazon Elastic Compute Cloud (Amazon EC2) or AWS Fargate with an Amazon ECS cluster to test and run ECS tasks. Now, by using Amazon ECS Anywhere, you can add Amazon WorkSpaces as external instances directly to an ECS cluster, and you can run your tasks directly. This reduces your development time, because you can test your container with an ECS cluster locally on Amazon WorkSpaces. You can also save the cost of using EC2 or Fargate instances for testing your container applications.

This pattern showcases how to deploy ECS tasks on Amazon WorkSpaces with Amazon ECS Anywhere. It sets up the ECS cluster and uses AWS Directory Service Simple AD to launch the WorkSpaces. Then the example ECS task launches NGINX in the WorkSpaces.

## Prerequisites and limitations
<a name="run-amazon-ecs-tasks-on-amazon-workspaces-with-amazon-ecs-anywhere-prereqs"></a>
+ An active AWS account
+ AWS Command Line Interface (AWS CLI)
+ AWS credentials [configured on your machine](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

## Architecture
<a name="run-amazon-ecs-tasks-on-amazon-workspaces-with-amazon-ecs-anywhere-architecture"></a>

**Target technology stack**
+ A virtual private cloud (VPC)
+ An Amazon ECS cluster
+ Amazon WorkSpaces
+ AWS Directory Service with Simple AD

**Target architecture **

![ECS Anywhere sets up ECS cluster and uses Simple AD to launch WorkSpaces.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/da8b2249-3423-485c-9fef-6f902025e969/images/fd354d14-f29b-4b9e-8f1a-c3cb7ed4d6bf.png)

The architecture includes the following services and resources:
+ An ECS cluster with public and private subnets in a custom VPC
+ Simple AD in the VPC to provide user access to Amazon WorkSpaces
+ Amazon WorkSpaces provisioned in the VPC using Simple AD
+ AWS Systems Manager activated for adding Amazon WorkSpaces as managed instances
+ Using Amazon ECS and AWS Systems Manager Agent (SSM Agent), Amazon WorkSpaces added to Systems Manager and the ECS cluster
+ An example ECS task to run in the WorkSpaces in the ECS cluster

## Tools
<a name="run-amazon-ecs-tasks-on-amazon-workspaces-with-amazon-ecs-anywhere-tools"></a>
+ [AWS Directory Service Simple Active Directory (Simple AD)](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html) is a standalone managed directory powered by a Samba 4 Active Directory Compatible Server. Simple AD provides a subset of the features offered by AWS Managed Microsoft AD, including the ability to manage users and to securely connect to Amazon EC2 instances.
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a fast and scalable container management service that helps you run, stop, and manage containers on a cluster.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale.
+ [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) helps you provision virtual, cloud-based Microsoft Windows or Amazon Linux desktops for your users, known as *WorkSpaces*. WorkSpaces eliminates the need to procure and deploy hardware or install complex software.

## Epics
<a name="run-amazon-ecs-tasks-on-amazon-workspaces-with-amazon-ecs-anywhere-epics"></a>

### Set up the ECS cluster
<a name="set-up-the-ecs-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and configure the ECS cluster. | To create the ECS cluster, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create_cluster.html), including the following steps:+ For **Select cluster compatibility**, choose **Networking only**, which will support an Amazon WorkSpace as an external instance to the ECS cluster.<br />+ Choose to create a new VPC. | Cloud architect |

### Launch Amazon WorkSpaces
<a name="launch-amazon-workspaces"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Simple AD and launch Amazon WorkSpaces. | To provision a Simple AD directory for your newly created VPC and launch Amazon WorkSpaces, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspace-simple-ad.html). | Cloud architect |

### Set up AWS Systems Manager for a hybrid environment
<a name="set-up-aws-systems-manager-for-a-hybrid-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the attached scripts. | On your local machine, download the `ssm-trust-policy.json` and `ssm-activation.json` files that are in the *Attachments* section. | Cloud architect |
| Add the IAM role. | Add environment variables based on your business requirements.<pre>export AWS_DEFAULT_REGION=${AWS_REGION_ID}<br />export ROLE_NAME=${ECS_TASK_ROLE}<br />export CLUSTER_NAME=${ECS_CLUSTER_NAME}<br />export SERVICE_NAME=${ECS_CLUSTER_SERVICE_NAME}</pre><br />Run the following command.<pre>aws iam create-role --role-name $ROLE_NAME --assume-role-policy-document file://ssm-trust-policy.json</pre> | Cloud architect |
| Add the AmazonSSMManagedInstanceCore policy to the IAM role. | Run the following command.<pre>aws iam attach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore</pre> | Cloud architect |
| Add the AmazonEC2ContainerServiceforEC2Role policy to IAM role. | Run the following command.<pre>aws iam attach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role</pre> | Cloud architect |
| Verify the IAM role. | To verify the IAM role, run the following command.<pre>aws iam list-attached-role-policies --role-name $ROLE_NAME</pre> | Cloud architect |
| Activate Systems Manager. | Run the following command.<pre>aws ssm create-activation --iam-role $ROLE_NAME | tee ssm-activation.json</pre> | Cloud architect |

### Add WorkSpaces to the ECS cluster
<a name="add-workspaces-to-the-ecs-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Connect to your WorkSpaces. | To connect to and set up your Workspaces, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/workspaces/latest/userguide/workspaces-user-getting-started.html). | App developer |
| Download the ecs-anywhere install script. | At the command prompt, run the following command.<pre>curl -o "ecs-anywhere-install.sh" "https://amazon-ecs-agent-packages-preview.s3.us-east-1.amazonaws.com/ecs-anywhere-install.sh" && sudo chmod +x ecs-anywhere-install.sh</pre> | App developer |
| Check integrity of the shell script. | (Optional) Run the following command.<pre>curl -o "ecs-anywhere-install.sh.sha256" "https://amazon-ecs-agent-packages-preview.s3.us-east-1.amazonaws.com/ecs-anywhere-install.sh.sha256" && sha256sum -c ecs-anywhere-install.sh.sha256<br /><br /><br /></pre> | App developer |
| Add an EPEL repository on Amazon Linux. | To add an Extra Packages for Enterprise Linux (EPEL) repository, run the  command `sudo amazon-linux-extras install epel -y`. | App developer |
| Install Amazon ECS Anywhere. | To run the install script, use the following command.<pre>sudo ./ecs-anywhere-install.sh --cluster $CLUSTER_NAME --activation-id $ACTIVATION_ID --activation-code $ACTIVATION_CODE --region $AWS_REGION<br /><br /><br /></pre> |  |
| Check instance information from the ECS cluster. | To check the Systems Manager and ECS cluster instance information and validate that WorkSpaces were added on the cluster, run the following command from your local machine.<pre>aws ssm describe-instance-information" && "aws ecs list-container-instances --cluster $CLUSTER_NAME</pre> | App developer |

### Add an ECS task for the WorkSpaces
<a name="add-an-ecs-task-for-the-workspaces"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a task execution IAM role. | Download `task-execution-assume-role.json` and `external-task-definition.json` from the *Attachments* section. <br />On your local machine, run the following command.<pre>aws iam --region $AWS_DEFAULT_REGION create-role --role-name $ECS_TASK_EXECUTION_ROLE --assume-role-policy-document file://task-execution-assume-role.json</pre> | Cloud architect |
| Add the policy to the execution role. | Run the following command.<pre>aws iam --region $AWS_DEFAULT_REGION attach-role-policy --role-name $ECS_TASK_EXECUTION_ROLE --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy</pre> | Cloud architect |
| Create a task role. | Run the following command.<pre>aws iam --region $AWS_DEFAULT_REGION create-role --role-name $ECS_TASK_EXECUTION_ROLE --assume-role-policy-document file://task-execution-assume-role.json<br /><br /><br /></pre> | Cloud architect |
| Register the task definition to the cluster. | On your local machine, run the following command.<pre>aws ecs register-task-definition --cli-input-json file://external-task-definition.json</pre> | Cloud architect |
| Run the task. | On your local machine, run the following command.<pre>aws ecs run-task --cluster $CLUSTER_NAME --launch-type EXTERNAL --task-definition nginx</pre> | Cloud architect |
| Validate the task running state. | To fetch the task ID, run the following command.<pre>export TEST_TASKID=$(aws ecs list-tasks --cluster $CLUSTER_NAME | jq -r '.taskArns[0]')</pre><br />With the task ID, run the following command.<pre>aws ecs describe-tasks --cluster $CLUSTER_NAME --tasks ${TEST_TASKID}</pre> | Cloud architect |
| Verify the task on the WorkSpace. | To check that NGINX is running on the WorkSpace, run the command` curl http://localhost:8080`. | App developer |

## Related resources
<a name="run-amazon-ecs-tasks-on-amazon-workspaces-with-amazon-ecs-anywhere-resources"></a>
+ [ECS clusters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html)
+ [Setting up a hybrid environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html)
+ [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html)
+ [Simple AD](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspace-simple-ad.html)

## Attachments
<a name="attachments-da8b2249-3423-485c-9fef-6f902025e969"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/da8b2249-3423-485c-9fef-6f902025e969/attachments/attachment.zip)
