---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LineageGroupSummary.html
---

# LineageGroupSummary
<a name="API_LineageGroupSummary"></a>

Lists a summary of the properties of a lineage group. A lineage group provides a group of shareable lineage entity resources.

## Contents
<a name="API_LineageGroupSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-LineageGroupSummary-CreationTime"></a>
The creation time of the lineage group summary.
Type: Timestamp
Required: No

 ** DisplayName **   <a name="sagemaker-Type-LineageGroupSummary-DisplayName"></a>
The display name of the lineage group summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-LineageGroupSummary-LastModifiedTime"></a>
The last modified time of the lineage group summary.
Type: Timestamp
Required: No

 ** LineageGroupArn **   <a name="sagemaker-Type-LineageGroupSummary-LineageGroupArn"></a>
The Amazon Resource Name (ARN) of the lineage group resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:lineage-group/.*`
Required: No

 ** LineageGroupName **   <a name="sagemaker-Type-LineageGroupSummary-LineageGroupName"></a>
The name or Amazon Resource Name (ARN) of the lineage group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

## See Also
<a name="API_LineageGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LineageGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LineageGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LineageGroupSummary)
