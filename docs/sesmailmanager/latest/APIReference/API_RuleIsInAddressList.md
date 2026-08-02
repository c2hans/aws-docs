---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleIsInAddressList.html
---

# RuleIsInAddressList
<a name="API_RuleIsInAddressList"></a>

The structure type for a boolean condition that provides the address lists and address list attribute to evaluate.

## Contents
<a name="API_RuleIsInAddressList_Contents"></a>

 ** AddressLists **   <a name="sesmailmanager-Type-RuleIsInAddressList-AddressLists"></a>
The address lists that will be used for evaluation.
Type: Array of strings
Array Members: Fixed number of 1 item.
Required: Yes

 ** Attribute **   <a name="sesmailmanager-Type-RuleIsInAddressList-Attribute"></a>
The email attribute that needs to be evaluated against the address list.
Type: String
Valid Values: `RECIPIENT | MAIL_FROM | SENDER | FROM | TO | CC`
Required: Yes

## See Also
<a name="API_RuleIsInAddressList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleIsInAddressList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleIsInAddressList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleIsInAddressList)
