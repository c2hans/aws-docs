---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/managing-route-calculators.html
---

# Managing your route calculator resources (V1)
<a name="managing-route-calculators"></a>

**Important**
**This page documents the previous Routes API (V1). Use it only for existing applications.** The Routes V2 API is the latest version. Use it for all new applications; see the latest [Amazon Location Service Routes](https://docs.aws.amazon.com/location/latest/developerguide/routes.html) developer guide.
The latest API calls `CalculateRoutes` (plural) directly. This operation is under the `geo-routes` namespace. It is exposed as `@aws-sdk/client-geo-routes` for JavaScript and `boto3.client('geo-routes')` for Python.
There is no `RouteCalculator` resource to create, describe, or delete.

You can manage your route calculator resources using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

## List your route calculator resources
<a name="viewing-route-calculators"></a>

You can view your route calculator list using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

------
#### [ Console ]

**To view a list of route calculators using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Route calculators** from the left navigation pane.

1. View the route calculator details under **My route calculators**.

------
#### [ API ]

Use the `[ListRouteCalculators](https://docs.aws.amazon.com/location/previous/APIReference/API_ListRouteCalculators.html)` operation from the Amazon Location Routes APIs.

The following example is an API request to get a list of route calculators in the AWS account.

```
POST /routes/v0/list-calculators
```

The following is an example response for `[ListRouteCalculators](https://docs.aws.amazon.com/location/previous/APIReference/API_ListRouteCalculators.html)`:

```
{
       "Entries": [
          {
             "CalculatorName": "{{ExampleCalculator}}",
             "CreateTime": 2020-09-30T22:59:34.142Z,
             "DataSource": "Esri",
             "Description": "string",
             "UpdateTime": 2020-09-30T23:59:34.142Z
          }
       ],
       "NextToken": "1234-5678-9012"
    }
```

------
#### [ CLI ]

Use the `list-route-calculators` command.

The following example is an AWS CLI to get a list of route calculators in the AWS account.

```
aws location list-route-calculators
```

------

## Get route calculator details
<a name="get-route-calculator-details"></a>

You can get details about any route calculator resource in your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

------
#### [ Console ]

**To view the details of a route calculator using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Route calculators** from the left navigation pane.

1. Under **My route calculators**, select the name link of the target route calculator.

------
#### [ API ]

Use the `[DescribeRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeRouteCalculator.html)` operation from the Amazon Location Routes APIs.

The following example is an API request to get the route calculator details for {{ExampleCalculator}}.

```
GET /routes/v0/calculators/{{ExampleCalculator}}
```

The following is an example response for `[DescribeRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeRouteCalculator.html)`:

```
{
       "CalculatorArn": "arn:aws:geo:us-west-2:123456789012:route-calculator/{{ExampleCalculator}}",
       "CalculatorName": "{{ExampleCalculator}}",
       "CreateTime": 2020-09-30T22:59:34.142Z,
       "DataSource": "Esri",
       "Description": "string",
       "Tags": {
          "Tag1" : "Value1"
       },
       "UpdateTime": 2020-09-30T23:59:34.142Z
    }
```

------
#### [ CLI ]

Use the `describe-route-calculator` command.

The following example is an AWS CLI to get the route calculator details for {{ExampleCalculator}}.

```
aws location describe-route-calculator \
        --calculator-name "{{ExampleCalculator}}"
```

------

## Delete a route calculator
<a name="delete-route-calculator"></a>

You can delete a route calculator from your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

------
#### [ Console ]

**To delete a route calculator using the Amazon Location console**

**Warning**
This operation deletes the resource permanently.

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Route calculators** from the left navigation pane.

1. Under **My route calculators**, select the target route calculator.

1. Choose **Delete route calculator**.

------
#### [ API ]

Use the `[DeleteRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteRouteCalculator.html)` operation from the Amazon Location Routes APIs.

The following example is an API request to delete the geofence collection {{ExampleCalculator}}.

```
DELETE /routes/v0/calculators/{{ExampleCalculator}}
```

The following is an example response for `[DeleteRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteRouteCalculator.html)`:

```
HTTP/1.1 200
```

------
#### [ CLI ]

Use the `delete-route-calculator` command.

The following example is an AWS CLI command to delete the geofence collection {{ExampleCalculator}}.

```
aws location delete-route-calculator \
        --calculator-name "{{ExampleCalculator}}"
```

------
