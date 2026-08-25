---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html
---

# Amazon Location Service quotas
<a name="location-quotas"></a>

**Note**
We released a new version of the Places, Maps, and Routes APIs, see the updated [Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html) for revised information and new topics, such as [Geofences](https://docs.aws.amazon.com/location/latest/developerguide/geofences.html) and [Trackers](https://docs.aws.amazon.com/location/latest/developerguide/trackers.html).

This topic provides a summary of rate limits and quotas for Amazon Location Service.

Service Quotas console allows you to [request quota increases or decrease quota](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) for adjustable quotas. Service quotas are the maximum number of API calls or resources you can have per AWS account and AWS Region. When requesting a quota increase, select the Region you require the quota increase in since most quotas are Region-specific. Amazon Location Service denies additional requests that exceed the service quota.

Rate limits (quotas that start with *Rate of...*) are the maximum number of requests per second, with a burst rate of 80 percent of the limit within any part of the second, defined for each API operation. Operations with rate limits increased for an account through Service Quotas may have a burst rate lower than 80 percent of the increased rate limit. Amazon Location Service throttles requests that exceed the operation's rate limit.

| Name | Default | Adjustable | Description |
| --- | --- | --- | --- |
| API Key resources per account | Each supported Region: 500 | No | The maximum number of API key resources (active or expired) that you can have per account. |
| Geofence Collection resources per account | Each supported Region: 1,500 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-93FB3073)  | The maximum number of Geofence Collection resources that you can create per account. |
| Geofences per Geofence Collection | Each supported Region: 50,000 | No | The maximum number of Geofences that you can create per Geofence Collection. |
| Map resources per account | Each supported Region: 40 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-A94FDED2)  | The maximum number of Map resources that you can create per account. |
| Place Index resources per account | Each supported Region: 40 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-AF0CC293)  | The maximum number of Place Index resources that you can create per account. |
| Rate of AssociateTrackerConsumer API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-664067C5)  | The maximum number of AssociateTrackerConsumer requests that you can make per second. Additional requests are throttled. |
| Rate of BatchDeleteDevicePositionHistory API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-CA16DE37)  | The maximum number of BatchDeleteDevicePositionHistory requests that you can make per second. Additional requests are throttled. |
| Rate of BatchDeleteGeofence API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-93F5D44A)  | The maximum number of BatchDeleteGeofence requests that you can make per second. Additional requests are throttled. |
| Rate of BatchEvaluateGeofences API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-9A0A3162)  | The maximum number of BatchEvaluateGeofences requests that you can make per second. Additional requests are throttled. |
| Rate of BatchGetDevicePosition API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-1D4EB556)  | The maximum number of BatchGetDevicePosition requests that you can make per second. Additional requests are throttled. |
| Rate of BatchPutGeofence API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-4D8FB6E2)  | The maximum number of BatchPutGeofence requests that you can make per second. Additional requests are throttled. |
| Rate of BatchUpdateDevicePosition API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-16C77FC0)  | The maximum number of BatchUpdateDevicePosition requests that you can make per second. Additional requests are throttled. |
| Rate of CalculateRoute API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-44B9F1A6)  | The maximum number of CalculateRoute requests that you can make per second. Additional requests are throttled. |
| Rate of CalculateRouteMatrix API requests | Each supported Region: 5 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-0E174A76)  | The maximum number of CalculateRouteMatrix requests that you can make per second. Additional requests are throttled. |
| Rate of CancelJob API requests | Each supported Region: 5 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-1652DE7E)  | The maximum number of CancelJob requests that you can make per second. Additional requests are throttled. |
| Rate of CreateGeofenceCollection API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-DFE2C362)  | The maximum number of CreateGeofenceCollection requests that you can make per second. Additional requests are throttled. |
| Rate of CreateKey API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-0C20A2F2)  | The maximum number of CreateKey requests that you can make per second. Additional requests are throttled. |
| Rate of CreateMap API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-8A769EC2)  | The maximum number of CreateMap requests that you can make per second. Additional requests are throttled. |
| Rate of CreatePlaceIndex API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-0A4EAAD0)  | The maximum number of CreatePlaceIndex requests that you can make per second. Additional requests are throttled. |
| Rate of CreateRouteCalculator API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-AF53BB1C)  | The maximum number of CreateRouteCalculator requests that you can make per second. Additional requests are throttled. |
| Rate of CreateTracker API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-0316544D)  | The maximum number of CreateTracker requests that you can make per second. Additional requests are throttled. |
| Rate of DeleteGeofenceCollection API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-779B9CA5)  | The maximum number of DeleteGeofenceCollection requests that you can make per second. Additional requests are throttled. |
| Rate of DeleteKey API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-FF8C0CDC)  | The maximum number of DeleteKey requests that you can make per second. Additional requests are throttled. |
| Rate of DeleteMap API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-66B4C7B5)  | The maximum number of DeleteMap requests that you can make per second. Additional requests are throttled. |
| Rate of DeletePlaceIndex API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-D012773A)  | The maximum number of DeletePlaceIndex requests that you can make per second. Additional requests are throttled. |
| Rate of DeleteRouteCalculator API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-EF11EFBE)  | The maximum number of DeleteRouteCalculator requests that you can make per second. Additional requests are throttled. |
| Rate of DeleteTracker API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-24CBFF24)  | The maximum number of DeleteTracker requests that you can make per second. Additional requests are throttled. |
| Rate of DescribeGeofenceCollection API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-68C0FF09)  | The maximum number of DescribeGeofenceCollection requests that you can make per second. Additional requests are throttled. |
| Rate of DescribeKey API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-4B4C2391)  | The maximum number of DescribeKey requests that you can make per second. Additional requests are throttled. |
| Rate of DescribeMap API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-3B6F7C26)  | The maximum number of DescribeMap requests that you can make per second. Additional requests are throttled. |
| Rate of DescribePlaceIndex API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-772C0B77)  | The maximum number of DescribePlaceIndex requests that you can make per second. Additional requests are throttled. |
| Rate of DescribeRouteCalculator API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-EA3098B7)  | The maximum number of DescribeRouteCalculator requests that you can make per second. Additional requests are throttled. |
| Rate of DescribeTracker API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-4BA89359)  | The maximum number of DescribeTracker requests that you can make per second. Additional requests are throttled. |
| Rate of DisassociateTrackerConsumer API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-32299313)  | The maximum number of DisassociateTrackerConsumer requests that you can make per second. Additional requests are throttled. |
| Rate of ForecastGeofenceEvents API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-46173623)  | The maximum number of ForecastGeofenceEvents requests that you can make per second. Additional requests are throttled. |
| Rate of GetDevicePosition API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-55FCDA52)  | The maximum number of GetDevicePosition requests that you can make per second. Additional requests are throttled. |
| Rate of GetDevicePositionHistory API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-9A60EA62)  | The maximum number of GetDevicePositionHistory requests that you can make per second. Additional requests are throttled. |
| Rate of GetGeofence API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-E2B35742)  | The maximum number of GetGeofence requests that you can make per second. Additional requests are throttled. |
| Rate of GetJob API requests | Each supported Region: 5 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-EE3EE95B)  | The maximum number of GetJob requests that you can make per second. Additional requests are throttled. |
| Rate of GetMapGlyphs API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-25528367)  | The maximum number of GetMapGlyphs requests that you can make per second. Additional requests are throttled. |
| Rate of GetMapSprites API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-C2D15753)  | The maximum number of GetMapSprites requests that you can make per second. Additional requests are throttled. |
| Rate of GetMapStyleDescriptor API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-05EFD12D)  | The maximum number of GetMapStyleDescriptor requests that you can make per second. Additional requests are throttled. |
| Rate of GetMapTile API requests | Each supported Region: 500 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-7FB5719A)  | The maximum number of GetMapTile requests that you can make per second. Additional requests are throttled. |
| Rate of GetPlace API requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-CF1B7B95)  | The maximum number of GetPlace requests that you can make per second. Additional requests are throttled. |
| Rate of ListDevicePositions API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-B26E5E95)  | The maximum number of ListDevicePositions requests that you can make per second. Additional requests are throttled. |
| Rate of ListGeofenceCollections API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-42524A80)  | The maximum number of ListGeofenceCollections requests that you can make per second. Additional requests are throttled. |
| Rate of ListGeofences API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-2A3A5399)  | The maximum number of ListGeofences requests that you can make per second. Additional requests are throttled. |
| Rate of ListJobs API requests | Each supported Region: 5 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-F9BDB0EC)  | The maximum number of ListJobs requests that you can make per second. Additional requests are throttled. |
| Rate of ListKeys API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-BE8C4A7E)  | The maximum number of ListKeys requests that you can make per second. Additional requests are throttled. |
| Rate of ListMaps API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-004FBC04)  | The maximum number of ListMaps requests that you can make per second. Additional requests are throttled. |
| Rate of ListPlaceIndexes API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-E3E8B4BC)  | The maximum number of ListPlaceIndexes requests that you can make per second. Additional requests are throttled. |
| Rate of ListRouteCalculators API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-D3A51B68)  | The maximum number of ListRouteCalculators requests that you can make per second. Additional requests are throttled. |
| Rate of ListTagsForResource API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-E976E608)  | The maximum number of ListTagsForResource requests that you can make per second. Additional requests are throttled. |
| Rate of ListTrackerConsumers API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-3B5E6DAC)  | The maximum number of ListTrackerConsumers requests that you can make per second. Additional requests are throttled. |
| Rate of ListTrackers API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-F0E58BD7)  | The maximum number of ListTrackers requests that you can make per second. Additional requests are throttled. |
| Rate of PutGeofence API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-8C4D918C)  | The maximum number of PutGeofence requests that you can make per second. Additional requests are throttled. |
| Rate of SearchPlaceIndexForPosition API requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-201B3D58)  | The maximum number of SearchPlaceIndexForPosition requests that you can make per second. Additional requests are throttled. |
| Rate of SearchPlaceIndexForSuggestions API requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-EC3CCC13)  | The maximum number of SearchPlaceIndexForSuggestions requests that you can make per second. Additional requests are throttled. |
| Rate of SearchPlaceIndexForText API requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-20F1367A)  | The maximum number of SearchPlaceIndexForText requests that you can make per second. Additional requests are throttled. |
| Rate of StartJob API requests | Each supported Region: 5 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-8E246EB1)  | The maximum number of StartJob requests that you can make per second. Additional requests are throttled. |
| Rate of TagResource API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-2CA6C84D)  | The maximum number of TagResource requests that you can make per second. Additional requests are throttled. |
| Rate of UntagResource API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-C236DAD6)  | The maximum number of UntagResource requests that you can make per second. Additional requests are throttled. |
| Rate of UpdateGeofenceCollection API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-4D54A4EF)  | The maximum number of UpdateGeofenceCollection requests that you can make per second. Additional requests are throttled. |
| Rate of UpdateKey API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-E31E6201)  | The maximum number of UpdateKey requests that you can make per second. Additional requests are throttled. |
| Rate of UpdateMap API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-123EEE95)  | The maximum number of UpdateMap requests that you can make per second. Additional requests are throttled. |
| Rate of UpdatePlaceIndex API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-AE2D8C2E)  | The maximum number of UpdatePlaceIndex requests that you can make per second. Additional requests are throttled. |
| Rate of UpdateRouteCalculator API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-85DB3370)  | The maximum number of UpdateRouteCalculator requests that you can make per second. Additional requests are throttled. |
| Rate of UpdateTracker API requests | Each supported Region: 10 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-5C766737)  | The maximum number of UpdateTracker requests that you can make per second. Additional requests are throttled. |
| Rate of VerifyDevicePosition API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-5FC982A3)  | The maximum number of VerifyDevicePosition requests that you can make per second. Additional requests are throttled. |
| Rate of geo-maps:GetStaticMap API requests | Each supported Region: 50 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-8524BC5F)  | The maximum number of geo-maps:GetStaticMap requests that you can make per second. Additional requests are throttled. |
| Rate of geo-maps:GetTile API requests | Each supported Region: 2,000 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-CB597B2B)  | The maximum number of geo-maps:GetTile requests that you can make per second. Additional requests are throttled. |
| Rate of geo-places:Autocomplete API requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-EF9582AD)  | The maximum number of geo-places:Autocomplete requests that you can make per second. Additional requests are throttled. |
| Rate of geo-places:Geocode API requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-80BBD6B4)  | The maximum number of geo-places:Geocode requests that you can make per second. Additional requests are throttled. |
| Rate of geo-places:GetPlace API requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-6FC30467)  | The maximum number of geo-places:GetPlace requests that you can make per second. Additional requests are throttled. |
| Rate of geo-places:ReverseGeocode API requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-E2610803)  | The maximum number of geo-places:ReverseGeocode requests that you can make per second. Additional requests are throttled. |
| Rate of geo-places:SearchNearby API requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-D877D921)  | The maximum number of geo-places:SearchNearby requests that you can make per second. Additional requests are throttled. |
| Rate of geo-places:SearchText API requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-7746796E)  | The maximum number of geo-places:SearchText requests that you can make per second. Additional requests are throttled. |
| Rate of geo-places:Suggest API requests | Each supported Region: 100 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-A8DEDDAD)  | The maximum number of geo-places:Suggest requests that you can make per second. Additional requests are throttled. |
| Rate of geo-routes:CalculateIsolines API requests | Each supported Region: 20 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-9181BDFA)  | The maximum number of geo-routes:CalculateIsolines requests that you can make per second. Additional requests are throttled. |
| Rate of geo-routes:CalculateRouteMatrix API requests | Each supported Region: 5 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-8EACF4A4)  | The maximum number of geo-routes:CalculateRouteMatrix requests that you can make per second. Additional requests are throttled. |
| Rate of geo-routes:CalculateRoutes API requests | Each supported Region: 20 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-8652D4FC)  | The maximum number of geo-routes:CalculateRoutes requests that you can make per second. Additional requests are throttled. |
| Rate of geo-routes:OptimizeWaypoints API requests | Each supported Region: 5 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-E2D2B83E)  | The maximum number of geo-routes:OptimizeWaypoints requests that you can make per second. Additional requests are throttled. |
| Rate of geo-routes:SnapToRoads API requests | Each supported Region: 20 per second |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-18D30F94)  | The maximum number of geo-routes:SnapToRoads requests that you can make per second. Additional requests are throttled. |
| Route Calculator resources per account | Each supported Region: 40 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-D4E15F64)  | The maximum number of Route Calculator resources that you can create per account. |
| Tracker consumers per tracker | Each supported Region: 5 | No | The maximum number of Geofence Collection that Tracker resource can be associated with. |
| Tracker resources per account | Each supported Region: 500 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/geo/quotas/L-8CDBA5E9)  | The maximum number of Tracker resources that you can create per account. |

**Note**
You can monitor your usage against your quotas with Cloudwatch. For more information, see [Use CloudWatch to monitor usage against quotas](monitoring-using-cloudwatch.md#alarms-on-quotas).

## Managing your Amazon Location service quotas
<a name="service-quotas-manage"></a>

Amazon Location Service is integrated with Service Quotas, an AWS service that enables you to view and manage your quotas from a central location. For more information, see [What Is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) in the *Service Quotas User Guide*.

Service Quotas makes it easy to look up the value of your Amazon Location service quotas.

------
#### [ AWS Management Console ]

**To view Amazon Location service quotas using the console**

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **AWS services**.

1. From the **AWS services** list, search for and select **Amazon Location**.

   In the **Service quotas** list, you can see the service quota name, applied value (if it is available), AWS default quota, and whether the quota value is adjustable.

1. To view additional information about a service quota, such as the description, choose the quota name.

1. (Optional) To request a quota increase, select the quota that you want to increase, select **Request quota increase**, enter or select the required information, and select **Request**.

To work more with service quotas using the console see the [Service Quotas User Guide](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html). To request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

------
#### [ AWS CLI ]

**To view Amazon Location service quotas using the AWS CLI**
Run the following command to view the default Amazon Location quotas.

```
aws service-quotas list-aws-default-service-quotas \
    --query 'Quotas[*].{Adjustable:Adjustable,Name:QuotaName,Value:Value,Code:QuotaCode}' \
    --service-code geo \
    --output table
```

To work more with service quotas using the AWS CLI, see the [Service Quotas AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/index.html#cli-aws-service-quotas). To request a quota increase, see the [`request-service-quota-increase`](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/request-service-quota-increase.html) command in the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/index.html#cli-aws-service-quotas).

------
