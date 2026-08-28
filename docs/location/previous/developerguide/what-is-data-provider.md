---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html
---

# What is a data provider?
<a name="what-is-data-provider"></a>

Use Amazon Location Service to access geolocation resources from multiple data providers through your AWS account without requiring third-party contracts or integrations. This can help you focus on building your application, without having to manage third-party accounts, credentials, licenses, and billing.

The following Amazon Location services use data providers.
+ ****Maps**** – Choose styles from different map providers when you [create a map resource](https://docs.aws.amazon.com/location/previous/developerguide/using-maps.html). You can use map resources to build an interactive map to visualize data.
+ ****Places**** – Choose a data provider when you [create a place index resource](https://docs.aws.amazon.com/location/previous/developerguide/places-prerequisites.html#create-place-index-resource) to support queries for geocoding, reverse geocoding, and searches.
+ ****Routes**** – Choose a data provider to support queries for route calculations in different geographies and applications when you [create a route calculator resource](https://docs.aws.amazon.com/location/previous/developerguide/routes-prerequisites.html#create-route-calculator-resource). With your chosen data provider, Amazon Location Service enables you to calculate routes based on up-to-date road network data, live traffic data, planned closures, and historic traffic patterns.

Each provider gathers and curates their data using different means. They may also have varying expertise in different regions of the world. This section provides details about our data providers. You may select any data provider based on your preference.

Make sure you read the terms of conditions when using Amazon Location Service data providers. For more information, see the [AWS Service Terms](https://aws.amazon.com/service-terms/). Also see the [Data privacy](data-privacy.md) section for more information about how Amazon Location protects your privacy.

## Map styles
<a name="data-provider-map-styles"></a>

Each data provider provides a set of map styles to render the map data that they provide. For example a style might include satellite imagery, or might be optimized to show the roads for navigation. You can find the list and examples of the styles for each provider in the following topics.
+ [Esri map styles](esri.md#esri-map-styles)
+ [Grab map styles](grab.md#grab-map-styles)
+ [HERE map styles](HERE.md#HERE-map-styles)
+ [Open Data map styles](open-data.md#open-data-map-styles)

## More information about each data provider
<a name="data-provider-details"></a>

The following links provide more information about each data provider.
+ [Esri](esri.md)
+ [GrabMaps](grab.md)
+ [HERE Technologies](HERE.md)
+ [Open Data](open-data.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
