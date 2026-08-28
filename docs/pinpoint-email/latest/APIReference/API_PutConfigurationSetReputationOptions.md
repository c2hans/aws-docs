---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetReputationOptions.html
---

# PutConfigurationSetReputationOptions
<a name="API_PutConfigurationSetReputationOptions"></a>

Enable or disable collection of reputation metrics for emails that you send using a particular configuration set in a specific AWS Region.

## Request Syntax
<a name="API_PutConfigurationSetReputationOptions_RequestSyntax"></a>

```
PUT /v1/email/configuration-sets/{{ConfigurationSetName}}/reputation-options HTTP/1.1
Content-type: application/json

{
   "ReputationMetricsEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_PutConfigurationSetReputationOptions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationSetName](#API_PutConfigurationSetReputationOptions_RequestSyntax) **   <a name="pinpoint-PutConfigurationSetReputationOptions-request-uri-ConfigurationSetName"></a>
The name of the configuration set that you want to enable or disable reputation metric tracking for.
Required: Yes

## Request Body
<a name="API_PutConfigurationSetReputationOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ReputationMetricsEnabled](#API_PutConfigurationSetReputationOptions_RequestSyntax) **   <a name="pinpoint-PutConfigurationSetReputationOptions-request-ReputationMetricsEnabled"></a>
If `true`, tracking of reputation metrics is enabled for the configuration set. If `false`, tracking of reputation metrics is disabled for the configuration set.
Type: Boolean
Required: No

## Response Syntax
<a name="API_PutConfigurationSetReputationOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutConfigurationSetReputationOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutConfigurationSetReputationOptions_Errors"></a>

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
<a name="API_PutConfigurationSetReputationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
