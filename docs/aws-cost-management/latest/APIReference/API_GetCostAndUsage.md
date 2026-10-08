---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsage.html
---

# GetCostAndUsage
<a name="API_GetCostAndUsage"></a>

Retrieves cost and usage metrics for your account. You can specify which cost and usage-related metric that you want the request to return. For example, you can specify `BlendedCosts` or `UsageQuantity`. You can also filter and group your data by various dimensions, such as `SERVICE` or `AZ`, in a specific time range. For a complete list of valid dimensions, see the [GetDimensionValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html) operation. Management account in an organization in AWS Organizations have access to all member accounts.

For information about filter limitations, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html) in the *Billing and Cost Management User Guide*.

## Request Syntax
<a name="API_GetCostAndUsage_RequestSyntax"></a>

```
{
   "BillingViewArn": "{{string}}",
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
   "Metrics": [ "{{string}}" ],
   "NextPageToken": "{{string}}",
   "TimePeriod": {
      "End": "{{string}}",
      "Start": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetCostAndUsage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BillingViewArn](#API_GetCostAndUsage_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsage-request-BillingViewArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to AWS Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[-a-zA-Z0-9/:_+=.-@]{1,43}$`
Required: No

 ** [Filter](#API_GetCostAndUsage_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsage-request-Filter"></a>
Filters AWS costs by different dimensions. For example, you can specify `SERVICE` and `LINKED_ACCOUNT` and get the costs that are associated with that account's usage of that service. You can nest `Expression` objects to define any combination of dimension filters. For more information, see [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html).
Valid values for `MatchOptions` for `Dimensions` are `EQUALS` and `CASE_SENSITIVE`.
Valid values for `MatchOptions` for `CostCategories`, `Tags`, and `ProductAttributes` are `EQUALS`, `ABSENT`, and `CASE_SENSITIVE`. Default values are `EQUALS` and `CASE_SENSITIVE`.
You can filter by product attributes with or without grouping by them. If you filter or group by product attributes, the results include only the costs of supported services, and a `SERVICE` filter is optional. For more information, see [ProductAttributeValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ProductAttributeValues.html).
If you include a `SERVICE` filter, it must apply to the whole request: combine it with other filters by using `And`, and include it in every branch of an `Or`. A `SERVICE` filter inside `Not` doesn't meet this requirement, and the request fails with a `ValidationException`.
Type: [Expression](API_Expression.md) object
Required: No

 ** [Granularity](#API_GetCostAndUsage_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsage-request-Granularity"></a>
Sets the AWS cost granularity to `MONTHLY` or `DAILY`, or `HOURLY`. If `Granularity` isn't set, the response object doesn't include the `Granularity`, either `MONTHLY` or `DAILY`, or `HOURLY`.
Type: String
Valid Values: `DAILY | MONTHLY | HOURLY`
Required: Yes

 ** [GroupBy](#API_GetCostAndUsage_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsage-request-GroupBy"></a>
You can group AWS costs using up to two different groups, either dimensions, tag keys, cost categories, product attributes, or any two group by types.
Valid values for the `DIMENSION` type are `AZ`, `INSTANCE_TYPE`, `LEGAL_ENTITY_NAME`, `INVOICING_ENTITY`, `LINKED_ACCOUNT`, `OPERATION`, `PLATFORM`, `PURCHASE_TYPE`, `SERVICE`, `TENANCY`, `RECORD_TYPE`, and `USAGE_TYPE`.
When you group by the `TAG` type and include a valid tag key, you get all tag values, including empty strings.
To group by the `PRODUCT_ATTRIBUTE` type, set `Key` to a product attribute key, such as `model`. For the keys of each supported service, see [ProductAttributeValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ProductAttributeValues.html). The results include only the costs of supported services, and if you have no such costs, the response contains no groups.
In the response, each group key has the format `key$value`, for example, `model$Claude Sonnet 5`. Costs that have no value for the key are in the group `key$`, for example, `model$`. Remove the `key$` prefix before you use a value in a `ProductAttributes` filter. Keys are case-sensitive: if you group by a key that doesn't exist, such as `Model`, all of your costs of supported services are in the group `Model$`.
Type: Array of [GroupDefinition](API_GroupDefinition.md) objects
Required: No

 ** [Metrics](#API_GetCostAndUsage_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsage-request-Metrics"></a>
Which metrics are returned in the query. For more information about blended and unblended rates, see [Why does the "blended" annotation appear on some line items in my bill?](http://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/).
Valid values are `AmortizedCost`, `BlendedCost`, `NetAmortizedCost`, `NetUnblendedCost`, `NormalizedUsageAmount`, `UnblendedCost`, and `UsageQuantity`.
If you return the `UsageQuantity` metric, the service aggregates all usage numbers without taking into account the units. For example, if you aggregate `usageQuantity` across all of Amazon EC2, the results aren't meaningful because Amazon EC2 compute hours and data transfer are measured in different units (for example, hours and GB). To get more meaningful `UsageQuantity` metrics, filter by `UsageType` or `UsageTypeGroups`.
 `Metrics` is required for `GetCostAndUsage` requests.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** [NextPageToken](#API_GetCostAndUsage_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsage-request-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [TimePeriod](#API_GetCostAndUsage_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsage-request-TimePeriod"></a>
Sets the start date and end date for retrieving AWS costs. The start date is inclusive, but the end date is exclusive. For example, if `start` is `2017-01-01` and `end` is `2017-05-01`, then the cost and usage data is retrieved from `2017-01-01` up to and including `2017-04-30` but not including `2017-05-01`.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

## Response Syntax
<a name="API_GetCostAndUsage_ResponseSyntax"></a>

```
{
   "DimensionValueAttributes": [
      {
         "Attributes": {
            "string" : "string"
         },
         "Value": "string"
      }
   ],
   "GroupDefinitions": [
      {
         "Key": "string",
         "Type": "string"
      }
   ],
   "NextPageToken": "string",
   "ResultsByTime": [
      {
         "Estimated": boolean,
         "Groups": [
            {
               "Keys": [ "string" ],
               "Metrics": {
                  "string" : {
                     "Amount": "string",
                     "Unit": "string"
                  }
               }
            }
         ],
         "TimePeriod": {
            "End": "string",
            "Start": "string"
         },
         "Total": {
            "string" : {
               "Amount": "string",
               "Unit": "string"
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetCostAndUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DimensionValueAttributes](#API_GetCostAndUsage_ResponseSyntax) **   <a name="awscostmanagement-GetCostAndUsage-response-DimensionValueAttributes"></a>
The attributes that apply to a specific dimension value. For example, if the value is a linked account, the attribute is that account name.
Type: Array of [DimensionValuesWithAttributes](API_DimensionValuesWithAttributes.md) objects

 ** [GroupDefinitions](#API_GetCostAndUsage_ResponseSyntax) **   <a name="awscostmanagement-GetCostAndUsage-response-GroupDefinitions"></a>
The groups that are specified by the `Filter` or `GroupBy` parameters in the request.
Type: Array of [GroupDefinition](API_GroupDefinition.md) objects

 ** [NextPageToken](#API_GetCostAndUsage_ResponseSyntax) **   <a name="awscostmanagement-GetCostAndUsage-response-NextPageToken"></a>
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [ResultsByTime](#API_GetCostAndUsage_ResponseSyntax) **   <a name="awscostmanagement-GetCostAndUsage-response-ResultsByTime"></a>
The time period that's covered by the results in the response.
Type: Array of [ResultByTime](API_ResultByTime.md) objects

## Errors
<a name="API_GetCostAndUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BillExpirationException **
The requested report expired. Update the date interval and try again.
HTTP Status Code: 400

 ** BillingViewHealthStatusException **
 The billing view status must be `HEALTHY` to perform this action. Try again when the status is `HEALTHY`.
HTTP Status Code: 400

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** RequestChangedException **
Your request parameters changed between pages. Try again with the old parameters or without a pagination token.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_GetCostAndUsage_Examples"></a>

### Example
<a name="API_GetCostAndUsage_Example_1"></a>

The following is a sample request and response of the `GetCostAndUsage` operation that you can use to retrieve your Amazon S3 costs. For more complex examples, such as multi-level groupings, see [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html).

#### Sample Request
<a name="API_GetCostAndUsage_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ce.us-east-1.amazonaws.com
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSInsightsIndexService.GetCostAndUsage
{
  "TimePeriod": {
    "Start":"2017-09-01",
    "End": "2017-10-01"
  },
  "Granularity": "MONTHLY",
  "Filter": {
    "Dimensions": {
      "Key": "SERVICE",
      "Values": [
        "Amazon Simple Storage Service"
      ]
    }
  },
  "GroupBy":[
    {
      "Type":"DIMENSION",
      "Key":"SERVICE"
    },
    {
      "Type":"TAG",
      "Key":"Environment"
    }
  ],
   "Metrics":["BlendedCost", "UnblendedCost", "UsageQuantity"]
}
```

#### Sample Response
<a name="API_GetCostAndUsage_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "GroupDefinitions": [
    {
      "Key": "SERVICE",
      "Type": "DIMENSION"
    },
    {
      "Key": "Environment",
      "Type": "TAG"
    }
  ],
  "ResultsByTime": [
    {
      "Estimated": false,
      "Groups": [
        {
          "Keys": [
            "Amazon Simple Storage Service",
            "Environment$Prod"
          ],
          "Metrics": {
            "BlendedCost": {
              "Amount": "39.1603300457",
              "Unit": "USD"
            },
            "UnblendedCost": {
              "Amount": "39.1603300457",
              "Unit": "USD"
            },
            "UsageQuantity": {
              "Amount": "173842.5440074444",
              "Unit": "N/A"
            }
          }
        },
        {
          "Keys": [
            "Amazon Simple Storage Service",
            "Environment$Test"
          ],
          "Metrics": {
            "BlendedCost": {
              "Amount": "0.1337464807",
              "Unit": "USD"
            },
            "UnblendedCost": {
             "Amount": "0.1337464807",
              "Unit": "USD"
            },
            "UsageQuantity": {
              "Amount": "15992.0786663399",
              "Unit": "N/A"
            }
          }
        }
      ],
      "TimePeriod": {
        "End": "2017-10-01",
        "Start": "2017-09-01"
      },
      "Total": {}
    }
  ]
}
```

## See Also
<a name="API_GetCostAndUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetCostAndUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetCostAndUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetCostAndUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetCostAndUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetCostAndUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetCostAndUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetCostAndUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetCostAndUsage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetCostAndUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetCostAndUsage)
