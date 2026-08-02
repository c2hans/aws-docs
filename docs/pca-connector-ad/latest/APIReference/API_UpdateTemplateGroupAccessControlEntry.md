---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_UpdateTemplateGroupAccessControlEntry.html
---

# UpdateTemplateGroupAccessControlEntry
<a name="API_UpdateTemplateGroupAccessControlEntry"></a>

Update a group access control entry you created using [CreateTemplateGroupAccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplateGroupAccessControlEntry.html).

## Request Syntax
<a name="API_UpdateTemplateGroupAccessControlEntry_RequestSyntax"></a>

```
PATCH /templates/{{TemplateArn}}/accessControlEntries/{{GroupSecurityIdentifier}} HTTP/1.1
Content-type: application/json

{
   "AccessRights": {
      "AutoEnroll": "{{string}}",
      "Enroll": "{{string}}"
   },
   "GroupDisplayName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTemplateGroupAccessControlEntry_RequestParameters"></a>

The request uses the following URI parameters.

 ** [GroupSecurityIdentifier](#API_UpdateTemplateGroupAccessControlEntry_RequestSyntax) **   <a name="PcaConnectorAd-UpdateTemplateGroupAccessControlEntry-request-uri-GroupSecurityIdentifier"></a>
Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".
Length Constraints: Minimum length of 7. Maximum length of 256.
Pattern: `S-[0-9]-([0-9]+-){1,14}[0-9]+`
Required: Yes

 ** [TemplateArn](#API_UpdateTemplateGroupAccessControlEntry_RequestSyntax) **   <a name="PcaConnectorAd-UpdateTemplateGroupAccessControlEntry-request-uri-TemplateArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html).
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\/template\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateTemplateGroupAccessControlEntry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccessRights](#API_UpdateTemplateGroupAccessControlEntry_RequestSyntax) **   <a name="PcaConnectorAd-UpdateTemplateGroupAccessControlEntry-request-AccessRights"></a>
Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.
Type: [AccessRights](API_AccessRights.md) object
Required: No

 ** [GroupDisplayName](#API_UpdateTemplateGroupAccessControlEntry_RequestSyntax) **   <a name="PcaConnectorAd-UpdateTemplateGroupAccessControlEntry-request-GroupDisplayName"></a>
Name of the Active Directory group. This name does not need to match the group name in Active Directory.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\x20-\x7E]+`
Required: No

## Response Syntax
<a name="API_UpdateTemplateGroupAccessControlEntry_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateTemplateGroupAccessControlEntry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTemplateGroupAccessControlEntry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your AWS Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an AWS Organizations service control policy (SCP) that affects your AWS account.
HTTP Status Code: 403

 ** ConflictException **
This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.
 ** ResourceId **
The identifier of the AWS resource.
 ** ResourceType **
The resource type, which can be one of `Connector`, `Template`, `TemplateGroupAccessControlEntry`, `ServicePrincipalName`, or `DirectoryRegistration`.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.
 ** ResourceId **
The identifier of the AWS resource.
 ** ResourceType **
The resource type, which can be one of `Connector`, `Template`, `TemplateGroupAccessControlEntry`, `ServicePrincipalName`, or `DirectoryRegistration`.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** QuotaCode **
The code associated with the quota.
 ** ServiceCode **
Identifies the originating service.
HTTP Status Code: 429

 ** ValidationException **
An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid.
 ** Reason **
The reason for the validation error. This won't be return for every validation exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTemplateGroupAccessControlEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pca-connector-ad-2018-05-10/UpdateTemplateGroupAccessControlEntry)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pca-connector-ad-2018-05-10/UpdateTemplateGroupAccessControlEntry)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/UpdateTemplateGroupAccessControlEntry)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pca-connector-ad-2018-05-10/UpdateTemplateGroupAccessControlEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/UpdateTemplateGroupAccessControlEntry)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pca-connector-ad-2018-05-10/UpdateTemplateGroupAccessControlEntry)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pca-connector-ad-2018-05-10/UpdateTemplateGroupAccessControlEntry)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pca-connector-ad-2018-05-10/UpdateTemplateGroupAccessControlEntry)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pca-connector-ad-2018-05-10/UpdateTemplateGroupAccessControlEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/UpdateTemplateGroupAccessControlEntry)
