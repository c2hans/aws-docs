---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContactFlowModuleAlias.html
---

# CreateContactFlowModuleAlias
<a name="API_CreateContactFlowModuleAlias"></a>

Creates a named alias that points to a specific version of a contact flow module.

## Request Syntax
<a name="API_CreateContactFlowModuleAlias_RequestSyntax"></a>

```
PUT /contact-flow-modules/{{InstanceId}}/{{ContactFlowModuleId}}/alias HTTP/1.1
Content-type: application/json

{
   "AliasName": "{{string}}",
   "ContactFlowModuleVersion": {{number}},
   "Description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateContactFlowModuleAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowModuleId](#API_CreateContactFlowModuleAlias_RequestSyntax) **   <a name="connect-CreateContactFlowModuleAlias-request-uri-ContactFlowModuleId"></a>
The identifier of the flow module.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_CreateContactFlowModuleAlias_RequestSyntax) **   <a name="connect-CreateContactFlowModuleAlias-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_CreateContactFlowModuleAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AliasName](#API_CreateContactFlowModuleAlias_RequestSyntax) **   <a name="connect-CreateContactFlowModuleAlias-request-AliasName"></a>
The name of the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([$0-9a-zA-Z][_-]?)+$`
Required: Yes

 ** [ContactFlowModuleVersion](#API_CreateContactFlowModuleAlias_RequestSyntax) **   <a name="connect-CreateContactFlowModuleAlias-request-ContactFlowModuleVersion"></a>
The version of the flow module.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** [Description](#API_CreateContactFlowModuleAlias_RequestSyntax) **   <a name="connect-CreateContactFlowModuleAlias-request-Description"></a>
The description of the alias.
Type: String
Required: No

## Response Syntax
<a name="API_CreateContactFlowModuleAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlowModuleArn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateContactFlowModuleAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlowModuleArn](#API_CreateContactFlowModuleAlias_ResponseSyntax) **   <a name="connect-CreateContactFlowModuleAlias-response-ContactFlowModuleArn"></a>
The Amazon Resource Name (ARN) of the flow module.
Type: String

 ** [Id](#API_CreateContactFlowModuleAlias_ResponseSyntax) **   <a name="connect-CreateContactFlowModuleAlias-response-Id"></a>
The identifier of the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_CreateContactFlowModuleAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

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
<a name="API_CreateContactFlowModuleAlias_Examples"></a>

### Sample Request
<a name="API_CreateContactFlowModuleAlias_Example_1"></a>

This example illustrates one usage of CreateContactFlowModuleAlias.

```
{
  "AliasName": "production",
  "ContactFlowModuleVersion": 2,
  "Description": "Production version of the customer service module"
}
```

### Sample Response
<a name="API_CreateContactFlowModuleAlias_Example_2"></a>

This example illustrates one usage of CreateContactFlowModuleAlias.

```
{
  "ContactFlowModuleArn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-1234-1234-123456789012/flow-module/abcdefgh-1234-5678-9012-abcdefghijkl",
  "Id": "12345678-1234-1234-1234-1234678-1234-1234-1234-123456789012-12345678"
}
```

## See Also
<a name="API_CreateContactFlowModuleAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateContactFlowModuleAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateContactFlowModuleAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateContactFlowModuleAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateContactFlowModuleAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateContactFlowModuleAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateContactFlowModuleAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateContactFlowModuleAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateContactFlowModuleAlias)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateContactFlowModuleAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateContactFlowModuleAlias)
