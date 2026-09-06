---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ScpActionDefinition.html
---

# ScpActionDefinition
<a name="API_budgets_ScpActionDefinition"></a>

The service control policies (SCP) action definition details.

## Contents
<a name="API_budgets_ScpActionDefinition_Contents"></a>

 ** PolicyId **   <a name="awscostmanagement-Type-budgets_ScpActionDefinition-PolicyId"></a>
The policy ID attached.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 130.
Pattern: `^p-[0-9a-zA-Z_]{8,128}$`
Required: Yes

 ** TargetIds **   <a name="awscostmanagement-Type-budgets_ScpActionDefinition-TargetIds"></a>
A list of target IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 12. Maximum length of 68.
Pattern: `^(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$)|(\d{12})`
Required: Yes

## See Also
<a name="API_budgets_ScpActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/ScpActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/ScpActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/ScpActionDefinition)
