---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbDomainMembership.html
---

# AwsRdsDbDomainMembership
<a name="API_AwsRdsDbDomainMembership"></a>

Information about an Active Directory domain membership record associated with the DB instance.

## Contents
<a name="API_AwsRdsDbDomainMembership_Contents"></a>

 ** Domain **   <a name="securityhub-Type-AwsRdsDbDomainMembership-Domain"></a>
The identifier of the Active Directory domain.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Fqdn **   <a name="securityhub-Type-AwsRdsDbDomainMembership-Fqdn"></a>
The fully qualified domain name of the Active Directory domain.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IamRoleName **   <a name="securityhub-Type-AwsRdsDbDomainMembership-IamRoleName"></a>
The name of the IAM role to use when making API calls to the Directory Service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsRdsDbDomainMembership-Status"></a>
The status of the Active Directory Domain membership for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRdsDbDomainMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbDomainMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbDomainMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbDomainMembership)
