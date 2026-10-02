---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentOrganizationalProfile.html
---

# CreateAgentOrganizationalProfile
<a name="API_CreateAgentOrganizationalProfile"></a>

**Important**
This operation is not available during the preview release.

Creates an Organizational Profile for use with AWS Organizations integration. Organizational Profiles are scoped to an AWS Organization and do not require an execution role or aggregation configuration. The organization is inferred from the caller's identity.

## Request Syntax
<a name="API_CreateAgentOrganizationalProfile_RequestSyntax"></a>

```
POST /api/v1/agent-organizational-profiles HTTP/1.1
Content-type: application/json

{
   "businessOverview": "{{string}}",
   "clientToken": "{{string}}",
   "deletionProtection": {{boolean}},
   "description": "{{string}}",
   "displayName": "{{string}}",
   "name": "{{string}}",
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
   "pillars": [ "{{string}}" ],
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAgentOrganizationalProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAgentOrganizationalProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [businessOverview](#API_CreateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-request-businessOverview"></a>
The business overview for this organizational profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`
Required: No

 ** [clientToken](#API_CreateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [deletionProtection](#API_CreateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-request-deletionProtection"></a>
Indicates whether deletion protection is enabled for the organizational profile.
Type: Boolean
Required: No

 ** [description](#API_CreateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-request-description"></a>
A description of the organizational profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`
Required: No

 ** [displayName](#API_CreateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-request-displayName"></a>
The display name of the organizational profile shown to users.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: No

 ** [name](#API_CreateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-request-name"></a>
The system name of the organizational profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [organizationalAggregationConfiguration](#API_CreateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-request-organizationalAggregationConfiguration"></a>
This is not available during the preview release.
The organizational monitoring boundary. Contains organizational unit or root entries and individual account entries that define the scope for the profile.
Type: [OrganizationalAggregationConfiguration](API_OrganizationalAggregationConfiguration.md) object
Required: No

 ** [pillars](#API_CreateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-request-pillars"></a>
The AWS Well-Architected Framework pillars to associate with this organizational profile.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: Yes

 ** [tags](#API_CreateAgentOrganizationalProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-request-tags"></a>
The tags to associate with the organizational profile.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateAgentOrganizationalProfile_ResponseSyntax"></a>

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
<a name="API_CreateAgentOrganizationalProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-arn"></a>
The Amazon Resource Name (ARN) of the created organizational profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`

 ** [businessOverview](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-businessOverview"></a>
The business overview of the created organizational profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`

 ** [createdAt](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-createdAt"></a>
The timestamp when the organizational profile was created.
Type: Timestamp

 ** [createdBy](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-createdBy"></a>
The identifier of the user or system that created this organizational profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [deletionProtection](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-deletionProtection"></a>
Indicates whether deletion protection is enabled.
Type: Boolean

 ** [description](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-description"></a>
A description of the created organizational profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`

 ** [displayName](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-displayName"></a>
The display name of the created organizational profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`

 ** [eligibleForArchitectureGeneration](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-eligibleForArchitectureGeneration"></a>
Indicates whether the profile is valid for manual architecture generation.
Type: Boolean

 ** [eligibleForScheduledGeneration](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-eligibleForScheduledGeneration"></a>
Indicates whether the profile is valid for scheduled recommendation generation.
Type: Boolean

 ** [fieldErrors](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-fieldErrors"></a>
A map of field paths to error messages for invalid or missing input fields.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Value Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [lastModifiedAt](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-lastModifiedAt"></a>
The timestamp when the organizational profile was last modified.
Type: Timestamp

 ** [lastModifiedBy](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-lastModifiedBy"></a>
The identifier of the user or system that last modified this organizational profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [name](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-name"></a>
The system name of the created organizational profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [organizationalAggregationConfiguration](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-organizationalAggregationConfiguration"></a>
This is not available during the preview release.
The organizational monitoring boundary for the created profile. Present only for organizational profiles.
Type: [OrganizationalAggregationConfiguration](API_OrganizationalAggregationConfiguration.md) object

 ** [organizationId](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-organizationId"></a>
The identifier of the AWS Organization this profile belongs to.
Type: String

 ** [pillars](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-pillars"></a>
The AWS Well-Architected Framework pillars associated with the created organizational profile.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`

 ** [tags](#API_CreateAgentOrganizationalProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalProfile-response-tags"></a>
The tags associated with the created organizational profile.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_CreateAgentOrganizationalProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The user has reached their resource quota.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 402

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
<a name="API_CreateAgentOrganizationalProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/CreateAgentOrganizationalProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/CreateAgentOrganizationalProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CreateAgentOrganizationalProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/CreateAgentOrganizationalProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CreateAgentOrganizationalProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/CreateAgentOrganizationalProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/CreateAgentOrganizationalProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/CreateAgentOrganizationalProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/CreateAgentOrganizationalProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CreateAgentOrganizationalProfile)
