---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteLoggingConfiguration.html
---

# DeleteLoggingConfiguration
<a name="API_waf_DeleteLoggingConfiguration"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Permanently deletes the [LoggingConfiguration](API_waf_LoggingConfiguration.md) from the specified web ACL.

## Request Syntax
<a name="API_waf_DeleteLoggingConfiguration_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_DeleteLoggingConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_waf_DeleteLoggingConfiguration_RequestSyntax) **   <a name="WAF-waf_DeleteLoggingConfiguration-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the web ACL from which you want to delete the [LoggingConfiguration](API_waf_LoggingConfiguration.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `.*\S.*`
Required: Yes

## Response Elements
<a name="API_waf_DeleteLoggingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_waf_DeleteLoggingConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 500

 ** WAFNonexistentItemException **
The operation failed because the referenced object doesn't exist.
HTTP Status Code: 400

 ** WAFStaleDataException **
The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.
HTTP Status Code: 400

## See Also
<a name="API_waf_DeleteLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/DeleteLoggingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/DeleteLoggingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/DeleteLoggingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/DeleteLoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/DeleteLoggingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/DeleteLoggingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/DeleteLoggingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/DeleteLoggingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/DeleteLoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/DeleteLoggingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
