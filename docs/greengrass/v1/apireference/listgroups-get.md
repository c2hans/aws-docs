---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/listgroups-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ListGroups
<a name="listgroups-get"></a>

Retrieves a list of groups.

URI: `GET /greengrass/groups`

Produces: application/json

## CLI:
<a name="listgroups-get-cli"></a>

```
aws greengrass list-groups \
  [--max-results <value>] \
  [--next-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"MaxResults": "integer",
"NextToken": "string"
}
```

## Parameters:
<a name="listgroups-get-params"></a>

[**MaxResults**](parameters-maxresultsparam.md)
The maximum number of results to be returned per request.
where used: query; required: false
type: integer

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

## Responses:
<a name="listgroups-get-resp"></a>

**200** (ListGroupsResponse)

 [ ListGroupsResponse](definitions-listgroupsresponse.md)

```
{
"Groups": [
  {
    "Name": "string",
    "Id": "string",
    "Arn": "string",
    "LastUpdatedTimestamp": "string",
    "CreationTimestamp": "string",
    "LatestVersion": "string",
    "LatestVersionArn": "string"
  }
],
"NextToken": "string"
}
```
ListGroupsResponse
type: object
Groups
Information about a group.
type: array
items: [GroupInformation](definitions-groupinformation.md)
GroupInformation
Information about a group.
type: object
Name
The name of the group.
type: string
Id
The ID of the group.
type: string
Arn
The ARN of the group.
type: string
LastUpdatedTimestamp
The time, in milliseconds since the epoch, when the group was last updated.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the group was created.
type: string
LatestVersion
The ID of the latest version associated with the group.
type: string
LatestVersionArn
The ARN of the latest version associated with the group.
type: string
NextToken
The token for the next set of results, or `null` if there are no more results.
type: string
