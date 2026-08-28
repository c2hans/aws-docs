---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_Ec2RecommendationsExportPreferences.html
---

# Ec2RecommendationsExportPreferences
<a name="API_Ec2RecommendationsExportPreferences"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 Indicates that the exported data must include EC2 instance type matches for on-premises servers that are discovered through AWS Application Discovery Service.

## Contents
<a name="API_Ec2RecommendationsExportPreferences_Contents"></a>

 ** cpuPerformanceMetricBasis **   <a name="DiscServ-Type-Ec2RecommendationsExportPreferences-cpuPerformanceMetricBasis"></a>
 The recommended EC2 instance type that matches the CPU usage metric of server performance data.
Type: [UsageMetricBasis](API_UsageMetricBasis.md) object
Required: No

 ** enabled **   <a name="DiscServ-Type-Ec2RecommendationsExportPreferences-enabled"></a>
 If set to true, the export [preferences](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html#API_StartExportTask_RequestSyntax) is set to `Ec2RecommendationsExportPreferences`.
Type: Boolean
Required: No

 ** excludedInstanceTypes **   <a name="DiscServ-Type-Ec2RecommendationsExportPreferences-excludedInstanceTypes"></a>
An array of instance types and families to exclude from recommendations. The following is an example: `["m5.4xlarge", "r3.large", "t3"]`
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `[a-zA-Z0-9\d\.\-]+`
Required: No

 ** preferredRegion **   <a name="DiscServ-Type-Ec2RecommendationsExportPreferences-preferredRegion"></a>
 The target AWS Region for the recommendations. You can use any of the Region codes available for the chosen service, as listed in [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-z]{2}-[a-z\-]+-[0-9]+`
Required: No

 ** ramPerformanceMetricBasis **   <a name="DiscServ-Type-Ec2RecommendationsExportPreferences-ramPerformanceMetricBasis"></a>
 The recommended EC2 instance type that matches the Memory usage metric of server performance data.
Type: [UsageMetricBasis](API_UsageMetricBasis.md) object
Required: No

 ** reservedInstanceOptions **   <a name="DiscServ-Type-Ec2RecommendationsExportPreferences-reservedInstanceOptions"></a>
 The contract type for a reserved instance. If blank, we assume an On-Demand instance is preferred.
Type: [ReservedInstanceOptions](API_ReservedInstanceOptions.md) object
Required: No

 ** tenancy **   <a name="DiscServ-Type-Ec2RecommendationsExportPreferences-tenancy"></a>
 The target tenancy to use for your recommended EC2 instances.
Type: String
Valid Values: `DEDICATED | SHARED`
Required: No

## See Also
<a name="API_Ec2RecommendationsExportPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/Ec2RecommendationsExportPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/Ec2RecommendationsExportPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/Ec2RecommendationsExportPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
