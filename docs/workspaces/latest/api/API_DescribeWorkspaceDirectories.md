---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectories.html
---

# DescribeWorkspaceDirectories
<a name="API_DescribeWorkspaceDirectories"></a>

Describes the available directories that are registered with Amazon WorkSpaces.

## Request Syntax
<a name="API_DescribeWorkspaceDirectories_RequestSyntax"></a>

```
{
   "DirectoryIds": [ "{{string}}" ],
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "WorkspaceDirectoryNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeWorkspaceDirectories_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryIds](#API_DescribeWorkspaceDirectories_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceDirectories-request-DirectoryIds"></a>
The identifiers of the directories. If the value is null, all directories are retrieved.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: No

 ** [Filters](#API_DescribeWorkspaceDirectories_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceDirectories-request-Filters"></a>
The filter condition for the WorkSpaces.
Type: Array of [DescribeWorkspaceDirectoriesFilter](API_DescribeWorkspaceDirectoriesFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

 ** [Limit](#API_DescribeWorkspaceDirectories_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceDirectories-request-Limit"></a>
The maximum number of directories to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeWorkspaceDirectories_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceDirectories-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [WorkspaceDirectoryNames](#API_DescribeWorkspaceDirectories_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceDirectories-request-WorkspaceDirectoryNames"></a>
The names of the WorkSpace directories.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.\s-]{1,64}$`
Required: No

## Response Syntax
<a name="API_DescribeWorkspaceDirectories_ResponseSyntax"></a>

```
{
   "Directories": [
      {
         "ActiveDirectoryConfig": {
            "DomainName": "string",
            "ServiceAccountSecretArn": "string"
         },
         "Alias": "string",
         "CertificateBasedAuthProperties": {
            "CertificateAuthorityArn": "string",
            "Status": "string"
         },
         "CustomerUserName": "string",
         "DirectoryId": "string",
         "DirectoryName": "string",
         "DirectoryType": "string",
         "DnsIpAddresses": [ "string" ],
         "DnsIpv6Addresses": [ "string" ],
         "EndpointEncryptionMode": "string",
         "ErrorMessage": "string",
         "IamRoleId": "string",
         "IDCConfig": {
            "ApplicationArn": "string",
            "InstanceArn": "string"
         },
         "ipGroupIds": [ "string" ],
         "MicrosoftEntraConfig": {
            "ApplicationConfigSecretArn": "string",
            "TenantId": "string"
         },
         "RegistrationCode": "string",
         "SamlProperties": {
            "RelayStateParameterName": "string",
            "Status": "string",
            "UserAccessUrl": "string"
         },
         "SelfservicePermissions": {
            "ChangeComputeType": "string",
            "IncreaseVolumeSize": "string",
            "RebuildWorkspace": "string",
            "RestartWorkspace": "string",
            "SwitchRunningMode": "string"
         },
         "State": "string",
         "StreamingProperties": {
            "GlobalAccelerator": {
               "Mode": "string",
               "PreferredProtocol": "string"
            },
            "StorageConnectors": [
               {
                  "ConnectorType": "string",
                  "Status": "string"
               }
            ],
            "StreamingExperiencePreferredProtocol": "string",
            "UserSettings": [
               {
                  "Action": "string",
                  "MaximumLength": number,
                  "Permission": "string"
               }
            ]
         },
         "SubnetIds": [ "string" ],
         "Tenancy": "string",
         "UserIdentityType": "string",
         "WorkspaceAccessProperties": {
            "AccessEndpointConfig": {
               "AccessEndpoints": [
                  {
                     "AccessEndpointType": "string",
                     "VpcEndpointId": "string"
                  }
               ],
               "InternetFallbackProtocols": [ "string" ]
            },
            "DeviceTypeAndroid": "string",
            "DeviceTypeChromeOs": "string",
            "DeviceTypeIos": "string",
            "DeviceTypeLinux": "string",
            "DeviceTypeOsx": "string",
            "DeviceTypeWeb": "string",
            "DeviceTypeWindows": "string",
            "DeviceTypeWorkSpacesThinClient": "string",
            "DeviceTypeZeroClient": "string"
         },
         "WorkspaceCreationProperties": {
            "CustomSecurityGroupId": "string",
            "DefaultOu": "string",
            "EnableInternetAccess": boolean,
            "EnableMaintenanceMode": boolean,
            "InstanceIamRoleArn": "string",
            "UserEnabledAsLocalAdministrator": boolean
         },
         "WorkspaceDirectoryDescription": "string",
         "WorkspaceDirectoryName": "string",
         "WorkspaceSecurityGroupId": "string",
         "WorkspaceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeWorkspaceDirectories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Directories](#API_DescribeWorkspaceDirectories_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaceDirectories-response-Directories"></a>
Information about the directories.
Type: Array of [WorkspaceDirectory](API_WorkspaceDirectory.md) objects

 ** [NextToken](#API_DescribeWorkspaceDirectories_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaceDirectories-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_DescribeWorkspaceDirectories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

## See Also
<a name="API_DescribeWorkspaceDirectories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeWorkspaceDirectories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeWorkspaceDirectories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeWorkspaceDirectories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeWorkspaceDirectories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeWorkspaceDirectories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeWorkspaceDirectories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeWorkspaceDirectories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeWorkspaceDirectories)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeWorkspaceDirectories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeWorkspaceDirectories)
