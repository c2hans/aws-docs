---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AccessPreviewSummary.html
---

# AccessPreviewSummary
<a name="API_AccessPreviewSummary"></a>

Contains a summary of information about an access preview.

## Contents
<a name="API_AccessPreviewSummary_Contents"></a>

 ** analyzerArn **   <a name="accessanalyzer-Type-AccessPreviewSummary-analyzerArn"></a>
The ARN of the analyzer used to generate the access preview.
Type: String
Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`
Required: Yes

 ** createdAt **   <a name="accessanalyzer-Type-AccessPreviewSummary-createdAt"></a>
The time at which the access preview was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="accessanalyzer-Type-AccessPreviewSummary-id"></a>
The unique ID for the access preview.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** status **   <a name="accessanalyzer-Type-AccessPreviewSummary-status"></a>
The status of the access preview.
+  `Creating` - The access preview creation is in progress.
+  `Completed` - The access preview is complete and previews the findings for external access to the resource.
+  `Failed` - The access preview creation has failed.
Type: String
Valid Values: `COMPLETED | CREATING | FAILED`
Required: Yes

 ** statusReason **   <a name="accessanalyzer-Type-AccessPreviewSummary-statusReason"></a>
Provides more details about the current status of the access preview. For example, if the creation of the access preview fails, a `Failed` status is returned. This failure can be due to an internal issue with the analysis or due to an invalid proposed resource configuration.
Type: [AccessPreviewStatusReason](API_AccessPreviewStatusReason.md) object
Required: No

## See Also
<a name="API_AccessPreviewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AccessPreviewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AccessPreviewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AccessPreviewSummary)
