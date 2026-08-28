---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_AnomalySourceMetadata.html
---

# AnomalySourceMetadata
<a name="API_AnomalySourceMetadata"></a>

Metadata about the detection source that generates proactive anomalies. The anomaly is detected using analysis of the metric data  over a period of time

## Contents
<a name="API_AnomalySourceMetadata_Contents"></a>

 ** Source **   <a name="DevOpsGuru-Type-AnomalySourceMetadata-Source"></a>
The source of the anomaly.
Type: String
Required: No

 ** SourceResourceName **   <a name="DevOpsGuru-Type-AnomalySourceMetadata-SourceResourceName"></a>
The name of the anomaly's resource.
Type: String
Required: No

 ** SourceResourceType **   <a name="DevOpsGuru-Type-AnomalySourceMetadata-SourceResourceType"></a>
The anomaly's resource type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z]+[a-zA-Z0-9-_:]*$`
Required: No

## See Also
<a name="API_AnomalySourceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/AnomalySourceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/AnomalySourceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/AnomalySourceMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
