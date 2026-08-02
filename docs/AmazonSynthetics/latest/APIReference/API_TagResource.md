---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Assigns one or more tags (key-value pairs) to the specified canary or group.

Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.

Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

You can use the `TagResource` action with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.

You can associate as many as 50 tags with a canary or group.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /tags/{{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="synthetics-TagResource-request-uri-ResourceArn"></a>
The ARN of the canary or group that you're adding tags to.
The ARN format of a canary is `arn:aws:synthetics:Region:account-id:canary:canary-name `.
The ARN format of a group is `arn:aws:synthetics:Region:account-id:group:group-name `
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2,4}(-[a-z]{2,4})?-[a-z]+-\d{1}:\d{12}:(canary|group):[0-9a-z_\-]+`
Required: Yes

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="synthetics-TagResource-request-Tags"></a>
The list of key-value pairs to associate with the resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The request was not valid.
HTTP Status Code: 400

 ** ConflictException **
A conflicting operation is already in progress.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred. Try the operation again.
HTTP Status Code: 500

 ** NotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** TooManyRequestsException **
There were too many simultaneous requests. Try the operation again.
HTTP Status Code: 429

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/TagResource)
