---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_AddTags.html
---

# AddTags
<a name="API_AddTags"></a>

Adds one or more tags to an object, up to a limit of 10. Each tag consists of a key and an optional value. If you add a tag using a key that is already associated with the ML object, `AddTags` updates the tag's value.

## Request Syntax
<a name="API_AddTags_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_AddTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceId](#API_AddTags_RequestSyntax) **   <a name="amazonml-AddTags-request-ResourceId"></a>
The ID of the ML object to tag. For example, `exampleModelId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [ResourceType](#API_AddTags_RequestSyntax) **   <a name="amazonml-AddTags-request-ResourceType"></a>
The type of the ML object to tag.
Type: String
Valid Values: `BatchPrediction | DataSource | Evaluation | MLModel`
Required: Yes

 ** [Tags](#API_AddTags_RequestSyntax) **   <a name="amazonml-AddTags-request-Tags"></a>
The key-value pairs to use to create tags. If you specify a key without specifying a value, Amazon ML creates a tag with the specified key and a value of null.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_AddTags_ResponseSyntax"></a>

```
{
   "ResourceId": "string",
   "ResourceType": "string"
}
```

## Response Elements
<a name="API_AddTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceId](#API_AddTags_ResponseSyntax) **   <a name="amazonml-AddTags-response-ResourceId"></a>
The ID of the ML object that was tagged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [ResourceType](#API_AddTags_ResponseSyntax) **   <a name="amazonml-AddTags-response-ResourceType"></a>
The type of the ML object that was tagged.
Type: String
Valid Values: `BatchPrediction | DataSource | Evaluation | MLModel`

## Errors
<a name="API_AddTags_Errors"></a>

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

 ** TagLimitExceededException **
The limit in the number of tags has been exceeded.
HTTP Status Code: 400

## Examples
<a name="API_AddTags_Examples"></a>

### The following is an example of a request and response for the AddTags operation.
<a name="API_AddTags_Example_1"></a>

This example illustrates one usage of AddTags.

#### Sample Request
<a name="API_AddTags_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.AddTags
{
  "ResourceId": "exampleModelId",
  "ResourceType": "MLModel",
  "Tags": {
      "Key":"exampleKey",
      "Value":"exampleKeyValue"
  }
}
```

#### Sample Response
<a name="API_AddTags_Example_1_Response"></a>

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
<a name="API_AddTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/AddTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/AddTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/AddTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/AddTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/AddTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/AddTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/AddTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/AddTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/AddTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/AddTags)
