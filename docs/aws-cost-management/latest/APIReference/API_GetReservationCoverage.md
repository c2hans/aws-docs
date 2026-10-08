---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetReservationCoverage.html
---

# GetReservationCoverage
<a name="API_GetReservationCoverage"></a>

Retrieves the reservation coverage for your account, which you can use to see how much of your Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon Relational Database Service, or Amazon Redshift usage is covered by a reservation. An organization's management account can see the coverage of the associated member accounts. This supports dimensions, cost categories, and nested expressions. For any time period, you can filter data about reservation usage by the following dimensions:
+ AZ
+ CACHE\_ENGINE
+ DATABASE\_ENGINE
+ DEPLOYMENT\_OPTION
+ INSTANCE\_TYPE
+ LINKED\_ACCOUNT
+ OPERATING\_SYSTEM
+ PLATFORM
+ REGION
+ SERVICE
+ TAG
+ TENANCY

To determine valid values for a dimension, use the `GetDimensionValues` operation.

## Request Syntax
<a name="API_GetReservationCoverage_RequestSyntax"></a>

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
      "ProductAttributes": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      },
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
   "Metrics": [ "{{string}}" ],
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
<a name="API_GetReservationCoverage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_GetReservationCoverage_RequestSyntax) **   <a name="awscostmanagement-GetReservationCoverage-request-Filter"></a>
Filters utilization data by dimensions. You can filter by the following dimensions:
+ AZ
+ CACHE\_ENGINE
+ DATABASE\_ENGINE
+ DEPLOYMENT\_OPTION
+ INSTANCE\_TYPE
+ LINKED\_ACCOUNT
+ OPERATING\_SYSTEM
+ PLATFORM
+ REGION
+ SERVICE
+ TAG
+ TENANCY
 `GetReservationCoverage` uses the same [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html) object as the other operations, but only `AND` is supported among each dimension. You can nest only one level deep. If there are multiple values for a dimension, they are OR'd together.
If you don't provide a `SERVICE` filter, Cost Explorer defaults to EC2.
Cost category is also supported.
Type: [Expression](API_Expression.md) object
Required: No

 ** [Granularity](#API_GetReservationCoverage_RequestSyntax) **   <a name="awscostmanagement-GetReservationCoverage-request-Granularity"></a>
The granularity of the AWS cost data for the reservation. Valid values are `MONTHLY` and `DAILY`.
If `GroupBy` is set, `Granularity` can't be set. If `Granularity` isn't set, the response object doesn't include `Granularity`, either `MONTHLY` or `DAILY`.
The `GetReservationCoverage` operation supports only `DAILY` and `MONTHLY` granularities.
Type: String
Valid Values: `DAILY | MONTHLY | HOURLY`
Required: No

 ** [GroupBy](#API_GetReservationCoverage_RequestSyntax) **   <a name="awscostmanagement-GetReservationCoverage-request-GroupBy"></a>
You can group the data by the following attributes:
+ AZ
+ CACHE\_ENGINE
+ DATABASE\_ENGINE
+ DEPLOYMENT\_OPTION
+ INSTANCE\_TYPE
+ INVOICING\_ENTITY
+ LINKED\_ACCOUNT
+ OPERATING\_SYSTEM
+ PLATFORM
+ REGION
+ TENANCY
Type: Array of [GroupDefinition](API_GroupDefinition.md) objects
Required: No

 ** [MaxResults](#API_GetReservationCoverage_RequestSyntax) **   <a name="awscostmanagement-GetReservationCoverage-request-MaxResults"></a>
The maximum number of objects that you returned for this request. If more objects are available, in the response, AWS provides a NextPageToken value that you can use in a subsequent call to get the next batch of objects.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Metrics](#API_GetReservationCoverage_RequestSyntax) **   <a name="awscostmanagement-GetReservationCoverage-request-Metrics"></a>
The measurement that you want your reservation coverage reported in.
Valid values are `Hour`, `Unit`, and `Cost`. You can use multiple values in a request.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [NextPageToken](#API_GetReservationCoverage_RequestSyntax) **   <a name="awscostmanagement-GetReservationCoverage-request-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [SortBy](#API_GetReservationCoverage_RequestSyntax) **   <a name="awscostmanagement-GetReservationCoverage-request-SortBy"></a>
The value by which you want to sort the data.
The following values are supported for `Key`:
+  `OnDemandCost`
+  `CoverageHoursPercentage`
+  `OnDemandHours`
+  `ReservedHours`
+  `TotalRunningHours`
+  `CoverageNormalizedUnitsPercentage`
+  `OnDemandNormalizedUnits`
+  `ReservedNormalizedUnits`
+  `TotalRunningNormalizedUnits`
+  `Time`
Supported values for `SortOrder` are `ASCENDING` or `DESCENDING`.
Type: [SortDefinition](API_SortDefinition.md) object
Required: No

 ** [TimePeriod](#API_GetReservationCoverage_RequestSyntax) **   <a name="awscostmanagement-GetReservationCoverage-request-TimePeriod"></a>
The start and end dates of the period that you want to retrieve data about reservation coverage for. You can retrieve data for a maximum of 13 months: the last 12 months and the current month. The start date is inclusive, but the end date is exclusive. For example, if `start` is `2017-01-01` and `end` is `2017-05-01`, then the cost and usage data is retrieved from `2017-01-01` up to and including `2017-04-30` but not including `2017-05-01`.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

## Response Syntax
<a name="API_GetReservationCoverage_ResponseSyntax"></a>

```
{
   "CoveragesByTime": [
      {
         "Groups": [
            {
               "Attributes": {
                  "string" : "string"
               },
               "Coverage": {
                  "CoverageCost": {
                     "OnDemandCost": "string"
                  },
                  "CoverageHours": {
                     "CoverageHoursPercentage": "string",
                     "OnDemandHours": "string",
                     "ReservedHours": "string",
                     "TotalRunningHours": "string"
                  },
                  "CoverageNormalizedUnits": {
                     "CoverageNormalizedUnitsPercentage": "string",
                     "OnDemandNormalizedUnits": "string",
                     "ReservedNormalizedUnits": "string",
                     "TotalRunningNormalizedUnits": "string"
                  }
               }
            }
         ],
         "TimePeriod": {
            "End": "string",
            "Start": "string"
         },
         "Total": {
            "CoverageCost": {
               "OnDemandCost": "string"
            },
            "CoverageHours": {
               "CoverageHoursPercentage": "string",
               "OnDemandHours": "string",
               "ReservedHours": "string",
               "TotalRunningHours": "string"
            },
            "CoverageNormalizedUnits": {
               "CoverageNormalizedUnitsPercentage": "string",
               "OnDemandNormalizedUnits": "string",
               "ReservedNormalizedUnits": "string",
               "TotalRunningNormalizedUnits": "string"
            }
         }
      }
   ],
   "NextPageToken": "string",
   "Total": {
      "CoverageCost": {
         "OnDemandCost": "string"
      },
      "CoverageHours": {
         "CoverageHoursPercentage": "string",
         "OnDemandHours": "string",
         "ReservedHours": "string",
         "TotalRunningHours": "string"
      },
      "CoverageNormalizedUnits": {
         "CoverageNormalizedUnitsPercentage": "string",
         "OnDemandNormalizedUnits": "string",
         "ReservedNormalizedUnits": "string",
         "TotalRunningNormalizedUnits": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetReservationCoverage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CoveragesByTime](#API_GetReservationCoverage_ResponseSyntax) **   <a name="awscostmanagement-GetReservationCoverage-response-CoveragesByTime"></a>
The amount of time that your reservations covered.
Type: Array of [CoverageByTime](API_CoverageByTime.md) objects

 ** [NextPageToken](#API_GetReservationCoverage_ResponseSyntax) **   <a name="awscostmanagement-GetReservationCoverage-response-NextPageToken"></a>
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [Total](#API_GetReservationCoverage_ResponseSyntax) **   <a name="awscostmanagement-GetReservationCoverage-response-Total"></a>
The total amount of instance usage that a reservation covered.
Type: [Coverage](API_Coverage.md) object

## Errors
<a name="API_GetReservationCoverage_Errors"></a>

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
<a name="API_GetReservationCoverage_Examples"></a>

### Example
<a name="API_GetReservationCoverage_Example_1"></a>

The following example request for the `GetReservationCoverage` operation retrieves reservation coverage for all `t2.nano` instance types from 2017-07-01 to 2017-10-01.

#### Sample Request
<a name="API_GetReservationCoverage_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ce.us-east-1.amazonaws.com
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSInsightsIndexService.GetReservationCoverage
{
  "TimePeriod": {
    "Start":"2017-07-01",
    "End": "2017-10-01"
  },
  "Filter": {
    "And": [
      {"Dimensions": {
        "Key": "INSTANCE_TYPE",
        "Values": [
          "t2.nano"
        ]
      },
      {"Dimensions": {
        "Key": "REGION",
        "Values": [
          "us-east-1"
        ]
      }}
    ]
  },
  "GroupBy":[
    {
      "Type":"Dimension",
      "Key":"REGION"
    }
  ]
}
```

#### Sample Response
<a name="API_GetReservationCoverage_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "CoveragesByTime": [{
    "Groups": [{
      "Attributes": {
        "region": "us-east-1"
      },
      "Coverage": {
        "CoverageHours": {
          "CoverageHoursPercentage": "40%",
          "OnDemandHours": "40",
          "ReservedHours": "40",
          "TotalRunningHours": "80"
        }
        "CoverageNormalizedUnits": {
          "CoverageNormalizedUnitsPercentage": "10",
          "OnDemandNormalizedUnits": "10",
          "ReservedNormalizedUnits": "10",
          "TotalRunningNormalizedUnits": "20"
        }
      }
    }],
    "TimePeriod": {
      "End": "2017-07-01",
      "Start": "2017-10-01"
    },
    "Total": {
      "CoverageHours": {
        "CoverageHoursPercentage": "40%",
        "OnDemandHours": "40",
        "ReservedHours": "40",
        "TotalRunningHours": "80"
      }
      "CoverageNormalizedUnits": {
        "CoverageNormalizedUnitsPercentage": "10",
        "OnDemandNormalizedUnits": "10",
        "ReservedNormalizedUnits": "10",
        "TotalRunningNormalizedUnits": "20"
      }
    }
  }],
  "Total": {
    "CoverageHours": {
      "CoverageHoursPercentage": "40%",
      "OnDemandHours": "40",
      "ReservedHours": "40",
      "TotalRunningHours": "80"
    }
  }
}
}
```

## See Also
<a name="API_GetReservationCoverage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetReservationCoverage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetReservationCoverage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetReservationCoverage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetReservationCoverage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetReservationCoverage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetReservationCoverage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetReservationCoverage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetReservationCoverage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetReservationCoverage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetReservationCoverage)
