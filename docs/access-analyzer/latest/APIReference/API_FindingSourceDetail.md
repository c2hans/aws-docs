---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingSourceDetail.html
---

# FindingSourceDetail
<a name="API_FindingSourceDetail"></a>

Includes details about how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.

## Contents
<a name="API_FindingSourceDetail_Contents"></a>

 ** accessPointAccount **   <a name="accessanalyzer-Type-FindingSourceDetail-accessPointAccount"></a>
The account of the cross-account access point that generated the finding.
Type: String
Required: No

 ** accessPointArn **   <a name="accessanalyzer-Type-FindingSourceDetail-accessPointArn"></a>
The ARN of the access point that generated the finding. The ARN format depends on whether the ARN represents an access point or a multi-region access point.
Type: String
Required: No

## See Also
<a name="API_FindingSourceDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingSourceDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingSourceDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingSourceDetail)
