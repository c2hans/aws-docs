---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GroundStationReservationListItem.html
---

# GroundStationReservationListItem
<a name="API_GroundStationReservationListItem"></a>

Item in a list of ground station reservations.

## Contents
<a name="API_GroundStationReservationListItem_Contents"></a>

 ** antennaName **   <a name="groundstation-Type-GroundStationReservationListItem-antennaName"></a>
Name of an antenna.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 256.
Pattern: `[ a-zA-Z0-9-._:=]{4,256}`
Required: Yes

 ** endTime **   <a name="groundstation-Type-GroundStationReservationListItem-endTime"></a>
End time of a ground station reservation in UTC.
Type: Timestamp
Required: Yes

 ** groundStationId **   <a name="groundstation-Type-GroundStationReservationListItem-groundStationId"></a>
ID of a ground station.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 97.
Pattern: `[ a-zA-Z0-9-._:=]{4,97}`
Required: Yes

 ** reservationDetails **   <a name="groundstation-Type-GroundStationReservationListItem-reservationDetails"></a>
Details of a ground station reservation.
Type: [ReservationDetails](API_ReservationDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** reservationType **   <a name="groundstation-Type-GroundStationReservationListItem-reservationType"></a>
Type of a ground station reservation.
Type: String
Valid Values: `MAINTENANCE | CONTACT`
Required: Yes

 ** startTime **   <a name="groundstation-Type-GroundStationReservationListItem-startTime"></a>
Start time of a ground station reservation in UTC.
Type: Timestamp
Required: Yes

## See Also
<a name="API_GroundStationReservationListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/GroundStationReservationListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/GroundStationReservationListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/GroundStationReservationListItem)
