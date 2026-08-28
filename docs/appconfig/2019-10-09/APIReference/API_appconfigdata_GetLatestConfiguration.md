---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html
---

# GetLatestConfiguration
<a name="API_appconfigdata_GetLatestConfiguration"></a>

Retrieves the latest deployed configuration. This API may return empty configuration data if the client already has the latest version. For more information about this API action and to view example AWS CLI commands that show how to use it with the [StartConfigurationSession](API_appconfigdata_StartConfigurationSession.md) API action, see [Retrieving feature flags and configuration data in AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/retrieving-feature-flags.html) in the * AWS AppConfig User Guide*.

**Important**
Note the following important information.
We recommend using the AWS AppConfig Agent to retrieve configuration data. Direct calls to the AWS AppConfig Data APIs are only recommended when using the Agent is not possible. For more information about the Agent, see [AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent.html) in the * AWS AppConfig User Guide*.
Each configuration token is only valid for one call to `GetLatestConfiguration`. The `GetLatestConfiguration` response includes a `NextPollConfigurationToken` that should always replace the token used for the just-completed call in preparation for the next one.
 `GetLatestConfiguration` is a priced call. For more information, see [Pricing](https://aws.amazon.com/systems-manager/pricing/).
You can configure applications to retrieve configuration data from a local cache rather than directly calling AWS AppConfig. Caching can improve performance and reduce costs. You can use the AWS AppConfig AWS Lambda extension to cache data on your behalf. For more information, see [AWS AppConfig integration with Lambda extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions.html) in the AWS AppConfig User Guide.
For containerized environments, you can use the AWS AppConfig agent for Amazon Elastic Container Service or Amazon Elastic Kubernetes Service. For more information, see [AWS AppConfig integration with Amazon ECS and Amazon EKS](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent.html).

## Request Syntax
<a name="API_appconfigdata_GetLatestConfiguration_RequestSyntax"></a>

```
GET /configuration?configuration_token={{ConfigurationToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_appconfigdata_GetLatestConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationToken](#API_appconfigdata_GetLatestConfiguration_RequestSyntax) **   <a name="appconfig-appconfigdata_GetLatestConfiguration-request-uri-ConfigurationToken"></a>
Token describing the current state of the configuration session. To obtain a token, first call the [StartConfigurationSession](API_appconfigdata_StartConfigurationSession.md) API. Note that every call to `GetLatestConfiguration` will return a new `ConfigurationToken` (`NextPollConfigurationToken` in the response) and *must* be provided to subsequent `GetLatestConfiguration` API calls.
This token should only be used once. To support long poll use cases, the token is valid for up to 24 hours. If a `GetLatestConfiguration` call uses an expired token, the system returns `BadRequestException`.
Pattern: `\S{1,8192}`
Required: Yes

## Request Body
<a name="API_appconfigdata_GetLatestConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_appconfigdata_GetLatestConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Next-Poll-Configuration-Token: {{NextPollConfigurationToken}}
Next-Poll-Interval-In-Seconds: {{NextPollIntervalInSeconds}}
Content-Type: {{ContentType}}
Version-Label: {{VersionLabel}}

{{Configuration}}
```

## Response Elements
<a name="API_appconfigdata_GetLatestConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ContentType](#API_appconfigdata_GetLatestConfiguration_ResponseSyntax) **   <a name="appconfig-appconfigdata_GetLatestConfiguration-response-ContentType"></a>
A standard MIME type describing the format of the configuration content.

 ** [NextPollConfigurationToken](#API_appconfigdata_GetLatestConfiguration_ResponseSyntax) **   <a name="appconfig-appconfigdata_GetLatestConfiguration-response-NextPollConfigurationToken"></a>
The latest token describing the current state of the configuration session. This *must* be provided to the next call to `GetLatestConfiguration.`
This token should only be used once. To support long poll use cases, the token is valid for up to 24 hours. If a `GetLatestConfiguration` call uses an expired token, the system returns `BadRequestException`.
Pattern: `\S{1,8192}`

 ** [NextPollIntervalInSeconds](#API_appconfigdata_GetLatestConfiguration_ResponseSyntax) **   <a name="appconfig-appconfigdata_GetLatestConfiguration-response-NextPollIntervalInSeconds"></a>
The amount of time the client should wait before polling for configuration updates again. The default value is 60 seconds. If you specify a value for `RequiredMinimumPollIntervalInSeconds`, the service uses the specified value for the desired poll interval instead.

 ** [VersionLabel](#API_appconfigdata_GetLatestConfiguration_ResponseSyntax) **   <a name="appconfig-appconfigdata_GetLatestConfiguration-response-VersionLabel"></a>
The user-defined label for the AWS AppConfig hosted configuration version. This attribute doesn't apply if the configuration is not from an AWS AppConfig hosted configuration version. If the client already has the latest version of the configuration data, this value is empty.

The response returns the following as the HTTP body.

 ** [Configuration](#API_appconfigdata_GetLatestConfiguration_ResponseSyntax) **   <a name="appconfig-appconfigdata_GetLatestConfiguration-response-Configuration"></a>
The data of the configuration. This may be empty if the client already has the latest version of configuration.

## Errors
<a name="API_appconfigdata_GetLatestConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by the service.
 ** Details **
Details describing why the request was invalid.
 ** Reason **
Code indicating the reason the request was invalid.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** ReferencedBy **
A map indicating which parameters in the request reference the resource that was not found.
 ** ResourceType **
The type of resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

## Examples
<a name="API_appconfigdata_GetLatestConfiguration_Examples"></a>

### Example
<a name="API_appconfigdata_GetLatestConfiguration_Example_1"></a>

This example illustrates one usage of GetLatestConfiguration.

#### Sample Request
<a name="API_appconfigdata_GetLatestConfiguration_Example_1_Request"></a>

```
GET /configuration?configuration_token=AYADeNgfsRxdKiJ37A12OZ9vN2cAXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZXkAREF1RzlLMTg1Tkx2Wjk4OGV2UXkyQ1UxV2ZxaGJTdkt2MkprKzJ4TlY2VkM0ZDVoRzBvbXFBTnFHcXpXcjU0dUM3Zz09AAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLXdlc3QtMTo4MzIyNzQ3ODA3Mzc6a2V5LzA4MGYxYWI3LTNjNmYtNGE1Yi04ZTg2LWE2MjdmNWJiMmRlMQC4AQIBAHiWVBJIpqEFGgjvLHxtJImRmyljpZnxt7FfxeEOE5H8xQF1SfOlWZFnHujbzJmIvNeSAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM0iTa25yw3uwnO6%2BrAgEQgDvLYYILWH%2Fx3SKKgyW1nOeBtS6go21vVPA6b8%2FwoFpxhzwjxy80jOfkVC2lM2l626BnJCvSPFfuZvcz%2FQIAAAAADAAAEAAAAAAAAAAAAAAAAADpQpWKSwnomgzEkYmidGKJ%2F%2F%2F%2F%2FwAAAAEAAAAAAAAAAAAAAAEAAAD8yfxkWB0geYfyI%2BDNJGiryebhmEoi8S8UHZSNN5JjJzTN2iORkjrA3DVvnhBTfoPh7o5bl4jwSYa%2F6as%2BmuQ9ntjYwymTZu7inYhsICYUKEDFxonBFJaEC32jEfg%2FMbPaGLOhNHdISiPAlMlOYmsw7phgl6ldbs9qrKVLlk1WNO3XTJiXyaWY4ANMfAX2JgMbGvNNY3HbfUneDGOENg6IfwKDykELIrJ6feE0JyKOV7mXfp%2F0r2pNiW9d6q%2BWDD1w4T87gCxgUGEPB%2FJ7JG3RhpGvECUmgKA0T06MjA7kWdt2IofDaLzRppFGpgLoPmxpM4qHz%2Fw6dMDmeXybKNZP84UP12zsJtUMhuspEQBnMGUCMQD8ssc6G8e6u8nov1ZdgF4m1ad3qyjiFd9DNRZHgLRFpw7%2BQIO%2FRB1l%2FIExP2ftUlkCMBT9oNlClJg4l9uGW5%2FqAiJ5n9ivK0ElRMwpvx96damGxt125XtMkmYf6a0OWSqnBw%3D%3D HTTP/1.1
Host: appconfigdata.us-west-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.4.15 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/appconfigdata.get-latest-configuration
X-Amz-Date: 20220218T190734Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220218/us-west-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_appconfigdata_GetLatestConfiguration_Example_1_Response"></a>

```
{
	"betaGroup": {
		"enabled": true
	}
}
```

## See Also
<a name="API_appconfigdata_GetLatestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfigdata-2021-11-11/GetLatestConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfigdata-2021-11-11/GetLatestConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfigdata-2021-11-11/GetLatestConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfigdata-2021-11-11/GetLatestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfigdata-2021-11-11/GetLatestConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfigdata-2021-11-11/GetLatestConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfigdata-2021-11-11/GetLatestConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfigdata-2021-11-11/GetLatestConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfigdata-2021-11-11/GetLatestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfigdata-2021-11-11/GetLatestConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
