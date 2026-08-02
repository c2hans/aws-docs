---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.html
---

# Create a launch template using advanced settings
<a name="advanced-settings-for-your-launch-template"></a>

This topic describes how to create a launch template with advanced settings from the AWS Management Console.

**To create a launch template using advanced settings**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, under **Instances**, choose **Launch Templates**, and then choose **Create launch template**.

1. Configure your launch template as described in the following topics:
   +  [Required settings](#configure-required-settings)
   +  [Advanced settings](#configure-advanced-settings)

1. Choose **Create launch template**.

## Required settings
<a name="configure-required-settings"></a>

When you create a launch template, you must include the following required settings.

**Launch template name**
Enter a unique name that describes the launch template.

**Application and OS Images (Amazon Machine Image)**
Choose the Amazon Machine Image (AMI) that you want to use. You can either search or browse for the AMI you want to use. For best scaling efficiency, choose a custom AMI that is fully configured to launch an instance with your application code and requires few modifications on launch.

**Instance type**
Choose an instance type that is compatible with your AMI. You can skip adding an instance type to your launch template if you plan to use multiple instances types that are embedded in the Auto Scaling group's own resource definition. An instance type is only required if you don't plan to create a [mixed instances group](ec2-auto-scaling-mixed-instances-groups.md).

## Advanced settings
<a name="configure-advanced-settings"></a>

The advanced settings are optional. If you do not configure any advanced settings, the specific capabilities will not be added to your instances.

Expand the **Advanced details** section to view the advanced settings. The following sections describe the most useful advanced settings to focus on when creating a launch template for an Auto Scaling group. For more information, see [Advanced details](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#lt-advanced-details) in the *Amazon EC2 User Guide*.

**IAM instance profile**
The instance profile contains the IAM role that you want to use. When your Auto Scaling group launches an EC2 instance, the permissions defined in the associated IAM role are granted to applications running on the instance. For more information, see [IAM role for applications that run on Amazon EC2 instances](us-iam-role.md).

**Termination protection**
When enabled, this feature prevents users from terminating an instance using the Amazon EC2 console, CLI commands, and API operations. Termination protection provides an extra safeguard against accidental termination. It does not prevent Amazon EC2 Auto Scaling from terminating an instance. To control which instances Amazon EC2 Auto Scaling can terminate, see [Use instance scale-in protection to control instance termination](ec2-auto-scaling-instance-protection.md).

**Detailed CloudWatch monitoring**
You can enable detailed monitoring for your EC2 instances to allow them to send metric data to Amazon CloudWatch at 1-minute intervals. By default, EC2 instances send metric data to CloudWatch at 5-minute intervals. Additional charges apply. For more information, see [Configure monitoring for Auto Scaling instances](enable-as-instance-metrics.md).

**Credit specification**
Amazon EC2 provides burstable performance instances, such as T2, T3, and T3a, that allow applications to burst beyond the baseline CPU performance when required. By default, these instances can burst for a limited time before their CPU usage is throttled. You can optionally enable unlimited mode so that the instances can burst beyond the baseline for as long as needed. This allows applications to sustain high CPU performance when required. Additional charges may apply. For more information, see [Use an Auto Scaling group to launch a burstable performance instance as Unlimited](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-how-to.html#burstable-performance-instances-auto-scaling-grp) in the *Amazon EC2 User Guide*.

**Placement group name**
You can specify a placement group and use a cluster or a partition strategy to influence how your instances are physically located in the AWS data center. For small Auto Scaling groups, you can also use the spread strategy. For more information, see [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide*.
There are some considerations when using placement groups with Auto Scaling groups:
+ If a placement group is specified in both the launch template and the Auto Scaling group, the placement group for the Auto Scaling group takes precedence.
+ In CloudFormation, be careful if you define a placement group in the launch template. Amazon EC2 Auto Scaling will launch instances into the specified placement group. However, CloudFormation will not receive signals from those instances if you use an [UpdatePolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html) with your Auto Scaling group (though this could change in the future).

**Purchasing option**
You can choose **Request Spot Instances** to request Spot Instances at the Spot price, capped at the On-Demand price, and choose **Customize** to change the default Spot Instance settings. For an Auto Scaling group, you must specify a one-time request with no end date (the default). For more information, see [Request Spot Instances for fault-tolerant and flexible applications](launch-template-spot-instances.md). This setting may be useful in special circumstances, but in general it's best to leave it unspecified and create a mixed instances group instead. For more information, see [Auto Scaling groups with multiple instance types and purchase options](ec2-auto-scaling-mixed-instances-groups.md).
If you specify a Spot Instance request in your launch template, you can't create a mixed instances group. If you try to use a launch template that requests Spot Instances with a mixed instances group, you receive the following error message: `Incompatible launch template: You cannot use a launch template that is set to request Spot Instances (InstanceMarketOptions) when you configure an Auto Scaling group with a mixed instances policy. Add a different launch template to the group and try again.`

**Capacity Reservation**
Capacity Reservations allow you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration. For more information, see [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*.
You can choose whether to launch instances into:
+ any open Capacity Reservation (**Open**)
+ a specific Capacity Reservation (**Target by ID**)
+ a group of Capacity Reservations (**Target by group**)
To target a specific Capacity Reservation, the instance type in your launch template must match the instance type of the reservation. When you create your Auto Scaling group, use the same Availability Zone as the Capacity Reservation. Depending on the AWS Region you choose, you can choose to target a Capacity Block instead. For more information, see [Use Capacity Blocks for machine learning workloads](launch-template-capacity-blocks.md).
To target a group of Capacity Reservations, see [Reserve capacity in specific Availability Zones with Capacity Reservations](use-ec2-capacity-reservations.md). By targeting a group of Capacity Reservations, you can have capacity distributed across multiple Availability Zones to improve resiliency.

**Tenancy**
Amazon EC2 provides three options for the tenancy of your EC2 instances:
+ Shared (**Shared**) – Multiple AWS accounts may share the same physical hardware. This is the default tenancy option when launching an instance.
+ Dedicated instances (**Dedicated**) – Your instance runs on single-tenant hardware. No other AWS customer shares the same physical server. For more information, see [Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html) in the *Amazon EC2 User Guide*.
+ Dedicated Hosts (**Dedicated host**) – The instance runs on a physical server that is dedicated to your use. Using Dedicated Hosts makes it easier to bring your own licenses (BYOL) that have dedicated hardware requirements to EC2 and meet compliance use cases. If you choose this option, you must provide a host resource group for **Tenancy host resource group**. For more information, see [Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html) in the *Amazon EC2 User Guide*.
Support for Dedicated Hosts is only available if you specify a host resource group. You can't target a specific host ID or use host placement affinity.
+ If you try to use a launch template that specifies a host ID, you receive the following error message: `Incompatible launch template: Tenancy host ID is not supported for Auto Scaling.`
+ If you try to use a launch template that specifies host placement affinity, you receive the following error message: `Incompatible launch template: Auto Scaling does not support host placement affinity.`

**Tenancy host resource group**
With AWS License Manager, you can bring your own licenses to AWS and manage them centrally. A host resource group is a group of Dedicated Hosts that are linked to a specific License Manager license configuration. Host resource groups allow you to easily launch EC2 instances onto Dedicated Hosts that match your software licensing needs. You do not need to manually allocate Dedicated Hosts ahead of time. They are automatically created as needed. Note that when you associate an AMI with a license configuration, that AMI can only be associated with one host resource group at a time. For more information, see [Host resource groups in AWS License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-groups.html) in the *License Manager User Guide*.

**License configurations**
With this setting, you can specify a license configuration for your instances without restricting their tenancy to Dedicated Hosts. The license configuration tracks the software licenses deployed on the instances so you can monitor your license usage and compliance. For more information, see [Create a self-managed license](https://docs.aws.amazon.com/license-manager/latest/userguide/create-license-configuration.html) in the *License Manager User Guide*.

**Metadata accessible**
You can choose whether to enable or disable access to the HTTP endpoint of the instance metadata service. By default, the HTTP endpoint is enabled. If you choose to disable the endpoint, access to your instance metadata is turned off. You can specify the condition to require IMDSv2 only when the HTTP endpoint is enabled. For more information, see [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the *Amazon EC2 User Guide*.

**Metadata version**
You can choose to require the use of Instance Metadata Service Version 2 (IMDSv2) when requesting instance metadata. If you do not specify a value, the default is to support both IMDSv1 and IMDSv2. For more information, see [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the *Amazon EC2 User Guide*.

**Metadata token response hop limit**
You can set the allowable number of network hops for the metadata token. If you do not specify a value, the default is 1. For more information, see [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the *Amazon EC2 User Guide*.

**User data**
You can customize and finish configuring your instances at launch time by specifying shell scripts or cloud-init directives as user data. The user data runs when the instance initially starts up, allowing you to automatically install applications, dependencies, or customizations at launch time. For more information, see [Run commands on your Linux instance at launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) in the *Amazon EC2 User Guide*.
If you have large downloads or complex scripts, this adds to the time it takes for the instance to become ready for use. In which case, you may need to configure a lifecycle hook to delay an instance from reaching the `InService` state until it's fully provisioned. For more information about adding a lifecycle hook to your Auto Scaling group, see [Amazon EC2 Auto Scaling lifecycle hooks](lifecycle-hooks.md).
