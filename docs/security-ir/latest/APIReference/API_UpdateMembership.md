---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateMembership.html
---

# UpdateMembership
<a name="API_UpdateMembership"></a>

Updates membership configuration.

## Request Syntax
<a name="API_UpdateMembership_RequestSyntax"></a>

```
PUT /v1/membership/{{membershipId}}/update-membership HTTP/1.1
Content-type: application/json

{
   "incidentResponseTeam": [
      {
         "communicationPreferences": [ "{{string}}" ],
         "email": "{{string}}",
         "jobTitle": "{{string}}",
         "name": "{{string}}"
      }
   ],
   "membershipAccountsConfigurationsUpdate": {
      "coverEntireOrganization": {{boolean}},
      "organizationalUnitsToAdd": [ "{{string}}" ],
      "organizationalUnitsToRemove": [ "{{string}}" ]
   },
   "membershipName": "{{string}}",
   "optInFeatures": [
      {
         "featureName": "{{string}}",
         "isEnabled": {{boolean}}
      }
   ],
   "undoMembershipCancellation": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipId](#API_UpdateMembership_RequestSyntax) **   <a name="securityir-UpdateMembership-request-uri-membershipId"></a>
Required element for UpdateMembership to identify the membership to update.
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `m-[a-z0-9]{10,32}`
Required: Yes

## Request Body
<a name="API_UpdateMembership_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [incidentResponseTeam](#API_UpdateMembership_RequestSyntax) **   <a name="securityir-UpdateMembership-request-incidentResponseTeam"></a>
Optional element for UpdateMembership to update the membership name.
Type: Array of [IncidentResponder](API_IncidentResponder.md) objects
Array Members: Minimum number of 2 items. Maximum number of 10 items.
Required: No

 ** [membershipAccountsConfigurationsUpdate](#API_UpdateMembership_RequestSyntax) **   <a name="securityir-UpdateMembership-request-membershipAccountsConfigurationsUpdate"></a>
The `membershipAccountsConfigurationsUpdate` field in the `UpdateMembershipRequest` structure allows you to update the configuration settings for accounts within a membership.
This field is optional and contains a structure of type `MembershipAccountsConfigurationsUpdate ` that specifies the updated account configurations for the membership.
Type: [MembershipAccountsConfigurationsUpdate](API_MembershipAccountsConfigurationsUpdate.md) object
Required: No

 ** [membershipName](#API_UpdateMembership_RequestSyntax) **   <a name="securityir-UpdateMembership-request-membershipName"></a>
Optional element for UpdateMembership to update the membership name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 50.
Required: No

 ** [optInFeatures](#API_UpdateMembership_RequestSyntax) **   <a name="securityir-UpdateMembership-request-optInFeatures"></a>
Optional element for UpdateMembership to enable or disable opt-in features for the service.
Type: Array of [OptInFeature](API_OptInFeature.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [undoMembershipCancellation](#API_UpdateMembership_RequestSyntax) **   <a name="securityir-UpdateMembership-request-undoMembershipCancellation"></a>
When set to true, reverses a previous membership cancellation and restores the membership to active status.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateMembership_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateMembership_Errors"></a>

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
<a name="API_UpdateMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/UpdateMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/UpdateMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/UpdateMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/UpdateMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/UpdateMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/UpdateMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/UpdateMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/UpdateMembership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/UpdateMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/UpdateMembership)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
