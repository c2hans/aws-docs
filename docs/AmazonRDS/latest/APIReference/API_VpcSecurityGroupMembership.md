---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_VpcSecurityGroupMembership.html
---

# VpcSecurityGroupMembership
<a name="API_VpcSecurityGroupMembership"></a>

This data type is used as a response element for queries on VPC security group membership.

## Contents
<a name="API_VpcSecurityGroupMembership_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Status **
The membership status of the VPC security group.
Currently, the only valid status is `active`.
Type: String
Required: No

 ** VpcSecurityGroupId **
The name of the VPC security group.
Type: String
Required: No

## See Also
<a name="API_VpcSecurityGroupMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/VpcSecurityGroupMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/VpcSecurityGroupMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/VpcSecurityGroupMembership)
