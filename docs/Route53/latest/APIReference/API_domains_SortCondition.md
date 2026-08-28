---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_SortCondition.html
---

# SortCondition
<a name="API_domains_SortCondition"></a>

Information for sorting a list of domains.

## Contents
<a name="API_domains_SortCondition_Contents"></a>

 ** Name **   <a name="Route53Domains-Type-domains_SortCondition-Name"></a>
Field to be used for sorting the list of domains. It can be either the name or the expiration for a domain. Note that if `filterCondition` is used in the same [ListDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains__ListDomains.html) call, the field used for sorting has to be the same as the field used for filtering.
Type: String
Valid Values: `DomainName | Expiry`
Required: Yes

 ** SortOrder **   <a name="Route53Domains-Type-domains_SortCondition-SortOrder"></a>
The sort order for a list of domains. Either ascending (ASC) or descending (DES).
Type: String
Valid Values: `ASC | DESC`
Required: Yes

## See Also
<a name="API_domains_SortCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/SortCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/SortCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/SortCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
