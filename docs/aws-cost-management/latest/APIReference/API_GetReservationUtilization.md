---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetReservationUtilization.html
---

# GetReservationUtilization
<a name="API_GetReservationUtilization"></a>

Retrieves the reservation utilization for your account. Management account in an organization have access to member accounts. You can filter data by dimensions in a time period. You can use `GetDimensionValues` to determine the possible dimension values. Currently, you can group only by `SUBSCRIPTION_ID`.

## Request Syntax
<a name="API_GetReservationUtilization_RequestSyntax"></a>

```
{
   "Filter": {
      "And": [
         "Expression"
      ],
      "CostCategories": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      },
      "Dimensions": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      },
      "Not": "Expression",
      "Or": [
         "Expression"
      ],
      "Tags": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      }
   },
   "Granularity": "{{string}}",
   "GroupBy": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextPageToken": "{{string}}",
   "SortBy": {
      "Key": "{{string}}",
      "SortOrder": "{{string}}"
   },
   "TimePeriod": {
      "End": "{{string}}",
      "Start": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetReservationUtilization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_GetReservationUtilization_RequestSyntax) **   <a name="awscostmanagement-GetReservationUtilization-request-Filter"></a>
Filters utilization data by dimensions. You can filter by the following dimensions:
+ AZ
+ CACHE\_ENGINE
+ DEPLOYMENT\_OPTION
+ INSTANCE\_TYPE
+ LINKED\_ACCOUNT
+ OPERATING\_SYSTEM
+ PLATFORM
+ REGION
+ SERVICE
**Note**
If not specified, the `SERVICE` filter defaults to Amazon Elastic Compute Cloud - Compute. Supported values for `SERVICE` are Amazon Elastic Compute Cloud - Compute, Amazon Relational Database Service, Amazon ElastiCache, Amazon Redshift, and Amazon Elasticsearch Service. The value for the `SERVICE` filter should not exceed "1".
+ SCOPE
+ TENANCY
 `GetReservationUtilization` uses the same [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html) object as the other operations, but only `AND` is supported among each dimension, and nesting is supported up to only one level deep. If there are multiple values for a dimension, they are OR'd together.
Type: [Expression](API_Expression.md) object
Required: No

 ** [Granularity](#API_GetReservationUtilization_RequestSyntax) **   <a name="awscostmanagement-GetReservationUtilization-request-Granularity"></a>
If `GroupBy` is set, `Granularity` can't be set. If `Granularity` isn't set, the response object doesn't include `Granularity`, either `MONTHLY` or `DAILY`. If both `GroupBy` and `Granularity` aren't set, `GetReservationUtilization` defaults to `DAILY`.
The `GetReservationUtilization` operation supports only `DAILY` and `MONTHLY` granularities.
Type: String
Valid Values: `DAILY | MONTHLY | HOURLY`
Required: No

 ** [GroupBy](#API_GetReservationUtilization_RequestSyntax) **   <a name="awscostmanagement-GetReservationUtilization-request-GroupBy"></a>
Groups only by `SUBSCRIPTION_ID`. Metadata is included.
Type: Array of [GroupDefinition](API_GroupDefinition.md) objects
Required: No

 ** [MaxResults](#API_GetReservationUtilization_RequestSyntax) **   <a name="awscostmanagement-GetReservationUtilization-request-MaxResults"></a>
The maximum number of objects that you returned for this request. If more objects are available, in the response, AWS provides a NextPageToken value that you can use in a subsequent call to get the next batch of objects.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextPageToken](#API_GetReservationUtilization_RequestSyntax) **   <a name="awscostmanagement-GetReservationUtilization-request-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [SortBy](#API_GetReservationUtilization_RequestSyntax) **   <a name="awscostmanagement-GetReservationUtilization-request-SortBy"></a>
The value that you want to sort the data by.
The following values are supported for `Key`:
+  `UtilizationPercentage`
+  `UtilizationPercentageInUnits`
+  `PurchasedHours`
+  `PurchasedUnits`
+  `TotalActualHours`
+  `TotalActualUnits`
+  `UnusedHours`
+  `UnusedUnits`
+  `OnDemandCostOfRIHoursUsed`
+  `NetRISavings`
+  `TotalPotentialRISavings`
+  `AmortizedUpfrontFee`
+  `AmortizedRecurringFee`
+  `TotalAmortizedFee`
+  `RICostForUnusedHours`
+  `RealizedSavings`
+  `UnrealizedSavings`
The supported values for `SortOrder` are `ASCENDING` and `DESCENDING`.
Type: [SortDefinition](API_SortDefinition.md) object
Required: No

 ** [TimePeriod](#API_GetReservationUtilization_RequestSyntax) **   <a name="awscostmanagement-GetReservationUtilization-request-TimePeriod"></a>
Sets the start and end dates for retrieving Reserved Instance (RI) utilization. The start date is inclusive, but the end date is exclusive. For example, if `start` is `2017-01-01` and `end` is `2017-05-01`, then the cost and usage data is retrieved from `2017-01-01` up to and including `2017-04-30` but not including `2017-05-01`.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

## Response Syntax
<a name="API_GetReservationUtilization_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "Total": {
      "AmortizedRecurringFee": "string",
      "AmortizedUpfrontFee": "string",
      "NetRISavings": "string",
      "OnDemandCostOfRIHoursUsed": "string",
      "PurchasedHours": "string",
      "PurchasedUnits": "string",
      "RealizedSavings": "string",
      "RICostForUnusedHours": "string",
      "TotalActualHours": "string",
      "TotalActualUnits": "string",
      "TotalAmortizedFee": "string",
      "TotalPotentialRISavings": "string",
      "UnrealizedSavings": "string",
      "UnusedHours": "string",
      "UnusedUnits": "string",
      "UtilizationPercentage": "string",
      "UtilizationPercentageInUnits": "string"
   },
   "UtilizationsByTime": [
      {
         "Groups": [
            {
               "Attributes": {
                  "string" : "string"
               },
               "Key": "string",
               "Utilization": {
                  "AmortizedRecurringFee": "string",
                  "AmortizedUpfrontFee": "string",
                  "NetRISavings": "string",
                  "OnDemandCostOfRIHoursUsed": "string",
                  "PurchasedHours": "string",
                  "PurchasedUnits": "string",
                  "RealizedSavings": "string",
                  "RICostForUnusedHours": "string",
                  "TotalActualHours": "string",
                  "TotalActualUnits": "string",
                  "TotalAmortizedFee": "string",
                  "TotalPotentialRISavings": "string",
                  "UnrealizedSavings": "string",
                  "UnusedHours": "string",
                  "UnusedUnits": "string",
                  "UtilizationPercentage": "string",
                  "UtilizationPercentageInUnits": "string"
               },
               "Value": "string"
            }
         ],
         "TimePeriod": {
            "End": "string",
            "Start": "string"
         },
         "Total": {
            "AmortizedRecurringFee": "string",
            "AmortizedUpfrontFee": "string",
            "NetRISavings": "string",
            "OnDemandCostOfRIHoursUsed": "string",
            "PurchasedHours": "string",
            "PurchasedUnits": "string",
            "RealizedSavings": "string",
            "RICostForUnusedHours": "string",
            "TotalActualHours": "string",
            "TotalActualUnits": "string",
            "TotalAmortizedFee": "string",
            "TotalPotentialRISavings": "string",
            "UnrealizedSavings": "string",
            "UnusedHours": "string",
            "UnusedUnits": "string",
            "UtilizationPercentage": "string",
            "UtilizationPercentageInUnits": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetReservationUtilization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_GetReservationUtilization_ResponseSyntax) **   <a name="awscostmanagement-GetReservationUtilization-response-NextPageToken"></a>
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [Total](#API_GetReservationUtilization_ResponseSyntax) **   <a name="awscostmanagement-GetReservationUtilization-response-Total"></a>
The total amount of time that you used your Reserved Instances (RIs).
Type: [ReservationAggregates](API_ReservationAggregates.md) object

 ** [UtilizationsByTime](#API_GetReservationUtilization_ResponseSyntax) **   <a name="awscostmanagement-GetReservationUtilization-response-UtilizationsByTime"></a>
The amount of time that you used your Reserved Instances (RIs).
Type: Array of [UtilizationByTime](API_UtilizationByTime.md) objects

## Errors
<a name="API_GetReservationUtilization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## Examples
<a name="API_GetReservationUtilization_Examples"></a>

### Example
<a name="API_GetReservationUtilization_Example_1"></a>

The following is a sample request and response of the `GetReservationUtilization` operation that enables you to retrieve your RI utilization for all `t2.nano` instance types from 2017-01-01 to 2017-05-01.

#### Sample Request
<a name="API_GetReservationUtilization_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ce.us-east-1.amazonaws.com
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSInsightsIndexService.GetReservationUtilization
{
  "TimePeriod": {
    "Start":"2017-07-01",
    "End": "2017-10-01"
  },
  "Filter": {
    "Dimensions": {
      "Key": "INSTANCE_TYPE",
      "Values": [
        "t2.nano"
      ]
    }
  },
  "GroupBy":[
    {
      "Type":"Dimension",
      "Key":"SUBSCRIPTION_ID"
    }
  ]
}
```

#### Sample Response
<a name="API_GetReservationUtilization_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "UtilizationsByTime": [{
    "Groups": [{
      "Attributes": {
        "AccountId": "0123456789",
        "AccountName": null,
        "AvailabilityZone": "",
        "CancellationDateTime": "2019-09-28T15:22:31.000Z",
        "EndDateTime": "2019-09-28T15:22:31.000Z",
        "InstanceType": "t2.nano",
        "LeaseId": null,
        "NumberOfInstances": "1",
        "OfferingType": "convertible",
        "Platform": "Linux/UNIX",
        "Region": "us-east-1",
        "Scope": "Region",
        "StartDateTime": "2016-09-28T15:22:32.000Z",
        "SubscriptionId": "359809062",
        "SubscriptionStatus": "Active",
        "SubscriptionType": "All Upfront",
        "Tenancy": "Shared"
      },
      "Key": "SUBSCRIPTION_ID",
      "Utilization": {
        "PurchasedHours": 2208,
        "TotalActualHours": 2208,
        "UnusedHours": 0,
        "UtilizationPercentage": 100
      },
      "Value": "359809062"
    },
    {
      "Attributes": {
        "": "0123456789",
        "AccountName": null,
        "AvailabilityZone": "us-east-1d",
        "CancellationDateTime": "2017-09-28T15:22:31.000Z",
        "EndDateTime": "2017-09-28T15:22:31.000Z",
        "InstanceType": "t2.nano",
        "LeaseId": null,
        "NumberOfInstances": "1",
        "OfferingType": "Standard",
        "Platform": "Linux/UNIX",
        "Region": "us-east-1",
        "Scope": "Availability Zone",
        "StartDateTime": "2016-09-28T15:22:32.000Z",
        "SubscriptionId": "359809070",
        "SubscriptionStatus": "Active",
        "SubscriptionType": "All Upfront",
        "Tenancy": "Shared"
      },
      "Key": "SUBSCRIPTION_ID",
      "Utilization": {
        "PurchasedHours": 2151,
        "TotalActualHours": 2151,
        "UnusedHours": 0,
        "UtilizationPercentage": 100
      },
      "Value": "359809070"
    },
    {
      "Attributes": {
        "AccountId": "0123456789",
        "AccountName": null,
        "AvailabilityZone": "us-west-2a",
        "CancellationDateTime": "2017-09-20T04:06:02.000Z",
        "EndDateTime": "2017-09-20T04:06:02.000Z",
        "InstanceType": "t2.nano",
        "LeaseId": null,
        "NumberOfInstances": "1",
        "OfferingType": "Standard",
        "Platform": "Linux/UNIX",
        "Region": "us-west-2",
        "Scope": "Availability Zone",
        "StartDateTime": "2016-09-20T04:06:03.000Z",
        "SubscriptionId": "353571154",
        "SubscriptionStatus": "Active",
        "SubscriptionType": "Partial Upfront",
        "Tenancy": "Shared"
      },
      "Key": "SUBSCRIPTION_ID",
      "Utilization": {
        "PurchasedHours": 1948,
        "TotalActualHours": 0,
        "UnusedHours": 1948,
        "UtilizationPercentage": 0
      },
      "Value": "353571154"
    }
  ],
  "TimePeriod": {
    "End": "2017-10-01",
    "Start": "2017-07-01"
  },
  "Total": {
    "PurchasedHours": 6307,
    "TotalActualHours": 4359,
    "UnusedHours": 1948,
    "UtilizationPercentage": 69.11368320913270968764864436340574
  }
  }]
}
```

## See Also
<a name="API_GetReservationUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetReservationUtilization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetReservationUtilization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetReservationUtilization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetReservationUtilization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetReservationUtilization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetReservationUtilization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetReservationUtilization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetReservationUtilization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetReservationUtilization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetReservationUtilization)
