---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL RequestBodyAssociatedResourceTypeConfig

Customizes the maximum size of the request body that your protected Application Load Balancer, CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access resources forward to AWS WAF for inspection. The default size is 8 KB (8,192 bytes) for Application Load Balancer and 16 KB (16,384 bytes) for the other resource types. You can change the setting for any of the available resource types.

**Note**
You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

Example JSON: ` { "API_GATEWAY": "KB_48", "APP_RUNNER_SERVICE": "KB_32", "APPLICATION_LOAD_BALANCER": "KB_16" }`

For AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).

This is used in the `AssociationConfig` of the web ACL.

## Syntax
<a name="aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig-syntax.json"></a>

```json
{
  "[DefaultSizeInspectionLimit](#cfn-wafv2-webacl-requestbodyassociatedresourcetypeconfig-defaultsizeinspectionlimit)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig-syntax.yaml"></a>

```yaml
  [DefaultSizeInspectionLimit](#cfn-wafv2-webacl-requestbodyassociatedresourcetypeconfig-defaultsizeinspectionlimit): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig-properties"></a>

`DefaultSizeInspectionLimit`  <a name="cfn-wafv2-webacl-requestbodyassociatedresourcetypeconfig-defaultsizeinspectionlimit"></a>
Specifies the maximum size of the web request body component that an associated Application Load Balancer, CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resource should send to AWS WAF for inspection. This applies to statements in the web ACL that inspect the body or JSON body.
You can specify `KB_8` only for Application Load Balancer, with the `APPLICATION_LOAD_BALANCER` resource type.
Default: `8 KB (8,192 bytes)` for Application Load Balancer and `16 KB (16,384 bytes)` for the other resource types
*Required*: Yes
*Type*: String
*Allowed values*: `KB_8 | KB_16 | KB_32 | KB_48 | KB_64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
