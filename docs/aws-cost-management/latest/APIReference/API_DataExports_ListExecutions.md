---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListExecutions.html
---

# ListExecutions
<a name="API_DataExports_ListExecutions"></a>

Lists the historical executions for the export.

## Request Syntax
<a name="API_DataExports_ListExecutions_RequestSyntax"></a>

```
{
   "ExportArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DataExports_ListExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExportArn](#API_DataExports_ListExecutions_RequestSyntax) **   <a name="awscostmanagement-DataExports_ListExecutions-request-ExportArn"></a>
The Amazon Resource Name (ARN) for this export.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:(bcm-data-exports):[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

 ** [MaxResults](#API_DataExports_ListExecutions_RequestSyntax) **   <a name="awscostmanagement-DataExports_ListExecutions-request-MaxResults"></a>
The maximum number of objects that are returned for the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 300.
Required: No

 ** [NextToken](#API_DataExports_ListExecutions_RequestSyntax) **   <a name="awscostmanagement-DataExports_ListExecutions-request-NextToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_DataExports_ListExecutions_ResponseSyntax"></a>

```
{
   "Executions": [
      {
         "ExecutionId": "string",
         "ExecutionStatus": {
            "CompletedAt": "string",
            "CreatedAt": "string",
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
<a name="API_DataExports_ListExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Executions](#API_DataExports_ListExecutions_ResponseSyntax) **   <a name="awscostmanagement-DataExports_ListExecutions-response-Executions"></a>
The list of executions.
Type: Array of [ExecutionReference](API_DataExports_ExecutionReference.md) objects

 ** [NextToken](#API_DataExports_ListExecutions_ResponseSyntax) **   <a name="awscostmanagement-DataExports_ListExecutions-response-NextToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_DataExports_ListExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified Amazon Resource Name (ARN) in the request doesn't exist.
 ** ResourceId **
The identifier of the resource that was not found.
 ** ResourceType **
The type of the resource that was not found.
HTTP Status Code: 400

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
<a name="API_DataExports_ListExecutions_Examples"></a>

### The following is a sample request of the ListExecutions operation.
<a name="API_DataExports_ListExecutions_Example_1"></a>

This example illustrates one usage of ListExecutions.

#### Sample Request
<a name="API_DataExports_ListExecutions_Example_1_Request"></a>

```
{
  "ExportArn": "arn:aws:bcm-data-exports:::export:Example/837fcfce-f85b-4600-b333-b38a12c3a927",
  "MaxResults": 100,
  "NextToken": ""
}
```

### The following is a sample response of the ListExecutions operation.
<a name="API_DataExports_ListExecutions_Example_2"></a>

This example illustrates one usage of ListExecutions.

#### Sample Response
<a name="API_DataExports_ListExecutions_Example_2_Response"></a>

```
{
    "Executions": [
        {
            "ExecutionId": "f0cfeaf0-c552-47e7-82bc-0107fbfc7a8b",
            "ExecutionStatus": {
                "CreatedAt": "2023-11-14T18:14:12.813Z",
                "LastUpdatedAt": "2023-11-14T18:18:14.252556820Z",
                "StatusCode": "DELIVERY_SUCCESS"
            }
        },
        {
            "ExecutionId": "2c173333-4b14-4740-98a1-d52304eced2d",
            "ExecutionStatus": {
                "CreatedAt": "2023-11-14T09:20:47.137Z",
                "LastUpdatedAt": "2023-11-14T09:53:48.285265457Z",
                "StatusCode": "DELIVERY_SUCCESS"
            }
        }
    ]
}
```

## See Also
<a name="API_DataExports_ListExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-data-exports-2023-11-26/ListExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-data-exports-2023-11-26/ListExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/ListExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-data-exports-2023-11-26/ListExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/ListExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-data-exports-2023-11-26/ListExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-data-exports-2023-11-26/ListExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-data-exports-2023-11-26/ListExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-data-exports-2023-11-26/ListExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/ListExecutions)
