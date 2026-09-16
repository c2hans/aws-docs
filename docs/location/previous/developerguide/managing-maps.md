---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/managing-maps.html
---

# Managing your map resources (V1)
<a name="managing-maps"></a>

**Important**
**This page documents the previous Maps API (V1). Use it only for existing applications.** The Maps V2 API is the latest version. Use it for all new applications; see the latest [Amazon Location Service Maps](https://docs.aws.amazon.com/location/latest/developerguide/maps.html) developer guide.
The latest API calls `GetTile`, `GetStyleDescriptor`, `GetStaticMap`, `GetSprites`, and `GetGlyphs` directly. These operations are under the `geo-maps` namespace. They are exposed as `@aws-sdk/client-geo-maps` for JavaScript and `boto3.client('geo-maps')` for Python.
There is no `Map` resource to create, describe, or delete.

This topic covers the management and configuration of maps within the Amazon Location Service. It explains how to create and customize map resources, enabling you to tailor the mapping experience for your location-based applications.

You can manage your map resources using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

## List map resources
<a name="viewing-maps"></a>

You can view a list of your map resources using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To view a list of existing map resources using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Maps ** from the left navigation pane.

1. View a list of your map resources under **My maps**.

------
#### [ API ]

Use the `[ListMaps](https://docs.aws.amazon.com/location/previous/APIReference/API_ListMaps.html)` operation from the Amazon Location Maps APIs.

The following example is an API request to get a list of map resources in the AWS account.

```
POST /maps/v0/list-maps
```

The following is an example response for `[ListMaps](https://docs.aws.amazon.com/location/previous/APIReference/API_ListMaps.html)`:

```
{
   "Entries": [
      {
         "CreateTime": 2020-10-30T01:38:36Z,
         "DataSource": "Esri",
         "Description": "string",
         "MapName": "{{ExampleMap}}",
         "UpdateTime": 2020-10-30T01:38:36Z
      }
   ],
   "NextToken": "1234-5678-9012"
}
```

------
#### [ CLI ]

Use the `[list-map](https://docs.aws.amazon.com/cli/latest/reference/location/list-maps.html)` command.

The following example is an AWS CLI to get a list of map resources in the AWS account.

```
aws location list-maps
```

------

## Get map resource details
<a name="get-map-details"></a>

You can get details about any map resource in your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To view the details of a map resource using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Maps ** from the left navigation pane.

1. Under **My maps**, select the name link of the target map resource.

------
#### [ API ]

Use the `[DescribeMap](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeMap.html)` operation from the Amazon Location Maps APIs.

The following example is an API request to get the map resource details for {{ExampleMap}}.

```
GET /maps/v0/maps/{{ExampleMap}}
```

The following is an example response for `[DescribeMap](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeMap.html)`:

```
{
   "Configuration": {
      "Style": "VectorEsriNavigation"
   },
   "CreateTime": 2020-10-30T01:38:36Z,
   "DataSource": "Esri",
   "Description": "string",
   "MapArn": "arn:aws:geo:us-west-2:123456789012:maps/ExampleMap",
   "MapName": "{{ExampleMap}}",
   "Tags": {
      "Tag1" : "Value1"
   },
   "UpdateTime": 2020-10-30T01:40:36Z
}
```

------
#### [ CLI ]

Use the `[describe-map](https://docs.aws.amazon.com/cli/latest/reference/location/describe-map.html)` command.

The following example is an AWS CLI to get the map resource details for {{ExampleMap}}.

```
aws location describe-map \
    --map-name "{{ExampleMap}}"
```

------

## Delete a map resource
<a name="delete-maps"></a>

You can delete a map resource from your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

**Warning**
This operation deletes the resource permanently.

------
#### [ Console ]

**To delete an existing map resource using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Maps ** from the left navigation pane.

1. Under **My maps** list, select the target map from the list.

1. Choose **Delete map**.

------
#### [ API ]

Use the `[DeleteMap](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteMap.html)` operation from the Amazon Location Maps APIs.

The following example is an API request to delete the map resource {{ExampleMap}}.

```
DELETE /maps/v0/maps/{{ExampleMap}}
```

The following is an example success response for `[DeleteMap](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteMap.html)`:

```
HTTP/1.1 200
```

------
#### [ CLI ]

Use the `[delete-map](https://docs.aws.amazon.com/cli/latest/reference/location/delete-map.html)` command.

The following example is an AWS CLI command to delete the map resource {{ExampleMap}}.

```
aws location delete-map \
    --map-name "{{ExampleMap}}"
```

------
