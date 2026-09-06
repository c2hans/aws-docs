---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeEmailAddress.html
---

# DescribeEmailAddress
<a name="API_DescribeEmailAddress"></a>

Describe email address form the specified Connect Customer instance.

## Request Syntax
<a name="API_DescribeEmailAddress_RequestSyntax"></a>

```
GET /email-addresses/{{InstanceId}}/{{EmailAddressId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeEmailAddress_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailAddressId](#API_DescribeEmailAddress_RequestSyntax) **   <a name="connect-DescribeEmailAddress-request-uri-EmailAddressId"></a>
The identifier of the email address.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [InstanceId](#API_DescribeEmailAddress_RequestSyntax) **   <a name="connect-DescribeEmailAddress-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeEmailAddress_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeEmailAddress_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AliasConfigurations": [
      {
         "EmailAddressId": "string"
      }
   ],
   "CreateTimestamp": "string",
   "Description": "string",
   "DisplayName": "string",
   "EmailAddress": "string",
   "EmailAddressArn": "string",
   "EmailAddressId": "string",
   "ModifiedTimestamp": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_DescribeEmailAddress_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AliasConfigurations](#API_DescribeEmailAddress_ResponseSyntax) **   <a name="connect-DescribeEmailAddress-response-AliasConfigurations"></a>
A list of alias configurations associated with this email address. Contains details about email addresses that forward to this primary email address. The list can contain at most one alias configuration per email address.
Type: Array of [AliasConfiguration](API_AliasConfiguration.md) objects
Array Members: Maximum number of 1 item.

 ** [CreateTimestamp](#API_DescribeEmailAddress_ResponseSyntax) **   <a name="connect-DescribeEmailAddress-response-CreateTimestamp"></a>
The email address creation timestamp in ISO 8601 Datetime.
Type: String

 ** [Description](#API_DescribeEmailAddress_ResponseSyntax) **   <a name="connect-DescribeEmailAddress-response-Description"></a>
The description of the email address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [DisplayName](#API_DescribeEmailAddress_ResponseSyntax) **   <a name="connect-DescribeEmailAddress-response-DisplayName"></a>
The display name of email address
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [EmailAddress](#API_DescribeEmailAddress_ResponseSyntax) **   <a name="connect-DescribeEmailAddress-response-EmailAddress"></a>
The email address, including the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^\s@]+@[^\s@]+\.[^\s@]+`

 ** [EmailAddressArn](#API_DescribeEmailAddress_ResponseSyntax) **   <a name="connect-DescribeEmailAddress-response-EmailAddressArn"></a>
The Amazon Resource Name (ARN) of the email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [EmailAddressId](#API_DescribeEmailAddress_ResponseSyntax) **   <a name="connect-DescribeEmailAddress-response-EmailAddressId"></a>
The identifier of the email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [ModifiedTimestamp](#API_DescribeEmailAddress_ResponseSyntax) **   <a name="connect-DescribeEmailAddress-response-ModifiedTimestamp"></a>
The email address last modification timestamp in ISO 8601 Datetime.
Type: String

 ** [Tags](#API_DescribeEmailAddress_ResponseSyntax) **   <a name="connect-DescribeEmailAddress-response-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_DescribeEmailAddress_Errors"></a>

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
<a name="API_DescribeEmailAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeEmailAddress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeEmailAddress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeEmailAddress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeEmailAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeEmailAddress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeEmailAddress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeEmailAddress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeEmailAddress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeEmailAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeEmailAddress)
