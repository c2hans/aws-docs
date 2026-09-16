---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateFleet.html
---

# UpdateFleet
<a name="API_UpdateFleet"></a>

Updates the specified fleet.

If the fleet is in the `STOPPED` state, you can update any attribute except the fleet name.

If the fleet is in the `RUNNING` state, you can update the following based on the fleet type:
+ Always-On and On-Demand fleet types

  You can update the `DisplayName`, `ComputeCapacity`, `ImageARN`, `ImageName`, `IdleDisconnectTimeoutInSeconds`, and `RootVolumeConfig`, and `DisconnectTimeoutInSeconds` attributes.
+ Elastic fleet type

  You can update the `DisplayName`, `IdleDisconnectTimeoutInSeconds`, `DisconnectTimeoutInSeconds`, `MaxConcurrentSessions`, `SessionScriptS3Location` and `UsbDeviceFilterStrings` attributes.

If the fleet is in the `STARTING` or `STOPPED` state, you can't update it.

## Request Syntax
<a name="API_UpdateFleet_RequestSyntax"></a>

```
{
   "AttributesToDelete": [ "{{string}}" ],
   "ComputeCapacity": {
      "DesiredInstances": {{number}},
      "DesiredSessions": {{number}}
   },
   "DeleteVpcConfig": {{boolean}},
   "Description": "{{string}}",
   "DisableIMDSV1": {{boolean}},
   "DisconnectTimeoutInSeconds": {{number}},
   "DisplayName": "{{string}}",
   "DomainJoinInfo": {
      "DirectoryName": "{{string}}",
      "OrganizationalUnitDistinguishedName": "{{string}}"
   },
   "EnableDefaultInternetAccess": {{boolean}},
   "IamRoleArn": "{{string}}",
   "IdleDisconnectTimeoutInSeconds": {{number}},
   "ImageArn": "{{string}}",
   "ImageName": "{{string}}",
   "InstanceType": "{{string}}",
   "MaxConcurrentSessions": {{number}},
   "MaxSessionsPerInstance": {{number}},
   "MaxUserDurationInSeconds": {{number}},
   "Name": "{{string}}",
   "Platform": "{{string}}",
   "RootVolumeConfig": {
      "VolumeSizeInGb": {{number}}
   },
   "SessionScriptS3Location": {
      "S3Bucket": "{{string}}",
      "S3Key": "{{string}}"
   },
   "StreamView": "{{string}}",
   "UsbDeviceFilterStrings": [ "{{string}}" ],
   "VpcConfig": {
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_UpdateFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributesToDelete](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-AttributesToDelete"></a>
The fleet attributes to delete.
Type: Array of strings
Valid Values: `VPC_CONFIGURATION | VPC_CONFIGURATION_SECURITY_GROUP_IDS | DOMAIN_JOIN_INFO | IAM_ROLE_ARN | USB_DEVICE_FILTER_STRINGS | SESSION_SCRIPT_S3_LOCATION | MAX_SESSIONS_PER_INSTANCE | VOLUME_CONFIGURATION`
Required: No

 ** [ComputeCapacity](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-ComputeCapacity"></a>
The desired capacity for the fleet. This is not allowed for Elastic fleets.
Type: [ComputeCapacity](API_ComputeCapacity.md) object
Required: No

 ** [DeleteVpcConfig](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-DeleteVpcConfig"></a>
 *This parameter has been deprecated.*
Deletes the VPC association for the specified fleet.
Type: Boolean
Required: No

 ** [Description](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-Description"></a>
The description to display.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DisableIMDSV1](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-DisableIMDSV1"></a>
Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.
Before disabling IMDSv1, ensure your WorkSpaces Applications images are running the agent version or managed image update released on or after January 16, 2024 to support IMDSv2 enforcement.
Type: Boolean
Required: No

 ** [DisconnectTimeoutInSeconds](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-DisconnectTimeoutInSeconds"></a>
The amount of time that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.
Specify a value between 60 and 36000.
Type: Integer
Required: No

 ** [DisplayName](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-DisplayName"></a>
The fleet name to display.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [DomainJoinInfo](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-DomainJoinInfo"></a>
The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain.
Type: [DomainJoinInfo](API_DomainJoinInfo.md) object
Required: No

 ** [EnableDefaultInternetAccess](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-EnableDefaultInternetAccess"></a>
Enables or disables default internet access for the fleet.
Type: Boolean
Required: No

 ** [IamRoleArn](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-IamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to apply to the fleet. To assume a role, a fleet instance calls the AWS Security Token Service (STS) `AssumeRole` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the **appstream\_machine\_role** credential profile on the instance.
For more information, see [Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html) in the *Amazon WorkSpaces Applications Administration Guide*.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** [IdleDisconnectTimeoutInSeconds](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-IdleDisconnectTimeoutInSeconds"></a>
The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the `DisconnectTimeoutInSeconds` time interval begins. Users are notified before they are disconnected due to inactivity. If users try to reconnect to the streaming session before the time interval specified in `DisconnectTimeoutInSeconds` elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in `IdleDisconnectTimeoutInSeconds` elapses, they are disconnected.
To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 36000. The default value is 0.
If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity.
Type: Integer
Required: No

 ** [ImageArn](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-ImageArn"></a>
The ARN of the public, private, or shared image to use.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** [ImageName](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-ImageName"></a>
The name of the image used to create the fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [InstanceType](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-InstanceType"></a>
The instance type to use when launching fleet instances. The following instance types are available:
+ stream.standard.small
+ stream.standard.medium
+ stream.standard.large
+ stream.standard.xlarge
+ stream.standard.2xlarge
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
The following instance types are available for Elastic fleets:
+ stream.standard.small
+ stream.standard.medium
+ stream.standard.large
+ stream.standard.xlarge
+ stream.standard.2xlarge
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [MaxConcurrentSessions](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-MaxConcurrentSessions"></a>
The maximum number of concurrent sessions for a fleet.
Type: Integer
Required: No

 ** [MaxSessionsPerInstance](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-MaxSessionsPerInstance"></a>
The maximum number of user sessions on an instance. This only applies to multi-session fleets.
Type: Integer
Required: No

 ** [MaxUserDurationInSeconds](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-MaxUserDurationInSeconds"></a>
The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.
Specify a value between 600 and 432000.
Type: Integer
Required: No

 ** [Name](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-Name"></a>
A unique name for the fleet.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: No

 ** [Platform](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-Platform"></a>
The platform of the fleet. WINDOWS\_SERVER\_2019, AMAZON\_LINUX2 and UBUNTU\_PRO\_2404 are supported for Elastic fleets.
Type: String
Valid Values: `WINDOWS | WINDOWS_SERVER_2016 | WINDOWS_SERVER_2019 | WINDOWS_SERVER_2022 | WINDOWS_SERVER_2025 | WINDOWS_11 | AMAZON_LINUX2 | RHEL8 | ROCKY_LINUX8 | UBUNTU_PRO_2404`
Required: No

 ** [RootVolumeConfig](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-RootVolumeConfig"></a>
The updated configuration for the root volume of fleet instances. Note that volume size cannot be decreased below the image volume size.
Type: [VolumeConfig](API_VolumeConfig.md) object
Required: No

 ** [SessionScriptS3Location](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-SessionScriptS3Location"></a>
The S3 location of the session scripts configuration zip file. This only applies to Elastic fleets.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** [StreamView](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-StreamView"></a>
The WorkSpaces Applications view that is displayed to your users when they stream from the fleet. When `APP` is specified, only the windows of applications opened by users display. When `DESKTOP` is specified, the standard desktop that is provided by the operating system displays.
The default value is `APP`.
Type: String
Valid Values: `APP | DESKTOP`
Required: No

 ** [UsbDeviceFilterStrings](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-UsbDeviceFilterStrings"></a>
The USB device filter strings that specify which USB devices a user can redirect to the fleet streaming session, when using the Windows native client. This is allowed but not required for Elastic fleets.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `^((\w*)\s*(\w*)\s*\,\s*(\w*)\s*\,\s*\*?(\w*)\s*\,\s*\*?(\w*)\s*\,\s*\*?\d*\s*\,\s*\*?\d*\s*\,\s*[0-1]\s*\,\s*[0-1]\s*)$`
Required: No

 ** [VpcConfig](#API_UpdateFleet_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-request-VpcConfig"></a>
The VPC configuration for the fleet. This is required for Elastic fleets, but not required for other fleet types. Elastic fleets require that you specify at least two subnets in different availability zones.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateFleet_ResponseSyntax"></a>

```
{
   "Fleet": {
      "Arn": "string",
      "ComputeCapacityStatus": {
         "ActiveUserSessions": number,
         "ActualUserSessions": number,
         "Available": number,
         "AvailableUserSessions": number,
         "Desired": number,
         "DesiredUserSessions": number,
         "Draining": number,
         "DrainModeActiveUserSessions": number,
         "DrainModeUnusedUserSessions": number,
         "InUse": number,
         "Running": number
      },
      "CreatedTime": number,
      "Description": "string",
      "DisableIMDSV1": boolean,
      "DisconnectTimeoutInSeconds": number,
      "DisplayName": "string",
      "DomainJoinInfo": {
         "DirectoryName": "string",
         "OrganizationalUnitDistinguishedName": "string"
      },
      "EnableDefaultInternetAccess": boolean,
      "FleetErrors": [
         {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         }
      ],
      "FleetType": "string",
      "IamRoleArn": "string",
      "IdleDisconnectTimeoutInSeconds": number,
      "ImageArn": "string",
      "ImageName": "string",
      "InstanceType": "string",
      "MaxConcurrentSessions": number,
      "MaxSessionsPerInstance": number,
      "MaxUserDurationInSeconds": number,
      "Name": "string",
      "Platform": "string",
      "RootVolumeConfig": {
         "VolumeSizeInGb": number
      },
      "SessionScriptS3Location": {
         "S3Bucket": "string",
         "S3Key": "string"
      },
      "State": "string",
      "StreamView": "string",
      "UsbDeviceFilterStrings": [ "string" ],
      "VpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "SubnetIds": [ "string" ]
      }
   }
}
```

## Response Elements
<a name="API_UpdateFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Fleet](#API_UpdateFleet_ResponseSyntax) **   <a name="WorkSpacesApplications-UpdateFleet-response-Fleet"></a>
Information about the fleet.
Type: [Fleet](API_Fleet.md) object

## Errors
<a name="API_UpdateFleet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** IncompatibleImageException **
The image can't be updated because it's not compatible for updates.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidAccountStatusException **
The resource cannot be created because your AWS account is suspended. For assistance, contact AWS Support.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidRoleException **
The specified role is invalid.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** RequestLimitExceededException **
WorkSpaces Applications can't process the request right now because this operation is being throttled. Try again later.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceInUseException **
The specified resource is in use.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotAvailableException **
The specified resource exists and is not in use, but isn't available.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/UpdateFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/UpdateFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UpdateFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/UpdateFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UpdateFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/UpdateFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/UpdateFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/UpdateFleet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/UpdateFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UpdateFleet)
