---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

## Amazon Location Service Routes V2
<a name="Welcome_Amazon_Location_Service_Routes_V2"></a>

With the Routes API you can calculate routes and estimate travel time based on up-to-date road network and live traffic information. Key features include:
+ Point-to-point routing with estimated travel time, distance, and turn-by-turn directions. See [CalculateRoutes](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRoutes.html).
+ Multi-point route optimization to minimize travel time or distance. See [OptimizeWaypoints](https://docs.aws.amazon.com/location/latest/APIReference/API_OptimizeWaypoints.html).
+ Route matrices for efficient multi-destination planning. See [CalculateRouteMatrix](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRouteMatrix.html).
+ Isoline calculations to determine reachable areas within specified time or distance thresholds. See [CalculateIsolines](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateIsolines.html).
+ Map-matching to align GPS traces with the road network. See [SnapToRoads](https://docs.aws.amazon.com/location/latest/APIReference/API_SnapToRoads.html).

## Amazon Location Service Maps V2
<a name="Welcome_Amazon_Location_Service_Maps_V2"></a>

 Integrate high-quality base map data into your applications using [MapLibre](https://maplibre.org). Capabilities include:
+ Access to comprehensive base map data, allowing you to tailor the map display to your specific needs. See [GetTile](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetTile.html).
+ Multiple pre-designed map styles suited for various application types, such as navigation, logistics, or data visualization. See [GetStyleDescriptor](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStyleDescriptor.html).
+ Generation of static map images for scenarios where interactive maps aren't suitable. See [GetStaticMap](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStaticMap.html). Use cases include:
  + Embedding in emails or documents
  + Displaying in low-bandwidth environments
  + Creating printable maps
  + Enhancing application performance by reducing client-side rendering

## Amazon Location Service Places V2
<a name="Welcome_Amazon_Location_Service_Places_V2"></a>

 The Places API enables powerful location search and geocoding capabilities for your applications, offering global coverage with rich, detailed information. Key features include:
+ Forward and reverse geocoding for addresses and coordinates. See [Geocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Geocode.html) and [ReverseGeocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocode.html).
+ Comprehensive place searches with detailed information. See [SearchText](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchText.html), [SearchNearby](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearby.html), and [GetPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GetPlace.html). Place information you can find include:
  + Business names and addresses
  + Contact information
  + Hours of operation
  + Points of Interest (POI) categories
  + Food types for restaurants
  + Chain affiliation for relevant businesses
+ Address and place completion as users type, enhancing input efficiency by completing partial queries with valid addresses. See [Autocomplete](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Autocomplete.html).
+ Intelligent place and query recommendation based on user's input or context, returning relevant places, points of interest, query terms, or search categories. See [Suggest](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Suggest.html).
+ Global data coverage with a wide range of POI categories.
+ Regular data updates to ensure accuracy and relevance.
+ Bulk address validation for verifying and standardizing large volumes of addresses in a single operation using [Amazon Location Service Jobs](https://docs.aws.amazon.com/location/latest/APIReference/Welcome.html#Welcome_Amazon_Location_Service_Jobs).

## Amazon Location Service API Keys
<a name="Welcome_Amazon_Location_Service_API_Keys"></a>

Use API key authentication in Amazon Location Service to manage and authenticate API key resources that grant access to Amazon Location APIs. API keys let you grant actions for Amazon Location resources to the API key bearer.

For more information about [using API keys to authenticate](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html), see the Amazon Location Service Developer Guide.

## Amazon Location Service Jobs
<a name="Welcome_Amazon_Location_Service_Jobs"></a>

Amazon Location Service Jobs provide asynchronous bulk processing capabilities that enable you to validate and standardize large volumes of addresses efficiently and cost-effectively. Instead of making individual API calls for each address, you can process thousands of addresses in a single operation using the Jobs API.

The Jobs API introduces a new paradigm for address validation within Amazon Location Service, allowing you to submit bulk operations that run asynchronously in the background. You upload your address data to Amazon S3, submit a job through the API, and retrieve standardized results when processing is complete.

## Amazon Location Service Tags
<a name="Welcome_Amazon_Location_Service_Tags"></a>

Use resource tagging in Amazon Location Service to create tags to categorize your resources by purpose, owner, environment, or criteria. Tagging your resources helps you manage, identify, organize, search, and filter your resources.

For more information about [tagging your Amazon Location resources](https://docs.aws.amazon.com/location/latest/developerguide/manage-resources.html), see the Amazon Location Service Developer Guide. It provides definitions, tutorials, code examples, and instructions about how to integrate Amazon Location features into your application.

## Amazon Location Service Geofences
<a name="Welcome_Amazon_Location_Service_Geofences"></a>

Amazon Location Geofences lets you give your application the ability to detect and act when a tracked device enters or exits a defined geographical boundary known as a geofence.

With Amazon Location Geofences, you can automatically send an exit or entry event to Amazon EventBridge when a geofence breach is detected. This lets you trigger downstream actions such as sending a notification to a target. For additional information, see the [Amazon Location Service Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html). It provides definitions, tutorials, code examples, and instructions about how to integrate features into web or mobile apps.

## Amazon Location Service Trackers
<a name="Welcome_Amazon_Location_Service_Trackers"></a>

Use trackers to store position updates for a collection of devices. The tracker can be used to query the devices' current location or location history. It stores the updates, but reduces storage space and visual noise by filtering the locations before storing them.

For more information, see the [Amazon Location Service Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html). It provides definitions, tutorials, code examples, and instructions about how to integrate Amazon Location features into your application.
