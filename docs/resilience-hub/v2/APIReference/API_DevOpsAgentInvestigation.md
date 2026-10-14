---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DevOpsAgentInvestigation.html
---

# DevOpsAgentInvestigation
<a name="API_DevOpsAgentInvestigation"></a>

The result when DevOps Agent investigates a resilience test run. The verdict is advisory and builds on the test run's own result, which remains authoritative.

## Contents
<a name="API_DevOpsAgentInvestigation_Contents"></a>

 ** confidence **   <a name="ngresiliencehub-Type-DevOpsAgentInvestigation-confidence"></a>
The confidence level of the verdict. Valid values:
+ HIGH - The verdict is highly reliable.
+ MEDIUM - The verdict has moderate reliability.
+ LOW - The verdict has low reliability.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: No

 ** deepLink **   <a name="ngresiliencehub-Type-DevOpsAgentInvestigation-deepLink"></a>
A deep link to the interactive DevOps Agent investigation session.
Type: String
Required: No

 ** status **   <a name="ngresiliencehub-Type-DevOpsAgentInvestigation-status"></a>
The lifecycle status of the investigation. Valid values:
+ PENDING - The investigation has been created but has not started.
+ IN\_PROGRESS - The investigation is running.
+ COMPLETED - The investigation finished successfully.
+ FAILED - The investigation failed to complete.
+ TIMED\_OUT - The investigation did not complete within the allotted time.
+ CANCELED - The investigation was canceled.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | TIMED_OUT | CANCELED`
Required: No

 ** summary **   <a name="ngresiliencehub-Type-DevOpsAgentInvestigation-summary"></a>
The DevOps Agent analysis summary for the investigation.
Type: String
Required: No

 ** verdict **   <a name="ngresiliencehub-Type-DevOpsAgentInvestigation-verdict"></a>
The investigation verdict. Valid values:
+ PASS - The resilience test run passed.
+ FAIL - The resilience test run failed.
+ INCONCLUSIVE - The investigation could not determine a clear outcome.
Type: String
Valid Values: `PASS | FAIL`
Required: No

## See Also
<a name="API_DevOpsAgentInvestigation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/DevOpsAgentInvestigation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/DevOpsAgentInvestigation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/DevOpsAgentInvestigation)
