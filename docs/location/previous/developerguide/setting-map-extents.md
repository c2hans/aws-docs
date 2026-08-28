---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/setting-map-extents.html
---

# Setting extents for a map using MapLibre
<a name="setting-map-extents"></a>

There are times that you do not want your users to be able to pan or zoom around the entire world. If you are using MapLibre's map control, you can limit the *extents*, or *bounds*, of the map control with the `maxBounds` option, and constrain the zoom with `minZoom` and `maxZoom` options.

The following code example shows how to initialize the map control to constrain panning to a specific boundary (in this case, the extents of the Grab data source).

**Note**
These samples are in JavaScript, and work within the context of the [Create a web app to use Amazon Location Service](qs-web.md) tutorial.

```
// Set bounds to Grab data provider region
var bounds = [
        [90.0, -21.943045533438166], // Southwest coordinates
        [146.25, 31.952162238024968] // Northeast coordinates
    ];

var mlglMap = new maplibregl.Map(
    {
    container: 'map',
    style: mapName,
    maxBounds: bounds // Sets bounds as max
    transformRequest,
    }
);
```

Similarly, you can set a minimum and maximum zoom level for the map. The values for both can be between 0 and 24, although the defaults are 0 for minimum zoom and 22 for maximum (data providers may not provide data at all zoom levels. Most map libraries handle this automatically). The following example initializes the `minZoom` and `maxZoom` options on the MapLibre Map control.

```
// Set the minimum and maximum zoom levels
var mlglMap = new maplibregl.Map(
    {
    container: 'map',
    style: mapName,
    maxZoom: 12,
    minZoom: 5,
    transformRequest,
    }
);
```

**Tip**
The MapLibre Map control also allows setting these options at runtime, rather than during initialization, with `get...` and `set...` functions. For example, use `getMaxBounds` and `setMaxBounds` to change the map bounds at runtime.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
