---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplicationOperation.html
---

# DescribeApplicationOperation
<a name="API_DescribeApplicationOperation"></a>

Provides a detailed description of a specified application operation. To see a list of all the operations of an application, invoke the [ListApplicationOperations](API_ListApplicationOperations.md) operation.

**Note**
This operation is supported only for Managed Service for Apache Flink.

## Request Syntax
<a name="API_DescribeApplicationOperation_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "OperationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeApplicationOperation_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_DescribeApplicationOperation_RequestSyntax) **   <a name="APIReference-DescribeApplicationOperation-request-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [OperationId](#API_DescribeApplicationOperation_RequestSyntax) **   <a name="APIReference-DescribeApplicationOperation-request-OperationId"></a>
The operation ID of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_DescribeApplicationOperation_ResponseSyntax"></a>

```
{
   "ApplicationOperationInfoDetails": {
      "ApplicationVersionChangeDetails": {
         "ApplicationVersionUpdatedFrom": number,
         "ApplicationVersionUpdatedTo": number
      },
      "EndTime": number,
      "Operation": "string",
      "OperationFailureDetails": {
         "ErrorInfo": {
            "ErrorString": "string"
         },
         "RollbackOperationId": "string"
      },
      "OperationStatus": "string",
      "StartTime": number
   }
}
```

## Response Elements
<a name="API_DescribeApplicationOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationOperationInfoDetails](#API_DescribeApplicationOperation_ResponseSyntax) **   <a name="APIReference-DescribeApplicationOperation-response-ApplicationOperationInfoDetails"></a>
A description of the application operation that provides information about the updates that were made to the application.
Type: [ApplicationOperationInfoDetails](API_ApplicationOperationInfoDetails.md) object

## Errors
<a name="API_DescribeApplicationOperation_Errors"></a>

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
<a name="API_DescribeApplicationOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DescribeApplicationOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DescribeApplicationOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DescribeApplicationOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DescribeApplicationOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DescribeApplicationOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DescribeApplicationOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DescribeApplicationOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DescribeApplicationOperation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DescribeApplicationOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DescribeApplicationOperation)
