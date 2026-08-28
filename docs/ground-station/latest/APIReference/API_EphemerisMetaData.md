---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisMetaData.html
---

# EphemerisMetaData
<a name="API_EphemerisMetaData"></a>

Metadata describing a particular ephemeris.

## Contents
<a name="API_EphemerisMetaData_Contents"></a>

 ** source **   <a name="groundstation-Type-EphemerisMetaData-source"></a>
The `EphemerisSource` that generated a given ephemeris.
Type: String
Valid Values: `CUSTOMER_PROVIDED | SPACE_TRACK`
Required: Yes

 ** ephemerisId **   <a name="groundstation-Type-EphemerisMetaData-ephemerisId"></a>
UUID of a customer-provided ephemeris.
This field is not populated for default ephemerides from Space Track.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** epoch **   <a name="groundstation-Type-EphemerisMetaData-epoch"></a>
The epoch of a default, ephemeris from Space Track in UTC.
This field is not populated for customer-provided ephemerides.
Type: Timestamp
Required: No

 ** name **   <a name="groundstation-Type-EphemerisMetaData-name"></a>
A name string associated with the ephemeris. Used as a human-readable identifier for the ephemeris.
A name is only returned for customer-provider ephemerides that have a name associated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: No

## See Also
<a name="API_EphemerisMetaData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/EphemerisMetaData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/EphemerisMetaData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/EphemerisMetaData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
