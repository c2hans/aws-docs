---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplicationOperations.html
---

# ListApplicationOperations
<a name="API_ListApplicationOperations"></a>

Lists all the operations performed for the specified application such as UpdateApplication, StartApplication etc. The response also includes a summary of the operation.

To get the complete description of a specific operation, invoke the [DescribeApplicationOperation](API_DescribeApplicationOperation.md) operation.

**Note**
This operation is supported only for Managed Service for Apache Flink.

## Request Syntax
<a name="API_ListApplicationOperations_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "Operation": "{{string}}",
   "OperationStatus": "{{string}}"
}
```

## Request Parameters
<a name="API_ListApplicationOperations_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_ListApplicationOperations_RequestSyntax) **   <a name="APIReference-ListApplicationOperations-request-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Limit](#API_ListApplicationOperations_RequestSyntax) **   <a name="APIReference-ListApplicationOperations-request-Limit"></a>
The limit on the number of records to be returned in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListApplicationOperations_RequestSyntax) **   <a name="APIReference-ListApplicationOperations-request-NextToken"></a>
A pagination token that can be used in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [Operation](#API_ListApplicationOperations_RequestSyntax) **   <a name="APIReference-ListApplicationOperations-request-Operation"></a>
The type of operation that is performed on an application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [OperationStatus](#API_ListApplicationOperations_RequestSyntax) **   <a name="APIReference-ListApplicationOperations-request-OperationStatus"></a>
The status of the operation.
Type: String
Valid Values: `IN_PROGRESS | CANCELLED | SUCCESSFUL | FAILED`
Required: No

## Response Syntax
<a name="API_ListApplicationOperations_ResponseSyntax"></a>

```
{
   "ApplicationOperationInfoList": [
      {
         "EndTime": number,
         "Operation": "string",
         "OperationId": "string",
         "OperationStatus": "string",
         "StartTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListApplicationOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationOperationInfoList](#API_ListApplicationOperations_ResponseSyntax) **   <a name="APIReference-ListApplicationOperations-response-ApplicationOperationInfoList"></a>
A list of `ApplicationOperationInfo` objects that are associated with an application.
Type: Array of [ApplicationOperationInfo](API_ApplicationOperationInfo.md) objects

 ** [NextToken](#API_ListApplicationOperations_ResponseSyntax) **   <a name="APIReference-ListApplicationOperations-response-NextToken"></a>
A pagination token that can be used in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

## Errors
<a name="API_ListApplicationOperations_Errors"></a>

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_ListApplicationOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/ListApplicationOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/ListApplicationOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ListApplicationOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/ListApplicationOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ListApplicationOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/ListApplicationOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/ListApplicationOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/ListApplicationOperations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/ListApplicationOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ListApplicationOperations)
