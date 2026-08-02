---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_PerformanceTarget.html
---

# PerformanceTarget
<a name="API_PerformanceTarget"></a>

An object that represents the price performance target settings for the workgroup.

## Contents
<a name="API_PerformanceTarget_Contents"></a>

 ** level **   <a name="redshiftserverless-Type-PerformanceTarget-level"></a>
The target price performance level for the workgroup. Valid values include 1, 25, 50, 75, and 100. These correspond to the price performance levels LOW\_COST, ECONOMICAL, BALANCED, RESOURCEFUL, and HIGH\_PERFORMANCE.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** status **   <a name="redshiftserverless-Type-PerformanceTarget-status"></a>
Whether the price performance target is enabled for the workgroup.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_PerformanceTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/PerformanceTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/PerformanceTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/PerformanceTarget)
