---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateFlow.html
---

# UpdateFlow
<a name="API_UpdateFlow"></a>

Updates an existing flow. Supply only the fields you want to change. Updates both DRAFT and PUBLISHED versions. When `FlowDefinition` is provided, all existing steps are replaced with the new definition.

## Request Syntax
<a name="API_UpdateFlow_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/flows/{{FlowId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "FlowDefinition": {{JSON value}},
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateFlow_RequestSyntax) **   <a name="QS-UpdateFlow-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the flow that you are updating.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** [FlowId](#API_UpdateFlow_RequestSyntax) **   <a name="QS-UpdateFlow-request-uri-FlowId"></a>
The unique identifier of the flow to update.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_UpdateFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateFlow_RequestSyntax) **   <a name="QS-UpdateFlow-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Description](#API_UpdateFlow_RequestSyntax) **   <a name="QS-UpdateFlow-request-Description"></a>
Updated description for the flow. Omit to preserve the existing description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(?!\s+$)[^{}"\\<>]*`
Required: No

 ** [FlowDefinition](#API_UpdateFlow_RequestSyntax) **   <a name="QS-UpdateFlow-request-FlowDefinition"></a>
The definition of the flow, specifying the steps and configurations. This is the flow definition in Quick Flow's internal format. The format is subject to change. When provided, all existing steps are replaced. Omit to preserve the existing definition.
Always derive or depend on the flow definition from the `DescribeFlow` operation to ensure you are working with the latest format.
Type: JSON value
Required: No

 ** [Name](#API_UpdateFlow_RequestSyntax) **   <a name="QS-UpdateFlow-request-Name"></a>
Updated display name for the flow. Omit to preserve the existing name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!\s+$)[^{}"\\<>]*`
Required: No

## Response Syntax
<a name="API_UpdateFlow_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "FlowId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateFlow_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateFlow_ResponseSyntax) **   <a name="QS-UpdateFlow-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateFlow_ResponseSyntax) **   <a name="QS-UpdateFlow-response-Arn"></a>
The Amazon Resource Name (ARN) of the flow.
Type: String

 ** [FlowId](#API_UpdateFlow_ResponseSyntax) **   <a name="QS-UpdateFlow-response-FlowId"></a>
The unique identifier of the flow.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [RequestId](#API_UpdateFlow_ResponseSyntax) **   <a name="QS-UpdateFlow-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateFlow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateFlow)
