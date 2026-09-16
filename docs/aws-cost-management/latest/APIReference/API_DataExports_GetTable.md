---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_GetTable.html
---

# GetTable
<a name="API_DataExports_GetTable"></a>

Returns the metadata for the specified table and table properties. This includes the list of columns in the table schema, their data types, and column descriptions.

## Request Syntax
<a name="API_DataExports_GetTable_RequestSyntax"></a>

```
{
   "TableName": "{{string}}",
   "TableProperties": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_DataExports_GetTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TableName](#API_DataExports_GetTable_RequestSyntax) **   <a name="awscostmanagement-DataExports_GetTable-request-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** [TableProperties](#API_DataExports_GetTable_RequestSyntax) **   <a name="awscostmanagement-DataExports_GetTable-request-TableProperties"></a>
TableProperties are additional configurations you can provide to change the data and schema of a table. Each table can have different TableProperties. Tables are not required to have any TableProperties. Each table property has a default value that it assumes if not specified.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[\S\s]*`
Value Length Constraints: Minimum length of 0. Maximum length of 16384.
Value Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_DataExports_GetTable_ResponseSyntax"></a>

```
{
   "Description": "string",
   "Schema": [
      {
         "Description": "string",
         "Name": "string",
         "Type": "string"
      }
   ],
   "TableName": "string",
   "TableProperties": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_DataExports_GetTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_DataExports_GetTable_ResponseSyntax) **   <a name="awscostmanagement-DataExports_GetTable-response-Description"></a>
The table description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`

 ** [Schema](#API_DataExports_GetTable_ResponseSyntax) **   <a name="awscostmanagement-DataExports_GetTable-response-Schema"></a>
The schema of the table.
Type: Array of [Column](API_DataExports_Column.md) objects

 ** [TableName](#API_DataExports_GetTable_ResponseSyntax) **   <a name="awscostmanagement-DataExports_GetTable-response-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`

 ** [TableProperties](#API_DataExports_GetTable_ResponseSyntax) **   <a name="awscostmanagement-DataExports_GetTable-response-TableProperties"></a>
TableProperties are additional configurations you can provide to change the data and schema of a table. Each table can have different TableProperties. Tables are not required to have any TableProperties. Each table property has a default value that it assumes if not specified.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[\S\s]*`
Value Length Constraints: Minimum length of 0. Maximum length of 16384.
Value Pattern: `[\S\s]*`

## Errors
<a name="API_DataExports_GetTable_Errors"></a>

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
<a name="API_DataExports_GetTable_Examples"></a>

### The following is a sample request of the GetTable operation.
<a name="API_DataExports_GetTable_Example_1"></a>

This example illustrates one usage of GetTable.

#### Sample Request
<a name="API_DataExports_GetTable_Example_1_Request"></a>

```
{
    "TableName": "COST_AND_USAGE_REPORT",
    "TableProperties": {
    }
}
```

### The following is a sample response of the GetTable operation.
<a name="API_DataExports_GetTable_Example_2"></a>

This example illustrates one usage of GetTable.

#### Sample Response
<a name="API_DataExports_GetTable_Example_2_Response"></a>

```
{
    "Description": "Cost and Usage Report",
    "Schema": [
        {
            "Description": "This field is generated for each line item and is unique in a given partition. This does not guarantee that the field will be unique across an entire delivery (that is, all partitions in an update) of the AWS CUR. The line item ID isn't consistent between different Cost and Usage Reports and can't be used to identify the same line item across different reports.",
            "Name": "identity_line_item_id",
            "Type": "String"
        },
        {
            "Description": "The time interval that this line item applies to, in the following format: YYYY-MM-DDTHH:mm:ssZ/YYYY-MM-DDTHH:mm:ssZ. The time interval is in UTC and can be either daily or hourly, depending on the granularity of the report.",
            "Name": "identity_time_interval",
            "Type": "String"
        },
        {
            "Description": "The ID associated with a specific line item. Until the report is final, the InvoiceId is blank.",
            "Name": "bill_invoice_id",
            "Type": "String"
        }
    ],
    "TableName": "COST_AND_USAGE_REPORT",
    "TableProperties": {
        "INCLUDE_MANUAL_DISCOUNT_COMPATIBILITY": "FALSE",
        "INCLUDE_RESOURCES": "FALSE",
        "INCLUDE_SPLIT_COST_ALLOCATION_DATA": "FALSE",
        "TIME_GRANULARITY": "HOURLY"
    }
}
```

## See Also
<a name="API_DataExports_GetTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-data-exports-2023-11-26/GetTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-data-exports-2023-11-26/GetTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/GetTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-data-exports-2023-11-26/GetTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/GetTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-data-exports-2023-11-26/GetTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-data-exports-2023-11-26/GetTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-data-exports-2023-11-26/GetTable)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bcm-data-exports-2023-11-26/GetTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/GetTable)
