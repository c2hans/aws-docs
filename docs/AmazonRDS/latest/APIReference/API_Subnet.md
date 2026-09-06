---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Subnet.html
---

# Subnet
<a name="API_Subnet"></a>

This data type is used as a response element for the `DescribeDBSubnetGroups` operation.

## Contents
<a name="API_Subnet_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SubnetAvailabilityZone **
Contains Availability Zone information.
This data type is used as an element in the `OrderableDBInstanceOption` data type.
Type: [AvailabilityZone](API_AvailabilityZone.md) object
Required: No

 ** SubnetIdentifier **
The identifier of the subnet.
Type: String
Required: No

 ** SubnetOutpost **
If the subnet is associated with an Outpost, this value specifies the Outpost.
For more information about RDS on Outposts, see [Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide.*
Type: [Outpost](API_Outpost.md) object
Required: No

 ** SubnetStatus **
The status of the subnet.
Type: String
Required: No

## See Also
<a name="API_Subnet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/Subnet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/Subnet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/Subnet)
