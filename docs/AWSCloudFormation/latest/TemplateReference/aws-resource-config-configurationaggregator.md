---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-configurationaggregator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConfigurationAggregator
<a name="aws-resource-config-configurationaggregator"></a>

The details about the configuration aggregator, including information about source accounts, regions, and metadata of the aggregator.

## Syntax
<a name="aws-resource-config-configurationaggregator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-config-configurationaggregator-syntax.json"></a>

```
{
  "Type" : "AWS::Config::ConfigurationAggregator",
  "Properties" : {
      "[AccountAggregationSources](#cfn-config-configurationaggregator-accountaggregationsources)" : {{[ AccountAggregationSource, ... ]}},
      "[ConfigurationAggregatorName](#cfn-config-configurationaggregator-configurationaggregatorname)" : {{String}},
      "[OrganizationAggregationSource](#cfn-config-configurationaggregator-organizationaggregationsource)" : {{OrganizationAggregationSource}},
      "[Tags](#cfn-config-configurationaggregator-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-config-configurationaggregator-syntax.yaml"></a>

```
Type: AWS::Config::ConfigurationAggregator
Properties:
  [AccountAggregationSources](#cfn-config-configurationaggregator-accountaggregationsources): {{
    - AccountAggregationSource}}
  [ConfigurationAggregatorName](#cfn-config-configurationaggregator-configurationaggregatorname): {{String}}
  [OrganizationAggregationSource](#cfn-config-configurationaggregator-organizationaggregationsource): {{
    OrganizationAggregationSource}}
  [Tags](#cfn-config-configurationaggregator-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-config-configurationaggregator-properties"></a>

`AccountAggregationSources`  <a name="cfn-config-configurationaggregator-accountaggregationsources"></a>
Provides a list of source accounts and regions to be aggregated.
*Required*: No
*Type*: Array of [AccountAggregationSource](aws-properties-config-configurationaggregator-accountaggregationsource.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigurationAggregatorName`  <a name="cfn-config-configurationaggregator-configurationaggregatorname"></a>
The name of the aggregator.
*Required*: No
*Type*: String
*Pattern*: `[\w\-]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OrganizationAggregationSource`  <a name="cfn-config-configurationaggregator-organizationaggregationsource"></a>
Provides an organization and list of regions to be aggregated.
*Required*: No
*Type*: [OrganizationAggregationSource](aws-properties-config-configurationaggregator-organizationaggregationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-config-configurationaggregator-tags"></a>
An array of tag object.
*Required*: No
*Type*: Array of [Tag](aws-properties-config-configurationaggregator-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-config-configurationaggregator-return-values"></a>

### Ref
<a name="aws-resource-config-configurationaggregator-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ConfigurationAggregatorName, such as `myConfigurationAggregator`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-config-configurationaggregator-return-values-fn--getatt"></a>

####
<a name="aws-resource-config-configurationaggregator-return-values-fn--getatt-fn--getatt"></a>

`ConfigurationAggregatorArn`  <a name="ConfigurationAggregatorArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the aggregator.

## Examples
<a name="aws-resource-config-configurationaggregator--examples"></a>

**Topics**
+ [Configuration Aggregator With Multiple Accounts Multiple Regions](#aws-resource-config-configurationaggregator--examples--Configuration_Aggregator_With_Multiple_Accounts_Multiple_Regions)
+ [Configuration Aggregator for an Organization](#aws-resource-config-configurationaggregator--examples--Configuration_Aggregator_for_an_Organization)

### Configuration Aggregator With Multiple Accounts Multiple Regions
<a name="aws-resource-config-configurationaggregator--examples--Configuration_Aggregator_With_Multiple_Accounts_Multiple_Regions"></a>

The following example creates a `ConfigurationAggregator`.

#### JSON
<a name="aws-resource-config-configurationaggregator--examples--Configuration_Aggregator_With_Multiple_Accounts_Multiple_Regions--json"></a>

```
"ConfigurationAggregator": {
    "Type": "AWS::Config::ConfigurationAggregator",
    "Properties": {
      "AccountAggregationSources": [
        {
          "AccountIds": [
            "123456789012",
            "987654321012"
          ],
          "AwsRegions": [
            "us-west-2",
            "us-east-1"
          ],
          "AllAwsRegions": false
        }
      ],
      "ConfigurationAggregatorName": "MyConfigurationAggregator"
    }
  }
```

#### YAML
<a name="aws-resource-config-configurationaggregator--examples--Configuration_Aggregator_With_Multiple_Accounts_Multiple_Regions--yaml"></a>

```
ConfigurationAggregator:
  Type: 'AWS::Config::ConfigurationAggregator'
  Properties:
    AccountAggregationSources:
      - AccountIds:
          - '123456789012'
          - '987654321012'
        AwsRegions:
          - us-west-2
          - us-east-1
        AllAwsRegions: false
    ConfigurationAggregatorName: MyConfigurationAggregator
```

### Configuration Aggregator for an Organization
<a name="aws-resource-config-configurationaggregator--examples--Configuration_Aggregator_for_an_Organization"></a>

The following example creates a `ConfigurationAggregator` for an organization.

 **Considerations**
+ The aggregator account must be the management account or a delegated administrator account in the organization
+ AWS Config must be enabled with proper service access in the organization
+ The role must have proper permissions to call AWS Organizations APIs

#### JSON
<a name="aws-resource-config-configurationaggregator--examples--Configuration_Aggregator_for_an_Organization--json"></a>

```
"ConfigurationAggregator": {
    "Type": "AWS::Config::ConfigurationAggregator",
    "Properties": {
        "OrganizationAggregationSource": {
            "RoleArn": { "Fn::GetAtt" : [ "MyRole", "Arn" ] },
            "AwsRegions": [
                "us-west-2",
                "us-east-1"
            ],
            "AllAwsRegions": false
        },
        "ConfigurationAggregatorName": "MyConfigurationAggregator"
    }
}

"MyRole": {
    "Type": "AWS::IAM::Role",
    "Properties": {
        "ManagedPolicyArns": [
            "arn:aws:iam::aws:policy/service-role/AWSConfigRoleForOrganizations"
        ],
        "Path": "/service-role/",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "config.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        },
        "Policies": [
            {
                "PolicyName": "OrganizationAccess",
                "PolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": [
                                "organizations:DescribeOrganization",
                                "organizations:ListAWSServiceAccessForOrganization",
                                "organizations:ListAccounts"
                            ],
                            "Resource": "*"
                        }
                    ]
                }
            }
        ]
    }
}
```

#### YAML
<a name="aws-resource-config-configurationaggregator--examples--Configuration_Aggregator_for_an_Organization--yaml"></a>

```
ConfigurationAggregator:
    Type: 'AWS::Config::ConfigurationAggregator'
    Properties:
        OrganizationAggregationSource:
            RoleArn: !GetAtt MyRole.Arn
            AwsRegions:
                - us-west-2
                - us-east-1
            AllAwsRegions: false
        ConfigurationAggregatorName: MyConfigurationAggregator

MyRole:
    Type: AWS::IAM::Role
    Properties:
        ManagedPolicyArns:
            - arn:aws:iam::aws:policy/service-role/AWSConfigRoleForOrganizations
        Path: "/service-role/"
        AssumeRolePolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Principal:
                    Service:
                        - config.amazonaws.com
                Action:
                    - 'sts:AssumeRole'
        Policies:
            - PolicyName: OrganizationAccess
              PolicyDocument:
                Version: "2012-10-17"
                Statement:
                    - Effect: Allow
                      Action:
                        - organizations:DescribeOrganization
                        - organizations:ListAWSServiceAccessForOrganization
                        - organizations:ListAccounts
                      Resource: "*"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
