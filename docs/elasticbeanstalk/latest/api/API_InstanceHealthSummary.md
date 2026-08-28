---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_InstanceHealthSummary.html
---

# InstanceHealthSummary
<a name="API_InstanceHealthSummary"></a>

Represents summary information about the health of an instance. For more information, see [Health Colors and Statuses](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html).

## Contents
<a name="API_InstanceHealthSummary_Contents"></a>

 ** Degraded **
 **Red.** The health agent is reporting a high number of request failures or other issues for an instance or environment.
Type: Integer
Required: No

 ** Info **
 **Green.** An operation is in progress on an instance.
Type: Integer
Required: No

 ** NoData **
 **Grey.** AWS Elastic Beanstalk and the health agent are reporting no data on an instance.
Type: Integer
Required: No

 ** Ok **
 **Green.** An instance is passing health checks and the health agent is not reporting any problems.
Type: Integer
Required: No

 ** Pending **
 **Grey.** An operation is in progress on an instance within the command timeout.
Type: Integer
Required: No

 ** Severe **
 **Red.** The health agent is reporting a very high number of request failures or other issues for an instance or environment.
Type: Integer
Required: No

 ** Unknown **
 **Grey.** AWS Elastic Beanstalk and the health agent are reporting an insufficient amount of data on an instance.
Type: Integer
Required: No

 ** Warning **
 **Yellow.** The health agent is reporting a moderate number of request failures or other issues for an instance or environment.
Type: Integer
Required: No

## See Also
<a name="API_InstanceHealthSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/InstanceHealthSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/InstanceHealthSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/InstanceHealthSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
