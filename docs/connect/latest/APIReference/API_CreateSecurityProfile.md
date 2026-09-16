---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateSecurityProfile.html
---

# CreateSecurityProfile
<a name="API_CreateSecurityProfile"></a>

Creates a security profile.

For information about security profiles, see [Security Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html) in the *Connect Customer Administrator Guide*. For a mapping of the API name and user interface name of the security profile permissions, see [List of security profile permissions](https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html).

## Request Syntax
<a name="API_CreateSecurityProfile_RequestSyntax"></a>

```
PUT /security-profiles/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "AllowedAccessControlHierarchyGroupId": "{{string}}",
   "AllowedAccessControlTags": {
      "{{string}}" : "{{string}}"
   },
   "AllowedFlowModules": [
      {
         "FlowModuleId": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "Applications": [
      {
         "ApplicationPermissions": [ "{{string}}" ],
         "Namespace": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "Description": "{{string}}",
   "GranularAccessControlConfiguration": {
      "DataTableAccessControlConfiguration": {
         "PrimaryAttributeAccessControlConfiguration": {
            "PrimaryAttributeValues": [
               {
                  "AccessType": "{{string}}",
                  "AttributeName": "{{string}}",
                  "Values": [ "{{string}}" ]
               }
            ]
         }
      }
   },
   "HierarchyRestrictedResources": [ "{{string}}" ],
   "Permissions": [ "{{string}}" ],
   "SecurityProfileName": "{{string}}",
   "TagRestrictedResources": [ "{{string}}" ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSecurityProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateSecurityProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AllowedAccessControlHierarchyGroupId](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-AllowedAccessControlHierarchyGroupId"></a>
The identifier of the hierarchy group that a security profile uses to restrict access to resources in Connect Customer.
Type: String
Required: No

 ** [AllowedAccessControlTags](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-AllowedAccessControlTags"></a>
The list of tags that a security profile uses to restrict access to resources in Connect Customer.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

 ** [AllowedFlowModules](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-AllowedFlowModules"></a>
 A list of Flow Modules an AI Agent can invoke as a tool.
Type: Array of [FlowModule](API_FlowModule.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** [Applications](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-Applications"></a>
A list of third-party applications or MCP Servers that the security profile will give access to.
Type: Array of [Application](API_Application.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** [Description](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-Description"></a>
The description of the security profile.
Type: String
Length Constraints: Maximum length of 250.
Required: No

 ** [GranularAccessControlConfiguration](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-GranularAccessControlConfiguration"></a>
The granular access control configuration for the security profile, including data table permissions.
Type: [GranularAccessControlConfiguration](API_GranularAccessControlConfiguration.md) object
Required: No

 ** [HierarchyRestrictedResources](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-HierarchyRestrictedResources"></a>
The list of resources that a security profile applies hierarchy restrictions to in Connect Customer. Following are acceptable ResourceNames: `User`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Permissions](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-Permissions"></a>
Permissions assigned to the security profile. For a list of valid permissions, see [List of security profile permissions](https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html).
Type: Array of strings
Array Members: Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [SecurityProfileName](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-SecurityProfileName"></a>
The name of the security profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[ a-zA-Z0-9_@-]+$`
Required: Yes

 ** [TagRestrictedResources](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-TagRestrictedResources"></a>
The list of resources that a security profile applies tag restrictions to in Connect Customer. For a list of Connect Customer resources that you can tag, see [Add tags to resources in Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/tagging.html) in the *Connect Customer Administrator Guide*.
Type: Array of strings
Array Members: Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Tags](#API_CreateSecurityProfile_RequestSyntax) **   <a name="connect-CreateSecurityProfile-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateSecurityProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SecurityProfileArn": "string",
   "SecurityProfileId": "string"
}
```

## Response Elements
<a name="API_CreateSecurityProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SecurityProfileArn](#API_CreateSecurityProfile_ResponseSyntax) **   <a name="connect-CreateSecurityProfile-response-SecurityProfileArn"></a>
The Amazon Resource Name (ARN) for the security profile.
Type: String

 ** [SecurityProfileId](#API_CreateSecurityProfile_ResponseSyntax) **   <a name="connect-CreateSecurityProfile-response-SecurityProfileId"></a>
The identifier for the security profle.
Type: String

## Errors
<a name="API_CreateSecurityProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateSecurityProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateSecurityProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateSecurityProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateSecurityProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateSecurityProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateSecurityProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateSecurityProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateSecurityProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateSecurityProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateSecurityProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateSecurityProfile)
