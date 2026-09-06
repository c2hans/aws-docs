---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-membershipprotectedjobresultconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership MembershipProtectedJobResultConfiguration
<a name="aws-properties-cleanrooms-membership-membershipprotectedjobresultconfiguration"></a>

Contains configurations for protected job results.

## Syntax
<a name="aws-properties-cleanrooms-membership-membershipprotectedjobresultconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-membershipprotectedjobresultconfiguration-syntax.json"></a>

```
{
  "[OutputConfiguration](#cfn-cleanrooms-membership-membershipprotectedjobresultconfiguration-outputconfiguration)" : {{MembershipProtectedJobOutputConfiguration}},
  "[RoleArn](#cfn-cleanrooms-membership-membershipprotectedjobresultconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-membershipprotectedjobresultconfiguration-syntax.yaml"></a>

```
  [OutputConfiguration](#cfn-cleanrooms-membership-membershipprotectedjobresultconfiguration-outputconfiguration): {{
    MembershipProtectedJobOutputConfiguration}}
  [RoleArn](#cfn-cleanrooms-membership-membershipprotectedjobresultconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-membershipprotectedjobresultconfiguration-properties"></a>

`OutputConfiguration`  <a name="cfn-cleanrooms-membership-membershipprotectedjobresultconfiguration-outputconfiguration"></a>
 The output configuration for a protected job result.
*Required*: Yes
*Type*: [MembershipProtectedJobOutputConfiguration](aws-properties-cleanrooms-membership-membershipprotectedjoboutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-cleanrooms-membership-membershipprotectedjobresultconfiguration-rolearn"></a>
The unique ARN for an IAM role that is used by AWS Clean Rooms to write protected job results to the result location, given by the member who can receive results.
*Required*: Yes
*Type*: String
*Minimum*: `32`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
