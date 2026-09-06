---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect.html
---

# Access a bastion host by using Session Manager and Amazon EC2 Instance Connect
<a name="access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect"></a>

*Piotr Chotkowski and Witold Kowalik, Amazon Web Services*

## Summary
<a name="access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-summary"></a>

A *bastion host*, sometimes called a *jump box*, is a server that provides a single point of access from an external network to the resources located in a private network. A server exposed to an external public network, such as the internet, poses a potential security risk for unauthorized access. It’s important to secure and control access to these servers.

This pattern describes how you can use [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) and [Amazon EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html) to securely connect to an Amazon Elastic Compute Cloud (Amazon EC2) bastion host deployed in your AWS account. Session Manager is a capability of AWS Systems Manager. The benefits of this pattern include:
+ The deployed bastion host doesn’t have any open, inbound ports exposed to the public internet. This reduces the potential attack surface.
+ You don’t need to store and maintain long-term Secure Shell (SSH) keys in your AWS account. Instead, each user generates a new SSH key pair each time they connect to the bastion host. AWS Identity and Access Management (IAM) policies that are attached to the user’s AWS credentials control access to the bastion host.

**Intended audience**

This pattern is intended for readers who have experience with basic understanding of Amazon EC2, Amazon Virtual Private Cloud (Amazon VPC), and Hashicorp Terraform.

## Prerequisites and limitations
<a name="access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ AWS Command Line Interface (AWS CLI) version 2, [installed](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
+ Session Manager plugin for the AWS CLI, [installed](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html)
+ Terraform CLI, [installed](https://developer.hashicorp.com/terraform/cli)
+ Storage for the Terraform [state](https://developer.hashicorp.com/terraform/language/state), such as an Amazon Simple Storage Service (Amazon S3) bucket and an Amazon DynamoDB table that serve as a remote backend to store the Terraform state. For more information on using remote backends for the Terraform state, see [Amazon S3 Backends](https://www.terraform.io/language/settings/backends/s3) (Terraform documentation). For a code sample that sets up remote state management with an Amazon S3 backend, see [remote-state-s3-backend](https://registry.terraform.io/modules/nozaq/remote-state-s3-backend/aws/latest) (Terraform Registry). Note the following requirements:
  + The Amazon S3 bucket and DynamoDB table must be in the same AWS Region.
  + When creating the DynamoDB table, the partition key must be `LockID` (case-sensitive), and the partition key type must be `String`. All other table settings must be at their default values. For more information, see [About primary keys](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey) and [Create a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html) in the DynamoDB documentation.
+ An SSH client, installed

**Limitations**
+ This pattern is intended as a proof of concept (PoC) or as a basis for further development. It should not be used in its current form in production environments. Before deployment, adjust the sample code in the repository to meet your requirements and use case.
+ This pattern assumes that the target bastion host uses Amazon Linux 2 as its operating system. While it is possible to use other Amazon Machine Images (AMIs), other operating systems are out of scope for this pattern.
**Note**
Amazon Linux 2 is nearing end of support. For more information, see the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/).
+ In this pattern, the bastion host is located in a private subnet without an NAT gateway and internet gateway. This design isolates the Amazon EC2 instance from the public internet. You can add a specific network configuration that allows it to communicate with the internet. For more information, see [Connect your virtual private cloud (VPC) to other networks](https://docs.aws.amazon.com/vpc/latest/userguide/extend-intro.html) in the Amazon VPC documentation. Similarly, following the [principle of least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege), the bastion host doesn’t have access to any other resources in your AWS account unless you explicitly grant permissions. For more information, see [Resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based) in the IAM documentation.

**Product versions**
+ AWS CLI version 2
+ Terraform version 1.3.9

## Architecture
<a name="access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-architecture"></a>

**Target technology stack**
+ A VPC with a single private subnet
+ The following [interface VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html):
  + `amazonaws.<region>.ssm` – The endpoint for the AWS Systems Manager service.
  + `amazonaws.<region>.ec2messages` – Systems Manager uses this endpoint to make calls from SSM Agent to the Systems Manager service.
  + `amazonaws.<region>.ssmmessages` – Session Manager uses this endpoint to connect to your Amazon EC2 instance through a secure data channel.
+ A `t3.nano` Amazon EC2 instance running Amazon Linux 2
+ IAM role and instance profile
+ Amazon VPC security groups and security group rules for the endpoints and Amazon EC2 instance

**Target architecture**

![Architecture diagram of using Session Manager to access a bastion host.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a02aed20-1852-4c91-902f-f553795006e2/images/819c503b-7eec-4a9c-862b-b87107d50dc1.png)

The diagram shows the following process:

1. The user assumes an IAM role that has permissions to do the following:
   + Authenticate, authorize, and connect to the Amazon EC2 instance
   + Start a session with Session Manager

1. The user initiates an SSH session through Session Manager.

1. Session Manager authenticates the user, verifies the permissions in the associated IAM policies, checks the configuration settings, and sends a message to SSM Agent to open a two-way connection.

1. The user pushes the SSH public key to the bastion host through Amazon EC2 metadata. This must be done before each connection. The SSH public key remains available for 60 seconds.

1. The bastion host communicates with the interface VPC endpoints for Systems Manager and Amazon EC2.

1. The user accesses the bastion host through Session Manager by using a TLS 1.2 encrypted bidirectional communication channel.

**Automation and scale**

The following options are available to automate deployment or to scale this architecture:
+ You can deploy the architecture through a continuous integration and continuous delivery (CI/CD) pipeline.
+ You can modify the code to change the instance type of the bastion host.
+ You can modify the code to deploy multiple bastion hosts. In the `bastion-host/main.tf` file, in the `aws_instance` resource block, add the `count` meta-argument. For more information, see the [Terraform documentation](https://developer.hashicorp.com/terraform/language/meta-arguments/count).

## Tools
<a name="access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale. This pattern uses [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html), a capability of Systems Manager.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Other tools**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources. This pattern uses [Terraform CLI](https://developer.hashicorp.com/terraform/cli).

**Code repository**

The code for this pattern is available in the GitHub [Access a bastion host by using Session Manager and Amazon EC2 Instance Connect](https://github.com/aws-samples/secured-bastion-host-terraform) repository.

## Best practices
<a name="access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-best-practices"></a>
+ We recommend using automated code-scanning tools to improve the security and quality of the code. This pattern was scanned by using [Checkov](https://www.checkov.io/), a static code-analysis tool for IaC. At a minimum, we recommend that you perform basic validation and formatting checks by using the `terraform validate` and `terraform fmt -check -recursive` Terraform commands.
+ It’s a good practice to add automated tests for IaC. For more information about the different approaches for testing Terraform code, see [Testing HashiCorp Terraform](https://www.hashicorp.com/blog/testing-hashicorp-terraform) (Terraform blog post).
+ During deployment, Terraform uses the replaces the Amazon EC2 instance each time a new version of the [Amazon Linux 2 AMI](https://aws.amazon.com/marketplace/pp/prodview-zc4x2k7vt6rpu?sr=0-1&ref_=beagle&applicationId=AWSMPContessa) is detected. This deploys the new version of the operating system, including patches and upgrades. If the deployment schedule is infrequent, this can pose a security risk because the instance doesn’t have the latest patches. It is important to frequently update and apply security patches to deployed Amazon EC2 instances. For more information, see [Update management in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/update-management.html).
+ Because this pattern is a proof of concept, it uses AWS managed policies, such as `AmazonSSMManagedInstanceCore`. AWS managed policies cover common use cases but don't grant least-privilege permissions. As needed for your use case, we recommend that you create custom policies that grant least-privilege permissions for the resources deployed in this architecture. For more information, see [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies).
+ Use a password to protect access to SSH keys and store keys in a secure location.
+ Set up logging and monitoring for the bastion host. Logging and monitoring are important parts of maintaining systems, from both an operational and security perspective. There are multiple ways to monitor connections and activity in your bastion host. For more information, see the following topics in the Systems Manager documentation:
  + [Monitoring AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring.html)
  + [Logging and monitoring in AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/logging-and-monitoring.html)
  + [Auditing session activity](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-auditing.html)
  + [Logging session activity](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging.html)

## Epics
<a name="access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-epics"></a>

### Deploy the resources
<a name="deploy-the-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the code repository. | 1. In a command-line interface, change your working directory to the location where you want to store the sample files.<br />2. Enter the following command.<br />`git clone https://github.com/aws-samples/secured-bastion-host-terraform.git` | DevOps engineer, Developer |
| Initialize the Terraform working directory. | This step is necessary for only the first deployment. If you are redeploying the pattern, skip to the next step.<br />In the root directory of the cloned repository, enter the following command, where:+ `$S3_STATE_BUCKET` is the name of Amazon S3 bucket that contains the Terraform state<br />+ `$PATH_TO_STATE_FILE` is the key to the Terraform state file, such as `infra/bastion-host/tetfstate`<br />+ `$AWS_REGION` is the Region where the Amazon S3 bucket is deployed<pre>terraform init \<br />    -backend-config="bucket=$S3_STATE_BUCKET" \<br />    -backend-config="key=$PATH_TO_STATE_FILE" \<br />    -backend-config="region=$AWS_REGION</pre>Alternatively, you can open the **config.tf** file and, in the `terraform` section, manually provide these values. | DevOps engineer, Developer, Terraform |
| Deploy the resources. | 1. In the root directory of the cloned repository, enter the following command.<pre>terraform apply -var-file="dev.tfvars"</pre><br />2. Review the list of all changes that will be applied to your AWS account, and then confirm the deployment.<br />3. Wait until all resources are deployed. | DevOps engineer, Developer, Terraform |

### Set up the local environment
<a name="set-up-the-local-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the SSH connection. | Update the SSH configuration file to allow SSH connections through Session Manager. For instructions, see [Allowing SSH connections for Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-enable-ssh-connections.html#ssh-connections-enable). This allows authorized users to enter a proxy command that starts a Session Manager session and transfers all data through a two-way connection. | DevOps engineer |
| Generate the SSH keys. | Enter the following command to generate a local private and public SSH key pair. You use this key pair to connect to the bastion host.<pre>ssh-keygen -t rsa -f my_key</pre> | DevOps engineer, Developer |

### Connect to the bastion host by using Session Manager
<a name="connect-to-the-bastion-host-by-using-sesh"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Get the instance ID. | 1. In order to connect to the deployed bastion host, you need the ID of the Amazon EC2 instance. Do one of the following to locate the ID:Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/). In the navigation pane, choose **Instances**. Locate the bastion host instance.In the AWS CLI, enter the following command.<pre>aws ec2 describe-instances</pre><br />To filter the results, enter the following command, where `$BASTION_HOST_TAG` is the tag you assigned to the bastion host. The default value for this tag is `sandbox-dev-bastion-host`.<pre>aws ec2 describe-instances \<br />    --filters "Name=tag:Name,Values=$BASTION_HOST_TAG" \<br />    --output text \<br />    --query 'Reservations[*].Instances[*].InstanceId' \<br />    --output text</pre><br />2. Copy the ID of the Amazon EC2 instance. You use this ID later. | General AWS |
| Send the SSH public key. | In this section, you upload the public key to the [instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) of the bastion host. After the key is uploaded, you have 60 seconds to start a connection with the bastion host. After 60 seconds, the public key is removed. For more information, see the [Troubleshooting](#access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-troubleshooting) section of this pattern. Complete the next steps quickly to prevent the key from being removed before you connect to the bastion host.1. Send the SSH key to the bastion host by using Amazon EC2 Instance Connect. Enter the following command, where:`$INSTANCE_ID` is the ID of the Amazon EC2 instance`$PUBLIC_KEY_FILE` is the path to your public key file, such as `my_key.pub`Be sure to use the public key and not the private key.<pre>aws ec2-instance-connect send-ssh-public-key \<br />    --instance-id $INSTANCE_ID \<br />    --instance-os-user ec2-user \<br />    --ssh-public-key file://$PUBLIC_KEY_FILE</pre><br />2. Wait until you receive a message indicating that the key has been successfully uploaded. Continue to the next step immediately. | General AWS |
| Connect to the bastion host. | 1. Enter the following command to connect to the bastion host through Session Manager, where:`$PRIVATE_KEY_FILE` is the path to your private key, such as `my_key``$INSTANCE_ID` is the ID of the Amazon EC2 instance<pre>ssh -i $PRIVATE_KEY_FILE ec2-user@$INSTANCE_ID</pre><br />2. Confirm the connection by entering `yes`. This opens an SSH connection by using Session Manager.There are other options for opening an SSH connection with the bastion host. For more information, see *Alternative approaches to establish an SSH connection with the bastion host* in the [Additional information](#access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-additional) section of this pattern. | General AWS |

### (Optional) Clean up
<a name="optional-clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove the deployed resources. | 1. In order to remove all deployed resources, run the following command from the root directory of the cloned repository.<pre>terraform destroy -var-file="dev.tfvars"</pre><br />2. Confirm the removal of the resources. | DevOps engineer, Developer, Terraform |

## Troubleshooting
<a name="access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `TargetNotConnected` error when trying to connect to the bastion host | 1. Reboot the bastion host according to the instructions in [Reboot your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-reboot.html) in the Amazon EC2 documentation.<br />2. After the instance has successfully rebooted, resend the public key to the bastion host and reattempt the connection. |
| `Permission denied` error when trying to connect to the bastion host | After the public key is uploaded to the bastion host, you have only 60 seconds to start the connection. After 60 seconds, the key is automatically removed, and you can’t use it to connect to the instance. If this occurs, you can repeat the step to resend the key to the instance. |

## Related resources
<a name="access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-resources"></a>

**AWS documentation**
+ [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) (Systems Manager documentation)
+ [Install the Session Manager plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html) (Systems Manager documentation)
+ [Allowing SSH connections for Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-enable-ssh-connections.html#ssh-connections-enable) (Systems Manager documentation)
+ [About using EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html) (Amazon EC2 documentation)
+ [Connect using EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html) (Amazon EC2 documentation)
+ [Identity and access management for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-iam.html) (Amazon EC2 documentation)
+ [Using an IAM role to grant permissions to applications running on Amazon EC2 instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) (IAM documentation)
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) (IAM documentation)
+ [Control traffic to resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) (Amazon VPC documentation)

**Other resources**
+ [Terraform Developer webpage](https://developer.hashicorp.com/terraform)
+ [Command: validate](https://developer.hashicorp.com/terraform/cli/commands/validate) (Terraform documentation)
+ [Command: fmt](https://developer.hashicorp.com/terraform/cli/commands/fmt) (Terraform documentation)
+ [Testing HashiCorp Terraform](https://www.hashicorp.com/blog/testing-hashicorp-terraform) (HashiCorp blog post)
+ [Checkov webpage](https://www.checkov.io/)

## Additional information
<a name="access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-additional"></a>

**Alternative approaches to establish an SSH connection with the bastion host**

*Port forwarding*

You can use the `-D 8888` option to open an SSH connection with dynamic port forwarding. For more information, see the [instructions](https://explainshell.com/explain?cmd=ssh+-i+%24PRIVATE_KEY_FILE+-D+8888+ec2-user%40%24INSTANCE_ID) at explainshell.com. The following is an example of a command to open an SSH connection by using port forwarding.

```
ssh -i $PRIVATE_KEY_FILE -D 8888 ec2-user@$INSTANCE_ID
```

This is kind of connection opens a SOCKS proxy that can forward traffic from your local browser through the bastion host. If you are using Linux or MacOS, to see all options, enter `man ssh`. This displays the SSH reference manual.

*Using the provided script*

Instead of manually running the steps described in *Connect to the bastion host by using Session Manager* in the [Epics](#access-a-bastion-host-by-using-session-manager-and-amazon-ec2-instance-connect-epics) section, you can use the **connect.sh** script included in the code repository. This script generates the SSH key pair, pushes the public key to the Amazon EC2 instance, and initiates a connection with the bastion host. When you run the script, you pass the tag and key name as arguments. The following is an example of the command to run the script.

```
./connect.sh sandbox-dev-bastion-host my_key
```
