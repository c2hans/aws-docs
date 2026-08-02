---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetTags.html
---

# GetTags
<a name="API_GetTags"></a>

Queries for available tag keys and tag values for a specified period. You can search the tag values for an arbitrary string.

## Request Syntax
<a name="API_GetTags_RequestSyntax"></a>

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
      "Tags": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      }
   },
   "MaxResults": {{number}},
   "NextPageToken": "{{string}}",
   "SearchString": "{{string}}",
   "SortBy": [
      {
         "Key": "{{string}}",
         "SortOrder": "{{string}}"
      }
   ],
   "TagKey": "{{string}}",
   "TimePeriod": {
      "End": "{{string}}",
      "Start": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BillingViewArn](#API_GetTags_RequestSyntax) **   <a name="awscostmanagement-GetTags-request-BillingViewArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to AWS Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[-a-zA-Z0-9/:_+=.-@]{1,43}$`
Required: No

 ** [Filter](#API_GetTags_RequestSyntax) **   <a name="awscostmanagement-GetTags-request-Filter"></a>
Use `Expression` to filter in various Cost Explorer APIs.
Not all `Expression` types are supported in each API. Refer to the documentation for each specific API to see what is supported.
There are two patterns:
+ Simple dimension values.
  + There are three types of simple dimension values: `CostCategories`, `Tags`, and `Dimensions`.
    + Specify the `CostCategories` field to define a filter that acts on Cost Categories.
    + Specify the `Tags` field to define a filter that acts on Cost Allocation Tags.
    + Specify the `Dimensions` field to define a filter that acts on the [https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues.html](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues.html).
  + For each filter type, you can set the dimension name and values for the filters that you plan to use.
    + For example, you can filter for `REGION==us-east-1 OR REGION==us-west-1`. For `GetRightsizingRecommendation`, the Region is a full name (for example, `REGION==US East (N. Virginia)`.
    + The corresponding `Expression` for this example is as follows: `{ "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] } }`
    + As shown in the previous example, lists of dimension values are combined with `OR` when applying the filter.
  + You can also set different match options to further control how the filter behaves. Not all APIs support match options. Refer to the documentation for each specific API to see what is supported.
    + For example, you can filter for linked account names that start with "a".
    + The corresponding `Expression` for this example is as follows: `{ "Dimensions": { "Key": "LINKED_ACCOUNT_NAME", "MatchOptions": [ "STARTS_WITH" ], "Values": [ "a" ] } }`
+ Compound `Expression` types with logical operations.
  + You can use multiple `Expression` types and the logical operators `AND/OR/NOT` to create a list of one or more `Expression` objects. By doing this, you can filter by more advanced options.
  + For example, you can filter by `((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`.
  + The corresponding `Expression` for this example is as follows: `{ "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] } `
**Note**
Because each `Expression` can have only one operator, the service returns an error if more than one is specified. The following example shows an `Expression` object that creates an error: ` { "And": [ ... ], "Dimensions": { "Key": "USAGE_TYPE", "Values": [ "DataTransfer" ] } } `
The following is an example of the corresponding error message: `"Expression has more than one roots. Only one root operator is allowed for each expression: And, Or, Not, Dimensions, Tags, CostCategories"`
For the `GetRightsizingRecommendation` action, a combination of OR and NOT isn't supported. OR isn't supported between different dimensions, or dimensions and tags. NOT operators aren't supported. Dimensions are also limited to `LINKED_ACCOUNT`, `REGION`, or `RIGHTSIZING_TYPE`.
For the `GetReservationPurchaseRecommendation` action, only NOT is supported. AND and OR aren't supported. Dimensions are limited to `LINKED_ACCOUNT`.
Type: [Expression](API_Expression.md) object
Required: No

 ** [MaxResults](#API_GetTags_RequestSyntax) **   <a name="awscostmanagement-GetTags-request-MaxResults"></a>
This field is only used when SortBy is provided in the request. The maximum number of objects that are returned for this request. If MaxResults isn't specified with SortBy, the request returns 1000 results as the default value for this parameter.
For `GetTags`, MaxResults has an upper quota of 1000.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextPageToken](#API_GetTags_RequestSyntax) **   <a name="awscostmanagement-GetTags-request-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [SearchString](#API_GetTags_RequestSyntax) **   <a name="awscostmanagement-GetTags-request-SearchString"></a>
The value that you want to search for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [SortBy](#API_GetTags_RequestSyntax) **   <a name="awscostmanagement-GetTags-request-SortBy"></a>
The value that you want to sort the data by.
The key represents cost and usage metrics. The following values are supported:
+  `BlendedCost`
+  `UnblendedCost`
+  `AmortizedCost`
+  `NetAmortizedCost`
+  `NetUnblendedCost`
+  `UsageQuantity`
+  `NormalizedUsageAmount`
The supported values for `SortOrder` are `ASCENDING` and `DESCENDING`.
When you use `SortBy`, `NextPageToken` and `SearchString` aren't supported.
Type: Array of [SortDefinition](API_SortDefinition.md) objects
Required: No

 ** [TagKey](#API_GetTags_RequestSyntax) **   <a name="awscostmanagement-GetTags-request-TagKey"></a>
The key of the tag that you want to return values for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [TimePeriod](#API_GetTags_RequestSyntax) **   <a name="awscostmanagement-GetTags-request-TimePeriod"></a>
The start and end dates for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if `start` is `2017-01-01` and `end` is `2017-05-01`, then the cost and usage data is retrieved from `2017-01-01` up to and including `2017-04-30` but not including `2017-05-01`.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

## Response Syntax
<a name="API_GetTags_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "ReturnSize": number,
   "Tags": [ "string" ],
   "TotalSize": number
}
```

## Response Elements
<a name="API_GetTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_GetTags_ResponseSyntax) **   <a name="awscostmanagement-GetTags-response-NextPageToken"></a>
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [ReturnSize](#API_GetTags_ResponseSyntax) **   <a name="awscostmanagement-GetTags-response-ReturnSize"></a>
The number of query results that AWS returns at a time.
Type: Integer

 ** [Tags](#API_GetTags_ResponseSyntax) **   <a name="awscostmanagement-GetTags-response-Tags"></a>
The tags that match your request.
Type: Array of strings

 ** [TotalSize](#API_GetTags_ResponseSyntax) **   <a name="awscostmanagement-GetTags-response-TotalSize"></a>
The total number of query results.
Type: Integer

## Errors
<a name="API_GetTags_Errors"></a>

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
<a name="API_GetTags_Examples"></a>

### Example
<a name="API_GetTags_Example_1"></a>

The following example shows how to retrieve the list of tag keys using the `GetTags` operation.

#### Sample Request
<a name="API_GetTags_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ce.us-east-1.amazonaws.com
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSInsightsIndexService.GetTags
{
  "TimePeriod": {
    "Start": "2017-01-01",
    "End": "2017-05-18"
  },
  "TagKey": "Project",
  "SearchString": "secretProject"
}
```

#### Sample Response
<a name="API_GetTags_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "ReturnSize": 2,
  "Tags": [
    secretProject1",
    "secretProject2"
    ],
  "TotalSize": 2
}
```

## See Also
<a name="API_GetTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetTags)
