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
The TLD registry didn't reply with a definitive answer about whether the domain name can be transferred. Route 53 can return this response for a variety of reasons, for example, the registry is performing maintenance. Try again later.
PENDING
The TLD registry didn't return a response in the expected amount of time. When the response is delayed, it usually takes just a few extra seconds. You can resubmit the request immediately.
DOMAIN\_IN\_OWN\_ACCOUNT
The domain already exists in the current AWS account.
DOMAIN\_IN\_ANOTHER\_ACCOUNT
 The domain exists in another AWS account.
PREMIUM\_DOMAIN
Premium domain transfer is not supported.
Type: String
Valid Values: `TRANSFERABLE | UNTRANSFERABLE | DONT_KNOW | DOMAIN_IN_OWN_ACCOUNT | DOMAIN_IN_ANOTHER_ACCOUNT | PREMIUM_DOMAIN | PENDING`
Required: No

## See Also
<a name="API_domains_DomainTransferability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/DomainTransferability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/DomainTransferability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/DomainTransferability)
