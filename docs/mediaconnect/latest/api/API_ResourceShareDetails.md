---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ResourceShareDetails.html
---

# ResourceShareDetails
<a name="API_ResourceShareDetails"></a>

The cross-account sharing details for an endpoint. Endpoints are shared through AWS Resource Access Manager (AWS RAM). This is a union type, so exactly one of its members is set: `owned` when this account owns the endpoint and shares it with other accounts, or `consumed` when this account consumes an endpoint that another account shares. To change how an endpoint is shared, use AWS RAM.

## Contents
<a name="API_ResourceShareDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** consumed **   <a name="mediaconnect-Type-ResourceShareDetails-consumed"></a>
The sharing details for an endpoint that another account shares with this account through AWS RAM.
Type: [ConsumedResourceShareDetails](API_ConsumedResourceShareDetails.md) object
Required: No

 ** owned **   <a name="mediaconnect-Type-ResourceShareDetails-owned"></a>
The sharing details for an endpoint that this account owns and shares with other accounts through AWS RAM.
Type: [OwnedResourceShareDetails](API_OwnedResourceShareDetails.md) object
Required: No

## See Also
<a name="API_ResourceShareDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ResourceShareDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ResourceShareDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ResourceShareDetails)
