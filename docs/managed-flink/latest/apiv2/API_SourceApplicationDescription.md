---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SourceApplicationDescription.html
---

# SourceApplicationDescription
<a name="API_SourceApplicationDescription"></a>

Describes the application that an enhanced snapshot was created from.

## Contents
<a name="API_SourceApplicationDescription_Contents"></a>

 ** ApplicationCreationTimestamp **   <a name="APIReference-Type-SourceApplicationDescription-ApplicationCreationTimestamp"></a>
The timestamp that indicates when the source application was created.
Type: Timestamp
Required: Yes

 ** ApplicationName **   <a name="APIReference-Type-SourceApplicationDescription-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** ApplicationVersionId **   <a name="APIReference-Type-SourceApplicationDescription-ApplicationVersionId"></a>
The version ID of the source application when the snapshot was created.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

## See Also
<a name="API_SourceApplicationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SourceApplicationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SourceApplicationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SourceApplicationDescription)
