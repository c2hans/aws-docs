---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DropDuplicates.html
---

# DropDuplicates
<a name="API_DropDuplicates"></a>

Specifies a transform that removes rows of repeating data from a data set.

## Contents
<a name="API_DropDuplicates_Contents"></a>

 ** Inputs **   <a name="Glue-Type-DropDuplicates-Inputs"></a>
The data inputs identified by their node names.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-DropDuplicates-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Columns **   <a name="Glue-Type-DropDuplicates-Columns"></a>
The name of the columns to be merged or removed if repeating.
Type: Array of arrays of strings
Pattern: `[A-Za-z0-9_-]*`
Required: No

## See Also
<a name="API_DropDuplicates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DropDuplicates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DropDuplicates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DropDuplicates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
