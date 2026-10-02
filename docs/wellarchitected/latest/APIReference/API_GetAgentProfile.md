---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentProfile.html
---

# GetAgentProfile
<a name="API_GetAgentProfile"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

**Important**
Organizational profiles are not available during the preview release.

Retrieves detailed information about an optimization profile, including its configuration and metadata.

## Request Syntax
<a name="API_GetAgentProfile_RequestSyntax"></a>

```
GET /api/v1/agent-profiles/{{profileArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAgentProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileArn](#API_GetAgentProfile_RequestSyntax) **   <a name="wellarchitected-GetAgentProfile-request-uri-profileArn"></a>
The Amazon Resource Name (ARN) of the optimization profile to retrieve.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_GetAgentProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgentProfile_ResponseSyntax"></a>

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
   "pillars": [ "string" ],
   "profileType": "string",
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetAgentProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregationConfiguration](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-aggregationConfiguration"></a>
The aggregation configuration. Not present for basic profiles.
Type: Array of [AggregationConfiguration](API_AggregationConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [arn](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-arn"></a>
The Amazon Resource Name (ARN) of the profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`

 ** [businessOverview](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-businessOverview"></a>
The business overview of the profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`

 ** [createdAt](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-createdAt"></a>
The timestamp when the profile was created.
Type: Timestamp

 ** [createdBy](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-createdBy"></a>
The identifier of the user or system that created this profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [deletionProtection](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-deletionProtection"></a>
Indicates whether deletion protection is enabled.
Type: Boolean

 ** [description](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-description"></a>
A description of the profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`

 ** [displayName](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-displayName"></a>
The display name of the profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`

 ** [eligibleForArchitectureGeneration](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-eligibleForArchitectureGeneration"></a>
Indicates whether the profile is valid for manual architecture generation.
Type: Boolean

 ** [eligibleForScheduledGeneration](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-eligibleForScheduledGeneration"></a>
Indicates whether the profile is valid for scheduled recommendation generation.
Type: Boolean

 ** [executionRoleArn](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-executionRoleArn"></a>
The ARN of the IAM execution role. Not present for basic profiles.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:([a-z\-]+):iam::\d{12}:role/(service-role/)?[a-zA-Z0-9+=,.@\-_]+`

 ** [fieldErrors](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-fieldErrors"></a>
A map of field paths to error messages for invalid or missing input fields.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Value Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [lastModifiedAt](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-lastModifiedAt"></a>
The timestamp when the profile was last modified.
Type: Timestamp

 ** [lastModifiedBy](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-lastModifiedBy"></a>
The identifier of the user or system that last modified this profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [name](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-name"></a>
The system name of the profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [organizationalAggregationConfiguration](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-organizationalAggregationConfiguration"></a>
This is not available during the preview release.
The organizational monitoring boundary. Present only for organizational profiles.
Type: [OrganizationalAggregationConfiguration](API_OrganizationalAggregationConfiguration.md) object

 ** [pillars](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-pillars"></a>
The AWS Well-Architected Framework pillars associated with the profile. Not present for basic profiles.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`

 ** [profileType](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-profileType"></a>
The type of the profile. `ORGANIZATIONAL` is not available during the preview release.
Type: String
Valid Values: `STANDARD | BASIC | ORGANIZATIONAL`

 ** [tags](#API_GetAgentProfile_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfile-response-tags"></a>
The tags associated with the profile.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_GetAgentProfile_Errors"></a>

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
<a name="API_GetAgentProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetAgentProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetAgentProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetAgentProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetAgentProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetAgentProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetAgentProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetAgentProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetAgentProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetAgentProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetAgentProfile)
