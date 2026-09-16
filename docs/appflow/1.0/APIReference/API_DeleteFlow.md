---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DeleteFlow.html
---

# DeleteFlow
<a name="API_DeleteFlow"></a>

 Enables your application to delete an existing flow. Before deleting the flow, Amazon AppFlow validates the request by checking the flow configuration and status. You can delete flows one at a time.

## Request Syntax
<a name="API_DeleteFlow_RequestSyntax"></a>

```
POST /delete-flow HTTP/1.1
Content-type: application/json

{
   "flowName": "{{string}}",
   "forceDelete": {{boolean}}
}
```

## URI Request Parameters
<a name="API_DeleteFlow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [flowName](#API_DeleteFlow_RequestSyntax) **   <a name="appflow-DeleteFlow-request-flowName"></a>
 The specified name of the flow. Spaces are not allowed. Use underscores (\_) or hyphens (-) only.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: Yes

 ** [forceDelete](#API_DeleteFlow_RequestSyntax) **   <a name="appflow-DeleteFlow-request-forceDelete"></a>
 Indicates whether Amazon AppFlow should delete the flow, even if it is currently in use.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DeleteFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
 There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again.
HTTP Status Code: 409

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request (such as the source or destination connector profile) is not found.
HTTP Status Code: 404

## Examples
<a name="API_DeleteFlow_Examples"></a>

### An active scheduled flow with forceDelete false
<a name="API_DeleteFlow_Example_1"></a>

This example shows an active scheduled flow with `forceDelete` false. The result is that a conflict exception is thrown.

#### Sample Request
<a name="API_DeleteFlow_Example_1_Request"></a>

```
{
  "flowName": "flowName_value"
}
```

#### Sample Response
<a name="API_DeleteFlow_Example_1_Response"></a>

```
{
  "message": "Conflict executing request: Flow is in active state, please set forceDelete to true or deactivate the flow: flowName_value"
}
```

### An active scheduled flow with forceDelete true
<a name="API_DeleteFlow_Example_2"></a>

This example shows an active scheduled flow with `forceDelete` true. The result is that the flow is deleted successfully.

#### Sample Request
<a name="API_DeleteFlow_Example_2_Request"></a>

```
{
  "flowName": "flowName_value",
  "forceDelete": true
}
```

#### Sample Response
<a name="API_DeleteFlow_Example_2_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/DeleteFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/DeleteFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/DeleteFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/DeleteFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/DeleteFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/DeleteFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/DeleteFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/DeleteFlow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/DeleteFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/DeleteFlow)
