---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-organizations-root.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Organizations::Root
<a name="aws-resource-organizations-root"></a>

Contains details about a root. A root is a top-level parent node in the hierarchy of an organization that can contain organizational units (OUs) and accounts. The root contains every AWS account in the organization.

## Syntax
<a name="aws-resource-organizations-root-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-organizations-root-syntax.json"></a>

```
{
  "Type" : "AWS::Organizations::Root"
}
```

### YAML
<a name="aws-resource-organizations-root-syntax.yaml"></a>

```
Type: AWS::Organizations::Root
```

## Return values
<a name="aws-resource-organizations-root-return-values"></a>

### Ref
<a name="aws-resource-organizations-root-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-organizations-root-return-values-fn--getatt"></a>

####
<a name="aws-resource-organizations-root-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the root.
For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the *AWS Service Authorization Reference*.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier (ID) for the root. The ID is unique to the organization only.
The [regex pattern](http://wikipedia.org/wiki/regex) for a root ID string requires "r-" followed by from 4 to 32 lowercase letters or digits.

`Name`  <a name="Name-fn::getatt"></a>
The friendly name of the root.
The [regex pattern](http://wikipedia.org/wiki/regex) that is used to validate this parameter is a string of any of the characters in the ASCII character range.

`OrganizationId`  <a name="OrganizationId-fn::getatt"></a>
The unique identifier (ID) of an organization.
The [regex pattern](http://wikipedia.org/wiki/regex) for an organization ID string requires "o-" followed by from 10 to 32 lowercase letters or digits.

`PolicyTypes`  <a name="PolicyTypes-fn::getatt"></a>
The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts.
Even if a policy type is shown as available in the organization, you can separately enable and disable them at the root level by using EnablePolicyType and DisablePolicyType. Use DescribeOrganization to see the availability of the policy types in that organization.

`Tags`  <a name="Tags-fn::getatt"></a>
Property description not available.
