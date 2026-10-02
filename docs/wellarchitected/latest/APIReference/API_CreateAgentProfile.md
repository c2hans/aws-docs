---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentProfile.html
---

# CreateAgentProfile
<a name="API_CreateAgentProfile"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Creates an optimization profile that defines the scope and configuration for generating recommendations. A profile specifies the execution role, target pillars, and aggregation settings for analyzing your AWS resources.

## Request Syntax
<a name="API_CreateAgentProfile_RequestSyntax"></a>

```
POST /api/v1/agent-profiles HTTP/1.1
Content-type: application/json

{
   "aggregationConfiguration": [
      {
         "accessRoleArn": "{{string}}",
         "accountId": "{{string}}",
         "regions": [ "{{string}}" ]
      }
   ],
   "businessOverview": "{{string}}",
   "clientToken": "{{string}}",
   "deletionProtection": {{boolean}},
   "description": "{{string}}",
   "displayName": "{{string}}",
   "executionRoleArn": "{{string}}",
   "name": "{{string}}",
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
<a name="API_CreateAgentProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAgentProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aggregationConfiguration](#API_CreateAgentProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentProfile-request-aggregationConfiguration"></a>
The aggregation configuration that defines which AWS accounts and Regions to analyze.
Type: Array of [AggregationConfiguration](API_AggregationConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** [businessOverview](#API_CreateAgentProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentProfile-request-businessOverview"></a>
The business overview for this profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`
Required: No

 ** [clientToken](#API_CreateAgentProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentProfile-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [deletionProtection](#API_CreateAgentProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentProfile-request-deletionProtection"></a>
Indicates whether deletion protection is enabled for the profile.
Type: Boolean
Required: No

 ** [description](#API_CreateAgentProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentProfile-request-description"></a>
A description of the profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`
Required: No

 ** [displayName](#API_CreateAgentProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentProfile-request-displayName"></a>
The display name of the profile shown to users.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: No

 ** [executionRoleArn](#API_CreateAgentProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentProfile-request-executionRoleArn"></a>
The ARN of the IAM execution role used for recommendation actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:([a-z\-]+):iam::\d{12}:role/(service-role/)?[a-zA-Z0-9+=,.@\-_]+`
Required: Yes

 ** [name](#API_CreateAgentProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentProfile-request-name"></a>
The system name of the profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [pillars](#API_CreateAgentProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentProfile-request-pillars"></a>
The AWS Well-Architected Framework pillars to associate with this profile.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: Yes

 ** [tags](#API_CreateAgentProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentProfile-request-tags"></a>
The tags to associate with the profile.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateAgentProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aggregationConfiguration": [
      {
         "accessRoleArn": "string",
         "accountId": "string",
         "regions": [ "string" ]
      }
   ],
   "arn": "string",
   "businessOverview": "string",
   "createdAt": "string",
   "createdBy": "string",
   "deletionProtection": boolean,
   "description": "string",
   "displayName": "string",
   "eligibleForArchitectureGeneration": boolean,
   "eligibleForScheduledGeneration": boolean,
   "executionRoleArn": "string",
   "fieldErrors": {
      "string" : "string"
   },
   "lastModifiedAt": "string",
   "lastModifiedBy": "string",
   "name": "string",
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
<a name="API_CreateAgentProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregationConfiguration](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-aggregationConfiguration"></a>
The aggregation configuration.
Type: Array of [AggregationConfiguration](API_AggregationConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [arn](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-arn"></a>
The Amazon Resource Name (ARN) of the created profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`

 ** [businessOverview](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-businessOverview"></a>
The business overview of the created profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`

 ** [createdAt](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-createdAt"></a>
The timestamp when the profile was created.
Type: Timestamp

 ** [createdBy](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-createdBy"></a>
The identifier of the user or system that created this profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [deletionProtection](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-deletionProtection"></a>
Indicates whether deletion protection is enabled.
Type: Boolean

 ** [description](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-description"></a>
A description of the created profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`

 ** [displayName](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-displayName"></a>
The display name of the created profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`

 ** [eligibleForArchitectureGeneration](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-eligibleForArchitectureGeneration"></a>
Indicates whether the profile is valid for manual architecture generation.
Type: Boolean

 ** [eligibleForScheduledGeneration](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-eligibleForScheduledGeneration"></a>
Indicates whether the profile is valid for scheduled recommendation generation.
Type: Boolean

 ** [executionRoleArn](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-executionRoleArn"></a>
The ARN of the IAM execution role.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:([a-z\-]+):iam::\d{12}:role/(service-role/)?[a-zA-Z0-9+=,.@\-_]+`

 ** [fieldErrors](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-fieldErrors"></a>
A map of field paths to error messages for invalid or missing input fields.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Value Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [lastModifiedAt](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-lastModifiedAt"></a>
The timestamp when the profile was last modified.
Type: Timestamp

 ** [lastModifiedBy](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-lastModifiedBy"></a>
The identifier of the user or system that last modified this profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [name](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-name"></a>
The system name of the created profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [pillars](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-pillars"></a>
The AWS Well-Architected Framework pillars associated with the created profile.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`

 ** [tags](#API_CreateAgentProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentProfile-response-tags"></a>
The tags associated with the created profile.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_CreateAgentProfile_Errors"></a>

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
<a name="API_CreateAgentProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/CreateAgentProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/CreateAgentProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CreateAgentProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/CreateAgentProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CreateAgentProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/CreateAgentProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/CreateAgentProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/CreateAgentProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/CreateAgentProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CreateAgentProfile)
