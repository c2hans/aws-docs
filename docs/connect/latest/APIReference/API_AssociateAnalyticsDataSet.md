---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateAnalyticsDataSet.html
---

# AssociateAnalyticsDataSet
<a name="API_AssociateAnalyticsDataSet"></a>

Associates the specified dataset for a Connect Customer instance with the target account. You can associate only one dataset in a single call.

## Request Syntax
<a name="API_AssociateAnalyticsDataSet_RequestSyntax"></a>

```
PUT /analytics-data/instance/{{InstanceId}}/association HTTP/1.1
Content-type: application/json

{
   "DataSetId": "{{string}}",
   "TargetAccountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateAnalyticsDataSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_AssociateAnalyticsDataSet_RequestSyntax) **   <a name="connect-AssociateAnalyticsDataSet-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_AssociateAnalyticsDataSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataSetId](#API_AssociateAnalyticsDataSet_RequestSyntax) **   <a name="connect-AssociateAnalyticsDataSet-request-DataSetId"></a>
The identifier of the dataset to associate with the target account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [TargetAccountId](#API_AssociateAnalyticsDataSet_RequestSyntax) **   <a name="connect-AssociateAnalyticsDataSet-request-TargetAccountId"></a>
The identifier of the target account. Use to associate a dataset to a different account than the one containing the Connect Customer instance. If not specified, by default this value is the AWS account that has the Connect Customer instance.
Type: String
Required: No

## Response Syntax
<a name="API_AssociateAnalyticsDataSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataSetId": "string",
   "ResourceShareArn": "string",
   "ResourceShareId": "string",
   "TargetAccountId": "string"
}
```

## Response Elements
<a name="API_AssociateAnalyticsDataSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataSetId](#API_AssociateAnalyticsDataSet_ResponseSyntax) **   <a name="connect-AssociateAnalyticsDataSet-response-DataSetId"></a>
The identifier of the dataset that was associated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [ResourceShareArn](#API_AssociateAnalyticsDataSet_ResponseSyntax) **   <a name="connect-AssociateAnalyticsDataSet-response-ResourceShareArn"></a>
The Amazon Resource Name (ARN) of the AWS Resource Access Manager share.
Type: String

 ** [ResourceShareId](#API_AssociateAnalyticsDataSet_ResponseSyntax) **   <a name="connect-AssociateAnalyticsDataSet-response-ResourceShareId"></a>
The AWS Resource Access Manager share ID that is generated.
Type: String

 ** [TargetAccountId](#API_AssociateAnalyticsDataSet_ResponseSyntax) **   <a name="connect-AssociateAnalyticsDataSet-response-TargetAccountId"></a>
The identifier of the target account.
Type: String

## Errors
<a name="API_AssociateAnalyticsDataSet_Errors"></a>

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
<a name="API_AssociateAnalyticsDataSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/AssociateAnalyticsDataSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/AssociateAnalyticsDataSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociateAnalyticsDataSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/AssociateAnalyticsDataSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociateAnalyticsDataSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/AssociateAnalyticsDataSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/AssociateAnalyticsDataSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/AssociateAnalyticsDataSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/AssociateAnalyticsDataSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociateAnalyticsDataSet)
