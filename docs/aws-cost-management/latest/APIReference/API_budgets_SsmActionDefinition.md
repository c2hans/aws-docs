---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_SsmActionDefinition.html
---

# SsmActionDefinition
<a name="API_budgets_SsmActionDefinition"></a>

The AWS Systems Manager (SSM) action definition details.

## Contents
<a name="API_budgets_SsmActionDefinition_Contents"></a>

 ** ActionSubType **   <a name="awscostmanagement-Type-budgets_SsmActionDefinition-ActionSubType"></a>
The action subType.
Type: String
Valid Values: `STOP_EC2_INSTANCES | STOP_RDS_INSTANCES`
Required: Yes

 ** InstanceIds **   <a name="awscostmanagement-Type-budgets_SsmActionDefinition-InstanceIds"></a>
The EC2 and RDS instance IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^i-(\w{8}|\w{17})$|^[a-zA-Z]([\w-]{0,61}\w)?$`
Required: Yes

 ** Region **   <a name="awscostmanagement-Type-budgets_SsmActionDefinition-Region"></a>
The Region to run the SSM document.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 20.
Pattern: `^\w{2,4}-\w+(-\w+)?-\d$`
Required: Yes

## See Also
<a name="API_budgets_SsmActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/SsmActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/SsmActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/SsmActionDefinition)
