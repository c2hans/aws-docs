---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContactFlowModuleVersion.html
---

# CreateContactFlowModuleVersion
<a name="API_CreateContactFlowModuleVersion"></a>

Creates an immutable snapshot of a contact flow module, preserving its content and settings at a specific point in time for version control and rollback capabilities.

## Request Syntax
<a name="API_CreateContactFlowModuleVersion_RequestSyntax"></a>

```
PUT /contact-flow-modules/{{InstanceId}}/{{ContactFlowModuleId}}/version HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "FlowModuleContentSha256": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateContactFlowModuleVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowModuleId](#API_CreateContactFlowModuleVersion_RequestSyntax) **   <a name="connect-CreateContactFlowModuleVersion-request-uri-ContactFlowModuleId"></a>
The identifier of the flow module.
Required: Yes

 ** [InstanceId](#API_CreateContactFlowModuleVersion_RequestSyntax) **   <a name="connect-CreateContactFlowModuleVersion-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateContactFlowModuleVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateContactFlowModuleVersion_RequestSyntax) **   <a name="connect-CreateContactFlowModuleVersion-request-Description"></a>
The description of the flow module version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `.*\S.*`
Required: No

 ** [FlowModuleContentSha256](#API_CreateContactFlowModuleVersion_RequestSyntax) **   <a name="connect-CreateContactFlowModuleVersion-request-FlowModuleContentSha256"></a>
Indicates the checksum value of the flow module content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9]{64}$`
Required: No

## Response Syntax
<a name="API_CreateContactFlowModuleVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlowModuleArn": "string",
   "Version": number
}
```

## Response Elements
<a name="API_CreateContactFlowModuleVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlowModuleArn](#API_CreateContactFlowModuleVersion_ResponseSyntax) **   <a name="connect-CreateContactFlowModuleVersion-response-ContactFlowModuleArn"></a>
The Amazon Resource Name (ARN) of the flow module.
Type: String

 ** [Version](#API_CreateContactFlowModuleVersion_ResponseSyntax) **   <a name="connect-CreateContactFlowModuleVersion-response-Version"></a>
The version of the flow module.
Type: Long
Valid Range: Minimum value of 1.

## Errors
<a name="API_CreateContactFlowModuleVersion_Errors"></a>

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
<a name="API_CreateContactFlowModuleVersion_Examples"></a>

### Sample Request
<a name="API_CreateContactFlowModuleVersion_Example_1"></a>

This example illustrates one usage of CreateContactFlowModuleVersion.

```
{
  "Description": "Initial version of the customer service module"
}
```

### Sample Response
<a name="API_CreateContactFlowModuleVersion_Example_2"></a>

This example illustrates one usage of CreateContactFlowModuleVersion.

```
{
  "ContactFlowModuleArn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-1234-1234-123456789012/flow-module/abcdefgh-1234-5678-9012-abcdefghijkl",
  "Version": 1
}
```

## See Also
<a name="API_CreateContactFlowModuleVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateContactFlowModuleVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateContactFlowModuleVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateContactFlowModuleVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateContactFlowModuleVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateContactFlowModuleVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateContactFlowModuleVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateContactFlowModuleVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateContactFlowModuleVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateContactFlowModuleVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateContactFlowModuleVersion)
