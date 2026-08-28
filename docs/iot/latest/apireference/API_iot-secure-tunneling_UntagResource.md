---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_UntagResource.html
---

# UntagResource
<a name="API_iot-secure-tunneling_UntagResource"></a>

Removes a tag from a resource.

## Request Syntax
<a name="API_iot-secure-tunneling_UntagResource_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}",
   "tagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_iot-secure-tunneling_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_iot-secure-tunneling_UntagResource_RequestSyntax) **   <a name="iot-iot-secure-tunneling_UntagResource-request-resourceArn"></a>
The resource ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

 ** [tagKeys](#API_iot-secure-tunneling_UntagResource_RequestSyntax) **   <a name="iot-iot-secure-tunneling_UntagResource-request-tagKeys"></a>
The keys of the tags to remove.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Response Elements
<a name="API_iot-secure-tunneling_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_iot-secure-tunneling_UntagResource_Errors"></a>

 ** ResourceNotFoundException **
Thrown when an operation is attempted on a resource that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_iot-secure-tunneling_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsecuretunneling-2018-10-05/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsecuretunneling-2018-10-05/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsecuretunneling-2018-10-05/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsecuretunneling-2018-10-05/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsecuretunneling-2018-10-05/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsecuretunneling-2018-10-05/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsecuretunneling-2018-10-05/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsecuretunneling-2018-10-05/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsecuretunneling-2018-10-05/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsecuretunneling-2018-10-05/UntagResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
