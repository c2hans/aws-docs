---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayPolicyTable.html
---

# TransitGatewayPolicyTable
<a name="API_TransitGatewayPolicyTable"></a>

Describes a transit gateway policy table.

## Contents
<a name="API_TransitGatewayPolicyTable_Contents"></a>

 ** creationTime **
The timestamp when the transit gateway policy table was created.
Type: Timestamp
Required: No

 ** state **
The state of the transit gateway policy table
Type: String
Valid Values: `pending | available | deleting | deleted`
Required: No

 ** TagSet.N **
he key-value pairs associated with the transit gateway policy table.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** transitGatewayId **
The ID of the transit gateway.
Type: String
Required: No

 ** transitGatewayPolicyTableId **
The ID of the transit gateway policy table.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayPolicyTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayPolicyTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayPolicyTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayPolicyTable)
