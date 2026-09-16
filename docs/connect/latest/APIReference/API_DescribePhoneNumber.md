---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html
---

# DescribePhoneNumber
<a name="API_DescribePhoneNumber"></a>

Gets details and status of a phone number that’s claimed to your Connect Customer instance or traffic distribution group.

**Important**
If the number is claimed to a traffic distribution group, and you are calling in the AWS Region where the traffic distribution group was created, you can use either a phone number ARN or UUID value for the `PhoneNumberId` URI request parameter. However, if the number is claimed to a traffic distribution group and you are calling this API in the alternate AWS Region associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you receive a `ResourceNotFoundException`.

## Request Syntax
<a name="API_DescribePhoneNumber_RequestSyntax"></a>

```
GET /phone-number/{{PhoneNumberId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribePhoneNumber_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PhoneNumberId](#API_DescribePhoneNumber_RequestSyntax) **   <a name="connect-DescribePhoneNumber-request-uri-PhoneNumberId"></a>
A unique identifier for the phone number.
Required: Yes

## Request Body
<a name="API_DescribePhoneNumber_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribePhoneNumber_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ClaimedPhoneNumberSummary": {
      "InstanceId": "string",
      "PhoneNumber": "string",
      "PhoneNumberArn": "string",
      "PhoneNumberCountryCode": "string",
      "PhoneNumberDescription": "string",
      "PhoneNumberId": "string",
      "PhoneNumberStatus": {
         "Message": "string",
         "Status": "string"
      },
      "PhoneNumberType": "string",
      "SourcePhoneNumberArn": "string",
      "Tags": {
         "string" : "string"
      },
      "TargetArn": "string"
   }
}
```

## Response Elements
<a name="API_DescribePhoneNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClaimedPhoneNumberSummary](#API_DescribePhoneNumber_ResponseSyntax) **   <a name="connect-DescribePhoneNumber-response-ClaimedPhoneNumberSummary"></a>
Information about a phone number that's been claimed to your Connect Customer instance or traffic distribution group.
Type: [ClaimedPhoneNumberSummary](API_ClaimedPhoneNumberSummary.md) object

## Errors
<a name="API_DescribePhoneNumber_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribePhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribePhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribePhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribePhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribePhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribePhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribePhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribePhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribePhoneNumber)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribePhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribePhoneNumber)
