---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AutoUpgradeMetadata.html
---

# AutoUpgradeMetadata
<a name="API_AutoUpgradeMetadata"></a>

The auto-upgrade assessment information for a job configured with `GlueVersion=auto`.

## Contents
<a name="API_AutoUpgradeMetadata_Contents"></a>

 ** AnalysisId **   <a name="Glue-Type-AutoUpgradeMetadata-AnalysisId"></a>
The unique identifier of the auto-upgrade assessment analysis.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** SourceVersion **   <a name="Glue-Type-AutoUpgradeMetadata-SourceVersion"></a>
The source AWS Glue runtime version the job was running before auto-version was enabled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

 ** Status **   <a name="Glue-Type-AutoUpgradeMetadata-Status"></a>
The current auto-upgrade lifecycle status (OBSERVING, UPGRADING, UPGRADE\_SUCCEEDED, UPGRADE\_FAILED, STOPPED, WAITING\_FOR\_CONSENT).
Type: String
Valid Values: `OBSERVING | UPGRADING | UPGRADE_SUCCEEDED | UPGRADE_FAILED | STOPPED | WAITING_FOR_CONSENT`
Required: No

 ** TargetVersion **   <a name="Glue-Type-AutoUpgradeMetadata-TargetVersion"></a>
The target AWS Glue runtime version the job is being upgraded to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

## See Also
<a name="API_AutoUpgradeMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AutoUpgradeMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AutoUpgradeMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AutoUpgradeMetadata)
