---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_CodeScanSummary.html
---

# CodeScanSummary
<a name="API_CodeScanSummary"></a>

The code Scan Summary.

## Contents
<a name="API_CodeScanSummary_Contents"></a>

 ** createdAt **   <a name="continuum-Type-CodeScanSummary-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp
Required: Yes

 ** origin **   <a name="continuum-Type-CodeScanSummary-origin"></a>
The origin.
Type: String
Valid Values: `MANUAL | SCHEDULED`
Required: Yes

 ** scanRunId **   <a name="continuum-Type-CodeScanSummary-scanRunId"></a>
The identifier of the scan Run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** status **   <a name="continuum-Type-CodeScanSummary-status"></a>
The current status of the resource.
Type: String
Valid Values: `SUBMITTED | WAITING_FOR_BUILD | BUILDING | WAITING_FOR_SCAN | SCANNING | SUCCEEDED | FAILED`
Required: Yes

 ** completedAt **   <a name="continuum-Type-CodeScanSummary-completedAt"></a>
The completed At.
Type: Timestamp
Required: No

 ** failureMessage **   <a name="continuum-Type-CodeScanSummary-failureMessage"></a>
The failure Message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** failureStage **   <a name="continuum-Type-CodeScanSummary-failureStage"></a>
The failure Stage.
Type: String
Valid Values: `SUBMITTED | WAITING_FOR_BUILD | BUILDING | WAITING_FOR_SCAN | SCANNING`
Required: No

## See Also
<a name="API_CodeScanSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/CodeScanSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/CodeScanSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/CodeScanSummary)
