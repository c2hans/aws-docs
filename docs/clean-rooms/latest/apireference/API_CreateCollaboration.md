---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateCollaboration.html
---

# CreateCollaboration
<a name="API_CreateCollaboration"></a>

Creates a new collaboration.

## Request Syntax
<a name="API_CreateCollaboration_RequestSyntax"></a>

```
POST /collaborations HTTP/1.1
Content-type: application/json

{
   "allowedResultRegions": [ "{{string}}" ],
   "analyticsEngine": "{{string}}",
   "autoApprovedChangeRequestTypes": [ "{{string}}" ],
   "creatorDisplayName": "{{string}}",
   "creatorMemberAbilities": [ "{{string}}" ],
   "creatorMLMemberAbilities": {
      "customMLMemberAbilities": [ "{{string}}" ]
   },
   "creatorPaymentConfiguration": {
      "jobCompute": {
         "isResponsible": {{boolean}}
      },
      "machineLearning": {
         "modelInference": {
            "isResponsible": {{boolean}}
         },
         "modelTraining": {
            "isResponsible": {{boolean}}
         },
         "syntheticDataGeneration": {
            "isResponsible": {{boolean}}
         }
      },
      "queryCompute": {
         "isResponsible": {{boolean}}
      }
   },
   "dataEncryptionMetadata": {
      "allowCleartext": {{boolean}},
      "allowDuplicates": {{boolean}},
      "allowJoinsOnColumnsWithDifferentNames": {{boolean}},
      "preserveNulls": {{boolean}}
   },
   "description": "{{string}}",
   "isMetricsEnabled": {{boolean}},
   "jobLogStatus": "{{string}}",
   "members": [
      {
         "accountId": "{{string}}",
         "displayName": "{{string}}",
         "memberAbilities": [ "{{string}}" ],
         "mlMemberAbilities": {
            "customMLMemberAbilities": [ "{{string}}" ]
         },
         "paymentConfiguration": {
            "jobCompute": {
               "isResponsible": {{boolean}}
            },
            "machineLearning": {
               "modelInference": {
                  "isResponsible": {{boolean}}
               },
               "modelTraining": {
                  "isResponsible": {{boolean}}
               },
               "syntheticDataGeneration": {
                  "isResponsible": {{boolean}}
               }
            },
            "queryCompute": {
               "isResponsible": {{boolean}}
            }
         }
      }
   ],
   "name": "{{string}}",
   "queryLogStatus": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateCollaboration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCollaboration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowedResultRegions](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-allowedResultRegions"></a>
The AWS Regions where collaboration query results can be stored. When specified, results can only be written to these Regions. This parameter enables you to meet your compliance and data governance requirements, and implement regional data governance policies.
Type: Array of strings
Valid Values: `us-west-1 | us-west-2 | us-east-1 | us-east-2 | af-south-1 | ap-east-1 | ap-east-2 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-3 | ap-southeast-5 | ap-southeast-4 | ap-southeast-7 | ap-south-1 | ap-northeast-3 | ap-northeast-1 | ap-northeast-2 | ca-central-1 | ca-west-1 | eu-south-1 | eu-west-3 | eu-south-2 | eu-central-2 | eu-central-1 | eu-north-1 | eu-west-1 | eu-west-2 | me-south-1 | me-central-1 | il-central-1 | sa-east-1 | mx-central-1`
Required: No

 ** [analyticsEngine](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-analyticsEngine"></a>
 The analytics engine.
After July 16, 2025, the `CLEAN_ROOMS_SQL` parameter will no longer be available.
Type: String
Valid Values: `SPARK | CLEAN_ROOMS_SQL`
Required: No

 ** [autoApprovedChangeRequestTypes](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-autoApprovedChangeRequestTypes"></a>
The types of change requests that are automatically approved for this collaboration.
Type: Array of strings
Valid Values: `ADD_MEMBER | GRANT_RECEIVE_RESULTS_ABILITY | REVOKE_RECEIVE_RESULTS_ABILITY | GRANT_EXPORT_QUERY_ANALYSIS_LOG_ABILITY | REVOKE_EXPORT_QUERY_ANALYSIS_LOG_ABILITY`
Required: No

 ** [creatorDisplayName](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-creatorDisplayName"></a>
The display name of the collaboration creator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [creatorMemberAbilities](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-creatorMemberAbilities"></a>
The abilities granted to the collaboration creator.
Type: Array of strings
Valid Values: `CAN_QUERY | CAN_RECEIVE_RESULTS | CAN_RUN_JOB | CAN_EXPORT_QUERY_ANALYSIS_LOG`
Required: Yes

 ** [creatorMLMemberAbilities](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-creatorMLMemberAbilities"></a>
The ML abilities granted to the collaboration creator.
Type: [MLMemberAbilities](API_MLMemberAbilities.md) object
Required: No

 ** [creatorPaymentConfiguration](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-creatorPaymentConfiguration"></a>
The collaboration creator's payment responsibilities set by the collaboration creator.
If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer.
Type: [PaymentConfiguration](API_PaymentConfiguration.md) object
Required: No

 ** [dataEncryptionMetadata](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-dataEncryptionMetadata"></a>
The settings for client-side encryption with Cryptographic Computing for Clean Rooms.
Type: [DataEncryptionMetadata](API_DataEncryptionMetadata.md) object
Required: No

 ** [description](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-description"></a>
A description of the collaboration provided by the collaboration owner.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(?!\s+$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [isMetricsEnabled](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-isMetricsEnabled"></a>
An indicator as to whether metrics have been enabled or disabled for the collaboration.
When `true`, collaboration members can opt in to Amazon CloudWatch metrics for their membership queries. The default value is `false`.
Type: Boolean
Required: No

 ** [jobLogStatus](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-jobLogStatus"></a>
Specifies whether job logs are enabled for this collaboration.
When `ENABLED`, AWS Clean Rooms logs details about jobs run within this collaboration; those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [members](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-members"></a>
A list of initial members, not including the creator. This list is immutable.
Type: Array of [MemberSpecification](API_MemberSpecification.md) objects
Array Members: Minimum number of 0 items.
Required: Yes

 ** [name](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-name"></a>
The display name for a collaboration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [queryLogStatus](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-queryLogStatus"></a>
An indicator as to whether query logging has been enabled or disabled for the collaboration.
When `ENABLED`, AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** [tags](#API_CreateCollaboration_RequestSyntax) **   <a name="API-CreateCollaboration-request-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateCollaboration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collaboration": {
      "allowedResultRegions": [ "string" ],
      "analyticsEngine": "string",
      "arn": "string",
      "autoApprovedChangeTypes": [ "string" ],
      "createTime": number,
      "creatorAccountId": "string",
      "creatorDisplayName": "string",
      "dataEncryptionMetadata": {
         "allowCleartext": boolean,
         "allowDuplicates": boolean,
         "allowJoinsOnColumnsWithDifferentNames": boolean,
         "preserveNulls": boolean
      },
      "description": "string",
      "id": "string",
      "isMetricsEnabled": boolean,
      "jobLogStatus": "string",
      "membershipArn": "string",
      "membershipId": "string",
      "memberStatus": "string",
      "name": "string",
      "queryLogStatus": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_CreateCollaboration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaboration](#API_CreateCollaboration_ResponseSyntax) **   <a name="API-CreateCollaboration-response-collaboration"></a>
The collaboration.
Type: [Collaboration](API_Collaboration.md) object

## Errors
<a name="API_CreateCollaboration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Request denied because service quota has been exceeded.
 ** quotaName **
The name of the quota.
 ** quotaValue **
The value of the quota.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateCollaboration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/CreateCollaboration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/CreateCollaboration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CreateCollaboration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/CreateCollaboration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CreateCollaboration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/CreateCollaboration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/CreateCollaboration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/CreateCollaboration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/CreateCollaboration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CreateCollaboration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
