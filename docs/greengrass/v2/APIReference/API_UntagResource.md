---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes a tag from an AWS IoT Greengrass resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="greengrassv2-UntagResource-request-uri-resourceArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource to untag.
Pattern: `arn:[^:]*:greengrass:[^:]*:(aws|[0-9]+):(components|deployments|coreDevices):.*`
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="greengrassv2-UntagResource-request-uri-tagKeys"></a>
A list of keys for tags to remove from the resource.
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 AWS IoT Greengrass can't process your request right now. Try again later.
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** resourceId **
The ID of the resource that isn't found.
 ** resourceType **
The type of the resource that isn't found.
HTTP Status Code: 404

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** fields **
The list of fields that failed to validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/UntagResource)
