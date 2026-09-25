---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateRecoveryPlan.html
---

# CreateRecoveryPlan
<a name="API_CreateRecoveryPlan"></a>

Creates a Recovery Plan to orchestrate multi-server disaster recovery.

## Request Syntax
<a name="API_CreateRecoveryPlan_RequestSyntax"></a>

```
POST /CreateRecoveryPlan HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRecoveryPlan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRecoveryPlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateRecoveryPlan_RequestSyntax) **   <a name="drs-CreateRecoveryPlan-request-clientToken"></a>
A unique string provided to ensure request idempotency.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [description](#API_CreateRecoveryPlan_RequestSyntax) **   <a name="drs-CreateRecoveryPlan-request-description"></a>
The description of the Recovery Plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [name](#API_CreateRecoveryPlan_RequestSyntax) **   <a name="drs-CreateRecoveryPlan-request-name"></a>
The name of the Recovery Plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _-]*`
Required: Yes

 ** [tags](#API_CreateRecoveryPlan_RequestSyntax) **   <a name="drs-CreateRecoveryPlan-request-tags"></a>
The tags to apply to the Recovery Plan.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateRecoveryPlan_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "recoveryPlan": {
      "createdAt": "string",
      "description": "string",
      "name": "string",
      "recoveryPlanArn": "string",
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_CreateRecoveryPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [recoveryPlan](#API_CreateRecoveryPlan_ResponseSyntax) **   <a name="drs-CreateRecoveryPlan-response-recoveryPlan"></a>
The created Recovery Plan.
Type: [RecoveryPlan](API_RecoveryPlan.md) object

## Errors
<a name="API_CreateRecoveryPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request could not be completed because its exceeded the service quota.
 ** quotaCode **
Quota code.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
 ** serviceCode **
Service code.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_CreateRecoveryPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/CreateRecoveryPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/CreateRecoveryPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/CreateRecoveryPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/CreateRecoveryPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/CreateRecoveryPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/CreateRecoveryPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/CreateRecoveryPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/CreateRecoveryPlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/CreateRecoveryPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/CreateRecoveryPlan)
