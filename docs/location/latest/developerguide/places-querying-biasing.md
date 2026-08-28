---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/places-querying-biasing.html
---

# Querying and biasing
<a name="places-querying-biasing"></a>

Amazon Location Service Places API offers querying and biasing options to retrieve and search location data.

## Querying
<a name="places-querying"></a>

A query refers to the input parameters used to retrieve and search location data. The way APIs returns results is determined by these queries types.

| Filter Type | Geocode | Reverse Geocode | Autocomplete | Get Place | Search Text | Search Nearby | Suggest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QueryText | Yes | No | Yes | N/A | Yes | No | Yes |
| Query component  | Yes | No | No | N/A | No | No | No |
| Query Position  | No | Yes | No | N/A | No | Yes | No |
| Query Radius  | No | Yes | No | N/A | No | Yes | No |
| Query Id | No | No | No | N/A | No | No | No |
| Place Id | No | No | No | Yes | No | No | No |

## Biasing
<a name="places-biasing"></a>

The "bias position" is a location that influences search results, giving priority to places near biased position. It doesn't restrict results, but biases them toward the specified area. This feature prioritizes relevant location results when multiple places have similar names.

| Filter Type | Geocode | Reverse Geocode | Autocomplete | Get Place | Search Text | Search Nearby | Suggest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BiasPosition | Yes | No | Yes | N/A | Yes | No | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
