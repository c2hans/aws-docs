---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html
---

# GetDimensionValues
<a name="API_GetDimensionValues"></a>

Retrieves all available filter values for a specified filter over a period of time. You can search the dimension values for an arbitrary string.

## Request Syntax
<a name="API_GetDimensionValues_RequestSyntax"></a>

```
{
   "BillingViewArn": "{{string}}",
   "Context": "{{string}}",
   "Dimension": "{{string}}",
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
   "TimePeriod": {
      "End": "{{string}}",
      "Start": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetDimensionValues_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BillingViewArn](#API_GetDimensionValues_RequestSyntax) **   <a name="awscostmanagement-GetDimensionValues-request-BillingViewArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to AWS Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[-a-zA-Z0-9/:_+=.-@]{1,43}$`
Required: No

 ** [Context](#API_GetDimensionValues_RequestSyntax) **   <a name="awscostmanagement-GetDimensionValues-request-Context"></a>
The context for the call to `GetDimensionValues`. This can be `RESERVATIONS` or `COST_AND_USAGE`. The default value is `COST_AND_USAGE`. If the context is set to `RESERVATIONS`, the resulting dimension values can be used in the `GetReservationUtilization` operation. If the context is set to `COST_AND_USAGE`, the resulting dimension values can be used in the `GetCostAndUsage` operation.
If you set the context to `COST_AND_USAGE`, you can use the following dimensions for searching:
+ AZ - The Availability Zone. An example is `us-east-1a`.
+ BILLING\_ENTITY - The AWS seller that your account is with. Possible values are the following:

  - AWS(Amazon Web Services): The entity that sells AWS services.

  - AISPL (Amazon Internet Services Pvt. Ltd.): The local Indian entity that's an acting reseller for AWS services in India.

  - AWS Marketplace: The entity that supports the sale of solutions that are built on AWS by third-party software providers.
+ CACHE\_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.
+ DEPLOYMENT\_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are `SingleAZ` and `MultiAZ`.
+ DATABASE\_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.
+ INSTANCE\_TYPE - The type of Amazon EC2 instance. An example is `m4.xlarge`.
+ INSTANCE\_TYPE\_FAMILY - A family of instance types optimized to fit different use cases. Examples are `Compute Optimized` (for example, `C4`, `C5`, `C6g`, and `C7g`), `Memory Optimization` (for example, `R4`, `R5n`, `R5b`, and `R6g`).
+ INVOICING\_ENTITY - The name of the entity that issues the AWS invoice.
+ LEGAL\_ENTITY\_NAME - The name of the organization that sells you AWS services, such as Amazon Web Services.
+ LINKED\_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
+ OPERATING\_SYSTEM - The operating system. Examples are Windows or Linux.
+ OPERATION - The action performed. Examples include `RunInstance` and `CreateBucket`.
+ PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
+ PURCHASE\_TYPE - The reservation type of the purchase that this usage is related to. Examples include On-Demand Instances and Standard Reserved Instances.
+ RESERVATION\_ID - The unique identifier for an AWS Reservation Instance.
+ SAVINGS\_PLAN\_ARN - The unique identifier for your Savings Plans.
+ SAVINGS\_PLANS\_TYPE - Type of Savings Plans (EC2 Instance or Compute).
+ SERVICE - The AWS service such as Amazon DynamoDB.
+ TENANCY - The tenancy of a resource. Examples are shared or dedicated.
+ USAGE\_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the `GetDimensionValues` operation includes a unit attribute. Examples include GB and Hrs.
+ USAGE\_TYPE\_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch – Alarms. The response for this operation includes a unit attribute.
+ REGION - The AWS Region.
+ RECORD\_TYPE - The different types of charges such as Reserved Instance (RI) fees, usage costs, tax refunds, and credits.
+ RESOURCE\_ID - The unique identifier of the resource. ResourceId is an opt-in feature only available for last 14 days for EC2-Compute Service.
If you set the context to `RESERVATIONS`, you can use the following dimensions for searching:
+ AZ - The Availability Zone. An example is `us-east-1a`.
+ CACHE\_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.
+ DEPLOYMENT\_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are `SingleAZ` and `MultiAZ`.
+ INSTANCE\_TYPE - The type of Amazon EC2 instance. An example is `m4.xlarge`.
+ LINKED\_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
+ PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
+ REGION - The AWS Region.
+ SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.
+ TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).
+ TENANCY - The tenancy of a resource. Examples are shared or dedicated.
If you set the context to `SAVINGS_PLANS`, you can use the following dimensions for searching:
+ SAVINGS\_PLANS\_TYPE - Type of Savings Plans (EC2 Instance or Compute)
+ PAYMENT\_OPTION - The payment option for the given Savings Plans (for example, All Upfront)
+ REGION - The AWS Region.
+ INSTANCE\_TYPE\_FAMILY - The family of instances (For example, `m5`)
+ LINKED\_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
+ SAVINGS\_PLAN\_ARN - The unique identifier for your Savings Plans.
Type: String
Valid Values: `COST_AND_USAGE | RESERVATIONS | SAVINGS_PLANS`
Required: No

 ** [Dimension](#API_GetDimensionValues_RequestSyntax) **   <a name="awscostmanagement-GetDimensionValues-request-Dimension"></a>
The name of the dimension. Each `Dimension` is available for a different `Context`. For more information, see `Context`. `LINK_ACCOUNT_NAME` and `SERVICE_CODE` can only be used in [CostCategoryRule](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/AAPI_CostCategoryRule.html).
Type: String
Valid Values: `AZ | INSTANCE_TYPE | LINKED_ACCOUNT | PAYER_ACCOUNT | LINKED_ACCOUNT_NAME | OPERATION | PURCHASE_TYPE | REGION | SERVICE | SERVICE_CODE | USAGE_TYPE | USAGE_TYPE_GROUP | RECORD_TYPE | OPERATING_SYSTEM | TENANCY | SCOPE | PLATFORM | SUBSCRIPTION_ID | LEGAL_ENTITY_NAME | DEPLOYMENT_OPTION | DATABASE_ENGINE | CACHE_ENGINE | INSTANCE_TYPE_FAMILY | BILLING_ENTITY | RESERVATION_ID | RESOURCE_ID | RIGHTSIZING_TYPE | SAVINGS_PLANS_TYPE | SAVINGS_PLAN_ARN | PAYMENT_OPTION | AGREEMENT_END_DATE_TIME_AFTER | AGREEMENT_END_DATE_TIME_BEFORE | INVOICING_ENTITY | ANOMALY_TOTAL_IMPACT_ABSOLUTE | ANOMALY_TOTAL_IMPACT_PERCENTAGE`
Required: Yes

 ** [Filter](#API_GetDimensionValues_RequestSyntax) **   <a name="awscostmanagement-GetDimensionValues-request-Filter"></a>
Use `Expression` to filter in various Cost Explorer APIs.
Not all `Expression` types are supported in each API. Refer to the documentation for each specific API to see what is supported.
There are two patterns:
+ Simple dimension values.
  + There are three types of simple dimension values: `CostCategories`, `Tags`, and `Dimensions`.
    + Specify the `CostCategories` field to define a filter that acts on Cost Categories.
    + Specify the `Tags` field to define a filter that acts on Cost Allocation Tags.
    + Specify the `Dimensions` field to define a filter that acts on the [`DimensionValues`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues.html).
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

 ** [MaxResults](#API_GetDimensionValues_RequestSyntax) **   <a name="awscostmanagement-GetDimensionValues-request-MaxResults"></a>
This field is only used when SortBy is provided in the request. The maximum number of objects that are returned for this request. If MaxResults isn't specified with SortBy, the request returns 1000 results as the default value for this parameter.
For `GetDimensionValues`, MaxResults has an upper limit of 1000.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextPageToken](#API_GetDimensionValues_RequestSyntax) **   <a name="awscostmanagement-GetDimensionValues-request-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [SearchString](#API_GetDimensionValues_RequestSyntax) **   <a name="awscostmanagement-GetDimensionValues-request-SearchString"></a>
The value that you want to search the filter values for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [SortBy](#API_GetDimensionValues_RequestSyntax) **   <a name="awscostmanagement-GetDimensionValues-request-SortBy"></a>
The value that you want to sort the data by.
The key represents cost and usage metrics. The following values are supported:
+  `BlendedCost`
+  `UnblendedCost`
+  `AmortizedCost`
+  `NetAmortizedCost`
+  `NetUnblendedCost`
+  `UsageQuantity`
+  `NormalizedUsageAmount`
The supported values for the `SortOrder` key are `ASCENDING` or `DESCENDING`.
When you specify a `SortBy` paramater, the context must be `COST_AND_USAGE`. Further, when using `SortBy`, `NextPageToken` and `SearchString` aren't supported.
Type: Array of [SortDefinition](API_SortDefinition.md) objects
Required: No

 ** [TimePeriod](#API_GetDimensionValues_RequestSyntax) **   <a name="awscostmanagement-GetDimensionValues-request-TimePeriod"></a>
The start date and end date for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if `start` is `2017-01-01` and `end` is `2017-05-01`, then the cost and usage data is retrieved from `2017-01-01` up to and including `2017-04-30` but not including `2017-05-01`.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

## Response Syntax
<a name="API_GetDimensionValues_ResponseSyntax"></a>

```
{
   "DimensionValues": [
      {
         "Attributes": {
            "string" : "string"
         },
         "Value": "string"
      }
   ],
   "NextPageToken": "string",
   "ReturnSize": number,
   "TotalSize": number
}
```

## Response Elements
<a name="API_GetDimensionValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DimensionValues](#API_GetDimensionValues_ResponseSyntax) **   <a name="awscostmanagement-GetDimensionValues-response-DimensionValues"></a>
The filters that you used to filter your request. Some dimensions are available only for a specific context.
If you set the context to `COST_AND_USAGE`, you can use the following dimensions for searching:
+ AZ - The Availability Zone. An example is `us-east-1a`.
+ DATABASE\_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.
+ INSTANCE\_TYPE - The type of Amazon EC2 instance. An example is `m4.xlarge`.
+ LEGAL\_ENTITY\_NAME - The name of the organization that sells you AWS services, such as Amazon Web Services.
+ LINKED\_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
+ OPERATING\_SYSTEM - The operating system. Examples are Windows or Linux.
+ OPERATION - The action performed. Examples include `RunInstance` and `CreateBucket`.
+ PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
+ PURCHASE\_TYPE - The reservation type of the purchase to which this usage is related. Examples include On-Demand Instances and Standard Reserved Instances.
+ SERVICE - The AWS service such as Amazon DynamoDB.
+ USAGE\_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the `GetDimensionValues` operation includes a unit attribute. Examples include GB and Hrs.
+ USAGE\_TYPE\_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch – Alarms. The response for this operation includes a unit attribute.
+ RECORD\_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and credits.
+ RESOURCE\_ID - The unique identifier of the resource. ResourceId is an opt-in feature only available for last 14 days for EC2-Compute Service. You can opt-in by enabling `Hourly` and `Resource Level Data` in AWS Cost Management Console preferences.
If you set the context to `RESERVATIONS`, you can use the following dimensions for searching:
+ AZ - The Availability Zone. An example is `us-east-1a`.
+ CACHE\_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.
+ DEPLOYMENT\_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are `SingleAZ` and `MultiAZ`.
+ INSTANCE\_TYPE - The type of Amazon EC2 instance. An example is `m4.xlarge`.
+ LINKED\_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
+ PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
+ REGION - The AWS Region.
+ SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.
+ TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).
+ TENANCY - The tenancy of a resource. Examples are shared or dedicated.
If you set the context to `SAVINGS_PLANS`, you can use the following dimensions for searching:
+ SAVINGS\_PLANS\_TYPE - Type of Savings Plans (EC2 Instance or Compute)
+ PAYMENT\_OPTION - Payment option for the given Savings Plans (for example, All Upfront)
+ REGION - The AWS Region.
+ INSTANCE\_TYPE\_FAMILY - The family of instances (For example, `m5`)
+ LINKED\_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
+ SAVINGS\_PLAN\_ARN - The unique identifier for your Savings Plan
Type: Array of [DimensionValuesWithAttributes](API_DimensionValuesWithAttributes.md) objects

 ** [NextPageToken](#API_GetDimensionValues_ResponseSyntax) **   <a name="awscostmanagement-GetDimensionValues-response-NextPageToken"></a>
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [ReturnSize](#API_GetDimensionValues_ResponseSyntax) **   <a name="awscostmanagement-GetDimensionValues-response-ReturnSize"></a>
The number of results that AWS returned at one time.
Type: Integer

 ** [TotalSize](#API_GetDimensionValues_ResponseSyntax) **   <a name="awscostmanagement-GetDimensionValues-response-TotalSize"></a>
The total number of search results.
Type: Integer

## Errors
<a name="API_GetDimensionValues_Errors"></a>

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
<a name="API_GetDimensionValues_Examples"></a>

### Example
<a name="API_GetDimensionValues_Example_1"></a>

The following is a sample request and response of the `GetDimensionValues` operation that enables you to search for all the member accounts in an organization in AWS Organizations that have "Elastic" in their name.

#### Sample Request
<a name="API_GetDimensionValues_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ce.us-east-1.amazonaws.com
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSInsightsIndexService.GetDimensionValues
{
  "TimePeriod": {
    "Start": "2017-01-01",
    "End": "2017-05-18"
  },
  "SearchString": "Elastic",
  "Dimension": "Service"
}
```

#### Sample Response
<a name="API_GetDimensionValues_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
//Attributes are optional metadata that are returned depending on the dimension that you select.
{
  "DimensionValues": [
    {
      "Attributes": {},
      "Value": "Amazon ElastiCache"
    },
    {
      "Attributes": {},
      "Value": "EC2 - Other"
    },
    {
      "Attributes": {},
      "Value": "Amazon Elastic Compute Cloud - Compute"
    },
    {
      "Attributes": {},
      "Value": "Amazon Elasticsearch Service"
    }
  ],
  "ReturnSize": 4,
  "TotalSize": 4
}
```

## See Also
<a name="API_GetDimensionValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetDimensionValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetDimensionValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetDimensionValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetDimensionValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetDimensionValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetDimensionValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetDimensionValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetDimensionValues)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetDimensionValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetDimensionValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
