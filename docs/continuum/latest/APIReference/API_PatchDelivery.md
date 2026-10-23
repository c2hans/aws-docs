---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_PatchDelivery.html
---

# PatchDelivery
<a name="API_PatchDelivery"></a>

Delivery of a patch to a destination the customer owns: an object in the environment's source bucket or a pull request in the source repository.

## Contents
<a name="API_PatchDelivery_Contents"></a>

 ** status **   <a name="continuum-Type-PatchDelivery-status"></a>
The current status of the resource.
Type: String
Valid Values: `PENDING | SUCCEEDED | FAILED | SKIPPED | ABANDONED`
Required: Yes

 ** updatedAt **   <a name="continuum-Type-PatchDelivery-updatedAt"></a>
The timestamp when the resource was last updated.
Type: Timestamp
Required: Yes

 ** target **   <a name="continuum-Type-PatchDelivery-target"></a>
The target.
Type: [DestinationTarget](API_DestinationTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_PatchDelivery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/PatchDelivery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/PatchDelivery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/PatchDelivery)
