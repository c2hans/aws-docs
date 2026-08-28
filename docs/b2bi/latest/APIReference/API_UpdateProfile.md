---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UpdateProfile.html
---

# UpdateProfile
<a name="API_UpdateProfile"></a>

Updates the specified parameters for a profile. A profile is the mechanism used to create the concept of a private network.

## Request Syntax
<a name="API_UpdateProfile_RequestSyntax"></a>

```
{
   "businessName": "{{string}}",
   "email": "{{string}}",
   "name": "{{string}}",
   "phone": "{{string}}",
   "profileId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [businessName](#API_UpdateProfile_RequestSyntax) **   <a name="b2bi-UpdateProfile-request-businessName"></a>
Specifies the name for the business associated with this profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Required: No

 ** [email](#API_UpdateProfile_RequestSyntax) **   <a name="b2bi-UpdateProfile-request-email"></a>
Specifies the email address associated with this customer profile.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 254.
Pattern: `[\w\.\-]+@[\w\.\-]+`
Required: No

 ** [name](#API_UpdateProfile_RequestSyntax) **   <a name="b2bi-UpdateProfile-request-name"></a>
The name of the profile, used to identify it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Required: No

 ** [phone](#API_UpdateProfile_RequestSyntax) **   <a name="b2bi-UpdateProfile-request-phone"></a>
Specifies the phone number associated with the profile.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 22.
Pattern: `\+?([0-9 \t\-()\/]{7,})(?:\s*(?:#|x\.?|ext\.?|extension) \t*(\d+))?`
Required: No

 ** [profileId](#API_UpdateProfile_RequestSyntax) **   <a name="b2bi-UpdateProfile-request-profileId"></a>
Specifies the unique, system-generated identifier for the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Response Syntax
<a name="API_UpdateProfile_ResponseSyntax"></a>

```
{
   "businessName": "string",
   "createdAt": "string",
   "email": "string",
   "logging": "string",
   "logGroupName": "string",
   "modifiedAt": "string",
   "name": "string",
   "phone": "string",
   "profileArn": "string",
   "profileId": "string"
}
```

## Response Elements
<a name="API_UpdateProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [businessName](#API_UpdateProfile_ResponseSyntax) **   <a name="b2bi-UpdateProfile-response-businessName"></a>
Returns the name for the business associated with this profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.

 ** [createdAt](#API_UpdateProfile_ResponseSyntax) **   <a name="b2bi-UpdateProfile-response-createdAt"></a>
Returns a timestamp for creation date and time of the profile.
Type: Timestamp

 ** [email](#API_UpdateProfile_ResponseSyntax) **   <a name="b2bi-UpdateProfile-response-email"></a>
Returns the email address associated with this customer profile.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 254.
Pattern: `[\w\.\-]+@[\w\.\-]+`

 ** [logging](#API_UpdateProfile_ResponseSyntax) **   <a name="b2bi-UpdateProfile-response-logging"></a>
Specifies whether or not logging is enabled for this profile.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [logGroupName](#API_UpdateProfile_ResponseSyntax) **   <a name="b2bi-UpdateProfile-response-logGroupName"></a>
Returns the name of the logging group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [modifiedAt](#API_UpdateProfile_ResponseSyntax) **   <a name="b2bi-UpdateProfile-response-modifiedAt"></a>
Returns a timestamp for last time the profile was modified.
Type: Timestamp

 ** [name](#API_UpdateProfile_ResponseSyntax) **   <a name="b2bi-UpdateProfile-response-name"></a>
Returns the name of the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.

 ** [phone](#API_UpdateProfile_ResponseSyntax) **   <a name="b2bi-UpdateProfile-response-phone"></a>
Returns the phone number associated with the profile.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 22.
Pattern: `\+?([0-9 \t\-()\/]{7,})(?:\s*(?:#|x\.?|ext\.?|extension) \t*(\d+))?`

 ** [profileArn](#API_UpdateProfile_ResponseSyntax) **   <a name="b2bi-UpdateProfile-response-profileArn"></a>
Returns an Amazon Resource Name (ARN) for the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [profileId](#API_UpdateProfile_ResponseSyntax) **   <a name="b2bi-UpdateProfile-response-profileId"></a>
Returns the unique, system-generated identifier for the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_UpdateProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.
HTTP Status Code: 400

 ** InternalServerException **
This exception is thrown when an error occurs in the AWS B2B Data Interchange service.
 ** retryAfterSeconds **
The server attempts to retry a failed command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.
 ** quotaCode **
The quota that was exceeded, which caused the exception.
 ** resourceId **
The ID for the resource that exceeded the quota, which caused the exception.
 ** resourceType **
The resource type (profile, partnership, transformer, or capability) that exceeded the quota, which caused the exception.
 ** serviceCode **
The code responsible for exceeding the quota, which caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.
 ** retryAfterSeconds **
The server attempts to retry a command that was throttled.
HTTP Status Code: 400

 ** ValidationException **
When you use Transformer APIs, `TestConversion`, or `TestParsing`, the service throws a validation exception if a rule is configured incorrectly. For example, a validation exception occurs when:
+ A rule references an element that doesn't exist in the selected transaction set
+ An element length rule specifies a minimum length less than 0
If your custom validation rules are configured correctly but the EDI validation fails due to those rules, this is expected behavior and doesn't result in a `ValidationException`.
For all other API operations, a validation exception occurs when a Trading Partner object can't be validated against a request from another object. This can happen during:
+ Standard EDI validation
+ Custom validation rule evaluation, such as when:
  + Element lengths don't meet specified constraints
  + Code list validations contain invalid codes
  + Required elements are missing based on your element requirement rules
HTTP Status Code: 400

## Examples
<a name="API_UpdateProfile_Examples"></a>

### Example
<a name="API_UpdateProfile_Example_1"></a>

The following example updates a profile.

#### Sample Request
<a name="API_UpdateProfile_Example_1_Request"></a>

```
{
    "businessName": "John's Shipping",
    "email": "john@example.com",
    "name": "Shipping Profile",
    "phone": "5555555555",
    "profileId": "p-ABCDE111122223333"
}
```

#### Sample Response
<a name="API_UpdateProfile_Example_1_Response"></a>

```
{
    "businessName": "John's Trucking",
    "createdAt": "2023-11-01T21:51:05.504Z",
    "email": "john@example.com",
    "logging": "ENABLED",
    "logGroupName": "b2bi/p-ABCDE111122223333-Logs",
    "modifiedAt": "2023-11-02T21:51:05.504Z",
    "name": "Shipping Profile",
    "phone": "5555555555",
    "profileArn": "arn:aws:b2bi:us-west-2:123456789012:profile/p-ABCDE111122223333",
    "profileId": "p-ABCDE111122223333"
}
```

## See Also
<a name="API_UpdateProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/UpdateProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/UpdateProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/UpdateProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/UpdateProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/UpdateProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/UpdateProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/UpdateProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/UpdateProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/UpdateProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/UpdateProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
