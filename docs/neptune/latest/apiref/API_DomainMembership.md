---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DomainMembership.html
---

# DomainMembership
<a name="API_DomainMembership"></a>

An Active Directory Domain membership record associated with a DB instance.

## Contents
<a name="API_DomainMembership_Contents"></a>

 ** Domain **
The identifier of the Active Directory Domain.
Type: String
Required: No

 ** FQDN **
The fully qualified domain name of the Active Directory Domain.
Type: String
Required: No

 ** IAMRoleName **
The name of the IAM role to be used when making API calls to the Directory Service.
Type: String
Required: No

 ** Status **
The status of the DB instance's Active Directory Domain membership, such as joined, pending-join, failed etc).
Type: String
Required: No

## See Also
<a name="API_DomainMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DomainMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DomainMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DomainMembership)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
