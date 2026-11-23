---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateResourcePermissions.html
---

# UpdateResourcePermissions

Updates the service role configuration that Amazon Quick Sight uses to access resources in your AWS account. To use this operation, you must have the `quicksight:UpdateResourcePermissions` and `iam:PassRole` permissions.

Call this operation in the AWS Region where your Amazon Quick Sight account is registered (the home Region). You can switch from a role managed by Amazon Quick Sight to a customer-managed role, or replace one customer-managed role with another. You can't use this operation to switch back to a role managed by Amazon Quick Sight.

## Request Syntax
<a name="API_UpdateResourcePermissions_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/account-resource-permissions HTTP/1.1
Content-type: application/json

{
   "CustomerManagedRoleArn": "{{string}}",
   "RoleType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateResourcePermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateResourcePermissions_RequestSyntax) **   <a name="QS-UpdateResourcePermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account whose service role configuration you want to update.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateResourcePermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CustomerManagedRoleArn](#API_UpdateResourcePermissions_RequestSyntax) **   <a name="QS-UpdateResourcePermissions-request-CustomerManagedRoleArn"></a>
The ARN of the customer-managed role that you want Amazon Quick Sight to use. To use this operation, you must have the `iam:PassRole` permission for the role.
Configure the role as follows:
+ The role must belong to the AWS account specified by `AwsAccountId`.
+ Configure the role trust policy to allow the Amazon Quick Sight service principal to call `sts:AssumeRole`.
+ Attach a permissions policy that allows access to the resources that you want Amazon Quick Sight to use.
+ To use features that rely on session tags, configure the role trust policy to allow the Amazon Quick Sight service principal to call `sts:TagSession`.
If the role doesn't exist or its trust policy doesn't allow `sts:AssumeRole`, the request returns an `AccessDeniedException`.
When you call this operation, Amazon Quick Sight attempts to assume the role with session tags and records whether the attempt succeeds. If you later add or remove `sts:TagSession` from the trust policy, call this operation again with the same role ARN to refresh the stored capability.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [RoleType](#API_UpdateResourcePermissions_RequestSyntax) **   <a name="QS-UpdateResourcePermissions-request-RoleType"></a>
The type of service role that you want Amazon Quick Sight to use. The only supported value for this operation is `CUSTOMER_MANAGED`. Requests that specify `QUICKSIGHT_MANAGED` are rejected.
Type: String
Valid Values: `QUICKSIGHT_MANAGED | CUSTOMER_MANAGED`
Required: Yes

## Response Syntax
<a name="API_UpdateResourcePermissions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "CustomerManagedRoleArn": "string",
   "RequestId": "string",
   "RoleType": "string"
}
```

## Response Elements
<a name="API_UpdateResourcePermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateResourcePermissions_ResponseSyntax) **   <a name="QS-UpdateResourcePermissions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [CustomerManagedRoleArn](#API_UpdateResourcePermissions_ResponseSyntax) **   <a name="QS-UpdateResourcePermissions-response-CustomerManagedRoleArn"></a>
The ARN of the customer-managed role that Amazon Quick Sight uses for your account after the update.
Type: String

 ** [RequestId](#API_UpdateResourcePermissions_ResponseSyntax) **   <a name="QS-UpdateResourcePermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [RoleType](#API_UpdateResourcePermissions_ResponseSyntax) **   <a name="QS-UpdateResourcePermissions-response-RoleType"></a>
The type of service role that Amazon Quick Sight uses for your account after the update. This value is `CUSTOMER_MANAGED`.
Type: String
Valid Values: `QUICKSIGHT_MANAGED | CUSTOMER_MANAGED`

## Errors
<a name="API_UpdateResourcePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

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

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateResourcePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateResourcePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateResourcePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateResourcePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateResourcePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateResourcePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateResourcePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateResourcePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateResourcePermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateResourcePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateResourcePermissions)
