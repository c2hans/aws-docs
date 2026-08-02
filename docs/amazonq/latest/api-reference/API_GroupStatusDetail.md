---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GroupStatusDetail.html
---

# GroupStatusDetail
<a name="API_GroupStatusDetail"></a>

Provides the details of a group's status.

## Contents
<a name="API_GroupStatusDetail_Contents"></a>

 ** errorDetail **   <a name="qbusiness-Type-GroupStatusDetail-errorDetail"></a>
The details of an error associated a group status.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** lastUpdatedAt **   <a name="qbusiness-Type-GroupStatusDetail-lastUpdatedAt"></a>
The Unix timestamp when the Amazon Q Business application was last updated.
Type: Timestamp
Required: No

 ** status **   <a name="qbusiness-Type-GroupStatusDetail-status"></a>
The status of a group.
Type: String
Valid Values: `FAILED | SUCCEEDED | PROCESSING | DELETING | DELETED`
Required: No

## See Also
<a name="API_GroupStatusDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/GroupStatusDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/GroupStatusDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/GroupStatusDetail)
