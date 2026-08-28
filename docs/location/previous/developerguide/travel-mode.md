---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/travel-mode.html
---

# Travel mode with Amazon Location
<a name="travel-mode"></a>

You can set a travel mode when using `CalculateRoute` or `CalculateRouteMatrix`. The mode of travel affects speed of travel and road compatibility. While the default mode of travel is by car, you can specify which mode of travel you're using while traveling along a route with the following optional parameter:
+ `TravelMode` – Specifies the mode of transport when calculating a route, such as: {{`Bicycle`}}, {{`Car`}}, {{`Motorcycle`}}, {{`Truck`}}, or {{`Walking`}}.

**Limitations**
+ If you specify `Walking` for the travel mode and your data provider is Esri, the start and destination must be within 40km.
+ `Bicycle` or `Motorcycle` are available only when using Grab as the data provider.
+ Grab provides only `Bicycle` and `Walking` routes in certain cities. For more information, see [Countries/regions and area covered](grab.md#grab-coverage-area).
+ `Truck` is not available when using Grab as the data provider.

**Additional preferences**

If you specify a `TravelMode` of {{`Car`}}, you can specify additional route preferences with the following optional parameter:
+ `CarModeOptions` – Specifies route preferences when traveling in a car, such as {{`AvoidFerries`}} or {{`AvoidTolls`}}.

If you specify a `TravelMode` of {{`Truck`}}, you can specify additional route preferences with the following optional parameter:
+ `TruckModeOptions` – Specifies route preferences when traveling in a truck, such as {{`AvoidFerries`}} or {{`AvoidTolls`}}, in addition to specifying routes that can accommodate the {{`TruckDimensions`}} and {{`TruckWeight`}}.

**Example**
The following `[CalculateRoute](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CalculateRoute.html)` request specifies {{`Truck`}} as the mode of travel. Additional route restrictions include: avoiding routes that use ferries and avoiding roads that can't accommodate the truck dimensions and weight.

```
{
   "DeparturePosition": [-122.7565,49.0021],
   "DestinationPosition": [-122.3394, 47.6159],
   "DepartNow": true,
   "TravelMode": "{{Truck}}",
   "TruckModeOptions": {
      "AvoidFerries": {{true}},
      "AvoidTolls": {{false}},
      "Dimensions": {
         "Height": {{4.5}},
         "Length": {{15.5}},
         "Unit": "{{Meters}}",
         "Width": {{4.5}}
      },
      "Weight": {
         "Total": {{7500}},
         "Unit": "{{Pounds}}"
      }
   }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
