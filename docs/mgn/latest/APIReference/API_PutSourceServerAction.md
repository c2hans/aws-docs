---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_PutSourceServerAction.html
---

# PutSourceServerAction
<a name="API_PutSourceServerAction"></a>

Put source server post migration custom action.

## Request Syntax
<a name="API_PutSourceServerAction_RequestSyntax"></a>

```
POST /PutSourceServerAction HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "actionID": "{{string}}",
   "actionName": "{{string}}",
   "active": {{boolean}},
   "category": "{{string}}",
   "description": "{{string}}",
   "documentIdentifier": "{{string}}",
   "documentVersion": "{{string}}",
   "externalParameters": {
      "{{string}}" : { ... }
   },
   "mustSucceedForCutover": {{boolean}},
   "order": {{number}},
   "parameters": {
      "{{string}}" : [
         {
            "parameterName": "{{string}}",
            "parameterType": "{{string}}"
         }
      ]
   },
   "sourceServerID": "{{string}}",
   "timeoutSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_PutSourceServerAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutSourceServerAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-accountID"></a>
Source server post migration custom account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [actionID](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-actionID"></a>
Source server post migration custom action ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[0-9a-zA-Z]`
Required: Yes

 ** [actionName](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-actionName"></a>
Source server post migration custom action name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`
Required: Yes

 ** [active](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-active"></a>
Source server post migration custom action active status.
Type: Boolean
Required: No

 ** [category](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-category"></a>
Source server post migration custom action category.
Type: String
Valid Values: `DISASTER_RECOVERY | OPERATING_SYSTEM | LICENSE_AND_SUBSCRIPTION | VALIDATION | OBSERVABILITY | REFACTORING | SECURITY | NETWORKING | CONFIGURATION | BACKUP | OTHER`
Required: No

 ** [description](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-description"></a>
Source server post migration custom action description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[0-9a-zA-Z ():/.,'-_#*; ]*`
Required: No

 ** [documentIdentifier](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-documentIdentifier"></a>
Source server post migration custom action document identifier.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [documentVersion](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-documentVersion"></a>
Source server post migration custom action document version.
Type: String
Pattern: `(\$DEFAULT|\$LATEST|[0-9]+)`
Required: No

 ** [externalParameters](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-externalParameters"></a>
Source server post migration custom action external parameters.
Type: String to [SsmExternalParameter](API_SsmExternalParameter.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Required: No

 ** [mustSucceedForCutover](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-mustSucceedForCutover"></a>
Source server post migration custom action must succeed for cutover.
Type: Boolean
Required: No

 ** [order](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-order"></a>
Source server post migration custom action order.
Type: Integer
Valid Range: Minimum value of 1001. Maximum value of 10000.
Required: Yes

 ** [parameters](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-parameters"></a>
Source server post migration custom action parameters.
Type: String to array of [SsmParameterStoreParameter](API_SsmParameterStoreParameter.md) objects map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [sourceServerID](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-sourceServerID"></a>
Source server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

 ** [timeoutSeconds](#API_PutSourceServerAction_RequestSyntax) **   <a name="mgn-PutSourceServerAction-request-timeoutSeconds"></a>
Source server post migration custom action timeout in seconds.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## Response Syntax
<a name="API_PutSourceServerAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionID": "string",
   "actionName": "string",
   "active": boolean,
   "category": "string",
   "description": "string",
   "documentIdentifier": "string",
   "documentVersion": "string",
   "externalParameters": {
      "string" : { ... }
   },
   "mustSucceedForCutover": boolean,
   "order": number,
   "parameters": {
      "string" : [
         {
            "parameterName": "string",
            "parameterType": "string"
         }
      ]
   },
   "timeoutSeconds": number
}
```

## Response Elements
<a name="API_PutSourceServerAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionID](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-actionID"></a>
Source server post migration custom action ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[0-9a-zA-Z]`

 ** [actionName](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-actionName"></a>
Source server post migration custom action name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`

 ** [active](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-active"></a>
Source server post migration custom action active status.
Type: Boolean

 ** [category](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-category"></a>
Source server post migration custom action category.
Type: String
Valid Values: `DISASTER_RECOVERY | OPERATING_SYSTEM | LICENSE_AND_SUBSCRIPTION | VALIDATION | OBSERVABILITY | REFACTORING | SECURITY | NETWORKING | CONFIGURATION | BACKUP | OTHER`

 ** [description](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-description"></a>
Source server post migration custom action description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[0-9a-zA-Z ():/.,'-_#*; ]*`

 ** [documentIdentifier](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-documentIdentifier"></a>
Source server post migration custom action document identifier.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [documentVersion](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-documentVersion"></a>
Source server post migration custom action document version.
Type: String
Pattern: `(\$DEFAULT|\$LATEST|[0-9]+)`

 ** [externalParameters](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-externalParameters"></a>
Source server post migration custom action external parameters.
Type: String to [SsmExternalParameter](API_SsmExternalParameter.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`

 ** [mustSucceedForCutover](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-mustSucceedForCutover"></a>
Source server post migration custom action must succeed for cutover.
Type: Boolean

 ** [order](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-order"></a>
Source server post migration custom action order.
Type: Integer
Valid Range: Minimum value of 1001. Maximum value of 10000.

 ** [parameters](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-parameters"></a>
Source server post migration custom action parameters.
Type: String to array of [SsmParameterStoreParameter](API_SsmParameterStoreParameter.md) objects map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [timeoutSeconds](#API_PutSourceServerAction_ResponseSyntax) **   <a name="mgn-PutSourceServerAction-response-timeoutSeconds"></a>
Source server post migration custom action timeout in seconds.
Type: Integer
Valid Range: Minimum value of 1.

## Errors
<a name="API_PutSourceServerAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** errors **
Conflict Exception specific errors.
 ** resourceId **
A conflict occurred when prompting for the Resource ID.
 ** resourceType **
A conflict occurred when prompting for resource type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_PutSourceServerAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/PutSourceServerAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/PutSourceServerAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/PutSourceServerAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/PutSourceServerAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/PutSourceServerAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/PutSourceServerAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/PutSourceServerAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/PutSourceServerAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/PutSourceServerAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/PutSourceServerAction)
