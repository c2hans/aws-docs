---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateProfile.html
---

# UpdateProfile
<a name="API_UpdateProfile"></a>

Updates a *profile*, a list of the roles that IAM Roles Anywhere service is trusted to assume. You use profiles to intersect permissions with IAM managed policies.

 **Required permissions: ** `rolesanywhere:UpdateProfile`.

## Request Syntax
<a name="API_UpdateProfile_RequestSyntax"></a>

```
PATCH /profile/{{profileId}} HTTP/1.1
Content-type: application/json

{
   "acceptRoleSessionName": {{boolean}},
   "aliasName": "{{string}}",
   "durationSeconds": {{number}},
   "managedPolicyArns": [ "{{string}}" ],
   "name": "{{string}}",
   "roleArns": [ "{{string}}" ],
   "sessionPolicy": "{{string}}",
   "tipConfiguration": {
      "status": "{{string}}",
      "subjectSource": "{{string}}",
      "subjectType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileId](#API_UpdateProfile_RequestSyntax) **   <a name="rolesanywhere-UpdateProfile-request-uri-profileId"></a>
The profile to act on. You can specify one of the following:
+ The profile ID.
+ The profile ARN.
+ The alias ARN of the profile.
An ARN must be for a profile in your account and Region.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `([a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}|arn:aws(-[^:]+)?:rolesanywhere(:.*){2}:(profile|alias/profile)/.*)`
Required: Yes

## Request Body
<a name="API_UpdateProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [acceptRoleSessionName](#API_UpdateProfile_RequestSyntax) **   <a name="rolesanywhere-UpdateProfile-request-acceptRoleSessionName"></a>
Used to determine if a custom role session name will be accepted in a temporary credential request.
Type: Boolean
Required: No

 ** [aliasName](#API_UpdateProfile_RequestSyntax) **   <a name="rolesanywhere-UpdateProfile-request-aliasName"></a>
The alias for the profile.
You can use this parameter in the following ways:
+ To set or change the alias, specify the new alias name. After the change, the previous alias ARN no longer identifies the resource. You can then assign the previous alias to another resource of the same type. A change can take a short time to take effect for requests that use an alias ARN.
+ To remove the alias, specify an empty string.
+ To keep the current alias, omit this parameter.
An alias name contains 1 to 256 characters. It must begin with a letter (A-Z or a-z). It can contain only letters (A-Z and a-z), numbers (0-9), underscores (\_), hyphens (-), and forward slashes (/). A forward slash can appear only between two other characters, so an alias name can't end with a forward slash or contain two in a row. Alias names that begin with `aws/`, in any combination of uppercase and lowercase letters, are reserved. Alias names are case sensitive.
The alias name must be unique among resources of the same type in your account and Region. If another resource of the same type already has the alias, the request fails with a `ValidationException`. An invalid or reserved alias name also causes a `ValidationException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?!.*//)([A-Za-z]([A-Za-z0-9_/-]*[A-Za-z0-9_-])?)?`
Required: No

 ** [durationSeconds](#API_UpdateProfile_RequestSyntax) **   <a name="rolesanywhere-UpdateProfile-request-durationSeconds"></a>
 Used to determine how long sessions vended using this profile are valid for. See the `Expiration` section of the [CreateSession API documentation](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object) page for more details. In requests, if this value is not provided, the default value will be 3600.
Type: Integer
Valid Range: Minimum value of 900. Maximum value of 43200.
Required: No

 ** [managedPolicyArns](#API_UpdateProfile_RequestSyntax) **   <a name="rolesanywhere-UpdateProfile-request-managedPolicyArns"></a>
A list of managed policy ARNs that apply to the vended session credentials.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** [name](#API_UpdateProfile_RequestSyntax) **   <a name="rolesanywhere-UpdateProfile-request-name"></a>
The name of the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[ a-zA-Z0-9-_]*`
Required: No

 ** [roleArns](#API_UpdateProfile_RequestSyntax) **   <a name="rolesanywhere-UpdateProfile-request-roleArns"></a>
A list of IAM roles that this profile can assume in a temporary credential request.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 250 items.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[^:]+)?:iam(:.*){2}(:role.*)`
Required: No

 ** [sessionPolicy](#API_UpdateProfile_RequestSyntax) **   <a name="rolesanywhere-UpdateProfile-request-sessionPolicy"></a>
A session policy that applies to the trust boundary of the vended session credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: No

 ** [tipConfiguration](#API_UpdateProfile_RequestSyntax) **   <a name="rolesanywhere-UpdateProfile-request-tipConfiguration"></a>
The trusted identity propagation (TIP) settings for the profile. The settings that you specify replace the current settings, and a field that you omit returns to its default. If you omit this parameter, the TIP settings don't change.
Type: [TipConfiguration](API_TipConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "profile": {
      "acceptRoleSessionName": boolean,
      "aliasArn": "string",
      "aliasName": "string",
      "attributeMappings": [
         {
            "certificateField": "string",
            "mappingRules": [
               {
                  "specifier": "string"
               }
            ]
         }
      ],
      "createdAt": "string",
      "createdBy": "string",
      "durationSeconds": number,
      "enabled": boolean,
      "managedPolicyArns": [ "string" ],
      "name": "string",
      "previousAliasName": "string",
      "profileArn": "string",
      "profileId": "string",
      "requireInstanceProperties": boolean,
      "roleArns": [ "string" ],
      "sessionPolicy": "string",
      "tipConfiguration": {
         "status": "string",
         "subjectSource": "string",
         "subjectType": "string"
      },
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_UpdateProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [profile](#API_UpdateProfile_ResponseSyntax) **   <a name="rolesanywhere-UpdateProfile-response-profile"></a>
The state of the profile after a read or write operation.
Type: [ProfileDetail](API_ProfileDetail.md) object

## Errors
<a name="API_UpdateProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The resource could not be found.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The request has failed due to a temporary failure of the service.
 ** message **
The exception message.
 ** retryAfterSeconds **
The recommended number of seconds after which the client should retry the request.
HTTP Status Code: 503

 ** ValidationException **
Validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_UpdateProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/UpdateProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/UpdateProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/UpdateProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/UpdateProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/UpdateProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/UpdateProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/UpdateProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/UpdateProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/UpdateProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/UpdateProfile)
