---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_AuroraProvisionedScalingConfiguration.html
---

# AuroraProvisionedScalingConfiguration
<a name="API_AuroraProvisionedScalingConfiguration"></a>

Configuration for Amazon Aurora provisioned cluster scaling used in a Region switch plan.

## Contents
<a name="API_AuroraProvisionedScalingConfiguration_Contents"></a>

 ** globalClusterIdentifier **   <a name="regionswitch-Type-AuroraProvisionedScalingConfiguration-globalClusterIdentifier"></a>
The global cluster identifier for a global database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: Yes

 ** instanceArns **   <a name="regionswitch-Type-AuroraProvisionedScalingConfiguration-instanceArns"></a>
Per-Region configuration that maps each Region to the Aurora database instance ARN for scaling.
Type: String to string map
Map Entries: Maximum number of 2 items.
Key Pattern: `[a-z]{2}-[a-z-]+-\d+`
Value Pattern: `arn:aws[a-zA-Z-]*:rds:[a-z0-9-]+:\d{12}:db:[A-Za-z][0-9A-Za-z-]{0,62}`
Required: Yes

 ** regionDatabaseClusterArns **   <a name="regionswitch-Type-AuroraProvisionedScalingConfiguration-regionDatabaseClusterArns"></a>
Per-Region configuration that maps each Region to the Aurora database cluster ARN for scaling.
Type: String to string map
Map Entries: Fixed number of 2 items.
Key Pattern: `[a-z]{2}-[a-z-]+-\d+`
Value Pattern: `arn:aws[a-zA-Z-]*:rds:[a-z0-9-]+:\d{12}:cluster:[A-Za-z][0-9A-Za-z-:._]*`
Required: Yes

 ** crossAccountRole **   <a name="regionswitch-Type-AuroraProvisionedScalingConfiguration-crossAccountRole"></a>
The cross account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-AuroraProvisionedScalingConfiguration-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

 ** timeoutMinutes **   <a name="regionswitch-Type-AuroraProvisionedScalingConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_AuroraProvisionedScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/AuroraProvisionedScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/AuroraProvisionedScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/AuroraProvisionedScalingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
