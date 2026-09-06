---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AccessPreviewStatusReason.html
---

# AccessPreviewStatusReason
<a name="API_AccessPreviewStatusReason"></a>

Provides more details about the current status of the access preview. For example, if the creation of the access preview fails, a `Failed` status is returned. This failure can be due to an internal issue with the analysis or due to an invalid proposed resource configuration.

## Contents
<a name="API_AccessPreviewStatusReason_Contents"></a>

 ** code **   <a name="accessanalyzer-Type-AccessPreviewStatusReason-code"></a>
The reason code for the current status of the access preview.
Type: String
Valid Values: `INTERNAL_ERROR | INVALID_CONFIGURATION`
Required: Yes

## See Also
<a name="API_AccessPreviewStatusReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AccessPreviewStatusReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AccessPreviewStatusReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AccessPreviewStatusReason)
