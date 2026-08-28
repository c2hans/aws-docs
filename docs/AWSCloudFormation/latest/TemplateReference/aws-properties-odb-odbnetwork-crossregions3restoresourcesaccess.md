---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-odbnetwork-crossregions3restoresourcesaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::OdbNetwork CrossRegionS3RestoreSourcesAccess
<a name="aws-properties-odb-odbnetwork-crossregions3restoresourcesaccess"></a>

The configuration access for the cross-Region Amazon S3 database restore source for the ODB network.

## Syntax
<a name="aws-properties-odb-odbnetwork-crossregions3restoresourcesaccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-odbnetwork-crossregions3restoresourcesaccess-syntax.json"></a>

```
{
  "[Ipv4Addresses](#cfn-odb-odbnetwork-crossregions3restoresourcesaccess-ipv4addresses)" : {{[ String, ... ]}},
  "[Region](#cfn-odb-odbnetwork-crossregions3restoresourcesaccess-region)" : {{String}},
  "[Status](#cfn-odb-odbnetwork-crossregions3restoresourcesaccess-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-odb-odbnetwork-crossregions3restoresourcesaccess-syntax.yaml"></a>

```
  [Ipv4Addresses](#cfn-odb-odbnetwork-crossregions3restoresourcesaccess-ipv4addresses): {{
    - String}}
  [Region](#cfn-odb-odbnetwork-crossregions3restoresourcesaccess-region): {{String}}
  [Status](#cfn-odb-odbnetwork-crossregions3restoresourcesaccess-status): {{String}}
```

## Properties
<a name="aws-properties-odb-odbnetwork-crossregions3restoresourcesaccess-properties"></a>

`Ipv4Addresses`  <a name="cfn-odb-odbnetwork-crossregions3restoresourcesaccess-ipv4addresses"></a>
The IPv4 addresses allowed for cross-Region Amazon S3 restore access.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-odb-odbnetwork-crossregions3restoresourcesaccess-region"></a>
The AWS Region for cross-Region Amazon S3 restore access.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-odb-odbnetwork-crossregions3restoresourcesaccess-status"></a>
The current status of the cross-Region Amazon S3 restore access configuration.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | ENABLING | DISABLED | DISABLING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
