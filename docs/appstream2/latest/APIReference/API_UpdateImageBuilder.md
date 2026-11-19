---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateImageBuilder.html
---

# UpdateImageBuilder

Updates the specified fields for the specified image builder. The image builder must be in the STOPPED state.

## Request Syntax
<a name="API_UpdateImageBuilder_RequestSyntax"></a>

```
{
   "AgentAccessConfig": {
      "S3BucketArn": "{{string}}",
      "ScreenImageFormat": "{{string}}",
      "ScreenResolution": "{{string}}",
      "ScreenshotsUploadEnabled": {{boolean}},
      "Settings": [
         {
            "AgentAction": "{{string}}",
            "Permission": "{{string}}"
         }
      ],
      "UserControlMode": "{{string}}"
   },
   "AttributesToDelete": [ "{{string}}" ],
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateImageBuilder_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AgentAccessConfig](#API_UpdateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateImageBuilder-request-AgentAccessConfig"></a>
The configuration for agent access on the image builder. Specify this to update agent access settings. To remove agent access, use AttributesToDelete with the AGENT\_ACCESS\_CONFIG value.
Type: [ImageBuilderAgentAccessConfigForUpdate](API_ImageBuilderAgentAccessConfigForUpdate.md) object
Required: No

 ** [AttributesToDelete](#API_UpdateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateImageBuilder-request-AttributesToDelete"></a>
The image builder attributes to delete.
Type: Array of strings
Array Members: Maximum number of 2 items.
Valid Values: `AGENT_ACCESS_CONFIG`
Required: No

 ** [Description](#API_UpdateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateImageBuilder-request-Description"></a>
The description to display.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DisplayName](#API_UpdateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateImageBuilder-request-DisplayName"></a>
The image builder name to display.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Name](#API_UpdateImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateImageBuilder-request-Name"></a>
The name of the image builder.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Syntax
<a name="API_UpdateImageBuilder_ResponseSyntax"></a>

```
{
   "ImageBuilder": {
      "AccessEndpoints": [
         {
            "EndpointType": "string",
            "VpceId": "string"
         }
      ],
      "AgentAccessConfig": {
         "S3BucketArn": "string",
         "ScreenImageFormat": "string",
         "ScreenResolution": "string",
         "ScreenshotsUploadEnabled": boolean,
         "Settings": [
            {
               "AgentAction": "string",
               "Permission": "string"
            }
         ],
         "UserControlMode": "string"
      },
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
<a name="API_UpdateImageBuilder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageBuilder](#API_UpdateImageBuilder_ResponseSyntax) **   <a name="WorkSpacesApplications-UpdateImageBuilder-response-ImageBuilder"></a>
Information about the image builder.
Type: [ImageBuilder](API_ImageBuilder.md) object

## Errors
<a name="API_UpdateImageBuilder_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateImageBuilder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/UpdateImageBuilder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/UpdateImageBuilder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UpdateImageBuilder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/UpdateImageBuilder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UpdateImageBuilder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/UpdateImageBuilder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/UpdateImageBuilder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/UpdateImageBuilder)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/UpdateImageBuilder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UpdateImageBuilder)
