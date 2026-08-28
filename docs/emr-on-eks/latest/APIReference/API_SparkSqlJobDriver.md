---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_SparkSqlJobDriver.html
---

# SparkSqlJobDriver
<a name="API_SparkSqlJobDriver"></a>

The job driver for job type.

## Contents
<a name="API_SparkSqlJobDriver_Contents"></a>

 ** entryPoint **   <a name="emroneks-Type-SparkSqlJobDriver-entryPoint"></a>
The SQL file to be executed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** sparkSqlParameters **   <a name="emroneks-Type-SparkSqlJobDriver-sparkSqlParameters"></a>
The Spark parameters to be included in the Spark SQL command.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 102400.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SparkSqlJobDriver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/SparkSqlJobDriver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/SparkSqlJobDriver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/SparkSqlJobDriver)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
