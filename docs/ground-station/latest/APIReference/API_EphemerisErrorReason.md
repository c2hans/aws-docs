---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisErrorReason.html
---

# EphemerisErrorReason
<a name="API_EphemerisErrorReason"></a>

Detailed error information for ephemeris validation failures.

Provides an error code and descriptive message to help diagnose and resolve validation issues.

## Contents
<a name="API_EphemerisErrorReason_Contents"></a>

 ** errorCode **   <a name="groundstation-Type-EphemerisErrorReason-errorCode"></a>
The error code identifying the type of validation failure.
See the [Troubleshooting Invalid Ephemerides guide](https://docs.aws.amazon.com/ground-station/latest/ug/troubleshooting-invalid-ephemerides.html) for error code details.
Type: String
Valid Values: `INTERNAL_ERROR | MISMATCHED_SATCAT_ID | OEM_VERSION_UNSUPPORTED | ORIGINATOR_MISSING | CREATION_DATE_MISSING | OBJECT_NAME_MISSING | OBJECT_ID_MISSING | REF_FRAME_UNSUPPORTED | REF_FRAME_EPOCH_UNSUPPORTED | TIME_SYSTEM_UNSUPPORTED | CENTER_BODY_UNSUPPORTED | INTERPOLATION_MISSING | INTERPOLATION_DEGREE_INVALID | AZ_EL_SEGMENT_LIST_MISSING | INSUFFICIENT_TIME_AZ_EL | START_TIME_IN_FUTURE | END_TIME_IN_PAST | EXPIRATION_TIME_TOO_EARLY | START_TIME_METADATA_TOO_EARLY | STOP_TIME_METADATA_TOO_LATE | AZ_EL_SEGMENT_END_TIME_BEFORE_START_TIME | AZ_EL_SEGMENT_TIMES_OVERLAP | AZ_EL_SEGMENTS_OUT_OF_ORDER | TIME_AZ_EL_ITEMS_OUT_OF_ORDER | MEAN_MOTION_INVALID | TIME_AZ_EL_AZ_RADIAN_RANGE_INVALID | TIME_AZ_EL_EL_RADIAN_RANGE_INVALID | TIME_AZ_EL_AZ_DEGREE_RANGE_INVALID | TIME_AZ_EL_EL_DEGREE_RANGE_INVALID | TIME_AZ_EL_ANGLE_UNITS_INVALID | INSUFFICIENT_KMS_PERMISSIONS | FILE_FORMAT_INVALID | AZ_EL_SEGMENT_REFERENCE_EPOCH_INVALID | AZ_EL_SEGMENT_START_TIME_INVALID | AZ_EL_SEGMENT_END_TIME_INVALID | AZ_EL_SEGMENT_VALID_TIME_RANGE_INVALID | AZ_EL_SEGMENT_END_TIME_TOO_LATE | AZ_EL_TOTAL_DURATION_EXCEEDED`
Required: Yes

 ** errorMessage **   <a name="groundstation-Type-EphemerisErrorReason-errorMessage"></a>
A human-readable message describing the validation failure.
Provides specific details about what failed and may include suggestions for remediation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

## See Also
<a name="API_EphemerisErrorReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/EphemerisErrorReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/EphemerisErrorReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/EphemerisErrorReason)
