---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchDeleteByResourceArns.html
---

# BatchDeleteByResourceArns
<a name="API_BatchDeleteByResourceArns"></a>

Parameters for targeted delete by ARN list.

## Contents
<a name="API_BatchDeleteByResourceArns_Contents"></a>

 ** InstrumentationType **   <a name="applicationsignals-Type-BatchDeleteByResourceArns-InstrumentationType"></a>
The instrumentation type: `BREAKPOINT` or `PROBE`.
Type: String
Valid Values: `BREAKPOINT | PROBE`
Required: Yes

 ** ResourceArns **   <a name="applicationsignals-Type-BatchDeleteByResourceArns-ResourceArns"></a>
The list of resource ARNs to delete.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_BatchDeleteByResourceArns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/BatchDeleteByResourceArns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/BatchDeleteByResourceArns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/BatchDeleteByResourceArns)
