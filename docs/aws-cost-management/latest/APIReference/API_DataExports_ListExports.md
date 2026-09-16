---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListExports.html
---

# ListExports
<a name="API_DataExports_ListExports"></a>

Lists all data export definitions.

## Request Syntax
<a name="API_DataExports_ListExports_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DataExports_ListExports_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DataExports_ListExports_RequestSyntax) **   <a name="awscostmanagement-DataExports_ListExports-request-MaxResults"></a>
The maximum number of objects that are returned for the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 300.
Required: No

 ** [NextToken](#API_DataExports_ListExports_RequestSyntax) **   <a name="awscostmanagement-DataExports_ListExports-request-NextToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_DataExports_ListExports_ResponseSyntax"></a>

```
{
   "Exports": [
      {
         "ExportArn": "string",
         "ExportName": "string",
         "ExportStatus": {
            "CreatedAt": "string",
            "LastRefreshedAt": "string",
            "LastUpdatedAt": "string",
            "StatusCode": "string",
            "StatusReason": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DataExports_ListExports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Exports](#API_DataExports_ListExports_ResponseSyntax) **   <a name="awscostmanagement-DataExports_ListExports-response-Exports"></a>
The details of the exports, including name and export status.
Type: Array of [ExportReference](API_DataExports_ExportReference.md) objects

 ** [NextToken](#API_DataExports_ListExports_ResponseSyntax) **   <a name="awscostmanagement-DataExports_ListExports-response-NextToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_DataExports_ListExports_Errors"></a>

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
<a name="API_DataExports_ListExports_Examples"></a>

### The following is a sample request of the ListExports operation.
<a name="API_DataExports_ListExports_Example_1"></a>

This example illustrates one usage of ListExports.

#### Sample Request
<a name="API_DataExports_ListExports_Example_1_Request"></a>

```
{
    "MaxResults": 100,
    "NextToken": ""
}
```

### The following is a sample response of the ListExports operation.
<a name="API_DataExports_ListExports_Example_2"></a>

This example illustrates one usage of ListExports.

#### Sample Response
<a name="API_DataExports_ListExports_Example_2_Response"></a>

```
{
    "Exports": [
        {
            "ExportArn": "arn:aws:bcm-data-exports:::export:Example/837fcfce-f85b-4600-b333-b38a12c3a927",
            "ExportName": "ExampleExportName1",
            "ExportStatus": {
                "CreatedAt": "2023-11-14T18:02:02.371Z",
                "LastRefreshedAt": "2023-11-14T18:18:12.592Z",
                "LastUpdatedAt": "2023-11-14T18:02:02.371Z",
                "StatusCode": "HEALTHY"
            }
        },
        {
            "ExportArn": "arn:aws:bcm-data-exports:::export:Example/837fcfce-f85b-4600-b333-b38a12c3a927",
            "ExportName": "ExampleExportName2",
            "ExportStatus": {
                "CreatedAt": "2023-11-14T18:03:02.038Z",
                "LastRefreshedAt": "2023-11-14T18:18:12.629Z",
                "LastUpdatedAt": "2023-11-14T18:03:02.038Z",
                "StatusCode": "UNHEALTHY"
            }
        }
    ]
}
```

## See Also
<a name="API_DataExports_ListExports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-data-exports-2023-11-26/ListExports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-data-exports-2023-11-26/ListExports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/ListExports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-data-exports-2023-11-26/ListExports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/ListExports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-data-exports-2023-11-26/ListExports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-data-exports-2023-11-26/ListExports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-data-exports-2023-11-26/ListExports)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bcm-data-exports-2023-11-26/ListExports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/ListExports)
