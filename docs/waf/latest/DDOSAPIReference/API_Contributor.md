---
source_url: https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Contributor.html
---

# Contributor
<a name="API_Contributor"></a>

A contributor to the attack and their contribution.

## Contents
<a name="API_Contributor_Contents"></a>

 ** Name **   <a name="AWSShield-Type-Contributor-Name"></a>
The name of the contributor. The type of name that you'll find here depends on the `AttackPropertyIdentifier` setting in the `AttackProperty` where this contributor is defined. For example, if the `AttackPropertyIdentifier` is `SOURCE_COUNTRY`, the `Name` could be `United States`.
Type: String
Required: No

 ** Value **   <a name="AWSShield-Type-Contributor-Value"></a>
The contribution of this contributor expressed in [Protection](API_Protection.md) units. For example `10,000`.
Type: Long
Required: No

## See Also
<a name="API_Contributor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/Contributor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/Contributor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/Contributor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
