---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-membershipprotectedjoboutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership MembershipProtectedJobOutputConfiguration
<a name="aws-properties-cleanrooms-membership-membershipprotectedjoboutputconfiguration"></a>

Contains configurations for protected job results.

## Syntax
<a name="aws-properties-cleanrooms-membership-membershipprotectedjoboutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-membershipprotectedjoboutputconfiguration-syntax.json"></a>

```
{
  "[S3](#cfn-cleanrooms-membership-membershipprotectedjoboutputconfiguration-s3)" : {{ProtectedJobS3OutputConfigurationInput}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-membershipprotectedjoboutputconfiguration-syntax.yaml"></a>

```
  [S3](#cfn-cleanrooms-membership-membershipprotectedjoboutputconfiguration-s3): {{
    ProtectedJobS3OutputConfigurationInput}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-membershipprotectedjoboutputconfiguration-properties"></a>

`S3`  <a name="cfn-cleanrooms-membership-membershipprotectedjoboutputconfiguration-s3"></a>
Contains the configuration to write the job results to S3.
*Required*: Yes
*Type*: [ProtectedJobS3OutputConfigurationInput](aws-properties-cleanrooms-membership-protectedjobs3outputconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
