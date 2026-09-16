---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchDisassociateAnalyticsDataSet.html
---

# BatchDisassociateAnalyticsDataSet
<a name="API_BatchDisassociateAnalyticsDataSet"></a>

Removes a list of analytics datasets associated with a given Connect Customer instance. You can disassociate multiple datasets in a single call.

## Request Syntax
<a name="API_BatchDisassociateAnalyticsDataSet_RequestSyntax"></a>

```
POST /analytics-data/instance/{{InstanceId}}/associations HTTP/1.1
Content-type: application/json

{
   "DataSetIds": [ "{{string}}" ],
   "TargetAccountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchDisassociateAnalyticsDataSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_BatchDisassociateAnalyticsDataSet_RequestSyntax) **   <a name="connect-BatchDisassociateAnalyticsDataSet-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_BatchDisassociateAnalyticsDataSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataSetIds](#API_BatchDisassociateAnalyticsDataSet_RequestSyntax) **   <a name="connect-BatchDisassociateAnalyticsDataSet-request-DataSetIds"></a>
An array of associated dataset identifiers to remove.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [TargetAccountId](#API_BatchDisassociateAnalyticsDataSet_RequestSyntax) **   <a name="connect-BatchDisassociateAnalyticsDataSet-request-TargetAccountId"></a>
The identifier of the target account. Use to disassociate a dataset from a different account than the one containing the Connect Customer instance. If not specified, by default this value is the AWS account that has the Connect Customer instance.
Type: String
Required: No

## Response Syntax
<a name="API_BatchDisassociateAnalyticsDataSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Deleted": [ "string" ],
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDisassociateAnalyticsDataSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Deleted](#API_BatchDisassociateAnalyticsDataSet_ResponseSyntax) **   <a name="connect-BatchDisassociateAnalyticsDataSet-response-Deleted"></a>
An array of successfully disassociated dataset identifiers.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Errors](#API_BatchDisassociateAnalyticsDataSet_ResponseSyntax) **   <a name="connect-BatchDisassociateAnalyticsDataSet-response-Errors"></a>
A list of errors for any datasets not successfully removed.
Type: Array of [ErrorResult](API_ErrorResult.md) objects

## Errors
<a name="API_BatchDisassociateAnalyticsDataSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_BatchDisassociateAnalyticsDataSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/BatchDisassociateAnalyticsDataSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/BatchDisassociateAnalyticsDataSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/BatchDisassociateAnalyticsDataSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/BatchDisassociateAnalyticsDataSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/BatchDisassociateAnalyticsDataSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/BatchDisassociateAnalyticsDataSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/BatchDisassociateAnalyticsDataSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/BatchDisassociateAnalyticsDataSet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/BatchDisassociateAnalyticsDataSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/BatchDisassociateAnalyticsDataSet)
