---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_RequestValidator.html
---

# RequestValidator
<a name="API_RequestValidator"></a>

A set of validation rules for incoming Method requests.

## Contents
<a name="API_RequestValidator_Contents"></a>

 ** id **   <a name="apigw-Type-RequestValidator-id"></a>
The identifier of this RequestValidator.
Type: String
Required: No

 ** name **   <a name="apigw-Type-RequestValidator-name"></a>
The name of this RequestValidator
Type: String
Required: No

 ** validateRequestBody **   <a name="apigw-Type-RequestValidator-validateRequestBody"></a>
A Boolean flag to indicate whether to validate a request body according to the configured Model schema.
Type: Boolean
Required: No

 ** validateRequestParameters **   <a name="apigw-Type-RequestValidator-validateRequestParameters"></a>
A Boolean flag to indicate whether to validate request parameters (`true`) or not (`false`).
Type: Boolean
Required: No

## See Also
<a name="API_RequestValidator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/RequestValidator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/RequestValidator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/RequestValidator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
