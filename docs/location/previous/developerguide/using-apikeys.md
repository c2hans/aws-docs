---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html
---

# Allow unauthenticated guest access to your application using API keys
<a name="using-apikeys"></a>

When you call Amazon Location Service APIs in your applications, you typically make this call as an *authenticated user* who is authorized to make the API calls. However, there are some cases where you do not want to authenticate every user of your application. For example, you might want a web application that shows your business location to be available to anyone using the website, whether they are logged in or not. In this case, one alternative is to use API keys to make the API calls.

*API keys* are a key value that is associated with specific Amazon Location Service resources in your AWS account, and specific actions that you can perform on those resources. You can use an API key in your application to make unauthenticated calls to the Amazon Location APIs for those resources. For example, if you associate an API key with the map resource *myMap*, and the `GetMap*` actions, then an application that uses that API key will be able to view maps created with that resource, and your account will be charged as any other usage from your account. That same API key would not give permissions to change or update the map resource—only using the resource is allowed.

**Note**
API keys are available to use only with **map**, **place**, and **route** resources, and you cannot modify or create those resources. If your application needs access to other resources or actions for unauthenticated users, you can use Amazon Cognito to provide access along with, or instead of, API keys. For more information, see [Allow unauthenticated guest access to your application using Amazon Cognito](authenticating-using-cognito.md).

API keys include a plain text *value* that gives access to one or more resources in your AWS account. If someone copies your API key, they can access those same resources. To avoid this, you can specify the domains where the API key can be used when you create the key. These domains are called referers. If needed, you can also create short term API Keys by setting expiration times for your API Keys.

**Topics**
+ [API keys compared to Amazon Cognito](#using-apikeys-vs-cognito)
+ [Create API keys](#using-apikeys-create)
+ [Use an API key to call an Amazon Location API](#using-apikeys-in-api)
+ [Use an API key to render a map](#using-apikeys-in-maps)
+ [Manage API key lifetimes](#using-apikeys-expirations)

## API keys compared to Amazon Cognito
<a name="using-apikeys-vs-cognito"></a>

API keys and Amazon Cognito are used in similar ways for similar scenarios, so why would you use one over the other? The following list highlights some of the differences between the two.
+ API keys are available only for map, place, and route resources, and only for certain actions. Amazon Cognito can be used to authenticate access to most Amazon Location Service APIs.
+ The performance of map requests with API keys is typically faster than similar scenarios with Amazon Cognito. Simpler authentication means fewer round trips to the service and cached requests when getting the same map tile again in a short time period.
+ With Amazon Cognito, you can use your own authentication process or combine multiple authentication methods, using Amazon Cognito Federated Identities. For more information, see [Getting Started with Federated Identities](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-identity-pools.html) in the *Amazon Cognito Developer Guide*.

## Create API keys
<a name="using-apikeys-create"></a>

You can create an API key, and associate it with one or more resources in your AWS account.

You can create an API key using the Amazon Location Service console, the AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To create an API key using the Amazon Location Service console**

1. In the [**Amazon Location console**](https://console.aws.amazon.com/location), choose **API keys** from the left menu.

1. On the **API keys** page, choose **Create API key**.

1. On the **Create API key **page, fill in the following information:
   + **Name** – A name for your API key, such as `MyWebAppKey`.
   + **Description** – An optional description for your API key.
   + **Resources** – Choose the Amazon Location resources to give access to with this API key from the dropdown. You can add more than one resource by choosing **Add resource**.
   + **Actions** – Specify the actions you want to authorize with this API key. You must select at least one action to match each resource type you have selected. For example, if you selected a place resource, you must select at least one of the choices under **Places Actions**.
   + **Expiration time** – Optionally, add an expiration date and time for your API key. For more information, see [Manage API key lifetimes](#using-apikeys-expirations).
   + **Referers** – Optionally, add one or more domains where you can use the API key. For example, if the API key is to allow an application running on the website `example.com`, then you could put `*.example.com/` as an allowed referer.
   + **Tags** – Optionally, add tags to the API key.

1. Choose **Create API key** to create the API key.

1. On the detail page for the API key, you can see information about the API key that you have created. Choose **Show API key** to see the key value that you use when calling Amazon Location APIs. The key value will have the format `v1.public.{{a1b2c3d4...}}`. For more information about using the API key to render maps, see [Use an API key to render a map](#using-apikeys-in-maps).

------
#### [ API ]

**To create an API key using the Amazon Location APIs**

Use the `[CreateKey](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateKey.html)` operation from the Amazon Location APIs.

The following example is an API request to create an API key called {{ExampleKey}} with no expiration date, and access to a single map resource.

```
POST /metadata/v0/keys HTTP/1.1
Content-type: application/json

{
   "KeyName": "{{ExampleKey}}"
   "Restrictions": {
      "AllowActions": [
         "geo:GetMap*"
      ],
      "AllowResources": [
         "arn:aws:geo:{{region}}:{{account}}:map/{{mapname}}"
      ]
   },
   "NoExpiry": {{true}}
   }
}
```

The response includes the API key value to use when accessing resources in your applications. The key value will have the format `v1.public.{{a1b2c3d4...}}`. To learn more about using the API key to render maps, see [Use an API key to render a map](#using-apikeys-in-maps).

You can also use the `[DescribeKey](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeKey.html)` API to find the key value for a key at a later time.

------
#### [ AWS CLI ]

**To create an API key using AWS CLI commands**

Use the `[create-key](https://docs.aws.amazon.com/cli/latest/reference/location/create-key.html)` command.

The following example creates an API key called {{ExampleKey}} with no expiration date, and access to a single map resource.

```
aws location \
  create-key \
  --key-name {{ExampleKey}} \
  --restrictions '{"AllowActions":["geo:GetMap*"],"AllowResources":["arn:aws:geo:{{region}}:{{account}}:map/{{mapname}}"]}' \
  --no-expiry
```

The response includes the API key value to use when accessing resources in your applications. The key value will have the format `v1.public.{{a1b2c3d4...}}`. To learn more about using the API key to render maps, see [Use an API key to render a map](#using-apikeys-in-maps). The response to `create-key` looks like the following.

```
{
    "Key": "v1.public.{{a1b2c3d4...}}",
    "KeyArn": "arn:aws:geo:{{region}}:{{account}}:api-key/{{ExampleKey}}",
    "KeyName": "{{ExampleKey}}",
    "CreateTime": "2023-02-06T22:33:15.693Z"
}
```

You can also use `describe-key` to find the key value at a later time. The following example shows how to call `describe-key` on an API key named {{ExampleKey}}.

```
aws location describe-key \
    --key-name {{ExampleKey}}
```

------

## Use an API key to call an Amazon Location API
<a name="using-apikeys-in-api"></a>

After you create an API key, you can use the key value to make calls to Amazon Location APIs in your application.

The APIs that support API keys have an additional parameter that takes the API key value. For example, if you call the `GetPlace` API, you can fill in the [key](https://docs.aws.amazon.com/location/previous/APIReference/API_GetPlace.html#API_GetPlace_RequestSyntax) parameter, as follows

```
GET /places/v0/indexes/{{IndexName}}/places/{{PlaceId}}?key={{KeyValue}}
```

If you fill in this value, you do not need to authenticate the API call with AWS Sig v4 as you normally would.

For JavaScript developers, you can use the Amazon Location [JavaScript Authentication helper](loc-sdk-auth.md) to help with authenticating API operations with API keys.

For mobile developers, you can use the following Amazon Location mobile authentication SDKs:
+ [Amazon Location Service Mobile Authentication SDK for iOS](https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios/)
+ [Amazon Location Service Mobile Authentication SDK for Android](https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-android/)

For AWS CLI users, when you use the `--key` parameter, you should also use the `--no-sign-request` parameter, to avoid signing with Sig v4.

**Note**
If you include both a `key` and an AWS Sig v4 signature in a call to Amazon Location Service, only the API key is used.

## Use an API key to render a map
<a name="using-apikeys-in-maps"></a>

You can use the API key value to render a map in your application using MapLibre. This is a little bit different than using the API keys in other Amazon Location APIs that you are calling directly, because MapLibre makes those calls for you.

The following sample code shows using the API key to render a map in a simple webpage by using the MapLibre GL JS map control. For this code to work properly, replace the {{v1.public.your-api-key-value}}, {{us-east-1}}, and {{ExampleMap}} strings with values that match your AWS account.

```
<!-- index.html -->
<html>
  <head>
    <link href="https://unpkg.com/maplibre-gl@1.14.0/dist/maplibre-gl.css" rel="stylesheet" />
    <style>
      body { margin: 0; }
      #map { height: 100vh; }
    </style>
  </head>
  <body>
    <!-- Map container -->
    <div id="map" />
    <!-- JavaScript dependencies -->
    <script src="https://unpkg.com/maplibre-gl@1.14.0/dist/maplibre-gl.js"></script>
    <script>
      const apiKey = "{{v1.public.your-api-key-value}}"; // API key
      const region = "{{us-east-1}}"; // Region
      const mapName = "{{ExampleMap}}"; // Map name
      // URL for style descriptor
      const styleUrl = `https://maps.geo.${region}.amazonaws.com/maps/v0/maps/${mapName}/style-descriptor?key=${apiKey}`;
      // Initialize the map
      const map = new maplibregl.Map({
        container: "map",
        style: styleUrl,
        center: [-123.1187, 49.2819],
        zoom: 11,
      });
      map.addControl(new maplibregl.NavigationControl(), "top-left");
    </script>
  </body>
</html>
```

## Manage API key lifetimes
<a name="using-apikeys-expirations"></a>

You can create API keys that work indefinitely. However, if you want to create a temporary API key, rotate API keys on a regular basis, or revoke an existing API key, you can use *API key expiration*.

When creating a new API key, or updating an existing one, you can set the expiration time for that API key.
+ When an API key reaches its expiration time, the key is automatically deactivated. Inactive keys can no longer be used to make maps requests.
+ You can delete an API key 90 days after deactivating it.
+ If you have an inactive key that you haven't yet deleted, you can restore it by updating the expiration time to a future time.
+ To create a permanent key, you can remove the expiration time.
+ If you attempt to deactivate an API key that has been used within the last 7 days, you'll be prompted to confirm that you want to make the change. If you are using the Amazon Location Service API, or the AWS CLI, you will receive an error, unless you set `ForceUpdate` parameter to true.
