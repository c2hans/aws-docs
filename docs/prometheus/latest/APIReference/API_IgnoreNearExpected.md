---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_IgnoreNearExpected.html
---

# IgnoreNearExpected
<a name="API_IgnoreNearExpected"></a>

Configuration for threshold settings that determine when values near expected values should be ignored during anomaly detection.

## Contents
<a name="API_IgnoreNearExpected_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** amount **   <a name="prometheus-Type-IgnoreNearExpected-amount"></a>
The absolute amount by which values can differ from expected values before being considered anomalous.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** ratio **   <a name="prometheus-Type-IgnoreNearExpected-ratio"></a>
The ratio by which values can differ from expected values before being considered anomalous.
Type: Double
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_IgnoreNearExpected_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/IgnoreNearExpected)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/IgnoreNearExpected)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/IgnoreNearExpected)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
