---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_JobDriver.html
---

# JobDriver
<a name="API_JobDriver"></a>

Specify the driver that the job runs on. Exactly one of the two available job drivers is required, either sparkSqlJobDriver or sparkSubmitJobDriver.

## Contents
<a name="API_JobDriver_Contents"></a>

 ** sparkSqlJobDriver **   <a name="emroneks-Type-JobDriver-sparkSqlJobDriver"></a>
The job driver for job type.
Type: [SparkSqlJobDriver](API_SparkSqlJobDriver.md) object
Required: No

 ** sparkSubmitJobDriver **   <a name="emroneks-Type-JobDriver-sparkSubmitJobDriver"></a>
The job driver parameters specified for spark submit.
Type: [SparkSubmitJobDriver](API_SparkSubmitJobDriver.md) object
Required: No

## See Also
<a name="API_JobDriver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/JobDriver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/JobDriver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/JobDriver)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
