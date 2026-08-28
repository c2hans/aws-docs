---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DetachPrincipalPolicy.html
---

# DetachPrincipalPolicy
<a name="API_DetachPrincipalPolicy"></a>

Removes the specified policy from the specified certificate.

 **Note:** This action is deprecated and works as expected for backward compatibility, but we won't add enhancements. Use [DetachPolicy](API_DetachPolicy.md) instead.

Requires permission to access the [DetachPrincipalPolicy](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DetachPrincipalPolicy_RequestSyntax"></a>

```
DELETE /principal-policies/{{policyName}} HTTP/1.1
x-amzn-iot-principal: {{principal}}
```

## URI Request Parameters
<a name="API_DetachPrincipalPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyName](#API_DetachPrincipalPolicy_RequestSyntax) **   <a name="iot-DetachPrincipalPolicy-request-uri-policyName"></a>
The name of the policy to detach.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** [principal](#API_DetachPrincipalPolicy_RequestSyntax) **   <a name="iot-DetachPrincipalPolicy-request-principal"></a>
The principal.
Valid principals are CertificateArn (arn:aws:iot:*region*:*accountId*:cert/*certificateId*), thingGroupArn (arn:aws:iot:*region*:*accountId*:thinggroup/*groupName*) and CognitoId (*region*:*id*).
Required: Yes

## Request Body
<a name="API_DetachPrincipalPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DetachPrincipalPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DetachPrincipalPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DetachPrincipalPolicy_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_DetachPrincipalPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DetachPrincipalPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DetachPrincipalPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DetachPrincipalPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DetachPrincipalPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DetachPrincipalPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DetachPrincipalPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DetachPrincipalPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DetachPrincipalPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DetachPrincipalPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DetachPrincipalPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
