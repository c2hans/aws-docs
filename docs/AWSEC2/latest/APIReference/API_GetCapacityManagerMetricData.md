---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetCapacityManagerMetricData.html
---

# GetCapacityManagerMetricData
<a name="API_GetCapacityManagerMetricData"></a>

 Retrieves capacity usage metrics for your EC2 resources. Returns time-series data for metrics like unused capacity, utilization rates, and costs across On-Demand, Spot, and Capacity Reservations. Data can be grouped and filtered by various dimensions such as region, account, and instance family.

## Request Parameters
<a name="API_GetCapacityManagerMetricData_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
 Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EndTime**
 The end time for the metric data query, in ISO 8601 format. If the end time is beyond the latest ingested data, it will be automatically adjusted to the latest available data point.
Type: Timestamp
Required: Yes

 **FilterBy.N**
 Conditions to filter the metric data. Each filter specifies a dimension, comparison operator ('equals', 'in'), and values to match against.
Type: Array of [CapacityManagerCondition](API_CapacityManagerCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 **GroupBy.N**
 The dimensions by which to group the metric data. This determines how the data is aggregated and returned.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 0. Maximum length of 300.
Valid Values: `resource-region | availability-zone-id | account-id | account-name | instance-family | instance-type | instance-platform | reservation-arn | reservation-id | reservation-type | reservation-create-timestamp | reservation-start-timestamp | reservation-end-timestamp | reservation-end-date-type | tenancy | reservation-state | reservation-instance-match-criteria | reservation-unused-financial-owner`
Required: No

 **MaxResults**
 The maximum number of data points to return. Valid range is 1 to 100,000. Use with NextToken for pagination of large result sets.
Type: Integer
Required: No

 **MetricName.N**
 The names of the metrics to retrieve. Maximum of 10 metrics per request.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Valid Values: `reservation-total-capacity-hrs-vcpu | reservation-total-capacity-hrs-inst | reservation-max-size-vcpu | reservation-max-size-inst | reservation-min-size-vcpu | reservation-min-size-inst | reservation-unused-total-capacity-hrs-vcpu | reservation-unused-total-capacity-hrs-inst | reservation-unused-total-estimated-cost | reservation-max-unused-size-vcpu | reservation-max-unused-size-inst | reservation-min-unused-size-vcpu | reservation-min-unused-size-inst | reservation-max-utilization | reservation-min-utilization | reservation-avg-utilization-vcpu | reservation-avg-utilization-inst | reservation-total-count | reservation-total-estimated-cost | reservation-avg-future-size-vcpu | reservation-avg-future-size-inst | reservation-min-future-size-vcpu | reservation-min-future-size-inst | reservation-max-future-size-vcpu | reservation-max-future-size-inst | reservation-avg-committed-size-vcpu | reservation-avg-committed-size-inst | reservation-max-committed-size-vcpu | reservation-max-committed-size-inst | reservation-min-committed-size-vcpu | reservation-min-committed-size-inst | reserved-total-usage-hrs-vcpu | reserved-total-usage-hrs-inst | reserved-total-estimated-cost | unreserved-total-usage-hrs-vcpu | unreserved-total-usage-hrs-inst | unreserved-total-estimated-cost | spot-total-usage-hrs-vcpu | spot-total-usage-hrs-inst | spot-total-estimated-cost | spot-avg-run-time-before-interruption-inst | spot-max-run-time-before-interruption-inst | spot-min-run-time-before-interruption-inst`
Required: Yes

 **NextToken**
 The token for the next page of results. Use this value in a subsequent call to retrieve additional data points.
Type: String
Required: No

 **Period**
 The granularity, in seconds, of the returned data points.
Type: Integer
Valid Range: Minimum value of 3600.
Required: Yes

 **StartTime**
 The start time for the metric data query, in ISO 8601 format. The time range (end time - start time) must be a multiple of the specified period.
Type: Timestamp
Required: Yes

## Response Elements
<a name="API_GetCapacityManagerMetricData_ResponseElements"></a>

The following elements are returned by the service.

 **metricDataResultSet**
 The metric data points returned by the query. Each result contains dimension values, timestamp, and metric values with their associated statistics.
Type: Array of [MetricDataResult](API_MetricDataResult.md) objects

 **nextToken**
 The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetCapacityManagerMetricData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetCapacityManagerMetricData_Examples"></a>

### Example
<a name="API_GetCapacityManagerMetricData_Example_1"></a>

This example retrieves hourly unused capacity metrics grouped by instance family for a specific time range.

#### Sample Request
<a name="API_GetCapacityManagerMetricData_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetCapacityManagerMetricData
&MetricName.1=reservation-unused-total-capacity-hrs-vcpu
&StartTime=2024-01-15T00:00:00Z
&EndTime=2024-01-16T00:00:00Z
&Period=3600
&GroupBy.1=instanceFamily
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetCapacityManagerMetricData_Example_1_Response"></a>

```
<GetCapacityManagerMetricDataResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <metricDataResultSet>
        <item>
            <dimension>
                <instanceFamily>m5</instanceFamily>
            </dimension>
            <timestamp>2024-01-15T00:00:00.000Z</timestamp>
            <metricValueSet>
                <item>
                    <metric>reservation-unused-total-capacity-hrs-vcpu</metric>
                    <value>150.0</value>
                </item>
            </metricValueSet>
        </item>
        <item>
            <dimension>
                <instanceFamily>c5</instanceFamily>
            </dimension>
            <timestamp>2024-01-15T00:00:00.000Z</timestamp>
            <metricValueSet>
                <item>
                    <metric>reservation-unused-total-capacity-hrs-vcpu</metric>
                    <value>75.5</value>
                </item>
            </metricValueSet>
        </item>
    </metricDataResultSet>
</GetCapacityManagerMetricDataResponse>
```

### Example 2
<a name="API_GetCapacityManagerMetricData_Example_2"></a>

This example retrieves On-Demand usage metrics grouped by the `environment` tag dimension and filtered to only production resources.

#### Sample Request
<a name="API_GetCapacityManagerMetricData_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetCapacityManagerMetricData
&MetricName.1=unreserved-total-usage-hrs-vcpu
&StartTime=2024-01-15T00:00:00Z
&EndTime=2024-01-16T00:00:00Z
&Period=3600
&GroupBy.1=tag:environment
&FilterBy.1.DimensionCondition.Dimension=tag:environment
&FilterBy.1.DimensionCondition.Comparison=equals
&FilterBy.1.DimensionCondition.Value.1=prod
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetCapacityManagerMetricData_Example_2_Response"></a>

```
<GetCapacityManagerMetricDataResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>a1b2c3d4-e5f6-7890-abcd-1234EXAMPLE</requestId>
    <metricDataResultSet>
        <item>
            <dimension>
                <tagSet>
                    <item>
                        <key>environment</key>
                        <value>prod</value>
                    </item>
                </tagSet>
            </dimension>
            <timestamp>2024-01-15T00:00:00.000Z</timestamp>
            <metricValueSet>
                <item>
                    <metric>unreserved-total-usage-hrs-vcpu</metric>
                    <value>320.0</value>
                </item>
            </metricValueSet>
        </item>
    </metricDataResultSet>
</GetCapacityManagerMetricDataResponse>
```

## See Also
<a name="API_GetCapacityManagerMetricData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetCapacityManagerMetricData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetCapacityManagerMetricData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetCapacityManagerMetricData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetCapacityManagerMetricData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetCapacityManagerMetricData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetCapacityManagerMetricData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetCapacityManagerMetricData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetCapacityManagerMetricData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetCapacityManagerMetricData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetCapacityManagerMetricData)
