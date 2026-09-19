---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html
---

# Create a launch template for an Auto Scaling group
<a name="create-launch-template"></a>

Before you can create an Auto Scaling group using a launch template, you must create a launch template that contains the configuration information to launch an instance, including the ID of the Amazon Machine Image (AMI).

To create new launch templates, use the following procedures.

**Contents**
+ [Create your launch template (console)](#create-launch-template-for-auto-scaling)
+ [Change the default network interface settings (console)](#change-network-interface)
+ [Modify the storage configuration (console)](#modify-storage-configuration)
+ [Create a launch template from an existing instance (console)](#create-launch-template-from-instance)
+ [Related resources](#create-launch-template-related-resources)
+ [Limitations](#create-launch-template-limitations)

**Important**
Launch template parameters are not fully validated when you create the launch template. If you specify incorrect values for parameters, or if you do not use supported parameter combinations, no instances can launch using this launch template. Be sure to specify the correct values for the parameters and use supported parameter combinations. For example, to launch instances with an Arm-based AWS Graviton or Graviton2 AMI, you must specify an Arm-compatible instance type. For more information, see [Launch template restrictions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-template-restrictions.html) in the *Amazon EC2 User Guide*.

## Create your launch template (console)
<a name="create-launch-template-for-auto-scaling"></a>

The following steps describe how to configure a basic launch template:
+ Specify the Amazon Machine Image (AMI) from which to launch the instances.
+ Choose an instance type that is compatible with the AMI that you specify.
+ Specify the key pair to use when connecting to instances, for example, using SSH.
+ Add one or more security groups to allow network access to the instances.
+ Specify whether to attach additional volumes to each instance.
+ Add custom tags (key-value pairs) to the instances and volumes.

**To create a launch template**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, under **Instances**, choose **Launch Templates**.

1. Choose **Create launch template**. Enter a name and provide a description for the initial version of the launch template.

1. (Optional) Under **Auto Scaling guidance**, select the check box to have Amazon EC2 provide guidance to help create a template to use with Amazon EC2 Auto Scaling.

1. Under **Launch template contents**, fill out each required field and any optional fields as needed.

   1. **Application and OS Images (Amazon Machine Image)**: (Required) Choose the ID of the AMI for your instances. You can search through all available AMIs, or select an AMI from the **Recents** or **Quick Start** list. If you don't see the AMI that you need, choose **Browse more AMIs** to browse the full AMI catalog.

      To choose a custom AMI, you must first create your AMI from a customized instance. For more information, see [Create an Amazon EBS-backed AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html) in the *Amazon EC2 User Guide*.

   1. For **Instance type**, choose a single instance type that's compatible with the AMI that you specified.

      Alternatively, to use attribute-based instance type selection, choose **Advanced**, **Specify instance type attributes**, and then specify the following options:
      + **Number of vCPUs**: Enter the minimum and maximum number of vCPUs. To indicate no limits, enter a minimum of 0, and keep the maximum blank.
      + **Amount of memory (MiB)**: Enter the minimum and maximum amount of memory, in MiB. To indicate no limits, enter a minimum of 0, and keep the maximum blank.
      + Expand **Optional instance type attributes** and choose **Add attribute** to further limit the types of instances that can be used to fulfill your desired capacity. For information about each attribute, see [InstanceRequirementsRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceRequirementsRequest.html) in the *Amazon EC2 API Reference*.
      + **Resulting instance types**: You can view the instance types that match the specified compute requirements, such as vCPUs, memory, and storage.
      + To exclude instance types, choose **Add attribute**. From the **Attribute** list, choose **Excluded instance types**. From the **Attribute value** list, select the instance types to exclude.

   1. **Key pair (login)**: For **Key pair name**, choose an existing key pair, or choose **Create new key pair** to create a new one. For more information, see [Amazon EC2 key pairs and Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon EC2 User Guide*.

   1. **Network settings**: For **Firewall (security groups)**, use one or more security groups, or keep this blank and configure one or more security groups as part of the network interface. For more information, see [Amazon EC2 security groups for Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) in the *Amazon EC2 User Guide*.

      If you don't specify any security groups in your launch template, Amazon EC2 uses the default security group for the VPC that your Auto Scaling group will launch instances into. By default, this security group doesn't allow inbound traffic from external networks. For more information, see [Default security groups for your VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/default-security-group.html) in the *Amazon VPC User Guide*.

   1. Do one of the following:
      + Change the default network interface settings. For example, you can enable or disable the public IPv4 addressing feature, which overrides the auto-assign public IPv4 addresses setting on the subnet. For more information, see [Change the default network interface settings (console)](#change-network-interface).
      + Skip this step to keep the default network interface settings.

   1. Do one of the following:
      + Modify the storage configuration. For more information, see [Modify the storage configuration (console)](#modify-storage-configuration).
      + Skip this step to keep the default storage configuration.

   1. For **Resource tags**, specify tags by providing key and value combinations. If you specify instance tags in your launch template and then you choose to propagate your Auto Scaling group's tags to its instances, all the tags are merged. If the same tag key is specified for a tag in your launch template and a tag in your Auto Scaling group, then the tag value from the group takes precedence.

1. (Optional) Configure advanced settings. For example, you can choose an IAM role that your application can use when it accesses other AWS resources or specify the instance user data that can be used to perform common automated configuration tasks after an instance starts. For more information, see [Create a launch template using advanced settings](advanced-settings-for-your-launch-template.md).

1. When you are ready to create the launch template, choose **Create launch template**.

1. To create an Auto Scaling group, choose **Create Auto Scaling group** from the confirmation page.

## Change the default network interface settings (console)
<a name="change-network-interface"></a>

Network interfaces provide connectivity to other resources in your VPC and the internet. For more information, see [Provide network connectivity for your Auto Scaling instances using Amazon VPC](asg-in-vpc.md).

This section shows you how to change the default network interface settings. For example, you can define whether you want to assign a public IPv4 address to each instance instead of defaulting to the auto-assign public IPv4 addresses setting on the subnet.

**Considerations and limitations**

When changing the default network interface settings, keep in mind the following considerations and limitations:
+ You must configure the security groups as part of the network interface, not in the **Security groups** section of the template. You cannot specify security groups in both places.
+ If you specify any existing network interface IDs, you can launch only one instance. This is because a network interface can be attached to only one instance at a time. To do this, you must use the AWS CLI or an SDK to create the Auto Scaling group. When you create the group, specify a single Availability Zone, but not a subnet ID.

  You must include one existing network interface with a device index of 0. You can optionally add secondary existing network interfaces. The maximum number of network interfaces depends on the instance type. All specified network interfaces must be in the Availability Zone that you configure for the Auto Scaling group. The interfaces can be in different subnets, as long as each subnet is in that Availability Zone.
+ You cannot auto-assign a public IPv4 address if you specify more than one network interface. You also cannot specify duplicate device indexes across network interfaces. Both the primary and secondary network interfaces reside in the same subnet.
+ When an instance launches, a private address is automatically allocated to each network interface. The address comes from the CIDR range of the subnet in which the instance is launched. For information on specifying CIDR blocks (or IP address ranges) for your VPC or subnet, see the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/).

**To change the default network interface settings**

1. Under **Network settings**, expand **Advanced network configuration**.

1. Choose **Add network interface** to configure the primary network interface, paying attention to the following fields:

   1. **Device index**: Keep the default value, 0, to apply your changes to the primary network interface (eth0).

   1. **Network interface**: Keep the default value, **New interface**, to have Amazon EC2 Auto Scaling automatically create a new network interface when an instance is launched. Alternatively, you can choose an existing, available network interface with a device index of 0, but this limits your Auto Scaling group to one instance.

   1. **Description**: (Optional) Enter a descriptive name.

   1. **Subnet**: Keep the default **Don't include in launch template** setting.

      If the AMI specifies a subnet for the network interface, this results in an error. We recommend turning off **Auto Scaling guidance** as a workaround. After you make this change, you will not receive an error message. However, regardless of where the subnet is specified, the subnet settings of the Auto Scaling group take precedence and cannot be overridden.

   1. **Auto-assign public IP**: Change whether your network interface with a device index of 0 receives a public IPv4 address. By default, instances in a default subnet receive a public IPv4 address, while instances in a nondefault subnet do not. Select **Enable** or **Disable** to override the subnet's default setting.

   1. **Security groups**: Choose one or more security groups for the network interface. Each security group must be configured for the VPC that your Auto Scaling group will launch instances into. For more information, see [Amazon EC2 security groups for Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) in the *Amazon EC2 User Guide*.

   1. **Delete on termination**: Choose **Yes** to delete the network interface when the instance is terminated, or choose **No** to keep the network interface.

   1. **Elastic Fabric Adapter**: To support high performance computing and machine learning use cases, change the network interface into an Elastic Fabric Adapter network interface. For more information, see [Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) in the *Amazon EC2 User Guide*.

   1. **Network card index**: Choose **0** to attach the primary network interface to the network card with a device index of 0. If this option isn't available, keep the default value, **Don't include in launch template**. Attaching the network interface to a specific network card is available only for supported instance types. For more information, see [Network cards](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#network-cards) in the *Amazon EC2 User Guide*.

   1. **ENA Express**: For instance types that support ENA Express, choose **Enable** to enable ENA Express or **Disable** to disable it. For more information, see [Improve network performance with ENA Express on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express.html) in the *Amazon EC2 User Guide*.

   1. **ENA Express UDP**: If you enable **ENA Express**, you can optionally use it for UDP traffic. Choose **Enable** to enable ENA Express UDP or **Disable** to disable it.

1. To add a secondary network interface, choose **Add network interface**.

## Modify the storage configuration (console)
<a name="modify-storage-configuration"></a>

You can modify the storage configuration for instances launched from an Amazon EBS-backed AMI or an instance store-backed AMI. You can also specify additional EBS volumes to attach to the instances. The AMI includes one or more volumes of storage, including the root volume (**Volume 1 (AMI Root)**).

**To modify the storage configuration**

1. In **Configure storage**, modify the size or type of volume.

   If the value you specify for volume size is outside the limits of the volume type, or smaller than the snapshot size, an error message is displayed. To help you address the issue, this message gives the minimum or maximum value that the field can accept.

   Only volumes associated with an Amazon EBS-backed AMI appear. To display information about the storage configuration for an instance launched from an instance store-backed AMI, choose **Show details** from the **Instance store volumes** section.

   To specify all EBS volume parameters, switch to the **Advanced** view in the top right corner.

1. For advanced options, expand the volume that you want to modify and configure the volume as follows:

   1. **Storage type**: The type of volume (EBS or ephemeral) to associate with your instance. The instance store (ephemeral) volume type is only available if you select an instance type that supports it. For more information, see [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html) in the *Amazon EBS User Guide* and [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide*.

   1. **Device name**: Select from the list of available device names for the volume.

   1. **Snapshot**: Select the snapshot from which to create the volume. You can search for available shared and public snapshots by entering text into the **Snapshot** field.

   1. **Size (GiB)**: For EBS volumes, you can specify a storage size. If you have selected an AMI and instance that are eligible for the free tier, keep in mind that to stay within the free tier, you must stay under 30 GiB of total storage. For more information, see [Constraints on the size and configuration of an EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/volume_constraints.html) in the *Amazon EBS User Guide*.

   1. **Volume type**: For EBS volumes, choose the volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide*.

   1. **IOPS**: If you have selected a Provisioned IOPS SSD (`io1` and `io2`) or General Purpose SSD (`gp3`) volume type, then you can enter the number of I/O operations per second (IOPS) that the volume can support. This is required for io1, io2, and gp3 volumes. It is not supported for gp2, st1, sc1, or standard volumes.

   1. **Delete on termination**: For EBS volumes, choose **Yes** to delete the volume when the instance is terminated, or choose **No** to keep the volume.

   1. **Encrypted**: If the instance type supports EBS encryption, you can choose **Yes** to enable encryption for the volume. If you have enabled encryption by default in this Region, encryption is enabled for you. For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) and [Enable Amazon EBS encryption by default](https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html) in the *Amazon EBS User Guide*.

      The default effect of setting this parameter varies with the choice of volume source, as described in the following table. In all cases, you must have permission to use the specified AWS KMS key.

**Encryption outcomes**

<table>
<thead>
  <tr><th> If <code>Encrypted</code> parameter is set to...</th><th>And if source of volume is...</th><th>Then the default encryption state is...</th><th>Notes</th></tr>
</thead>
<tbody>
  <tr><td rowspan="5">No</td><td>New (empty) volume</td><td>Unencrypted*</td><td rowspan="5">N/A</td></tr>
  <tr><td>Unencrypted snapshot that you own</td><td>Unencrypted*</td></tr>
  <tr><td>Encrypted snapshot that you own</td><td>Encrypted by same key</td></tr>
  <tr><td>Unencrypted snapshot that is shared with you</td><td>Unencrypted*</td></tr>
  <tr><td>Encrypted snapshot that is shared with you</td><td>Encrypted by default KMS key</td></tr>
  <tr><td rowspan="5">Yes</td><td>New volume</td><td>Encrypted by default KMS key</td><td rowspan="5">To use a non-default KMS key, specify a value for the <b>KMS key</b> parameter. </td></tr>
  <tr><td>Unencrypted snapshot that you own</td><td>Encrypted by default KMS key</td></tr>
  <tr><td>Encrypted snapshot that you own</td><td>Encrypted by same key</td></tr>
  <tr><td>Unencrypted snapshot that is shared with you</td><td>Encrypted by default KMS key</td></tr>
  <tr><td>Encrypted snapshot that is shared with you</td><td>Encrypted by default KMS key</td></tr>
</tbody>
</table>

      \* If encryption by default is enabled, all newly created volumes (whether or not the **Encrypted** parameter is set to **Yes**) are encrypted using the default KMS key. If you set both the **Encrypted** and **KMS key** parameters, then you can specify a non-default KMS key.

   1. **KMS key**: If you chose **Yes** for **Encrypted**, then you must select a customer managed key to use to encrypt the volume. If you have enabled encryption by default in this Region, the default customer managed key is selected for you. You can select a different key or specify the ARN of any customer managed key that you previously created using the AWS Key Management Service.

1. To specify additional volumes to attach to the instances launched by this launch template, choose **Add new volume**.

## Create a launch template from an existing instance (console)
<a name="create-launch-template-from-instance"></a>

**To create a launch template from an existing instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, under **Instances**, choose **Instances**.

1. Select the instance and choose **Actions**, **Image and templates**, **Create template from instance**.

1. Provide a name and description.

1. Under **Auto Scaling guidance**, select the check box.

1. Adjust any settings as required, and choose **Create launch template**.

1. To create an Auto Scaling group, choose **Create Auto Scaling group** from the confirmation page.

## Related resources
<a name="create-launch-template-related-resources"></a>

We provide a few JSON and YAML template snippets that you can use to understand how to declare launch templates in your CloudFormation stack templates. For more information, see the [AWS::EC2::LaunchTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html) and [Create launch templates with CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2-launch-templates.html) sections of the *AWS CloudFormation User Guide*.

For more information about launch templates, see [Launching an instance from a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.

## Limitations
<a name="create-launch-template-limitations"></a>
+ While you can specify a subnet in a launch template, doing so isn't necessary if you only use the launch template to create Auto Scaling groups. You can't specify the subnet for an Auto Scaling group by specifying the subnet in a launch template. The subnets for the Auto Scaling group are taken from the Auto Scaling group's own resource definition.
+ For other limitations on user-defined network interfaces, see [Change the default network interface settings (console)](#change-network-interface).
