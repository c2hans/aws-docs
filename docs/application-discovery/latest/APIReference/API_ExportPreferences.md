---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ExportPreferences.html
---

# ExportPreferences
<a name="API_ExportPreferences"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 Indicates the type of data that is being exported. Only one `ExportPreferences` can be enabled for a [StartExportTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html) action.

## Contents
<a name="API_ExportPreferences_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ec2RecommendationsPreferences **   <a name="DiscServ-Type-ExportPreferences-ec2RecommendationsPreferences"></a>
 If enabled, exported data includes EC2 instance type matches for on-premises servers discovered through AWS Application Discovery Service.
Type: [Ec2RecommendationsExportPreferences](API_Ec2RecommendationsExportPreferences.md) object
Required: No

## See Also
<a name="API_ExportPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/ExportPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/ExportPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/ExportPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
