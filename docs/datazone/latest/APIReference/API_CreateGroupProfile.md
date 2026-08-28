---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateGroupProfile.html
---

# CreateGroupProfile
<a name="API_CreateGroupProfile"></a>

Creates a group profile in Amazon DataZone.

## Request Syntax
<a name="API_CreateGroupProfile_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/group-profiles HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "groupIdentifier": "{{string}}",
   "rolePrincipalArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateGroupProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateGroupProfile_RequestSyntax) **   <a name="datazone-CreateGroupProfile-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which the group profile is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateGroupProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateGroupProfile_RequestSyntax) **   <a name="datazone-CreateGroupProfile-request-clientToken"></a>
 A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Required: No

 ** [groupIdentifier](#API_CreateGroupProfile_RequestSyntax) **   <a name="datazone-CreateGroupProfile-request-groupIdentifier"></a>
The identifier of the group for which the group profile is created.
Type: String
Pattern: `.*(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r ]+).*`
Required: No

 ** [rolePrincipalArn](#API_CreateGroupProfile_RequestSyntax) **   <a name="datazone-CreateGroupProfile-request-rolePrincipalArn"></a>
The ARN of the IAM role that will be associated with the group profile. This role defines the permissions that group members will assume when accessing Amazon DataZone resources.
Type: String
Required: No

## Response Syntax
<a name="API_CreateGroupProfile_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "domainId": "string",
   "groupName": "string",
   "id": "string",
   "rolePrincipalArn": "string",
   "rolePrincipalId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateGroupProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [domainId](#API_CreateGroupProfile_ResponseSyntax) **   <a name="datazone-CreateGroupProfile-response-domainId"></a>
The identifier of the Amazon DataZone domain in which the group profile is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [groupName](#API_CreateGroupProfile_ResponseSyntax) **   <a name="datazone-CreateGroupProfile-response-groupName"></a>
The name of the group for which group profile is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9+=,.@-]+`

 ** [id](#API_CreateGroupProfile_ResponseSyntax) **   <a name="datazone-CreateGroupProfile-response-id"></a>
The identifier of the group profile.
Type: String
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [rolePrincipalArn](#API_CreateGroupProfile_ResponseSyntax) **   <a name="datazone-CreateGroupProfile-response-rolePrincipalArn"></a>
The ARN of the IAM role principal. This role is associated with the group profile.
Type: String

 ** [rolePrincipalId](#API_CreateGroupProfile_ResponseSyntax) **   <a name="datazone-CreateGroupProfile-response-rolePrincipalId"></a>
The unique identifier of the IAM role principal. This principal is associated with the group profile.
Type: String

 ** [status](#API_CreateGroupProfile_ResponseSyntax) **   <a name="datazone-CreateGroupProfile-response-status"></a>
The status of the group profile.
Type: String
Valid Values: `ASSIGNED | NOT_ASSIGNED`

## Errors
<a name="API_CreateGroupProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_CreateGroupProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateGroupProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateGroupProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateGroupProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateGroupProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateGroupProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateGroupProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateGroupProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateGroupProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateGroupProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateGroupProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
