---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnablementStatusSummary.html
---

# EnablementStatusSummary
<a name="API_EnablementStatusSummary"></a>

The deployment summary of an `EnabledControl` or `EnabledBaseline` resource.

## Contents
<a name="API_EnablementStatusSummary_Contents"></a>

 ** lastOperationIdentifier **   <a name="controltower-Type-EnablementStatusSummary-lastOperationIdentifier"></a>
The last operation identifier for the enabled resource.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** status **   <a name="controltower-Type-EnablementStatusSummary-status"></a>
 The deployment status of the enabled resource.
Valid values:
+  `SUCCEEDED`: The `EnabledControl` or `EnabledBaseline` configuration was deployed successfully.
+  `UNDER_CHANGE`: The `EnabledControl` or `EnabledBaseline` configuration is changing.
+  `FAILED`: The `EnabledControl` or `EnabledBaseline` configuration failed to deploy.
Type: String
Valid Values: `SUCCEEDED | FAILED | UNDER_CHANGE`
Required: No

## See Also
<a name="API_EnablementStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnablementStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnablementStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnablementStatusSummary)
