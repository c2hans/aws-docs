---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ImageBuilder.html
---

# ImageBuilder
<a name="API_ImageBuilder"></a>

Describes a virtual machine that is used to create an image.

## Contents
<a name="API_ImageBuilder_Contents"></a>

 ** Name **   <a name="WorkSpacesApplications-Type-ImageBuilder-Name"></a>
The name of the image builder.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** AccessEndpoints **   <a name="WorkSpacesApplications-Type-ImageBuilder-AccessEndpoints"></a>
The list of virtual private cloud (VPC) interface endpoint objects. Administrators can connect to the image builder only through the specified endpoints.
Type: Array of [AccessEndpoint](API_AccessEndpoint.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: No

 ** AppstreamAgentVersion **   <a name="WorkSpacesApplications-Type-ImageBuilder-AppstreamAgentVersion"></a>
The version of the WorkSpaces Applications agent that is currently being used by the image builder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Arn **   <a name="WorkSpacesApplications-Type-ImageBuilder-Arn"></a>
The ARN for the image builder.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** CreatedTime **   <a name="WorkSpacesApplications-Type-ImageBuilder-CreatedTime"></a>
The time stamp when the image builder was created.
Type: Timestamp
Required: No

 ** Description **   <a name="WorkSpacesApplications-Type-ImageBuilder-Description"></a>
The description to display.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** DisableIMDSV1 **   <a name="WorkSpacesApplications-Type-ImageBuilder-DisableIMDSV1"></a>
Indicates whether Instance Metadata Service Version 1 (IMDSv1) is disabled for the image builder.
Type: Boolean
Required: No

 ** DisplayName **   <a name="WorkSpacesApplications-Type-ImageBuilder-DisplayName"></a>
The image builder name to display.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** DomainJoinInfo **   <a name="WorkSpacesApplications-Type-ImageBuilder-DomainJoinInfo"></a>
The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.
Type: [DomainJoinInfo](API_DomainJoinInfo.md) object
Required: No

 ** EnableDefaultInternetAccess **   <a name="WorkSpacesApplications-Type-ImageBuilder-EnableDefaultInternetAccess"></a>
Enables or disables default internet access for the image builder.
Type: Boolean
Required: No

 ** IamRoleArn **   <a name="WorkSpacesApplications-Type-ImageBuilder-IamRoleArn"></a>
The ARN of the IAM role that is applied to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) `AssumeRole` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the **appstream\_machine\_role** credential profile on the instance.
For more information, see [Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html) in the *Amazon WorkSpaces Applications Administration Guide*.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** ImageArn **   <a name="WorkSpacesApplications-Type-ImageBuilder-ImageArn"></a>
The ARN of the image from which this builder was created.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** ImageBuilderErrors **   <a name="WorkSpacesApplications-Type-ImageBuilder-ImageBuilderErrors"></a>
The image builder errors.
Type: Array of [ResourceError](API_ResourceError.md) objects
Required: No

 ** InstanceType **   <a name="WorkSpacesApplications-Type-ImageBuilder-InstanceType"></a>
The instance type for the image builder. The following instance types are available:
+ stream.standard.small
+ stream.standard.medium
+ stream.standard.large
+ stream.compute.large
+ stream.compute.xlarge
+ stream.compute.2xlarge
+ stream.compute.4xlarge
+ stream.compute.8xlarge
+ stream.memory.large
+ stream.memory.xlarge
+ stream.memory.2xlarge
+ stream.memory.4xlarge
+ stream.memory.8xlarge
+ stream.memory.z1d.large
+ stream.memory.z1d.xlarge
+ stream.memory.z1d.2xlarge
+ stream.memory.z1d.3xlarge
+ stream.memory.z1d.6xlarge
+ stream.memory.z1d.12xlarge
+ stream.graphics.g4dn.xlarge
+ stream.graphics.g4dn.2xlarge
+ stream.graphics.g4dn.4xlarge
+ stream.graphics.g4dn.8xlarge
+ stream.graphics.g4dn.12xlarge
+ stream.graphics.g4dn.16xlarge
+ stream.graphics.g5.xlarge
+ stream.graphics.g5.2xlarge
+ stream.graphics.g5.4xlarge
+ stream.graphics.g5.8xlarge
+ stream.graphics.g5.16xlarge
+ stream.graphics.g5.12xlarge
+ stream.graphics.g5.24xlarge
+ stream.graphics.g6.xlarge
+ stream.graphics.g6.2xlarge
+ stream.graphics.g6.4xlarge
+ stream.graphics.g6.8xlarge
+ stream.graphics.g6.16xlarge
+ stream.graphics.g6.12xlarge
+ stream.graphics.g6.24xlarge
+ stream.graphics.gr6.4xlarge
+ stream.graphics.gr6.8xlarge
+ stream.graphics.g6f.large
+ stream.graphics.g6f.xlarge
+ stream.graphics.g6f.2xlarge
+ stream.graphics.g6f.4xlarge
+ stream.graphics.gr6f.4xlarge
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** LatestAppstreamAgentVersion **   <a name="WorkSpacesApplications-Type-ImageBuilder-LatestAppstreamAgentVersion"></a>
Indicates whether the image builder is using the latest WorkSpaces Applications agent version or not.
Type: String
Valid Values: `TRUE | FALSE`
Required: No

 ** NetworkAccessConfiguration **   <a name="WorkSpacesApplications-Type-ImageBuilder-NetworkAccessConfiguration"></a>
Describes the network details of the fleet or image builder instance.
Type: [NetworkAccessConfiguration](API_NetworkAccessConfiguration.md) object
Required: No

 ** Platform **   <a name="WorkSpacesApplications-Type-ImageBuilder-Platform"></a>
The operating system platform of the image builder.
Type: String
Valid Values: `WINDOWS | WINDOWS_SERVER_2016 | WINDOWS_SERVER_2019 | WINDOWS_SERVER_2022 | WINDOWS_SERVER_2025 | WINDOWS_11 | AMAZON_LINUX2 | RHEL8 | ROCKY_LINUX8 | UBUNTU_PRO_2404`
Required: No

 ** RootVolumeConfig **   <a name="WorkSpacesApplications-Type-ImageBuilder-RootVolumeConfig"></a>
The current configuration of the root volume for the image builder, including the storage size in GB.
Type: [VolumeConfig](API_VolumeConfig.md) object
Required: No

 ** State **   <a name="WorkSpacesApplications-Type-ImageBuilder-State"></a>
The state of the image builder.
Type: String
Valid Values: `PENDING | UPDATING_AGENT | RUNNING | STOPPING | STOPPED | REBOOTING | SNAPSHOTTING | DELETING | FAILED | UPDATING | PENDING_QUALIFICATION | PENDING_SYNCING_APPS | SYNCING_APPS | PENDING_IMAGE_IMPORT`
Required: No

 ** StateChangeReason **   <a name="WorkSpacesApplications-Type-ImageBuilder-StateChangeReason"></a>
The reason why the last state change occurred.
Type: [ImageBuilderStateChangeReason](API_ImageBuilderStateChangeReason.md) object
Required: No

 ** VpcConfig **   <a name="WorkSpacesApplications-Type-ImageBuilder-VpcConfig"></a>
The VPC configuration of the image builder.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_ImageBuilder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ImageBuilder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ImageBuilder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ImageBuilder)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
