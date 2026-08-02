---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Retrieve a list of the tags (keys and values) that are associated with a specified resource. A *tag* is a label that you optionally define and associate with a resource in Amazon Pinpoint. Each tag consists of a required *tag key* and an optional associated *tag value*. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
GET /v1/email/tags?ResourceArn={{ResourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="pinpoint-ListTagsForResource-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource that you want to retrieve tag information for.
Required: Yes

## Request Body
<a name="API_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="pinpoint-ListTagsForResource-response-Tags"></a>
An array that lists all the tags that are associated with the resource. Each tag consists of a required tag key (`Key`) and an associated tag value (`Value`)
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/ListTagsForResource)
