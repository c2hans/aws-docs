---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateMembership.html
---

# UpdateMembership
<a name="API_UpdateMembership"></a>

Updates a membership.

## Request Syntax
<a name="API_UpdateMembership_RequestSyntax"></a>

```
PATCH /memberships/{{membershipIdentifier}} HTTP/1.1
Content-type: application/json

{
   "defaultJobResultConfiguration": {
      "outputConfiguration": { ... },
      "roleArn": "{{string}}"
   },
   "defaultResultConfiguration": {
      "outputConfiguration": { ... },
      "roleArn": "{{string}}"
   },
   "jobLogStatus": "{{string}}",
   "membershipPaymentConfiguration": {
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
   "queryLogStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_UpdateMembership_RequestSyntax) **   <a name="API-UpdateMembership-request-uri-membershipIdentifier"></a>
The unique identifier of the membership.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateMembership_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [defaultJobResultConfiguration](#API_UpdateMembership_RequestSyntax) **   <a name="API-UpdateMembership-request-defaultJobResultConfiguration"></a>
 The default job result configuration.
Type: [MembershipProtectedJobResultConfiguration](API_MembershipProtectedJobResultConfiguration.md) object
Required: No

 ** [defaultResultConfiguration](#API_UpdateMembership_RequestSyntax) **   <a name="API-UpdateMembership-request-defaultResultConfiguration"></a>
The default protected query result configuration as specified by the member who can receive results.
Type: [MembershipProtectedQueryResultConfiguration](API_MembershipProtectedQueryResultConfiguration.md) object
Required: No

 ** [jobLogStatus](#API_UpdateMembership_RequestSyntax) **   <a name="API-UpdateMembership-request-jobLogStatus"></a>
An indicator as to whether job logging has been enabled or disabled for the collaboration.
When `ENABLED`, AWS Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [membershipPaymentConfiguration](#API_UpdateMembership_RequestSyntax) **   <a name="API-UpdateMembership-request-membershipPaymentConfiguration"></a>
The payment configuration to update for the membership.
Type: [UpdateMembershipPaymentConfiguration](API_UpdateMembershipPaymentConfiguration.md) object
Required: No

 ** [queryLogStatus](#API_UpdateMembership_RequestSyntax) **   <a name="API-UpdateMembership-request-queryLogStatus"></a>
An indicator as to whether query logging has been enabled or disabled for the membership.
When `ENABLED`, AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_UpdateMembership_ResponseSyntax"></a>

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
<a name="API_UpdateMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [membership](#API_UpdateMembership_ResponseSyntax) **   <a name="API-UpdateMembership-response-membership"></a>
The membership object.
Type: [Membership](API_Membership.md) object

## Errors
<a name="API_UpdateMembership_Errors"></a>

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
<a name="API_UpdateMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/UpdateMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/UpdateMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/UpdateMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/UpdateMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/UpdateMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/UpdateMembership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/UpdateMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateMembership)
