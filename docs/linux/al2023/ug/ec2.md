---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/ec2.html
---

# AL2023 on Amazon EC2
<a name="ec2"></a>

Use one of the following procedures to launch an Amazon EC2 instance with an AL2023 AMI. You can choose either the standard AMI, or the minimal AMI. For more information about the differences between the standard AMI and the minimal AMI, see [Comparing AL2023 standard (default) and minimal AMIs](AMI-minimal-and-standard-differences.md).

**Topics**
+ [Launching AL2023 using the Amazon EC2 console](#launch-from-ec2-console)
+ [Launching AL2023 using the SSM parameter and AWS CLI](#launch-via-aws-cli)
+ [Launching the latest AL2023 AMI using CloudFormation](#launch-from-cloudformation)
+ [Launching AL2023 using a specific AMI ID](#launch-by-ami-id)
+ [AL2023 AMI deprecation and life cycle](#ami-deprecation)
+ [Connecting to AL2023 instances](connecting-to-instances.md)
+ [Comparing AL2023 standard and minimal AMIs](AMI-minimal-and-standard-differences.md)

## Launching AL2023 using the Amazon EC2 console
<a name="launch-from-ec2-console"></a>

Use the Amazon EC2 console to launch an AL2023 AMI.

**Note**
For Arm-based instances, AL2023 only supports instance types that use Graviton2 or later processors. AL2023 doesn't support A1 instances.

Use the following steps to launch an Amazon EC2 instance with an AL2023 AMI from the Amazon EC2 console.

**To launch an EC2 instance with an AL2023 AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. From the filter drop-down, choose **Public images**.

1. In the search field, enter **al2023-ami**.
**Note**
Make sure that **amazon** appears in the **Owner alias** column.

1. Select an image from the list. Under **Source**, you can determine whether the AMI is standard or minimal. An AL2023 AMI name can be interpreted by using this format:

   `'al2023-[ami || ami-minimal]-2023.0.[release build date].[build number]-kernel-[version number]-[arm64 || x86_64]'`

1. The following image shows a partial list of AL2023 AMIs.
![A listing of AL2023 AMIs under the Source column.](http://docs.aws.amazon.com/linux/al2023/ug/images/launch-instance.png)

For more information about launching Amazon EC2 instances, see [Get started with Amazon EC2 Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) in the *Amazon EC2 User Guide*.

## Launching AL2023 using the SSM parameter and AWS CLI
<a name="launch-via-aws-cli"></a>

**Important**
 Starting August 17, 2026, the default kernel for AL2023 will change from 6.1 to 6.18. New instances launched from the `al2023-ami-kernel-default` AMIs will boot kernel 6.18. Already-running instances are not affected and will keep the kernel they booted with. To stay on a specific kernel version, launch from version-specific AMIs such as `al2023-ami-kernel-6.1`.
 For FIPS workloads, note that the default kernel might not always be the FIPS-validated kernel. If you require FIPS mode, see the [AL2023 FIPS FAQ on the AWS website](https://aws.amazon.com/linux/amazon-linux-2023/faqs/#al2023-fips-faq--3m3tsn).

In the AWS CLI, you can use an AMI's SSM parameter value to launch a new instance of AL2023. More specifically, use one of the dynamic SSM parameter values from the following list, and add `/aws/service/ami-amazon-linux-latest/` before the SSM parameter value/. You use this to launch the instance in the AWS CLI.
+ `al2023-ami-kernel-default-arm64` for arm64 architecture
+ `al2023-ami-minimal-kernel-default-arm64` for arm64 architecture (minimal AMI)
+ `al2023-ami-kernel-default-x86_64` for x86\_64 architecture
+ `al2023-ami-minimal-kernel-default-x86_64` for x86\_64 architecture (minimal AMI)

**Note**
Each of the {{italic}} items is an example parameter. Replace them with your own information.

```
$ aws ec2 run-instances \
  --image-id \
    resolve:ssm:/aws/service/ami-amazon-linux-latest/{{al2023-ami-kernel-default-x86_64}} \
  --instance-type {{m5.xlarge}} \
  --region {{us-east-1}} \
  --key-name {{aws-key-us-east-1}} \
  --security-group-ids {{sg-004a7650}}
```

The `--image-id` flag specifies the SSM parameter value.

The `--instance-type` flag specifies the type and size of the instance. This flag must be compatible with the AMI type that you selected.

The `--region` flag specifies the AWS Region where you create your instance.

The `--key-name` flag specifies the AWS Region's key that's used to connect to the instance. If you don't provide a key that exists in the Region where you create the instance, you can't connect to the instance using SSH.

The `--security-group-ids` flag specifies the security group that determines the access permissions for inbound and outbound network traffic.

**Important**
The AWS CLI requires that you specify an existing security group that allows access to the instance from your remote machine over port TCP:22. Without a specified security group, your new instance are placed in a default security group. In a default security group, your instance can only connect with the other instances within your VPC.

For more information, see [Launching, listing, and terminating Amazon EC2 instances](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-instances.html) in the *AWS Command Line Interface User Guide*.

## Launching the latest AL2023 AMI using CloudFormation
<a name="launch-from-cloudformation"></a>

To launch an AL2023 AMI using CloudFormation, use one of the following templates.

**Note**
The `x86_64` and `Arm64` AMIs each require different instance types. For more information, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)

`JSON` template:

```
{
  "Parameters": {
    "LatestAmiId": {
      "Type": "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>",
      "Default": "/aws/service/ami-amazon-linux-latest/al2023-ami-minimal-kernel-default-x86_64"
    }
  },
  "Resources": {
    "MyEC2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "InstanceType": "t2.large",
        "ImageId": {
          "Ref": "LatestAmiId"
        }
      }
    }
  }
}
```

`YAML` template:

```
Parameters:
  LatestAmiId:
    Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: '/aws/service/ami-amazon-linux-latest/al2023-ami-minimal-kernel-default-x86_64'

Resources:
  Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: 't2.large'
      ImageId: !Ref LatestAmiId
```

Make sure to replace the AMI parameter at the end of the "Default" section, if needed.

The following are dynamic kernel specifications. The default kernel version automatically changes with each major kernel version update.
+ `al2023-ami-kernel-default-arm64` for arm64 architecture
+ `al2023-ami-minimal-kernel-default-arm64` for arm64 architecture (minimal AMI)
+ `al2023-ami-kernel-default-x86_64` for x86\_64 architecture
+ `al2023-ami-minimal-kernel-default-x86_64` for x86\_64 architecture (minimal AMI)

The following version-specific parameter values are also available:

### For kernel 6.18
<a name="cfn-kernel6.18-params"></a>
+ `al2023-ami-kernel-6.18-arm64` for arm64 architecture
+ `al2023-ami-minimal-kernel-6.18-arm64` for arm64 architecture (minimal AMI)
+ `al2023-ami-kernel-6.18-x86_64` for x86\_64 architecture
+ `al2023-ami-minimal-kernel-6.18-x86_64` for x86\_64 architecture (minimal AMI)

### For kernel 6.12
<a name="cfn-kernel6.12-params"></a>
+ `al2023-ami-kernel-6.12-arm64` for arm64 architecture
+ `al2023-ami-minimal-kernel-6.12-arm64` for arm64 architecture (minimal AMI)
+ `al2023-ami-kernel-6.12-x86_64` for x86\_64 architecture
+ `al2023-ami-minimal-kernel-6.12-x86_64` for x86\_64 architecture (minimal AMI)

### For kernel 6.1
<a name="cfn-kernel6.1-params"></a>
+ `al2023-ami-kernel-6.1-arm64` for arm64 architecture
+ `al2023-ami-minimal-kernel-6.1-arm64` for arm64 architecture (minimal AMI)
+ `al2023-ami-kernel-6.1-x86_64` for x86\_64 architecture
+ `al2023-ami-minimal-kernel-6.1-x86_64` for x86\_64 architecture (minimal AMI)

## Launching AL2023 using a specific AMI ID
<a name="launch-by-ami-id"></a>

You can launch a specific AL2023 AMI using the AMI ID. You can determine which AL2023 AMI ID is needed by looking at the AMI list in the Amazon EC2 console. Or, you can use AWS Systems Manager. If you're using Systems Manager, make sure to select the AMI alias from those that are listed in the previous section. For more information, see [Query for the latest Amazon Linux AMI IDs using AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/).

## AL2023 AMI deprecation and life cycle
<a name="ami-deprecation"></a>

Each new AL2023 release includes a new AMI. When the AMI is registered, it's marked with a deprecation date. The deprecation date for each AL2023 AMI is 90 days from the time it was released to match the time period that [Kernel Live Patching on AL2023](live-patching.md) is offered for each individual kernel release.

**Note**
The 90 day deprecation date refers to an individual AMI and doesn’t refer to the AL2023 [Release cadence](release-cadence.md) or product support period.

For more information about AMI deprecation, see [Deprecate an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deprecate.html) in the *Amazon EC2 User Guide*.

Regularly using an updated AMI to launch an instance ensures that the instance starts with the latest security updates, including an updated kernel. If you launch a previous version of an AMI and apply updates, there is a period of time that the instance doesn't have the latest security updates. To ensure you're using the latest AMI, we recommend that you use SSM parameters.

For more information about using SSM parameters to launch an instance, see:
+ [Launching AL2023 using the SSM parameter and AWS CLI](#launch-via-aws-cli)
+ [Launching the latest AL2023 AMI using CloudFormation](#launch-from-cloudformation)
