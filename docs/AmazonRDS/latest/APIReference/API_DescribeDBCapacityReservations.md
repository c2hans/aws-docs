---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBCapacityReservations.html
---

# DescribeDBCapacityReservations
<a name="API_DescribeDBCapacityReservations"></a>

Describes one or more DB capacity reservations. A DB capacity reservation reserves capacity for Amazon RDS DB instances in one or more Availability Zones.

If you don't specify a `DBCapacityReservationIdentifier`, this operation returns information about all DB capacity reservations for your AWS account.

This operation supports pagination.

## Request Parameters
<a name="API_DescribeDBCapacityReservations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBCapacityReservationIdentifier **
The identifier or the name of the DB capacity reservation to describe. You can specify the identifier, which has the prefix `dbcr-`, or the reservation name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z](?:-?[a-z0-9]+){0,15}`
Required: No

 **Filters.Filter.N**
A filter that specifies which DB capacity reservations to describe.
Supported filters:
+  `db-capacity-reservation-name` - Accepts DB capacity reservation names. The response includes only the reservations that these names identify. Use this filter to describe several reservations by name in one request.
+  `state` - Accepts reservation states. The response includes only the reservations in these states.
+  `engine` - Accepts database engine names. The response includes only the reservations that reserve capacity for these engines.
+  `db-instance-class` - Accepts DB instance classes. The response includes only the reservations that reserve capacity for these DB instance classes.
+  `availability-zone` - Accepts Availability Zone names. The response includes only the reservations that cover these Availability Zones.
When you specify more than one value for a filter, the response includes the reservations that match any of those values. When you specify more than one filter, the response includes only the reservations that match every filter.
Amazon RDS rejects the request when a filter name isn't in this list, or when a filter specifies no values.
The `state` filter doesn't accept `expired`. To find an expired reservation, compare `EndDate` against the current date and time.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** Marker **
An optional pagination token provided by a previous `DescribeDBCapacityReservations` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** MaxRecords **
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.
Default: 100
Constraints:
+ Must be a minimum of 20.
+ Can't exceed 100.
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 100.
Required: No

## Response Elements
<a name="API_DescribeDBCapacityReservations_ResponseElements"></a>

The following elements are returned by the service.

 **DBCapacityReservations.member.N**
A list of DB capacity reservations.
Type: Array of [DBCapacityReservation](API_DBCapacityReservation.md) objects

 ** Marker **
A pagination token that you can use in a later `DescribeDBCapacityReservations` request. If this value is returned, more records are available beyond this response.
Type: String

## Errors
<a name="API_DescribeDBCapacityReservations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBCapacityReservationNotFound **
 `DBCapacityReservationIdentifier` doesn't refer to an existing DB capacity reservation.
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBCapacityReservations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBCapacityReservations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBCapacityReservations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBCapacityReservations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBCapacityReservations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBCapacityReservations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBCapacityReservations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBCapacityReservations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBCapacityReservations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBCapacityReservations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBCapacityReservations)
