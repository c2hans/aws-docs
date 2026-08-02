---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ApiKeyRestrictions.html
---

# ApiKeyRestrictions
<a name="API_ApiKeyRestrictions"></a>

API Restrictions on the allowed actions, resources, and referers for an API key resource.

## Contents
<a name="API_ApiKeyRestrictions_Contents"></a>

 ** AllowActions **   <a name="location-Type-ApiKeyRestrictions-AllowActions"></a>
A list of allowed actions that an API key resource grants permissions to perform. You must have at least one action for each type of resource. For example, if you have a place resource, you must include at least one place action.
The following are valid values for the actions.
+  **Map actions**
  +  `geo:GetMap*` - Allows all actions needed for map rendering.
  +  `geo-maps:GetTile` - Allows retrieving map tiles.
  +  `geo-maps:GetStaticMap` - Allows retrieving static map images.
  +  `geo-maps:*` - Allows all actions related to map functionalities.
+  **Place actions**
  +  `geo:SearchPlaceIndexForText` - Allows geocoding.
  +  `geo:SearchPlaceIndexForPosition` - Allows reverse geocoding.
  +  `geo:SearchPlaceIndexForSuggestions` - Allows generating suggestions from text.
  +  `GetPlace` - Allows finding a place by place ID.
  +  `geo-places:Geocode` - Allows geocoding using place information.
  +  `geo-places:ReverseGeocode` - Allows reverse geocoding from location coordinates.
  +  `geo-places:SearchNearby` - Allows searching for places near a location.
  +  `geo-places:SearchText` - Allows searching for places based on text input.
  +  `geo-places:Autocomplete` - Allows auto-completion of place names based on text input.
  +  `geo-places:Suggest` - Allows generating suggestions for places based on partial input.
  +  `geo-places:GetPlace` - Allows finding a place by its ID.
  +  `geo-places:*` - Allows all actions related to place services.
+  **Route actions**
  +  `geo:CalculateRoute` - Allows point to point routing.
  +  `geo:CalculateRouteMatrix` - Allows calculating a matrix of routes.
  +  `geo-routes:CalculateRoutes` - Allows calculating multiple routes between points.
  +  `geo-routes:CalculateRouteMatrix` - Allows calculating a matrix of routes between points.
  +  `geo-routes:CalculateIsolines` - Allows calculating isolines for a given area.
  +  `geo-routes:OptimizeWaypoints` - Allows optimizing the order of waypoints in a route.
  +  `geo-routes:SnapToRoads` - Allows snapping a route to the nearest roads.
  +  `geo-routes:*` - Allows all actions related to routing functionalities.
You must use these strings exactly. For example, to provide access to map rendering, the only valid action is `geo:GetMap*` as an input to the list. `["geo:GetMap*"]` is valid but `["geo:GetMapTile"]` is not. Similarly, you cannot use `["geo:SearchPlaceIndexFor*"]` - you must list each of the Place actions separately.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 24 items.
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `(geo|geo-routes|geo-places|geo-maps):\w*\*?`
Required: Yes

 ** AllowResources **   <a name="location-Type-ApiKeyRestrictions-AllowResources"></a>
A list of allowed resource ARNs that a API key bearer can perform actions on.
+ The ARN must be the correct ARN for a map, place, or route ARN. You may include wildcards in the resource-id to match multiple resources of the same type.
+ The resources must be in the same `partition`, `region`, and `account-id` as the key that is being created.
+ Other than wildcards, you must include the full ARN, including the `arn`, `partition`, `service`, `region`, `account-id` and `resource-id` delimited by colons (:).
+ No spaces allowed, even with wildcards. For example, `arn:aws:geo:region:account-id:map/ExampleMap*`.
For more information about ARN format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `.*(^arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))$)|(^arn(:[a-z0-9]+([.-][a-z0-9]+)*):(geo-routes|geo-places|geo-maps)(:((\*)|([a-z0-9]+([.-][a-z0-9]+)*)))::((provider[\/][*-._\w]+))$).*`
Required: Yes

 ** AllowAndroidApps **   <a name="location-Type-ApiKeyRestrictions-AllowAndroidApps"></a>
An optional list of allowed Android applications for which requests must originate from. Requests using this API key from other sources will not be allowed.
Type: Array of [AndroidApp](API_AndroidApp.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** AllowAppleApps **   <a name="location-Type-ApiKeyRestrictions-AllowAppleApps"></a>
An optional list of allowed Apple applications for which requests must originate from. Requests using this API key from other sources will not be allowed.
Type: Array of [AppleApp](API_AppleApp.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** AllowReferers **   <a name="location-Type-ApiKeyRestrictions-AllowReferers"></a>
An optional list of allowed HTTP referers for which requests must originate from. Requests using this API key from other domains will not be allowed.
Requirements:
+ Contain only alphanumeric characters (A–Z, a–z, 0–9) or any symbols in this list `$\-._+!*`(),;/?:@=&`
+ May contain a percent (%) if followed by 2 hexadecimal digits (A-F, a-f, 0-9); this is used for URL encoding purposes.
+ May contain wildcard characters question mark (?) and asterisk (\*).

  Question mark (?) will replace any single character (including hexadecimal digits).

  Asterisk (\*) will replace any multiple characters (including multiple hexadecimal digits).
+ No spaces allowed. For example, `https://example.com`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 253.
Pattern: `([\w!$&()*+,./:;=?@\x{60}-]|%([\dA-Fa-f]{2}|[\dA-Fa-f]?\*))+`
Required: No

## See Also
<a name="API_ApiKeyRestrictions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ApiKeyRestrictions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ApiKeyRestrictions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ApiKeyRestrictions)
