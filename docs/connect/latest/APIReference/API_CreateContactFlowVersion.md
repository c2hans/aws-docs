---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContactFlowVersion.html
---

# CreateContactFlowVersion
<a name="API_CreateContactFlowVersion"></a>

Publishes a new version of the flow provided. Versions are immutable and monotonically increasing. If the `FlowContentSha256` provided is different from the `FlowContentSha256` of the `$LATEST` published flow content, then an error is returned. This API only supports creating versions for flows of type `Campaign`.

## Request Syntax
<a name="API_CreateContactFlowVersion_RequestSyntax"></a>

```
PUT /contact-flows/{{InstanceId}}/{{ContactFlowId}}/version HTTP/1.1
Content-type: application/json

{
   "ContactFlowVersion": {{number}},
   "Description": "{{string}}",
   "FlowContentSha256": "{{string}}",
   "LastModifiedRegion": "{{string}}",
   "LastModifiedTime": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateContactFlowVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowId](#API_CreateContactFlowVersion_RequestSyntax) **   <a name="connect-CreateContactFlowVersion-request-uri-ContactFlowId"></a>
The identifier of the flow.
Required: Yes

 ** [InstanceId](#API_CreateContactFlowVersion_RequestSyntax) **   <a name="connect-CreateContactFlowVersion-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateContactFlowVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ContactFlowVersion](#API_CreateContactFlowVersion_RequestSyntax) **   <a name="connect-CreateContactFlowVersion-request-ContactFlowVersion"></a>
The identifier of the flow version.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** [Description](#API_CreateContactFlowVersion_RequestSyntax) **   <a name="connect-CreateContactFlowVersion-request-Description"></a>
The description of the flow version.
Type: String
Required: No

 ** [FlowContentSha256](#API_CreateContactFlowVersion_RequestSyntax) **   <a name="connect-CreateContactFlowVersion-request-FlowContentSha256"></a>
Indicates the checksum value of the flow content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9]{64}$`
Required: No

 ** [LastModifiedRegion](#API_CreateContactFlowVersion_RequestSyntax) **   <a name="connect-CreateContactFlowVersion-request-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** [LastModifiedTime](#API_CreateContactFlowVersion_RequestSyntax) **   <a name="connect-CreateContactFlowVersion-request-LastModifiedTime"></a>
The AWS Region where this resource was last modified.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_CreateContactFlowVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlowArn": "string",
   "Version": number
}
```

## Response Elements
<a name="API_CreateContactFlowVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlowArn](#API_CreateContactFlowVersion_ResponseSyntax) **   <a name="connect-CreateContactFlowVersion-response-ContactFlowArn"></a>
The Amazon Resource Name (ARN) of the flow.
Type: String

 ** [Version](#API_CreateContactFlowVersion_ResponseSyntax) **   <a name="connect-CreateContactFlowVersion-response-Version"></a>
The identifier of the flow version.
Type: Long
Valid Range: Minimum value of 1.

## Errors
<a name="API_CreateContactFlowVersion_Errors"></a>

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

## Examples
<a name="API_CreateContactFlowVersion_Examples"></a>

### Sample Request
<a name="API_CreateContactFlowVersion_Example_1"></a>

This example illustrates one usage of CreateContactFlowVersion.

```
{
  "Description": "description of the flow version"
}
```

### Sample Response
<a name="API_CreateContactFlowVersion_Example_2"></a>

This example illustrates one usage of CreateContactFlowVersion.

```
{
  "ContactFlowArn": "[contact_flow_arn]",
  "Version": 1
}
```

## See Also
<a name="API_CreateContactFlowVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateContactFlowVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateContactFlowVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateContactFlowVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateContactFlowVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateContactFlowVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateContactFlowVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateContactFlowVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateContactFlowVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateContactFlowVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateContactFlowVersion)
