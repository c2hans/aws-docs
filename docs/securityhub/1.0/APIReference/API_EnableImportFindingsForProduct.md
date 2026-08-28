---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_EnableImportFindingsForProduct.html
---

# EnableImportFindingsForProduct
<a name="API_EnableImportFindingsForProduct"></a>

Enables the integration of a partner product with Security Hub CSPM. Integrated products send findings to Security Hub CSPM.

When you enable a product integration, a permissions policy that grants permission for the product to send findings to Security Hub CSPM is applied.

## Request Syntax
<a name="API_EnableImportFindingsForProduct_RequestSyntax"></a>

```
POST /productSubscriptions HTTP/1.1
Content-type: application/json

{
   "ProductArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_EnableImportFindingsForProduct_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_EnableImportFindingsForProduct_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ProductArn](#API_EnableImportFindingsForProduct_RequestSyntax) **   <a name="securityhub-EnableImportFindingsForProduct-request-ProductArn"></a>
The ARN of the product to enable the integration for.
Type: String
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_EnableImportFindingsForProduct_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProductSubscriptionArn": "string"
}
```

## Response Elements
<a name="API_EnableImportFindingsForProduct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProductSubscriptionArn](#API_EnableImportFindingsForProduct_ResponseSyntax) **   <a name="securityhub-EnableImportFindingsForProduct-response-ProductSubscriptionArn"></a>
The ARN of your subscription to the product to enable integrations for.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_EnableImportFindingsForProduct_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceConflictException **
The resource specified in the request conflicts with an existing resource.
HTTP Status Code: 409

## See Also
<a name="API_EnableImportFindingsForProduct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/EnableImportFindingsForProduct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/EnableImportFindingsForProduct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/EnableImportFindingsForProduct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/EnableImportFindingsForProduct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/EnableImportFindingsForProduct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/EnableImportFindingsForProduct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/EnableImportFindingsForProduct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/EnableImportFindingsForProduct)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/EnableImportFindingsForProduct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/EnableImportFindingsForProduct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
