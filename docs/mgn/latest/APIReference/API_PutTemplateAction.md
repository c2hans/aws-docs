---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_PutTemplateAction.html
---

# PutTemplateAction
<a name="API_PutTemplateAction"></a>

Put template post migration custom action.

## Request Syntax
<a name="API_PutTemplateAction_RequestSyntax"></a>

```
POST /PutTemplateAction HTTP/1.1
Content-type: application/json

{
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
   "launchConfigurationTemplateID": "{{string}}",
   "mustSucceedForCutover": {{boolean}},
   "operatingSystem": "{{string}}",
   "order": {{number}},
   "parameters": {
      "{{string}}" : [
         {
            "parameterName": "{{string}}",
            "parameterType": "{{string}}"
         }
      ]
   },
   "timeoutSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_PutTemplateAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutTemplateAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionID](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-actionID"></a>
Template post migration custom action ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[0-9a-zA-Z]`
Required: Yes

 ** [actionName](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-actionName"></a>
Template post migration custom action name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [active](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-active"></a>
Template post migration custom action active status.
Type: Boolean
Required: No

 ** [category](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-category"></a>
Template post migration custom action category.
Type: String
Valid Values: `DISASTER_RECOVERY | OPERATING_SYSTEM | LICENSE_AND_SUBSCRIPTION | VALIDATION | OBSERVABILITY | REFACTORING | SECURITY | NETWORKING | CONFIGURATION | BACKUP | OTHER`
Required: No

 ** [description](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-description"></a>
Template post migration custom action description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[0-9a-zA-Z ():/.,'-_#*; ]*`
Required: No

 ** [documentIdentifier](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-documentIdentifier"></a>
Template post migration custom action document identifier.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [documentVersion](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-documentVersion"></a>
Template post migration custom action document version.
Type: String
Pattern: `(\$DEFAULT|\$LATEST|[0-9]+)`
Required: No

 ** [externalParameters](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-externalParameters"></a>
Template post migration custom action external parameters.
Type: String to [SsmExternalParameter](API_SsmExternalParameter.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Required: No

 ** [launchConfigurationTemplateID](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-launchConfigurationTemplateID"></a>
Launch configuration template ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `lct-[0-9a-zA-Z]{17}`
Required: Yes

 ** [mustSucceedForCutover](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-mustSucceedForCutover"></a>
Template post migration custom action must succeed for cutover.
Type: Boolean
Required: No

 ** [operatingSystem](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-operatingSystem"></a>
Operating system eligible for this template post migration custom action.
Type: String
Pattern: `(linux|windows)`
Required: No

 ** [order](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-order"></a>
Template post migration custom action order.
Type: Integer
Valid Range: Minimum value of 1001. Maximum value of 10000.
Required: Yes

 ** [parameters](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-parameters"></a>
Template post migration custom action parameters.
Type: String to array of [SsmParameterStoreParameter](API_SsmParameterStoreParameter.md) objects map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [timeoutSeconds](#API_PutTemplateAction_RequestSyntax) **   <a name="mgn-PutTemplateAction-request-timeoutSeconds"></a>
Template post migration custom action timeout in seconds.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## Response Syntax
<a name="API_PutTemplateAction_ResponseSyntax"></a>

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
   "operatingSystem": "string",
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
<a name="API_PutTemplateAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionID](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-actionID"></a>
Template post migration custom action ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[0-9a-zA-Z]`

 ** [actionName](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-actionName"></a>
Template post migration custom action name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [active](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-active"></a>
Template post migration custom action active status.
Type: Boolean

 ** [category](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-category"></a>
Template post migration custom action category.
Type: String
Valid Values: `DISASTER_RECOVERY | OPERATING_SYSTEM | LICENSE_AND_SUBSCRIPTION | VALIDATION | OBSERVABILITY | REFACTORING | SECURITY | NETWORKING | CONFIGURATION | BACKUP | OTHER`

 ** [description](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-description"></a>
Template post migration custom action description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[0-9a-zA-Z ():/.,'-_#*; ]*`

 ** [documentIdentifier](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-documentIdentifier"></a>
Template post migration custom action document identifier.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [documentVersion](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-documentVersion"></a>
Template post migration custom action document version.
Type: String
Pattern: `(\$DEFAULT|\$LATEST|[0-9]+)`

 ** [externalParameters](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-externalParameters"></a>
Template post migration custom action external parameters.
Type: String to [SsmExternalParameter](API_SsmExternalParameter.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`

 ** [mustSucceedForCutover](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-mustSucceedForCutover"></a>
Template post migration custom action must succeed for cutover.
Type: Boolean

 ** [operatingSystem](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-operatingSystem"></a>
Operating system eligible for this template post migration custom action.
Type: String
Pattern: `(linux|windows)`

 ** [order](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-order"></a>
Template post migration custom action order.
Type: Integer
Valid Range: Minimum value of 1001. Maximum value of 10000.

 ** [parameters](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-parameters"></a>
Template post migration custom action parameters.
Type: String to array of [SsmParameterStoreParameter](API_SsmParameterStoreParameter.md) objects map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [timeoutSeconds](#API_PutTemplateAction_ResponseSyntax) **   <a name="mgn-PutTemplateAction-response-timeoutSeconds"></a>
Template post migration custom action timeout in seconds.
Type: Integer
Valid Range: Minimum value of 1.

## Errors
<a name="API_PutTemplateAction_Errors"></a>

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
<a name="API_PutTemplateAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/PutTemplateAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/PutTemplateAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/PutTemplateAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/PutTemplateAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/PutTemplateAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/PutTemplateAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/PutTemplateAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/PutTemplateAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/PutTemplateAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/PutTemplateAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
