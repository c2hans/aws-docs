---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_LabelMatchStatement.html
---

# LabelMatchStatement
<a name="API_LabelMatchStatement"></a>

A rule statement to match against labels that have been added to the web request by rules that have already run in the web ACL.

The label match statement provides the label or namespace string to search for. The label string can represent a part or all of the fully qualified label name that had been added to the web request. Fully qualified labels have a prefix, optional namespaces, and label name. The prefix identifies the rule group or web ACL context of the rule that added the label. If you do not provide the fully qualified name in your label match string, AWS WAF performs the search for labels that were added in the same context as the label match statement.

## Contents
<a name="API_LabelMatchStatement_Contents"></a>

 ** Key **   <a name="WAF-Type-LabelMatchStatement-Key"></a>
The string to match against. The setting you provide for this depends on the match statement's `Scope` setting:
+ If the `Scope` indicates `LABEL`, then this specification must include the name and can include any number of preceding namespace specifications and prefix up to providing the fully qualified label name.
+ If the `Scope` indicates `NAMESPACE`, then this specification can include any number of contiguous namespace strings, and can include the entire label namespace prefix from the rule group or web ACL where the label originates.
Labels are case sensitive and components of a label must be separated by colon, for example `NS1:NS2:name`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9A-Za-z_\-:]+$`
Required: Yes

 ** Scope **   <a name="WAF-Type-LabelMatchStatement-Scope"></a>
Specify whether you want to match using the label name or just the namespace.
Type: String
Valid Values: `LABEL | NAMESPACE`
Required: Yes

## See Also
<a name="API_LabelMatchStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/LabelMatchStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/LabelMatchStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/LabelMatchStatement)
