---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GlobalAuroraConfiguration.html
---

# GlobalAuroraConfiguration
<a name="API_GlobalAuroraConfiguration"></a>

Configuration for Amazon Aurora global databases used in a Region switch plan.

## Contents
<a name="API_GlobalAuroraConfiguration_Contents"></a>

 ** behavior **   <a name="regionswitch-Type-GlobalAuroraConfiguration-behavior"></a>
The behavior for a global database, that is, only allow switchover or also allow failover.
Type: String
Valid Values: `switchoverOnly | failover`
Required: Yes

 ** databaseClusterArns **   <a name="regionswitch-Type-GlobalAuroraConfiguration-databaseClusterArns"></a>
The database cluster Amazon Resource Names (ARNs) for a global database.
Type: Array of strings
Pattern: `arn:aws[a-zA-Z-]*:rds:[a-z0-9-]+:\d{12}:cluster:[A-Za-z][0-9A-Za-z-:._]*`
Required: Yes

 ** globalClusterIdentifier **   <a name="regionswitch-Type-GlobalAuroraConfiguration-globalClusterIdentifier"></a>
The global cluster identifier for a global database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: Yes

 ** crossAccountRole **   <a name="regionswitch-Type-GlobalAuroraConfiguration-crossAccountRole"></a>
The cross account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-GlobalAuroraConfiguration-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

 ** timeoutMinutes **   <a name="regionswitch-Type-GlobalAuroraConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ungraceful **   <a name="regionswitch-Type-GlobalAuroraConfiguration-ungraceful"></a>
The settings for ungraceful execution.
Type: [GlobalAuroraUngraceful](API_GlobalAuroraUngraceful.md) object
Required: No

## See Also
<a name="API_GlobalAuroraConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/GlobalAuroraConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/GlobalAuroraConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/GlobalAuroraConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
