---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateTarget.html
---

# UpdateTarget

What an update targeted.

## Contents
<a name="API_UpdateTarget_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** gateway **   <a name="rtbfabric-Type-UpdateTarget-gateway"></a>
The gateway itself.
Type: Structure
Required: No

 ** link **   <a name="rtbfabric-Type-UpdateTarget-link"></a>
A link on the gateway.
Type: [LinkTarget](API_LinkTarget.md) object
Required: No

 ** routingRule **   <a name="rtbfabric-Type-UpdateTarget-routingRule"></a>
A routing rule on one of the gateway's links.
Type: [RoutingRuleTarget](API_RoutingRuleTarget.md) object
Required: No

## See Also
<a name="API_UpdateTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/UpdateTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/UpdateTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/UpdateTarget)
