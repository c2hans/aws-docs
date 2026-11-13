---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_AuditMergeMetadata.html
---

# AuditMergeMetadata
<a name="API_connect-cases_AuditMergeMetadata"></a>

Information about the merge that produced an audit event.

## Contents
<a name="API_connect-cases_AuditMergeMetadata_Contents"></a>

 ** mergeEventId **   <a name="connect-Type-connect-cases_AuditMergeMetadata-mergeEventId"></a>
The unique identifier of the merge. All audit events produced by the same merge, on both cases, have the same value. Use it to group the changes that a merge made.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** primaryCaseId **   <a name="connect-Type-connect-cases_AuditMergeMetadata-primaryCaseId"></a>
The unique identifier of the primary case of the merge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`
Required: Yes

 ** secondaryCaseId **   <a name="connect-Type-connect-cases_AuditMergeMetadata-secondaryCaseId"></a>
The unique identifier of the secondary case of the merge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`
Required: Yes

## See Also
<a name="API_connect-cases_AuditMergeMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/AuditMergeMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/AuditMergeMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/AuditMergeMetadata)
