---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoapikeys_DescribeKey.html
---

# DescribeKey
<a name="API_geoapikeys_DescribeKey"></a>

Retrieves the API key resource details.

For more information, see [Use API keys to authenticate](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geoapikeys_DescribeKey_RequestSyntax"></a>

```
GET /metadata/v0/keys/{{KeyName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geoapikeys_DescribeKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [KeyName](#API_geoapikeys_DescribeKey_RequestSyntax) **   <a name="location-geoapikeys_DescribeKey-request-uri-KeyName"></a>
The name of the API key resource.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_geoapikeys_DescribeKey_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geoapikeys_DescribeKey_ResponseSyntax"></a>

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
<a name="API_geoapikeys_DescribeKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateTime](#API_geoapikeys_DescribeKey_ResponseSyntax) **   <a name="location-geoapikeys_DescribeKey-response-CreateTime"></a>
The timestamp for when the API key resource was created in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp

 ** [Description](#API_geoapikeys_DescribeKey_ResponseSyntax) **   <a name="location-geoapikeys_DescribeKey-response-Description"></a>
The optional description for the API key resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [ExpireTime](#API_geoapikeys_DescribeKey_ResponseSyntax) **   <a name="location-geoapikeys_DescribeKey-response-ExpireTime"></a>
The timestamp for when the API key resource will expire in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp

 ** [Key](#API_geoapikeys_DescribeKey_ResponseSyntax) **   <a name="location-geoapikeys_DescribeKey-response-Key"></a>
The key value/string of an API key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [KeyArn](#API_geoapikeys_DescribeKey_ResponseSyntax) **   <a name="location-geoapikeys_DescribeKey-response-KeyArn"></a>
The Amazon Resource Name (ARN) for the API key resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:key/ExampleKey`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [KeyName](#API_geoapikeys_DescribeKey_ResponseSyntax) **   <a name="location-geoapikeys_DescribeKey-response-KeyName"></a>
The name of the API key resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [Restrictions](#API_geoapikeys_DescribeKey_ResponseSyntax) **   <a name="location-geoapikeys_DescribeKey-response-Restrictions"></a>
API Restrictions on the allowed actions, resources, referers, Android apps, and Apple apps for an API key resource.
Type: [ApiKeyRestrictions](API_geoapikeys_ApiKeyRestrictions.md) object

 ** [Tags](#API_geoapikeys_DescribeKey_ResponseSyntax) **   <a name="location-geoapikeys_DescribeKey-response-Tags"></a>
Tags associated with the API key resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`

 ** [UpdateTime](#API_geoapikeys_DescribeKey_ResponseSyntax) **   <a name="location-geoapikeys_DescribeKey-response-UpdateTime"></a>
The timestamp for when the API key resource was last updated in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp

## Errors
<a name="API_geoapikeys_DescribeKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A resource associated with the request could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_geoapikeys_DescribeKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geoapikeys-2020-11-19/DescribeKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geoapikeys-2020-11-19/DescribeKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geoapikeys-2020-11-19/DescribeKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geoapikeys-2020-11-19/DescribeKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geoapikeys-2020-11-19/DescribeKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geoapikeys-2020-11-19/DescribeKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geoapikeys-2020-11-19/DescribeKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geoapikeys-2020-11-19/DescribeKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geoapikeys-2020-11-19/DescribeKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geoapikeys-2020-11-19/DescribeKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
