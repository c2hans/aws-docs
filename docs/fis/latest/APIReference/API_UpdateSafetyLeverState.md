---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateSafetyLeverState.html
---

# UpdateSafetyLeverState
<a name="API_UpdateSafetyLeverState"></a>

 Updates the specified safety lever state.

## Request Syntax
<a name="API_UpdateSafetyLeverState_RequestSyntax"></a>

```
PATCH /safetyLevers/{{id}}/state HTTP/1.1
Content-type: application/json

{
   "state": {
      "reason": "{{string}}",
      "status": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateSafetyLeverState_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateSafetyLeverState_RequestSyntax) **   <a name="fis-UpdateSafetyLeverState-request-uri-id"></a>
 The ID of the safety lever.
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: Yes

## Request Body
<a name="API_UpdateSafetyLeverState_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [state](#API_UpdateSafetyLeverState_RequestSyntax) **   <a name="fis-UpdateSafetyLeverState-request-state"></a>
 The state of the safety lever.
Type: [UpdateSafetyLeverStateInput](API_UpdateSafetyLeverStateInput.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateSafetyLeverState_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "safetyLever": {
      "arn": "string",
      "id": "string",
      "state": {
         "reason": "string",
         "status": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateSafetyLeverState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [safetyLever](#API_UpdateSafetyLeverState_ResponseSyntax) **   <a name="fis-UpdateSafetyLeverState-response-safetyLever"></a>
 Information about the safety lever.
Type: [SafetyLever](API_SafetyLever.md) object

## Errors
<a name="API_UpdateSafetyLeverState_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be processed because of a conflict.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ValidationException **
The specified input is not valid, or fails to satisfy the constraints for the request.
HTTP Status Code: 400

## Examples
<a name="API_UpdateSafetyLeverState_Examples"></a>

### Example
<a name="API_UpdateSafetyLeverState_Example_1"></a>

This example illustrates one usage of UpdateSafetyLeverState.

```
{
    "id": "default",
    "state": {
        "status": "engaged",
        "reason": "Blocked days"
    }
}
```

## See Also
<a name="API_UpdateSafetyLeverState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fis-2020-12-01/UpdateSafetyLeverState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fis-2020-12-01/UpdateSafetyLeverState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/UpdateSafetyLeverState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fis-2020-12-01/UpdateSafetyLeverState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/UpdateSafetyLeverState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fis-2020-12-01/UpdateSafetyLeverState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fis-2020-12-01/UpdateSafetyLeverState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fis-2020-12-01/UpdateSafetyLeverState)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fis-2020-12-01/UpdateSafetyLeverState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/UpdateSafetyLeverState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
