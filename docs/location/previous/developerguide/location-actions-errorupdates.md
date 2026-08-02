---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/location-actions-errorupdates.html
---

# Amazon Location API error message updates
<a name="location-actions-errorupdates"></a>

Beginning August 1, 2023, the Amazon Location team is changing API error messages as described in the following tables. Error codes will not be changed. If your applications depend on exact error message strings, you must update your applications with the new strings. For help with questions or problems, contact AWS Support.

**Topics**
+ [Places](#location-actions-errorupdates-places)
+ [Maps](#location-actions-errorupdates-maps)
+ [Trackers](#location-actions-errorupdates-trackers)
+ [Routes](#location-actions-errorupdates-routes)
+ [Metadata](#location-actions-errorupdates-metadata)
+ [Geofences](#location-actions-errorupdates-geofences)

## Places
<a name="location-actions-errorupdates-places"></a>

**Places**

| Error code | Exception | Old error message | New error message |
| --- | --- | --- | --- |
| 500 | InternalServerException | Internal Server Exception | Internal server error. Try again later. |
| 404 | ResourceNotFoundException | resource <PlaceIndexName> not found, reason: <Reason><br />Resource '<PlaceIndexName>' not found<br />placeIdx<PlaceIndexName> not found, reason: <Reason><br />no place index with name '%s' found | Place index not found: <PlaceIndexName>. |
| 404 | ResourceNotFoundException | place not found | Place not found: <PlaceId>. |
| 400 | ValidationException | PlaceIndex <PlaceIndexName> cannot be used for SearchPlaceIndexForSuggestions because it has IntendedUse <IntendedUse> | A place index with 'IntendedUse' set to Storage does not support 'SearchPlaceIndexForSuggestion' operation. |
| 400 | ValidationException | only one of 'BiasPosition' or 'FilterBBox' may be set | Only one of 'BiasPosition' or 'FilterBBox' may be set. |
| 400 | ValidationException | BiasPosition must have exactly 2 entries | 'BiasPosition' must have exactly 2 entries. |
| 400 | ValidationException | BiasPosition[0] must be between -180 and 180 | 'BiasPosition[0]' must be between -180 and 180. |
| 400 | ValidationException | BiasPosition[1] must be between -90 and 90 | 'BiasPosition[1]' must be between -90 and 90. |
| 400 | ValidationException | FilterBBox must have exactly 4 entries | 'FilterBBox' must have exactly 4 entries. |
| 400 | ValidationException | FilterBBox[0] must be between -180 and 180 | 'FilterBBox[0]' must be between -180 and 180. |
| 400 | ValidationException | FilterBBox[1] must be between -90 and 90 | 'FilterBBox[1]' must be between -90 and 90. |
| 400 | ValidationException | FilterBBox[2] must be between -180 and 180 | 'FilterBBox[2]' must be between -180 and 180. |
| 400 | ValidationException | FilterBBox[3] must be between -90 and 90 | 'FilterBBox[3]' must be between -90 and 90. |
| 400 | ValidationException | FilterBBox must have more southwesterly point before more northeasterly point | 'FilterBBox' must have more southwesterly position before more northeasterly position. |
| 400 | ValidationException | Position must have exactly 2 entries | 'Position' must have exactly 2 entries. |
| 400 | ValidationException | Position[0] must be between -180 and 180 | 'Position[0]' must be between -180 and 180. |
| 400 | ValidationException | Position[1] must be between -90 and 90 | 'Position[1]' must be between -90 and 90. |
| 400 | ValidationException | Language is not a valid BCP 47 language tag | 'Language' must comply with the BCP 47 Language Tag standard, but was set to <GivenValue>. For more information, see https://wikipedia.org/wiki/IETF\_language\_tag. |
| 400 | ValidationException | 'placeID' is invalid | 'PlaceId' must be a valid ID. |
| 400 | ValidationException | no customer account ID parameter found | 'RequesterAccountID' is a required field. |
| 400 | ValidationException | Invalid token | 'NextToken' must be a valid token. |
| 400 | ValidationException | Expired token | 'NextToken' must not be expired. |
| 400 | ValidationException | unsupported price plan '<PricingPlan>' | 'PricingPlan' must be set to RequestBasedUsage. |
| 400 | ValidationException | 'DataSource' must be one of: Here, Esri | 'DataSource' must be one of Esri, Grab, Here. |
| 400 | ValidationException | Grab is only supported in the ap-southeast-1 region | 'DataSource' Grab must only be used in following regions: ap-southeast-1. |
| 400 | ValidationException | 'IntendedUse' and 'PricingPlan' must both be provided to update either property | 'IntendedUse' and 'PricingPlan' must both be provided to update either attribute. |
| 402 | ServiceQuotaExceededException | Place resources per account exceeded quota limits. For more info, see https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/ | Place index resources have exceeded the quota per account per region. For more information, see https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/. |
| 409 | ConflictException | Resource already exists | Place index already exists: <PlaceIndexName>. |

## Maps
<a name="location-actions-errorupdates-maps"></a>

**Maps**

| Error code | Exception | Old error message | New error message |
| --- | --- | --- | --- |
| 500 | InternalServerException | Internal Server Exception<br />unable to find style template<br />Error fetching style<br />was not able to serialize the map style file | Internal server error. Try again later. |
| 404 | ResourceNotFoundException | Map not found | Map not found: <MapName>. |
| 404 | ResourceNotFoundException | Sprites are not supported for this resource | Sprite not found: <SpriteName>. |
| 400 | ValidationException | Resource name should be set | 'MapName' is a required field. |
| 400 | ValidationException | Must provide a valid number for start and end of Range | Font Unicode range start and end numbers must both be provided. |
| 400 | ValidationException | Start of range is an invalid number: <StartValue> | Start of font Unicode range must be a valid number. |
| 400 | ValidationException | End of range is an invalid number: <StartValue> | End of font Unicode range must be a valid number. |
| 400 | ValidationException | End of range must be exactly 255 higher from start of range, difference found: <Difference> | The difference between the start and end of the font Unicode range must be exactly 255. Difference found: <Difference>. |
| 400 | ValidationException | Start of range must be a multiple of 256, found <StartValue> | Start of font Unicode range must be a multiple of 256, but was set to: <StartValue>. |
| 400 | ValidationException | Request font is empty | 'FontStack' is a required field. |
| 400 | ValidationException | Request font is not valid for the datasource <DataSource> | <FontStack> is not a supported font stack for data source <DataSource>. For more information about the list of supported font stacks, see https://docs.aws.amazon.com/location/previous/APIReference/API\_GetMapGlyphs.html. |
| 400 | ValidationException | Request font is not valid | <FontStack> is not a supported font stack for data source <DataSource>. For more information about the list of supported font stacks, see https://docs.aws.amazon.com/location/previous/APIReference/API\_GetMapGlyphs.html. |
| 400 | ValidationException | DataSource is invalid: <DataSource> | 'DataSource' must be one of Esri, Grab, Here. |
| 400 | ValidationException | Request filename is empty | 'FileName' is a required field. |
| 400 | ValidationException | Request filename is not valid | <SpriteFile> is not a supported sprite file name. For more information about the list of supported sprite file names, see https://docs.aws.amazon.com/location/previous/APIReference/API\_GetMapSprites.html. |
| 400 | ValidationException | Filename is invalid: <FileName> | <SpriteFile> is not a supported sprite file name. For more information about the list of supported sprite file names, see https://docs.aws.amazon.com/location/previous/APIReference/API\_GetMapSprites.html. |
| 400 | ValidationException | Filename is an invalid content type: <FileName> | <SpriteFile> is not a supported sprite file name. For more information about the list of supported sprite file names, see https://docs.aws.amazon.com/location/previous/APIReference/API\_GetMapSprites.html. |
| 400 | ValidationException | Filename is invalid: <FileName> | 'Filename' must not be empty. |
| 400 | ValidationException | y-coordinate part of 'Y' must be a valid integer | y- coordinate part of 'Y' must be an integer. |
| 400 | ValidationException | tile resolution part of 'Y' must be a valid integer followed by 'x' | Tile resolution part of 'Y' must be an integer followed by 'X'. |
| 400 | ValidationException | file type extension part of 'Y' must not be empty if a '.' is present | File type extension part of 'Y' must not be empty if a '.' is present. |
| 400 | ValidationException | 'Z' must be a valid integer | 'Z' must be an integer. |
| 400 | ValidationException | 'X' must be a valid integer | 'X' must be an integer. |
| 400 | ValidationException | 'Z' must not be less than minimum zoom of style '<Style>' (<MinimumValue>) | 'Z' must not be less than minimum zoom of style <Style> (<MinimumValue>). |
| 400 | ValidationException | 'Z' must not be greater than maximum zoom of style '<Style' (<MaximumValue>) | 'Z' must not be greater than maximum zoom of style Style (<MaximumValue>). |
| 400 | ValidationException | 'Z' value not supported | 'Z' must be between 0 and 63. |
| 400 | ValidationException | tile resolution part of 'Y' must be omitted because '<Style>' is a vector style | Tile resolution part of 'Y' must be omitted for style <Style>. |
| 400 | ValidationException | tile resolution part of 'Y' must be at least 1 | Tile resolution part of 'Y' must be at least 1. |
| 400 | ValidationException | tile resolution part of 'Y' must not be greater than max resolution of style '<Style>' (<MaximumResolution>) | Tile resolution part of 'Y' must not be greater than maximum resolution of style <Style> (max <MaxResolution>). |
| 400 | ValidationException | file type extension part of 'Y' must be one of <SupportedFileFormats> (or may be omitted) for style '<Style>' | File type extension part of 'Y' must be one of <SupportedFileFormats> (or may be omitted) for style <Style>. |
| 400 | ValidationException | file type extension part of 'Y' must be omitted for style '<Style>' | File type extension part of 'Y' must be omitted for style <Style>. |
| 400 | ValidationException | y-coordinate part of 'Y' must be an integer in the range 0..2^Zoom-1 (0..<MaxTileCoordinate>) | y-coordinate part of 'Y' must be an integer in the range 0..2^Zoom-1 (0..<MaxTileCoordinate>). |
| 400 | ValidationException | 'DataSource' must be one of: Here, Esri | 'DataSource' must be one of Esri, Grab, Here. |
| 400 | ValidationException | unsupported price plan '<PricingPlan>' | 'PricingPlan' must be set to RequestBasedUsage. |
| 400 | ValidationException | Invalid token | 'NextToken' must be a valid token. |
| 400 | ValidationException | Expired token | 'NextToken' must not be expired. |
| 400 | ValidationException | Unsupported Map Style: <Style> | <Style> is not a supported map style. For more information about list of supported map styles, see https://docs.aws.amazon.com/location/previous/APIReference/API\_MapConfiguration.html. |
| 402 | ServiceQuotaExceededException | Map resources per account exceeded quota limits. For more info, see https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/ | Map resources have exceeded the quota per account per region. For more information, see https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/. |
| 409 | ConflictException | Resource already exists | Map already exists: <MapName>. |

## Trackers
<a name="location-actions-errorupdates-trackers"></a>

**Trackers**

| Error code | Exception | Old error message | New error message |
| --- | --- | --- | --- |
| 500 | InternalServerException | Internal Server Exception<br />internal server error<br />unable to retrieve point from the storage<br />unable to verify tracker<br />Error processing List request | Internal server error. Try again later. |
| 404 | ResourceNotFoundException | tracker not found: <TrackerName><br />Tracker with name <TrackerName> was not found | Tracker not found: <TrackerName>. |
| 404 | ResourceNotFoundException | association not found: TrackerName <TrackerName>; and ConsumerArn < ConsumerArn > | Association between tracker <TrackerName> and consumer <ConsumerArn> is not found. |
| 400 | ValidationException | 'ConsumerArn' must refer to a geofence collection resource | 'ConsumerArn' must refer to a geofence collection resource. |
| 400 | ValidationException | 'ConsumerArn' must refer to a resource in the same region as the tracker it is associated to | 'ConsumerArn' must refer to a resource in the same region as the tracker it is associated with. |
| 400 | ValidationException | 'ConsumerArn' must refer to a resource in the same AWS account as the tracker is it associated to | 'ConsumerArn' must refer to a resource in the same AWS account as the tracker it is associated with. |
| 400 | ValidationException | 'DataSource' must be one of: Here, Esri | 'DataSource' must be one of Esri, Grab, Here. |
| 400 | ValidationException | Nothing to update. | At least one of the following fields must be set: 'Description', 'PositionFiltering' |
| 400 | ValidationException | Invalid token | 'NextToken' must be a valid token. |
| 400 | ValidationException | Expired token | 'NextToken' must not be expired. |
| 400 | ValidationException | request.TrackerName not found on request | 'TrackerName ' is a required field. |
| 400 | ValidationException | no deviceId parameter found | 'DeviceId' is a required field. |
| 400 | ValidationException | unsupported price plan '<PricingPlan>' | 'PricingPlan' must be set to RequestBasedUsage |
| 400 | ValidationException | Invalid token | 'NextToken' must be a valid token. |
| 400 | ValidationException | Expired token | 'NextToken' must not be expired. |
| 400 | ValidationException | provided start time is incorrect, should follow the format YYYY-MM-DDThh:mm:ss.sssZ“ | 'StartTimeInclusive' must follow the format YYYY-MM-DDThh:mm:ss.sssZ. |
| 400 | ValidationException | provided end time is incorrect, should follow the format YYYY-MM-DDThh:mm:ss.sssZ | 'EndTimeExclusive' must follow the format YYYY-MM-DDThh:mm:ss.sssZ. |
| 400 | ValidationException | end time must be after start time | 'EndTimeExclusive' must be after 'StartTimeInclusive'. |
| 400 | ValidationException | invalid key state | KMS key must be a symmetric Customer Master Key (CMK). Invalid state found. For more information about how key state affects the use of a KMS key, see https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html. |
| 400 | ValidationException | key not found | Invalid KMS key. '<KmsKeyId>' <KmsKeyIdValue> not found. |
| 400 | ValidationException | key is disabled | Symmetric Customer Master Key (CMK) must be enabled. |
| 400 | ValidationException | access denied | Symmetric Customer Master Key (CMK) must allow Amazon Location to create grants to its KMS key. |
| 402 | ServiceQuotaExceededException | Tracker <TrackerName> may not have more than <Max> consumer associations | Tracker resource may not have more than <Max> consumer associations. For more information, see https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/. |
| 402 | ServiceQuotaExceededException | Trackers per account exceeded quota limits. For more info, see https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/ | Tracking resources have exceeded the quota per account per region. For more information, see https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/. |
| 409 | ConflictException | association already exists: TrackerName <TrackerName>; and ConsumerArn <ConsumerArn> | An association already exists between tracker <TrackerName> and consumer <ConsumerArn>. |
| 409 | ConflictException | Tracker already exists: <TrackerName> | Tracker already exists: <TrackerName>. |

## Routes
<a name="location-actions-errorupdates-routes"></a>

**Routes**

| Error code | Exception | Old error message | New error message |
| --- | --- | --- | --- |
| 500 | InternalServerException | Internal Server Exception | Internal server error. Try again later. |
| 404 | ResourceNotFoundException | Resource not found | Route calculator not found: <RouteCalculatorName>. |
| 400 | ValidationException | Invalid token | 'NextToken' must be a valid token. |
| 400 | ValidationException | Expired token | 'NextToken' must not be expired. |
| 400 | ValidationException | 'DataSource' must be one of: Here, Esri, Grab | 'DataSource' must be one of Esri, Grab, Here. |
| 400 | ValidationException | <PricingPlan> pricing plan is not supported | 'PricingPlan' must be set to RequestBasedUsage |
| 400 | ValidationException | unsupported price plan '<PricingPlan>' | 'PricingPlan' must be set to RequestBasedUsage |
| 400 | ValidationException | Grab is only supported in the ap-southeast-1 region | 'DataSource' <DataSourceName> must only be used in following regions: ap-southeast-1. |
| 400 | ValidationException | PricingPlan must be 'RequestBasedUsage' | 'PricingPlan' must be set to RequestBasedUsage. |
| 400 | ValidationException | 'DeparturePositions[0][0]' must be between -180 and 180 | 'DeparturePositions[0][0]' must be between -180 and 180. |
| 400 | ValidationException | 'DeparturePositions[0][1]' must be between -90 and 90 | 'DeparturePositions[0][1]' must be between -90 and 90. |
| 400 | ValidationException | 'DestinationPositions[0][0]' must be between -180 and 180 | 'DestinationPositions[0][0]' must be between -180 and 180. |
| 400 | ValidationException | 'DestinationPositions[0][1]' must be between -90 and 90. | 'DestinationPositions[0][1]' must be between -90 and 90 |
| 400 | ValidationException | 'DepartNow' may not be true if 'DepartureTime' is set | Only one of 'DepartNow' or 'DepartureTime' may be set. |
| 400 | ValidationException | '<TravelModeOption>'' may not be set when 'TravelMode' has value <TravelModeOption> | '<TravelModeOption>' must not be set when 'TravelMode' has value <TravelModeOption>. |
| 400 | ValidationException | 'CarModeOptions' may not be set when 'TravelMode' has value Walking | 'CarModeOptions' must not be set when 'TravelMode' has value Walking. |
| 400 | ValidationException | 'TruckModeOptions' may not be set when 'TravelMode' has value Walking | 'TruckModeOptions' must not be set when 'TravelMode' has value Walking. |
| 400 | ValidationException | 'TruckModeOptions' may not be set when 'TravelMode' has value Car | 'TruckModeOptions' must not be set when 'TravelMode' has value Car. |
| 400 | ValidationException | 'CarModeOptions' may not be set when 'TravelMode' has value Truck | 'CarModeOptions' must not be set when 'TravelMode' has value Truck. |
| 400 | ValidationException | At least one of [Height, Length, Width] must be set in 'TruckModeOptions.Dimensions' | At least one of the following attribute must be set in TruckModeOptions.Dimensions: Height, Length, Width. |
| 400 | ValidationException | At least one of [Total] must be set in 'TruckModeOptions.Weight' | At least one of the following attribute must be set in TruckModeOptions.Weight: Total. |
| 400 | ValidationException | 'DeparturePositions' count must be 10 or less with DataSource set to Esri | 'DeparturePositions' must have length at most 10 for 'DataSource' Esri. |
| 400 | ValidationException | 'DestinationPositions' count must be 10 or less with DataSource set to Esri | 'DestinationPositions' must have length at most 10 for 'DataSource' Esri. |
| 400 | ValidationException | 'DeparturePositions[0]' is more than 40km away from 'DestinationPositions[0]' | 'DeparturePositions[0]' must not be more than 40 km away from 'DestinationPositions[0]'. |
| 400 | ValidationException | 'DeparturePositions[0]' is more than 400km away from 'DestinationPositions[0]' | 'DeparturePositions[0]' must not be more than 400 km away from 'DestinationPositions[0]'. |
| 400 | ValidationException | DeparturePositions[0] is contained within an unsupported region. Korea is not supported for CalculateRouteMatrix with the provider Esri. | DeparturePositions[0] is located in Korea, which is not supported when using CalculateRouteMatrix with data provider Esri. |
| 400 | ValidationException | '<HereTruckDimension>' must be between <Min> and <Max> <Unit> | 'HereTruckDimension' must be between <Min> and <Max> <Unit>. |
| 400 | ValidationException | 'WaypointPositions[0][0]' must be between -180 and 180 | 'WaypointPositions[0][0]' must be between -180 and 180. |
| 400 | ValidationException | 'WaypointPositions[0][1]' must be between -90 and 90 | 'WaypointPositions[0][1]' must be between -90 and 90. |
| 400 | ValidationException | 'WaypointPositions[1][0]' must be between -180 and 180 | 'WaypointPositions[1][0]' must be between -180 and 180. |
| 400 | ValidationException | 'WaypointPositions[1][1]' must be between -90 and 90 | 'WaypointPositions[1][1]' must be between -90 and 90. |
| 400 | ValidationException | No road segment could be matched for one or more coordinates within a radius (1km) | One or more provided positions are more than 1 km from the nearest road segment. |
| 400 | ValidationException | Some positions in the request are unreachable | Some positions in the request are unreachable. |
| 400 | ValidationException | Total distance between all waypoints must be not be greater than 40km for DataSource Esri when using TravelMode Walking | Total distance between all route positions must not be greater than 40 km for 'DataSource' Esri and 'TravelMode' Walking. |
| 400 | ValidationException | Total distance between all waypoints must be not be greater than 400km for DataSource Esri | Total distance between all route positions must not be greater than 400 km for 'DataSource' Esri. |
| 400 | ValidationException | Following positions in the request are unreachable: <UnreachablePositions> | The following positions are unreachable: <UnreachablePositions>. |
| 400 | ValidationException | 'DepartureTime' contains a badly-formatted timestamp | 'DepartureTime' must follow the format YYYY-MM-DDThh:mm:ss.sssZ. |
| 400 | ValidationException | 'TravelMode' <TravelMode> is not supported by <DataProvider> | 'TravelMode' <TravelMode> not supported by data provider <DataProvider>. |
| 400 | ValidationException | 'DeparturePositions' must be set | 'DeparturePositions' must not be empty. |
| 400 | ValidationException | 'DestinationPositions' must be set | 'DestinationPositions' must not be empty. |
| 400 | ValidationException | Some inputs in the request are invalid | Some inputs in the request are invalid. |
| 400 | ValidationException | No route found between position <FirstPosition> and position <SecondPosition> | No route found between position <FirstPosition> and position <SecondPosition>. |
| 400 | ValidationException | No route found | No route found. For more information, see https://developer.here.com/documentation/routing-api/dev\_guide/topics/notice.html. |
| 400 | ValidationException | No route found | No route found. |
| 402 | ServiceQuotaExceededException | Route calculators per account exceeded quota limits. For more info, see https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/ | Route calculator resources have exceeded the quota per account per region. For more information, see https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/. |
| 409 | ConflictException | Resource already exists | Route calculator already exists: <RouteCalculatorName>. |

## Metadata
<a name="location-actions-errorupdates-metadata"></a>

**Metadata**

| Error code | Exception | Old error message | New error message |
| --- | --- | --- | --- |
| 500 | InternalServerException | Internal Server Error<br />Error processing List request | Internal server error. Try again later. |
| 404 | ResourceNotFoundException | APIKey not found | Api key not found: <APIKeyName>. |
| 404 | ResourceNotFoundException | APIKeyID not found | ApiKeyId not found: <APIKeyID>. |
| 400 | ValidationException | Either ExpireTime or NoExpiry must be provided | At least one of the following fields must be set: 'ExpireTime', 'NoExpiry'. |
| 400 | ValidationException | NoExpiry cannot be set to false if no ExpireTime is provided | 'ExpireTime' must be set when 'NoExpiry' has value false. |
| 400 | ValidationException | ExpireTime cannot be set if NoExpiry is true | 'ExpireTime' must not be set when 'NoExpiry' has value true. |
| 400 | ValidationException | Expire time '<ExpireTimeValue>' is not a valid time format | 'ExpireTime' must follow the format YYYY-MM-DDThh:mm:ss.sssZ. |
| 400 | ValidationException | Expire time '<ExpireTimeValue>' cannot be in the past when creating a key | 'ExpireTime' must not be in the past. |
| 400 | ValidationException | Invalid token | 'NextToken' must be a valid token. |
| 400 | ValidationException | Expired token | 'NextToken' must not be expired. |
| 400 | ValidationException | The API Key %s has been recently used and the requested update may impact current usage. Specify ForceUpdate=true to update the API Key configuration. | This update may cause some users to lose API access. Because this API Key has been used in the last 7 days, you must set 'ForceUpdate' to true to confirm this change. |
| 400 | ValidationException | Expire time '<ExpireTimeValue>' must not be more than 1 minute in the past | 'ExpireTime' must not be more than 1 minute in the past. |
| 400 | ValidationException | Description, ExpireTime, NoExpiry and Restrictions can't all be empty | At least one of the following fields must be set: 'Description', 'ExpireTime', 'NoExpiry', 'Restrictions'. |
| 400 | ValidationException | API Key expired | 'ApiKeyId' must not be expired. |
| 409 | ConflictException | API key named <APIKeyName> already exists | Api key already exists: <APIKeyName>. |

## Geofences
<a name="location-actions-errorupdates-geofences"></a>

**Geofences**

| Error code | Exception | Old error message | New error message |
| --- | --- | --- | --- |
| 500 | InternalServerException | internal server error<br />Internal server error<br />Unsupported geofence geometry encountered<br />geometry marshal error<br />geometry load error<br />unable to get geofence collection<br />unable to delete geofences<br />unable to retrieve geofence<br />Error processing List request | Internal server error. Try again later. |
| 404 | ResourceNotFoundException | collection not found: <GeofenceCollectionName><br /><GeofenceCollectionName> geofence collection not found<br />Resource not found error<br />no geofence with given name found | Geofence Collection not found: <GeofenceCollectionName>. |
| 400 | ValidationException | unsupported price plan '<PricingPlan>' | 'PricingPlan' must be set to RequestBasedUsage. |
| 400 | ValidationException | KMS key must be a symmetric CMK. Invalid usage type: <UsageType> | KMS key must be a symmetric Customer Master Key (CMK). Invalid usage type <UsageType>. For how to create a symmetric CMK, refer to https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html\#create-symmetric-cmk. |
| 400 | ValidationException | Invalid token | 'NextToken' must be a valid token. |
| 400 | ValidationException | Expired token | 'NextToken' must not be expired. |
| 400 | ValidationException | PricingPlanDataSource cannot be updated without updating PricingPlan | 'PricingPlan' must be provided to update 'PricingPlanDataSource'. |
| 400 | ValidationException | nothing to update | At least one of the following fields must be set: 'Description' |
| 400 | ValidationException | invalid key state | KMS key must be a symmetric Customer Master Key (CMK). Invalid state <InvalidState>. For more information about how key state affects the use of a KMS key, see https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html. |
| 400 | ValidationException | key not found | Invalid KMS key. '<KmsKeyId>' <KmsKeyIdValue> not found. |
| 400 | ValidationException | key is disabled | Symmetric Customer Master Key (CMK) must be enabled. |
| 400 | ValidationException | access denied | Symmetric Customer Master Key (CMK) must allow Amazon Location to create grants to its KMS key. |
| 400 | ValidationException | duplicate geofence ID in batch | 'GeofenceId' <DuplicatedGeofenceID> is duplicated in batch. |
| 400 | ValidationException | missing GeofenceId | 'GeofenceId' must not be empty. |
| 400 | ValidationException | Invalid token | 'NextToken' must be a valid token. |
| 400 | ValidationException | Expired token | 'NextToken' must not be expired. |
| 400 | ValidationException | Position[0] must be between -180 and 180 | 'Position[0]' must be between -180 and 180. |
| 400 | ValidationException | Position[1] must be between -90 and 90 | 'Position[1]' must be between -90 and 90. |
| 400 | ValidationException | radius must be less than or equal to 1000km | 'Geometry.Circle.Radius' must be less than or equal to 1000km. |
| 400 | ValidationException | no geofence with given name found | Geofence not found: <CollectionName>. |
| 400 | ValidationException | Geometry must contain either a Circle or Polygon, not both | Only one of 'Circle' or 'Polygon' may be set within 'Geometry'. |
| 400 | ValidationException | Geometry must contain a Polygon or a Circle | One of 'Polygon' or 'Circle' must be set within 'Geometry'. |
| 400 | ValidationException | radius must be greater than 0m | 'Geometry.Circle.Radius' must be greater than 0m. |
| 400 | ValidationException | empty polygon | 'Geometry.Polygon' must not be empty. |
| 400 | ValidationException | empty polygon ring | 'Geometry.Polygon' must not be empty. |
| 400 | ValidationException | circle can not cross antimeridian | 'Geometry.Circle' must not cross antimeridian. Cut it in two such that neither part's representation crosses the antimeridian. |
| 400 | ValidationException | polygon can not cross antimeridian | 'Geometry.Polygon' must not cross antimeridian. Cut it in two such that neither part's representation crosses the antimeridian. |
| 400 | ValidationException | polygon can not have interior rings (holes), remove holes | 'Geometry.Polygon' must not have interior rings (holes). For more information about interior rings see https://www.rfc-editor.org/rfc/rfc7946.html\#appendix-A.3. |
| 400 | ValidationException | polygon ring is not closed | 'Geometry.Polygon' contains an open ring. Close the ring by ensuring the first and last positions are equal. |
| 400 | ValidationException | polygon ring has more than 1000 vertices | 'Geometry.Polygon' must not have more than 1000 vertices. |
| 400 | ValidationException | polygon ring has fewer than 4 positions | Number of vertices in 'Geometry.Polygon' must be greater or equal to 4. |
| 400 | ValidationException | invalid center | 'Geometry.Circle.Center' must be a valid position (longitude/latitude pair). |
| 400 | ValidationException | radius must be greater than 0m | 'Geometry.Circle.Radius' must be greater than 0 m. |
| 400 | ValidationException | longitude range should be between -180 and 180 degrees | Longitude must be between -180 and 180 degrees, but was set to <ProvidedLongitude>. |
| 400 | ValidationException | latitude range should be between -90 and 90 degrees | Latitude must be between -90 and 90 degrees, but was set to <ProvidedLongitude>. |
| 400 | ValidationException | polygon exterior ring is expected to be counter clockwise | 'Geometry.Polygon' must be oriented counter-clockwise. |
| 400 | ValidationException | polygon interior ring should be clockwise oriented | 'Geometry.Polygon' must be oriented clockwise. |
| 400 | ValidationException | radius must be less than or equal to 1000km | 'Geometry.Circle.Radius' must be less than or equal to 1000 km. |
| 400 | ValidationException | timestamp.Parse() error | 'SampleTime' must follow the format YYYY-MM-DDThh:mm:ss.sssZ. |
| 400 | ValidationException | invalid input | 'SourceArn' must refer to a tracker resource. |
| 400 | ValidationException | arn: invalid prefix | 'SourceArn' must be a valid ARN. For more information, see https://docs.aws.amazon.com/general/latest/gr/AWS-arns-and-namespaces.html. |
| 400 | ValidationException | arn: not enough sections | 'SourceArn' must be a valid ARN. For more information, see https://docs.aws.amazon.com/general/latest/gr/AWS-arns-and-namespaces.html. |
| 400 | ValidationException | invalid resource part | 'SourceArn' must refer to a tracker resource. |
| 402 | ServiceQuotaExceededException | Geofence collections per account exceeded quota limits. For more info, see https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/ | Geofence collection resources have exceeded the quota per account per region. For more information, see https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/. |
| 409 | ConflictException | collection already exists: <GeofenceCollectionName> | Geofence Collection already exists: <GeofenceCollectionName>. |
| 409 | ConflictException | Resource conflict error | Geofence already exists: <GeofenceName>. |
