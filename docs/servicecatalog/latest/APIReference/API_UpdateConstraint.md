---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateConstraint.html
---

# UpdateConstraint
<a name="API_UpdateConstraint"></a>

Updates the specified constraint.

## Request Syntax
<a name="API_UpdateConstraint_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Description": "{{string}}",
   "Id": "{{string}}",
   "Parameters": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateConstraint_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_UpdateConstraint_RequestSyntax) **   <a name="servicecatalog-UpdateConstraint-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Description](#API_UpdateConstraint_RequestSyntax) **   <a name="servicecatalog-UpdateConstraint-request-Description"></a>
The updated description of the constraint.
Type: String
Length Constraints: Maximum length of 2000.
Required: No

 ** [Id](#API_UpdateConstraint_RequestSyntax) **   <a name="servicecatalog-UpdateConstraint-request-Id"></a>
The identifier of the constraint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [Parameters](#API_UpdateConstraint_RequestSyntax) **   <a name="servicecatalog-UpdateConstraint-request-Parameters"></a>
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
Required: No

## Response Syntax
<a name="API_UpdateConstraint_ResponseSyntax"></a>

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
<a name="API_UpdateConstraint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConstraintDetail](#API_UpdateConstraint_ResponseSyntax) **   <a name="servicecatalog-UpdateConstraint-response-ConstraintDetail"></a>
Information about the constraint.
Type: [ConstraintDetail](API_ConstraintDetail.md) object

 ** [ConstraintParameters](#API_UpdateConstraint_ResponseSyntax) **   <a name="servicecatalog-UpdateConstraint-response-ConstraintParameters"></a>
The constraint parameters.
Type: String

 ** [Status](#API_UpdateConstraint_ResponseSyntax) **   <a name="servicecatalog-UpdateConstraint-response-Status"></a>
The status of the current request.
Type: String
Valid Values: `AVAILABLE | CREATING | FAILED`

## Errors
<a name="API_UpdateConstraint_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateConstraint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/UpdateConstraint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateConstraint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/UpdateConstraint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateConstraint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateConstraint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateConstraint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateConstraint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateConstraint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/UpdateConstraint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateConstraint)
