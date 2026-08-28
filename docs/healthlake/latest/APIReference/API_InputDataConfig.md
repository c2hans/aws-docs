---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_InputDataConfig.html
---

# InputDataConfig
<a name="API_InputDataConfig"></a>

 The import job input properties.

## Contents
<a name="API_InputDataConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** S3Uri **   <a name="HealthLake-Type-InputDataConfig-S3Uri"></a>
The `S3Uri` is the user-specified Amazon S3 location of the FHIR data to be imported into AWS HealthLake.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: No

## See Also
<a name="API_InputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/InputDataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/InputDataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/InputDataConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
