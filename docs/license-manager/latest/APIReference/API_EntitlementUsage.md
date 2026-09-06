---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_EntitlementUsage.html
---

# EntitlementUsage
<a name="API_EntitlementUsage"></a>

Usage associated with an entitlement resource.

## Contents
<a name="API_EntitlementUsage_Contents"></a>

 ** ConsumedValue **   <a name="licensemanager-Type-EntitlementUsage-ConsumedValue"></a>
Resource usage consumed.
Type: String
Required: Yes

 ** Name **   <a name="licensemanager-Type-EntitlementUsage-Name"></a>
Entitlement usage name.
Type: String
Required: Yes

 ** Unit **   <a name="licensemanager-Type-EntitlementUsage-Unit"></a>
Entitlement usage unit.
Type: String
Valid Values: `Count | None | Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second`
Required: Yes

 ** MaxCount **   <a name="licensemanager-Type-EntitlementUsage-MaxCount"></a>
Maximum entitlement usage count.
Type: String
Required: No

## See Also
<a name="API_EntitlementUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/EntitlementUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/EntitlementUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/EntitlementUsage)
