---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_PercentOrAbsoluteLong.html
---

# PercentOrAbsoluteLong
<a name="API_PercentOrAbsoluteLong"></a>

Percent or Absolute Long for InfluxDB parameters

## Contents
<a name="API_PercentOrAbsoluteLong_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** absolute **   <a name="tsinfluxdb-Type-PercentOrAbsoluteLong-absolute"></a>
Absolute long for InfluxDB parameters.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1610612736000.
Required: No

 ** percent **   <a name="tsinfluxdb-Type-PercentOrAbsoluteLong-percent"></a>
Percent for InfluxDB parameters.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 4.
Pattern: `(?:100|[1-9]?[0-9])%`
Required: No

## See Also
<a name="API_PercentOrAbsoluteLong_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/PercentOrAbsoluteLong)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/PercentOrAbsoluteLong)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/PercentOrAbsoluteLong)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Timestream for InfluxDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ts-influxdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
