---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediastore-container-corsrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaStore::Container CorsRule
<a name="aws-properties-mediastore-container-corsrule"></a>

A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.

## Syntax
<a name="aws-properties-mediastore-container-corsrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediastore-container-corsrule-syntax.json"></a>

```
{
  "[AllowedHeaders](#cfn-mediastore-container-corsrule-allowedheaders)" : {{[ String, ... ]}},
  "[AllowedMethods](#cfn-mediastore-container-corsrule-allowedmethods)" : {{[ String, ... ]}},
  "[AllowedOrigins](#cfn-mediastore-container-corsrule-allowedorigins)" : {{[ String, ... ]}},
  "[ExposeHeaders](#cfn-mediastore-container-corsrule-exposeheaders)" : {{[ String, ... ]}},
  "[MaxAgeSeconds](#cfn-mediastore-container-corsrule-maxageseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediastore-container-corsrule-syntax.yaml"></a>

```
  [AllowedHeaders](#cfn-mediastore-container-corsrule-allowedheaders): {{
    - String}}
  [AllowedMethods](#cfn-mediastore-container-corsrule-allowedmethods): {{
    - String}}
  [AllowedOrigins](#cfn-mediastore-container-corsrule-allowedorigins): {{
    - String}}
  [ExposeHeaders](#cfn-mediastore-container-corsrule-exposeheaders): {{
    - String}}
  [MaxAgeSeconds](#cfn-mediastore-container-corsrule-maxageseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediastore-container-corsrule-properties"></a>

`AllowedHeaders`  <a name="cfn-mediastore-container-corsrule-allowedheaders"></a>
Specifies which headers are allowed in a preflight `OPTIONS` request through the `Access-Control-Request-Headers` header. Each header name that is specified in `Access-Control-Request-Headers` must have a corresponding entry in the rule. Only the headers that were requested are sent back.
This element can contain only one wildcard character (\*).
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedMethods`  <a name="cfn-mediastore-container-corsrule-allowedmethods"></a>
Identifies an HTTP method that the origin that is specified in the rule is allowed to execute.
Each CORS rule must contain at least one `AllowedMethods` and one `AllowedOrigins` element.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedOrigins`  <a name="cfn-mediastore-container-corsrule-allowedorigins"></a>
One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript `XMLHttpRequest` object).
Each CORS rule must have at least one `AllowedOrigins` element. The string value can include only one wildcard character (\*), for example, http://\*.example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExposeHeaders`  <a name="cfn-mediastore-container-corsrule-exposeheaders"></a>
One or more headers in the response that you want users to be able to access from their applications (for example, from a JavaScript `XMLHttpRequest` object).
This element is optional for each rule.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxAgeSeconds`  <a name="cfn-mediastore-container-corsrule-maxageseconds"></a>
The time in seconds that your browser caches the preflight response for the specified resource.
A CORS rule can have only one `MaxAgeSeconds` element.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
