---
source_url: https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_GetSpace.html
---

# GetSpace
<a name="API_GetSpace"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html).

Displays information about the AWS re:Post Private private re:Post.

## Request Syntax
<a name="API_GetSpace_RequestSyntax"></a>

```
GET /spaces/{{spaceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSpace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [spaceId](#API_GetSpace_RequestSyntax) **   <a name="repostprivate-GetSpace-request-uri-spaceId"></a>
The ID of the private re:Post.
Required: Yes

## Request Body
<a name="API_GetSpace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSpace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string",
   "arn": "string",
   "clientId": "string",
   "configurationStatus": "string",
   "contentSize": number,
   "createDateTime": "string",
   "customerRoleArn": "string",
   "deleteDateTime": "string",
   "description": "string",
   "groupAdmins": [ "string" ],
   "identityStoreId": "string",
   "name": "string",
   "randomDomain": "string",
   "roles": {
      "string" : [ "string" ]
   },
   "spaceId": "string",
   "status": "string",
   "storageLimit": number,
   "supportedEmailDomains": {
      "allowedDomains": [ "string" ],
      "enabled": "string"
   },
   "tier": "string",
   "userAdmins": [ "string" ],
   "userCount": number,
   "userKMSKey": "string",
   "vanityDomain": "string",
   "vanityDomainStatus": "string"
}
```

## Response Elements
<a name="API_GetSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-applicationArn"></a>

Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [arn](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-arn"></a>
The ARN of the private re:Post.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [clientId](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-clientId"></a>
The Identity Center identifier for the Application Instance.
Type: String

 ** [configurationStatus](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-configurationStatus"></a>
The configuration status of the private re:Post.
Type: String
Valid Values: `CONFIGURED | UNCONFIGURED`

 ** [contentSize](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-contentSize"></a>
The content size of the private re:Post.
Type: Long

 ** [createDateTime](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-createDateTime"></a>
The date when the private re:Post was created.
Type: Timestamp

 ** [customerRoleArn](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-customerRoleArn"></a>
The IAM role that grants permissions to the private re:Post to convert unanswered questions into AWS support tickets.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [deleteDateTime](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-deleteDateTime"></a>
The date when the private re:Post was deleted.
Type: Timestamp

 ** [description](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-description"></a>
The description of the private re:Post.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [groupAdmins](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-groupAdmins"></a>
 *This parameter has been deprecated.*
The list of groups that are administrators of the private re:Post.
Type: Array of strings

 ** [identityStoreId](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-identityStoreId"></a>

Type: String

 ** [name](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-name"></a>
The name of the private re:Post.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.

 ** [randomDomain](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-randomDomain"></a>
The AWS generated subdomain of the private re:Post
Type: String

 ** [roles](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-roles"></a>
A map of accessor identifiers and their roles.
Type: String to array of strings map
Valid Values: `EXPERT | MODERATOR | ADMINISTRATOR | SUPPORTREQUESTOR`

 ** [spaceId](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-spaceId"></a>
The unique ID of the private re:Post.
Type: String

 ** [status](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-status"></a>
The creation or deletion status of the private re:Post.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.

 ** [storageLimit](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-storageLimit"></a>
The storage limit of the private re:Post.
Type: Long

 ** [supportedEmailDomains](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-supportedEmailDomains"></a>

Type: [SupportedEmailDomainsStatus](API_SupportedEmailDomainsStatus.md) object

 ** [tier](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-tier"></a>
The pricing tier of the private re:Post.
Type: String
Valid Values: `BASIC | STANDARD`

 ** [userAdmins](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-userAdmins"></a>
 *This parameter has been deprecated.*
The list of users that are administrators of the private re:Post.
Type: Array of strings

 ** [userCount](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-userCount"></a>
The number of users that have onboarded to the private re:Post.
Type: Integer

 ** [userKMSKey](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-userKMSKey"></a>
The custom AWS KMS key ARN that’s used for the AWS KMS encryption.
Type: String

 ** [vanityDomain](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-vanityDomain"></a>
The custom subdomain that you use to access your private re:Post. All custom subdomains must be approved by AWS before use.
Type: String

 ** [vanityDomainStatus](#API_GetSpace_ResponseSyntax) **   <a name="repostprivate-GetSpace-response-vanityDomainStatus"></a>
The approval status of the custom subdomain.
Type: String
Valid Values: `PENDING | APPROVED | UNAPPROVED`

## Errors
<a name="API_GetSpace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
The code to identify the quota.
 ** retryAfterSeconds **
 Advice to clients on when the call can be safely retried.
 ** serviceCode **
The code to identify the service.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The field that caused the error, if applicable.
 ** reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/repostspace-2022-05-13/GetSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/repostspace-2022-05-13/GetSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/repostspace-2022-05-13/GetSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/repostspace-2022-05-13/GetSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/repostspace-2022-05-13/GetSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/repostspace-2022-05-13/GetSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/repostspace-2022-05-13/GetSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/repostspace-2022-05-13/GetSpace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/repostspace-2022-05-13/GetSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/repostspace-2022-05-13/GetSpace)
