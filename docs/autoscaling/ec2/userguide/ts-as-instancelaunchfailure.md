---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-instancelaunchfailure.html
---

# Troubleshoot Amazon EC2 Auto Scaling: EC2 instance launch failures
<a name="ts-as-instancelaunchfailure"></a>

This page provides information about your EC2 instances that fail to launch, potential causes, and the steps you can take to resolve the issues.

To retrieve an error message, see [Retrieve an error message from scaling activities](CHAP_Troubleshooting.md#RetrievingErrors).

When your EC2 instances fail to launch, you might get one or more of the following error messages:

**Topics**
+ [The requested configuration is currently not supported.](#ts-as-instancelaunchfailure-3)
+ [The security group <name of the security group> does not exist. Launching EC2 instance failed.](#ts-as-instancelaunchfailure-1)
+ [The key pair <key pair associated with your EC2 instance> does not exist. Launching EC2 instance failed.](#ts-as-instancelaunchfailure-2)
+ [Your requested instance type (<instance type>) is not supported in your requested Availability Zone (<instance Availability Zone>)...](#ts-as-instancelaunchfailure-6)
+ [Your Spot request price of 0.015 is lower than the minimum required Spot request fulfillment price of 0.0735...](#ts-as-instancelaunchfailure-7)
+ [Invalid device name <device name> / Invalid device name upload. Launching EC2 instance failed.](#ts-as-instancelaunchfailure-8)
+ [Value (<name associated with the instance storage device>) for parameter virtualName is invalid... Launching EC2 instance failed.](#ts-as-instancelaunchfailure-9)
+ [EBS block device mappings not supported for instance-store AMIs.](#ts-as-instancelaunchfailure-10)
+ [Placement groups may not be used with instances of type '<instance type>'. Launching EC2 instance failed.](#ts-as-instancelaunchfailure-11)
+ [Client.InternalError: Client error on launch.](#ts-as-instancelaunchfailure-12)
+ [We currently do not have sufficient <instance type> capacity in the Availability Zone you requested... Launching EC2 instance failed.](#ts-as-capacity-1)
+ [The requested reservation does not have sufficient compatible and available capacity for this request. Launching EC2 instance failed.](#ts-as-capacity-4)
+ [Your Capacity Block reservation <reservation id> is not active yet. Launching EC2 instance failed.](#ts-as-capacity-5)
+ [There is no Spot capacity available that matches your request. Launching EC2 instance failed.](#ts-as-capacity-2)
+ [<number of instances> instance(s) are already running. Launching EC2 instance failed.](#ts-as-capacity-3)

## The requested configuration is currently not supported.
<a name="ts-as-instancelaunchfailure-3"></a>

**Cause**: Some options in your launch template or launch configuration might not be compatible with the instance type, or the instance configuration might not be supported in your requested AWS Region or Availability Zones.

**Solution**: Try a different instance configuration. To search for an instance type that meets your requirements, see [Finding an Amazon EC2 instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-discovery.html) in the *Amazon EC2 User Guide*.

For further guidance to resolve this issue, check the following:
+ Ensure that you have chosen an AMI that is supported by your instance type. For example, if the instance type uses an Arm-based AWS Graviton processor instead of an Intel Xeon processor, you need an Arm-compatible AMI. For more information about choosing a compatible instance type, see [Compatibility for changing the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resize-limitations.html) in the *Amazon EC2 User Guide*.
+ Test that the instance type is available in your requested Region and Availability Zones. The newest generation instance types might not yet be available in a given Region or Availability Zone. The older generation instance types might not be available in newer Regions and Availability Zones. To search for instance types offered by location (Region or Availability Zone), use the [describe-instance-type-offerings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-type-offerings.html) command. For more information, see [Finding an Amazon EC2 instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-discovery.html) in the *Amazon EC2 User Guide*.
+ If you use Dedicated Instances or Dedicated Hosts, ensure that you have chosen an instance type that's supported as a Dedicated Instance or Dedicated Host.

## The security group <name of the security group> does not exist. Launching EC2 instance failed.
<a name="ts-as-instancelaunchfailure-1"></a>

**Cause**: The security group specified in your launch template or launch configuration might have been deleted.

**Solution**:

1. Use the [describe-security-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-groups.html) command to get the list of the security groups associated with your account.

1. From the list, select the security groups to use. To create a security group instead, use the [create-security-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-security-group.html) command.

1. Create a new launch template or launch configuration.

1. Update your Auto Scaling group with the new launch template or launch configuration using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

## The key pair <key pair associated with your EC2 instance> does not exist. Launching EC2 instance failed.
<a name="ts-as-instancelaunchfailure-2"></a>

**Cause**: The key pair that was used when launching the instance might have been deleted.

**Solution**:

1. Use the [describe-key-pairs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-key-pairs.html) command to get the list of the key pairs available to you.

1. From the list, select the key pair to use. To create a key pair instead, use the [create-key-pair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-key-pair.html) command.

1. Create a new launch template or launch configuration.

1. Update your Auto Scaling group with the new launch template or launch configuration using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

## Your requested instance type (<instance type>) is not supported in your requested Availability Zone (<instance Availability Zone>)...
<a name="ts-as-instancelaunchfailure-6"></a>

**Error message**: Your requested instance type (<instance type>) is not supported in your requested Availability Zone (<instance Availability Zone>)...Launching EC2 instance failed.

**Cause**: The Availability Zones specified in your Auto Scaling group don't support your chosen instance type.

**Solution**:

1. Verify which Availability Zones support your chosen instance type using the [describe-instance-type-offerings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-type-offerings.html) command or from the Amazon EC2 console by checking the **Availability Zones** value on the networking pane of the **Instance types** page.

1. Update or remove the subnet for any unsupported zones in the settings of your Auto Scaling group using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command. For more information, see [Add an Availability Zone](as-add-az-console.md).

## Your Spot request price of 0.015 is lower than the minimum required Spot request fulfillment price of 0.0735...
<a name="ts-as-instancelaunchfailure-7"></a>

**Cause**: The Spot maximum price in your request is lower than the Spot price for the instance type that you selected.

**Solution**: Submit a new request with a higher Spot maximum price (possibly the On-Demand price). Previously, the Spot price you paid was based on bidding. Today, you pay the current Spot price. By setting your maximum price higher, it gives the Amazon EC2 Spot service a better chance of launching and maintaining your required amount of capacity.

## Invalid device name <device name> / Invalid device name upload. Launching EC2 instance failed.
<a name="ts-as-instancelaunchfailure-8"></a>

**Cause 1**: The block device mappings in your launch template or launch configuration might contain block device names that are not available or currently not supported.

**Solution**:

1. Verify which device names are available for your specific instance configuration. For more details on device naming, see [Device names on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html) in the *Amazon EC2 User Guide*.

1. Manually create an Amazon EC2 instance that is not part of the Auto Scaling group and investigate the problem. If the block device naming configuration conflicts with the names in the Amazon Machine Image (AMI), the instance will fail during launch. For more information, see [Block device mappings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide*.

1. After you confirm that your instance launched successfully, use the [describe-volumes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volumes.html) command to see how the volumes are exposed to the instance.

1. Create a new launch template or launch configuration using the device name listed in the volume description.

1. Update your Auto Scaling group with the new launch template or launch configuration using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

## Value (<name associated with the instance storage device>) for parameter virtualName is invalid... Launching EC2 instance failed.
<a name="ts-as-instancelaunchfailure-9"></a>

**Cause**: The format specified for the virtual name associated with the block device is incorrect.

**Solution**:

1. Create a new launch template or launch configuration by specifying the device name in the `virtualName` parameter. For information about the device name format, see [Device naming on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html) in the *Amazon EC2 User Guide*.

1. Update your Auto Scaling group with the new launch template or launch configuration using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

## EBS block device mappings not supported for instance-store AMIs.
<a name="ts-as-instancelaunchfailure-10"></a>

**Cause**: The block device mappings specified in the launch template or launch configuration are not supported on your instance.

**Solution**:

1. Create a new launch template or launch configuration with block device mappings supported by your instance type. For more information, see [Block device mapping](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide*.

1. Update your Auto Scaling group with the new launch template or launch configuration using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

## Placement groups may not be used with instances of type '<instance type>'. Launching EC2 instance failed.
<a name="ts-as-instancelaunchfailure-11"></a>

**Cause**: Your cluster placement group contains an invalid instance type.

**Solution**:

1. For information about valid instance types supported by the placement groups, see [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide*.

1. Follow the instructions detailed in the [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) to create a new placement group.

1.  Alternatively, create a new launch template or launch configuration with the supported instance type.

1. Update your Auto Scaling group with a new placement group, launch template, or launch configuration using the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

## Client.InternalError: Client error on launch.
<a name="ts-as-instancelaunchfailure-12"></a>

**Problem**: Amazon EC2 Auto Scaling tries to launch an instance that has an encrypted EBS volume, but the service-linked role does not have access to the AWS KMS customer managed key used to encrypt it. For more information, see [Required AWS KMS key policy for use with encrypted volumes](key-policy-requirements-EBS-encryption.md).

**Cause 1**: You need a key policy that gives permission to use the customer managed key to the proper service-linked role.

**Solution 1**: Allow the service-linked role to use the customer managed key as follows:

1. Determine which service-linked role to use for this Auto Scaling group.

1. Update the key policy on the customer managed key and allow the service-linked role to use the customer managed key.

1. Update the Auto Scaling group to use the service-linked role.

For an example of a key policy that lets the service-linked role use the customer managed key, see [Example 1: Key policy sections that allow access to the customer managed key](key-policy-requirements-EBS-encryption.md#policy-example-cmk-access).

**Cause 2**: If the customer managed key and Auto Scaling group are in *different* AWS accounts, you need to configure cross-account access to the customer managed key in order to give permission to use the customer managed key to the proper service-linked role.

**Solution 2**: Allow the service-linked role in the external account to use the customer managed key in the local account as follows:

1. Update the key policy on the customer managed key to allow the Auto Scaling group account access to the customer managed key.

1. Define an IAM user or role in the Auto Scaling group account that can create a grant.

1. Determine which service-linked role to use for this Auto Scaling group.

1. Create a grant to the customer managed key with the proper service-linked role as the grantee principal.

1. Update the Auto Scaling group to use the service-linked role.

For more information, see [Example 2: Key policy sections that allow cross-account access to the customer managed key](key-policy-requirements-EBS-encryption.md#policy-example-cmk-cross-account-access).

**Solution 3**: Use a customer managed key in the same AWS account as the Auto Scaling group.

1. Copy and re-encrypt the snapshot with another customer managed key that belongs to the same account as the Auto Scaling group.

1. Allow the service-linked role to use the new customer managed key. See the steps for Solution 1.

## We currently do not have sufficient <instance type> capacity in the Availability Zone you requested... Launching EC2 instance failed.
<a name="ts-as-capacity-1"></a>

**Error message**: We currently do not have sufficient <instance type> capacity in the Availability Zone you requested (<requested Availability Zone>). Our system will be working on provisioning additional capacity. You can currently get <instance type> capacity by not specifying an Availability Zone in your request or choosing <list of Availability Zones that currently supports the instance type>. Launching EC2 instance failed.

**Cause**: At this time, the requested instance type and Availability Zone combination isn't supported.

**Solution**: To resolve the issue, try the following:
+ Wait a few minutes for Amazon EC2 Auto Scaling to find capacity for this instance type in other enabled Availability Zones.
+ Expand your Auto Scaling group to additional Availability Zones. For more information, see [Add an Availability Zone](as-add-az-console.md).
+ Follow the best practice of using a diverse set of instance types so that you're not reliant on one specific instance type. For more information, see [Auto Scaling groups with multiple instance types and purchase options](ec2-auto-scaling-mixed-instances-groups.md).

## The requested reservation does not have sufficient compatible and available capacity for this request. Launching EC2 instance failed.
<a name="ts-as-capacity-4"></a>

**Cause 1**: You've reached the limit on the number of instances that you can launch with a `targeted` On-Demand Capacity Reservation.

**Solution 1**: Either increase the number of instances that you can launch with the `targeted` On-Demand Capacity Reservation, or use a Capacity Reservations group so that anything beyond the reserved capacity will launch as regular On-Demand capacity. For more information, see [Use Capacity Reservations in your Auto Scaling group](use-ec2-capacity-reservations.md).

**Cause 2**: You've reached the limit on the number of instances that you can launch with a Capacity Block.

With Capacity Blocks, you are constrained by the amount of capacity originally purchased. If you experience a higher number of launches than anticipated and use up all the capacity that you have available, this causes launches to fail. Terminating instances go through a lengthy clean up process before they're fully terminated. During this time, they can't be reused. This can also cause launches to fail. For more information, see [Target Capacity Blocks or interruptible Capacity Reservations from a launch template](capacity-reservation-create-asg-procedure.md#target-capacity-blocks-or-interruptible-capacity-reservations-from-a-launch-template).

**Solution 2**: To resolve the issue, try the following:
+ Keep the request as is. If a Capacity Block instance is terminating, you must wait several minutes for the instance to finish terminating and capacity to become available again. Amazon EC2 Auto Scaling continues to automatically make the launch request until capacity becomes available.
+ Make sure that you purchase sufficient capacity to accommodate your peak workload so that you do not encounter this error frequently.

## Your Capacity Block reservation <reservation id> is not active yet. Launching EC2 instance failed.
<a name="ts-as-capacity-5"></a>

**Cause**: The specified Capacity Block is not active yet.

**Solution**: Follow the recommended approach for Capacity Blocks and use scheduled scaling. Doing so helps you make sure you increase the desired capacity of your Auto Scaling group only when the reservation is active and decrease it before the reservation is over.

## There is no Spot capacity available that matches your request. Launching EC2 instance failed.
<a name="ts-as-capacity-2"></a>

**Cause**: At this time, there isn't enough spare capacity to fulfill your request for Spot Instances.

**Solution**: To resolve the issue, try the following:
+ Wait a few minutes; capacity can shift frequently. Amazon EC2 Auto Scaling continues to automatically make the launch request until capacity becomes available.
+ Expand your Auto Scaling group to additional Availability Zones. For more information, see [Add an Availability Zone](as-add-az-console.md).
+ Follow the best practice of using a diverse set of instance types so that you're not reliant on one specific instance type. For more information, see [Auto Scaling groups with multiple instance types and purchase options](ec2-auto-scaling-mixed-instances-groups.md).

## <number of instances> instance(s) are already running. Launching EC2 instance failed.
<a name="ts-as-capacity-3"></a>

**Cause**: You have reached the limit on the number of instances that you can launch in a Region. When you create your AWS account, we set default limits on the number of instances you can run on a per-Region basis.

**Solution**: To resolve the issue, try the following:
+ If your current limits aren't adequate for your needs, you can request a quota increase on a per-Region basis. For more information, see [Amazon EC2 service quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) in the *Amazon EC2 User Guide*.
+ Submit a new request with a reduced number of instances (which you can increase at a later stage).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
