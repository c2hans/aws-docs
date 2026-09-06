---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-function-httprequestconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Function HttpRequestConfiguration
<a name="aws-properties-mediatailor-function-httprequestconfiguration"></a>

The configuration for an `HTTP_REQUEST` function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions for the request. For more information, see [HTTP\_REQUEST](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types-http-request.html) in the *MediaTailor User Guide*.

## Syntax
<a name="aws-properties-mediatailor-function-httprequestconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-function-httprequestconfiguration-syntax.json"></a>

```
{
  "[Body](#cfn-mediatailor-function-httprequestconfiguration-body)" : {{String}},
  "[Headers](#cfn-mediatailor-function-httprequestconfiguration-headers)" : {{{{{Key}}: {{Value}}, ...}}},
  "[MethodType](#cfn-mediatailor-function-httprequestconfiguration-methodtype)" : {{String}},
  "[Output](#cfn-mediatailor-function-httprequestconfiguration-output)" : {{{{{Key}}: {{Value}}, ...}}},
  "[RequestTimeoutMilliseconds](#cfn-mediatailor-function-httprequestconfiguration-requesttimeoutmilliseconds)" : {{Integer}},
  "[Runtime](#cfn-mediatailor-function-httprequestconfiguration-runtime)" : {{String}},
  "[Url](#cfn-mediatailor-function-httprequestconfiguration-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-function-httprequestconfiguration-syntax.yaml"></a>

```
  [Body](#cfn-mediatailor-function-httprequestconfiguration-body): {{String}}
  [Headers](#cfn-mediatailor-function-httprequestconfiguration-headers): {{
    {{Key}}: {{Value}}}}
  [MethodType](#cfn-mediatailor-function-httprequestconfiguration-methodtype): {{String}}
  [Output](#cfn-mediatailor-function-httprequestconfiguration-output): {{
    {{Key}}: {{Value}}}}
  [RequestTimeoutMilliseconds](#cfn-mediatailor-function-httprequestconfiguration-requesttimeoutmilliseconds): {{Integer}}
  [Runtime](#cfn-mediatailor-function-httprequestconfiguration-runtime): {{String}}
  [Url](#cfn-mediatailor-function-httprequestconfiguration-url): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-function-httprequestconfiguration-properties"></a>

`Body`  <a name="cfn-mediatailor-function-httprequestconfiguration-body"></a>
An expression that evaluates to the request body. Used with `POST` requests. The maximum size after evaluation is 64 KB.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Headers`  <a name="cfn-mediatailor-function-httprequestconfiguration-headers"></a>
A map of HTTP header names to expression values. MediaTailor evaluates each header value expression at runtime and includes the result in the outbound HTTP request. Maximum 50 headers.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MethodType`  <a name="cfn-mediatailor-function-httprequestconfiguration-methodtype"></a>
The HTTP method for the request. Valid values: `GET` and `POST`.
*Required*: Yes
*Type*: String
*Allowed values*: `GET | POST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Output`  <a name="cfn-mediatailor-function-httprequestconfiguration-output"></a>
A map of output bindings. Each key is a namespaced output path (such as `player_params.device_type` or `temp.identity`), and each value is an expression that MediaTailor evaluates at runtime. Output expressions in an `HTTP_REQUEST` function can reference the `response` object returned by the HTTP call. For more information about expression syntax, see [JSONata expression reference](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-jsonata.html) in the *MediaTailor User Guide*.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequestTimeoutMilliseconds`  <a name="cfn-mediatailor-function-httprequestconfiguration-requesttimeoutmilliseconds"></a>
The maximum time, in milliseconds, that MediaTailor waits for a response from the external service. If the call exceeds this timeout, MediaTailor sets the response status code to `null` and proceeds with output expression evaluation. Valid values: `100` to `2000`.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Runtime`  <a name="cfn-mediatailor-function-httprequestconfiguration-runtime"></a>
The expression language used to evaluate expressions in the function configuration. Set this to `JSONata`.
*Required*: Yes
*Type*: String
*Allowed values*: `JSONATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-mediatailor-function-httprequestconfiguration-url"></a>
An expression that evaluates to the request URL. Use `{%...%}` delimiters for dynamic expressions. The maximum length after evaluation is 2,048 characters.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
