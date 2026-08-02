---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TLEEphemeris.html
---

# TLEEphemeris
<a name="API_TLEEphemeris"></a>

Two-line element set (TLE) ephemeris.

 For more detail about providing Two-line element sets to AWS Ground Station, see the [TLE section](https://docs.aws.amazon.com/ground-station/latest/ug/providing-tle-ephemeris-data.html) of the AWS Ground Station user guide.

## Contents
<a name="API_TLEEphemeris_Contents"></a>

 ** s3Object **   <a name="groundstation-Type-TLEEphemeris-s3Object"></a>
The Amazon S3 object that contains the ephemeris data.
Type: [S3Object](API_S3Object.md) object
Required: No

 ** tleData **   <a name="groundstation-Type-TLEEphemeris-tleData"></a>
TLE data that you provide directly instead of using an Amazon S3 object.
Type: Array of [TLEData](API_TLEData.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

## See Also
<a name="API_TLEEphemeris_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/TLEEphemeris)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/TLEEphemeris)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/TLEEphemeris)
