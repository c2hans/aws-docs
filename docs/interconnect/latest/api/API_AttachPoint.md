---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_AttachPoint.html
---

# AttachPoint
<a name="API_AttachPoint"></a>

A generalization of an AWS network location to which a [Connection](API_Connection.md) can be attached.

Currently, the only supported type of AttachPoint is a DirectConnect Gateway.

## Contents
<a name="API_AttachPoint_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** arn **   <a name="interconnect-Type-AttachPoint-arn"></a>
Identifies an attach point by full ARN.
Type: String
Length Constraints: Minimum length of 59. Maximum length of 150.
Pattern: `arn:aws[a-z-]*:interconnect:[^:]+:[0-9]{12}:connection/(mcc|lmcc)-[a-z0-9]{8}`
Required: No

 ** directConnectGateway **   <a name="interconnect-Type-AttachPoint-directConnectGateway"></a>
Identifies an DirectConnect Gateway attach point by DirectConnectGatewayID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

## See Also
<a name="API_AttachPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/AttachPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/AttachPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/AttachPoint)
