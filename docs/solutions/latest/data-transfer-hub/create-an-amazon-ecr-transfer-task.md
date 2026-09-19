---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/create-an-amazon-ecr-transfer-task.html
---

# Create an Amazon ECR transfer task
<a name="create-an-amazon-ecr-transfer-task"></a>

 The Guidance allows you to create an Amazon S3 transfer task in the following ways:
+  [using the web console](#using-the-web-console-1)
+  [using the ECR plugin](#using-the-ecr-plugin)
+  [using AWS CLI](#using-aws-cli-1)

You can make your choice according to your needs. For a comparison between those options, refer to [Create Amazon S3 transfer task](create-an-amazon-s3-transfer-task.md).

## Using the web console
<a name="using-the-web-console-1"></a>

 You can use the web console to create an Amazon ECR transfer task. For more information about how to launch the web console, see [Deploy the Guidance](deploy-the-solution.md#deployment-overview).

1.  From the **Create Transfer Task** page**,** select **Start a New Task**, and then select **Next**.

1.  From the **Engine options** page, under engine, select **Amazon ECR**, and then choose **Next Step**. You can also copy image from Docker Hub, GCR.io, Quay.io, and so on by choosing **Public Container Registry**.

1.  Specify the transfer task details. In **Source Type**, select the container warehouse type.

1.  In **Source settings**, enter **Source Region** and Amazon Web Services Account ID.

1.  To create credential information, select [Secrets Manager](https://console.aws.amazon.com/secretsmanager/home) to jump to the AWS Secrets Manager console in the current region.

   1.  From the left menu, select **Secrets**, then choose **Store a new secret** and select the **other type of secrets **key type.

   1.  Fill in the `access_key_id` and `secret_access_key` information in the Plaintext input box according to the displayed format. For more information, refer to IAM features in the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html). Choose **Next**.

   1.  (Optional) Enter the key name and description. Choose **Next**.

   1.  In the configuration of automatic rotation, select **Disable automatic rotation**. Choose **Next**.

   1.  Keep the default value and choose **Save** to complete the creation of the key.

   1.  Navigate back to the Data Transfer Hub task creation interface and refresh the interface. Your new secret is displayed in the drop-down list.

1.  Select the certificate (Secret).
**Note**
If the source is in the same account with Data Transfer Hub deployment, you need to create/provide credential info for the destination. Otherwise, no credential information is needed.

1.  Enter an email address in **Alarm Email**.

1.  Choose **Next** and review your task parameter details.

1.  Choose **Create Task**.

 After the task is created successfully, it will appear on the **Tasks** page.

## Using the ECR plugin
<a name="using-the-ecr-plugin"></a>

**Note**
This tutorial provides instructions for the backend-only version. For more details, please refer to [ECR Plugin Introduction](https://github.com/awslabs/data-transfer-hub/blob/main/docs/ECR_PLUGIN.md).

 **Step 1. Prepare VPC (optional)**

 This Guidance can be deployed in both public and private subnets. Using public subnets is recommended.
+  If you want to use existing VPC, please make sure the VPC has at least 2 subnets, and both subnets must have public internet access (either public subnets with internet gateway or private subnets with NAT gateway).
+  If you want to create new default VPC for this Guidance, please go to Step 2 and make sure you have **Create a new VPC for this cluster** selected when you create the cluster.

 **Step 2. Set up ECS Cluster**

 An ECS Cluster is required for this Guidance to run Fargate task.

1.  Sign in to AWS Management Console, and choose Elastic Container Service (ECS).

1.  From ECS Cluster home page, choose **Create Cluster**.

1.  Select Cluster Template. Choose **Network Only** type.

1.  Specify a cluster name and click Create to create a cluster. If you want to also create a new VPC (public subnets only), please also check the **Create a new VPC for this cluster** option.
![Configure cluster page with cluster name field and Create VPC checkbox highlighted.](https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/cluster.png)

 **Step 3. Configure credentials**

 If source (or destination) is NOT in current AWS account, you will need to provide AccessKeyID and SecretAccessKey (namely AK/SK) to pull from or push to Amazon ECR. And Secrets Manager is used to store the credentials in a secure manner.

 If source type is Public, there is no need to provide the source credentials.

1. Go to AWS Management Console > Secrets Manager.

1. From Secrets Manager home page, choose **Store a new secret**.

1. For secret type, select **Other type of secrets**.

1. For key/value paris, please copy and paste below JSON text into the **Plaintext** section, and change value to your AK/SK accordingly.

   ```
   {
     "access_key_id": "<Your Access Key ID>",
     "secret_access_key": "<Your Access Key Secret>"
   }
   ```
![Other type of secrets option selected with JSON format showing access key ID and secret key pairs.](https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/secret.png)

1. Choose **Next** to specify a secret name, and choose **Create**.

 **Step 4. Launch AWS Cloudformation Stack**

 Please follow below steps to deploy this plugin via AWS Cloudformation.

1.  Sign in to AWS Management Console, and switch to the Region where you want to deploy the CloudFormation Stack.

1.  Choose the following to launch the CloudFormation Stack in that Region.
   +  For AWS China Regions

      [![Blue rectangular button labeled "Launch Stack" with a play icon.](https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/launch-stack.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/create/template?stackName=DTHECRStack&templateURL=https://solutions-reference.s3.amazonaws.com/data-transfer-hub/latest/DataTransferECRStack.template)
   +  For AWS Global Regions

      [![Blue rectangular button labeled "Launch Stack" with a play icon.](https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/template?stackName=DTHECRStack&templateURL=https://solutions-reference.s3.amazonaws.com/data-transfer-hub/latest/DataTransferECRStack.template)

1.  Choose **Next**. Specify values to parameters accordingly. Change the stack name if required.

1.  Choose **Next**. Configure additional stack options such as tags if needed.

1.  Choose **Next**. Review and confirm acknowledgement, and then choose **Create Stack** to start the deployment.

 The deployment will take approximately 3 to 5 minutes.

## Using AWS CLI
<a name="using-aws-cli-1"></a>

 You can use the [*AWS CLI*](https://aws.amazon.com/cli/) to create an Amazon ECR transfer task. Note that if you have deployed the Datat Transfer Hub Portal at the same time, the tasks started through the CLI will not appear in the Task List on your Portal.

1.  Create an Amazon VPC with two public subnets or two private subnets with [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html).

1.  Replace <CLOUDFORMATION\_URL> as shown below.

   ```
   https://solutions-reference.s3.amazonaws.com/data-transfer-hub/latest/DataTransferECRStack.template
   ```

1.  Go to your terminal and enter the following command. For the parameter details, refer to the Parameters table.

   ```
   aws cloudformation create-stack --stack-name dth-ecr-task --template-url CLOUDFORMATION_URL \
   --capabilities CAPABILITY_NAMED_IAM \
   --parameters \
   ParameterKey=sourceType,ParameterValue=Amazon_ECR \
   ParameterKey=srcRegion,ParameterValue=us-east-1 \
   ParameterKey=srcAccountId,ParameterValue=123456789012 \
   ParameterKey=srcList,ParameterValue=ALL \
   ParameterKey=includeUntagged,ParameterValue=false \
   ParameterKey=srcImageList,ParameterValue= \
   ParameterKey=srcCredential,ParameterValue=dev-us-credential \
   ParameterKey=destAccountId,ParameterValue= \
   ParameterKey=destRegion,ParameterValue=us-west-2 \
   ParameterKey=destCredential,ParameterValue= \
   ParameterKey=destPrefix,ParameterValue= \
   ParameterKey=alarmEmail,ParameterValue=your_email@example.com \
   ParameterKey=ecsVpcId,ParameterValue=vpc-07f56e8e21630a2a0 \
   ParameterKey=ecsClusterName,ParameterValue=dth-v22-01-TaskCluster-eHzKkHatj0tN \
   ParameterKey=ecsSubnetA,ParameterValue=subnet-034c58fe0e696eb0b \
   ParameterKey=ecsSubnetB,ParameterValue=subnet-0487ae5a1d3badde7
   ```

<table>
<thead>
  <tr><th> Parameter </th><th> Allowed Value </th><th> Default Value </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> sourceType </td><td>Amazon_ECR<br />Public</td><td> Amazon_ECR </td><td> Choose type of source container registry, for example Amazon_ECR, or Public from Docker Hub, gco.io, etc. </td></tr>
  <tr><td> srcRegion </td><td> </td><td> </td><td> Source Region Name (only required if source type is Amazon ECR), for example, us-west-1 </td></tr>
  <tr><td> srcAccountId </td><td> </td><td> </td><td> Source AWS Account ID (only required if source type is Amazon ECR), leave it blank if source is in current account </td></tr>
  <tr><td> srcList </td><td>ALL<br />SELECTED</td><td> ALL </td><td> Type of Source Image List, either ALL or SELECTED, for public registry, please use SELECTED only </td></tr>
  <tr><td> srcImageList </td><td> </td><td> </td><td> Selected Image List delimited by comma, for example, ubuntu:latest,alpine:latest..., leave it blank if Type is ALL. For ECR source, using ALL_TAGS tag to get all tags. </td></tr>
  <tr><td> srcCredential </td><td> </td><td> </td><td> The secret name in Secrets Manager only when using AK/SK credentials to pull images from source Amazon ECR, leave it blank for public registry </td></tr>
  <tr><td> destRegion </td><td> </td><td> </td><td> Destination Region Name, for example, cn-north-1 </td></tr>
  <tr><td> destAccountId </td><td> </td><td> </td><td> Destination AWS Account ID, leave it blank if destination is in current account </td></tr>
  <tr><td> destPrefix </td><td> </td><td> </td><td> Destination Repo Prefix </td></tr>
  <tr><td> destCredential </td><td> </td><td> </td><td> The secret name in Secrets Manager only when using AK/SK credentials to push images to destination Amazon ECR </td></tr>
  <tr><td> includeUntagged </td><td>true<br />false</td><td> true </td><td> Whether to include untagged images in the replication </td></tr>
  <tr><td> ecsClusterName </td><td> </td><td> </td><td> ECS Cluster Name to run ECS task (Please make sure the cluster exists) </td></tr>
  <tr><td> ecsVpcId </td><td> </td><td> </td><td> VPC ID to run ECS task, e.g. vpc-bef13dc7 </td></tr>
  <tr><td> ecsSubnetA </td><td> </td><td> </td><td> First Subnet ID to run ECS task, e.g. subnet-97bfc4cd </td></tr>
  <tr><td> ecsSubnetB </td><td> </td><td> </td><td> Second Subnet ID to run ECS task, e.g. subnet-7ad7de32 </td></tr>
  <tr><td> alarmEmail </td><td> </td><td> </td><td> Alarm Email address to receive notification in case of any failure </td></tr>
  <tr><td> sourceType </td><td>Amazon_ECR<br />Public</td><td> Amazon_ECR </td><td> Choose type of source container registry, for example Amazon_ECR, or Public from Docker Hub, gco.io, etc. </td></tr>
  <tr><td> srcRegion </td><td> </td><td> </td><td> Source Region Name (only required if source type is Amazon ECR), for example, us-west-1 </td></tr>
  <tr><td> srcAccountId </td><td> </td><td> </td><td> Source AWS Account ID (only required if source type is Amazon ECR), leave it blank if source is in current account </td></tr>
  <tr><td> srcList </td><td> ALL SELECTED </td><td> ALL </td><td> Type of Source Image List, either ALL or SELECTED, for public registry, please use SELECTED only </td></tr>
  <tr><td> srcImageList </td><td> </td><td> </td><td> Selected Image List delimited by comma, for example, ubuntu:latest,alpine:latest..., leave it blank if Type is ALL. For ECR source, using ALL_TAGS tag to get all tags. </td></tr>
  <tr><td> srcCredential </td><td> </td><td> </td><td> The secret name in Secrets Manager only when using AK/SK credentials to pull images from source Amazon ECR, leave it blank for public registry </td></tr>
  <tr><td> destRegion </td><td> </td><td> </td><td> Destination Region Name, for example, cn-north-1 </td></tr>
  <tr><td> destAccountId </td><td> </td><td> </td><td> Destination AWS Account ID, leave it blank if destination is in current account </td></tr>
  <tr><td> destPrefix </td><td> </td><td> </td><td> Destination Repo Prefix </td></tr>
  <tr><td> destCredential </td><td> </td><td> </td><td> The secret name in Secrets Manager only when using AK/SK credentials to push images to destination Amazon ECR </td></tr>
  <tr><td> includeUntagged </td><td>true<br />false</td><td> true </td><td> Whether to include untagged images in the replication </td></tr>
  <tr><td> ecsClusterName </td><td> </td><td> </td><td> ECS Cluster Name to run ECS task (Please make sure the cluster exists) </td></tr>
  <tr><td> ecsVpcId </td><td> </td><td> </td><td> VPC ID to run ECS task, e.g. vpc-bef13dc7 </td></tr>
  <tr><td> ecsSubnetA </td><td> </td><td> </td><td> First Subnet ID to run ECS task, e.g. subnet-97bfc4cd </td></tr>
  <tr><td> ecsSubnetB </td><td> </td><td> </td><td> Second Subnet ID to run ECS task, e.g. subnet-7ad7de32 </td></tr>
  <tr><td> alarmEmail </td><td> </td><td> </td><td> Alarm Email address to receive notification in case of any failure </td></tr>
</tbody>
</table>
