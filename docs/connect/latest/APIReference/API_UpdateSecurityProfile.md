---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateSecurityProfile.html
---

# UpdateSecurityProfile
<a name="API_UpdateSecurityProfile"></a>

Updates a security profile.

For information about security profiles, see [Security Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html) in the *Connect Customer Administrator Guide*. For a mapping of the API name and user interface name of the security profile permissions, see [List of security profile permissions](https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html).

## Request Syntax
<a name="API_UpdateSecurityProfile_RequestSyntax"></a>

```
POST /security-profiles/{{InstanceId}}/{{SecurityProfileId}} HTTP/1.1
Content-type: application/json

{
   "AllowedAccessControlHierarchyGroupId": "{{string}}",
   "AllowedAccessControlTags": {
      "{{string}}" : "{{string}}"
   },
   "AllowedAIAgents": [
      {
         "Arn": "{{string}}",
         "Type": "{{string}}"
      }
   ],
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
   "TagRestrictedResources": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateSecurityProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [SecurityProfileId](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-uri-SecurityProfileId"></a>
The identifier for the security profle.
Required: Yes

## Request Body
<a name="API_UpdateSecurityProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AllowedAccessControlHierarchyGroupId](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-AllowedAccessControlHierarchyGroupId"></a>
The identifier of the hierarchy group that a security profile uses to restrict access to resources in Connect Customer.
Type: String
Required: No

 ** [AllowedAccessControlTags](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-AllowedAccessControlTags"></a>
The list of tags that a security profile uses to restrict access to resources in Connect Customer.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

 ** [AllowedAIAgents](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-AllowedAIAgents"></a>
A list of AI agents that the security profile will give access to.
Type: Array of [AIAgent](API_AIAgent.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** [AllowedFlowModules](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-AllowedFlowModules"></a>
 A list of Flow Modules an AI Agent can invoke as a tool
Type: Array of [FlowModule](API_FlowModule.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** [Applications](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-Applications"></a>
A list of the third-party application's metadata.
Type: Array of [Application](API_Application.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** [Description](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-Description"></a>
The description of the security profile.
Type: String
Length Constraints: Maximum length of 250.
Required: No

 ** [GranularAccessControlConfiguration](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-GranularAccessControlConfiguration"></a>
The granular access control configuration for the security profile, including data table permissions.
Type: [GranularAccessControlConfiguration](API_GranularAccessControlConfiguration.md) object
Required: No

 ** [HierarchyRestrictedResources](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-HierarchyRestrictedResources"></a>
The list of resources that a security profile applies hierarchy restrictions to in Connect Customer. Following are acceptable ResourceNames: `User`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Permissions](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-Permissions"></a>
The permissions granted to a security profile. For a list of valid permissions, see [List of security profile permissions](https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html).
Type: Array of strings
Array Members: Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [TagRestrictedResources](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="connect-UpdateSecurityProfile-request-TagRestrictedResources"></a>
The list of resources that a security profile applies tag restrictions to in Connect Customer.
Type: Array of strings
Array Members: Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## Response Syntax
<a name="API_UpdateSecurityProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateSecurityProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateSecurityProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateSecurityProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateSecurityProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateSecurityProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateSecurityProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateSecurityProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateSecurityProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateSecurityProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateSecurityProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateSecurityProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateSecurityProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateSecurityProfile)
