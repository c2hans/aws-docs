---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_Location.html
---

# Location
<a name="API_Location"></a>

Returns information about the location of a change or comment in the comparison between two commits or a pull request.

## Contents
<a name="API_Location_Contents"></a>

 ** filePath **   <a name="CodeCommit-Type-Location-filePath"></a>
The name of the file being compared, including its extension and subdirectory, if any.
Type: String
Required: No

 ** filePosition **   <a name="CodeCommit-Type-Location-filePosition"></a>
The position of a change in a compared file, in line number format.
Type: Long
Required: No

 ** relativeFileVersion **   <a name="CodeCommit-Type-Location-relativeFileVersion"></a>
In a comparison of commits or a pull request, whether the change is in the before or after of that comparison.
Type: String
Valid Values: `BEFORE | AFTER`
Required: No

## See Also
<a name="API_Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/Location)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
