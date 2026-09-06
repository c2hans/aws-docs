---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule HttpHeaderConfig
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig"></a>

Information about an HTTP header condition.

There is a set of standard HTTP header fields. You can also define custom HTTP header fields.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig-syntax.json"></a>

```
{
  "[HttpHeaderName](#cfn-elasticloadbalancingv2-listenerrule-httpheaderconfig-httpheadername)" : {{String}},
  "[RegexValues](#cfn-elasticloadbalancingv2-listenerrule-httpheaderconfig-regexvalues)" : {{[ String, ... ]}},
  "[Values](#cfn-elasticloadbalancingv2-listenerrule-httpheaderconfig-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig-syntax.yaml"></a>

```
  [HttpHeaderName](#cfn-elasticloadbalancingv2-listenerrule-httpheaderconfig-httpheadername): {{String}}
  [RegexValues](#cfn-elasticloadbalancingv2-listenerrule-httpheaderconfig-regexvalues): {{
    - String}}
  [Values](#cfn-elasticloadbalancingv2-listenerrule-httpheaderconfig-values): {{
    - String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig-properties"></a>

`HttpHeaderName`  <a name="cfn-elasticloadbalancingv2-listenerrule-httpheaderconfig-httpheadername"></a>
The name of the HTTP header field. The maximum size is 40 characters. The header name is case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not supported.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegexValues`  <a name="cfn-elasticloadbalancingv2-listenerrule-httpheaderconfig-regexvalues"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-elasticloadbalancingv2-listenerrule-httpheaderconfig-values"></a>
The strings to compare against the value of the HTTP header. The maximum length of each string is 128 characters. The comparison strings are case insensitive. The following wildcard characters are supported: \* (matches 0 or more characters) and ? (matches exactly 1 character).
If the same header appears multiple times in the request, we search them in order until a match is found.
If you specify multiple strings, the condition is satisfied if one of the strings matches the value of the HTTP header. To require that all of the strings are a match, create one condition per string.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig--examples"></a>

###
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig--examples--"></a>

This example creates a listener rule with an action that redirects requests with the specified values for the `User-Agent` header to the mobile version of the website.

#### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig--examples----yaml"></a>

```
myHttpHeaderListenerRule:
   Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
   Properties:
     ListenerArn: !Ref myListener
     Priority: 30
     Conditions:
       - Field: http-header
         HttpHeaderConfig:
           HttpHeaderName: User-Agent
           Values:
             - "*Mobile*"
             - "*Android*"
             - "*iPhone*"
     Actions:
       - Type: redirect
         RedirectConfig:
           Host: m.example.com
           StatusCode: HTTP_302
```

#### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig--examples----json"></a>

```
{
    "myHttpHeaderListenerRule": {
        "Type": "AWS::ElasticLoadBalancingV2::ListenerRule",
        "Properties": {
            "ListenerArn": {
                "Ref": "myListener"
            },
            "Priority": 30,
            "Conditions": [
                {
                    "Field": "http-header",
                    "HttpHeaderConfig": {
                        "HttpHeaderName": "User-Agent",
                        "Values": [
                            "*Mobile*",
                            "*Android*",
                            "*iPhone*"
                        ]
                    }
                }
            ],
            "Actions": [
                {
                    "Type": "redirect",
                    "RedirectConfig": {
                        "Host": "m.example.com",
                        "StatusCode": "HTTP_302"
                    }
                }
            ]
        }
    }
}
```
