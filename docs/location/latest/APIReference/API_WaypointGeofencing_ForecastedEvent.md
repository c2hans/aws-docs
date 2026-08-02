---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ForecastedEvent.html
---

# ForecastedEvent
<a name="API_WaypointGeofencing_ForecastedEvent"></a>

A forecasted event represents a geofence event in relation to the requested device state, that may occur given the provided device state and time horizon.

## Contents
<a name="API_WaypointGeofencing_ForecastedEvent_Contents"></a>

 ** EventId **   <a name="location-Type-WaypointGeofencing_ForecastedEvent-EventId"></a>
The forecasted event identifier.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** EventType **   <a name="location-Type-WaypointGeofencing_ForecastedEvent-EventType"></a>
The event type, forecasting three states for which a device can be in relative to a geofence:
 `ENTER`: If a device is outside of a geofence, but would breach the fence if the device is moving at its current speed within time horizon window.
 `EXIT`: If a device is inside of a geofence, but would breach the fence if the device is moving at its current speed within time horizon window.
 `IDLE`: If a device is inside of a geofence, and the device is not moving.
Type: String
Valid Values: `ENTER | EXIT | IDLE`
Required: Yes

 ** GeofenceId **   <a name="location-Type-WaypointGeofencing_ForecastedEvent-GeofenceId"></a>
The geofence identifier pertaining to the forecasted event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** IsDeviceInGeofence **   <a name="location-Type-WaypointGeofencing_ForecastedEvent-IsDeviceInGeofence"></a>
Indicates if the device is located within the geofence.
Type: Boolean
Required: Yes

 ** NearestDistance **   <a name="location-Type-WaypointGeofencing_ForecastedEvent-NearestDistance"></a>
The closest distance from the device's position to the geofence.
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

 ** ForecastedBreachTime **   <a name="location-Type-WaypointGeofencing_ForecastedEvent-ForecastedBreachTime"></a>
The forecasted time the device will breach the geofence in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`
Type: Timestamp
Required: No

 ** GeofenceProperties **   <a name="location-Type-WaypointGeofencing_ForecastedEvent-GeofenceProperties"></a>
The geofence properties.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 3 items.
Key Length Constraints: Minimum length of 1. Maximum length of 20.
Value Length Constraints: Minimum length of 1. Maximum length of 40.
Required: No

## See Also
<a name="API_WaypointGeofencing_ForecastedEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/ForecastedEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/ForecastedEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/ForecastedEvent)
