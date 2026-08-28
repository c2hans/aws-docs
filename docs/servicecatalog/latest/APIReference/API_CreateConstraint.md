---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreateConstraint.html
---

# CreateConstraint
<a name="API_CreateConstraint"></a>

Creates a constraint.

A delegated admin is authorized to invoke this command.

## Request Syntax
<a name="API_CreateConstraint_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Description": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "Parameters": "{{string}}",
   "PortfolioId": "{{string}}",
   "ProductId": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateConstraint_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_CreateConstraint_RequestSyntax) **   <a name="servicecatalog-CreateConstraint-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Description](#API_CreateConstraint_RequestSyntax) **   <a name="servicecatalog-CreateConstraint-request-Description"></a>
The description of the constraint.
Type: String
Length Constraints: Maximum length of 2000.
Required: No

 ** [IdempotencyToken](#API_CreateConstraint_RequestSyntax) **   <a name="servicecatalog-CreateConstraint-request-IdempotencyToken"></a>
A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [Parameters](#API_CreateConstraint_RequestSyntax) **   <a name="servicecatalog-CreateConstraint-request-Parameters"></a>
The constraint parameters, in JSON format. The syntax depends on the constraint type as follows:
LAUNCH
You are required to specify either the `RoleArn` or the `LocalRoleName` but can't use both.
Specify the `RoleArn` property as follows:
 `{"RoleArn" : "arn:aws:iam::123456789012:role/LaunchRole"}`
Specify the `LocalRoleName` property as follows:
 `{"LocalRoleName": "SCBasicLaunchRole"}`
If you specify the `LocalRoleName` property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account.
The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.
You cannot have both a `LAUNCH` and a `STACKSET` constraint.
You also cannot have more than one `LAUNCH` constraint on a product and portfolio.
NOTIFICATION
Specify the `NotificationArns` property as follows:
 `{"NotificationArns" : ["arn:aws:sns:us-east-1:123456789012:Topic"]}`
RESOURCE\_UPDATE
Specify the `TagUpdatesOnProvisionedProduct` property as follows:
 `{"Version":"2.0","Properties":{"TagUpdateOnProvisionedProduct":"String"}}`
The `TagUpdatesOnProvisionedProduct` property accepts a string value of `ALLOWED` or `NOT_ALLOWED`.
STACKSET
Specify the `Parameters` property as follows:
 `{"Version": "String", "Properties": {"AccountList": [ "String" ], "RegionList": [ "String" ], "AdminRole": "String", "ExecutionRole": "String"}}`
You cannot have both a `LAUNCH` and a `STACKSET` constraint.
You also cannot have more than one `STACKSET` constraint on a product and portfolio.
Products with a `STACKSET` constraint will launch an AWS CloudFormation stack set.
TEMPLATE
Specify the `Rules` property. For more information, see [Template Constraint Rules](http://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html).
Type: String
Required: Yes

 ** [PortfolioId](#API_CreateConstraint_RequestSyntax) **   <a name="servicecatalog-CreateConstraint-request-PortfolioId"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [ProductId](#API_CreateConstraint_RequestSyntax) **   <a name="servicecatalog-CreateConstraint-request-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [Type](#API_CreateConstraint_RequestSyntax) **   <a name="servicecatalog-CreateConstraint-request-Type"></a>
The type of constraint.
+  `LAUNCH`
+  `NOTIFICATION`
+  `RESOURCE_UPDATE`
+  `STACKSET`
+  `TEMPLATE`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_CreateConstraint_ResponseSyntax"></a>

```
{
   "ConstraintDetail": {
      "ConstraintId": "string",
      "Description": "string",
      "Owner": "string",
      "PortfolioId": "string",
      "ProductId": "string",
      "Type": "string"
   },
   "ConstraintParameters": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_CreateConstraint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConstraintDetail](#API_CreateConstraint_ResponseSyntax) **   <a name="servicecatalog-CreateConstraint-response-ConstraintDetail"></a>
Information about the constraint.
Type: [ConstraintDetail](API_ConstraintDetail.md) object

 ** [ConstraintParameters](#API_CreateConstraint_ResponseSyntax) **   <a name="servicecatalog-CreateConstraint-response-ConstraintParameters"></a>
The constraint parameters.
Type: String

 ** [Status](#API_CreateConstraint_ResponseSyntax) **   <a name="servicecatalog-CreateConstraint-response-Status"></a>
The status of the current request.
Type: String
Valid Values: `AVAILABLE | CREATING | FAILED`

## Errors
<a name="API_CreateConstraint_Errors"></a>

 ** DuplicateResourceException **
The specified resource is a duplicate.
HTTP Status Code: 400

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateConstraint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/CreateConstraint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/CreateConstraint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/CreateConstraint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/CreateConstraint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/CreateConstraint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CreateConstraint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/CreateConstraint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/CreateConstraint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/CreateConstraint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/CreateConstraint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
