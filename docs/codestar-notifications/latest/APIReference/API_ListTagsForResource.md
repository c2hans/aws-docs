---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Returns a list of the tags associated with a notification rule.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
POST /listTagsForResource HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTagsForResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_ListTagsForResource_RequestSyntax) **   <a name="codestarnotifications-ListTagsForResource-request-Arn"></a>
The Amazon Resource Name (ARN) for the notification rule.
Type: String
Pattern: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="codestarnotifications-ListTagsForResource-response-Tags"></a>
The tags associated with the notification rule.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
 AWS CodeStar Notifications can't find a resource that matches the provided ARN.
HTTP Status Code: 404

 ** ValidationException **
One or more parameter values are not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codestar-notifications-2019-10-15/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codestar-notifications-2019-10-15/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codestar-notifications-2019-10-15/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codestar-notifications-2019-10-15/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codestar-notifications-2019-10-15/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codestar-notifications-2019-10-15/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codestar-notifications-2019-10-15/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/ListTagsForResource)
