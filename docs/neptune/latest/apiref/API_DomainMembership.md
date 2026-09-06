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
