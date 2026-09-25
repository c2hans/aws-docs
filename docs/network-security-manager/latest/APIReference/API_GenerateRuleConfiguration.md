---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_GenerateRuleConfiguration.html
---

# GenerateRuleConfiguration
<a name="API_GenerateRuleConfiguration"></a>

Generates a rule configuration from a natural-language description. Provide a prompt along with the rule's firewall type and rule type. The service returns a configuration that you can use when you create or update a rule. If you also provide an existing configuration, the service edits that configuration instead of generating a new one.

## Request Syntax
<a name="API_GenerateRuleConfiguration_RequestSyntax"></a>

```
POST /GenerateRuleConfiguration HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "currentConfiguration": "{{string}}",
   "prompt": "{{string}}",
   "ruleFirewallType": "{{string}}",
   "ruleType": "{{string}}",
   "wafConfigDataType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GenerateRuleConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GenerateRuleConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_GenerateRuleConfiguration_RequestSyntax) **   <a name="networksecuritymanager-GenerateRuleConfiguration-request-clientToken"></a>
A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [currentConfiguration](#API_GenerateRuleConfiguration_RequestSyntax) **   <a name="networksecuritymanager-GenerateRuleConfiguration-request-currentConfiguration"></a>
An existing configuration to edit, as a JSON string. When you provide this value, the operation edits the configuration. When you omit it, the operation generates a new configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Required: No

 ** [prompt](#API_GenerateRuleConfiguration_RequestSyntax) **   <a name="networksecuritymanager-GenerateRuleConfiguration-request-prompt"></a>
A natural-language description of the configuration that you want to generate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `[A-Za-z0-9.,?!@&:;()'"\s\-\/\n_=<>+*\#\[\]{}]*`
Required: Yes

 ** [ruleFirewallType](#API_GenerateRuleConfiguration_RequestSyntax) **   <a name="networksecuritymanager-GenerateRuleConfiguration-request-ruleFirewallType"></a>
The firewall type of the rule.
Type: String
Valid Values: `WAF`
Required: Yes

 ** [ruleType](#API_GenerateRuleConfiguration_RequestSyntax) **   <a name="networksecuritymanager-GenerateRuleConfiguration-request-ruleType"></a>
The type of the rule. `CONFIGURATION` rules contain firewall settings, and `INSPECTION` rules contain rule groups.
Type: String
Valid Values: `CONFIGURATION | INSPECTION`
Required: Yes

 ** [wafConfigDataType](#API_GenerateRuleConfiguration_RequestSyntax) **   <a name="networksecuritymanager-GenerateRuleConfiguration-request-wafConfigDataType"></a>
For AWS WAF configuration rules, the specific AWS WAF configuration variant to generate. This is optional; if you omit it, the service selects the variant.
Type: String
Valid Values: `DefaultAction | VisibilityConfig | CaptchaConfig | ChallengeConfig | CustomResponseBodies | LoggingConfiguration | DataProtectionConfig | AssociationConfig | OnSourceDDoSProtectionConfig | TokenDomains`
Required: No

## Response Syntax
<a name="API_GenerateRuleConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": "string",
   "description": "string"
}
```

## Response Elements
<a name="API_GenerateRuleConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_GenerateRuleConfiguration_ResponseSyntax) **   <a name="networksecuritymanager-GenerateRuleConfiguration-response-configuration"></a>
The generated configuration, as a JSON string. You can use this value in the `configuration` field of a rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.

 ** [description](#API_GenerateRuleConfiguration_ResponseSyntax) **   <a name="networksecuritymanager-GenerateRuleConfiguration-response-description"></a>
Reserved for a future human-readable description of the generated configuration. This field is currently not populated.
Type: String

## Errors
<a name="API_GenerateRuleConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing failed because of an internal error in the service. This is a retryable error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because of request throttling. Reduce your request rate and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation. For details, see the `reason` and `fieldList` members of the response.
 ** fieldList **
The list of request fields that failed validation, if any.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GenerateRuleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-security-manager-2025-10-30/GenerateRuleConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-security-manager-2025-10-30/GenerateRuleConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/GenerateRuleConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-security-manager-2025-10-30/GenerateRuleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/GenerateRuleConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-security-manager-2025-10-30/GenerateRuleConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-security-manager-2025-10-30/GenerateRuleConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-security-manager-2025-10-30/GenerateRuleConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-security-manager-2025-10-30/GenerateRuleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/GenerateRuleConfiguration)
