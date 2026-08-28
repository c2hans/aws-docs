---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateKey.html
---

# UpdateKey
<a name="API_UpdateKey"></a>

Updates the specified properties of a given API key resource.

## Request Syntax
<a name="API_UpdateKey_RequestSyntax"></a>

```
PATCH /metadata/v0/keys/{{KeyName}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "ExpireTime": "{{string}}",
   "ForceUpdate": {{boolean}},
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
   }
}
```

## URI Request Parameters
<a name="API_UpdateKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [KeyName](#API_UpdateKey_RequestSyntax) **   <a name="location-UpdateKey-request-uri-KeyName"></a>
The name of the API key resource to update.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_UpdateKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateKey_RequestSyntax) **   <a name="location-UpdateKey-request-Description"></a>
Updates the description for the API key resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [ExpireTime](#API_UpdateKey_RequestSyntax) **   <a name="location-UpdateKey-request-ExpireTime"></a>
Updates the timestamp for when the API key resource will expire in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: No

 ** [ForceUpdate](#API_UpdateKey_RequestSyntax) **   <a name="location-UpdateKey-request-ForceUpdate"></a>
The boolean flag to be included for updating `ExpireTime` or `Restrictions` details.
Must be set to `true` to update an API key resource that has been used in the past 7 days.
 `False` if force update is not preferred
Default value: `False`
Type: Boolean
Required: No

 ** [NoExpiry](#API_UpdateKey_RequestSyntax) **   <a name="location-UpdateKey-request-NoExpiry"></a>
Whether the API key should expire. Set to `true` to set the API key to have no expiration time.
Type: Boolean
Required: No

 ** [Restrictions](#API_UpdateKey_RequestSyntax) **   <a name="location-UpdateKey-request-Restrictions"></a>
Updates the API key restrictions for the API key resource.
Type: [ApiKeyRestrictions](API_ApiKeyRestrictions.md) object
Required: No

## Response Syntax
<a name="API_UpdateKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "KeyArn": "string",
   "KeyName": "string",
   "UpdateTime": "string"
}
```

## Response Elements
<a name="API_UpdateKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyArn](#API_UpdateKey_ResponseSyntax) **   <a name="location-UpdateKey-response-KeyArn"></a>
The Amazon Resource Name (ARN) for the API key resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:key/ExampleKey`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [KeyName](#API_UpdateKey_ResponseSyntax) **   <a name="location-UpdateKey-response-KeyName"></a>
The name of the API key resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [UpdateTime](#API_UpdateKey_ResponseSyntax) **   <a name="location-UpdateKey-response-UpdateTime"></a>
The timestamp for when the API key resource was last updated in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

## Errors
<a name="API_UpdateKey_Errors"></a>

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
<a name="API_UpdateKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/UpdateKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/UpdateKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/UpdateKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/UpdateKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/UpdateKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/UpdateKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/UpdateKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/UpdateKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/UpdateKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/UpdateKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
