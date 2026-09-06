---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ContactData.html
---

# ContactData
<a name="API_ContactData"></a>

Data describing a contact.

## Contents
<a name="API_ContactData_Contents"></a>

 ** contactId **   <a name="groundstation-Type-ContactData-contactId"></a>
UUID of a contact.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** contactStatus **   <a name="groundstation-Type-ContactData-contactStatus"></a>
Status of a contact.
Type: String
Valid Values: `SCHEDULING | FAILED_TO_SCHEDULE | SCHEDULED | CANCELLED | AWS_CANCELLED | PREPASS | PASS | POSTPASS | COMPLETED | FAILED | AVAILABLE | CANCELLING | AWS_FAILED`
Required: No

 ** endTime **   <a name="groundstation-Type-ContactData-endTime"></a>
End time of a contact in UTC.
Type: Timestamp
Required: No

 ** ephemeris **   <a name="groundstation-Type-ContactData-ephemeris"></a>
The ephemeris that determines antenna pointing for the contact.
Type: [EphemerisResponseData](API_EphemerisResponseData.md) object
Required: No

 ** errorMessage **   <a name="groundstation-Type-ContactData-errorMessage"></a>
Error message of a contact.
Type: String
Required: No

 ** groundStation **   <a name="groundstation-Type-ContactData-groundStation"></a>
Name of a ground station.
Type: String
Required: No

 ** maximumElevation **   <a name="groundstation-Type-ContactData-maximumElevation"></a>
Maximum elevation angle of a contact.
Type: [Elevation](API_Elevation.md) object
Required: No

 ** missionProfileArn **   <a name="groundstation-Type-ContactData-missionProfileArn"></a>
ARN of a mission profile.
Type: String
Length Constraints: Minimum length of 89. Maximum length of 138.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:mission-profile/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** postPassEndTime **   <a name="groundstation-Type-ContactData-postPassEndTime"></a>
End time in UTC of the post-pass period, at which you receive a CloudWatch event indicating the pass has finished.
Type: Timestamp
Required: No

 ** prePassStartTime **   <a name="groundstation-Type-ContactData-prePassStartTime"></a>
Start time in UTC of the pre-pass period, at which you receive a CloudWatch event indicating an upcoming pass.
Type: Timestamp
Required: No

 ** region **   <a name="groundstation-Type-ContactData-region"></a>
Region of a contact.
Type: String
Required: No

 ** satelliteArn **   <a name="groundstation-Type-ContactData-satelliteArn"></a>
ARN of a satellite.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 132.
Pattern: `arn:aws:groundstation:([-a-z0-9]{1,50})?:[0-9]{12}:satellite/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** startTime **   <a name="groundstation-Type-ContactData-startTime"></a>
Start time of a contact in UTC.
Type: Timestamp
Required: No

 ** tags **   <a name="groundstation-Type-ContactData-tags"></a>
Tags assigned to a contact.
Type: String to string map
Required: No

 ** version **   <a name="groundstation-Type-ContactData-version"></a>
Version information for a contact.
Type: [ContactVersion](API_ContactVersion.md) object
Required: No

 ** visibilityEndTime **   <a name="groundstation-Type-ContactData-visibilityEndTime"></a>
 Projected time in UTC your satellite will set below the [receive mask](https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html). This time is based on the satellite's current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts. *This field is not present for contacts with a `SCHEDULING` or `SCHEDULED` status.*
Type: Timestamp
Required: No

 ** visibilityStartTime **   <a name="groundstation-Type-ContactData-visibilityStartTime"></a>
 Projected time in UTC your satellite will rise above the [receive mask](https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html). This time is based on the satellite's current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts. *This field is not present for contacts with a `SCHEDULING` or `SCHEDULED` status.*
Type: Timestamp
Required: No

## See Also
<a name="API_ContactData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ContactData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ContactData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ContactData)
