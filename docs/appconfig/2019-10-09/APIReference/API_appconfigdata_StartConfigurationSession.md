---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.html
---

# StartConfigurationSession
<a name="API_appconfigdata_StartConfigurationSession"></a>

Starts a configuration session used to retrieve a deployed configuration. For more information about this API action and to view example AWS CLI commands that show how to use it with the [GetLatestConfiguration](API_appconfigdata_GetLatestConfiguration.md) API action, see [Retrieving feature flags and configuration data in AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/retrieving-feature-flags.html) in the * AWS AppConfig User Guide*.

**Important**
We recommend using the AWS AppConfig Agent to retrieve configuration data. Direct calls to the AWS AppConfig Data APIs are only recommended when using the Agent is not possible. For more information about the Agent, see [AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent.html) in the * AWS AppConfig User Guide*.

## Request Syntax
<a name="API_appconfigdata_StartConfigurationSession_RequestSyntax"></a>

```
POST /configurationsessions HTTP/1.1
Content-type: application/json

{
   "ApplicationIdentifier": "{{string}}",
   "ConfigurationProfileIdentifier": "{{string}}",
   "EnvironmentIdentifier": "{{string}}",
   "RequiredMinimumPollIntervalInSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_appconfigdata_StartConfigurationSession_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_appconfigdata_StartConfigurationSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationIdentifier](#API_appconfigdata_StartConfigurationSession_RequestSyntax) **   <a name="appconfig-appconfigdata_StartConfigurationSession-request-ApplicationIdentifier"></a>
The application ID or the application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [ConfigurationProfileIdentifier](#API_appconfigdata_StartConfigurationSession_RequestSyntax) **   <a name="appconfig-appconfigdata_StartConfigurationSession-request-ConfigurationProfileIdentifier"></a>
The configuration profile ID or the configuration profile name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [EnvironmentIdentifier](#API_appconfigdata_StartConfigurationSession_RequestSyntax) **   <a name="appconfig-appconfigdata_StartConfigurationSession-request-EnvironmentIdentifier"></a>
The environment ID or the environment name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [RequiredMinimumPollIntervalInSeconds](#API_appconfigdata_StartConfigurationSession_RequestSyntax) **   <a name="appconfig-appconfigdata_StartConfigurationSession-request-RequiredMinimumPollIntervalInSeconds"></a>
(Optional) Sets a constraint on a session. If you specify a value of, for example, 60 seconds, then the client that established the session can't call [GetLatestConfiguration](API_appconfigdata_GetLatestConfiguration.md) more frequently than every 60 seconds.
Type: Integer
Valid Range: Minimum value of 15. Maximum value of 86400.
Required: No

## Response Syntax
<a name="API_appconfigdata_StartConfigurationSession_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "InitialConfigurationToken": "string"
}
```

## Response Elements
<a name="API_appconfigdata_StartConfigurationSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [InitialConfigurationToken](#API_appconfigdata_StartConfigurationSession_ResponseSyntax) **   <a name="appconfig-appconfigdata_StartConfigurationSession-response-InitialConfigurationToken"></a>
Token encapsulating state about the configuration session. Provide this token to the `GetLatestConfiguration` API to retrieve configuration data.
This token should only be used once in your first call to `GetLatestConfiguration`. You *must* use the new token in the `GetLatestConfiguration` response (`NextPollConfigurationToken`) in each subsequent call to `GetLatestConfiguration`. If there is no change to a configuration, the token doesn't return the AWS AppConfig configuration profile.
The `InitialConfigurationToken` and `NextPollConfigurationToken` should only be used once. To support long poll use cases, the tokens are valid for up to 24 hours. If a `GetLatestConfiguration` call uses an expired token, the system returns `BadRequestException`.
Type: String
Pattern: `\S{1,8192}`

## Errors
<a name="API_appconfigdata_StartConfigurationSession_Errors"></a>

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
<a name="API_appconfigdata_StartConfigurationSession_Examples"></a>

### Example
<a name="API_appconfigdata_StartConfigurationSession_Example_1"></a>

This example illustrates one usage of StartConfigurationSession.

#### Sample Request
<a name="API_appconfigdata_StartConfigurationSession_Example_1_Request"></a>

```
POST /configurationsessions HTTP/1.1
Host: appconfigdata.us-west-1.amazonaws.com
Accept-Encoding: identity
Content-Type: application/json
User-Agent: aws-cli/2.4.15 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/appconfigdata.start-configuration-session
X-Amz-Date: 20220218T190442Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220218/us-west-1/appconfig/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 141

{"ApplicationIdentifier": "MyMobileApp", "ConfigurationProfileIdentifier": "MyAccessListFlag", "EnvironmentIdentifier": "MyMobileAppProdEnv"}
```

#### Sample Response
<a name="API_appconfigdata_StartConfigurationSession_Example_1_Response"></a>

```
{
	"InitialConfigurationToken": "AYADeNgfsRxdKiJ37A12OZ9vN2cAXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZXkAREF1RzlLMTg1Tkx2Wjk4OGV2UXkyQ1UxV2ZxaGJTdkt2MkprKzJ4TlY2VkM0ZDVoRzBvbXFBTnFHcXpXcjU0dUM3Zz09AAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLXdlc3QtMTo4MzIyNzQ3ODA3Mzc6a2V5LzA4MGYxYWI3LTNjNmYtNGE1Yi04ZTg2LWE2MjdmNWJiMmRlMQC4AQIBAHiWVBJIpqEFGgjvLHxtJImRmyljpZnxt7FfxeEOE5H8xQF1SfOlWZFnHujbzJmIvNeSAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM0iTa25yw3uwnO6+rAgEQgDvLYYILWH/x3SKKgyW1nOeBtS6go21vVPA6b8/woFpxhzwjxy80jOfkVC2lM2l626BnJCvSPFfuZvcz/QIAAAAADAAAEAAAAAAAAAAAAAAAAADpQpWKSwnomgzEkYmidGKJ/////wAAAAEAAAAAAAAAAAAAAAEAAAD8yfxkWB0geYfyI+DNJGiryebhmEoi8S8UHZSNN5JjJzTN2iORkjrA3DVvnhBTfoPh7o5bl4jwSYa/6as+muQ9ntjYwymTZu7inYhsICYUKEDFxonBFJaEC32jEfg/MbPaGLOhNHdISiPAlMlOYmsw7phgl6ldbs9qrKVLlk1WNO3XTJiXyaWY4ANMfAX2JgMbGvNNY3HbfUneDGOENg6IfwKDykELIrJ6feE0JyKOV7mXfp/0r2pNiW9d6q+WDD1w4T87gCxgUGEPB/J7JG3RhpGvECUmgKA0T06MjA7kWdt2IofDaLzRppFGpgLoPmxpM4qHz/w6dMDmeXybKNZP84UP12zsJtUMhuspEQBnMGUCMQD8ssc6G8e6u8nov1ZdgF4m1ad3qyjiFd9DNRZHgLRFpw7+QIO/RB1l/IExP2ftUlkCMBT9oNlClJg4l9uGW5/qAiJ5n9ivK0ElRMwpvx96damGxt125XtMkmYf6a0OWSqnBw=="
}
```

## See Also
<a name="API_appconfigdata_StartConfigurationSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfigdata-2021-11-11/StartConfigurationSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfigdata-2021-11-11/StartConfigurationSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfigdata-2021-11-11/StartConfigurationSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfigdata-2021-11-11/StartConfigurationSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfigdata-2021-11-11/StartConfigurationSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfigdata-2021-11-11/StartConfigurationSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfigdata-2021-11-11/StartConfigurationSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfigdata-2021-11-11/StartConfigurationSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfigdata-2021-11-11/StartConfigurationSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfigdata-2021-11-11/StartConfigurationSession)
