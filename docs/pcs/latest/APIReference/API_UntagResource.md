---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Deletes tags from an AWS PCS resource. To delete a tag, specify the tag key and the Amazon Resource Name (ARN) of the AWS PCS resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}",
   "tagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="PCS-UntagResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws.*:pcs:.*:[0-9]{12}:.*/[a-z0-9_\-]+`
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="PCS-UntagResource-request-tagKeys"></a>
1 or more tag keys to remove from the resource. Specify only tag keys and not tag values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.
 *Examples*
 ** resourceId **
 The unique identifier of the resource that was not found.
 ** resourceType **
 The type or category of the resource that was not found.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pcs-2023-02-10/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pcs-2023-02-10/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pcs-2023-02-10/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pcs-2023-02-10/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pcs-2023-02-10/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pcs-2023-02-10/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pcs-2023-02-10/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/UntagResource)
