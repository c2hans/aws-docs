---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeTags.html
---

# DescribeTags
<a name="API_DescribeTags"></a>

Describes one or more of the tags for your Amazon ML object.

## Request Syntax
<a name="API_DescribeTags_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceId](#API_DescribeTags_RequestSyntax) **   <a name="amazonml-DescribeTags-request-ResourceId"></a>
The ID of the ML object. For example, `exampleModelId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [ResourceType](#API_DescribeTags_RequestSyntax) **   <a name="amazonml-DescribeTags-request-ResourceType"></a>
The type of the ML object.
Type: String
Valid Values: `BatchPrediction | DataSource | Evaluation | MLModel`
Required: Yes

## Response Syntax
<a name="API_DescribeTags_ResponseSyntax"></a>

```
{
   "ResourceId": "string",
   "ResourceType": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceId](#API_DescribeTags_ResponseSyntax) **   <a name="amazonml-DescribeTags-response-ResourceId"></a>
The ID of the tagged ML object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [ResourceType](#API_DescribeTags_ResponseSyntax) **   <a name="amazonml-DescribeTags-response-ResourceType"></a>
The type of the tagged ML object.
Type: String
Valid Values: `BatchPrediction | DataSource | Evaluation | MLModel`

 ** [Tags](#API_DescribeTags_ResponseSyntax) **   <a name="amazonml-DescribeTags-response-Tags"></a>
A list of tags associated with the ML object.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 100 items.

## Errors
<a name="API_DescribeTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An error on the server occurred when trying to process a request.
HTTP Status Code: 500

 ** InvalidInputException **
An error on the client occurred. Typically, the cause is an invalid input value.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A specified resource cannot be located.
HTTP Status Code: 400

## Examples
<a name="API_DescribeTags_Examples"></a>

### The following are an example request and response for the DescribeTags operation.
<a name="API_DescribeTags_Example_1"></a>

This example illustrates one usage of DescribeTags.

#### Sample Request
<a name="API_DescribeTags_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.DescribeTags
{
  "ResourceId": "exampleModelId",
  "ResourceType": "MLModel"
}
```

#### Sample Response
<a name="API_DescribeTags_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "ResourceId": "exampleModelId",
  "ResourceType": "MLModel",
  "Tags": {
      "Key":"exampleKey",
	  "Value":"exampleKeyValue"
  }
}
```

## See Also
<a name="API_DescribeTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/DescribeTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/DescribeTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/DescribeTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/DescribeTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/DescribeTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/DescribeTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/DescribeTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/DescribeTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/DescribeTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/DescribeTags)
