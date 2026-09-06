---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

 Returns a list of tags for the resource identified by a specified Amazon Resource Name (ARN). Tags are used to organize and categorize your CodeDeploy resources.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListTagsForResource_RequestSyntax) **   <a name="CodeDeploy-ListTagsForResource-request-NextToken"></a>
An identifier returned from the previous `ListTagsForResource` call. It can be used to return the next set of applications in the list.
Type: String
Required: No

 ** [ResourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="CodeDeploy-ListTagsForResource-request-ResourceArn"></a>
 The ARN of a CodeDeploy resource. `ListTagsForResource` returns all the tags associated with the resource that is identified by the `ResourceArn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "NextToken": "string",
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

 ** [NextToken](#API_ListTagsForResource_ResponseSyntax) **   <a name="CodeDeploy-ListTagsForResource-response-NextToken"></a>
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list application revisions call to return the next set of application revisions in the list.
Type: String

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="CodeDeploy-ListTagsForResource-response-Tags"></a>
 A list of tags returned by `ListTagsForResource`. The tags are associated with the resource identified by the input `ResourceArn` parameter.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArnNotSupportedException **
 The specified ARN is not supported. For example, it might be an ARN for a resource that is not expected.
HTTP Status Code: 400

 ** InvalidArnException **
 The specified ARN is not in a valid format.
HTTP Status Code: 400

 ** ResourceArnRequiredException **
 The ARN of a resource is required, but was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ListTagsForResource)
