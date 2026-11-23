---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distributiontenant-domainresult.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::DistributionTenant DomainResult

The details about the domain result.

## Syntax
<a name="aws-properties-cloudfront-distributiontenant-domainresult-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distributiontenant-domainresult-syntax.json"></a>

```json
{
  "[Domain](#cfn-cloudfront-distributiontenant-domainresult-domain)" : {{String}},
  "[ServeOn](#cfn-cloudfront-distributiontenant-domainresult-serveon)" : {{String}},
  "[Status](#cfn-cloudfront-distributiontenant-domainresult-status)" : {{String}},
  "[StatusReason](#cfn-cloudfront-distributiontenant-domainresult-statusreason)" : {{String}},
  "[StatusReasonCode](#cfn-cloudfront-distributiontenant-domainresult-statusreasoncode)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distributiontenant-domainresult-syntax.yaml"></a>

```yaml
  [Domain](#cfn-cloudfront-distributiontenant-domainresult-domain): {{String}}
  [ServeOn](#cfn-cloudfront-distributiontenant-domainresult-serveon): {{String}}
  [Status](#cfn-cloudfront-distributiontenant-domainresult-status): {{String}}
  [StatusReason](#cfn-cloudfront-distributiontenant-domainresult-statusreason): {{String}}
  [StatusReasonCode](#cfn-cloudfront-distributiontenant-domainresult-statusreasoncode): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distributiontenant-domainresult-properties"></a>

`Domain`  <a name="cfn-cloudfront-distributiontenant-domainresult-domain"></a>
The specified domain.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServeOn`  <a name="cfn-cloudfront-distributiontenant-domainresult-serveon"></a>
Specifies which requests for this domain CloudFront routes to the distribution tenant. Valid values are:
+ `any` – CloudFront routes requests for this domain to the distribution tenant regardless of the IP address that they arrive on. This is the default if you don't specify a value.
+ `anycast-ip-list-only` – CloudFront routes requests for this domain to the distribution tenant only when they arrive on the Anycast static IPs of the distribution tenant's connection group. CloudFront treats requests that arrive on other IP addresses as requests for an unknown domain.
*Required*: No
*Type*: String
*Allowed values*: `any | anycast-ip-list-only`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-cloudfront-distributiontenant-domainresult-status"></a>
Whether the domain is active or inactive.
*Required*: No
*Type*: String
*Allowed values*: `active | inactive`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusReason`  <a name="cfn-cloudfront-distributiontenant-domainresult-statusreason"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusReasonCode`  <a name="cfn-cloudfront-distributiontenant-domainresult-statusreasoncode"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
