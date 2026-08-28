---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CollectorHealthCheck.html
---

# CollectorHealthCheck
<a name="API_CollectorHealthCheck"></a>

Describes the last Fleet Advisor collector health check.

## Contents
<a name="API_CollectorHealthCheck_Contents"></a>

 ** CollectorStatus **   <a name="DMS-Type-CollectorHealthCheck-CollectorStatus"></a>
The status of the Fleet Advisor collector.
Type: String
Valid Values: `UNREGISTERED | ACTIVE`
Required: No

 ** LocalCollectorS3Access **   <a name="DMS-Type-CollectorHealthCheck-LocalCollectorS3Access"></a>
Whether the local collector can access its Amazon S3 bucket.
Type: Boolean
Required: No

 ** WebCollectorGrantedRoleBasedAccess **   <a name="DMS-Type-CollectorHealthCheck-WebCollectorGrantedRoleBasedAccess"></a>
Whether the role that you provided when creating the Fleet Advisor collector has sufficient permissions to access the Fleet Advisor web collector.
Type: Boolean
Required: No

 ** WebCollectorS3Access **   <a name="DMS-Type-CollectorHealthCheck-WebCollectorS3Access"></a>
Whether the web collector can access its Amazon S3 bucket.
Type: Boolean
Required: No

## See Also
<a name="API_CollectorHealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CollectorHealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CollectorHealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CollectorHealthCheck)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
