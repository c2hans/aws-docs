---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-fieldtomatch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup FieldToMatch
<a name="aws-properties-wafv2-rulegroup-fieldtomatch"></a>

Specifies a web request component to be used in a rule match statement or in a logging configuration.
+ In a rule statement, this is the part of the web request that you want AWS WAF to inspect. Include the single `FieldToMatch` type that you want to inspect, with additional specifications as needed, according to the type. You specify a single request component in `FieldToMatch` for each rule statement that requires it. To inspect more than one component of the web request, create a separate rule statement for each component.

  Example JSON for a `QueryString` field to match:

   ` "FieldToMatch": { "QueryString": {} }`

  Example JSON for a `Method` field to match specification:

   ` "FieldToMatch": { "Method": { "Name": "DELETE" } }`
+ In a logging configuration, this is used in the `RedactedFields` property to specify a field to redact from the logging records. For this use case, note the following:
  + Even though all `FieldToMatch` settings are available, the only valid settings for field redaction are `UriPath`, `QueryString`, `SingleHeader`, and `Method`.
  + In this documentation, the descriptions of the individual fields talk about specifying the web request component to inspect, but for field redaction, you are specifying the component type to redact from the logs.
  + If you have request sampling enabled, the redacted fields configuration for logging has no impact on sampling. You can only exclude fields from request sampling by disabling sampling in the web ACL visibility configuration or by configuring data protection for the web ACL.

## Syntax
<a name="aws-properties-wafv2-rulegroup-fieldtomatch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-fieldtomatch-syntax.json"></a>

```
{
  "[AllQueryArguments](#cfn-wafv2-rulegroup-fieldtomatch-allqueryarguments)" : {{Json}},
  "[Body](#cfn-wafv2-rulegroup-fieldtomatch-body)" : {{Body}},
  "[Cookies](#cfn-wafv2-rulegroup-fieldtomatch-cookies)" : {{Cookies}},
  "[HeaderOrder](#cfn-wafv2-rulegroup-fieldtomatch-headerorder)" : {{HeaderOrder}},
  "[Headers](#cfn-wafv2-rulegroup-fieldtomatch-headers)" : {{Headers}},
  "[JA3Fingerprint](#cfn-wafv2-rulegroup-fieldtomatch-ja3fingerprint)" : {{JA3Fingerprint}},
  "[JA4Fingerprint](#cfn-wafv2-rulegroup-fieldtomatch-ja4fingerprint)" : {{JA4Fingerprint}},
  "[JsonBody](#cfn-wafv2-rulegroup-fieldtomatch-jsonbody)" : {{JsonBody}},
  "[Method](#cfn-wafv2-rulegroup-fieldtomatch-method)" : {{Json}},
  "[QueryString](#cfn-wafv2-rulegroup-fieldtomatch-querystring)" : {{Json}},
  "[SingleHeader](#cfn-wafv2-rulegroup-fieldtomatch-singleheader)" : {{SingleHeader}},
  "[SingleQueryArgument](#cfn-wafv2-rulegroup-fieldtomatch-singlequeryargument)" : {{SingleQueryArgument}},
  "[UriFragment](#cfn-wafv2-rulegroup-fieldtomatch-urifragment)" : {{UriFragment}},
  "[UriPath](#cfn-wafv2-rulegroup-fieldtomatch-uripath)" : {{Json}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-fieldtomatch-syntax.yaml"></a>

```
  [AllQueryArguments](#cfn-wafv2-rulegroup-fieldtomatch-allqueryarguments): {{Json}}
  [Body](#cfn-wafv2-rulegroup-fieldtomatch-body): {{
    Body}}
  [Cookies](#cfn-wafv2-rulegroup-fieldtomatch-cookies): {{
    Cookies}}
  [HeaderOrder](#cfn-wafv2-rulegroup-fieldtomatch-headerorder): {{
    HeaderOrder}}
  [Headers](#cfn-wafv2-rulegroup-fieldtomatch-headers): {{
    Headers}}
  [JA3Fingerprint](#cfn-wafv2-rulegroup-fieldtomatch-ja3fingerprint): {{
    JA3Fingerprint}}
  [JA4Fingerprint](#cfn-wafv2-rulegroup-fieldtomatch-ja4fingerprint): {{
    JA4Fingerprint}}
  [JsonBody](#cfn-wafv2-rulegroup-fieldtomatch-jsonbody): {{
    JsonBody}}
  [Method](#cfn-wafv2-rulegroup-fieldtomatch-method): {{Json}}
  [QueryString](#cfn-wafv2-rulegroup-fieldtomatch-querystring): {{Json}}
  [SingleHeader](#cfn-wafv2-rulegroup-fieldtomatch-singleheader): {{
    SingleHeader}}
  [SingleQueryArgument](#cfn-wafv2-rulegroup-fieldtomatch-singlequeryargument): {{
    SingleQueryArgument}}
  [UriFragment](#cfn-wafv2-rulegroup-fieldtomatch-urifragment): {{
    UriFragment}}
  [UriPath](#cfn-wafv2-rulegroup-fieldtomatch-uripath): {{Json}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-fieldtomatch-properties"></a>

`AllQueryArguments`  <a name="cfn-wafv2-rulegroup-fieldtomatch-allqueryarguments"></a>
Inspect all query arguments.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Body`  <a name="cfn-wafv2-rulegroup-fieldtomatch-body"></a>
Inspect the request body as plain text. The request body immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
AWS WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to AWS WAF for inspection.
+ For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).
+ For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL `AssociationConfig`, for additional processing fees.
+ For AWS Amplify, use the CloudFront limit.
For information about how to handle oversized request bodies, see the `Body` object configuration.
*Required*: No
*Type*: [Body](aws-properties-wafv2-rulegroup-body.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Cookies`  <a name="cfn-wafv2-rulegroup-fieldtomatch-cookies"></a>
Inspect the request cookies. You must configure scope and pattern matching filters in the `Cookies` object, to define the set of cookies and the parts of the cookies that AWS WAF inspects.
Only the first 8 KB (8192 bytes) of a request's cookies and only the first 200 cookies are forwarded to AWS WAF for inspection by the underlying host service. You must configure how to handle any oversize cookie content in the `Cookies` object. AWS WAF applies the pattern matching filters to the cookies that it receives from the underlying host service.
*Required*: No
*Type*: [Cookies](aws-properties-wafv2-rulegroup-cookies.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HeaderOrder`  <a name="cfn-wafv2-rulegroup-fieldtomatch-headerorder"></a>
Inspect a string containing the list of the request's header names, ordered as they appear in the web request that AWS WAF receives for inspection. AWS WAF generates the string and then uses that as the field to match component in its inspection. AWS WAF separates the header names in the string using colons and no added spaces, for example `host:user-agent:accept:authorization:referer`.
*Required*: No
*Type*: [HeaderOrder](aws-properties-wafv2-rulegroup-headerorder.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Headers`  <a name="cfn-wafv2-rulegroup-fieldtomatch-headers"></a>
Inspect the request headers. You must configure scope and pattern matching filters in the `Headers` object, to define the set of headers to and the parts of the headers that AWS WAF inspects.
Only the first 8 KB (8192 bytes) of a request's headers and only the first 200 headers are forwarded to AWS WAF for inspection by the underlying host service. You must configure how to handle any oversize header content in the `Headers` object. AWS WAF applies the pattern matching filters to the headers that it receives from the underlying host service.
*Required*: No
*Type*: [Headers](aws-properties-wafv2-rulegroup-headers.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JA3Fingerprint`  <a name="cfn-wafv2-rulegroup-fieldtomatch-ja3fingerprint"></a>
Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the request's JA3 fingerprint. The JA3 fingerprint is a 32-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. AWS WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation. Almost all web requests include this information.
You can use this choice only with a string match `ByteMatchStatement` with the `PositionalConstraint` set to `EXACTLY`.
You can obtain the JA3 fingerprint for client requests from the web ACL logs. If AWS WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see [Log fields](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) in the *AWS WAF Developer Guide*.
Provide the JA3 fingerprint string from the logs in your string match statement specification, to match with any future requests that have the same TLS configuration.
*Required*: No
*Type*: [JA3Fingerprint](aws-properties-wafv2-rulegroup-ja3fingerprint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JA4Fingerprint`  <a name="cfn-wafv2-rulegroup-fieldtomatch-ja4fingerprint"></a>
Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the request's JA4 fingerprint. The JA4 fingerprint is a 36-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. AWS WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation. Almost all web requests include this information.
You can use this choice only with a string match `ByteMatchStatement` with the `PositionalConstraint` set to `EXACTLY`.
You can obtain the JA4 fingerprint for client requests from the web ACL logs. If AWS WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see [Log fields](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) in the *AWS WAF Developer Guide*.
Provide the JA4 fingerprint string from the logs in your string match statement specification, to match with any future requests that have the same TLS configuration.
*Required*: No
*Type*: [JA4Fingerprint](aws-properties-wafv2-rulegroup-ja4fingerprint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JsonBody`  <a name="cfn-wafv2-rulegroup-fieldtomatch-jsonbody"></a>
Inspect the request body as JSON. The request body immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
AWS WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to AWS WAF for inspection.
+ For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).
+ For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL `AssociationConfig`, for additional processing fees.
+ For AWS Amplify, use the CloudFront limit.
For information about how to handle oversized request bodies, see the `JsonBody` object configuration.
*Required*: No
*Type*: [JsonBody](aws-properties-wafv2-rulegroup-jsonbody.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Method`  <a name="cfn-wafv2-rulegroup-fieldtomatch-method"></a>
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryString`  <a name="cfn-wafv2-rulegroup-fieldtomatch-querystring"></a>
Inspect the query string. This is the part of a URL that appears after a `?` character, if any.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleHeader`  <a name="cfn-wafv2-rulegroup-fieldtomatch-singleheader"></a>
Inspect a single header. Provide the name of the header to inspect, for example, `User-Agent` or `Referer`. This setting isn't case sensitive.
Example JSON: `"SingleHeader": { "Name": "haystack" }`
Alternately, you can filter and inspect all headers with the `Headers``FieldToMatch` setting.
*Required*: No
*Type*: [SingleHeader](aws-properties-wafv2-rulegroup-singleheader.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleQueryArgument`  <a name="cfn-wafv2-rulegroup-fieldtomatch-singlequeryargument"></a>
Inspect a single query argument. Provide the name of the query argument to inspect, such as *UserName* or *SalesRegion*. The name can be up to 30 characters long and isn't case sensitive.
Example JSON: `"SingleQueryArgument": { "Name": "myArgument" }`
*Required*: No
*Type*: [SingleQueryArgument](aws-properties-wafv2-rulegroup-singlequeryargument.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UriFragment`  <a name="cfn-wafv2-rulegroup-fieldtomatch-urifragment"></a>
Inspect fragments of the request URI. You must configure scope and pattern matching filters in the `UriFragment` object, to define the fragment of a URI that AWS WAF inspects.
Only the first 8 KB (8192 bytes) of a request's URI fragments and only the first 200 URI fragments are forwarded to AWS WAF for inspection by the underlying host service. You must configure how to handle any oversize URI fragment content in the `UriFragment` object. AWS WAF applies the pattern matching filters to the cookies that it receives from the underlying host service.
*Required*: No
*Type*: [UriFragment](aws-properties-wafv2-rulegroup-urifragment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UriPath`  <a name="cfn-wafv2-rulegroup-fieldtomatch-uripath"></a>
Inspect the request URI path. This is the part of the web request that identifies a resource, for example, `/images/daily-ad.jpg`.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-wafv2-rulegroup-fieldtomatch--examples"></a>

**Topics**
+ [Set the field to match to `QueryString`](#aws-properties-wafv2-rulegroup-fieldtomatch--examples--Set_the_field_to_match_to_QueryString)
+ [Set the field to match to `Method`](#aws-properties-wafv2-rulegroup-fieldtomatch--examples--Set_the_field_to_match_to_Method)

### Set the field to match to `QueryString`
<a name="aws-properties-wafv2-rulegroup-fieldtomatch--examples--Set_the_field_to_match_to_QueryString"></a>

The following shows an example field to match specification for a setting that doesn't requires additional configuration.

#### YAML
<a name="aws-properties-wafv2-rulegroup-fieldtomatch--examples--Set_the_field_to_match_to_QueryString--yaml"></a>

```
FieldToMatch:
  QueryString: {}
```

#### JSON
<a name="aws-properties-wafv2-rulegroup-fieldtomatch--examples--Set_the_field_to_match_to_QueryString--json"></a>

```
"FieldToMatch":
    {
         "QueryString": {}
    }
```

### Set the field to match to `Method`
<a name="aws-properties-wafv2-rulegroup-fieldtomatch--examples--Set_the_field_to_match_to_Method"></a>

The following shows an example field to match specification for a setting that has additional configuration requirements.

#### YAML
<a name="aws-properties-wafv2-rulegroup-fieldtomatch--examples--Set_the_field_to_match_to_Method--yaml"></a>

```
FieldToMatch:
  Method:
     Name: DELETE
```

#### JSON
<a name="aws-properties-wafv2-rulegroup-fieldtomatch--examples--Set_the_field_to_match_to_Method--json"></a>

```
"FieldToMatch":
{
    "Method":
    {
         "Name": "DELETE"
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
