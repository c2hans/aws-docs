---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/managing-place-indexes.html
---

# Managing your place index resources with Amazon Location
<a name="managing-place-indexes"></a>

You can manage your place index resources using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

## List your place index resources
<a name="viewing-place-indexes"></a>

You can view your place index resources list using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

------
#### [ Console ]

**To view a list of place index resources using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Place indexes** from the left navigation pane.

1. View a list of your place index resources under the **My place indexes**.

------
#### [ API ]

Use the `[ListPlaceIndexes](https://docs.aws.amazon.com/location-places/latest/APIReference/API_ListPlaceIndexes.html)` operation from the Amazon Location Places APIs.

The following example is an API request to get a list of place index resources in the AWS account.

```
POST /places/v0/list-indexes
```

The following is an example response for `[ListPlaceIndexes](https://docs.aws.amazon.com/location-places/latest/APIReference/API_ListPlaceIndexes.html)`:

```
{
   "Entries": [
      {
         "CreateTime": 2020-10-30T01:38:36Z,
         "DataSource": "Esri",
         "Description": "string",
         "IndexName": "{{ExamplePlaceIndex}}",
         "UpdateTime": 2020-10-30T01:40:36Z
      }
   ],
   "NextToken": "1234-5678-9012"
}
```

------
#### [ CLI ]

Use the `[list-place-indexes](https://docs.aws.amazon.com/cli/latest/reference/location/list-place-indexes.html)` command.

The following example is an AWS CLI to get a list of place index resources in the AWS account.

```
aws location list-place-indexes
```

------

## Get place index resource details
<a name="get-place-index-details"></a>

You can get details about any place index resource in your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

------
#### [ Console ]

**To view the details of a place index resource using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Place indexes** from the left navigation pane.

1. Under **My place indexes**, select the name link of the target place index resource.

------
#### [ API ]

Use the `[DescribePlaceIndex](https://docs.aws.amazon.com/location-places/latest/APIReference/API_DescribePlaceIndex.html)` operation from the Amazon Location Place APIs.

The following example is an API request to get the place index resource details for {{ExamplePlaceIndex}}.

```
GET /places/v0/indexes/{{ExamplePlaceIndex}}
```

The following is an example response for `[DescribePlaceIndex](https://docs.aws.amazon.com/location-places/latest/APIReference/API_DescribePlaceIndex.html)`:

```
{
   "CreateTime": 2020-10-30T01:38:36Z,
   "DataSource": "Esri",
   "DataSourceConfiguration": {
      "IntendedUse": "SingleUse"
   },
   "Description": "string",
   "IndexArn": "arn:aws:geo:us-west-2:123456789012:place-indexes/ExamplePlaceIndex",
   "IndexName": "{{ExamplePlaceIndex}}",
   "Tags": {
      "string" : "string"
   },
   "UpdateTime": 2020-10-30T01:40:36Z
}
```

------
#### [ CLI ]

Use the `[describe-place-index](https://docs.aws.amazon.com/cli/latest/reference/location/describe-place-index.html)` command.

The following example is an AWS CLI to get the place index resource details for {{ExamplePlaceIndex}}.

```
aws location describe-place-index \
    --index-name "{{ExamplePlaceIndex}}"
```

------

## Delete a place index resource
<a name="delete-place-index"></a>

You can delete a place index resource from your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

------
#### [ Console ]

**To delete a place index resource using the Amazon Location console**

**Warning**
This operation deletes the resource permanently.

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Place indexes** from the left navigation pane.

1. Under **My place index**, select the target place index resource.

1. Choose **Delete place index**.

------
#### [ API ]

Use the `[DeletePlaceIndex](https://docs.aws.amazon.com/location-places/latest/APIReference/API_DeletePlaceIndex.html)` operation from the Amazon Location Places APIs.

The following example is an API request to delete the place index resource {{ExamplePlaceIndex}}.

```
DELETE /places/v0/indexes/{{ExamplePlaceIndex}}
```

The following is an example success response for `[DeletePlaceIndex](https://docs.aws.amazon.com/location-places/latest/APIReference/API_DeletePlaceIndex.html)`:

```
HTTP/1.1 200
```

------
#### [ CLI ]

Use the `[delete-place-index](https://docs.aws.amazon.com/cli/latest/reference/location/delete-place-index.html)` command.

The following example is an AWS CLI command to delete the place index resource {{ExamplePlaceIndex}}.

```
aws location delete-place-index \
    --index-name "{{ExamplePlaceIndex}}"
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
