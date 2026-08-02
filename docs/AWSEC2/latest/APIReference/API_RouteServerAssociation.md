---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RouteServerAssociation.html
---

# RouteServerAssociation
<a name="API_RouteServerAssociation"></a>

Describes the association between a route server and a VPC.

A route server association is the connection established between a route server and a VPC.

## Contents
<a name="API_RouteServerAssociation_Contents"></a>

 ** routeServerId **
The ID of the associated route server.
Type: String
Required: No

 ** state **
The current state of the association.
Type: String
Valid Values: `associating | associated | disassociating`
Required: No

 ** vpcId **
The ID of the associated VPC.
Type: String
Required: No

## See Also
<a name="API_RouteServerAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RouteServerAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RouteServerAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RouteServerAssociation)
