---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateGroupProfile.html
---

# UpdateGroupProfile
<a name="API_UpdateGroupProfile"></a>

Updates the specified group profile in Amazon DataZone.

## Request Syntax
<a name="API_UpdateGroupProfile_RequestSyntax"></a>

```
PUT /v2/domains/{{domainIdentifier}}/group-profiles/{{groupIdentifier}} HTTP/1.1
Content-type: application/json

{
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateGroupProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateGroupProfile_RequestSyntax) **   <a name="datazone-UpdateGroupProfile-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which a group profile is updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [groupIdentifier](#API_UpdateGroupProfile_RequestSyntax) **   <a name="datazone-UpdateGroupProfile-request-uri-groupIdentifier"></a>
The identifier of the group profile that is updated.
Pattern: `.*(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r ]+).*`
Required: Yes

## Request Body
<a name="API_UpdateGroupProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [status](#API_UpdateGroupProfile_RequestSyntax) **   <a name="datazone-UpdateGroupProfile-request-status"></a>
The status of the group profile that is updated.
Type: String
Valid Values: `ASSIGNED | NOT_ASSIGNED`
Required: Yes

## Response Syntax
<a name="API_UpdateGroupProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateGroupProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainId](#API_UpdateGroupProfile_ResponseSyntax) **   <a name="datazone-UpdateGroupProfile-response-domainId"></a>
The identifier of the Amazon DataZone domain in which a group profile is updated.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [groupName](#API_UpdateGroupProfile_ResponseSyntax) **   <a name="datazone-UpdateGroupProfile-response-groupName"></a>
The name of the group profile that is updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9+=,.@-]+`

 ** [id](#API_UpdateGroupProfile_ResponseSyntax) **   <a name="datazone-UpdateGroupProfile-response-id"></a>
The identifier of the group profile that is updated.
Type: String
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [rolePrincipalArn](#API_UpdateGroupProfile_ResponseSyntax) **   <a name="datazone-UpdateGroupProfile-response-rolePrincipalArn"></a>
The ARN of the IAM role principal. This role is associated with the updated group profile.
Type: String

 ** [rolePrincipalId](#API_UpdateGroupProfile_ResponseSyntax) **   <a name="datazone-UpdateGroupProfile-response-rolePrincipalId"></a>
The unique identifier of the IAM role principal. This principal is associated with the updated group profile.
Type: String

 ** [status](#API_UpdateGroupProfile_ResponseSyntax) **   <a name="datazone-UpdateGroupProfile-response-status"></a>
The status of the group profile that is updated.
Type: String
Valid Values: `ASSIGNED | NOT_ASSIGNED`

## Errors
<a name="API_UpdateGroupProfile_Errors"></a>

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
<a name="API_UpdateGroupProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateGroupProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateGroupProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateGroupProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateGroupProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateGroupProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateGroupProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateGroupProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateGroupProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateGroupProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateGroupProfile)
