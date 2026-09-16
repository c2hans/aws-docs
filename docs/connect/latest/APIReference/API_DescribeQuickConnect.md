---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeQuickConnect.html
---

# DescribeQuickConnect
<a name="API_DescribeQuickConnect"></a>

Describes the quick connect.

## Request Syntax
<a name="API_DescribeQuickConnect_RequestSyntax"></a>

```
GET /quick-connects/{{InstanceId}}/{{QuickConnectId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeQuickConnect_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DescribeQuickConnect_RequestSyntax) **   <a name="connect-DescribeQuickConnect-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [QuickConnectId](#API_DescribeQuickConnect_RequestSyntax) **   <a name="connect-DescribeQuickConnect-request-uri-QuickConnectId"></a>
The identifier for the quick connect.
Required: Yes

## Request Body
<a name="API_DescribeQuickConnect_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeQuickConnect_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "QuickConnect": {
      "Description": "string",
      "LastModifiedRegion": "string",
      "LastModifiedTime": number,
      "Name": "string",
      "QuickConnectARN": "string",
      "QuickConnectConfig": {
         "FlowConfig": {
            "ContactFlowId": "string"
         },
         "PhoneConfig": {
            "PhoneNumber": "string"
         },
         "QueueConfig": {
            "ContactFlowId": "string",
            "QueueId": "string"
         },
         "QuickConnectType": "string",
         "UserConfig": {
            "ContactFlowId": "string",
            "UserId": "string"
         }
      },
      "QuickConnectId": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeQuickConnect_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QuickConnect](#API_DescribeQuickConnect_ResponseSyntax) **   <a name="connect-DescribeQuickConnect-response-QuickConnect"></a>
Information about the quick connect.
Type: [QuickConnect](API_QuickConnect.md) object

## Errors
<a name="API_DescribeQuickConnect_Errors"></a>

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
<a name="API_DescribeQuickConnect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeQuickConnect)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeQuickConnect)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeQuickConnect)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeQuickConnect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeQuickConnect)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeQuickConnect)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeQuickConnect)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeQuickConnect)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeQuickConnect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeQuickConnect)
