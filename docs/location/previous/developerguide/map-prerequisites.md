---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/map-prerequisites.html
---

# Prerequisites for using Amazon Location maps
<a name="map-prerequisites"></a>

Before you start utilizing the mapping capabilities of Amazon Location Service, there are a few prerequisites that need to be fulfilled. This page outlines the necessary steps and requirements to ensure a smooth integration of interactive maps into your applications.

## Create a map resource
<a name="create-map-resource"></a>

To use a map in your application you must have a map resource, which specifies the map style and data provider to use in your maps.

**Note**
The latest API has no map resource and no data provider to select at resource-creation time. For new code, request tiles and styles directly with [`GetTile`](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetTile.html) and [`GetStyleDescriptor`](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStyleDescriptor.html) under `geo-maps`. See the latest [Amazon Location Service Maps](https://docs.aws.amazon.com/location/latest/developerguide/maps.html) developer guide.

**Note**
If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the [AWS service terms](https://aws.amazon.com/service-terms) for more details.

You can create a map resource using the Amazon Location Service console, the AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To create a map resource using the Amazon Location Service console**

1. In the Amazon Location console, on the [**Maps**](https://console.aws.amazon.com/location/maps/home) page, choose **Create map** to preview map styles.

1. Add a name and description for the new map resource.

1. Choose a map style.
**Note**
If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the [AWS service terms](https://aws.amazon.com/service-terms) for more details.

1. Choose from the [Political views](map-concepts.md#political-views) to use.

1. Agree to the **Amazon Location Terms and Conditions**, then choose **Create map**. You can interact with the map that you've chosen: zoom in, zoom out, or pan in any direction.

1. To allow your users to switch styles (for example, to allow them to switch between satellite imagery and vector style), you must create a map resource for each style.

   You can delete resources with map styles that you don’t want to use on the [Maps home page](https://console.aws.amazon.com/location/maps/home) in the console.

------
#### [ API ]

**To create a map resource using the Amazon Location APIs**

Use the `[CreateMap](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateMap.html)` operation from the Amazon Location APIs.

The following example is an API request to create a map resource called {{ExampleMap}} using the {{VectorEsriStreets}} map style.

```
POST /maps/v0/maps HTTP/1.1
Content-type: application/json

{
   "Configuration": {
      "Style": "{{VectorEsriStreets}}"
   },
   "MapName": "{{ExampleMap}}"
   }
}
```

**Note**
If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the [AWS service terms](https://aws.amazon.com/service-terms) for more details.

------
#### [ AWS CLI ]

**To create a map resource using AWS CLI commands**

Use the `[create-map](https://docs.aws.amazon.com/cli/latest/reference/location/create-map.html)` command.

The following example creates a map resource called {{ExampleMap}} using {{VectorEsriStreets}} as the map style.

```
aws location \
  create-map \
  --configuration Style="{{VectorEsriStreets}}" \
  --map-name "{{ExampleMap}}"
```

**Note**
If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the [AWS service terms](https://aws.amazon.com/service-terms) for more details.

------

## Authenticating your requests
<a name="using-maps-set-up-authentication"></a>

Once you create a map resource and you're ready to begin building location features into your application, you need to choose how you would authenticate your requests.

**Note**
Most maps front end applications require unauthenticated access to the maps or other features of Amazon Location Service. Depending on your application, you might want to use AWS Signature v4 to authenticate requests, or you can use Amazon Cognito or Amazon Location API keys for unauthenticated use. To learn more about all of these options, see [Grant access to Amazon Location Service](how-to-access.md).
