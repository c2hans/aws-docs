---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Assigns one or more tags (key-value pairs) to the specified Amazon Quick Sight resource.

Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values. You can use the `TagResource` operation with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.

You can associate as many as 50 tags with a resource. Amazon Quick Sight supports tagging on data set, data source, dashboard, template, topic, and user.

Tagging for Amazon Quick Sight works in a similar way to tagging for other AWS services, except for the following:
+ Tags are used to track costs for users in Amazon Quick Sight. You can't tag other resources that Amazon Quick Sight costs are based on, such as storage capacoty (SPICE), session usage, alert consumption, or reporting units.
+ Amazon Quick Sight doesn't currently support the tag editor for AWS Resource Groups.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /resources/{{ResourceArn}}/tags HTTP/1.1
Content-type: application/json

{
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_TagResource_RequestSyntax) **   <a name="QS-TagResource-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource that you want to tag.
Required: Yes

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="QS-TagResource-request-Tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string"
}
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_TagResource_ResponseSyntax) **   <a name="QS-TagResource-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_TagResource_ResponseSyntax) **   <a name="QS-TagResource-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TagResource)
