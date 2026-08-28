---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeConstraint.html
---

# DescribeConstraint
<a name="API_DescribeConstraint"></a>

Gets information about the specified constraint.

## Request Syntax
<a name="API_DescribeConstraint_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConstraint_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DescribeConstraint_RequestSyntax) **   <a name="servicecatalog-DescribeConstraint-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Id](#API_DescribeConstraint_RequestSyntax) **   <a name="servicecatalog-DescribeConstraint-request-Id"></a>
The identifier of the constraint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_DescribeConstraint_ResponseSyntax"></a>

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
<a name="API_DescribeConstraint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConstraintDetail](#API_DescribeConstraint_ResponseSyntax) **   <a name="servicecatalog-DescribeConstraint-response-ConstraintDetail"></a>
Information about the constraint.
Type: [ConstraintDetail](API_ConstraintDetail.md) object

 ** [ConstraintParameters](#API_DescribeConstraint_ResponseSyntax) **   <a name="servicecatalog-DescribeConstraint-response-ConstraintParameters"></a>
The constraint parameters.
Type: String

 ** [Status](#API_DescribeConstraint_ResponseSyntax) **   <a name="servicecatalog-DescribeConstraint-response-Status"></a>
The status of the current request.
Type: String
Valid Values: `AVAILABLE | CREATING | FAILED`

## Errors
<a name="API_DescribeConstraint_Errors"></a>

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConstraint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribeConstraint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeConstraint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribeConstraint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeConstraint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeConstraint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeConstraint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeConstraint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeConstraint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribeConstraint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeConstraint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
