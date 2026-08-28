---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetTrackingOptions.html
---

# PutConfigurationSetTrackingOptions
<a name="API_PutConfigurationSetTrackingOptions"></a>

Specify a custom domain to use for open and click tracking elements in email that you send using Amazon Pinpoint.

## Request Syntax
<a name="API_PutConfigurationSetTrackingOptions_RequestSyntax"></a>

```
PUT /v1/email/configuration-sets/{{ConfigurationSetName}}/tracking-options HTTP/1.1
Content-type: application/json

{
   "CustomRedirectDomain": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutConfigurationSetTrackingOptions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationSetName](#API_PutConfigurationSetTrackingOptions_RequestSyntax) **   <a name="pinpoint-PutConfigurationSetTrackingOptions-request-uri-ConfigurationSetName"></a>
The name of the configuration set that you want to add a custom tracking domain to.
Required: Yes

## Request Body
<a name="API_PutConfigurationSetTrackingOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CustomRedirectDomain](#API_PutConfigurationSetTrackingOptions_RequestSyntax) **   <a name="pinpoint-PutConfigurationSetTrackingOptions-request-CustomRedirectDomain"></a>
The domain that you want to use to track open and click events.
Type: String
Required: No

## Response Syntax
<a name="API_PutConfigurationSetTrackingOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutConfigurationSetTrackingOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutConfigurationSetTrackingOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_PutConfigurationSetTrackingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
