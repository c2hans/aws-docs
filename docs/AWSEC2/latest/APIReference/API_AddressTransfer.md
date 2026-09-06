---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AddressTransfer.html
---

# AddressTransfer
<a name="API_AddressTransfer"></a>

Details on the Elastic IP address transfer. For more information, see [Transfer Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html#transfer-EIPs-intro) in the *Amazon VPC User Guide*.

## Contents
<a name="API_AddressTransfer_Contents"></a>

 ** addressTransferStatus **
The Elastic IP address transfer status.
Type: String
Valid Values: `pending | disabled | accepted`
Required: No

 ** allocationId **
The allocation ID of an Elastic IP address.
Type: String
Required: No

 ** publicIp **
The Elastic IP address being transferred.
Type: String
Required: No

 ** transferAccountId **
The ID of the account that you want to transfer the Elastic IP address to.
Type: String
Required: No

 ** transferOfferAcceptedTimestamp **
The timestamp when the Elastic IP address transfer was accepted.
Type: Timestamp
Required: No

 ** transferOfferExpirationTimestamp **
The timestamp when the Elastic IP address transfer expired. When the source account starts the transfer, the transfer account has seven hours to allocate the Elastic IP address to complete the transfer, or the Elastic IP address will return to its original owner.
Type: Timestamp
Required: No

## See Also
<a name="API_AddressTransfer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AddressTransfer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AddressTransfer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AddressTransfer)
