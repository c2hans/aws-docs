---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/ec2.html
---

# AL2027 on Amazon EC2
<a name="ec2"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

Use one of the following procedures to launch an Amazon EC2 instance with an AL2027 AMI. You can choose either the standard AMI or the minimal AMI.

**Note**
For x86-64 instances, AL2027 requires x86-64-v3 or later processors. The following instance types are not supported: `c1`, `c3`, `i2`, `m1`, `m2`, `m3`, `r3`, and `t1`.
For Arm-based instances, AL2027 requires Graviton2 or later processors. `a1` instances are not supported.

## Launching AL2027 using the Amazon EC2 console
<a name="launch-from-ec2-console"></a>

**To launch an Amazon EC2 instance with an AL2027 AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. From the filter drop-down, choose **Public images**.

1. In the search field, enter **al2027-preview-ami**.
**Note**
Make sure that **amazon** appears in the **Owner alias** column.

1. Select an image from the list. Under **Source**, you can determine whether the AMI is standard or minimal. An AL2027 AMI name uses this format:

   `al2027-preview-[ami || ami-minimal]-2027.0.[release build date].[build number]-kernel-[version]-[arm64 || x86_64]`

1. Choose **Launch instance from AMI** and configure the instance type, networking, storage, and key pair as needed.

For more information about launching Amazon EC2 instances, see [Get started with Amazon EC2 Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) in the *Amazon EC2 User Guide*.

## Launching AL2027 using the SSM parameter and AWS CLI
<a name="launch-via-aws-cli"></a>

In the AWS CLI, you can use an AMI SSM parameter value to launch a new instance of AL2027. Use one of the following dynamic SSM parameter values with `/aws/service/ami-amazon-linux-latest/` as the prefix:
+ `al2027-preview-ami-kernel-default-arm64` for arm64 architecture
+ `al2027-preview-ami-minimal-kernel-default-arm64` for arm64 architecture (minimal AMI)
+ `al2027-preview-ami-kernel-default-x86_64` for x86\_64 architecture
+ `al2027-preview-ami-minimal-kernel-default-x86_64` for x86\_64 architecture (minimal AMI)

**Note**
Each of the following items in the command is a placeholder. Replace them with your own values: {{m5.xlarge}}, {{us-east-1}}, {{my-key-pair}}, and {{sg-004a7650}}.

```
$ aws ec2 run-instances \
  --image-id \
    resolve:ssm:/aws/service/ami-amazon-linux-latest/al2027-preview-ami-kernel-default-x86_64 \
  --instance-type {{m5.xlarge}} \
  --region {{us-east-1}} \
  --key-name {{my-key-pair}} \
  --security-group-ids {{sg-004a7650}}
```

The `--image-id` flag specifies the SSM parameter value. The `resolve:ssm:` prefix tells the AWS CLI to resolve the parameter to the latest AMI ID at launch time.

The `--instance-type` flag specifies the type and size of the instance. This must be compatible with the AMI architecture you selected.

The `--region` flag specifies the AWS Region where you create your instance.

The `--key-name` flag specifies the key pair used to connect to the instance using SSH.

The `--security-group-ids` flag specifies the security group that determines access permissions for inbound and outbound network traffic.

**Important**
The AWS CLI requires that you specify an existing security group that allows access to the instance from your remote machine over port TCP:22. Without a specified security group, your new instance is placed in a default security group.

For more information, see [Launching, listing, and terminating Amazon EC2 instances](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-instances.html) in the *AWS Command Line Interface User Guide*.

## Launching AL2027 using a specific AMI ID
<a name="launch-by-ami-id"></a>

You can launch a specific AL2027 AMI using the AMI ID. You can determine which AL2027 AMI ID is needed by looking at the AMI list in the Amazon EC2 console. Or, you can use AWS Systems Manager. For more information, see [Query for the latest Amazon Linux AMI IDs using AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/).

## Connect to your instance
<a name="ec2-connect"></a>

After your instance is running, connect to it using SSH:

```
ssh -i <your-key.pem> ec2-user@<instance-public-ip>
```

The default user for AL2027 instances is `ec2-user`.
