---
source_url: https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html
---

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

# AWS Config Rules supported by AWS Audit Manager
<a name="control-data-sources-config"></a>

You can use Audit Manager to capture AWS Config evaluations as evidence for audits. When you create or edit a custom control, you can specify one or more AWS Config rules as a data source mapping for evidence collection. AWS Config performs compliance checks based on these rules, and Audit Manager reports the results as compliance check evidence.

In addition to managed rules, you can also map your custom rules to a control data source.

**Contents**
+ [Key points](#aws-config-key-points)
+ [Supported AWS Config managed rules](#aws-config-managed-rules)
+ [Using AWS Config custom rules with Audit Manager](#aws-config-custom-rules)
+ [Additional resources](#aws-config-rules-troubleshoot)

## Key points
<a name="aws-config-key-points"></a>
+ Audit Manager doesn’t collect evidence from [service-linked AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/service-linked-awsconfig-rules.html), with the exception of service-linked rules from Conformance Packs and from AWS Organizations.
+ Audit Manager doesn't manage AWS Config rules for you. Before you start evidence collection, we recommend that you review your current AWS Config rule parameters. Then, validate those parameters against the requirements of your chosen framework. If needed, you can [update a rule's parameters in AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_manage-rules.html) so that it aligns with framework requirements. This will help to ensure that your assessments collect the correct compliance check evidence for that framework.

  For example, suppose that you’re creating an assessment for CIS v1.2.0. This framework has a control named [Ensure IAM password policy requires a minimum length of 14 or greater](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-15). In AWS Config, the [iam-password-policy](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html) rule has a `MinimumPasswordLength` parameter that checks password length. The default value for this parameter is 14 characters. As a result, the rule aligns with the control requirements. If you aren’t using the default parameter value, ensure that the value you’re using is equal to or greater than the 14 character requirement from CIS v1.2.0. You can find the default parameter details for each managed rule in the [AWS Config documentation](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html).
+ If you need to verify if an AWS Config rule is a managed rule or a custom rule, you can do this using the [AWS Config console](https://console.aws.amazon.com/config/). From the left navigation menu, choose **Rules** and look for the rule in the table. If it's a managed rule, the **Type** column shows **AWS managed**.
![A managed rule as shown in the AWS Config console.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/rules-managed-console.png)

## Supported AWS Config managed rules
<a name="aws-config-managed-rules"></a>

The following AWS Config managed rules are supported by Audit Manager. You can use any of the following managed rule identifier keywords when you set up a data source for a custom control. For more information about any of the managed rules listed below, choose an item from the list or see [AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) in the *AWS Config User Guide*.

**Tip**
When you choose a managed rule in the Audit Manager console during custom control creation, make sure that you look for one of the following rule identifier keywords, and not the rule name. For information about the difference between the rule name and rule identifier, and how to find the identifier for a managed rule, see the [Troubleshooting](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-issues.html#managed-rule-missing) section of this user guide.

| Supported AWS Config managed rule keywords |
| --- |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html)  |

## Using AWS Config custom rules with Audit Manager
<a name="aws-config-custom-rules"></a>

You can use AWS Config custom rules as a data source for audit reporting. When a control has a data source that's mapped to an AWS Config rule, Audit Manager adds the evaluation that was created by the AWS Config rule.

The custom rules that you can use depend on the AWS account that you sign in to Audit Manager with. If you can access a custom rule in AWS Config, you can use it as a data source mapping in Audit Manager.
+ **For individual AWS accounts** – You can use any of the custom rules that you created with your account.
+ **For accounts that are part of an organization** – Either, you can use any of your member-level custom rules. Or, you can use any of the organization-level custom rules that are available to you in AWS Config.

After you map your custom rules as a data source for a control, you can add that control to a custom framework in Audit Manager.

## Additional resources
<a name="aws-config-rules-troubleshoot"></a>
+ To find help with issues for this data source type, see [My assessment isn’t collecting compliance check evidence from AWS Config](evidence-collection-issues.md#no-evidence-from-config) and [AWS Config integration issues](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-issues.html#config-rule-integration.title).
+ To create a custom control using this data source type, see [Creating a custom control in AWS Audit Manager](create-controls.md).
+ To create a custom framework that uses your custom control, see [Creating a custom framework in AWS Audit Manager](custom-frameworks.md).
+ To add your custom control to an existing custom framework, see [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md).
+ To create a custom rule in AWS Config, see [Developing a custom rule for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) in the *AWS Config Developer Guide*.
