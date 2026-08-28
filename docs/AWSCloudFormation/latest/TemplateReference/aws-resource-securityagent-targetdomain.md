---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityagent-targetdomain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::TargetDomain
<a name="aws-resource-securityagent-targetdomain"></a>

The `AWS::SecurityAgent::TargetDomain` resource specifies a target domain for security testing. A target domain represents a web domain that you own and want to include in penetration testing scope.

## Syntax
<a name="aws-resource-securityagent-targetdomain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityagent-targetdomain-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityAgent::TargetDomain",
  "Properties" : {
      "[Tags](#cfn-securityagent-targetdomain-tags)" : {{[ Tag, ... ]}},
      "[TargetDomainName](#cfn-securityagent-targetdomain-targetdomainname)" : {{String}},
      "[VerificationMethod](#cfn-securityagent-targetdomain-verificationmethod)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-securityagent-targetdomain-syntax.yaml"></a>

```
Type: AWS::SecurityAgent::TargetDomain
Properties:
  [Tags](#cfn-securityagent-targetdomain-tags): {{
    - Tag}}
  [TargetDomainName](#cfn-securityagent-targetdomain-targetdomainname): {{String}}
  [VerificationMethod](#cfn-securityagent-targetdomain-verificationmethod): {{String}}
```

## Properties
<a name="aws-resource-securityagent-targetdomain-properties"></a>

`Tags`  <a name="cfn-securityagent-targetdomain-tags"></a>
The tags to associate with the target domain.
*Required*: No
*Type*: Array of [Tag](aws-properties-securityagent-targetdomain-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetDomainName`  <a name="cfn-securityagent-targetdomain-targetdomainname"></a>
The domain name to register as a target domain.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VerificationMethod`  <a name="cfn-securityagent-targetdomain-verificationmethod"></a>
The method to use for verifying domain ownership. Valid values are DNS\_TXT, HTTP\_ROUTE, and PRIVATE\_VPC.
*Required*: Yes
*Type*: String
*Allowed values*: `DNS_TXT | HTTP_ROUTE | PRIVATE_VPC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityagent-targetdomain-return-values"></a>

### Ref
<a name="aws-resource-securityagent-targetdomain-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the target domain ID. For example:

 `{ "Ref": "MyTargetDomain" }`

For the target domain `MyTargetDomain`, `Ref` returns the unique identifier of the target domain.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityagent-targetdomain-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityagent-targetdomain-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the target domain was registered, in ISO 8601 format. For example: `2024-01-01T00:00:00Z`.

`TargetDomainId`  <a name="TargetDomainId-fn::getatt"></a>
The unique identifier of the target domain. For example: `td-0123456789abcdef0`.

`VerificationStatus`  <a name="VerificationStatus-fn::getatt"></a>
The current verification status of the target domain. Valid values are `PENDING`, `VERIFIED`, `FAILED`, and `UNREACHABLE`.

`VerificationStatusReason`  <a name="VerificationStatusReason-fn::getatt"></a>
The reason for the current target domain verification status.

`VerifiedAt`  <a name="VerifiedAt-fn::getatt"></a>
The date and time when the target domain was last successfully verified, in ISO 8601 format. For example: `2024-01-01T00:00:00Z`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
