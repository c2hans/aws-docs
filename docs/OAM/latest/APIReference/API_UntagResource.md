---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes one or more tags from the specified resource.

**Important**
Unlike tagging permissions in other AWS services, to tag or untag links and sinks you must have the `oam:ResourceTag` permission. The `iam:TagResource` permission does not allow you to tag and untag links and sinks.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{ResourceArn}}?tagKeys={{TagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_UntagResource_RequestSyntax) **   <a name="OAM-UntagResource-request-uri-ResourceArn"></a>
The ARN of the resource that you're removing tags from.
The ARN format of a sink is `arn:aws:oam:Region:account-id:sink/sink-id `
The ARN format of a link is `arn:aws:oam:Region:account-id:link/link-id `
For more information about ARN format, see [CloudWatch Logs resources and operations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html).
Pattern: `arn:(\w|-)+:oam:.+:.+:.+.*`
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="OAM-UntagResource-request-uri-TagKeys"></a>
The list of tag keys to remove from the resource.
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

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 404

 ** ValidationException **
The value of a parameter in the request caused an error.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/oam-2022-06-10/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/oam-2022-06-10/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/oam-2022-06-10/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/oam-2022-06-10/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/oam-2022-06-10/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/oam-2022-06-10/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/oam-2022-06-10/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/UntagResource)
