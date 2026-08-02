---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-vpclattice-service.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Service
<a name="aws-resource-vpclattice-service"></a>

Creates a service. A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).

For more information, see [Services](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html) in the *Amazon VPC Lattice User Guide*.

## Syntax
<a name="aws-resource-vpclattice-service-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-vpclattice-service-syntax.json"></a>

```
{
  "Type" : "AWS::VpcLattice::Service",
  "Properties" : {
      "[AuthType](#cfn-vpclattice-service-authtype)" : {{String}},
      "[CertificateArn](#cfn-vpclattice-service-certificatearn)" : {{String}},
      "[CustomDomainName](#cfn-vpclattice-service-customdomainname)" : {{String}},
      "[DnsEntry](#cfn-vpclattice-service-dnsentry)" : {{DnsEntry}},
      "[IdleTimeoutSeconds](#cfn-vpclattice-service-idletimeoutseconds)" : {{Integer}},
      "[Name](#cfn-vpclattice-service-name)" : {{String}},
      "[Tags](#cfn-vpclattice-service-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-vpclattice-service-syntax.yaml"></a>

```
Type: AWS::VpcLattice::Service
Properties:
  [AuthType](#cfn-vpclattice-service-authtype): {{String}}
  [CertificateArn](#cfn-vpclattice-service-certificatearn): {{String}}
  [CustomDomainName](#cfn-vpclattice-service-customdomainname): {{String}}
  [DnsEntry](#cfn-vpclattice-service-dnsentry): {{
    DnsEntry}}
  [IdleTimeoutSeconds](#cfn-vpclattice-service-idletimeoutseconds): {{Integer}}
  [Name](#cfn-vpclattice-service-name): {{String}}
  [Tags](#cfn-vpclattice-service-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-vpclattice-service-properties"></a>

`AuthType`  <a name="cfn-vpclattice-service-authtype"></a>
The type of IAM policy.
+ `NONE`: The resource does not use an IAM policy. This is the default.
+ `AWS_IAM`: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.
*Required*: No
*Type*: String
*Allowed values*: `NONE | AWS_IAM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateArn`  <a name="cfn-vpclattice-service-certificatearn"></a>
The Amazon Resource Name (ARN) of the certificate.
*Required*: No
*Type*: String
*Pattern*: `^(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:certificate/[0-9a-z-]+)?$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomDomainName`  <a name="cfn-vpclattice-service-customdomainname"></a>
The custom domain name of the service.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DnsEntry`  <a name="cfn-vpclattice-service-dnsentry"></a>
Describes the DNS information of the service. This field is read-only.
*Required*: No
*Type*: [DnsEntry](aws-properties-vpclattice-service-dnsentry.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdleTimeoutSeconds`  <a name="cfn-vpclattice-service-idletimeoutseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-vpclattice-service-name"></a>
The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.
If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
*Required*: No
*Type*: String
*Pattern*: `^(?!svc-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-vpclattice-service-tags"></a>
The tags for the service.
*Required*: No
*Type*: Array of [Tag](aws-properties-vpclattice-service-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-vpclattice-service-return-values"></a>

### Ref
<a name="aws-resource-vpclattice-service-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the service.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-vpclattice-service-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-vpclattice-service-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the service.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the service was created, specified in ISO-8601 format.

`DnsEntry.DomainName`  <a name="DnsEntry.DomainName-fn::getatt"></a>
The domain name of the service.

`DnsEntry.HostedZoneId`  <a name="DnsEntry.HostedZoneId-fn::getatt"></a>
The ID of the hosted zone.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the service.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The date and time that the service was last updated, specified in ISO-8601 format.

`Status`  <a name="Status-fn::getatt"></a>
The status of the service.
