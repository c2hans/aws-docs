---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AccessPreview.html
---

# AccessPreview
<a name="API_AccessPreview"></a>

Contains information about an access preview.

## Contents
<a name="API_AccessPreview_Contents"></a>

 ** analyzerArn **   <a name="accessanalyzer-Type-AccessPreview-analyzerArn"></a>
The ARN of the analyzer used to generate the access preview.
Type: String
Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`
Required: Yes

 ** configurations **   <a name="accessanalyzer-Type-AccessPreview-configurations"></a>
A map of resource ARNs for the proposed resource configuration.
Type: String to [Configuration](API_Configuration.md) object map
Required: Yes

 ** createdAt **   <a name="accessanalyzer-Type-AccessPreview-createdAt"></a>
The time at which the access preview was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="accessanalyzer-Type-AccessPreview-id"></a>
The unique ID for the access preview.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** status **   <a name="accessanalyzer-Type-AccessPreview-status"></a>
The status of the access preview.
+  `Creating` - The access preview creation is in progress.
+  `Completed` - The access preview is complete. You can preview findings for external access to the resource.
+  `Failed` - The access preview creation has failed.
Type: String
Valid Values: `COMPLETED | CREATING | FAILED`
Required: Yes

 ** statusReason **   <a name="accessanalyzer-Type-AccessPreview-statusReason"></a>
Provides more details about the current status of the access preview.
For example, if the creation of the access preview fails, a `Failed` status is returned. This failure can be due to an internal issue with the analysis or due to an invalid resource configuration.
Type: [AccessPreviewStatusReason](API_AccessPreviewStatusReason.md) object
Required: No

## See Also
<a name="API_AccessPreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AccessPreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AccessPreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AccessPreview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
