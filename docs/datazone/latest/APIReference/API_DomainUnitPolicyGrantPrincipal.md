---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DomainUnitPolicyGrantPrincipal.html
---

# DomainUnitPolicyGrantPrincipal
<a name="API_DomainUnitPolicyGrantPrincipal"></a>

The domain unit principal to whom the policy is granted.

## Contents
<a name="API_DomainUnitPolicyGrantPrincipal_Contents"></a>

 ** domainUnitDesignation **   <a name="datazone-Type-DomainUnitPolicyGrantPrincipal-domainUnitDesignation"></a>
Specifes the designation of the domain unit users.
Type: String
Valid Values: `OWNER`
Required: Yes

 ** domainUnitGrantFilter **   <a name="datazone-Type-DomainUnitPolicyGrantPrincipal-domainUnitGrantFilter"></a>
The grant filter for the domain unit.
Type: [DomainUnitGrantFilter](API_DomainUnitGrantFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** domainUnitIdentifier **   <a name="datazone-Type-DomainUnitPolicyGrantPrincipal-domainUnitIdentifier"></a>
The ID of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: No

## See Also
<a name="API_DomainUnitPolicyGrantPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DomainUnitPolicyGrantPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DomainUnitPolicyGrantPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DomainUnitPolicyGrantPrincipal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
