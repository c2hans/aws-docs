---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContactFlowAlias.html
---

# CreateContactFlowAlias
<a name="API_CreateContactFlowAlias"></a>

Creates a named alias that points to a specific version of a flow.

## Request Syntax
<a name="API_CreateContactFlowAlias_RequestSyntax"></a>

```
PUT /contact-flows/{{InstanceId}}/{{ContactFlowId}}/alias HTTP/1.1
Content-type: application/json

{
   "AliasName": "{{string}}",
   "ContactFlowVersion": {{number}},
   "Description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateContactFlowAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowId](#API_CreateContactFlowAlias_RequestSyntax) **   <a name="connect-CreateContactFlowAlias-request-uri-ContactFlowId"></a>
The identifier of the flow.
Required: Yes

 ** [InstanceId](#API_CreateContactFlowAlias_RequestSyntax) **   <a name="connect-CreateContactFlowAlias-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_CreateContactFlowAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AliasName](#API_CreateContactFlowAlias_RequestSyntax) **   <a name="connect-CreateContactFlowAlias-request-AliasName"></a>
The name of the alias.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [ContactFlowVersion](#API_CreateContactFlowAlias_RequestSyntax) **   <a name="connect-CreateContactFlowAlias-request-ContactFlowVersion"></a>
The version of the flow.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** [Description](#API_CreateContactFlowAlias_RequestSyntax) **   <a name="connect-CreateContactFlowAlias-request-Description"></a>
The description of the alias.
Type: String
Required: No

## Response Syntax
<a name="API_CreateContactFlowAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlowArn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateContactFlowAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlowArn](#API_CreateContactFlowAlias_ResponseSyntax) **   <a name="connect-CreateContactFlowAlias-response-ContactFlowArn"></a>
The Amazon Resource Name (ARN) of the flow.
Type: String

 ** [Id](#API_CreateContactFlowAlias_ResponseSyntax) **   <a name="connect-CreateContactFlowAlias-response-Id"></a>
The identifier of the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_CreateContactFlowAlias_Errors"></a>

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
<a name="API_CreateContactFlowAlias_Examples"></a>

### Sample Request
<a name="API_CreateContactFlowAlias_Example_1"></a>

This example illustrates one usage of CreateContactFlowAlias.

```
{
  "AliasName": "production",
  "ContactFlowVersion": 2,
  "Description": "Production version of the customer service flow"
}
```

### Sample Response
<a name="API_CreateContactFlowAlias_Example_2"></a>

This example illustrates one usage of CreateContactFlowAlias.

```
{
  "ContactFlowArn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-1234-1234-123456789012/contact-flow/abcdefgh-1234-5678-9012-abcdefghijkl",
  "Id": "87654321-4321-4321-4321-210987654321"
}
```

## See Also
<a name="API_CreateContactFlowAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateContactFlowAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateContactFlowAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateContactFlowAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateContactFlowAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateContactFlowAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateContactFlowAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateContactFlowAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateContactFlowAlias)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateContactFlowAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateContactFlowAlias)
