---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisItem.html
---

# EphemerisItem
<a name="API_EphemerisItem"></a>

Ephemeris item.

## Contents
<a name="API_EphemerisItem_Contents"></a>

 ** creationTime **   <a name="groundstation-Type-EphemerisItem-creationTime"></a>
The time the ephemeris was uploaded in UTC.
Type: Timestamp
Required: No

 ** enabled **   <a name="groundstation-Type-EphemerisItem-enabled"></a>
Whether or not the ephemeris is enabled.
Type: Boolean
Required: No

 ** ephemerisId **   <a name="groundstation-Type-EphemerisItem-ephemerisId"></a>
The AWS Ground Station ephemeris ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** ephemerisType **   <a name="groundstation-Type-EphemerisItem-ephemerisType"></a>
The type of ephemeris.
Type: String
Valid Values: `TLE | OEM | AZ_EL | SERVICE_MANAGED`
Required: No

 ** name **   <a name="groundstation-Type-EphemerisItem-name"></a>
A name that you can use to identify the ephemeris.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: No

 ** priority **   <a name="groundstation-Type-EphemerisItem-priority"></a>
A priority score that determines which ephemeris to use when multiple ephemerides overlap.
Higher numbers take precedence. The default is 1. Must be 1 or greater.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 99999.
Required: No

 ** sourceS3Object **   <a name="groundstation-Type-EphemerisItem-sourceS3Object"></a>
Source Amazon S3 object used for the ephemeris.
Type: [S3Object](API_S3Object.md) object
Required: No

 ** status **   <a name="groundstation-Type-EphemerisItem-status"></a>
The status of the ephemeris.
Type: String
Valid Values: `VALIDATING | INVALID | ERROR | ENABLED | DISABLED | EXPIRED`
Required: No

## See Also
<a name="API_EphemerisItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/EphemerisItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/EphemerisItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/EphemerisItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
