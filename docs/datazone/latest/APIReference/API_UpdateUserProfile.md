---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateUserProfile.html
---

# UpdateUserProfile
<a name="API_UpdateUserProfile"></a>

Updates the specified user profile in Amazon DataZone.

## Request Syntax
<a name="API_UpdateUserProfile_RequestSyntax"></a>

```
PUT /v2/domains/{{domainIdentifier}}/user-profiles/{{userIdentifier}} HTTP/1.1
Content-type: application/json

{
   "sessionName": "{{string}}",
   "status": "{{string}}",
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateUserProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateUserProfile_RequestSyntax) **   <a name="datazone-UpdateUserProfile-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which a user profile is updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [userIdentifier](#API_UpdateUserProfile_RequestSyntax) **   <a name="datazone-UpdateUserProfile-request-uri-userIdentifier"></a>
The identifier of the user whose user profile is to be updated.
Pattern: `.*(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|^[a-zA-Z_0-9+=,.@-]+$|^arn:aws:iam::\d{12}:.+$).*`
Required: Yes

## Request Body
<a name="API_UpdateUserProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sessionName](#API_UpdateUserProfile_RequestSyntax) **   <a name="datazone-UpdateUserProfile-request-sessionName"></a>
The session name for IAM role sessions.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: No

 ** [status](#API_UpdateUserProfile_RequestSyntax) **   <a name="datazone-UpdateUserProfile-request-status"></a>
The status of the user profile that are to be updated.
Type: String
Valid Values: `ASSIGNED | NOT_ASSIGNED | ACTIVATED | DEACTIVATED`
Required: Yes

 ** [type](#API_UpdateUserProfile_RequestSyntax) **   <a name="datazone-UpdateUserProfile-request-type"></a>
The type of the user profile that are to be updated.
Type: String
Valid Values: `IAM | SSO`
Required: No

## Response Syntax
<a name="API_UpdateUserProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "details": { ... },
   "domainId": "string",
   "id": "string",
   "status": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_UpdateUserProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [details](#API_UpdateUserProfile_ResponseSyntax) **   <a name="datazone-UpdateUserProfile-response-details"></a>
The results of the UpdateUserProfile action.
Type: [UserProfileDetails](API_UserProfileDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [domainId](#API_UpdateUserProfile_ResponseSyntax) **   <a name="datazone-UpdateUserProfile-response-domainId"></a>
The identifier of the Amazon DataZone domain in which a user profile is updated.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_UpdateUserProfile_ResponseSyntax) **   <a name="datazone-UpdateUserProfile-response-id"></a>
The identifier of the user profile.
Type: String
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [status](#API_UpdateUserProfile_ResponseSyntax) **   <a name="datazone-UpdateUserProfile-response-status"></a>
The status of the user profile.
Type: String
Valid Values: `ASSIGNED | NOT_ASSIGNED | ACTIVATED | DEACTIVATED`

 ** [type](#API_UpdateUserProfile_ResponseSyntax) **   <a name="datazone-UpdateUserProfile-response-type"></a>
The type of the user profile.
Type: String
Valid Values: `IAM | SSO`

## Errors
<a name="API_UpdateUserProfile_Errors"></a>

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
<a name="API_UpdateUserProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateUserProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateUserProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateUserProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateUserProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateUserProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateUserProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateUserProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateUserProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateUserProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateUserProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
