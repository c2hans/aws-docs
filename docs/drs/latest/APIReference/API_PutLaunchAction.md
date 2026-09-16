---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_PutLaunchAction.html
---

# PutLaunchAction
<a name="API_PutLaunchAction"></a>

Puts a resource launch action.

## Request Syntax
<a name="API_PutLaunchAction_RequestSyntax"></a>

```
POST /PutLaunchAction HTTP/1.1
Content-type: application/json

{
   "actionCode": "{{string}}",
   "actionId": "{{string}}",
   "actionVersion": "{{string}}",
   "active": {{boolean}},
   "category": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "optional": {{boolean}},
   "order": {{number}},
   "parameters": {
      "{{string}}" : {
         "type": "{{string}}",
         "value": "{{string}}"
      }
   },
   "resourceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutLaunchAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutLaunchAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionCode](#API_PutLaunchAction_RequestSyntax) **   <a name="drs-PutLaunchAction-request-actionCode"></a>
Launch action code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `([A-Za-z0-9-/:])+`
Required: Yes

 ** [actionId](#API_PutLaunchAction_RequestSyntax) **   <a name="drs-PutLaunchAction-request-actionId"></a>
Launch action Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [actionVersion](#API_PutLaunchAction_RequestSyntax) **   <a name="drs-PutLaunchAction-request-actionVersion"></a>
Launch action version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `(\$DEFAULT|\$LATEST|[0-9]+)`
Required: Yes

 ** [active](#API_PutLaunchAction_RequestSyntax) **   <a name="drs-PutLaunchAction-request-active"></a>
Whether the launch action is active.
Type: Boolean
Required: Yes

 ** [category](#API_PutLaunchAction_RequestSyntax) **   <a name="drs-PutLaunchAction-request-category"></a>
Launch action category.
Type: String
Valid Values: `MONITORING | VALIDATION | CONFIGURATION | SECURITY | OTHER`
Required: Yes

 ** [description](#API_PutLaunchAction_RequestSyntax) **   <a name="drs-PutLaunchAction-request-description"></a>
Launch action description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[0-9a-zA-Z ():/.,'-_#*; ]*`
Required: Yes

 ** [name](#API_PutLaunchAction_RequestSyntax) **   <a name="drs-PutLaunchAction-request-name"></a>
Launch action name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][A-Za-z0-9 /_-]*`
Required: Yes

 ** [optional](#API_PutLaunchAction_RequestSyntax) **   <a name="drs-PutLaunchAction-request-optional"></a>
Whether the launch will not be marked as failed if this action fails.
Type: Boolean
Required: Yes

 ** [order](#API_PutLaunchAction_RequestSyntax) **   <a name="drs-PutLaunchAction-request-order"></a>
Launch action order.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10000.
Required: Yes

 ** [parameters](#API_PutLaunchAction_RequestSyntax) **   <a name="drs-PutLaunchAction-request-parameters"></a>
Launch action parameters.
Type: String to [LaunchActionParameter](API_LaunchActionParameter.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Required: No

 ** [resourceId](#API_PutLaunchAction_RequestSyntax) **   <a name="drs-PutLaunchAction-request-resourceId"></a>
Launch configuration template Id or Source Server Id
Type: String
Pattern: `(s-[0-9a-zA-Z]{17}$|lct-[0-9a-zA-Z]{17})`
Required: Yes

## Response Syntax
<a name="API_PutLaunchAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionCode": "string",
   "actionId": "string",
   "actionVersion": "string",
   "active": boolean,
   "category": "string",
   "description": "string",
   "name": "string",
   "optional": boolean,
   "order": number,
   "parameters": {
      "string" : {
         "type": "string",
         "value": "string"
      }
   },
   "resourceId": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_PutLaunchAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionCode](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-actionCode"></a>
Launch action code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `([A-Za-z0-9-/:])+`

 ** [actionId](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-actionId"></a>
Launch action Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [actionVersion](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-actionVersion"></a>
Launch action version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `(\$DEFAULT|\$LATEST|[0-9]+)`

 ** [active](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-active"></a>
Whether the launch action is active.
Type: Boolean

 ** [category](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-category"></a>
Launch action category.
Type: String
Valid Values: `MONITORING | VALIDATION | CONFIGURATION | SECURITY | OTHER`

 ** [description](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-description"></a>
Launch action description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[0-9a-zA-Z ():/.,'-_#*; ]*`

 ** [name](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-name"></a>
Launch action name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][A-Za-z0-9 /_-]*`

 ** [optional](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-optional"></a>
Whether the launch will not be marked as failed if this action fails.
Type: Boolean

 ** [order](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-order"></a>
Launch action order.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10000.

 ** [parameters](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-parameters"></a>
Launch action parameters.
Type: String to [LaunchActionParameter](API_LaunchActionParameter.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`

 ** [resourceId](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-resourceId"></a>
Launch configuration template Id or Source Server Id
Type: String
Pattern: `(s-[0-9a-zA-Z]{17}$|lct-[0-9a-zA-Z]{17})`

 ** [type](#API_PutLaunchAction_ResponseSyntax) **   <a name="drs-PutLaunchAction-response-type"></a>
Launch action type.
Type: String
Valid Values: `SSM_AUTOMATION | SSM_COMMAND`

## Errors
<a name="API_PutLaunchAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

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
<a name="API_PutLaunchAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/PutLaunchAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/PutLaunchAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/PutLaunchAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/PutLaunchAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/PutLaunchAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/PutLaunchAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/PutLaunchAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/PutLaunchAction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/PutLaunchAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/PutLaunchAction)
