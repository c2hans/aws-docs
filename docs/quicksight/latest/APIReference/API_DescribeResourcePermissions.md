---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeResourcePermissions.html
---

# DescribeResourcePermissions

Describes the service role configuration for your Amazon Quick Sight account.

Call this operation in the AWS Region where your Amazon Quick Sight account is registered (the home Region).

## Request Syntax
<a name="API_DescribeResourcePermissions_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/account-resource-permissions HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeResourcePermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeResourcePermissions_RequestSyntax) **   <a name="QS-DescribeResourcePermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account whose service role configuration you want to describe.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_DescribeResourcePermissions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeResourcePermissions_ResponseSyntax"></a>

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
<a name="API_DescribeResourcePermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeResourcePermissions_ResponseSyntax) **   <a name="QS-DescribeResourcePermissions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [CustomerManagedRoleArn](#API_DescribeResourcePermissions_ResponseSyntax) **   <a name="QS-DescribeResourcePermissions-response-CustomerManagedRoleArn"></a>
The ARN of the customer-managed role that Amazon Quick Sight uses for your account. Amazon Quick Sight returns this value only when `RoleType` is `CUSTOMER_MANAGED`.
Type: String

 ** [RequestId](#API_DescribeResourcePermissions_ResponseSyntax) **   <a name="QS-DescribeResourcePermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [RoleType](#API_DescribeResourcePermissions_ResponseSyntax) **   <a name="QS-DescribeResourcePermissions-response-RoleType"></a>
The type of service role that Amazon Quick Sight uses for your account.
Type: String
Valid Values: `QUICKSIGHT_MANAGED | CUSTOMER_MANAGED`

## Errors
<a name="API_DescribeResourcePermissions_Errors"></a>

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
<a name="API_DescribeResourcePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeResourcePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeResourcePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeResourcePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeResourcePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeResourcePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeResourcePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeResourcePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeResourcePermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeResourcePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeResourcePermissions)
