---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateMembership.html
---

# CreateMembership
<a name="API_CreateMembership"></a>

Creates a membership for a specific collaboration identifier and joins the collaboration.

## Request Syntax
<a name="API_CreateMembership_RequestSyntax"></a>

```
POST /memberships HTTP/1.1
Content-type: application/json

{
   "collaborationIdentifier": "{{string}}",
   "defaultJobResultConfiguration": {
      "outputConfiguration": { ... },
      "roleArn": "{{string}}"
   },
   "defaultResultConfiguration": {
      "outputConfiguration": { ... },
      "roleArn": "{{string}}"
   },
   "isMetricsEnabled": {{boolean}},
   "jobLogStatus": "{{string}}",
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
   },
   "queryLogStatus": "{{string}}",
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

 ** [collaborationIdentifier](#API_CreateMembership_RequestSyntax) **   <a name="API-CreateMembership-request-collaborationIdentifier"></a>
The unique ID for the associated collaboration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [defaultJobResultConfiguration](#API_CreateMembership_RequestSyntax) **   <a name="API-CreateMembership-request-defaultJobResultConfiguration"></a>
The default job result configuration that determines how job results are protected and managed within this membership. This configuration applies to all jobs.
Type: [MembershipProtectedJobResultConfiguration](API_MembershipProtectedJobResultConfiguration.md) object
Required: No

 ** [defaultResultConfiguration](#API_CreateMembership_RequestSyntax) **   <a name="API-CreateMembership-request-defaultResultConfiguration"></a>
The default protected query result configuration as specified by the member who can receive results.
Type: [MembershipProtectedQueryResultConfiguration](API_MembershipProtectedQueryResultConfiguration.md) object
Required: No

 ** [isMetricsEnabled](#API_CreateMembership_RequestSyntax) **   <a name="API-CreateMembership-request-isMetricsEnabled"></a>
An indicator as to whether Amazon CloudWatch metrics have been enabled or disabled for the membership.
Amazon CloudWatch metrics are only available when the collaboration has metrics enabled. This option can be set by collaboration members who have the ability to run queries (analysis runners) or by members who are configured as payers.
When `true`, metrics about query execution are collected in Amazon CloudWatch. The default value is `false`.
Type: Boolean
Required: No

 ** [jobLogStatus](#API_CreateMembership_RequestSyntax) **   <a name="API-CreateMembership-request-jobLogStatus"></a>
An indicator as to whether job logging has been enabled or disabled for the collaboration.
When `ENABLED`, AWS Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [paymentConfiguration](#API_CreateMembership_RequestSyntax) **   <a name="API-CreateMembership-request-paymentConfiguration"></a>
The payment responsibilities accepted by the collaboration member.
Not required if the collaboration member has the member ability to run queries.
Required if the collaboration member doesn't have the member ability to run queries but is configured as a payer by the collaboration creator.
Type: [MembershipPaymentConfiguration](API_MembershipPaymentConfiguration.md) object
Required: No

 ** [queryLogStatus](#API_CreateMembership_RequestSyntax) **   <a name="API-CreateMembership-request-queryLogStatus"></a>
An indicator as to whether query logging has been enabled or disabled for the membership.
When `ENABLED`, AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** [tags](#API_CreateMembership_RequestSyntax) **   <a name="API-CreateMembership-request-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateMembership_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "membership": {
      "arn": "string",
      "collaborationArn": "string",
      "collaborationCreatorAccountId": "string",
      "collaborationCreatorDisplayName": "string",
      "collaborationId": "string",
      "collaborationName": "string",
      "createTime": number,
      "defaultJobResultConfiguration": {
         "outputConfiguration": { ... },
         "roleArn": "string"
      },
      "defaultResultConfiguration": {
         "outputConfiguration": { ... },
         "roleArn": "string"
      },
      "id": "string",
      "isMetricsEnabled": boolean,
      "jobLogStatus": "string",
      "memberAbilities": [ "string" ],
      "mlMemberAbilities": {
         "customMLMemberAbilities": [ "string" ]
      },
      "paymentConfiguration": {
         "jobCompute": {
            "isResponsible": boolean
         },
         "machineLearning": {
            "modelInference": {
               "isResponsible": boolean
            },
            "modelTraining": {
               "isResponsible": boolean
            },
            "syntheticDataGeneration": {
               "isResponsible": boolean
            }
         },
         "queryCompute": {
            "isResponsible": boolean
         }
      },
      "queryLogStatus": "string",
      "status": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_CreateMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [membership](#API_CreateMembership_ResponseSyntax) **   <a name="API-CreateMembership-response-membership"></a>
The membership that was created.
Type: [Membership](API_Membership.md) object

## Errors
<a name="API_CreateMembership_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** reason **
A reason code for the exception.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

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
<a name="API_CreateMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/CreateMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/CreateMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CreateMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/CreateMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CreateMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/CreateMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/CreateMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/CreateMembership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/CreateMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CreateMembership)
