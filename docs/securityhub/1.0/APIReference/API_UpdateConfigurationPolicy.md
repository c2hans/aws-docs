---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateConfigurationPolicy.html
---

# UpdateConfigurationPolicy
<a name="API_UpdateConfigurationPolicy"></a>

 Updates a configuration policy. Only the AWS Security Hub CSPM delegated administrator can invoke this operation from the home Region.

## Request Syntax
<a name="API_UpdateConfigurationPolicy_RequestSyntax"></a>

```
PATCH /configurationPolicy/{{Identifier}} HTTP/1.1
Content-type: application/json

{
   "ConfigurationPolicy": { ... },
   "Description": "{{string}}",
   "Name": "{{string}}",
   "UpdatedReason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateConfigurationPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_UpdateConfigurationPolicy_RequestSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-request-uri-Identifier"></a>
 The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_UpdateConfigurationPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationPolicy](#API_UpdateConfigurationPolicy_RequestSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-request-ConfigurationPolicy"></a>
 An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls).
When updating a configuration policy, provide a complete list of standards that you want to enable and a complete list of controls that you want to enable or disable. The updated configuration replaces the current configuration.
Type: [Policy](API_Policy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [Description](#API_UpdateConfigurationPolicy_RequestSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-request-Description"></a>
 The description of the configuration policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [Name](#API_UpdateConfigurationPolicy_RequestSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-request-Name"></a>
 The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: `-, ., !, *, /`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [UpdatedReason](#API_UpdateConfigurationPolicy_RequestSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-request-UpdatedReason"></a>
 The reason for updating the configuration policy.
Type: String
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_UpdateConfigurationPolicy_ResponseSyntax"></a>

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
<a name="API_UpdateConfigurationPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-response-Arn"></a>
 The ARN of the configuration policy.
Type: String
Pattern: `.*\S.*`

 ** [ConfigurationPolicy](#API_UpdateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-response-ConfigurationPolicy"></a>
 An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If the request included a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If the request included a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls).
Type: [Policy](API_Policy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [CreatedAt](#API_UpdateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-response-CreatedAt"></a>
 The date and time, in UTC and ISO 8601 format, that the configuration policy was created.
Type: Timestamp

 ** [Description](#API_UpdateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-response-Description"></a>
 The description of the configuration policy.
Type: String
Pattern: `.*\S.*`

 ** [Id](#API_UpdateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-response-Id"></a>
 The UUID of the configuration policy.
Type: String
Pattern: `.*\S.*`

 ** [Name](#API_UpdateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-response-Name"></a>
 The name of the configuration policy.
Type: String
Pattern: `.*\S.*`

 ** [UpdatedAt](#API_UpdateConfigurationPolicy_ResponseSyntax) **   <a name="securityhub-UpdateConfigurationPolicy-response-UpdatedAt"></a>
 The date and time, in UTC and ISO 8601 format, that the configuration policy was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateConfigurationPolicy_Errors"></a>

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

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_UpdateConfigurationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/UpdateConfigurationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/UpdateConfigurationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UpdateConfigurationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/UpdateConfigurationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UpdateConfigurationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/UpdateConfigurationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/UpdateConfigurationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/UpdateConfigurationPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/UpdateConfigurationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UpdateConfigurationPolicy)
