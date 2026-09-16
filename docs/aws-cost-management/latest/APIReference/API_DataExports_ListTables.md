---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListTables.html
---

# ListTables
<a name="API_DataExports_ListTables"></a>

Lists all available tables in data exports.

## Request Syntax
<a name="API_DataExports_ListTables_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DataExports_ListTables_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DataExports_ListTables_RequestSyntax) **   <a name="awscostmanagement-DataExports_ListTables-request-MaxResults"></a>
The maximum number of objects that are returned for the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 300.
Required: No

 ** [NextToken](#API_DataExports_ListTables_RequestSyntax) **   <a name="awscostmanagement-DataExports_ListTables-request-NextToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_DataExports_ListTables_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Tables": [
      {
         "Description": "string",
         "TableName": "string",
         "TableProperties": [
            {
               "DefaultValue": "string",
               "Description": "string",
               "Name": "string",
               "ValidValues": [ "string" ]
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DataExports_ListTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DataExports_ListTables_ResponseSyntax) **   <a name="awscostmanagement-DataExports_ListTables-response-NextToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [Tables](#API_DataExports_ListTables_ResponseSyntax) **   <a name="awscostmanagement-DataExports_ListTables-response-Tables"></a>
The list of tables.
Type: Array of [Table](API_DataExports_Table.md) objects

## Errors
<a name="API_DataExports_ListTables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** QuotaCode **
The quota code that exceeded the throttling limit.
 ** ServiceCode **
The service code that exceeded the throttling limit. It will always be “AWSBillingAndCostManagementDataExports”.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Fields **
The list of fields that are invalid.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## Examples
<a name="API_DataExports_ListTables_Examples"></a>

### The following is a sample request of the ListTables operation.
<a name="API_DataExports_ListTables_Example_1"></a>

This example illustrates one usage of ListTables.

#### Sample Request
<a name="API_DataExports_ListTables_Example_1_Request"></a>

```
{
    "MaxResults": 100,
    "NextToken": ""
}
```

### The following is a sample response of the ListTables operation.
<a name="API_DataExports_ListTables_Example_2"></a>

This example illustrates one usage of ListTables.

#### Sample Response
<a name="API_DataExports_ListTables_Example_2_Response"></a>

```
{
    "Tables": [
        {
            "Description": "A view over CUR for CostAndUsageDashboard",
            "TableName": "COST_AND_USAGE_DASHBOARD",
            "TableProperties": [
                {}
            ]
        },
        {
            "Description": "Cost and Usage Report",
            "TableName": "COST_AND_USAGE_REPORT",
            "TableProperties": [
                {
                    "DefaultValue": "HOURLY",
                    "Description": "The granularity of the line-items in the table.",
                    "Name": "TIME_GRANULARITY",
                    "ValidValues": [
                        "DAILY",
                        "MONTHLY",
                        "HOURLY"
                    ]
                },
                {
                    "DefaultValue": "FALSE",
                    "Description": "Whether to simulate manual discounts for automated discount data.",
                    "Name": "INCLUDE_MANUAL_DISCOUNT_COMPATIBILITY",
                    "ValidValues": [
                        "TRUE",
                        "FALSE"
                    ]
                },
                {
                    "DefaultValue": "FALSE",
                    "Description": "Whether to include fission columns.",
                    "Name": "INCLUDE_SPLIT_COST_ALLOCATION_DATA",
                    "ValidValues": [
                        "TRUE",
                        "FALSE"
                    ]
                },
                {
                    "DefaultValue": "FALSE",
                    "Description": "Whether to include resource IDs on line items.",
                    "Name": "INCLUDE_RESOURCES",
                    "ValidValues": [
                        "TRUE",
                        "FALSE"
                    ]
                },
                {
                    "Description": "Specifies whether to include capacity reservation data in the data export.",
                    "Name": "INCLUDE_CAPACITY_RESERVATION_DATA",
                    "ValidValues": [
                        "TRUE",
                        "FALSE"
                    ]
                },
                {
                    "Description": "The Amazon Resource Name (ARN) of the billing group for this data export.",
                    "Name": "BILLING_VIEW_ARN",
                    "ValidValues": []
                },
                {
                    "Description": "Specifies whether to include Identity and Access Management (IAM) principal columns.",
                    "Name": "INCLUDE_IAM_PRINCIPAL_DATA",
                    "ValidValues": [
                        "TRUE",
                        "FALSE"
                    ]
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_DataExports_ListTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-data-exports-2023-11-26/ListTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-data-exports-2023-11-26/ListTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/ListTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-data-exports-2023-11-26/ListTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/ListTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-data-exports-2023-11-26/ListTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-data-exports-2023-11-26/ListTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-data-exports-2023-11-26/ListTables)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bcm-data-exports-2023-11-26/ListTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/ListTables)
