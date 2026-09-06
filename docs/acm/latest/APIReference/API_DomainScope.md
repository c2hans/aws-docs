---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_DomainScope.html
---

# DomainScope
<a name="API_DomainScope"></a>

Specifies the scope of domain validation.

## Contents
<a name="API_DomainScope_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ExactDomain **   <a name="ACM-Type-DomainScope-ExactDomain"></a>
Whether validation applies to the exact domain.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** Subdomains **   <a name="ACM-Type-DomainScope-Subdomains"></a>
Whether validation applies to subdomains.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** Wildcards **   <a name="ACM-Type-DomainScope-Wildcards"></a>
Whether validation applies to wildcard domains.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_DomainScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DomainScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DomainScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DomainScope)
