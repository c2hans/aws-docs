---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateConfigurationPolicy.html
---

# CreateConfigurationPolicy
<a name="API_CreateConfigurationPolicy"></a>

 Creates a configuration policy with the defined configuration. Only the AWS Security Hub CSPM delegated administrator can invoke this operation from the home Region.

## Request Syntax
<a name="API_CreateConfigurationPolicy_RequestSyntax"></a>

```
POST /configurationPolicy/create HTTP/1.1
Content-type: application/json

{
   "ConfigurationPolicy": { ... },
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateConfigurationPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConfigurationPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationPolicy](#API_CreateConfigurationPolicy_RequestSyntax) **   <a name="securityhub-CreateConfigurationPolicy-request-ConfigurationPolicy"></a>
 An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls).
Type: [Policy](API_Policy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Description](#API_CreateConfigurationPolicy_RequestSyntax) **   <a name="securityhub-CreateConfigurationPolicy-request-Description"></a>
 The description of the configuration policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [Name](#API_CreateConfigurationPolicy_RequestSyntax) **   <a name="securityhub-CreateConfigurationPolicy-request-Name"></a>
 The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: `-, ., !, *, /`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [Tags](#API_CreateConfigurationPolicy_RequestSyntax) **   <a name="securityhub-CreateConfigurationPolicy-request-Tags"></a>
 User-defined tags associated with a configuration policy. For more information, see [Tagging AWS Security Hub CSPM resources](https://docs.aws.amazon.com/securityhub/latest/userguide/tagging-resources.html) in the *Security Hub CSPM user guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateConfigurationPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "ConfigurationPolicy": { ... },
   "CreatedAt": "string",
   "Description": "string",
   "Id": "string",
   "Name": "string",
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_CreateConfigurationPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-CreateConfigurationPolicy-response-Arn"></a>
 The Amazon Resource Name (ARN) of the configuration policy.
Type: String
Pattern: `.*\S.*`

 ** [ConfigurationPolicy](#API_CreateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-CreateConfigurationPolicy-response-ConfigurationPolicy"></a>
 An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If the request included a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If the request included a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls).
Type: [Policy](API_Policy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [CreatedAt](#API_CreateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-CreateConfigurationPolicy-response-CreatedAt"></a>
 The date and time, in UTC and ISO 8601 format, that the configuration policy was created.
Type: Timestamp

 ** [Description](#API_CreateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-CreateConfigurationPolicy-response-Description"></a>
 The description of the configuration policy.
Type: String
Pattern: `.*\S.*`

 ** [Id](#API_CreateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-CreateConfigurationPolicy-response-Id"></a>
 The universally unique identifier (UUID) of the configuration policy.
Type: String
Pattern: `.*\S.*`

 ** [Name](#API_CreateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-CreateConfigurationPolicy-response-Name"></a>
 The name of the configuration policy.
Type: String
Pattern: `.*\S.*`

 ** [UpdatedAt](#API_CreateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-CreateConfigurationPolicy-response-UpdatedAt"></a>
 The date and time, in UTC and ISO 8601 format, that the configuration policy was last updated.
Type: Timestamp

## Errors
<a name="API_CreateConfigurationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceConflictException **
The resource specified in the request conflicts with an existing resource.
HTTP Status Code: 409

## See Also
<a name="API_CreateConfigurationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/CreateConfigurationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/CreateConfigurationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CreateConfigurationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/CreateConfigurationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CreateConfigurationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/CreateConfigurationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/CreateConfigurationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/CreateConfigurationPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/CreateConfigurationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CreateConfigurationPolicy)
