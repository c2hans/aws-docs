---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TLEData.html
---

# TLEData
<a name="API_TLEData"></a>

Two-line element set (TLE) data.

## Contents
<a name="API_TLEData_Contents"></a>

 ** tleLine1 **   <a name="groundstation-Type-TLEData-tleLine1"></a>
First line of two-line element set (TLE) data.
Type: String
Length Constraints: Fixed length of 69.
Pattern: `1 [ 0-9A-HJ-NP-Z][ 0-9]{4}[A-Z] [ 0-9]{5}[ A-Z]{3} [ 0-9]{5}[.][ 0-9]{8} (?:(?:[ 0+-][.][ 0-9]{8})|(?: [ +-][.][ 0-9]{7})) [ +-][ 0-9]{5}[+-][ 0-9] [ +-][ 0-9]{5}[+-][ 0-9] [ 0-9] [ 0-9]{4}[ 0-9]`
Required: Yes

 ** tleLine2 **   <a name="groundstation-Type-TLEData-tleLine2"></a>
Second line of two-line element set (TLE) data.
Type: String
Length Constraints: Fixed length of 69.
Pattern: `2 [ 0-9A-HJ-NP-Z][ 0-9]{4} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{7} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{2}[.][ 0-9]{13}[ 0-9]`
Required: Yes

 ** validTimeRange **   <a name="groundstation-Type-TLEData-validTimeRange"></a>
The valid time range for the TLE. Time ranges must be continuous without gaps or overlaps.
Type: [TimeRange](API_TimeRange.md) object
Required: Yes

## See Also
<a name="API_TLEData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/TLEData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/TLEData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/TLEData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
