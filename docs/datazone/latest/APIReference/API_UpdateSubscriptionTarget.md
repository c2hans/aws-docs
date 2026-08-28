---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateSubscriptionTarget.html
---

# UpdateSubscriptionTarget
<a name="API_UpdateSubscriptionTarget"></a>

Updates the specified subscription target in Amazon DataZone.

## Request Syntax
<a name="API_UpdateSubscriptionTarget_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/environments/{{environmentIdentifier}}/subscription-targets/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "applicableAssetTypes": [ "{{string}}" ],
   "authorizedPrincipals": [ "{{string}}" ],
   "manageAccessRole": "{{string}}",
   "name": "{{string}}",
   "provider": "{{string}}",
   "subscriptionGrantCreationMode": "{{string}}",
   "subscriptionTargetConfig": [
      {
         "content": "{{string}}",
         "formName": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateSubscriptionTarget_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateSubscriptionTarget_RequestSyntax) **   <a name="datazone-UpdateSubscriptionTarget-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which a subscription target is to be updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentIdentifier](#API_UpdateSubscriptionTarget_RequestSyntax) **   <a name="datazone-UpdateSubscriptionTarget-request-uri-environmentIdentifier"></a>
The identifier of the environment in which a subscription target is to be updated.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateSubscriptionTarget_RequestSyntax) **   <a name="datazone-UpdateSubscriptionTarget-request-uri-identifier"></a>
Identifier of the subscription target that is to be updated.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateSubscriptionTarget_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicableAssetTypes](#API_UpdateSubscriptionTarget_RequestSyntax) **   <a name="datazone-UpdateSubscriptionTarget-request-applicableAssetTypes"></a>
The applicable asset types to be updated as part of the `UpdateSubscriptionTarget` action.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\.]*.*`
Required: No

 ** [authorizedPrincipals](#API_UpdateSubscriptionTarget_RequestSyntax) **   <a name="datazone-UpdateSubscriptionTarget-request-authorizedPrincipals"></a>
The authorized principals to be updated as part of the `UpdateSubscriptionTarget` action.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9:/._-]*`
Required: No

 ** [manageAccessRole](#API_UpdateSubscriptionTarget_RequestSyntax) **   <a name="datazone-UpdateSubscriptionTarget-request-manageAccessRole"></a>
The manage access role to be updated as part of the `UpdateSubscriptionTarget` action.
Type: String
Pattern: `arn:aws(|-cn|-us-gov):iam::\d{12}:(role|role/service-role)/[\w+=,.@-]*`
Required: No

 ** [name](#API_UpdateSubscriptionTarget_RequestSyntax) **   <a name="datazone-UpdateSubscriptionTarget-request-name"></a>
The name to be updated as part of the `UpdateSubscriptionTarget` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [provider](#API_UpdateSubscriptionTarget_RequestSyntax) **   <a name="datazone-UpdateSubscriptionTarget-request-provider"></a>
The provider to be updated as part of the `UpdateSubscriptionTarget` action.
Type: String
Required: No

 ** [subscriptionGrantCreationMode](#API_UpdateSubscriptionTarget_RequestSyntax) **   <a name="datazone-UpdateSubscriptionTarget-request-subscriptionGrantCreationMode"></a>
 Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: No

 ** [subscriptionTargetConfig](#API_UpdateSubscriptionTarget_RequestSyntax) **   <a name="datazone-UpdateSubscriptionTarget-request-subscriptionTargetConfig"></a>
The configuration to be updated as part of the `UpdateSubscriptionTarget` action.
Type: Array of [SubscriptionTargetForm](API_SubscriptionTargetForm.md) objects
Required: No

## Response Syntax
<a name="API_UpdateSubscriptionTarget_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicableAssetTypes": [ "string" ],
   "authorizedPrincipals": [ "string" ],
   "createdAt": number,
   "createdBy": "string",
   "domainId": "string",
   "environmentId": "string",
   "id": "string",
   "manageAccessRole": "string",
   "name": "string",
   "projectId": "string",
   "provider": "string",
   "subscriptionGrantCreationMode": "string",
   "subscriptionTargetConfig": [
      {
         "content": "string",
         "formName": "string"
      }
   ],
   "type": "string",
   "updatedAt": number,
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_UpdateSubscriptionTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicableAssetTypes](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-applicableAssetTypes"></a>
The applicable asset types to be updated as part of the `UpdateSubscriptionTarget` action.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\.]*.*`

 ** [authorizedPrincipals](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-authorizedPrincipals"></a>
The authorized principals to be updated as part of the `UpdateSubscriptionTarget` action. Updates are supported in batches of 5 at a time.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9:/._-]*`

 ** [createdAt](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-createdAt"></a>
The timestamp of when a subscription target was created.
Type: Timestamp

 ** [createdBy](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-createdBy"></a>
The Amazon DataZone user who created the subscription target.
Type: String

 ** [domainId](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-domainId"></a>
The identifier of the Amazon DataZone domain in which a subscription target is to be updated.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentId](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-environmentId"></a>
The identifier of the environment in which a subscription target is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-id"></a>
Identifier of the subscription target that is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [manageAccessRole](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-manageAccessRole"></a>
The manage access role to be updated as part of the `UpdateSubscriptionTarget` action.
Type: String
Pattern: `arn:aws(|-cn|-us-gov):iam::\d{12}:(role|role/service-role)/[\w+=,.@-]*`

 ** [name](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-name"></a>
The name to be updated as part of the `UpdateSubscriptionTarget` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [projectId](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-projectId"></a>
The identifier of the project in which a subscription target is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [provider](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-provider"></a>
The provider to be updated as part of the `UpdateSubscriptionTarget` action.
Type: String

 ** [subscriptionGrantCreationMode](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-subscriptionGrantCreationMode"></a>
 Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually.
Type: String
Valid Values: `AUTOMATIC | MANUAL`

 ** [subscriptionTargetConfig](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-subscriptionTargetConfig"></a>
The configuration to be updated as part of the `UpdateSubscriptionTarget` action.
Type: Array of [SubscriptionTargetForm](API_SubscriptionTargetForm.md) objects

 ** [type](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-type"></a>
The type to be updated as part of the `UpdateSubscriptionTarget` action.
Type: String

 ** [updatedAt](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-updatedAt"></a>
The timestamp of when the subscription target was updated.
Type: Timestamp

 ** [updatedBy](#API_UpdateSubscriptionTarget_ResponseSyntax) **   <a name="datazone-UpdateSubscriptionTarget-response-updatedBy"></a>
The Amazon DataZone user who updated the subscription target.
Type: String

## Errors
<a name="API_UpdateSubscriptionTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSubscriptionTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateSubscriptionTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateSubscriptionTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateSubscriptionTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateSubscriptionTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateSubscriptionTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateSubscriptionTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateSubscriptionTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateSubscriptionTarget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateSubscriptionTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateSubscriptionTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
