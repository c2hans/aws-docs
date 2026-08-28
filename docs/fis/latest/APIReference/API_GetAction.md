---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_GetAction.html
---

# GetAction
<a name="API_GetAction"></a>

Gets information about the specified AWS FIS action.

## Request Syntax
<a name="API_GetAction_RequestSyntax"></a>

```
GET /actions/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetAction_RequestSyntax) **   <a name="fis-GetAction-request-uri-id"></a>
The ID of the action.
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: Yes

## Request Body
<a name="API_GetAction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "action": {
      "arn": "string",
      "description": "string",
      "id": "string",
      "parameters": {
         "string" : {
            "description": "string",
            "required": boolean
         }
      },
      "tags": {
         "string" : "string"
      },
      "targets": {
         "string" : {
            "resourceType": "string"
         }
      }
   }
}
```

## Response Elements
<a name="API_GetAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [action](#API_GetAction_ResponseSyntax) **   <a name="fis-GetAction-response-action"></a>
Information about the action.
Type: [Action](API_Action.md) object

## Errors
<a name="API_GetAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ValidationException **
The specified input is not valid, or fails to satisfy the constraints for the request.
HTTP Status Code: 400

## See Also
<a name="API_GetAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fis-2020-12-01/GetAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fis-2020-12-01/GetAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/GetAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fis-2020-12-01/GetAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/GetAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fis-2020-12-01/GetAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fis-2020-12-01/GetAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fis-2020-12-01/GetAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fis-2020-12-01/GetAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/GetAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
