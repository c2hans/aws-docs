---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsageWithResources.html
---

# GetCostAndUsageWithResources
<a name="API_GetCostAndUsageWithResources"></a>

Retrieves cost and usage metrics with resources for your account. You can specify which cost and usage-related metric, such as `BlendedCosts` or `UsageQuantity`, that you want the request to return. You can also filter and group your data by various dimensions, such as `SERVICE` or `AZ`, in a specific time range. For a complete list of valid dimensions, see the [GetDimensionValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html) operation. Management account in an organization in AWS Organizations have access to all member accounts.

Hourly granularity is only available for EC2-Instances (Elastic Compute Cloud) resource-level data. All other resource-level data is available at daily granularity.

**Note**
This is an opt-in only feature. You can enable this feature from the Cost Explorer Settings page. For information about how to access the Settings page, see [Controlling Access for Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-access.html) in the * AWS Billing and Cost Management User Guide*.

## Request Syntax
<a name="API_GetCostAndUsageWithResources_RequestSyntax"></a>

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
<a name="API_GetCostAndUsageWithResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BillingViewArn](#API_GetCostAndUsageWithResources_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageWithResources-request-BillingViewArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to AWS Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[-a-zA-Z0-9/:_+=.-@]{1,43}$`
Required: No

 ** [Filter](#API_GetCostAndUsageWithResources_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageWithResources-request-Filter"></a>
Filters Amazon Web Services costs by different dimensions. For example, you can specify `SERVICE` and `LINKED_ACCOUNT` and get the costs that are associated with that account's usage of that service. You can nest `Expression` objects to define any combination of dimension filters. For more information, see [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html).
The `GetCostAndUsageWithResources` operation requires that you either group by or filter by a `ResourceId`. It requires the [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html) `"SERVICE = Amazon Elastic Compute Cloud - Compute"` in the filter.
Valid values for `MatchOptions` for `Dimensions` are `EQUALS` and `CASE_SENSITIVE`.
Valid values for `MatchOptions` for `CostCategories`, `Tags`, and `ProductAttributes` are `EQUALS`, `ABSENT`, and `CASE_SENSITIVE`. Default values are `EQUALS` and `CASE_SENSITIVE`.
If you filter or group by product attributes, the `SERVICE` filter rules are the same as for [GetCostAndUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsage.html).
Type: [Expression](API_Expression.md) object
Required: Yes

 ** [Granularity](#API_GetCostAndUsageWithResources_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageWithResources-request-Granularity"></a>
Sets the AWS cost granularity to `MONTHLY`, `DAILY`, or `HOURLY`. If `Granularity` isn't set, the response object doesn't include the `Granularity`, `MONTHLY`, `DAILY`, or `HOURLY`.
Type: String
Valid Values: `DAILY | MONTHLY | HOURLY`
Required: Yes

 ** [GroupBy](#API_GetCostAndUsageWithResources_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageWithResources-request-GroupBy"></a>
You can group Amazon Web Services costs using up to two different groups: `DIMENSION`, `TAG`, `COST_CATEGORY`, and `PRODUCT_ATTRIBUTE`.
 `PRODUCT_ATTRIBUTE` groups work the same way as in [GetCostAndUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsage.html). A `PRODUCT_ATTRIBUTE` group or a `ProductAttributes` filter doesn't meet the requirement to group by or filter by a `ResourceId`.
Type: Array of [GroupDefinition](API_GroupDefinition.md) objects
Required: No

 ** [Metrics](#API_GetCostAndUsageWithResources_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageWithResources-request-Metrics"></a>
Which metrics are returned in the query. For more information about blended and unblended rates, see [Why does the "blended" annotation appear on some line items in my bill?](http://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/).
Valid values are `AmortizedCost`, `BlendedCost`, `NetAmortizedCost`, `NetUnblendedCost`, `NormalizedUsageAmount`, `UnblendedCost`, and `UsageQuantity`.
If you return the `UsageQuantity` metric, the service aggregates all usage numbers without taking the units into account. For example, if you aggregate `usageQuantity` across all of Amazon EC2, the results aren't meaningful because Amazon EC2 compute hours and data transfer are measured in different units (for example, hour or GB). To get more meaningful `UsageQuantity` metrics, filter by `UsageType` or `UsageTypeGroups`.
 `Metrics` is required for `GetCostAndUsageWithResources` requests.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [NextPageToken](#API_GetCostAndUsageWithResources_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageWithResources-request-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [TimePeriod](#API_GetCostAndUsageWithResources_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageWithResources-request-TimePeriod"></a>
Sets the start and end dates for retrieving Amazon Web Services costs. The range must be within the last 14 days (the start date cannot be earlier than 14 days ago). The start date is inclusive, but the end date is exclusive. For example, if `start` is `2017-01-01` and `end` is `2017-05-01`, then the cost and usage data is retrieved from `2017-01-01` up to and including `2017-04-30` but not including `2017-05-01`.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

## Response Syntax
<a name="API_GetCostAndUsageWithResources_ResponseSyntax"></a>

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
<a name="API_GetCostAndUsageWithResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DimensionValueAttributes](#API_GetCostAndUsageWithResources_ResponseSyntax) **   <a name="awscostmanagement-GetCostAndUsageWithResources-response-DimensionValueAttributes"></a>
The attributes that apply to a specific dimension value. For example, if the value is a linked account, the attribute is that account name.
Type: Array of [DimensionValuesWithAttributes](API_DimensionValuesWithAttributes.md) objects

 ** [GroupDefinitions](#API_GetCostAndUsageWithResources_ResponseSyntax) **   <a name="awscostmanagement-GetCostAndUsageWithResources-response-GroupDefinitions"></a>
The groups that are specified by the `Filter` or `GroupBy` parameters in the request.
Type: Array of [GroupDefinition](API_GroupDefinition.md) objects

 ** [NextPageToken](#API_GetCostAndUsageWithResources_ResponseSyntax) **   <a name="awscostmanagement-GetCostAndUsageWithResources-response-NextPageToken"></a>
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [ResultsByTime](#API_GetCostAndUsageWithResources_ResponseSyntax) **   <a name="awscostmanagement-GetCostAndUsageWithResources-response-ResultsByTime"></a>
The time period that's covered by the results in the response.
Type: Array of [ResultByTime](API_ResultByTime.md) objects

## Errors
<a name="API_GetCostAndUsageWithResources_Errors"></a>

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
<a name="API_GetCostAndUsageWithResources_Examples"></a>

### Example
<a name="API_GetCostAndUsageWithResources_Example_1"></a>

The following is a sample request and response of the `GetCostAndUsageWithResources` operation that enables you to retrieve your Amazon EC2 costs. For more complex examples, such as multi-level groupings, see [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html).

#### Sample Request
<a name="API_GetCostAndUsageWithResources_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ce.us-east-1.amazonaws.com
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSInsightsIndexService.GetCostAndUsageWithResources
{
  "TimePeriod": {
    "Start":"2018-11-19",
    "End": "2018-11-20"
  },
  "Granularity": "DAILY",
  "Filter": {
    "Dimensions": {
      "Key": "SERVICE",
      "Values": [
        "Amazon Elastic Compute Cloud - Compute"
      ]
    }
  },
  "GroupBy":[
    {
      "Type":"DIMENSION",
      "Key":"RESOURCE_ID"
    }
  ],
   "Metrics":["BlendedCost", "UnblendedCost", "UsageQuantity"]
}
```

#### Sample Response
<a name="API_GetCostAndUsageWithResources_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "GroupDefinitions": [
    {
      "Key": "RESOURCE_ID",
      "Type": "DIMENSION"
    }
  ],
  "ResultsByTime": [
    {
      "Estimated": true,
      "Groups": [
        {
          "Keys": [
            "i-00cb32c5f3163"
          ],
          "Metrics": {
            "BlendedCost": {
              "Amount": "0.0927335232",
              "Unit": "USD"
            },
            "UnblendedCost": {
              "Amount": "0.1276",
              "Unit": "USD"
            },
            "UsageQuantity": {
              "Amount": "24.0010557602",
              "Unit": "N/A"
            }
          }
        },
        {
          "Keys": [
            "i-04a0089019f41"
          ],
          "Metrics": {
            "BlendedCost": {
              "Amount": "0.1656",
              "Unit": "USD"
            },
            "UnblendedCost": {
              "Amount": "0.1656",
              "Unit": "USD"
            },
            "UsageQuantity": {
              "Amount": "24.0018044403",
              "Unit": "N/A"
            }
          }
        },
        {
          "Keys": [
            "i-03b49bda9fdef"
          ],
          "Metrics": {
            "BlendedCost": {
              "Amount": "0.0927335232",
              "Unit": "USD"
            },
            "UnblendedCost": {
              "Amount": "0.0116",
              "Unit": "USD"
            },
            "UsageQuantity": {
              "Amount": "24.0009345564",
              "Unit": "N/A"
            }
          }
        },
        {
          "Keys": [
            "i-0e56e09d11711"
          ],
          "Metrics": {
            "BlendedCost": {
              "Amount": "0.0927335232",
              "Unit": "USD"
            },
            "UnblendedCost": {
              "Amount": "0.1392",
              "Unit": "USD"
            },
            "UsageQuantity": {
              "Amount": "24.0011066563",
              "Unit": "N/A"
            }
          }
        }
      ],
      "TimePeriod": {
        "End": "2018-11-20T00:00:00Z",
        "Start": "2018-11-19T00:00:00Z"
      },
      "Total": {}
    }
  ]
}
```

## See Also
<a name="API_GetCostAndUsageWithResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetCostAndUsageWithResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetCostAndUsageWithResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetCostAndUsageWithResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetCostAndUsageWithResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetCostAndUsageWithResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetCostAndUsageWithResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetCostAndUsageWithResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetCostAndUsageWithResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetCostAndUsageWithResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetCostAndUsageWithResources)
