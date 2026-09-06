---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_Fleet.html
---

# Fleet
<a name="API_Fleet"></a>

Describes a fleet.

## Contents
<a name="API_Fleet_Contents"></a>

 ** Arn **   <a name="WorkSpacesApplications-Type-Fleet-Arn"></a>
The Amazon Resource Name (ARN) for the fleet.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** ComputeCapacityStatus **   <a name="WorkSpacesApplications-Type-Fleet-ComputeCapacityStatus"></a>
The capacity status for the fleet.
Type: [ComputeCapacityStatus](API_ComputeCapacityStatus.md) object
Required: Yes

 ** InstanceType **   <a name="WorkSpacesApplications-Type-Fleet-InstanceType"></a>
The instance type to use when launching fleet instances. The following instance types are available:
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
Required: Yes

 ** Name **   <a name="WorkSpacesApplications-Type-Fleet-Name"></a>
The name of the fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** State **   <a name="WorkSpacesApplications-Type-Fleet-State"></a>
The current state for the fleet.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED`
Required: Yes

 ** CreatedTime **   <a name="WorkSpacesApplications-Type-Fleet-CreatedTime"></a>
The time the fleet was created.
Type: Timestamp
Required: No

 ** Description **   <a name="WorkSpacesApplications-Type-Fleet-Description"></a>
The description to display.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** DisableIMDSV1 **   <a name="WorkSpacesApplications-Type-Fleet-DisableIMDSV1"></a>
Indicates whether Instance Metadata Service Version 1 (IMDSv1) is disabled for the fleet.
Type: Boolean
Required: No

 ** DisconnectTimeoutInSeconds **   <a name="WorkSpacesApplications-Type-Fleet-DisconnectTimeoutInSeconds"></a>
The amount of time that a streaming session remains active after users disconnect. If they try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.
Specify a value between 60 and 36000.
Type: Integer
Required: No

 ** DisplayName **   <a name="WorkSpacesApplications-Type-Fleet-DisplayName"></a>
The fleet name to display.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** DomainJoinInfo **   <a name="WorkSpacesApplications-Type-Fleet-DomainJoinInfo"></a>
The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain.
Type: [DomainJoinInfo](API_DomainJoinInfo.md) object
Required: No

 ** EnableDefaultInternetAccess **   <a name="WorkSpacesApplications-Type-Fleet-EnableDefaultInternetAccess"></a>
Indicates whether default internet access is enabled for the fleet.
Type: Boolean
Required: No

 ** FleetErrors **   <a name="WorkSpacesApplications-Type-Fleet-FleetErrors"></a>
The fleet errors.
Type: Array of [FleetError](API_FleetError.md) objects
Required: No

 ** FleetType **   <a name="WorkSpacesApplications-Type-Fleet-FleetType"></a>
The fleet type.
ALWAYS\_ON
Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.
ON\_DEMAND
Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.
Type: String
Valid Values: `ALWAYS_ON | ON_DEMAND | ELASTIC`
Required: No

 ** IamRoleArn **   <a name="WorkSpacesApplications-Type-Fleet-IamRoleArn"></a>
The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet instance calls the AWS Security Token Service (STS) `AssumeRole` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the **appstream\_machine\_role** credential profile on the instance.
For more information, see [Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html) in the *Amazon WorkSpaces Applications Administration Guide*.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** IdleDisconnectTimeoutInSeconds **   <a name="WorkSpacesApplications-Type-Fleet-IdleDisconnectTimeoutInSeconds"></a>
The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the `DisconnectTimeoutInSeconds` time interval begins. Users are notified before they are disconnected due to inactivity. If users try to reconnect to the streaming session before the time interval specified in `DisconnectTimeoutInSeconds` elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in `IdleDisconnectTimeoutInSeconds` elapses, they are disconnected.
To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 36000. The default value is 0.
If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity.
Type: Integer
Required: No

 ** ImageArn **   <a name="WorkSpacesApplications-Type-Fleet-ImageArn"></a>
The ARN for the public, private, or shared image.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** ImageName **   <a name="WorkSpacesApplications-Type-Fleet-ImageName"></a>
The name of the image used to create the fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** MaxConcurrentSessions **   <a name="WorkSpacesApplications-Type-Fleet-MaxConcurrentSessions"></a>
The maximum number of concurrent sessions for the fleet.
Type: Integer
Required: No

 ** MaxSessionsPerInstance **   <a name="WorkSpacesApplications-Type-Fleet-MaxSessionsPerInstance"></a>
The maximum number of user sessions on an instance. This only applies to multi-session fleets.
Type: Integer
Required: No

 ** MaxUserDurationInSeconds **   <a name="WorkSpacesApplications-Type-Fleet-MaxUserDurationInSeconds"></a>
The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.
Specify a value between 600 and 360000.
Type: Integer
Required: No

 ** Platform **   <a name="WorkSpacesApplications-Type-Fleet-Platform"></a>
The platform of the fleet.
Type: String
Valid Values: `WINDOWS | WINDOWS_SERVER_2016 | WINDOWS_SERVER_2019 | WINDOWS_SERVER_2022 | WINDOWS_SERVER_2025 | WINDOWS_11 | AMAZON_LINUX2 | RHEL8 | ROCKY_LINUX8 | UBUNTU_PRO_2404`
Required: No

 ** RootVolumeConfig **   <a name="WorkSpacesApplications-Type-Fleet-RootVolumeConfig"></a>
The current configuration of the root volume for fleet instances, including the storage size in GB.
Type: [VolumeConfig](API_VolumeConfig.md) object
Required: No

 ** SessionScriptS3Location **   <a name="WorkSpacesApplications-Type-Fleet-SessionScriptS3Location"></a>
The S3 location of the session scripts configuration zip file. This only applies to Elastic fleets.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** StreamView **   <a name="WorkSpacesApplications-Type-Fleet-StreamView"></a>
The WorkSpaces Applications view that is displayed to your users when they stream from the fleet. When `APP` is specified, only the windows of applications opened by users display. When `DESKTOP` is specified, the standard desktop that is provided by the operating system displays.
The default value is `APP`.
Type: String
Valid Values: `APP | DESKTOP`
Required: No

 ** UsbDeviceFilterStrings **   <a name="WorkSpacesApplications-Type-Fleet-UsbDeviceFilterStrings"></a>
The USB device filter strings associated with the fleet.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `^((\w*)\s*(\w*)\s*\,\s*(\w*)\s*\,\s*\*?(\w*)\s*\,\s*\*?(\w*)\s*\,\s*\*?\d*\s*\,\s*\*?\d*\s*\,\s*[0-1]\s*\,\s*[0-1]\s*)$`
Required: No

 ** VpcConfig **   <a name="WorkSpacesApplications-Type-Fleet-VpcConfig"></a>
The VPC configuration for the fleet.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_Fleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/Fleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/Fleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/Fleet)
