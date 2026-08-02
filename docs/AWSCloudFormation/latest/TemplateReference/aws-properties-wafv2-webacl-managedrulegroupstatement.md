---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-managedrulegroupstatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ManagedRuleGroupStatement
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement"></a>

A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names through the API call `ListAvailableManagedRuleGroups`.

You cannot nest a `ManagedRuleGroupStatement`, for example for use inside a `NotStatement` or `OrStatement`. You cannot use a managed rule group statement inside another rule group. You can only use a managed rule group statement as a top-level statement in a rule that you define in a web ACL.

**Note**
You are charged additional fees when you use the AWS WAF Bot Control managed rule group `AWSManagedRulesBotControlRuleSet`, the AWS WAF Fraud Control account takeover prevention (ATP) managed rule group `AWSManagedRulesATPRuleSet`, or the AWS WAF Fraud Control account creation fraud prevention (ACFP) managed rule group `AWSManagedRulesACFPRuleSet`. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

## Syntax
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement-syntax.json"></a>

```
{
  "[ExcludedRules](#cfn-wafv2-webacl-managedrulegroupstatement-excludedrules)" : {{[ ExcludedRule, ... ]}},
  "[ManagedRuleGroupConfigs](#cfn-wafv2-webacl-managedrulegroupstatement-managedrulegroupconfigs)" : {{[ ManagedRuleGroupConfig, ... ]}},
  "[Name](#cfn-wafv2-webacl-managedrulegroupstatement-name)" : {{String}},
  "[RuleActionOverrides](#cfn-wafv2-webacl-managedrulegroupstatement-ruleactionoverrides)" : {{[ RuleActionOverride, ... ]}},
  "[ScopeDownStatement](#cfn-wafv2-webacl-managedrulegroupstatement-scopedownstatement)" : {{Statement}},
  "[VendorName](#cfn-wafv2-webacl-managedrulegroupstatement-vendorname)" : {{String}},
  "[Version](#cfn-wafv2-webacl-managedrulegroupstatement-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement-syntax.yaml"></a>

```
  [ExcludedRules](#cfn-wafv2-webacl-managedrulegroupstatement-excludedrules): {{
    - ExcludedRule}}
  [ManagedRuleGroupConfigs](#cfn-wafv2-webacl-managedrulegroupstatement-managedrulegroupconfigs): {{
    - ManagedRuleGroupConfig}}
  [Name](#cfn-wafv2-webacl-managedrulegroupstatement-name): {{String}}
  [RuleActionOverrides](#cfn-wafv2-webacl-managedrulegroupstatement-ruleactionoverrides): {{
    - RuleActionOverride}}
  [ScopeDownStatement](#cfn-wafv2-webacl-managedrulegroupstatement-scopedownstatement): {{
    Statement}}
  [VendorName](#cfn-wafv2-webacl-managedrulegroupstatement-vendorname): {{String}}
  [Version](#cfn-wafv2-webacl-managedrulegroupstatement-version): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement-properties"></a>

`ExcludedRules`  <a name="cfn-wafv2-webacl-managedrulegroupstatement-excludedrules"></a>
Rules in the referenced rule group whose actions are set to `Count`.
Instead of this option, use `RuleActionOverrides`. It accepts any valid action setting, including `Count`.
*Required*: No
*Type*: Array of [ExcludedRule](aws-properties-wafv2-webacl-excludedrule.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedRuleGroupConfigs`  <a name="cfn-wafv2-webacl-managedrulegroupstatement-managedrulegroupconfigs"></a>
Additional information that's used by a managed rule group. Many managed rule groups don't require this.
The rule groups used for intelligent threat mitigation require additional configuration:
+ Use the `AWSManagedRulesACFPRuleSet` configuration object to configure the account creation fraud prevention managed rule group. The configuration includes the registration and sign-up pages of your application and the locations in the account creation request payload of data, such as the user email and phone number fields.
+ Use the `AWSManagedRulesAntiDDoSRuleSet` configuration object to configure the anti-DDoS managed rule group. The configuration includes the sensitivity levels to use in the rules that typically block and challenge requests that might be participating in DDoS attacks and the specification to use to indicate whether a request can handle a silent browser challenge.
+ Use the `AWSManagedRulesATPRuleSet` configuration object to configure the account takeover prevention managed rule group. The configuration includes the sign-in page of your application and the locations in the login request payload of data such as the username and password.
+ Use the `AWSManagedRulesBotControlRuleSet` configuration object to configure the protection level that you want the Bot Control rule group to use.
*Required*: No
*Type*: Array of [ManagedRuleGroupConfig](aws-properties-wafv2-webacl-managedrulegroupconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wafv2-webacl-managedrulegroupstatement-name"></a>
The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z_-]{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleActionOverrides`  <a name="cfn-wafv2-webacl-managedrulegroupstatement-ruleactionoverrides"></a>
Action settings to use in the place of the rule actions that are configured inside the rule group. You specify one override for each rule whose action you want to change.
Verify the rule names in your overrides carefully. With managed rule groups, AWS WAF silently ignores any override that uses an invalid rule name. With customer-owned rule groups, invalid rule names in your overrides will cause web ACL updates to fail. An invalid rule name is any name that doesn't exactly match the case-sensitive name of an existing rule in the rule group.
You can use overrides for testing, for example you can override all of rule actions to `Count` and then monitor the resulting count metrics to understand how the rule group would handle your web traffic. You can also permanently override some or all actions, to modify how the rule group manages your web traffic.
*Required*: No
*Type*: Array of [RuleActionOverride](aws-properties-wafv2-webacl-ruleactionoverride.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeDownStatement`  <a name="cfn-wafv2-webacl-managedrulegroupstatement-scopedownstatement"></a>
An optional nested statement that narrows the scope of the web requests that are evaluated by the managed rule group. Requests are only evaluated by the rule group if they match the scope-down statement. You can use any nestable [Statement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html#cfn-wafv2-webacl-notstatement-statement) in the scope-down statement, and you can nest statements at any level, the same as you can for a rule statement.
*Required*: No
*Type*: [Statement](aws-properties-wafv2-webacl-statement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VendorName`  <a name="cfn-wafv2-webacl-managedrulegroupstatement-vendorname"></a>
The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-wafv2-webacl-managedrulegroupstatement-version"></a>
The version of the managed rule group to use. If you specify this, the version setting is fixed until you change it. If you don't specify this, AWS WAF uses the vendor's default version, and then keeps the version at the vendor's default when the vendor updates the managed rule group settings.
*Required*: No
*Type*: String
*Pattern*: `^[\w#:\.\-/]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement--examples"></a>

**Topics**
+ [Configure the managed rule group statement for `AWSManagedRulesATPRuleSet`](#aws-properties-wafv2-webacl-managedrulegroupstatement--examples--Configure_the_managed_rule_group_statement_for_AWSManagedRulesATPRuleSet)
+ [Configure a standard managed rule group statement](#aws-properties-wafv2-webacl-managedrulegroupstatement--examples--Configure_a_standard_managed_rule_group_statement)

### Configure the managed rule group statement for `AWSManagedRulesATPRuleSet`
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement--examples--Configure_the_managed_rule_group_statement_for_AWSManagedRulesATPRuleSet"></a>

The following shows an example `ManagedRuleGroupStatement` for the AWS WAF ATP managed rule group. The `ManagedRuleGroupConfigs` settings are provided as a number of individual `ManagedRuleGroupConfig` settings.

#### YAML
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement--examples--Configure_the_managed_rule_group_statement_for_AWSManagedRulesATPRuleSet--yaml"></a>

```
ManagedRuleGroupStatement:
  VendorName: AWS
  Name: AWSManagedRulesATPRuleSet
  ManagedRuleGroupConfigs:
    - LoginPath: /api/accounts/login
    - PayloadType: JSON
    - PasswordField:
        Identifier: /form/password
    - UsernameField:
        Identifier: /form/username
```

#### JSON
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement--examples--Configure_the_managed_rule_group_statement_for_AWSManagedRulesATPRuleSet--json"></a>

```
{
  "ManagedRuleGroupStatement": {
    "VendorName": "AWS",
    "Name": "AWSManagedRulesATPRuleSet",
    "ManagedRuleGroupConfigs": [
      {
        "LoginPath": "/api/accounts/login"
      },
      {
        "PayloadType": "JSON"
      },
      {
        "PasswordField": {
          "Identifier": "/form/password"
        }
      },
      {
        "UsernameField": {
          "Identifier": "/form/username"
        }
      }
    ]
  }
}
```

### Configure a standard managed rule group statement
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement--examples--Configure_a_standard_managed_rule_group_statement"></a>

The following shows an example `ManagedRuleGroupStatement` for a managed rule group that doesn't require additional configuration.

#### YAML
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement--examples--Configure_a_standard_managed_rule_group_statement--yaml"></a>

```
ManagedRuleGroupStatement:
  VendorName: AWS
  Name: AWSManagedRulesCommonRuleSet
```

#### JSON
<a name="aws-properties-wafv2-webacl-managedrulegroupstatement--examples--Configure_a_standard_managed_rule_group_statement--json"></a>

```
{
  "ManagedRuleGroupStatement": {
    "VendorName": "AWS",
    "Name": "AWSManagedRulesCommonRuleSet"
  }
}
```
