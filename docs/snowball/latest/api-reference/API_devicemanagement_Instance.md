---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_Instance.html
---

# Instance
<a name="API_devicemanagement_Instance"></a>

The description of an instance. Currently, Amazon EC2 instances are the only supported instance type.

## Contents
<a name="API_devicemanagement_Instance_Contents"></a>

 ** amiLaunchIndex **   <a name="Snowball-Type-devicemanagement_Instance-amiLaunchIndex"></a>
The Amazon Machine Image (AMI) launch index, which you can use to find this instance in the launch group.
Type: Integer
Required: No

 ** blockDeviceMappings **   <a name="Snowball-Type-devicemanagement_Instance-blockDeviceMappings"></a>
Any block device mapping entries for the instance.
Type: Array of [InstanceBlockDeviceMapping](API_devicemanagement_InstanceBlockDeviceMapping.md) objects
Required: No

 ** cpuOptions **   <a name="Snowball-Type-devicemanagement_Instance-cpuOptions"></a>
The CPU options for the instance.
Type: [CpuOptions](API_devicemanagement_CpuOptions.md) object
Required: No

 ** createdAt **   <a name="Snowball-Type-devicemanagement_Instance-createdAt"></a>
When the instance was created.
Type: Timestamp
Required: No

 ** imageId **   <a name="Snowball-Type-devicemanagement_Instance-imageId"></a>
The ID of the AMI used to launch the instance.
Type: String
Required: No

 ** instanceId **   <a name="Snowball-Type-devicemanagement_Instance-instanceId"></a>
The ID of the instance.
Type: String
Required: No

 ** instanceType **   <a name="Snowball-Type-devicemanagement_Instance-instanceType"></a>
The instance type.
Type: String
Required: No

 ** privateIpAddress **   <a name="Snowball-Type-devicemanagement_Instance-privateIpAddress"></a>
The private IPv4 address assigned to the instance.
Type: String
Required: No

 ** publicIpAddress **   <a name="Snowball-Type-devicemanagement_Instance-publicIpAddress"></a>
The public IPv4 address assigned to the instance.
Type: String
Required: No

 ** rootDeviceName **   <a name="Snowball-Type-devicemanagement_Instance-rootDeviceName"></a>
The device name of the root device volume (for example, `/dev/sda1`).
Type: String
Required: No

 ** securityGroups **   <a name="Snowball-Type-devicemanagement_Instance-securityGroups"></a>
The security groups for the instance.
Type: Array of [SecurityGroupIdentifier](API_devicemanagement_SecurityGroupIdentifier.md) objects
Required: No

 ** state **   <a name="Snowball-Type-devicemanagement_Instance-state"></a>
The description of the current state of an instance.
Type: [InstanceState](API_devicemanagement_InstanceState.md) object
Required: No

 ** updatedAt **   <a name="Snowball-Type-devicemanagement_Instance-updatedAt"></a>
When the instance was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_devicemanagement_Instance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/Instance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/Instance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/Instance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
