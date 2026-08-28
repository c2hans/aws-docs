---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes one or more tags from the specified resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
POST /untag-resource HTTP/1.1
Content-type: application/json

{
   "ResourceArn": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_UntagResource_RequestSyntax) **   <a name="applicationsignals-UntagResource-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the CloudWatch resource that you want to delete tags from.
The ARN format of an Application Signals SLO is `arn:aws:cloudwatch:Region:account-id:slo:slo-name `
For more information about ARN format, see [ Resource Types Defined by Amazon CloudWatch](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies) in the *Amazon Web Services General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="applicationsignals-UntagResource-request-TagKeys"></a>
The list of tag keys to remove from the resource.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

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
Resource not found.
 ** ResourceId **
Can't find the resource id.
 ** ResourceType **
The resource type is not valid.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/UntagResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
