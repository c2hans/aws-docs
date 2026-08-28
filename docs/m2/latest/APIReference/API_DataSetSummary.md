---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_DataSetSummary.html
---

# DataSetSummary
<a name="API_DataSetSummary"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

A subset of the possible data set attributes.

## Contents
<a name="API_DataSetSummary_Contents"></a>

 ** dataSetName **   <a name="m2-Type-DataSetSummary-dataSetName"></a>
The name of the data set.
Type: String
Pattern: `\S{1,200}`
Required: Yes

 ** creationTime **   <a name="m2-Type-DataSetSummary-creationTime"></a>
The timestamp when the data set was created.
Type: Timestamp
Required: No

 ** dataSetOrg **   <a name="m2-Type-DataSetSummary-dataSetOrg"></a>
The type of data set. The only supported value is VSAM.
Type: String
Pattern: `\S{1,20}`
Required: No

 ** format **   <a name="m2-Type-DataSetSummary-format"></a>
The format of the data set.
Type: String
Pattern: `\S{1,20}`
Required: No

 ** lastReferencedTime **   <a name="m2-Type-DataSetSummary-lastReferencedTime"></a>
The last time the data set was referenced.
Type: Timestamp
Required: No

 ** lastUpdatedTime **   <a name="m2-Type-DataSetSummary-lastUpdatedTime"></a>
The last time the data set was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DataSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/DataSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/DataSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/DataSetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
