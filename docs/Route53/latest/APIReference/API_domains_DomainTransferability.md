---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DomainTransferability.html
---

# DomainTransferability
<a name="API_domains_DomainTransferability"></a>

A complex type that contains information about whether the specified domain can be transferred to Route 53.

## Contents
<a name="API_domains_DomainTransferability_Contents"></a>

 ** Transferable **   <a name="Route53Domains-Type-domains_DomainTransferability-Transferable"></a>
Whether the domain name can be transferred to Route 53.
You can transfer only domains that have a value of `TRANSFERABLE` or `Transferable`.
Valid values:
TRANSFERABLE
The domain name can be transferred to Route 53.
UNTRANSFERRABLE
The domain name can't be transferred to Route 53.
DONT\_KNOW
The TLD registry didn't respond in time or didn't provide a definitive answer about domain transferability, which can occur due to registry maintenance or temporary delays.
DOMAIN\_IN\_OWN\_ACCOUNT
The domain already exists in the current AWS account.
DOMAIN\_IN\_ANOTHER\_ACCOUNT
 The domain exists in another AWS account.
PREMIUM\_DOMAIN
Premium domain transfer is not supported.
Type: String
Valid Values: `TRANSFERABLE | UNTRANSFERABLE | DONT_KNOW | DOMAIN_IN_OWN_ACCOUNT | DOMAIN_IN_ANOTHER_ACCOUNT | PREMIUM_DOMAIN`
Required: No

## See Also
<a name="API_domains_DomainTransferability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/DomainTransferability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/DomainTransferability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/DomainTransferability)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
