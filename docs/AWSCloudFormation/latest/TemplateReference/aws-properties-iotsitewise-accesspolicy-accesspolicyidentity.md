---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AccessPolicy AccessPolicyIdentity
<a name="aws-properties-iotsitewise-accesspolicy-accesspolicyidentity"></a>

The identity (IAM Identity Center user, IAM Identity Center group, or IAM user) to which this access policy applies.

## Syntax
<a name="aws-properties-iotsitewise-accesspolicy-accesspolicyidentity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-accesspolicy-accesspolicyidentity-syntax.json"></a>

```
{
  "[IamRole](#cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamrole)" : {{IamRole}},
  "[IamUser](#cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamuser)" : {{IamUser}},
  "[User](#cfn-iotsitewise-accesspolicy-accesspolicyidentity-user)" : {{User}}
}
```

### YAML
<a name="aws-properties-iotsitewise-accesspolicy-accesspolicyidentity-syntax.yaml"></a>

```
  [IamRole](#cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamrole): {{
    IamRole}}
  [IamUser](#cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamuser): {{
    IamUser}}
  [User](#cfn-iotsitewise-accesspolicy-accesspolicyidentity-user): {{
    User}}
```

## Properties
<a name="aws-properties-iotsitewise-accesspolicy-accesspolicyidentity-properties"></a>

`IamRole`  <a name="cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamrole"></a>
An IAM role identity.
*Required*: No
*Type*: [IamRole](aws-properties-iotsitewise-accesspolicy-iamrole.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamUser`  <a name="cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamuser"></a>
An IAM user identity.
*Required*: No
*Type*: [IamUser](aws-properties-iotsitewise-accesspolicy-iamuser.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`User`  <a name="cfn-iotsitewise-accesspolicy-accesspolicyidentity-user"></a>
An IAM Identity Center user identity.
*Required*: No
*Type*: [User](aws-properties-iotsitewise-accesspolicy-user.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
