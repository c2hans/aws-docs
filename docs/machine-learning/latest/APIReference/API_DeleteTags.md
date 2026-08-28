---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteTags.html
---

# DeleteTags
<a name="API_DeleteTags"></a>

Deletes the specified tags associated with an ML object. After this operation is complete, you can't recover deleted tags.

If you specify a tag that doesn't exist, Amazon ML ignores it.

## Request Syntax
<a name="API_DeleteTags_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DeleteTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceId](#API_DeleteTags_RequestSyntax) **   <a name="amazonml-DeleteTags-request-ResourceId"></a>
The ID of the tagged ML object. For example, `exampleModelId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [ResourceType](#API_DeleteTags_RequestSyntax) **   <a name="amazonml-DeleteTags-request-ResourceType"></a>
The type of the tagged ML object.
Type: String
Valid Values: `BatchPrediction | DataSource | Evaluation | MLModel`
Required: Yes

 ** [TagKeys](#API_DeleteTags_RequestSyntax) **   <a name="amazonml-DeleteTags-request-TagKeys"></a>
One or more tags to delete.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Response Syntax
<a name="API_DeleteTags_ResponseSyntax"></a>

```
{
   "ResourceId": "string",
   "ResourceType": "string"
}
```

## Response Elements
<a name="API_DeleteTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceId](#API_DeleteTags_ResponseSyntax) **   <a name="amazonml-DeleteTags-response-ResourceId"></a>
The ID of the ML object from which tags were deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [ResourceType](#API_DeleteTags_ResponseSyntax) **   <a name="amazonml-DeleteTags-response-ResourceType"></a>
The type of the ML object from which tags were deleted.
Type: String
Valid Values: `BatchPrediction | DataSource | Evaluation | MLModel`

## Errors
<a name="API_DeleteTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An error on the server occurred when trying to process a request.
HTTP Status Code: 500

 ** InvalidInputException **
An error on the client occurred. Typically, the cause is an invalid input value.
HTTP Status Code: 400

 ** InvalidTagException **
A submitted tag is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A specified resource cannot be located.
HTTP Status Code: 400

## Examples
<a name="API_DeleteTags_Examples"></a>

### The following are an example request and response for the DeleteTags operation.
<a name="API_DeleteTags_Example_1"></a>

This example illustrates one usage of DeleteTags.

#### Sample Request
<a name="API_DeleteTags_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.DeleteTags
{
  "ResourceId": "exampleModelId",
  "ResourceType": "MLModel",
  "Tags": [
      "exampleKey"
  ]
}
```

#### Sample Response
<a name="API_DeleteTags_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "ResourceId": "exampleModelId",
  "ResourceType": "MLModel"
}
```

## See Also
<a name="API_DeleteTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/DeleteTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/DeleteTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/DeleteTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/DeleteTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/DeleteTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/DeleteTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/DeleteTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/DeleteTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/DeleteTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/DeleteTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
