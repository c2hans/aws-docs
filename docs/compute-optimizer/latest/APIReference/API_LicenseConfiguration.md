---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LicenseConfiguration.html
---

# LicenseConfiguration
<a name="API_LicenseConfiguration"></a>

 Describes the configuration of a license for an Amazon EC2 instance.

## Contents
<a name="API_LicenseConfiguration_Contents"></a>

 ** instanceType **   <a name="computeoptimizer-Type-LicenseConfiguration-instanceType"></a>
 The instance type used in the license.
Type: String
Required: No

 ** licenseEdition **   <a name="computeoptimizer-Type-LicenseConfiguration-licenseEdition"></a>
 The edition of the license for the application that runs on the instance.
Type: String
Valid Values: `Enterprise | Standard | Free | NoLicenseEditionFound`
Required: No

 ** licenseModel **   <a name="computeoptimizer-Type-LicenseConfiguration-licenseModel"></a>
 The license type associated with the instance.
Type: String
Valid Values: `LicenseIncluded | BringYourOwnLicense`
Required: No

 ** licenseName **   <a name="computeoptimizer-Type-LicenseConfiguration-licenseName"></a>
 The name of the license for the application that runs on the instance.
Type: String
Valid Values: `SQLServer`
Required: No

 ** licenseVersion **   <a name="computeoptimizer-Type-LicenseConfiguration-licenseVersion"></a>
 The version of the license for the application that runs on the instance.
Type: String
Required: No

 ** metricsSource **   <a name="computeoptimizer-Type-LicenseConfiguration-metricsSource"></a>
 The list of metric sources required to generate recommendations for commercial software licenses.
Type: Array of [MetricSource](API_MetricSource.md) objects
Required: No

 ** numberOfCores **   <a name="computeoptimizer-Type-LicenseConfiguration-numberOfCores"></a>
 The current number of cores associated with the instance.
Type: Integer
Required: No

 ** operatingSystem **   <a name="computeoptimizer-Type-LicenseConfiguration-operatingSystem"></a>
 The operating system of the instance.
Type: String
Required: No

## See Also
<a name="API_LicenseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/LicenseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/LicenseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/LicenseConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
