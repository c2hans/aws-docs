---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeKey.html
---

# DescribeKey
<a name="API_DescribeKey"></a>

Retrieves the API key resource details.

For more information, see [Use API keys to authenticate](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_DescribeKey_RequestSyntax"></a>

```
GET /metadata/v0/keys/{{KeyName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [KeyName](#API_DescribeKey_RequestSyntax) **   <a name="location-DescribeKey-request-uri-KeyName"></a>
The name of the API key resource.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_DescribeKey_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateTime": "string",
   "Description": "string",
   "ExpireTime": "string",
   "Key": "string",
   "KeyArn": "string",
   "KeyName": "string",
   "Restrictions": {
      "AllowActions": [ "string" ],
      "AllowAndroidApps": [
         {
            "CertificateFingerprint": "string",
            "Package": "string"
         }
      ],
      "AllowAppleApps": [
         {
            "BundleId": "string"
         }
      ],
      "AllowReferers": [ "string" ],
      "AllowResources": [ "string" ]
   },
   "Tags": {
      "string" : "string"
   },
   "UpdateTime": "string"
}
```

## Response Elements
<a name="API_DescribeKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateTime](#API_DescribeKey_ResponseSyntax) **   <a name="location-DescribeKey-response-CreateTime"></a>
The timestamp for when the API key resource was created in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

 ** [Description](#API_DescribeKey_ResponseSyntax) **   <a name="location-DescribeKey-response-Description"></a>
The optional description for the API key resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [ExpireTime](#API_DescribeKey_ResponseSyntax) **   <a name="location-DescribeKey-response-ExpireTime"></a>
The timestamp for when the API key resource will expire in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

 ** [Key](#API_DescribeKey_ResponseSyntax) **   <a name="location-DescribeKey-response-Key"></a>
The key value/string of an API key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [KeyArn](#API_DescribeKey_ResponseSyntax) **   <a name="location-DescribeKey-response-KeyArn"></a>
The Amazon Resource Name (ARN) for the API key resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:key/ExampleKey`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [KeyName](#API_DescribeKey_ResponseSyntax) **   <a name="location-DescribeKey-response-KeyName"></a>
The name of the API key resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [Restrictions](#API_DescribeKey_ResponseSyntax) **   <a name="location-DescribeKey-response-Restrictions"></a>
API Restrictions on the allowed actions, resources, and referers for an API key resource.
Type: [ApiKeyRestrictions](API_ApiKeyRestrictions.md) object

 ** [Tags](#API_DescribeKey_ResponseSyntax) **   <a name="location-DescribeKey-response-Tags"></a>
Tags associated with the API key resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`

 ** [UpdateTime](#API_DescribeKey_ResponseSyntax) **   <a name="location-DescribeKey-response-UpdateTime"></a>
The timestamp for when the API key resource was last updated in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

## Errors
<a name="API_DescribeKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource that you've entered was not found in your AWS account.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** FieldList **
The field where the invalid entry was detected.
 ** Reason **
A message with the reason for the validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_DescribeKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/DescribeKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/DescribeKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/DescribeKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/DescribeKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/DescribeKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/DescribeKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/DescribeKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/DescribeKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/DescribeKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/DescribeKey)
