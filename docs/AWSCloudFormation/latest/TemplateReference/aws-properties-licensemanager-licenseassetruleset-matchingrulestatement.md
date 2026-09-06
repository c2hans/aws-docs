---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-licenseassetruleset-matchingrulestatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseAssetRuleSet MatchingRuleStatement
<a name="aws-properties-licensemanager-licenseassetruleset-matchingrulestatement"></a>

Matching rule statement.

## Syntax
<a name="aws-properties-licensemanager-licenseassetruleset-matchingrulestatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-licenseassetruleset-matchingrulestatement-syntax.json"></a>

```
{
  "[Constraint](#cfn-licensemanager-licenseassetruleset-matchingrulestatement-constraint)" : {{String}},
  "[KeyToMatch](#cfn-licensemanager-licenseassetruleset-matchingrulestatement-keytomatch)" : {{String}},
  "[ValueToMatch](#cfn-licensemanager-licenseassetruleset-matchingrulestatement-valuetomatch)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-licensemanager-licenseassetruleset-matchingrulestatement-syntax.yaml"></a>

```
  [Constraint](#cfn-licensemanager-licenseassetruleset-matchingrulestatement-constraint): {{String}}
  [KeyToMatch](#cfn-licensemanager-licenseassetruleset-matchingrulestatement-keytomatch): {{String}}
  [ValueToMatch](#cfn-licensemanager-licenseassetruleset-matchingrulestatement-valuetomatch): {{
    - String}}
```

## Properties
<a name="aws-properties-licensemanager-licenseassetruleset-matchingrulestatement-properties"></a>

`Constraint`  <a name="cfn-licensemanager-licenseassetruleset-matchingrulestatement-constraint"></a>
Constraint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyToMatch`  <a name="cfn-licensemanager-licenseassetruleset-matchingrulestatement-keytomatch"></a>
Key to match.
The following keys and are supported when the RuleStatement type is `Instance`:
+ `Platform` - The name of the platform. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `EC2BillingProduct` - The billing product code. Logical operators are `EQUALS` and `NOT_EQUALS`. Possible values are: `windows-server-enterprise` \| `windows-byol` \| `rhel` \| `rhel-byol` \| `rhel-high-availability` \| `ubuntu-pro` \| `suse-linux` \| `sql-server-standard` \| `sql-server-enterprise`.
+ `MarketPlaceProductCode` - The Marketplace product code. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `AMIId` - The ID of the AMI. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `InstanceType` - The instance type. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `InstanceId` - The ID of the instance. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `HostId` - The ID of the host. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `AccountId` - The ID of the account. Logical operators are `EQUALS` and `NOT_EQUALS`.
The following keys and are supported when the RuleStatement type is `License`:
+ `LicenseArn` - The ARN of a Managed Entitlement License. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `ProductSKU` - The productSKU of the license. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `Issuer` - The issuer of the license. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `Beneficiary` - The beneficiary of the license. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `LicenseStatus` - The status of the license. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `HomeRegion` - The home region of the license. Logical operators are `EQUALS` and `NOT_EQUALS`.
The following keys and are supported when the RuleStatement type is `License Configuration`:
+ `LicenseConfigurationArn` - The ARN of a self-managed license configuration. Logical operators are `EQUALS` and `NOT_EQUALS`.
+ `AccountId` - The account of the license configuration. Logical operators are `EQUALS` and `NOT_EQUALS`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueToMatch`  <a name="cfn-licensemanager-licenseassetruleset-matchingrulestatement-valuetomatch"></a>
Value to match.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
