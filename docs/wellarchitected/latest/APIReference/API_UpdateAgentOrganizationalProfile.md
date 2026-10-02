---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentOrganizationalProfile.html
---

# UpdateAgentOrganizationalProfile
<a name="API_UpdateAgentOrganizationalProfile"></a>

**Important**
This operation is not available during the preview release.

Updates an Organizational Profile. Organizational Profiles are specific to Profiles created using AWS Organizations integration.

## Request Syntax
<a name="API_UpdateAgentOrganizationalProfile_RequestSyntax"></a>

```
PUT /api/v1/agent-organizational-profiles/{{profileArn}} HTTP/1.1
Content-type: application/json

{
   "businessOverview": "{{string}}",
   "clientToken": "{{string}}",
   "deletionProtection": {{boolean}},
   "description": "{{string}}",
   "displayName": "{{string}}",
   "organizationalAggregationConfiguration": {
      "accounts": [
         {
            "accountId": "{{string}}",
            "regions": [ "{{string}}" ]
         }
      ],
      "organizationalUnits": [
         {
            "organizationalUnitId": "{{string}}",
            "regions": [ "{{string}}" ]
         }
      ]
   },
   "pillars": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateAgentOrganizationalProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileArn](#API_UpdateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-request-uri-profileArn"></a>
The Amazon Resource Name (ARN) of the organizational profile to update.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_UpdateAgentOrganizationalProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [businessOverview](#API_UpdateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-request-businessOverview"></a>
The updated business overview for the organizational profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[\P{C}]*`
Required: No

 ** [clientToken](#API_UpdateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [deletionProtection](#API_UpdateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-request-deletionProtection"></a>
Indicates whether deletion protection is enabled for the organizational profile.
Type: Boolean
Required: No

 ** [description](#API_UpdateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-request-description"></a>
The updated description of the organizational profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[\P{C}]*`
Required: No

 ** [displayName](#API_UpdateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-request-displayName"></a>
The updated display name of the organizational profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[\P{C}]+`
Required: No

 ** [organizationalAggregationConfiguration](#API_UpdateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-request-organizationalAggregationConfiguration"></a>
This is not available during the preview release.
The organizational monitoring boundary. Contains organizational unit or root entries and individual account entries that define the scope for the profile.
Type: [OrganizationalAggregationConfiguration](API_OrganizationalAggregationConfiguration.md) object
Required: No

 ** [pillars](#API_UpdateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-request-pillars"></a>
The updated AWS Well-Architected Framework pillars for the organizational profile.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: No

## Response Syntax
<a name="API_UpdateAgentOrganizationalProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "businessOverview": "string",
   "createdAt": "string",
   "createdBy": "string",
   "deletionProtection": boolean,
   "description": "string",
   "displayName": "string",
   "eligibleForArchitectureGeneration": boolean,
   "eligibleForScheduledGeneration": boolean,
   "fieldErrors": {
      "string" : "string"
   },
   "lastModifiedAt": "string",
   "lastModifiedBy": "string",
   "name": "string",
   "organizationalAggregationConfiguration": {
      "accounts": [
         {
            "accountId": "string",
            "regions": [ "string" ]
         }
      ],
      "organizationalUnits": [
         {
            "organizationalUnitId": "string",
            "regions": [ "string" ]
         }
      ]
   },
   "organizationId": "string",
   "pillars": [ "string" ],
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_UpdateAgentOrganizationalProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-arn"></a>
The Amazon Resource Name (ARN) of the updated organizational profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`

 ** [businessOverview](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-businessOverview"></a>
The business overview of the updated organizational profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`

 ** [createdAt](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-createdAt"></a>
The timestamp when the organizational profile was created.
Type: Timestamp

 ** [createdBy](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-createdBy"></a>
The identifier of the user or system that created this organizational profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [deletionProtection](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-deletionProtection"></a>
Indicates whether deletion protection is enabled.
Type: Boolean

 ** [description](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-description"></a>
A description of the updated organizational profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`

 ** [displayName](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-displayName"></a>
The display name of the updated organizational profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`

 ** [eligibleForArchitectureGeneration](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-eligibleForArchitectureGeneration"></a>
Indicates whether the profile is valid for manual architecture generation.
Type: Boolean

 ** [eligibleForScheduledGeneration](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-eligibleForScheduledGeneration"></a>
Indicates whether the profile is valid for scheduled recommendation generation.
Type: Boolean

 ** [fieldErrors](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-fieldErrors"></a>
A map of field paths to error messages for invalid or missing input fields.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Value Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [lastModifiedAt](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-lastModifiedAt"></a>
The timestamp when the organizational profile was last modified.
Type: Timestamp

 ** [lastModifiedBy](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-lastModifiedBy"></a>
The identifier of the user or system that last modified this organizational profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [name](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-name"></a>
The system name of the updated organizational profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [organizationalAggregationConfiguration](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-organizationalAggregationConfiguration"></a>
This is not available during the preview release.
The organizational monitoring boundary for the updated profile.
Type: [OrganizationalAggregationConfiguration](API_OrganizationalAggregationConfiguration.md) object

 ** [organizationId](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-organizationId"></a>
The identifier of the AWS Organization this profile belongs to.
Type: String

 ** [pillars](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-pillars"></a>
The AWS Well-Architected Framework pillars associated with the updated organizational profile.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`

 ** [tags](#API_UpdateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentOrganizationalProfile-response-tags"></a>
The tags associated with the updated organizational profile.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_UpdateAgentOrganizationalProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAgentOrganizationalProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpdateAgentOrganizationalProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpdateAgentOrganizationalProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpdateAgentOrganizationalProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpdateAgentOrganizationalProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpdateAgentOrganizationalProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpdateAgentOrganizationalProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpdateAgentOrganizationalProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpdateAgentOrganizationalProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpdateAgentOrganizationalProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpdateAgentOrganizationalProfile)
