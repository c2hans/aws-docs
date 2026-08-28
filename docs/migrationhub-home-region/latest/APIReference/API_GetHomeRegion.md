---
source_url: https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_GetHomeRegion.html
---

# GetHomeRegion
<a name="API_GetHomeRegion"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Returns the calling account’s home region, if configured. This API is used by other AWS services to determine the regional endpoint for calling AWS Application Discovery Service and Migration Hub. You must call `GetHomeRegion` at least once before you call any other AWS Application Discovery Service and AWS Migration Hub APIs, to obtain the account's Migration Hub home region.

## Response Syntax
<a name="API_GetHomeRegion_ResponseSyntax"></a>

```
{
   "HomeRegion": "string"
}
```

## Response Elements
<a name="API_GetHomeRegion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HomeRegion](#API_GetHomeRegion_ResponseSyntax) **   <a name="migrationhubhomeregion-GetHomeRegion-response-HomeRegion"></a>
The name of the home region of the calling account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^([a-z]+)-([a-z]+)-([0-9]+)$`

## Errors
<a name="API_GetHomeRegion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerError **
Exception raised when an internal, configuration, or dependency error is encountered.
HTTP Status Code: 500

 ** InvalidInputException **
Exception raised when the provided input violates a policy constraint or is entered in the wrong format or data type.
HTTP Status Code: 400

 ** ServiceUnavailableException **
Exception raised when a request fails due to temporary unavailability of the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 400

## See Also
<a name="API_GetHomeRegion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhub-config-2019-06-30/GetHomeRegion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhub-config-2019-06-30/GetHomeRegion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhub-config-2019-06-30/GetHomeRegion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhub-config-2019-06-30/GetHomeRegion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhub-config-2019-06-30/GetHomeRegion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhub-config-2019-06-30/GetHomeRegion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhub-config-2019-06-30/GetHomeRegion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhub-config-2019-06-30/GetHomeRegion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhub-config-2019-06-30/GetHomeRegion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhub-config-2019-06-30/GetHomeRegion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-home-region` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
