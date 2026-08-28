---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ConfirmTopicRuleDestination.html
---

# ConfirmTopicRuleDestination
<a name="API_ConfirmTopicRuleDestination"></a>

Confirms a topic rule destination. When you create a rule requiring a destination, AWS IoT sends a confirmation message to the endpoint or base address you specify. The message includes a token which you pass back when calling `ConfirmTopicRuleDestination` to confirm that you own or have access to the endpoint.

Requires permission to access the [ConfirmTopicRuleDestination](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ConfirmTopicRuleDestination_RequestSyntax"></a>

```
GET /confirmdestination/{{confirmationToken+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ConfirmTopicRuleDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [confirmationToken](#API_ConfirmTopicRuleDestination_RequestSyntax) **   <a name="iot-ConfirmTopicRuleDestination-request-uri-confirmationToken"></a>
The token used to confirm ownership or access to the topic rule confirmation URL.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_ConfirmTopicRuleDestination_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ConfirmTopicRuleDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_ConfirmTopicRuleDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ConfirmTopicRuleDestination_Errors"></a>

 ** ConflictingResourceUpdateException **
A conflicting resource update exception. This exception is thrown when two pending updates cause a conflict.
 ** message **
The message for the exception.
HTTP Status Code: 409

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

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_ConfirmTopicRuleDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ConfirmTopicRuleDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ConfirmTopicRuleDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ConfirmTopicRuleDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ConfirmTopicRuleDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ConfirmTopicRuleDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ConfirmTopicRuleDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ConfirmTopicRuleDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ConfirmTopicRuleDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ConfirmTopicRuleDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ConfirmTopicRuleDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
