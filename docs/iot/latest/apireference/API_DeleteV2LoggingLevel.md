---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteV2LoggingLevel.html
---

# DeleteV2LoggingLevel
<a name="API_DeleteV2LoggingLevel"></a>

Deletes a logging level.

Requires permission to access the [DeleteV2LoggingLevel](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DeleteV2LoggingLevel_RequestSyntax"></a>

```
DELETE /v2LoggingLevel?targetName={{targetName}}&targetType={{targetType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteV2LoggingLevel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [targetName](#API_DeleteV2LoggingLevel_RequestSyntax) **   <a name="iot-DeleteV2LoggingLevel-request-uri-targetName"></a>
The name of the resource for which you are configuring logging.
Required: Yes

 ** [targetType](#API_DeleteV2LoggingLevel_RequestSyntax) **   <a name="iot-DeleteV2LoggingLevel-request-uri-targetType"></a>
The type of resource for which you are configuring logging. Must be `THING_Group`.
Valid Values: `DEFAULT | THING_GROUP | CLIENT_ID | SOURCE_IP | PRINCIPAL_ID`
Required: Yes

## Request Body
<a name="API_DeleteV2LoggingLevel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteV2LoggingLevel_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteV2LoggingLevel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteV2LoggingLevel_Errors"></a>

 ** InternalException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

## See Also
<a name="API_DeleteV2LoggingLevel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeleteV2LoggingLevel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeleteV2LoggingLevel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeleteV2LoggingLevel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeleteV2LoggingLevel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeleteV2LoggingLevel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeleteV2LoggingLevel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeleteV2LoggingLevel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeleteV2LoggingLevel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeleteV2LoggingLevel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeleteV2LoggingLevel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
