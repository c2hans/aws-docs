---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingSource.html
---

# FindingSource
<a name="API_FindingSource"></a>

The source of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

## Contents
<a name="API_FindingSource_Contents"></a>

 ** type **   <a name="accessanalyzer-Type-FindingSource-type"></a>
Indicates the type of access that generated the finding.
Type: String
Valid Values: `POLICY | BUCKET_ACL | S3_ACCESS_POINT | S3_ACCESS_POINT_ACCOUNT`
Required: Yes

 ** detail **   <a name="accessanalyzer-Type-FindingSource-detail"></a>
Includes details about how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.
Type: [FindingSourceDetail](API_FindingSourceDetail.md) object
Required: No

## See Also
<a name="API_FindingSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingSource)
