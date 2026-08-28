---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_JobSample.html
---

# JobSample
<a name="API_JobSample"></a>

A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run. If a `JobSample` value isn't provided, the default is used. The default value is CUSTOM\_ROWS for the mode parameter and 20,000 for the size parameter.

## Contents
<a name="API_JobSample_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Mode **   <a name="databrew-Type-JobSample-Mode"></a>
A value that determines whether the profile job is run on the entire dataset or a specified number of rows. This value must be one of the following:
+ FULL\_DATASET - The profile job is run on the entire dataset.
+ CUSTOM\_ROWS - The profile job is run on the number of rows specified in the `Size` parameter.
Type: String
Valid Values: `FULL_DATASET | CUSTOM_ROWS`
Required: No

 ** Size **   <a name="databrew-Type-JobSample-Size"></a>
The `Size` parameter is only required when the mode is CUSTOM\_ROWS. The profile job is run on the specified number of rows. The maximum value for size is Long.MAX\_VALUE.
Long.MAX\_VALUE = 9223372036854775807
Type: Long
Required: No

## See Also
<a name="API_JobSample_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/JobSample)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/JobSample)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/JobSample)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
