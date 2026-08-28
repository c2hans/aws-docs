---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_CreatePipeline.html
---

# CreatePipeline
<a name="API_CreatePipeline"></a>

Creates a new, empty pipeline. Use [PutPipelineDefinition](API_PutPipelineDefinition.md) to populate the pipeline.

## Request Syntax
<a name="API_CreatePipeline_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "uniqueId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePipeline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreatePipeline_RequestSyntax) **   <a name="DP-CreatePipeline-request-description"></a>
The description for the pipeline.
Type: String
Required: No

 ** [name](#API_CreatePipeline_RequestSyntax) **   <a name="DP-CreatePipeline-request-name"></a>
The name for the pipeline. You can use the same name for multiple pipelines associated with your AWS account, because AWS Data Pipeline assigns each pipeline a unique pipeline identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [tags](#API_CreatePipeline_RequestSyntax) **   <a name="DP-CreatePipeline-request-tags"></a>
A list of tags to associate with the pipeline at creation. Tags let you control access to pipelines. For more information, see [Controlling User Access to Pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html) in the *AWS Data Pipeline Developer Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [uniqueId](#API_CreatePipeline_RequestSyntax) **   <a name="DP-CreatePipeline-request-uniqueId"></a>
A unique identifier. This identifier is not the same as the pipeline identifier assigned by AWS Data Pipeline. You are responsible for defining the format and ensuring the uniqueness of this identifier. You use this parameter to ensure idempotency during repeated calls to `CreatePipeline`. For example, if the first call to `CreatePipeline` does not succeed, you can pass in the same unique identifier and pipeline name combination on a subsequent call to `CreatePipeline`. `CreatePipeline` ensures that if a pipeline already exists with the same name and unique identifier, a new pipeline is not created. Instead, you'll receive the pipeline identifier from the previous attempt. The uniqueness of the name and unique identifier combination is scoped to the AWS account or user credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

## Response Syntax
<a name="API_CreatePipeline_ResponseSyntax"></a>

```
{
   "pipelineId": "string"
}
```

## Response Elements
<a name="API_CreatePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pipelineId](#API_CreatePipeline_ResponseSyntax) **   <a name="DP-CreatePipeline-response-pipelineId"></a>
The ID that AWS Data Pipeline assigns the newly created pipeline. For example, `df-06372391ZG65EXAMPLE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`

## Errors
<a name="API_CreatePipeline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
An internal service error occurred.
 ** message **
Description of the error message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.
 ** message **
Description of the error message.
HTTP Status Code: 400

## Examples
<a name="API_CreatePipeline_Examples"></a>

### Example
<a name="API_CreatePipeline_Example_1"></a>

This example illustrates one usage of CreatePipeline.

#### Sample Request
<a name="API_CreatePipeline_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.CreatePipeline
Content-Length: 91
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"name": "myPipeline",
 "uniqueId": "123456789",
 "description": "This is my first pipeline"}
```

#### Sample Response
<a name="API_CreatePipeline_Example_1_Response"></a>

```

HTTP/1.1 200
x-amzn-RequestId: b16911ce-0774-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 40
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"pipelineId": "df-06372391ZG65EXAMPLE"}
```

## See Also
<a name="API_CreatePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/CreatePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/CreatePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/CreatePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/CreatePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/CreatePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/CreatePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/CreatePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/CreatePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/CreatePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/CreatePipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
