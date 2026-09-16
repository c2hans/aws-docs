---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_SendProjectSessionAction.html
---

# SendProjectSessionAction
<a name="API_SendProjectSessionAction"></a>

Performs a recipe step within an interactive DataBrew session that's currently open.

## Request Syntax
<a name="API_SendProjectSessionAction_RequestSyntax"></a>

```
PUT /projects/{{name}}/sendProjectSessionAction HTTP/1.1
Content-type: application/json

{
   "ClientSessionId": "{{string}}",
   "Preview": {{boolean}},
   "RecipeStep": {
      "Action": {
         "Operation": "{{string}}",
         "Parameters": {
            "{{string}}" : "{{string}}"
         }
      },
      "ConditionExpressions": [
         {
            "Condition": "{{string}}",
            "TargetColumn": "{{string}}",
            "Value": "{{string}}"
         }
      ]
   },
   "StepIndex": {{number}},
   "ViewFrame": {
      "Analytics": "{{string}}",
      "ColumnRange": {{number}},
      "HiddenColumns": [ "{{string}}" ],
      "RowRange": {{number}},
      "StartColumnIndex": {{number}},
      "StartRowIndex": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_SendProjectSessionAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_SendProjectSessionAction_RequestSyntax) **   <a name="databrew-SendProjectSessionAction-request-uri-Name"></a>
The name of the project to apply the action to.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_SendProjectSessionAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientSessionId](#API_SendProjectSessionAction_RequestSyntax) **   <a name="databrew-SendProjectSessionAction-request-ClientSessionId"></a>
A unique identifier for an interactive session that's currently open and ready for work. The action will be performed on this session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-]*$`
Required: No

 ** [Preview](#API_SendProjectSessionAction_RequestSyntax) **   <a name="databrew-SendProjectSessionAction-request-Preview"></a>
If true, the result of the recipe step will be returned, but not applied.
Type: Boolean
Required: No

 ** [RecipeStep](#API_SendProjectSessionAction_RequestSyntax) **   <a name="databrew-SendProjectSessionAction-request-RecipeStep"></a>
Represents a single step from a DataBrew recipe to be performed.
Type: [RecipeStep](API_RecipeStep.md) object
Required: No

 ** [StepIndex](#API_SendProjectSessionAction_RequestSyntax) **   <a name="databrew-SendProjectSessionAction-request-StepIndex"></a>
The index from which to preview a step. This index is used to preview the result of steps that have already been applied, so that the resulting view frame is from earlier in the view frame stack.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [ViewFrame](#API_SendProjectSessionAction_RequestSyntax) **   <a name="databrew-SendProjectSessionAction-request-ViewFrame"></a>
Represents the data being transformed during an action.
Type: [ViewFrame](API_ViewFrame.md) object
Required: No

## Response Syntax
<a name="API_SendProjectSessionAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ActionId": number,
   "Name": "string",
   "Result": "string"
}
```

## Response Elements
<a name="API_SendProjectSessionAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_SendProjectSessionAction_ResponseSyntax) **   <a name="databrew-SendProjectSessionAction-response-Name"></a>
The name of the project that was affected by the action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [ActionId](#API_SendProjectSessionAction_ResponseSyntax) **   <a name="databrew-SendProjectSessionAction-response-ActionId"></a>
A unique identifier for the action that was performed.
Type: Integer

 ** [Result](#API_SendProjectSessionAction_ResponseSyntax) **   <a name="databrew-SendProjectSessionAction-response-Result"></a>
A message indicating the result of performing the action.
Type: String

## Errors
<a name="API_SendProjectSessionAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_SendProjectSessionAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/SendProjectSessionAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/SendProjectSessionAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/SendProjectSessionAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/SendProjectSessionAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/SendProjectSessionAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/SendProjectSessionAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/SendProjectSessionAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/SendProjectSessionAction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/SendProjectSessionAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/SendProjectSessionAction)
