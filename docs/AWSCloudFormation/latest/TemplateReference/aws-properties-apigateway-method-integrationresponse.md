---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-method-integrationresponse.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::Method IntegrationResponse
<a name="aws-properties-apigateway-method-integrationresponse"></a>

`IntegrationResponse` is a property of the [Amazon API Gateway Method Integration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html) property type that specifies the response that API Gateway sends after a method's backend finishes processing a request.

## Syntax
<a name="aws-properties-apigateway-method-integrationresponse-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigateway-method-integrationresponse-syntax.json"></a>

```
{
  "[ContentHandling](#cfn-apigateway-method-integrationresponse-contenthandling)" : {{String}},
  "[ResponseParameters](#cfn-apigateway-method-integrationresponse-responseparameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ResponseTemplates](#cfn-apigateway-method-integrationresponse-responsetemplates)" : {{{{{Key}}: {{Value}}, ...}}},
  "[SelectionPattern](#cfn-apigateway-method-integrationresponse-selectionpattern)" : {{String}},
  "[StatusCode](#cfn-apigateway-method-integrationresponse-statuscode)" : {{String}}
}
```

### YAML
<a name="aws-properties-apigateway-method-integrationresponse-syntax.yaml"></a>

```
  [ContentHandling](#cfn-apigateway-method-integrationresponse-contenthandling): {{String}}
  [ResponseParameters](#cfn-apigateway-method-integrationresponse-responseparameters): {{
    {{Key}}: {{Value}}}}
  [ResponseTemplates](#cfn-apigateway-method-integrationresponse-responsetemplates): {{
    {{Key}}: {{Value}}}}
  [SelectionPattern](#cfn-apigateway-method-integrationresponse-selectionpattern): {{String}}
  [StatusCode](#cfn-apigateway-method-integrationresponse-statuscode): {{String}}
```

## Properties
<a name="aws-properties-apigateway-method-integrationresponse-properties"></a>

`ContentHandling`  <a name="cfn-apigateway-method-integrationresponse-contenthandling"></a>
Specifies how to handle response payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the following behaviors:
If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.
*Required*: No
*Type*: String
*Allowed values*: `CONVERT_TO_BINARY | CONVERT_TO_TEXT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResponseParameters`  <a name="cfn-apigateway-method-integrationresponse-responseparameters"></a>
A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of `method.response.header.{name}`, where `name` is a valid and unique header name. The mapped non-static value must match the pattern of `integration.response.header.{name}` or `integration.response.body.{JSON-expression}`, where `name` is a valid and unique response header name and `JSON-expression` is a valid JSON expression without the `$` prefix.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResponseTemplates`  <a name="cfn-apigateway-method-integrationresponse-responsetemplates"></a>
Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectionPattern`  <a name="cfn-apigateway-method-integrationresponse-selectionpattern"></a>
Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the `.+` regex to match error response. However, make sure that the error response does not contain any newline (`\n`) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusCode`  <a name="cfn-apigateway-method-integrationresponse-statuscode"></a>
Specifies the status code that is used to map the integration response to an existing MethodResponse.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-apigateway-method-integrationresponse--seealso"></a>
+ [Method](https://docs.aws.amazon.com/apigateway/latest/api/API_Method.html) in the *Amazon API Gateway REST API Reference*
