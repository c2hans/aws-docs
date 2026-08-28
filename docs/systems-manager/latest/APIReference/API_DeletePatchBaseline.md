---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeletePatchBaseline.html
---

# DeletePatchBaseline
<a name="API_DeletePatchBaseline"></a>

Deletes a patch baseline.

## Request Syntax
<a name="API_DeletePatchBaseline_RequestSyntax"></a>

```
{
   "BaselineId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePatchBaseline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BaselineId](#API_DeletePatchBaseline_RequestSyntax) **   <a name="systemsmanager-DeletePatchBaseline-request-BaselineId"></a>
The ID of the patch baseline to delete.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`
Required: Yes

## Response Syntax
<a name="API_DeletePatchBaseline_ResponseSyntax"></a>

```
{
   "BaselineId": "string"
}
```

## Response Elements
<a name="API_DeletePatchBaseline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BaselineId](#API_DeletePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-DeletePatchBaseline-response-BaselineId"></a>
The ID of the deleted patch baseline.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`

## Errors
<a name="API_DeletePatchBaseline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceInUseException **
Error returned if an attempt is made to delete a patch baseline that is registered for a patch group.
HTTP Status Code: 400

## Examples
<a name="API_DeletePatchBaseline_Examples"></a>

### Example
<a name="API_DeletePatchBaseline_Example_1"></a>

This example illustrates one usage of DeletePatchBaseline.

#### Sample Request
<a name="API_DeletePatchBaseline_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 38
X-Amz-Target: AmazonSSM.DeletePatchBaseline
X-Amz-Date: 20240309T062407Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240309/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "BaselineId": "pb-0c10e65780EXAMPLE"
}
```

#### Sample Response
<a name="API_DeletePatchBaseline_Example_1_Response"></a>

```
{
    "BaselineId": "pb-0c10e65780EXAMPLE"
}
```

## See Also
<a name="API_DeletePatchBaseline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeletePatchBaseline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeletePatchBaseline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeletePatchBaseline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeletePatchBaseline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeletePatchBaseline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeletePatchBaseline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeletePatchBaseline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeletePatchBaseline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeletePatchBaseline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeletePatchBaseline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
