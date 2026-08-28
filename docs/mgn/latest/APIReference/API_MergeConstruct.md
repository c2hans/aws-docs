---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_MergeConstruct.html
---

# MergeConstruct
<a name="API_MergeConstruct"></a>

A construct reference specifying the source segment and construct to merge.

## Contents
<a name="API_MergeConstruct_Contents"></a>

 ** constructID **   <a name="mgn-Type-MergeConstruct-constructID"></a>
The construct ID to merge.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** segmentID **   <a name="mgn-Type-MergeConstruct-segmentID"></a>
The segment ID of the construct to merge.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_MergeConstruct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/MergeConstruct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/MergeConstruct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/MergeConstruct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
