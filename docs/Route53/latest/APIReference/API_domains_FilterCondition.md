---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_FilterCondition.html
---

# FilterCondition
<a name="API_domains_FilterCondition"></a>

Information for the filtering of a list of domains returned by [ListDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains__ListDomains.html).

## Contents
<a name="API_domains_FilterCondition_Contents"></a>

 ** Name **   <a name="Route53Domains-Type-domains_FilterCondition-Name"></a>
Name of the field which should be used for filtering the list of domains.
Type: String
Valid Values: `DomainName | Expiry`
Required: Yes

 ** Operator **   <a name="Route53Domains-Type-domains_FilterCondition-Operator"></a>
The operator values for filtering domain names. The values can be:
+  `LE`: Less than, or equal to
+  `GE`: Greater than, or equal to
+  `BEGINS_WITH`: Begins with
Type: String
Valid Values: `LE | GE | BEGINS_WITH`
Required: Yes

 ** Values **   <a name="Route53Domains-Type-domains_FilterCondition-Values"></a>
 An array of strings presenting values to compare. Only 1 item in the list is currently supported.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_domains_FilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/FilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/FilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/FilterCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
