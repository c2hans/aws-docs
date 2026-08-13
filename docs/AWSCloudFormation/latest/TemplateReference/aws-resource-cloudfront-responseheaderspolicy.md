---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-responseheaderspolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ResponseHeadersPolicy
<a name="aws-resource-cloudfront-responseheaderspolicy"></a>

A response headers policy.

A response headers policy contains information about a set of HTTP response headers.

After you create a response headers policy, you can use its ID to attach it to one or more cache behaviors in a CloudFront distribution. When it's attached to a cache behavior, the response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to requests that match the cache behavior. CloudFront adds or removes response headers according to the configuration of the response headers policy.

For more information, see [Adding or removing HTTP headers in CloudFront responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html) in the *Amazon CloudFront Developer Guide*.

## Syntax
<a name="aws-resource-cloudfront-responseheaderspolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-responseheaderspolicy-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::ResponseHeadersPolicy",
  "Properties" : {
      "[ResponseHeadersPolicyConfig](#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig)" : {{ResponseHeadersPolicyConfig}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-responseheaderspolicy-syntax.yaml"></a>

```
Type: AWS::CloudFront::ResponseHeadersPolicy
Properties:
  [ResponseHeadersPolicyConfig](#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig): {{
    ResponseHeadersPolicyConfig}}
```

## Properties
<a name="aws-resource-cloudfront-responseheaderspolicy-properties"></a>

`ResponseHeadersPolicyConfig`  <a name="cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig"></a>
A response headers policy configuration.
*Required*: Yes
*Type*: [ResponseHeadersPolicyConfig](aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-responseheaderspolicy-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-responseheaderspolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the response headers policy ID. For example: `57f99797-3b20-4e1b-a728-27972a74082a`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudfront-responseheaderspolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudfront-responseheaderspolicy-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier for the response headers policy. For example: `57f99797-3b20-4e1b-a728-27972a74082a`.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The date and time when the response headers policy was last modified.

## Examples
<a name="aws-resource-cloudfront-responseheaderspolicy--examples"></a>

### Create a response headers policy
<a name="aws-resource-cloudfront-responseheaderspolicy--examples--Create_a_response_headers_policy"></a>

The following example creates a response headers policy.

#### JSON
<a name="aws-resource-cloudfront-responseheaderspolicy--examples--Create_a_response_headers_policy--json"></a>

```
{
  "Resources": {
    "MyResponseHeadersPolicy": {
      "Type": "AWS::CloudFront::ResponseHeadersPolicy",
      "Properties": {
        "ResponseHeadersPolicyConfig": {
          "Name": {
            "Fn::Join": [
              "-",
              [
                "canary-response-header-policy",
                {
                  "Fn::Select": [
                    0,
                    {
                      "Fn::Split": [
                        "-",
                        {
                          "Fn::Select": [
                            2,
                            {
                              "Fn::Split": [
                                "/",
                                {
                                  "Ref": "AWS::StackId"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            ]
          },
          "Comment": "Sample Comment",
          "CorsConfig": {
            "AccessControlAllowCredentials": true,
            "AccessControlAllowHeaders": {
              "Items": ["Header1"]
            },
            "AccessControlAllowMethods": {
              "Items": ["GET", "POST"]
            },
            "AccessControlAllowOrigins": {
              "Items": ["example1.com", "example2.com", "example3.com"]
            },
            "AccessControlExposeHeaders": {
              "Items": [
                "ExposeHeader1",
                "ExposeHeader2",
                "ExposeHeader3",
                "ExposeHeader4"
              ]
            },
            "AccessControlMaxAgeSec": 1200,
            "OriginOverride": true
          },
          "CustomHeadersConfig": {
            "Items": [
              {
                "Header": "HeaderX",
                "Override": true,
                "Value": "ValueX"
              },
              {
                "Header": "HeaderY",
                "Override": true,
                "Value": "ValueY"
              }
            ]
          },
          "RemoveHeadersConfig": {
            "Items": [
              {
                "Header": "RemoveHeaderX"
              },
              {
                "Header": "RemoveHeaderY"
              }
            ]
          },
          "SecurityHeadersConfig": {
            "ContentSecurityPolicy": {
              "ContentSecurityPolicy": "MyPolicy",
              "Override": true
            },
            "ContentTypeOptions": {
              "Override": true
            },
            "FrameOptions": {
              "FrameOption": "SAMEORIGIN",
              "Override": true
            },
            "ReferrerPolicy": {
              "ReferrerPolicy": "origin-when-cross-origin",
              "Override": true
            },
            "StrictTransportSecurity": {
              "AccessControlMaxAgeSec": 2400,
              "IncludeSubdomains": true,
              "Override": true,
              "Preload": true
            },
            "XSSProtection": {
              "ModeBlock": true,
              "Override": true,
              "Protection": true
            }
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cloudfront-responseheaderspolicy--examples--Create_a_response_headers_policy--yaml"></a>

```
Resources:
  ABCDE1FGHI:
  MyWaitConditionHandle:
    Type: AWS::CloudFormation::WaitConditionHandle
  MyResponseHeadersPolicy:
    Type: AWS::CloudFront::ResponseHeadersPolicy
    Properties:
      ResponseHeadersPolicyConfig:
        Name: !Join
          - "-"
          - - "canary-response-header-policy"
            - !Select
              - 0
              - !Split
                - "-"
                - !Select
                  - 2
                  - !Split
                    - "/"
                    - !Ref "AWS::StackId"
        Comment: "Sample Comment"
        CorsConfig:
          AccessControlAllowCredentials: true
          AccessControlAllowHeaders:
            Items:
              - "Header1"
          AccessControlAllowMethods:
            Items:
              - "GET"
              - "POST"
          AccessControlAllowOrigins:
            Items:
              - "example1.com"
              - "example2.com"
              - "example3.com"
          AccessControlExposeHeaders:
            Items:
              - "ExposeHeader1"
              - "ExposeHeader2"
              - "ExposeHeader3"
              - "ExposeHeader4"
          AccessControlMaxAgeSec: 1200
          OriginOverride: true
        CustomHeadersConfig:
          Items:
            - Header: "HeaderX"
              Override: true
              Value: "ValueX"
            - Header: "HeaderY"
              Override: true
              Value: "ValueY"
        RemoveHeadersConfig:
          Items:
            - Header: "RemoveHeaderX"
            - Header: "RemoveHeaderY"
        SecurityHeadersConfig:
          ContentSecurityPolicy:
            ContentSecurityPolicy: "MyPolicy"
            Override: true
          ContentTypeOptions:
            Override: true
          FrameOptions:
            FrameOption: "SAMEORIGIN"
            Override: true
          ReferrerPolicy:
            ReferrerPolicy: "origin-when-cross-origin"
            Override: true
          StrictTransportSecurity:
            AccessControlMaxAgeSec: 2400
            IncludeSubdomains: true
            Override: true
            Preload: true
          XSSProtection:
            ModeBlock: true
            Override: true
            Protection: true
  RHPolicyWaiterCustomResource:
    Type: AWS::CloudFormation::CustomResource
    DeletionPolicy: Retain
    Properties:
      ServiceToken: !ImportValue RHPolicyLambdaWaiter
      WaitSeconds: 300
```
