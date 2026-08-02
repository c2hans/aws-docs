---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessEndpointRdsOptions.html
---

# VerifiedAccessEndpointRdsOptions
<a name="API_VerifiedAccessEndpointRdsOptions"></a>

Describes the RDS options for a Verified Access endpoint.

## Contents
<a name="API_VerifiedAccessEndpointRdsOptions_Contents"></a>

 ** port **
The port.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** protocol **
The protocol.
Type: String
Valid Values: `http | https | tcp`
Required: No

 ** rdsDbClusterArn **
The ARN of the DB cluster.
Type: String
Required: No

 ** rdsDbInstanceArn **
The ARN of the RDS instance.
Type: String
Required: No

 ** rdsDbProxyArn **
The ARN of the RDS proxy.
Type: String
Required: No

 ** rdsEndpoint **
The RDS endpoint.
Type: String
Required: No

 ** SubnetIdSet.N **
The IDs of the subnets.
Type: Array of strings
Required: No

## See Also
<a name="API_VerifiedAccessEndpointRdsOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessEndpointRdsOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessEndpointRdsOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessEndpointRdsOptions)
