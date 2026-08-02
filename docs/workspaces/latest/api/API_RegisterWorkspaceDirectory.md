---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_RegisterWorkspaceDirectory.html
---

# RegisterWorkspaceDirectory
<a name="API_RegisterWorkspaceDirectory"></a>

Registers the specified directory. This operation is asynchronous and returns before the WorkSpace directory is registered. If this is the first time you are registering a directory, you will need to create the workspaces\_DefaultRole role before you can register a directory. For more information, see [ Creating the workspaces\_DefaultRole Role](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html#create-default-role).

## Request Syntax
<a name="API_RegisterWorkspaceDirectory_RequestSyntax"></a>

```
{
   "ActiveDirectoryConfig": {
      "DomainName": "{{string}}",
      "ServiceAccountSecretArn": "{{string}}"
   },
   "DirectoryId": "{{string}}",
   "EnableSelfService": {{boolean}},
   "IdcInstanceArn": "{{string}}",
   "MicrosoftEntraConfig": {
      "ApplicationConfigSecretArn": "{{string}}",
      "TenantId": "{{string}}"
   },
   "SubnetIds": [ "{{string}}" ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Tenancy": "{{string}}",
   "UserIdentityType": "{{string}}",
   "WorkspaceDirectoryDescription": "{{string}}",
   "WorkspaceDirectoryName": "{{string}}",
   "WorkspaceType": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterWorkspaceDirectory_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ActiveDirectoryConfig](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-ActiveDirectoryConfig"></a>
The active directory config of the directory.
Type: [ActiveDirectoryConfig](API_ActiveDirectoryConfig.md) object
Required: No

 ** [DirectoryId](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-DirectoryId"></a>
The identifier of the directory. You cannot register a directory if it does not have a status of Active. If the directory does not have a status of Active, you will receive an InvalidResourceStateException error. If you have already registered the maximum number of directories that you can register with Amazon WorkSpaces, you will receive a ResourceLimitExceededException error. Deregister directories that you are not using for WorkSpaces, and try again.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: No

 ** [EnableSelfService](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-EnableSelfService"></a>
Indicates whether self-service capabilities are enabled or disabled.
Type: Boolean
Required: No

 ** [IdcInstanceArn](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-IdcInstanceArn"></a>
The Amazon Resource Name (ARN) of the identity center instance.
Type: String
Pattern: `^arn:aws[a-z-]{0,7}:[A-Za-z0-9][A-za-z0-9_/.-]{0,62}:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** [MicrosoftEntraConfig](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-MicrosoftEntraConfig"></a>
The details about Microsoft Entra config.
Type: [MicrosoftEntraConfig](API_MicrosoftEntraConfig.md) object
Required: No

 ** [SubnetIds](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-SubnetIds"></a>
The identifiers of the subnets for your virtual private cloud (VPC). Make sure that the subnets are in supported Availability Zones. The subnets must also be in separate Availability Zones. If these conditions are not met, you will receive an OperationNotSupportedException error.
Type: Array of strings
Array Members: Maximum number of 2 items.
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `^(subnet-([0-9a-f]{8}|[0-9a-f]{17}))$`
Required: No

 ** [Tags](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-Tags"></a>
The tags associated with the directory.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [Tenancy](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-Tenancy"></a>
Indicates whether your WorkSpace directory is dedicated or shared. To use Bring Your Own License (BYOL) images, this value must be set to `DEDICATED` and your AWS account must be enabled for BYOL. If your account has not been enabled for BYOL, you will receive an InvalidParameterValuesException error. For more information about BYOL images, see [Bring Your Own Windows Desktop Images](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html).
Type: String
Valid Values: `DEDICATED | SHARED`
Required: No

 ** [UserIdentityType](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-UserIdentityType"></a>
The type of identity management the user is using.
Type: String
Valid Values: `CUSTOMER_MANAGED | AWS_DIRECTORY_SERVICE | AWS_IAM_IDENTITY_CENTER`
Required: No

 ** [WorkspaceDirectoryDescription](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-WorkspaceDirectoryDescription"></a>
Description of the directory to register.
Type: String
Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]{1,255}$`
Required: No

 ** [WorkspaceDirectoryName](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-WorkspaceDirectoryName"></a>
The name of the directory to register.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.\s-]{1,64}$`
Required: No

 ** [WorkspaceType](#API_RegisterWorkspaceDirectory_RequestSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-request-WorkspaceType"></a>
Indicates whether the directory's WorkSpace type is personal or pools.
Type: String
Valid Values: `PERSONAL | POOLS`
Required: No

## Response Syntax
<a name="API_RegisterWorkspaceDirectory_ResponseSyntax"></a>

```
{
   "DirectoryId": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_RegisterWorkspaceDirectory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryId](#API_RegisterWorkspaceDirectory_ResponseSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-response-DirectoryId"></a>
The identifier of the directory.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`

 ** [State](#API_RegisterWorkspaceDirectory_ResponseSyntax) **   <a name="WorkSpaces-RegisterWorkspaceDirectory-response-State"></a>
The registration status of the WorkSpace directory.
Type: String
Valid Values: `REGISTERING | REGISTERED | DEREGISTERING | DEREGISTERED | ERROR`

## Errors
<a name="API_RegisterWorkspaceDirectory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** InvalidResourceStateException **
The state of the resource is not valid for this operation.
HTTP Status Code: 400

 ** OperationNotSupportedException **
This operation is not supported.
 ** message **
The exception error message.
 ** reason **
The exception error reason.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
HTTP Status Code: 400

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

 ** UnsupportedNetworkConfigurationException **
The configuration of this network is not supported for this operation, or your network configuration conflicts with the Amazon WorkSpaces management network IP range. For more information, see [ Configure a VPC for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html).
HTTP Status Code: 400

 ** WorkspacesDefaultRoleNotFoundException **
The workspaces\_DefaultRole role could not be found. If this is the first time you are registering a directory, you will need to create the workspaces\_DefaultRole role before you can register a directory. For more information, see [Creating the workspaces\_DefaultRole Role](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html#create-default-role).
HTTP Status Code: 400

## See Also
<a name="API_RegisterWorkspaceDirectory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/RegisterWorkspaceDirectory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/RegisterWorkspaceDirectory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/RegisterWorkspaceDirectory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/RegisterWorkspaceDirectory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/RegisterWorkspaceDirectory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/RegisterWorkspaceDirectory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/RegisterWorkspaceDirectory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/RegisterWorkspaceDirectory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/RegisterWorkspaceDirectory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/RegisterWorkspaceDirectory)
