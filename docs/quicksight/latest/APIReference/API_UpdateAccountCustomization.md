---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAccountCustomization.html
---

# UpdateAccountCustomization
<a name="API_UpdateAccountCustomization"></a>

Updates Amazon Quick Sight customizations. Currently, the only customization that you can use is a theme.

You can use customizations for your AWS account or, if you specify a namespace, for a Quick Sight namespace instead. Customizations that apply to a namespace override customizations that apply to an AWS account. To find out which customizations apply, use the `DescribeAccountCustomization` API operation.

## Request Syntax
<a name="API_UpdateAccountCustomization_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/customizations?namespace={{Namespace}} HTTP/1.1
Content-type: application/json

{
   "AccountCustomization": {
      "DefaultEmailCustomizationTemplate": "{{string}}",
      "DefaultTheme": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateAccountCustomization_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateAccountCustomization_RequestSyntax) **   <a name="QS-UpdateAccountCustomization-request-uri-AwsAccountId"></a>
The ID for the AWS account that you want to update Quick Sight customizations for.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [Namespace](#API_UpdateAccountCustomization_RequestSyntax) **   <a name="QS-UpdateAccountCustomization-request-uri-Namespace"></a>
The namespace that you want to update Quick Sight customizations for.
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`

## Request Body
<a name="API_UpdateAccountCustomization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountCustomization](#API_UpdateAccountCustomization_RequestSyntax) **   <a name="QS-UpdateAccountCustomization-request-AccountCustomization"></a>
The Quick Sight customizations you're updating.
Type: [AccountCustomization](API_AccountCustomization.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateAccountCustomization_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AccountCustomization": {
      "DefaultEmailCustomizationTemplate": "string",
      "DefaultTheme": "string"
   },
   "Arn": "string",
   "AwsAccountId": "string",
   "Namespace": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateAccountCustomization_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateAccountCustomization_ResponseSyntax) **   <a name="QS-UpdateAccountCustomization-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AccountCustomization](#API_UpdateAccountCustomization_ResponseSyntax) **   <a name="QS-UpdateAccountCustomization-response-AccountCustomization"></a>
The Quick Sight customizations you're updating.
Type: [AccountCustomization](API_AccountCustomization.md) object

 ** [Arn](#API_UpdateAccountCustomization_ResponseSyntax) **   <a name="QS-UpdateAccountCustomization-response-Arn"></a>
The Amazon Resource Name (ARN) for the updated customization for this AWS account.
Type: String

 ** [AwsAccountId](#API_UpdateAccountCustomization_ResponseSyntax) **   <a name="QS-UpdateAccountCustomization-response-AwsAccountId"></a>
The ID for the AWS account that you want to update Quick Sight customizations for.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`

 ** [Namespace](#API_UpdateAccountCustomization_ResponseSyntax) **   <a name="QS-UpdateAccountCustomization-response-Namespace"></a>
The namespace associated with the customization that you're updating.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`

 ** [RequestId](#API_UpdateAccountCustomization_ResponseSyntax) **   <a name="QS-UpdateAccountCustomization-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateAccountCustomization_Errors"></a>

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

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ResourceUnavailableException **
This resource is currently unavailable.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateAccountCustomization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateAccountCustomization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateAccountCustomization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateAccountCustomization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateAccountCustomization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateAccountCustomization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateAccountCustomization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateAccountCustomization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateAccountCustomization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateAccountCustomization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateAccountCustomization)
