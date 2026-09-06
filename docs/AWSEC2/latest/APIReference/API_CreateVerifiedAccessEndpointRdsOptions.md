---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVerifiedAccessEndpointRdsOptions.html
---

# CreateVerifiedAccessEndpointRdsOptions
<a name="API_CreateVerifiedAccessEndpointRdsOptions"></a>

Describes the RDS options for a Verified Access endpoint.

## Contents
<a name="API_CreateVerifiedAccessEndpointRdsOptions_Contents"></a>

 ** Port **
The port.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** Protocol **
The protocol.
Type: String
Valid Values: `http | https | tcp`
Required: No

 ** RdsDbClusterArn **
The ARN of the DB cluster.
Type: String
Required: No

 ** RdsDbInstanceArn **
The ARN of the RDS instance.
Type: String
Required: No

 ** RdsDbProxyArn **
The ARN of the RDS proxy.
Type: String
Required: No

 ** RdsEndpoint **
The RDS endpoint.
Type: String
Required: No

 ** SubnetId.N **
The IDs of the subnets. You can specify only one subnet per Availability Zone.
Type: Array of strings
Required: No

## See Also
<a name="API_CreateVerifiedAccessEndpointRdsOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVerifiedAccessEndpointRdsOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVerifiedAccessEndpointRdsOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVerifiedAccessEndpointRdsOptions)
