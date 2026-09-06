---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership MembershipProtectedQueryOutputConfiguration
<a name="aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration"></a>

Contains configurations for protected query results.

## Syntax
<a name="aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration-syntax.json"></a>

```
{
  "[S3](#cfn-cleanrooms-membership-membershipprotectedqueryoutputconfiguration-s3)" : {{ProtectedQueryS3OutputConfiguration}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration-syntax.yaml"></a>

```
  [S3](#cfn-cleanrooms-membership-membershipprotectedqueryoutputconfiguration-s3): {{
    ProtectedQueryS3OutputConfiguration}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration-properties"></a>

`S3`  <a name="cfn-cleanrooms-membership-membershipprotectedqueryoutputconfiguration-s3"></a>
Required configuration for a protected query with an `s3` output type.
*Required*: Yes
*Type*: [ProtectedQueryS3OutputConfiguration](aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
