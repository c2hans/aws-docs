---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pricingplanmanager-subscription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PricingPlanManager::Subscription
<a name="aws-resource-pricingplanmanager-subscription"></a>

Creates a flat-rate pricing plan subscription that applies a fixed monthly rate to the associated resources instead of usage-based charges. Currently, `CloudFront` is the only supported plan family.

The service creates paid-tier subscriptions in `PENDING_APPROVAL` status. Billing does not start until you approve the subscription through a separate `ApprovePaidSubscription` API call — AWS CloudFormation does not approve the subscription automatically. The service activates free-tier subscriptions immediately.

When you delete an active subscription, the cancellation is scheduled for the end of the current billing period. When you delete a subscription in `PENDING_APPROVAL` status, the service removes it immediately with no further charges.

You can update the associated resources through a stack update, but you cannot change the plan tier or usage level. To change the tier or usage level, see [Common workflows](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/getting-started-pricingplanmanager-api.html#common-workflows) in the *AWS PricingPlanManager User Guide*, then update your template to match.

## Syntax
<a name="aws-resource-pricingplanmanager-subscription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pricingplanmanager-subscription-syntax.json"></a>

```
{
  "Type" : "AWS::PricingPlanManager::Subscription",
  "Properties" : {
      "[PlanFamily](#cfn-pricingplanmanager-subscription-planfamily)" : {{String}},
      "[PlanTier](#cfn-pricingplanmanager-subscription-plantier)" : {{String}},
      "[ResourceArns](#cfn-pricingplanmanager-subscription-resourcearns)" : {{[ String, ... ]}},
      "[UsageLevel](#cfn-pricingplanmanager-subscription-usagelevel)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-pricingplanmanager-subscription-syntax.yaml"></a>

```
Type: AWS::PricingPlanManager::Subscription
Properties:
  [PlanFamily](#cfn-pricingplanmanager-subscription-planfamily): {{String}}
  [PlanTier](#cfn-pricingplanmanager-subscription-plantier): {{String}}
  [ResourceArns](#cfn-pricingplanmanager-subscription-resourcearns): {{
    - String}}
  [UsageLevel](#cfn-pricingplanmanager-subscription-usagelevel): {{String}}
```

## Properties
<a name="aws-resource-pricingplanmanager-subscription-properties"></a>

`PlanFamily`  <a name="cfn-pricingplanmanager-subscription-planfamily"></a>
The pricing plan family. Use `CloudFront`.
*Required*: Yes
*Type*: String
*Allowed values*: `CloudFront`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlanTier`  <a name="cfn-pricingplanmanager-subscription-plantier"></a>
The plan tier. Valid values:
 `FREE`
No cost. The service activates free-tier subscriptions immediately.
 `PRO`
Paid tier billed at a flat monthly rate.
 `BUSINESS`
Paid tier billed at a flat monthly rate.
 `PREMIUM`
Paid tier billed at a flat monthly rate. Supports additional usage levels.
You cannot change the plan tier through a stack update. To change the tier, see [Common workflows](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/getting-started-pricingplanmanager-api.html#common-workflows) in the *AWS PricingPlanManager User Guide*, then update your template to match the new tier.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArns`  <a name="cfn-pricingplanmanager-subscription-resourcearns"></a>
The ARNs of resources to associate with the subscription. For Amazon CloudFront plans, you must include a CloudFront distribution ARN and an AWS WAF web ACL ARN. You can optionally include an Amazon Route 53 hosted zone ARN or a CloudFront KeyValueStore ARN.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsageLevel`  <a name="cfn-pricingplanmanager-subscription-usagelevel"></a>
The usage level within the plan tier. Valid values depend on the plan family and tier. For Amazon CloudFront Premium plans, valid values are:
 `DEFAULT`
The base usage level.
`CF_PREMIUM_L2` through `CF_PREMIUM_L6`
Increasing usage levels, each supporting higher traffic volumes.
You cannot change the usage level through a stack update. To change the usage level, see [Common workflows](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/getting-started-pricingplanmanager-api.html#common-workflows) in the *AWS PricingPlanManager User Guide*, then update your template to match the new usage level.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | CF_PREMIUM_L2 | CF_PREMIUM_L3 | CF_PREMIUM_L4 | CF_PREMIUM_L5 | CF_PREMIUM_L6 | CF_PREMIUM_L7`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-pricingplanmanager-subscription-return-values"></a>

### Ref
<a name="aws-resource-pricingplanmanager-subscription-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the subscription ARN. For example:

 `arn:aws:pricingplanmanager::111122223333:subscription:sub_35GHLKfG8y9CsMkHV8EXAMPLE`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-pricingplanmanager-subscription-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-pricingplanmanager-subscription-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the subscription. For example:
 `arn:aws:pricingplanmanager::111122223333:subscription:sub_35GHLKfG8y9CsMkHV8EXAMPLE`

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the subscription was created, in ISO 8601 format.

`CurrentPlanTier`  <a name="CurrentPlanTier-fn::getatt"></a>
The plan tier currently active on the subscription. This value diverges from `PlanTier` when a downgrade is scheduled — `CurrentPlanTier` reports the tier you are being billed for, while `PlanTier` reflects the requested tier.

`Status`  <a name="Status-fn::getatt"></a>
The status of the subscription. Valid values:
 `ACTIVE`
The subscription is active and the pricing plan applies to the associated resources. Billing is at the subscription's plan rate.
 `PENDING_APPROVAL`
The subscription is waiting for approval via `ApprovePaidSubscription`. The plan does not apply to the associated resources — usage is charged at pay-as-you-go rates until you approve the subscription. The subscription does not expire while pending approval.
 `SYNC_IN_PROGRESS`
The service is applying a subscription change to the associated resources. This typically takes 2–5 minutes. You cannot modify the subscription while it is in this state.
 `FAILED`
The subscription operation failed. Review the `StatusReason` attribute for details. Cancel the failed subscription and create a new one.

`StatusReason`  <a name="StatusReason-fn::getatt"></a>
A human-readable explanation of why the subscription failed. Populated only when `Status` is `FAILED`. Empty for all other statuses.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the subscription was last modified, in ISO 8601 format.

## Examples
<a name="aws-resource-pricingplanmanager-subscription--examples"></a>

**Topics**
+ [Associate existing resources with a free-tier subscription](#aws-resource-pricingplanmanager-subscription--examples--Associate_existing_resources_with_a_free-tier_subscription)
+ [Create a subscription together with its associated resources](#aws-resource-pricingplanmanager-subscription--examples--Create_a_subscription_together_with_its_associated_resources)
+ [Associate a Route 53 hosted zone with a subscription](#aws-resource-pricingplanmanager-subscription--examples--Associate_a_Route_53_hosted_zone_with_a_subscription)
+ [Add a CloudFront KeyValueStore to a paid-tier subscription](#aws-resource-pricingplanmanager-subscription--examples--Add_a_CloudFront_KeyValueStore_to_a_paid-tier_subscription)

### Associate existing resources with a free-tier subscription
<a name="aws-resource-pricingplanmanager-subscription--examples--Associate_existing_resources_with_a_free-tier_subscription"></a>

The following example creates a `FREE`-tier CloudFront subscription that covers an existing CloudFront distribution and an existing WAFv2 web ACL, referenced directly by ARN. Replace the account ID, distribution ID, and web ACL name and ID with the values for your own resources. The web ACL ARN must be a `CLOUDFRONT`-scope (`global`) WAFv2 ARN in `us-east-1`.

#### YAML
<a name="aws-resource-pricingplanmanager-subscription--examples--Associate_existing_resources_with_a_free-tier_subscription--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'

Resources:
  Subscription:
    Type: AWS::PricingPlanManager::Subscription
    Properties:
      PlanFamily: CloudFront
      PlanTier: FREE
      UsageLevel: DEFAULT
      ResourceArns:
        - arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE
        - arn:aws:wafv2:us-east-1:123456789012:global/webacl/example-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

### Create a subscription together with its associated resources
<a name="aws-resource-pricingplanmanager-subscription--examples--Create_a_subscription_together_with_its_associated_resources"></a>

The following example provisions a WAFv2 web ACL and a CloudFront distribution, then creates a `FREE`-tier subscription that references both. Because the subscription references the other resources, AWS CloudFormation creates it last and deletes it first. Deploy this stack in `us-east-1`, because `CLOUDFRONT`-scope web ACLs exist only in that Region.

#### YAML
<a name="aws-resource-pricingplanmanager-subscription--examples--Create_a_subscription_together_with_its_associated_resources--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'

Resources:
  SampleWebAcl:
    Type: AWS::WAFv2::WebACL
    Properties:
      Name: !Sub 'ppm-sample-${AWS::StackName}'
      Scope: CLOUDFRONT
      DefaultAction:
        Allow: {}
      VisibilityConfig:
        SampledRequestsEnabled: false
        CloudWatchMetricsEnabled: false
        MetricName: ppmSample

  SampleDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Comment: !Sub 'PricingPlanManager sample - ${AWS::StackName}'
        Enabled: true
        # A WAFv2 web ACL is associated by ARN; the WAF Classic ID form is rejected.
        WebACLId: !GetAtt SampleWebAcl.Arn
        Origins:
          - Id: sample-origin
            DomainName: example.com
            CustomOriginConfig:
              OriginProtocolPolicy: http-only
        DefaultCacheBehavior:
          TargetOriginId: sample-origin
          ViewerProtocolPolicy: redirect-to-https
          # Managed CachingOptimized cache policy.
          CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6

  # The references below make this depend on both resources, so CloudFormation creates
  # the subscription last and removes it first.
  SampleSubscription:
    Type: AWS::PricingPlanManager::Subscription
    Properties:
      PlanFamily: CloudFront
      PlanTier: FREE
      UsageLevel: DEFAULT
      ResourceArns:
        - !Sub 'arn:${AWS::Partition}:cloudfront::${AWS::AccountId}:distribution/${SampleDistribution}'
        - !GetAtt SampleWebAcl.Arn
```

### Associate a Route 53 hosted zone with a subscription
<a name="aws-resource-pricingplanmanager-subscription--examples--Associate_a_Route_53_hosted_zone_with_a_subscription"></a>

The following example extends the previous template with a Route 53 hosted zone and adds its ARN to the subscription's `ResourceArns`. A subscription can cover a distribution, a web ACL, and a hosted zone together.

#### YAML
<a name="aws-resource-pricingplanmanager-subscription--examples--Associate_a_Route_53_hosted_zone_with_a_subscription--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'

Resources:
  SampleWebAcl:
    Type: AWS::WAFv2::WebACL
    Properties:
      Name: !Sub 'ppm-sample-${AWS::StackName}'
      Scope: CLOUDFRONT
      DefaultAction:
        Allow: {}
      VisibilityConfig:
        SampledRequestsEnabled: false
        CloudWatchMetricsEnabled: false
        MetricName: ppmSample

  SampleDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Comment: !Sub 'PricingPlanManager sample - ${AWS::StackName}'
        Enabled: true
        # A WAFv2 web ACL is associated by ARN; the WAF Classic ID form is rejected.
        WebACLId: !GetAtt SampleWebAcl.Arn
        Origins:
          - Id: sample-origin
            DomainName: example.com
            CustomOriginConfig:
              OriginProtocolPolicy: http-only
        DefaultCacheBehavior:
          TargetOriginId: sample-origin
          ViewerProtocolPolicy: redirect-to-https
          # Managed CachingOptimized cache policy.
          CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6

  SampleHostedZone:
    Type: AWS::Route53::HostedZone
    Properties:
      Name: ppm-sample.example.com.

  # The references below make this depend on all three resources, so CloudFormation
  # creates the subscription last and removes it first.
  SampleSubscription:
    Type: AWS::PricingPlanManager::Subscription
    Properties:
      PlanFamily: CloudFront
      PlanTier: FREE
      UsageLevel: DEFAULT
      ResourceArns:
        - !Sub 'arn:${AWS::Partition}:cloudfront::${AWS::AccountId}:distribution/${SampleDistribution}'
        - !GetAtt SampleWebAcl.Arn
        - !Sub 'arn:${AWS::Partition}:route53:::hostedzone/${SampleHostedZone}'
```

### Add a CloudFront KeyValueStore to a paid-tier subscription
<a name="aws-resource-pricingplanmanager-subscription--examples--Add_a_CloudFront_KeyValueStore_to_a_paid-tier_subscription"></a>

A subscription associates exactly one distribution and one web ACL. A CloudFront KeyValueStore is optional, limited to one, and requires the `PRO` tier or higher. Paid tiers start in `PENDING_APPROVAL` and must be approved out of band before billing begins; AWS CloudFormation never approves them.

#### YAML
<a name="aws-resource-pricingplanmanager-subscription--examples--Add_a_CloudFront_KeyValueStore_to_a_paid-tier_subscription--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'

Resources:
  SampleWebAcl:
    Type: AWS::WAFv2::WebACL
    Properties:
      Name: !Sub 'ppm-sample-${AWS::StackName}'
      Scope: CLOUDFRONT
      DefaultAction:
        Allow: {}
      VisibilityConfig:
        SampledRequestsEnabled: false
        CloudWatchMetricsEnabled: false
        MetricName: ppmSample

  SampleDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Comment: !Sub 'PricingPlanManager sample - ${AWS::StackName}'
        Enabled: true
        # A WAFv2 web ACL is associated by ARN; the WAF Classic ID form is rejected.
        WebACLId: !GetAtt SampleWebAcl.Arn
        Origins:
          - Id: sample-origin
            DomainName: example.com
            CustomOriginConfig:
              OriginProtocolPolicy: http-only
        DefaultCacheBehavior:
          TargetOriginId: sample-origin
          ViewerProtocolPolicy: redirect-to-https
          # Managed CachingOptimized cache policy.
          CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6

  SampleKeyValueStore:
    Type: AWS::CloudFront::KeyValueStore
    Properties:
      Name: !Sub 'ppmkvs-${AWS::StackName}'

  # A subscription associates exactly one distribution and one web ACL. A Key Value
  # Store is optional, limited to one, and requires the Pro tier or higher. Paid tiers
  # start in PENDING_APPROVAL and must be approved out of band before billing begins.
  SampleSubscription:
    Type: AWS::PricingPlanManager::Subscription
    Properties:
      PlanFamily: CloudFront
      PlanTier: PRO
      UsageLevel: DEFAULT
      ResourceArns:
        - !Sub 'arn:${AWS::Partition}:cloudfront::${AWS::AccountId}:distribution/${SampleDistribution}'
        - !GetAtt SampleWebAcl.Arn
        - !GetAtt SampleKeyValueStore.Arn
```
