---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ContactVersion.html
---

# ContactVersion
<a name="API_ContactVersion"></a>

Version information for a contact.

## Contents
<a name="API_ContactVersion_Contents"></a>

 ** activated **   <a name="groundstation-Type-ContactVersion-activated"></a>
Time the contact version was activated in UTC. A version is activated when it becomes the current active version of the contact.
Type: Timestamp
Required: No

 ** created **   <a name="groundstation-Type-ContactVersion-created"></a>
Time the contact version was created in UTC.
Type: Timestamp
Required: No

 ** failureCodes **   <a name="groundstation-Type-ContactVersion-failureCodes"></a>
List of failure codes for the contact version.
Type: Array of strings
Valid Values: `INTERNAL_ERROR | INVALID_SATELLITE_ARN | INVALID_UPDATE_CONTACT_REQUEST | EPHEMERIS_NOT_FOUND | EPHEMERIS_TIME_RANGE_INVALID | EPHEMERIS_NOT_ENABLED | SATELLITE_DOES_NOT_MATCH_EPHEMERIS | NOT_ONBOARDED_TO_AZEL_EPHEMERIS | AZEL_EPHEMERIS_NOT_FOUND | AZEL_EPHEMERIS_WRONG_GROUND_STATION | AZEL_EPHEMERIS_INVALID_STATUS | AZEL_EPHEMERIS_TIME_RANGE_INVALID`
Required: No

 ** failureMessage **   <a name="groundstation-Type-ContactVersion-failureMessage"></a>
Failure message for the contact version.
Type: String
Required: No

 ** lastUpdated **   <a name="groundstation-Type-ContactVersion-lastUpdated"></a>
Time the contact version was last updated in UTC.
Type: Timestamp
Required: No

 ** status **   <a name="groundstation-Type-ContactVersion-status"></a>
Status of the contact version.
Type: String
Valid Values: `UPDATING | ACTIVE | SUPERSEDED | FAILED_TO_UPDATE`
Required: No

 ** superseded **   <a name="groundstation-Type-ContactVersion-superseded"></a>
Time the contact version was superseded in UTC. A version is superseded when a newer version becomes active.
Type: Timestamp
Required: No

 ** versionId **   <a name="groundstation-Type-ContactVersion-versionId"></a>
Version ID of a contact.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 128.
Required: No

## See Also
<a name="API_ContactVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ContactVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ContactVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ContactVersion)
