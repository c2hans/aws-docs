---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/how-to-create-logistic-map.html
---

# How to create a logistics map
<a name="how-to-create-logistic-map"></a>

The TravelModes feature lets you build logistic maps using Amazon Location Service. TravelModes displays relevant routing information for Truck navigation with related road restrictions. Use [Transit TravelMode](https://docs.aws.amazon.com/location/latest/developerguide/how-to-show-transit-details-map.html) to show public transportation details.

## Create a map with Truck TravelMode
<a name="how-to-create-truck-map"></a>

This example shows how to create a map with `Truck` `TravelMode` for logistic routing.

### Truck example
<a name="how-to-create-truck-map-code"></a>

------
#### [ index.html ]

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Truck Map</title>
        <meta charset='utf-8'>
            <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css' />
                <script src='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js'></script>
    </head>
    <body style="margin: 0; padding: 0;">
        <div id="map" style="width: 100%; height: 100vh;"></div>
        <script>
            const apiKey = "Add Your Api Key";
            const mapStyle = "Standard";
            const awsRegion = "us-east-1";

            const map = new maplibregl.Map({
                container: 'map',
                style: `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?travel-modes=Truck&key=${apiKey}`,
                center: [-74.0060 ,40.7128],
                zoom: 12,
                validateStyle: false, // Disable style validation for faster map load
            });
        </script>
    </body>
</html>
```

------
#### [ style.css ]

```
body {
    margin: 0;
    padding: 0;
}

#map {
    width: 100%;
    height: 100vh;
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
