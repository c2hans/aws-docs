---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_OEMEphemeris.html
---

# OEMEphemeris
<a name="API_OEMEphemeris"></a>

Ephemeris data in Orbit Ephemeris Message (OEM) format.

 AWS Ground Station processes OEM ephemerides according to the [CCSDS standard](https://ccsds.org/Pubs/502x0b3e1.pdf) with some extra restrictions. OEM files should be in KVN format. For more detail about the OEM format that AWS Ground Station supports, see [OEM ephemeris format](https://docs.aws.amazon.com/ground-station/latest/ug/providing-oem-ephemeris-data.html#oem-ephemeris-format) in the AWS Ground Station user guide.

## Contents
<a name="API_OEMEphemeris_Contents"></a>

 ** oemData **   <a name="groundstation-Type-OEMEphemeris-oemData"></a>
OEM data that you provide directly instead of using an Amazon S3 object.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\s\S]+`
Required: No

 ** s3Object **   <a name="groundstation-Type-OEMEphemeris-s3Object"></a>
The Amazon S3 object that contains the ephemeris data.
Type: [S3Object](API_S3Object.md) object
Required: No

## See Also
<a name="API_OEMEphemeris_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/OEMEphemeris)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/OEMEphemeris)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/OEMEphemeris)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
