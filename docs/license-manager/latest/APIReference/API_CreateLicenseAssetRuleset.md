---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicenseAssetRuleset.html
---

# CreateLicenseAssetRuleset
<a name="API_CreateLicenseAssetRuleset"></a>

Creates a license asset ruleset.

## Request Syntax
<a name="API_CreateLicenseAssetRuleset_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
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
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateLicenseAssetRuleset_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateLicenseAssetRuleset_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetRuleset-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: Yes

 ** [Description](#API_CreateLicenseAssetRuleset_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetRuleset-request-Description"></a>
License asset ruleset description.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [Name](#API_CreateLicenseAssetRuleset_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetRuleset-request-Name"></a>
License asset ruleset name.
Type: String
Length Constraints: Maximum length of 128.
Required: Yes

 ** [Rules](#API_CreateLicenseAssetRuleset_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetRuleset-request-Rules"></a>
License asset rules.
Type: Array of [LicenseAssetRule](API_LicenseAssetRule.md) objects
Required: Yes

 ** [Tags](#API_CreateLicenseAssetRuleset_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetRuleset-request-Tags"></a>
Tags to add to the license asset ruleset.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateLicenseAssetRuleset_ResponseSyntax"></a>

```
{
   "LicenseAssetRulesetArn": "string"
}
```

## Response Elements
<a name="API_CreateLicenseAssetRuleset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseAssetRulesetArn](#API_CreateLicenseAssetRuleset_ResponseSyntax) **   <a name="licensemanager-CreateLicenseAssetRuleset-response-LicenseAssetRulesetArn"></a>
Amazon Resource Name (ARN) of the license asset ruleset.
Type: String

## Errors
<a name="API_CreateLicenseAssetRuleset_Errors"></a>

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
<a name="API_CreateLicenseAssetRuleset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/CreateLicenseAssetRuleset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/CreateLicenseAssetRuleset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/CreateLicenseAssetRuleset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/CreateLicenseAssetRuleset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/CreateLicenseAssetRuleset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/CreateLicenseAssetRuleset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/CreateLicenseAssetRuleset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/CreateLicenseAssetRuleset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/CreateLicenseAssetRuleset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/CreateLicenseAssetRuleset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
