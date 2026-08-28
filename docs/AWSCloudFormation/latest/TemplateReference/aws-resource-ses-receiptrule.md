---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-receiptrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ReceiptRule
<a name="aws-resource-ses-receiptrule"></a>

Specifies a receipt rule.

## Syntax
<a name="aws-resource-ses-receiptrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-receiptrule-syntax.json"></a>

```
{
  "Type" : "AWS::SES::ReceiptRule",
  "Properties" : {
      "[After](#cfn-ses-receiptrule-after)" : {{String}},
      "[Rule](#cfn-ses-receiptrule-rule)" : {{Rule}},
      "[RuleSetName](#cfn-ses-receiptrule-rulesetname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ses-receiptrule-syntax.yaml"></a>

```
Type: AWS::SES::ReceiptRule
Properties:
  [After](#cfn-ses-receiptrule-after): {{String}}
  [Rule](#cfn-ses-receiptrule-rule): {{
    Rule}}
  [RuleSetName](#cfn-ses-receiptrule-rulesetname): {{String}}
```

## Properties
<a name="aws-resource-ses-receiptrule-properties"></a>

`After`  <a name="cfn-ses-receiptrule-after"></a>
The name of an existing rule after which the new rule is placed. If this parameter is null, the new rule is inserted at the beginning of the rule list.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rule`  <a name="cfn-ses-receiptrule-rule"></a>
A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.
*Required*: Yes
*Type*: [Rule](aws-properties-ses-receiptrule-rule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleSetName`  <a name="cfn-ses-receiptrule-rulesetname"></a>
The name of the rule set where the receipt rule is added.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ses-receiptrule-return-values"></a>

### Ref
<a name="aws-resource-ses-receiptrule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ses-receiptrule-return-values-fn--getatt"></a>

####
<a name="aws-resource-ses-receiptrule-return-values-fn--getatt-fn--getatt"></a>

`RuleName`  <a name="RuleName-fn::getatt"></a>
The name of the receipt rule to reposition.

## Examples
<a name="aws-resource-ses-receiptrule--examples"></a>

Specifies a receipt rule for incoming email.

###
<a name="aws-resource-ses-receiptrule--examples--"></a>

#### JSON
<a name="aws-resource-ses-receiptrule--examples----json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "AWS SES ReceiptRule Sample Template",
    "Parameters": {
        "RuleSetName": {
            "Type": "String"
        },
        "ReceiptRuleName1": {
            "Type": "String"
        },
        "ReceiptRuleName2": {
            "Type": "String"
        },
        "TlsPolicy": {
            "Type": "String"
        },
        "HeaderName": {
            "Type": "String"
        },
        "HeaderValue": {
            "Type": "String"
        }
    },
    "Resources": {
        "ReceiptRule1": {
            "Type": "AWS::SES::ReceiptRule",
            "Properties": {
                "RuleSetName": {
                    "Ref": "RuleSetName"
                },
                "Rule": {
                    "Name": {
                        "Ref": "ReceiptRuleName1"
                    },
                    "Enabled": true,
                    "ScanEnabled": true,
                    "TlsPolicy": {
                        "Ref": "TlsPolicy"
                    },
                    "Actions": [
                        {
                            "AddHeaderAction": {
                                "HeaderName": {
                                    "Ref": "HeaderName"
                                },
                                "HeaderValue": {
                                    "Ref": "HeaderValue"
                                }
                            }
                        }
                    ]
                }
            }
        },
        "ReceiptRule2": {
            "Type": "AWS::SES::ReceiptRule",
            "Properties": {
                "RuleSetName": {
                    "Ref": "RuleSetName"
                },
                "After": {
                    "Ref": "ReceiptRule1"
                },
                "Rule": {
                    "Name": {
                        "Ref": "ReceiptRuleName2"
                    }
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ses-receiptrule--examples----yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: AWS SES ReceiptRule Sample Template
Parameters:
  RuleSetName:
    Type: String
  ReceiptRuleName1:
    Type: String
  ReceiptRuleName2:
    Type: String
  TlsPolicy:
    Type: String
  HeaderName:
    Type: String
  HeaderValue:
    Type: String
Resources:
  ReceiptRule1:
    Type: 'AWS::SES::ReceiptRule'
    Properties:
      RuleSetName: !Ref RuleSetName
      Rule:
        Name: !Ref ReceiptRuleName1
        Enabled: true
        ScanEnabled: true
        TlsPolicy: !Ref TlsPolicy
        Actions:
          - AddHeaderAction:
              HeaderName: !Ref HeaderName
              HeaderValue: !Ref HeaderValue
  ReceiptRule2:
    Type: 'AWS::SES::ReceiptRule'
    Properties:
      RuleSetName: !Ref RuleSetName
      After: !Ref ReceiptRule1
      Rule:
        Name: !Ref ReceiptRuleName2
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
