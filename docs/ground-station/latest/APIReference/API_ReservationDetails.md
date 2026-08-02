---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ReservationDetails.html
---

# ReservationDetails
<a name="API_ReservationDetails"></a>

Details of a ground station reservation.

## Contents
<a name="API_ReservationDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** contact **   <a name="groundstation-Type-ReservationDetails-contact"></a>
Details of a contact reservation.
Type: [ContactReservationDetails](API_ContactReservationDetails.md) object
Required: No

 ** maintenance **   <a name="groundstation-Type-ReservationDetails-maintenance"></a>
Details of a maintenance reservation.
Type: [MaintenanceReservationDetails](API_MaintenanceReservationDetails.md) object
Required: No

## See Also
<a name="API_ReservationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ReservationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ReservationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ReservationDetails)
