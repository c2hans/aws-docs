---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateLicenseAssetRuleset.html
---

# UpdateLicenseAssetRuleset
<a name="API_UpdateLicenseAssetRuleset"></a>

Updates a license asset ruleset.

## Request Syntax
<a name="API_UpdateLicenseAssetRuleset_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "LicenseAssetRulesetArn": "{{string}}",
   "Name": "{{string}}",
   "Rules": [
      {
         "RuleStatement": {
            "InstanceRuleStatement": {
               "AndRuleStatement": {
                  "MatchingRuleStatements": [
                     {
                        "Constraint": "{{string}}",
                        "KeyToMatch": "{{string}}",
                        "ValueToMatch": [ "{{string}}" ]
                     }
                  ],
                  "ScriptRuleStatements": [
                     {
                        "KeyToMatch": "{{string}}",
                        "Script": "{{string}}"
                     }
                  ]
               },
               "MatchingRuleStatement": {
                  "Constraint": "{{string}}",
                  "KeyToMatch": "{{string}}",
                  "ValueToMatch": [ "{{string}}" ]
               },
               "OrRuleStatement": {
                  "MatchingRuleStatements": [
                     {
                        "Constraint": "{{string}}",
                        "KeyToMatch": "{{string}}",
                        "ValueToMatch": [ "{{string}}" ]
                     }
                  ],
                  "ScriptRuleStatements": [
                     {
                        "KeyToMatch": "{{string}}",
                        "Script": "{{string}}"
                     }
                  ]
               },
               "ScriptRuleStatement": {
                  "KeyToMatch": "{{string}}",
                  "Script": "{{string}}"
               }
            },
            "LicenseConfigurationRuleStatement": {
               "AndRuleStatement": {
                  "MatchingRuleStatements": [
                     {
                        "Constraint": "{{string}}",
                        "KeyToMatch": "{{string}}",
                        "ValueToMatch": [ "{{string}}" ]
                     }
                  ],
                  "ScriptRuleStatements": [
                     {
                        "KeyToMatch": "{{string}}",
                        "Script": "{{string}}"
                     }
                  ]
               },
               "MatchingRuleStatement": {
                  "Constraint": "{{string}}",
                  "KeyToMatch": "{{string}}",
                  "ValueToMatch": [ "{{string}}" ]
               },
               "OrRuleStatement": {
                  "MatchingRuleStatements": [
                     {
                        "Constraint": "{{string}}",
                        "KeyToMatch": "{{string}}",
                        "ValueToMatch": [ "{{string}}" ]
                     }
                  ],
                  "ScriptRuleStatements": [
                     {
                        "KeyToMatch": "{{string}}",
                        "Script": "{{string}}"
                     }
                  ]
               }
            },
            "LicenseRuleStatement": {
               "AndRuleStatement": {
                  "MatchingRuleStatements": [
                     {
                        "Constraint": "{{string}}",
                        "KeyToMatch": "{{string}}",
                        "ValueToMatch": [ "{{string}}" ]
                     }
                  ],
                  "ScriptRuleStatements": [
                     {
                        "KeyToMatch": "{{string}}",
                        "Script": "{{string}}"
                     }
                  ]
               },
               "MatchingRuleStatement": {
                  "Constraint": "{{string}}",
                  "KeyToMatch": "{{string}}",
                  "ValueToMatch": [ "{{string}}" ]
               },
               "OrRuleStatement": {
                  "MatchingRuleStatements": [
                     {
                        "Constraint": "{{string}}",
                        "KeyToMatch": "{{string}}",
                        "ValueToMatch": [ "{{string}}" ]
                     }
                  ],
                  "ScriptRuleStatements": [
                     {
                        "KeyToMatch": "{{string}}",
                        "Script": "{{string}}"
                     }
                  ]
               }
            }
         }
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateLicenseAssetRuleset_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateLicenseAssetRuleset_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetRuleset-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: Yes

 ** [Description](#API_UpdateLicenseAssetRuleset_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetRuleset-request-Description"></a>
License asset ruleset description.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [LicenseAssetRulesetArn](#API_UpdateLicenseAssetRuleset_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetRuleset-request-LicenseAssetRulesetArn"></a>
Amazon Resource Name (ARN) of the license asset ruleset.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [Name](#API_UpdateLicenseAssetRuleset_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetRuleset-request-Name"></a>
License asset ruleset name.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** [Rules](#API_UpdateLicenseAssetRuleset_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetRuleset-request-Rules"></a>
License asset rules.
Type: Array of [LicenseAssetRule](API_LicenseAssetRule.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdateLicenseAssetRuleset_ResponseSyntax"></a>

```
{
   "LicenseAssetRulesetArn": "string"
}
```

## Response Elements
<a name="API_UpdateLicenseAssetRuleset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseAssetRulesetArn](#API_UpdateLicenseAssetRuleset_ResponseSyntax) **   <a name="licensemanager-UpdateLicenseAssetRuleset-response-LicenseAssetRulesetArn"></a>
Amazon Resource Name (ARN) of the license asset ruleset.
Type: String

## Errors
<a name="API_UpdateLicenseAssetRuleset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameter values are not valid.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLicenseAssetRuleset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/UpdateLicenseAssetRuleset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/UpdateLicenseAssetRuleset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/UpdateLicenseAssetRuleset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/UpdateLicenseAssetRuleset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/UpdateLicenseAssetRuleset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/UpdateLicenseAssetRuleset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/UpdateLicenseAssetRuleset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/UpdateLicenseAssetRuleset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/UpdateLicenseAssetRuleset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/UpdateLicenseAssetRuleset)
