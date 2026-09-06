---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateImageBuilder.html
---

# CreateImageBuilder
<a name="API_CreateImageBuilder"></a>

Creates an image builder. An image builder is a virtual machine that is used to create an image.

The initial state of the builder is `PENDING`. When it is ready, the state is `RUNNING`.

## Request Syntax
<a name="API_CreateImageBuilder_RequestSyntax"></a>

```
{
   "AccessEndpoints": [
      {
         "EndpointType": "{{string}}",
         "VpceId": "{{string}}"
      }
   ],
   "AppstreamAgentVersion": "{{string}}",
   "Description": "{{string}}",
   "DisableIMDSV1": {{boolean}},
   "DisplayName": "{{string}}",
   "DomainJoinInfo": {
      "DirectoryName": "{{string}}",
      "OrganizationalUnitDistinguishedName": "{{string}}"
   },
   "EnableDefaultInternetAccess": {{boolean}},
   "IamRoleArn": "{{string}}",
   "ImageArn": "{{string}}",
   "ImageName": "{{string}}",
   "InstanceType": "{{string}}",
   "Name": "{{string}}",
   "RootVolumeConfig": {
      "VolumeSizeInGb": {{number}}
   },
   "SoftwaresToInstall": [ "{{string}}" ],
   "SoftwaresToUninstall": [ "{{string}}" ],
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "VpcConfig": {
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_CreateImageBuilder_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessEndpoints](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-AccessEndpoints"></a>
The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the image builder only through the specified endpoints.
Type: Array of [AccessEndpoint](API_AccessEndpoint.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: No

 ** [AppstreamAgentVersion](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-AppstreamAgentVersion"></a>
The version of the WorkSpaces Applications agent to use for this image builder. To use the latest version of the WorkSpaces Applications agent, specify [LATEST].
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [Description](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-Description"></a>
The description to display.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DisableIMDSV1](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-DisableIMDSV1"></a>
Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.
Starting July 8, 2026, resources created with compatible images default to IMDSv2 only when this parameter is not explicitly set. A compatible image uses a base image or managed image update released on or after January 16, 2024. To retain IMDSv1 access, explicitly set this parameter to false.
Type: Boolean
Required: No

 ** [DisplayName](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-DisplayName"></a>
The image builder name to display.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [DomainJoinInfo](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-DomainJoinInfo"></a>
The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.
Type: [DomainJoinInfo](API_DomainJoinInfo.md) object
Required: No

 ** [EnableDefaultInternetAccess](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-EnableDefaultInternetAccess"></a>
Enables or disables default internet access for the image builder.
Type: Boolean
Required: No

 ** [IamRoleArn](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-IamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to apply to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) `AssumeRole` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the **appstream\_machine\_role** credential profile on the instance.
For more information, see [Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html) in the *Amazon WorkSpaces Applications Administration Guide*.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** [ImageArn](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-ImageArn"></a>
The ARN of the public, private, or shared image to use.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** [ImageName](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-ImageName"></a>
The name of the image used to create the image builder.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [InstanceType](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-InstanceType"></a>
The instance type to use when launching the image builder. The following instance types are available:
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

 ** [Name](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-Name"></a>
A unique name for the image builder.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [RootVolumeConfig](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-RootVolumeConfig"></a>
The configuration for the root volume of the image builder. Use this to customize storage capacity from 200 GB up to 500 GB based on your application installation requirements.
Type: [VolumeConfig](API_VolumeConfig.md) object
Required: No

 ** [SoftwaresToInstall](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-SoftwaresToInstall"></a>
The list of license included applications to install on the image builder during creation.
Possible values include the following:
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_64Bit
+ Microsoft\_Project\_2021\_Professional\_32Bit
+ Microsoft\_Project\_2021\_Professional\_64Bit
+ Microsoft\_Project\_2024\_Professional\_32Bit
+ Microsoft\_Project\_2024\_Professional\_64Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Project\_2021\_Standard\_32Bit
+ Microsoft\_Project\_2021\_Standard\_64Bit
+ Microsoft\_Project\_2024\_Standard\_32Bit
+ Microsoft\_Project\_2024\_Standard\_64Bit
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** [SoftwaresToUninstall](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-SoftwaresToUninstall"></a>
The list of license included applications to uninstall from the image builder during creation.
Possible values include the following:
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_64Bit
+ Microsoft\_Project\_2021\_Professional\_32Bit
+ Microsoft\_Project\_2021\_Professional\_64Bit
+ Microsoft\_Project\_2024\_Professional\_32Bit
+ Microsoft\_Project\_2024\_Professional\_64Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Project\_2021\_Standard\_32Bit
+ Microsoft\_Project\_2021\_Standard\_64Bit
+ Microsoft\_Project\_2024\_Standard\_32Bit
+ Microsoft\_Project\_2024\_Standard\_64Bit
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** [Tags](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-Tags"></a>
The tags to associate with the image builder. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=.
Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters:
\_ . : / = \+ \\ - @
If you do not specify a value, the value is set to an empty string.
For more information about tags, see [Tagging Your Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html) in the *Amazon WorkSpaces Applications Administration Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(^(?!aws:).[\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [VpcConfig](#API_CreateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-request-VpcConfig"></a>
The VPC configuration for the image builder. You can specify only one subnet.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateImageBuilder_ResponseSyntax"></a>

```
{
   "ImageBuilder": {
      "AccessEndpoints": [
         {
            "EndpointType": "string",
            "VpceId": "string"
         }
      ],
      "AppstreamAgentVersion": "string",
      "Arn": "string",
      "CreatedTime": number,
      "Description": "string",
      "DisableIMDSV1": boolean,
      "DisplayName": "string",
      "DomainJoinInfo": {
         "DirectoryName": "string",
         "OrganizationalUnitDistinguishedName": "string"
      },
      "EnableDefaultInternetAccess": boolean,
      "IamRoleArn": "string",
      "ImageArn": "string",
      "ImageBuilderErrors": [
         {
            "ErrorCode": "string",
            "ErrorMessage": "string",
            "ErrorTimestamp": number
         }
      ],
      "InstanceType": "string",
      "LatestAppstreamAgentVersion": "string",
      "Name": "string",
      "NetworkAccessConfiguration": {
         "EniId": "string",
         "EniIpv6Addresses": [ "string" ],
         "EniPrivateIpAddress": "string"
      },
      "Platform": "string",
      "RootVolumeConfig": {
         "VolumeSizeInGb": number
      },
      "State": "string",
      "StateChangeReason": {
         "Code": "string",
         "Message": "string"
      },
      "VpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "SubnetIds": [ "string" ]
      }
   }
}
```

## Response Elements
<a name="API_CreateImageBuilder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageBuilder](#API_CreateImageBuilder_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilder-response-ImageBuilder"></a>
Information about the image builder.
Type: [ImageBuilder](API_ImageBuilder.md) object

## Errors
<a name="API_CreateImageBuilder_Errors"></a>

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

 ** ResourceAlreadyExistsException **
The specified resource already exists.
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
<a name="API_CreateImageBuilder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateImageBuilder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateImageBuilder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateImageBuilder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateImageBuilder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateImageBuilder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateImageBuilder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateImageBuilder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateImageBuilder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateImageBuilder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateImageBuilder)
