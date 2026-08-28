---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressIsInAddressList.html
---

# IngressIsInAddressList
<a name="API_IngressIsInAddressList"></a>

The address lists and the address list attribute value that is evaluated in a policy statement's conditional expression to either deny or block the incoming email.

## Contents
<a name="API_IngressIsInAddressList_Contents"></a>

 ** AddressLists **   <a name="sesmailmanager-Type-IngressIsInAddressList-AddressLists"></a>
The address lists that will be used for evaluation.
Type: Array of strings
Array Members: Fixed number of 1 item.
Required: Yes

 ** Attribute **   <a name="sesmailmanager-Type-IngressIsInAddressList-Attribute"></a>
The email attribute that needs to be evaluated against the address list.
Type: String
Valid Values: `RECIPIENT`
Required: Yes

## See Also
<a name="API_IngressIsInAddressList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/IngressIsInAddressList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/IngressIsInAddressList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/IngressIsInAddressList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
