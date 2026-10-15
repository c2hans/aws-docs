---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CriticalitySource.html
---

# CriticalitySource
<a name="API_CriticalitySource"></a>

Details the source and reason of a criticality.

## Contents
<a name="API_CriticalitySource_Contents"></a>

 ** Reason **   <a name="securityhub-Type-CriticalitySource-Reason"></a>
The reason the criticality was assigned.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Source **   <a name="securityhub-Type-CriticalitySource-Source"></a>
The source of the criticality.
Type: String
Valid Values: `AutomationRule | ResourceName | TagInference`
Required: Yes

## See Also
<a name="API_CriticalitySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CriticalitySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CriticalitySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CriticalitySource)
