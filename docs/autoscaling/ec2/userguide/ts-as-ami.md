---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-ami.html
---

# Troubleshoot Amazon EC2 Auto Scaling: AMI issues
<a name="ts-as-ami"></a>

This page provides information about the issues associated with your AMIs, potential causes, and the steps you can take to resolve the issues.

To retrieve an error message, see [Retrieve an error message from scaling activities](CHAP_Troubleshooting.md#RetrievingErrors).

When your EC2 instances fail to launch due to issues with your AMI, you might get one or more of the following error messages.

**Topics**
+ [The AMI ID <ID of your AMI> does not exist. Launching EC2 instance failed.](#ts-as-ami-1)
+ [AMI <AMI ID> is pending, and cannot be run. Launching EC2 instance failed.](#ts-as-ami-2)
+ [Invalid device name <device name>. Launching EC2 instance failed.](#ts-as-ami-4)
+ [The architecture 'arm64 ' of the specified instance type does not match the architecture 'x86\_64' of the specified AMI...Launching EC2 instance failed.](#ts-as-ami-5)
+ [AMI '<AMI ID>' is disabled, and cannot be run. Launching EC2 instance failed.](#ts-disabled-ami-error)

**Important**
AWS supports sharing an AMI privately with another AWS account by modifying the AMI permissions. If an AMI is made private without being shared, this can result in an authorization error when launching new instances. For more information about sharing private AMIs, see [Share an AMI with specific AWS accounts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html) in the *Amazon EC2 User Guide*.

## The AMI ID <ID of your AMI> does not exist. Launching EC2 instance failed.
<a name="ts-as-ami-1"></a>
+ **Cause**: The AMI might have been deleted after creating the launch template or launch configuration.
+ **Solution**:

  1. Create a new launch template or launch configuration using a valid AMI.

  1. Update your Auto Scaling group with the new launch template or launch configuration using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

## AMI <AMI ID> is pending, and cannot be run. Launching EC2 instance failed.
<a name="ts-as-ami-2"></a>

**Cause**: You might have just created your AMI (by taking a snapshot of a running instance or any other way), and it might not be available yet.

**Solution**: You must wait for your AMI to be available and then create your launch template or launch configuration.

## Invalid device name <device name>. Launching EC2 instance failed.
<a name="ts-as-ami-4"></a>

**Cause**: When attaching an EBS volume to an EC2 instance, you must provide a valid device name for the volume. The selected AMI must support this device name.

**Solution**:

1. Create a new launch template or launch configuration and specify the correct device name for your AMI. The recommended naming convention varies based on the virtualization type of the AMI. For more information, see [Device names](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html) in the *Amazon EC2 User Guide*.

1. Update your Auto Scaling group with the new launch template or launch configuration using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

## The architecture 'arm64 ' of the specified instance type does not match the architecture 'x86\_64' of the specified AMI...Launching EC2 instance failed.
<a name="ts-as-ami-5"></a>

**Cause 1**: If the architecture of the AMI and the instance type used in your launch template or launch configuration are not the same, you get an error when Amazon EC2 Auto Scaling tries to launch an instance using the incompatible instance configuration.

**Solution 1**:

1. Verify the architecture of your AMI using the [describe-images](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html) command or from the Amazon EC2 console by checking the **Architecture** value on the details pane of the **Amazon Machine Images (AMIs)** page.

1. Find an instance type that has the same architecture as your AMI using the [describe-instance-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-types.html) command or from the Amazon EC2 console by checking the **Architecture** column on the **Instance types** screen. For more information about choosing a compatible instance type, see [Compatibility for changing the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resize-limitations.html) in the *Amazon EC2 User Guide*.

1. Create a new launch template or launch configuration using an instance type that has the same architecture as your AMI.

1. Update your Auto Scaling group with the new launch template or launch configuration using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

**Cause 2**: Amazon EC2 Auto Scaling tries to launch an instance type that's specified in the mixed instances policy for your Auto Scaling group, but the instance type does not have the same architecture as the AMI specified in your launch template.

**Solution 1**: Do not include instance types that have different architectures in your mixed instances policy.

1. Verify the architecture of your AMI using the [describe-images](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html) command or from the Amazon EC2 console by checking the **Architecture** value on the details pane of the **Amazon Machine Images (AMIs)** page.

1. Verify the architecture of each instance type that you intend to include in your mixed instances policy using the [describe-instance-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-types.html) command or from the Amazon EC2 console by checking the **Architecture** column on the **Instance types** screen. For more information about choosing compatible instance types, see [Compatibility for changing the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resize-limitations.html) in the *Amazon EC2 User Guide*.

1. Update or remove the incompatible instance types from your Auto Scaling group using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

**Solution 2**: To launch both Arm (Graviton2) and x86\_64 (Intel) instances in the same Auto Scaling group, you must use launch templates supported by an Arm-compatible AMI and an Intel x86-compatible AMI, respectively, to match the instance types in your mixed instances policy.

1. Verify the architecture of the AMI in your existing launch template using the [describe-images](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html) command or from the Amazon EC2 console by checking the **Architecture** value on the details pane of the **Amazon Machine Images (AMIs)** page.

1. Create a new launch template using an AMI that matches the other architecture you intend to use.

1. Update your Auto Scaling group to override the existing launch template and specify the new launch template for each compatible instance type using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command. For more information, see [Use multiple launch templates](ec2-auto-scaling-mixed-instances-groups-launch-template-overrides.md).

## AMI '<AMI ID>' is disabled, and cannot be run. Launching EC2 instance failed.
<a name="ts-disabled-ami-error"></a>

**Cause**: You are attempting to launch instances from an AMI that has been disabled. For more information, see [Disable an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disable-an-ami.html) in the *Amazon EC2 User Guide*.

**Solution**:

1. Create a new launch template or launch configuration and specify an AMI that is not disabled.

1. Update your Auto Scaling group with the new launch template or launch configuration using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.
