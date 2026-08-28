---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_PathOptions.html
---

# PathOptions
<a name="API_PathOptions"></a>

Represents a set of options that define how DataBrew selects files for a given Amazon S3 path in a dataset.

## Contents
<a name="API_PathOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilesLimit **   <a name="databrew-Type-PathOptions-FilesLimit"></a>
If provided, this structure imposes a limit on a number of files that should be selected.
Type: [FilesLimit](API_FilesLimit.md) object
Required: No

 ** LastModifiedDateCondition **   <a name="databrew-Type-PathOptions-LastModifiedDateCondition"></a>
If provided, this structure defines a date range for matching Amazon S3 objects based on their LastModifiedDate attribute in Amazon S3.
Type: [FilterExpression](API_FilterExpression.md) object
Required: No

 ** Parameters **   <a name="databrew-Type-PathOptions-Parameters"></a>
A structure that maps names of parameters used in the Amazon S3 path of a dataset to their definitions.
Type: String to [DatasetParameter](API_DatasetParameter.md) object map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_PathOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/PathOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/PathOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/PathOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
