---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateFlow.html
---

# AssociateFlow
<a name="API_AssociateFlow"></a>

Associates a connect resource to a flow.

## Request Syntax
<a name="API_AssociateFlow_RequestSyntax"></a>

```
PUT /flow-associations/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "FlowId": "{{string}}",
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_AssociateFlow_RequestSyntax) **   <a name="connect-AssociateFlow-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_AssociateFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FlowId](#API_AssociateFlow_RequestSyntax) **   <a name="connect-AssociateFlow-request-FlowId"></a>
The identifier of the flow.
Type: String
Required: Yes

 ** [ResourceId](#API_AssociateFlow_RequestSyntax) **   <a name="connect-AssociateFlow-request-ResourceId"></a>
The identifier of the resource.
+  AWS End User Messaging SMS phone number ARN when using `SMS_PHONE_NUMBER`
+  AWS End User Messaging Social phone number ARN when using `WHATSAPP_MESSAGING_PHONE_NUMBER`
Type: String
Required: Yes

 ** [ResourceType](#API_AssociateFlow_RequestSyntax) **   <a name="connect-AssociateFlow-request-ResourceType"></a>
A valid resource type.
Type: String
Valid Values: `SMS_PHONE_NUMBER | INBOUND_EMAIL | OUTBOUND_EMAIL | ANALYTICS_CONNECTOR | WHATSAPP_MESSAGING_PHONE_NUMBER`
Required: Yes

## Response Syntax
<a name="API_AssociateFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_AssociateFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/AssociateFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/AssociateFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociateFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/AssociateFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociateFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/AssociateFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/AssociateFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/AssociateFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/AssociateFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociateFlow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
