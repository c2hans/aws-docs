---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StartCanary.html
---

# StartCanary
<a name="API_StartCanary"></a>

Use this operation to run a canary that has already been created. The frequency of the canary runs is determined by the value of the canary's `Schedule`. To see a canary's schedule, use [GetCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanary.html).

## Request Syntax
<a name="API_StartCanary_RequestSyntax"></a>

```
POST /canary/{{name}}/start HTTP/1.1
```

## URI Request Parameters
<a name="API_StartCanary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_StartCanary_RequestSyntax) **   <a name="synthetics-StartCanary-request-uri-Name"></a>
The name of the canary that you want to run. To find canary names, use [DescribeCanaries](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html).
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9a-z_\-]+$`
Required: Yes

## Request Body
<a name="API_StartCanary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StartCanary_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StartCanary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartCanary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
A conflicting operation is already in progress.
HTTP Status Code: 409

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One of the specified resources was not found.
HTTP Status Code: 404

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_StartCanary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/StartCanary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/StartCanary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/StartCanary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/StartCanary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/StartCanary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/StartCanary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/StartCanary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/StartCanary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/StartCanary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/StartCanary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
