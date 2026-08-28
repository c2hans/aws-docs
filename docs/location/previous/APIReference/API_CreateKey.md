---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_CreateKey.html
---

# CreateKey
<a name="API_CreateKey"></a>

Creates an API key resource in your AWS account, which lets you grant actions for Amazon Location resources to the API key bearer.

For more information, see [Use API keys to authenticate](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_CreateKey_RequestSyntax"></a>

```
POST /metadata/v0/keys HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "ExpireTime": "{{string}}",
   "KeyName": "{{string}}",
   "NoExpiry": {{boolean}},
   "Restrictions": {
      "AllowActions": [ "{{string}}" ],
      "AllowAndroidApps": [
         {
            "CertificateFingerprint": "{{string}}",
            "Package": "{{string}}"
         }
      ],
      "AllowAppleApps": [
         {
            "BundleId": "{{string}}"
         }
      ],
      "AllowReferers": [ "{{string}}" ],
      "AllowResources": [ "{{string}}" ]
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateKey_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateKey_RequestSyntax) **   <a name="location-CreateKey-request-Description"></a>
An optional description for the API key resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [ExpireTime](#API_CreateKey_RequestSyntax) **   <a name="location-CreateKey-request-ExpireTime"></a>
The optional timestamp for when the API key resource will expire in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`. One of `NoExpiry` or `ExpireTime` must be set.
Type: Timestamp
Required: No

 ** [KeyName](#API_CreateKey_RequestSyntax) **   <a name="location-CreateKey-request-KeyName"></a>
A custom name for the API key resource.
Requirements:
+ Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (\_).
+ Must be a unique API key name.
+ No spaces allowed. For example, `ExampleAPIKey`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [NoExpiry](#API_CreateKey_RequestSyntax) **   <a name="location-CreateKey-request-NoExpiry"></a>
Optionally set to `true` to set no expiration time for the API key. One of `NoExpiry` or `ExpireTime` must be set.
Type: Boolean
Required: No

 ** [Restrictions](#API_CreateKey_RequestSyntax) **   <a name="location-CreateKey-request-Restrictions"></a>
The API key restrictions for the API key resource.
Type: [ApiKeyRestrictions](API_ApiKeyRestrictions.md) object
Required: Yes

 ** [Tags](#API_CreateKey_RequestSyntax) **   <a name="location-CreateKey-request-Tags"></a>
Applies one or more tags to the map resource. A tag is a key-value pair that helps manage, identify, search, and filter your resources by labelling them.
Format: `"key" : "value"`
Restrictions:
+ Maximum 50 tags per resource
+ Each resource tag must be unique with a maximum of one value.
+ Maximum key length: 128 Unicode characters in UTF-8
+ Maximum value length: 256 Unicode characters in UTF-8
+ Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: \+ - = . \_ : / @.
+ Cannot use "aws:" as a prefix for a key.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_CreateKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateTime": "string",
   "Key": "string",
   "KeyArn": "string",
   "KeyName": "string"
}
```

## Response Elements
<a name="API_CreateKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateTime](#API_CreateKey_ResponseSyntax) **   <a name="location-CreateKey-response-CreateTime"></a>
The timestamp for when the API key resource was created in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

 ** [Key](#API_CreateKey_ResponseSyntax) **   <a name="location-CreateKey-response-Key"></a>
The key value/string of an API key. This value is used when making API calls to authorize the call. For example, see [GetMapGlyphs](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapGlyphs.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [KeyArn](#API_CreateKey_ResponseSyntax) **   <a name="location-CreateKey-response-KeyArn"></a>
The Amazon Resource Name (ARN) for the API key resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:key/ExampleKey`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [KeyName](#API_CreateKey_ResponseSyntax) **   <a name="location-CreateKey-response-KeyName"></a>
The name of the API key resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

## Errors
<a name="API_CreateKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** ConflictException **
The request was unsuccessful because of a conflict.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The operation was denied because the request would exceed the maximum [quota](https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html) set for Amazon Location Service.
 ** Message **
A message with the reason for the service quota exceeded exception error.
HTTP Status Code: 402

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
<a name="API_CreateKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/CreateKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/CreateKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/CreateKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/CreateKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/CreateKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/CreateKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/CreateKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/CreateKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/CreateKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/CreateKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
