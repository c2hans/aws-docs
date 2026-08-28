---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/drawing-on-a-map.html
---

# Drawing data features on a map
<a name="drawing-on-a-map"></a>

After you have an application that renders a map, using Amplify, MapLibre, or Tangram to render the map, a natural next step is to draw features on top of the map. For example, you might want to render your customer locations as markers on the map.

In general, you can use the [Places search functions](searching-for-places.md) to find locations from your data, and then use the functionality of Amplify, MapLibre, or Tangram to render the locations.

To see samples of rendering different types of objects on map, see the following MapLibre samples:
+ [Example: Draw markers](example-draw-markers.md)
+ [Example: Draw clustered points](example-draw-clusters.md)
+ [Example: Draw a polygon](example-draw-polygon.md)

For more samples and tutorials, see [Code examples and tutorials for working with Amazon Location Service](samples.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
