---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateAppBlockBuilder.html
---

# CreateAppBlockBuilder
<a name="API_CreateAppBlockBuilder"></a>

Creates an app block builder.

## Request Syntax
<a name="API_CreateAppBlockBuilder_RequestSyntax"></a>

```
{
   "AccessEndpoints": [
      {
         "EndpointType": "{{string}}",
         "VpceId": "{{string}}"
      }
   ],
   "Description": "{{string}}",
   "DisableIMDSV1": {{boolean}},
   "DisplayName": "{{string}}",
   "EnableDefaultInternetAccess": {{boolean}},
   "IamRoleArn": "{{string}}",
   "InstanceType": "{{string}}",
   "Name": "{{string}}",
   "Platform": "{{string}}",
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
<a name="API_CreateAppBlockBuilder_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessEndpoints](#API_CreateAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-request-AccessEndpoints"></a>
The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the app block builder only through the specified endpoints.
Type: Array of [AccessEndpoint](API_AccessEndpoint.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: No

 ** [Description](#API_CreateAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-request-Description"></a>
The description of the app block builder.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DisableIMDSV1](#API_CreateAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-request-DisableIMDSV1"></a>
Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.
Starting July 8, 2026, app block builders default to IMDSv2 only when this parameter is not explicitly set. To retain IMDSv1 access, explicitly set this parameter to false.
Type: Boolean
Required: No

 ** [DisplayName](#API_CreateAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-request-DisplayName"></a>
The display name of the app block builder.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [EnableDefaultInternetAccess](#API_CreateAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-request-EnableDefaultInternetAccess"></a>
Enables or disables default internet access for the app block builder.
Type: Boolean
Required: No

 ** [IamRoleArn](#API_CreateAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-request-IamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to apply to the app block builder. To assume a role, the app block builder calls the AWS Security Token Service (STS) `AssumeRole` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the **appstream\_machine\_role** credential profile on the instance.
For more information, see [Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html) in the *Amazon WorkSpaces Applications Administration Guide*.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** [InstanceType](#API_CreateAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-request-InstanceType"></a>
The instance type to use when launching the app block builder. The following instance types are available:
+ stream.standard.small
+ stream.standard.medium
+ stream.standard.large
+ stream.standard.xlarge
+ stream.standard.2xlarge
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [Name](#API_CreateAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-request-Name"></a>
The unique name for the app block builder.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [Platform](#API_CreateAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-request-Platform"></a>
The platform of the app block builder.
 `WINDOWS_SERVER_2019` is the only valid value.
Type: String
Valid Values: `WINDOWS_SERVER_2019`
Required: Yes

 ** [Tags](#API_CreateAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-request-Tags"></a>
The tags to associate with the app block builder. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=.
If you do not specify a value, the value is set to an empty string.
Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters:
\_ . : / = \+ \\ - @
For more information, see [Tagging Your Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html) in the *Amazon WorkSpaces Applications Administration Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(^(?!aws:).[\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [VpcConfig](#API_CreateAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-request-VpcConfig"></a>
The VPC configuration for the app block builder.
App block builders require that you specify at least two subnets in different availability zones.
Type: [VpcConfig](API_VpcConfig.md) object
Required: Yes

## Response Syntax
<a name="API_CreateAppBlockBuilder_ResponseSyntax"></a>

```
{
   "AppBlockBuilder": {
      "AccessEndpoints": [
         {
            "EndpointType": "string",
            "VpceId": "string"
         }
      ],
      "AppBlockBuilderErrors": [
         {
            "ErrorCode": "string",
            "ErrorMessage": "string",
            "ErrorTimestamp": number
         }
      ],
      "Arn": "string",
      "CreatedTime": number,
      "Description": "string",
      "DisableIMDSV1": boolean,
      "DisplayName": "string",
      "EnableDefaultInternetAccess": boolean,
      "IamRoleArn": "string",
      "InstanceType": "string",
      "Name": "string",
      "Platform": "string",
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
<a name="API_CreateAppBlockBuilder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppBlockBuilder](#API_CreateAppBlockBuilder_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilder-response-AppBlockBuilder"></a>
Describes an app block builder.
Type: [AppBlockBuilder](API_AppBlockBuilder.md) object

## Errors
<a name="API_CreateAppBlockBuilder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
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
<a name="API_CreateAppBlockBuilder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateAppBlockBuilder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateAppBlockBuilder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateAppBlockBuilder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateAppBlockBuilder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateAppBlockBuilder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateAppBlockBuilder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateAppBlockBuilder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateAppBlockBuilder)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateAppBlockBuilder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateAppBlockBuilder)
