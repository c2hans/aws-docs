---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_JobError.html
---

# JobError
<a name="API_geojobs_JobError"></a>

Error information for failed jobs.

## Contents
<a name="API_geojobs_JobError_Contents"></a>

 ** Code **   <a name="location-Type-geojobs_JobError-Code"></a>
Error code indicating the type of error that occurred.
Type: String
Valid Values: `ValidationError | InternalServerError`
Required: Yes

 ** Messages **   <a name="location-Type-geojobs_JobError-Messages"></a>
Error messages providing details about the failure.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_geojobs_JobError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geojobs-2020-11-19/JobError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geojobs-2020-11-19/JobError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geojobs-2020-11-19/JobError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
