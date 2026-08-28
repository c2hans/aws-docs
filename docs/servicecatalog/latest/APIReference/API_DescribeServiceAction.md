---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeServiceAction.html
---

# DescribeServiceAction
<a name="API_DescribeServiceAction"></a>

Describes a self-service action.

## Request Syntax
<a name="API_DescribeServiceAction_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeServiceAction_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DescribeServiceAction_RequestSyntax) **   <a name="servicecatalog-DescribeServiceAction-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Id](#API_DescribeServiceAction_RequestSyntax) **   <a name="servicecatalog-DescribeServiceAction-request-Id"></a>
The self-service action identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_DescribeServiceAction_ResponseSyntax"></a>

```
{
   "ServiceActionDetail": {
      "Definition": {
         "string" : "string"
      },
      "ServiceActionSummary": {
         "DefinitionType": "string",
         "Description": "string",
         "Id": "string",
         "Name": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeServiceAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ServiceActionDetail](#API_DescribeServiceAction_ResponseSyntax) **   <a name="servicecatalog-DescribeServiceAction-response-ServiceActionDetail"></a>
Detailed information about the self-service action.
Type: [ServiceActionDetail](API_ServiceActionDetail.md) object

## Errors
<a name="API_DescribeServiceAction_Errors"></a>

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeServiceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribeServiceAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeServiceAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribeServiceAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeServiceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeServiceAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeServiceAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeServiceAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeServiceAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribeServiceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeServiceAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
