---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisResponseData.html
---

# EphemerisResponseData
<a name="API_EphemerisResponseData"></a>

Ephemeris data for a contact.

## Contents
<a name="API_EphemerisResponseData_Contents"></a>

 ** ephemerisType **   <a name="groundstation-Type-EphemerisResponseData-ephemerisType"></a>
Type of ephemeris.
Type: String
Valid Values: `TLE | OEM | AZ_EL | SERVICE_MANAGED`
Required: Yes

 ** ephemerisId **   <a name="groundstation-Type-EphemerisResponseData-ephemerisId"></a>
Unique identifier of the ephemeris. Appears only for custom ephemerides.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_EphemerisResponseData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/EphemerisResponseData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/EphemerisResponseData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/EphemerisResponseData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
