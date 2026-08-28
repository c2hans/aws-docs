---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_IntegrationResponse.html
---

# IntegrationResponse
<a name="API_IntegrationResponse"></a>

Represents an integration response. The status code must map to an existing MethodResponse, and parameters and templates can be used to transform the back-end response.

## Contents
<a name="API_IntegrationResponse_Contents"></a>

 ** contentHandling **   <a name="apigw-Type-IntegrationResponse-contentHandling"></a>
Specifies how to handle response payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the following behaviors:
If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.
Type: String
Valid Values: `CONVERT_TO_BINARY | CONVERT_TO_TEXT`
Required: No

 ** responseParameters **   <a name="apigw-Type-IntegrationResponse-responseParameters"></a>
A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of `method.response.header.{name}`, where `name` is a valid and unique header name. The mapped non-static value must match the pattern of `integration.response.header.{name}` or `integration.response.body.{JSON-expression}`, where `name` is a valid and unique response header name and `JSON-expression` is a valid JSON expression without the `$` prefix.
Type: String to string map
Required: No

 ** responseTemplates **   <a name="apigw-Type-IntegrationResponse-responseTemplates"></a>
Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
Type: String to string map
Required: No

 ** selectionPattern **   <a name="apigw-Type-IntegrationResponse-selectionPattern"></a>
Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the `.+` regex to match error response. However, make sure that the error response does not contain any newline (`\n`) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.
Type: String
Required: No

 ** statusCode **   <a name="apigw-Type-IntegrationResponse-statusCode"></a>
Specifies the status code that is used to map the integration response to an existing MethodResponse.
Type: String
Pattern: `[1-5]\d\d`
Required: No

## See Also
<a name="API_IntegrationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/IntegrationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/IntegrationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/IntegrationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
