---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-uipath-rpa-bots-automatically-on-amazon-ec2-by-using-aws-cloudformation.html
---

# Set up UiPath RPA bots automatically on Amazon EC2 by using AWS CloudFormation
<a name="set-up-uipath-rpa-bots-automatically-on-amazon-ec2-by-using-aws-cloudformation"></a>

*Dr. Rahul Sharad Gaikwad and Tamilselvan P, Amazon Web Services*

## Summary
<a name="set-up-uipath-rpa-bots-automatically-on-amazon-ec2-by-using-aws-cloudformation-summary"></a>

This pattern explains how you can deploy robotic process automation (RPA) bots on Amazon Elastic Compute Cloud (Amazon EC2) instances. It uses an [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) pipeline to create a custom Amazon Machine Image (AMI). An AMI is a preconfigured virtual machine (VM) image that contains the operating system (OS) and preinstalled software to deploy EC2 instances. This pattern uses AWS CloudFormation templates to install [UiPath Studio Community edition](https://www.uipath.com/product/studio) on the custom AMI. UiPath is an RPA tool that helps you set up robots to automate your tasks.

As part of this solution, EC2 Windows instances are launched by using the base AMI, and the UiPath Studio application is installed on the instances. The pattern uses the Microsoft System Preparation (Sysprep) tool to duplicate the customized Windows installation. After that, it removes the host information and creates a final AMI from the instance. You can then launch the instances on demand by using the final AMI with your own naming conventions and monitoring setup.

|
|
| Note: This pattern doesn’t provide any information about using RPA bots. For that information, see the [UiPath documentation](https://docs.uipath.com/). You can also use this pattern to set up other RPA bot applications by customizing the installation steps based on your requirements. |
| --- |

This pattern provides the following automations and benefits:
+ Application deployment and sharing: You can build Amazon EC2 AMIs for application deployment and share them across multiple accounts through an EC2 Image Builder pipeline, which uses AWS CloudFormation templates as infrastructure as code (IaC) scripts.
+ Amazon EC2 provisioning and scaling: CloudFormation IaC templates provide custom computer name sequences and Active Directory join automation.
+ Observability and monitoring: The pattern sets up Amazon CloudWatch dashboards to help you monitor Amazon EC2 metrics (such as CPU and disk usage).
+ RPA benefits for your business: RPA improves accuracy because robots can perform assigned tasks automatically and consistently. RPA also increases speed and productivity because it removes operations that don’t add value and handles repetitious activities.

## Prerequisites and limitations
<a name="set-up-uipath-rpa-bots-automatically-on-amazon-ec2-by-using-aws-cloudformation-prereqs"></a>

**Prerequisites **
+ An active[ AWS account](https://aws.amazon.com/free/)
+ [AWS Identity and Access Management (IAM) permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) for deploying CloudFormation templates
+ [IAM policies](https://docs.aws.amazon.com/imagebuilder/latest/userguide/cross-account-dist.html) to set up cross-account AMI distribution with EC2 Image Builder

## Architecture
<a name="set-up-uipath-rpa-bots-automatically-on-amazon-ec2-by-using-aws-cloudformation-architecture"></a>

![Target architecture for setting up RPA bots on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5555a62d-91d4-4e81-9961-ff89faedd6ad/images/1893d2d3-8912-4473-adf1-6633b5badcd9.png)

1. The administrator provides the base Windows AMI in the `ec2-image-builder.yaml` file and deploys the stack in the CloudFormation console.

1. The CloudFormation stack deploys the EC2 Image Builder pipeline, which includes the following resources:
   + `Ec2ImageInfraConfiguration`
   + `Ec2ImageComponent`
   + `Ec2ImageRecipe`
   + `Ec2AMI`

1. The EC2 Image Builder pipeline launches a temporary Windows EC2 instance by using the base AMI and installs the required components (in this case, UiPath Studio).

1. The EC2 Image Builder removes all the host information and creates an AMI from Windows Server.

1. You update the `ec2-provisioning yaml` file with the custom AMI and launch a number of EC2 instances based on your requirements.

1. You deploy the Count macro by using a CloudFormation template. This macro provides a **Count** property for CloudFormation resources so you can specify multiple resources of the same type easily.

1. You update the name of the macro in the CloudFormation `ec2-provisioning.yaml` file and deploy the stack.

1. The administrator updates the `ec2-provisioning.yaml` file based on requirements and launches the stack.

1. The template deploys EC2 instances with the UiPath Studio application.

## Tools
<a name="set-up-uipath-rpa-bots-automatically-on-amazon-ec2-by-using-aws-cloudformation-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/) helps you model and manage infrastructure resources in an automated and secure manner.
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) helps you observe and monitor resources and applications on AWS, on premises, and on other clouds.
+ [Amazon Elastic Compute Cloud (Amazon EC2](https://aws.amazon.com/ec2/)) provides secure and resizable compute capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [EC2 Image Builder](https://aws.amazon.com/image-builder/) simplifies the building, testing, and deployment of virtual machines and container images for use on AWS or on premises.
+ [Amazon EventBridge](https://aws.amazon.com/eventbridge/) helps you build event-driven applications at scale across AWS, existing systems, or software as a service (SaaS) applications.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.
+ [AWS Lambda](https://aws.amazon.com/lambda/) is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. You can call Lambda functions from over 200 AWS services and SaaS applications, and pay only for what you use.
+ [Amazon Simple Storage Service (Amazon S3) ](https://aws.amazon.com/s3/)is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data..
+ [AWS Systems Manager Agent (SSM Agent)](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) helps Systems Manager update, manage, and configure EC2 instances, edge devices, on-premises servers, and virtual machines (VMs).

**Code repositories**

The code for this pattern is available in the GitHub [UiPath RPA bot setup using CloudFormation](https://github.com/aws-samples/uipath-rpa-setup-ec2-windows-ami-cloudformation) repository. The pattern also uses a macro that’s available from the [AWS CloudFormation Macros repository](https://github.com/aws-cloudformation/aws-cloudformation-macros/tree/master/Count).

## Best practices
<a name="set-up-uipath-rpa-bots-automatically-on-amazon-ec2-by-using-aws-cloudformation-best-practices"></a>
+ AWS releases new [Windows AMIs](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/windows-ami-version-history.html) each month. These contain the latest OS patches, drivers, and launch agents. We recommend that you use the latest AMI when you launch new instances or when you build your own custom images.
+ Apply all available Windows or Linux security patches during image builds.

## Epics
<a name="set-up-uipath-rpa-bots-automatically-on-amazon-ec2-by-using-aws-cloudformation-epics"></a>

### Deploy an image pipeline for the base image
<a name="deploy-an-image-pipeline-for-the-base-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up an EC2 Image Builder pipeline. | 1. Clone the [UiPath RPA bot setup using CloudFormation](https://github.com/aws-samples/uipath-rpa-setup-ec2-windows-ami-cloudformation) repository, or download the `ec2-image-builder.yaml` template from the repository.<br />2. Sign in to the AWS Management Console, and open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />3. Choose **Create stack**.<br />4. In the **Specify template** section, choose **Upload a template file**.<br />5. Locate and upload the `ec2-image-builder.yaml` template from your computer, and then choose **Next**.<br />6. Provide input parameters for your stack or accept the default values. Choose **Next**.The number and values of parameters might vary depending on your input values.<br />7. Optionally, configure stack options, and then choose **Next**.<br />8. Review your stack details.<br />9. At the end of the screen, select the check box to acknowledge capabilities, and then choose **Submit**.<br />10. Monitor the stack’s progress. When the status is `CREATE_COMPLETE`, the deployment is ready. | AWS DevOps |
| View EC2 Image Builder settings. | The EC2 Image Builder settings include infrastructure configuration, distribution settings, and security scanning settings. To view the settings:1. Open the [EC2 Image Builder console](https://console.aws.amazon.com/imagebuilder/).<br />2. From the navigation pane, navigate to various Image Builder settings.As a best practice, you should make any updates to EC2 Image Builder through the CloudFormation template only. | AWS DevOps |
| View the image pipeline. | To view the deployed image pipeline:1. On the EC2 Image Builder console, choose **Image pipelines** from the navigation pane.<br />2. Select the image pipeline you created.<br />3. View the configuration details of the output images, image recipe, infrastructure configuration, distribution settings, Amazon EventBridge rules, and tags. | AWS DevOps |
| View Image Builder logs. | EC2 Image Builder logs are aggregated in CloudWatch log groups. To view the logs in CloudWatch:1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).<br />2. In the navigation pane, choose **Logs**, **Log groups**.<br />3. Choose the log group name. EC2 Image Builder logs are aggregated in the log group `/aws/imagebuilder/XXX`.<br />4. Check the latest logs in the respective log stream for any errors encountered when running the image pipeline.<br />EC2 Image Builder logs are also stored in an S3 bucket. To view the logs in the bucket:1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/).<br />2. In the **Buckets** list, choose the bucket name. The logs are aggregated in the S3 bucket `<stack-name>-XXXXXX`. | AWS DevOps |
| Upload the UiPath file to an S3 bucket. | 1. Download the `.msi` file for UiPath Studio from the location [https://download.uipath.com/UiPathStudioCommunity.msi](https://download.uipath.com/UiPathStudioCommunity.msi).<br />2. Upload the file to an S3 bucket.<br />3. Update the bucket name and file key in the `ec2-image-builder.yaml` template, in the user data section, [line number 310](https://github.com/aws-samples/uipath-rpa-setup-ec2-windows-ami-cloudformation/blob/main/ec2-image-builder.yaml#L310). | AWS DevOps |

### Deploy and test the Count macro
<a name="deploy-and-test-the-count-macro"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the Count macro. | 1. Clone or download the [Count CloudFormation macro](https://github.com/aws-cloudformation/aws-cloudformation-macros).<br />2. Navigate to the `Count` folder.<br />3. You will need an S3 bucket to store the CloudFormation artifacts. If you don't have an S3 bucket already, create one with the name `aws s3 mb s3://<bucket name>`.<br />4. Package the Count macro template. The template uses the [AWS Serverless Application Model (SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html), so it must be transformed before you can deploy it.<pre>aws cloudformation package \<br />    --template-file template.yaml \<br />    --s3-bucket <your bucket name here> \<br />    --output-template-file packaged.yaml </pre><br />For example:<pre>aws cloudformation package \<br />    --template-file template.yaml \<br />    --s3-bucket count-macro-ec2 \<br />    --output-template-file packaged.yaml</pre><br />5. Deploy the packaged template to create a CloudFormation stack.<pre>aws cloudformation deploy \<br />    --stack-name Count-macro \<br />    --template-file packaged.yaml \<br />    --capabilities CAPABILITY_IAM </pre>If you want to use the console, follow the instructions in the previous epic or in the [CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html).  | DevOps engineer |
| Test the Count macro. | To test the macro's capabilities, try launching the example template that’s provided with the macro. <pre>aws cloudformation deploy \<br />    --stack-name Count-test \<br />    --template-file test.yaml \<br />    --capabilities CAPABILITY_IAM</pre> | DevOps engineer |

### Deploy the CloudFormation stack to provision instances with the custom image
<a name="deploy-the-cloudformation-stack-to-provision-instances-with-the-custom-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the Amazon EC2 provisioning template. | To deploy EC2 Image Pipeline by using CloudFormation:1. Download the `ec2-provisioning.yaml` template from the [GitHub repository](https://github.com/aws-samples/uipath-rpa-setup-ec2-windows-ami-cloudformation), or locate it on your computer if you cloned the repository.<br />2. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />3. Repeat the steps from the first epic (or follow the instructions in the [CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html)) to deploy `ec2-provisioning.yaml`. | AWS DevOps |
| View Amazon EC2 settings. | Amazon EC2 settings include security, networking, storage, status checks, monitoring, and tags configurations. To view these configurations:1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/).<br />2. In the navigation pane, choose **Instances**, and then select the EC2 instance that was created by the Amazon EC2 provisioning template.<br />3. In the instance summary, select the tabs to view the corresponding Amazon EC2 settings. | AWS DevOps |
| View the CloudWatch dashboard. | 1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).<br />2. In the navigation pane, choose **Dashboards**.<br />3. Choose the dashboard that has your stack name.After you provision the stack, it takes time to populate the dashboard with metrics.The dashboard provides these metrics: `CPUUtilization`, `DiskUtilization`, `MemoryUtilization`, `NetworkIn`, `NetworkOut`, `StatusCheckFailed`. | AWS DevOps |
| View custom metrics for memory and disk usage.  | 1. On the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/), choose **Dashboards**.<br />2. In the navigation pane, choose **Metrics**, **All metrics**.<br />3. Choose **Custom namespaces**, **CWAgent**. | AWS DevOps |
| View alarms for memory and disk usage.  | 1. On the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/), in the navigation pane, choose **Dashboards**.<br />2. Choose **All alarms**. | AWS DevOps |
| Verify the snapshot lifecyle rule. | 1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/).<br />2. In the navigation pane, choose **Lifecycle Manager**.<br />3. Verify the settings for the AMI lifecycle. | AWS DevOps |

### Delete the environment (optional)
<a name="delete-the-environment-optional"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the stacks. | When your PoC or pilot project is complete, we recommend that you delete the stacks you created to make sure that you aren’t charged for these resources.1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/). <br />2. In the navigation pane, choose **Stacks**, and then select one or both stacks you created earlier that you want to delete. The stack must be currently running.<br />3. In the stack details pane, choose **Delete**.<br />4. When prompted, choose **Delete stack**.The stack deletion operation can't be stopped after it begins. The stack proceeds to the `DELETE_IN_PROGRESS` state.<br />If the deletion fails, the stack will be in the `DELETE_FAILED` state. For solutions, see [Delete stack fails](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-delete-stack-fails) in the AWS CloudFormation troubleshooting documentation.<br />For information about protecting stacks from being accidentally deleted, see [Protecting a stack from being deleted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html) in the AWS CloudFormation documentation. | AWS DevOps |

## Troubleshooting
<a name="set-up-uipath-rpa-bots-automatically-on-amazon-ec2-by-using-aws-cloudformation-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| When you deploy the Amazon EC2 provisioning template, you get the error: *Received malformed response from transform 123xxxx::Count*. | This is a known issue. (See the custom solution and PR in the [AWS CloudFormation macros repository](https://github.com/aws-cloudformation/aws-cloudformation-macros/pull/20).)<br />To fix this issue, open the AWS Lambda console and update `index.py` with the content from the [GitHub repository](https://raw.githubusercontent.com/aws-cloudformation/aws-cloudformation-macros/f1629c96477dcd87278814d4063c37877602c0c8/Count/src/index.py).  |

## Related resources
<a name="set-up-uipath-rpa-bots-automatically-on-amazon-ec2-by-using-aws-cloudformation-resources"></a>

**GitHub repositories**
+ [UiPath RPA bot setup using CloudFormation](https://github.com/aws-samples/uipath-rpa-setup-ec2-windows-ami-cloudformation)
+ [Count CloudFormation Macro](https://github.com/aws-cloudformation/aws-cloudformation-macros/tree/master/Count)

**AWS references**
+ [Creating a stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) (CloudFormation documentation)
+ [Troubleshooting CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html) (CloudFormation documentation)
+ [Monitor memory and disk metrics forAmazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html) (Amazon EC2 documentation)
+ [How can I use the CloudWatch agent to view metrics for Performance Monitor on a Windows server?](https://repost.aws/knowledge-center/cloudwatch-performance-monitor-windows) (AWS re:Post article)

**Additional references**
+ [UiPath documentation](https://docs.uipath.com/)
+ [Setting the Hostname in a SysPreped AMI](https://blog.brianbeach.com/2014/07/setting-hostname-in-syspreped-ami.html) (blog post by Brian Beach)
+ [How do I make Cloudformation reprocess a template using a macro when parameters change?](https://stackoverflow.com/questions/59828989/how-do-i-make-cloudformation-reprocess-a-template-using-a-macro-when-parameters) (Stack Overflow)
