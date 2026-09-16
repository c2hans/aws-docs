---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CreateMembership.html
---

# CreateMembership
<a name="API_CreateMembership"></a>

Creates a new membership.

## Request Syntax
<a name="API_CreateMembership_RequestSyntax"></a>

```
POST /v1/membership HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "coverEntireOrganization": {{boolean}},
   "incidentResponseTeam": [
      {
         "communicationPreferences": [ "{{string}}" ],
         "email": "{{string}}",
         "jobTitle": "{{string}}",
         "name": "{{string}}"
      }
   ],
   "membershipName": "{{string}}",
   "optInFeatures": [
      {
         "featureName": "{{string}}",
         "isEnabled": {{boolean}}
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateMembership_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMembership_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateMembership_RequestSyntax) **   <a name="securityir-CreateMembership-request-clientToken"></a>
The `clientToken` field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [coverEntireOrganization](#API_CreateMembership_RequestSyntax) **   <a name="securityir-CreateMembership-request-coverEntireOrganization"></a>
The `coverEntireOrganization` parameter is a boolean flag that determines whether the membership should be applied to the entire AWS Organization. When set to true, the membership will be created for all accounts within the organization. When set to false, the membership will only be created for specified accounts.
This parameter is optional. If not specified, the default value is false.
+ If set to *true*: The membership will automatically include all existing and future accounts in the AWS Organization.
+ If set to *false*: The membership will only apply to explicitly specified accounts.
Type: Boolean
Required: No

 ** [incidentResponseTeam](#API_CreateMembership_RequestSyntax) **   <a name="securityir-CreateMembership-request-incidentResponseTeam"></a>
Required element used in combination with CreateMembership to add customer incident response team members and trusted partners to the membership.
Type: Array of [IncidentResponder](API_IncidentResponder.md) objects
Array Members: Minimum number of 2 items. Maximum number of 10 items.
Required: Yes

 ** [membershipName](#API_CreateMembership_RequestSyntax) **   <a name="securityir-CreateMembership-request-membershipName"></a>
Required element used in combination with CreateMembership to create a name for the membership.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 50.
Required: Yes

 ** [optInFeatures](#API_CreateMembership_RequestSyntax) **   <a name="securityir-CreateMembership-request-optInFeatures"></a>
A list of optional features to enable for the membership. These features provide additional capabilities beyond the standard membership functionality.
Type: Array of [OptInFeature](API_OptInFeature.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [tags](#API_CreateMembership_RequestSyntax) **   <a name="securityir-CreateMembership-request-tags"></a>
Optional element for customer configured tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateMembership_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "membershipId": "string"
}
```

## Response Elements
<a name="API_CreateMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [membershipId](#API_CreateMembership_ResponseSyntax) **   <a name="securityir-CreateMembership-response-membershipId"></a>
Response element for CreateMembership providing the newly created membership ID.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `m-[a-z0-9]{10,32}`

## Errors
<a name="API_CreateMembership_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** message **
The ID of the resource which lead to the access denial.
HTTP Status Code: 403

 ** ConflictException **
Returned when there is a conflict with the current state of the resource.
For UpdateResolverType, this error may occur when attempting to change an AWS-supported case to Self-managed, which is not supported.
 ** message **
The exception message.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **

 ** message **
The exception message.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
HTTP Status Code: 500

 ** InvalidTokenException **

 ** message **
The exception message.
HTTP Status Code: 423

 ** ResourceNotFoundException **

 ** message **
The exception message.
HTTP Status Code: 404

 ** SecurityIncidentResponseNotActiveException **

 ** message **
The exception message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

 ** message **
The exception message.
 ** quotaCode **
The code of the quota.
 ** resourceId **
The ID of the requested resource which lead to the service quota exception.
 ** resourceType **
The type of the requested resource which lead to the service quota exception.
 ** serviceCode **
The service code of the quota.
HTTP Status Code: 402

 ** ThrottlingException **

 ** message **
The exception message.
 ** quotaCode **
The quota code of the exception.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
 ** serviceCode **
The service code of the exception.
HTTP Status Code: 429

 ** ValidationException **
Returned when the request contains invalid parameters.
For UpdateResolverType, this error may occur when attempting an unsupported resolver type transition.
 ** fieldList **
The fields which lead to the exception.
 ** message **
The exception message.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/CreateMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/CreateMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/CreateMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/CreateMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/CreateMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/CreateMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/CreateMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/CreateMembership)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/CreateMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/CreateMembership)
