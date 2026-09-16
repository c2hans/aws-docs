---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContactFlow.html
---

# CreateContactFlow
<a name="API_CreateContactFlow"></a>

Creates a flow for the specified Connect Customer instance.

You can also create and update flows using the [Connect Customer Flow language](https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html).

## Request Syntax
<a name="API_CreateContactFlow_RequestSyntax"></a>

```
PUT /contact-flows/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "Content": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Status": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateContactFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateContactFlow_RequestSyntax) **   <a name="connect-CreateContactFlow-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateContactFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Content](#API_CreateContactFlow_RequestSyntax) **   <a name="connect-CreateContactFlow-request-Content"></a>
The JSON string that represents the content of the flow. For an example, see [Example flow in Connect Customer Flow language](https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html).
Length Constraints: Minimum length of 1. Maximum length of 256000.
Type: String
Required: Yes

 ** [Description](#API_CreateContactFlow_RequestSyntax) **   <a name="connect-CreateContactFlow-request-Description"></a>
The description of the flow.
Type: String
Required: No

 ** [Name](#API_CreateContactFlow_RequestSyntax) **   <a name="connect-CreateContactFlow-request-Name"></a>
The name of the flow.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [Status](#API_CreateContactFlow_RequestSyntax) **   <a name="connect-CreateContactFlow-request-Status"></a>
Indicates the flow status as either `SAVED` or `PUBLISHED`. The `PUBLISHED` status will initiate validation on the content. the `SAVED` status does not initiate validation of the content. `SAVED` \| `PUBLISHED`.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** [Tags](#API_CreateContactFlow_RequestSyntax) **   <a name="connect-CreateContactFlow-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [Type](#API_CreateContactFlow_RequestSyntax) **   <a name="connect-CreateContactFlow-request-Type"></a>
The type of the flow. For descriptions of the available types, see [Choose a flow type](https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types) in the *Connect Customer Administrator Guide*.
Type: String
Valid Values: `CONTACT_FLOW | CUSTOMER_QUEUE | CUSTOMER_HOLD | CUSTOMER_WHISPER | AGENT_HOLD | AGENT_WHISPER | OUTBOUND_WHISPER | AGENT_TRANSFER | QUEUE_TRANSFER | CAMPAIGN`
Required: Yes

## Response Syntax
<a name="API_CreateContactFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlowArn": "string",
   "ContactFlowId": "string",
   "FlowContentSha256": "string"
}
```

## Response Elements
<a name="API_CreateContactFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlowArn](#API_CreateContactFlow_ResponseSyntax) **   <a name="connect-CreateContactFlow-response-ContactFlowArn"></a>
The Amazon Resource Name (ARN) of the flow.
Type: String

 ** [ContactFlowId](#API_CreateContactFlow_ResponseSyntax) **   <a name="connect-CreateContactFlow-response-ContactFlowId"></a>
The identifier of the flow.
Type: String
Length Constraints: Maximum length of 500.

 ** [FlowContentSha256](#API_CreateContactFlow_ResponseSyntax) **   <a name="connect-CreateContactFlow-response-FlowContentSha256"></a>
Indicates the checksum value of the latest published flow content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9]{64}$`

## Errors
<a name="API_CreateContactFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidContactFlowException **
The flow is not valid.
 ** problems **
The problems with the flow. Please fix before trying again.
HTTP Status Code: 400

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

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateContactFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateContactFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateContactFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateContactFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateContactFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateContactFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateContactFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateContactFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateContactFlow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateContactFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateContactFlow)
