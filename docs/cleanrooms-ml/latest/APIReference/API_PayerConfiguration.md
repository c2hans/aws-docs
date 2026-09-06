---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_PayerConfiguration.html
---

# PayerConfiguration
<a name="API_PayerConfiguration"></a>

Specifies which member accounts are responsible for paying for compute and synthetic data generation costs in a Clean Rooms ML collaboration.

## Contents
<a name="API_PayerConfiguration_Contents"></a>

 ** computePayerAccountId **   <a name="API-Type-PayerConfiguration-computePayerAccountId"></a>
The account ID of the member that is responsible for paying compute costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** syntheticDataPayerAccountId **   <a name="API-Type-PayerConfiguration-syntheticDataPayerAccountId"></a>
The account ID of the member that is responsible for paying synthetic data generation costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_PayerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/PayerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/PayerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/PayerConfiguration)
