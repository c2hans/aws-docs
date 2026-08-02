---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_AddOnRequest.html
---

# AddOnRequest
<a name="API_AddOnRequest"></a>

Describes a request to enable, modify, or disable an add-on for an Amazon Lightsail resource.

**Note**
An additional cost may be associated with enabling add-ons. For more information, see the [Lightsail pricing page](https://aws.amazon.com/lightsail/pricing/).

## Contents
<a name="API_AddOnRequest_Contents"></a>

 ** addOnType **   <a name="Lightsail-Type-AddOnRequest-addOnType"></a>
The add-on type.
Type: String
Valid Values: `AutoSnapshot | StopInstanceOnIdle`
Required: Yes

 ** autoSnapshotAddOnRequest **   <a name="Lightsail-Type-AddOnRequest-autoSnapshotAddOnRequest"></a>
An object that represents additional parameters when enabling or modifying the automatic snapshot add-on.
Type: [AutoSnapshotAddOnRequest](API_AutoSnapshotAddOnRequest.md) object
Required: No

 ** stopInstanceOnIdleRequest **   <a name="Lightsail-Type-AddOnRequest-stopInstanceOnIdleRequest"></a>
An object that represents additional parameters when enabling or modifying the `StopInstanceOnIdle` add-on.
This object only applies to Lightsail for Research resources.
Type: [StopInstanceOnIdleRequest](API_StopInstanceOnIdleRequest.md) object
Required: No

## See Also
<a name="API_AddOnRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/AddOnRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/AddOnRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/AddOnRequest)
