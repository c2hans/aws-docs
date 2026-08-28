---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_CreateSecurityGroup.html
---

# CreateSecurityGroup
<a name="API_CreateSecurityGroup"></a>

Creates a new security group in a Wickr network. Security groups allow you to organize users and control their permissions, features, and security settings.

## Request Syntax
<a name="API_CreateSecurityGroup_RequestSyntax"></a>

```
POST /networks/{{networkId}}/security-groups HTTP/1.1
X-Client-Token: {{clientToken}}
Content-type: application/json

{
   "name": "{{string}}",
   "securityGroupSettings": {
      "enableGuestFederation": {{boolean}},
      "enableRestrictedGlobalFederation": {{boolean}},
      "federationMode": {{number}},
      "globalFederation": {{boolean}},
      "lockoutThreshold": {{number}},
      "permittedNetworks": [ "{{string}}" ],
      "permittedWickrAwsNetworks": [
         {
            "networkId": "{{string}}",
            "region": "{{string}}"
         }
      ],
      "permittedWickrEnterpriseNetworks": [
         {
            "domain": "{{string}}",
            "networkId": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_CreateSecurityGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_CreateSecurityGroup_RequestSyntax) **   <a name="wickr-CreateSecurityGroup-request-clientToken"></a>
A unique identifier for this request to ensure idempotency.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_:]+`

 ** [networkId](#API_CreateSecurityGroup_RequestSyntax) **   <a name="wickr-CreateSecurityGroup-request-uri-networkId"></a>
The ID of the Wickr network where the security group will be created.
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

## Request Body
<a name="API_CreateSecurityGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_CreateSecurityGroup_RequestSyntax) **   <a name="wickr-CreateSecurityGroup-request-name"></a>
The name for the new security group.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** [securityGroupSettings](#API_CreateSecurityGroup_RequestSyntax) **   <a name="wickr-CreateSecurityGroup-request-securityGroupSettings"></a>
The configuration settings for the security group, including permissions, federation settings, and feature controls.
Type: [SecurityGroupSettingsRequest](API_SecurityGroupSettingsRequest.md) object
Required: Yes

## Response Syntax
<a name="API_CreateSecurityGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "securityGroup": {
      "activeDirectoryGuid": "string",
      "activeMembers": number,
      "botMembers": number,
      "id": "string",
      "isDefault": boolean,
      "modified": number,
      "name": "string",
      "securityGroupSettings": {
         "alwaysReauthenticate": boolean,
         "atakPackageValues": [ "string" ],
         "calling": {
            "canStart11Call": boolean,
            "canVideoCall": boolean,
            "forceTcpCall": boolean
         },
         "checkForUpdates": boolean,
         "enableAtak": boolean,
         "enableCrashReports": boolean,
         "enableFileDownload": boolean,
         "enableGuestFederation": boolean,
         "enableNotificationPreview": boolean,
         "enableOpenAccessOption": boolean,
         "enableRestrictedGlobalFederation": boolean,
         "federationMode": number,
         "filesEnabled": boolean,
         "forceDeviceLockout": number,
         "forceOpenAccess": boolean,
         "forceReadReceipts": boolean,
         "globalFederation": boolean,
         "isAtoEnabled": boolean,
         "isLinkPreviewEnabled": boolean,
         "locationAllowMaps": boolean,
         "locationEnabled": boolean,
         "lockoutThreshold": number,
         "maxAutoDownloadSize": number,
         "maxBor": number,
         "maxNonSsoSessionMinutes": number,
         "maxTtl": number,
         "messageForwardingEnabled": boolean,
         "passwordRequirements": {
            "lowercase": number,
            "minLength": number,
            "numbers": number,
            "symbols": number,
            "uppercase": number
         },
         "permittedNetworks": [ "string" ],
         "permittedWickrAwsNetworks": [
            {
               "networkId": "string",
               "region": "string"
            }
         ],
         "permittedWickrEnterpriseNetworks": [
            {
               "domain": "string",
               "networkId": "string"
            }
         ],
         "presenceEnabled": boolean,
         "quickResponses": [ "string" ],
         "showMasterRecoveryKey": boolean,
         "shredder": {
            "canProcessManually": boolean,
            "intensity": number
         },
         "ssoMaxIdleMinutes": number
      }
   }
}
```

## Response Elements
<a name="API_CreateSecurityGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [securityGroup](#API_CreateSecurityGroup_ResponseSyntax) **   <a name="wickr-CreateSecurityGroup-response-securityGroup"></a>
The details of the newly created security group, including its ID, name, and settings.
Type: [SecurityGroup](API_SecurityGroup.md) object

## Errors
<a name="API_CreateSecurityGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [BadRequestError](API_BadRequestError.md)
The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.
 ** message **
A detailed message explaining what was wrong with the request and how to correct it.
HTTP Status Code: 400

 [ForbiddenError](API_ForbiddenError.md)
Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.
 ** message **
A message explaining why access was denied and what permissions are required.
HTTP Status Code: 403

 [InternalServerError](API_InternalServerError.md)
An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact AWS Support.
 ** message **
A message describing the internal server error that occurred.
HTTP Status Code: 500

 [RateLimitError](API_RateLimitError.md)
The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.
 ** message **
A message indicating that the rate limit was exceeded and suggesting when to retry.
HTTP Status Code: 429

 [ResourceNotFoundError](API_ResourceNotFoundError.md)
The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.
 ** message **
A message identifying which resource was not found.
HTTP Status Code: 404

 [UnauthorizedError](API_UnauthorizedError.md)
The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.
 ** message **
A message explaining why the authentication failed.
HTTP Status Code: 401

 [ValidationError](API_ValidationError.md)
One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.
 ** message **
A message describing the validation error error that occurred.
 ** reasons **
A list of validation error details, where each item identifies a specific field that failed validation and explains the reason for the failure.
HTTP Status Code: 422

## See Also
<a name="API_CreateSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wickr-2024-02-01/CreateSecurityGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wickr-2024-02-01/CreateSecurityGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/CreateSecurityGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wickr-2024-02-01/CreateSecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/CreateSecurityGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wickr-2024-02-01/CreateSecurityGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wickr-2024-02-01/CreateSecurityGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wickr-2024-02-01/CreateSecurityGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wickr-2024-02-01/CreateSecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/CreateSecurityGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
