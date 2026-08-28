---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseAssetRulesets.html
---

# ListLicenseAssetRulesets
<a name="API_ListLicenseAssetRulesets"></a>

Lists license asset rulesets.

## Request Syntax
<a name="API_ListLicenseAssetRulesets_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ShowAWSManagedLicenseAssetRulesets": {{boolean}}
}
```

## Request Parameters
<a name="API_ListLicenseAssetRulesets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListLicenseAssetRulesets_RequestSyntax) **   <a name="licensemanager-ListLicenseAssetRulesets-request-Filters"></a>
Filters to scope the results. Following filters are supported
+  `Name`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxResults](#API_ListLicenseAssetRulesets_RequestSyntax) **   <a name="licensemanager-ListLicenseAssetRulesets-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [NextToken](#API_ListLicenseAssetRulesets_RequestSyntax) **   <a name="licensemanager-ListLicenseAssetRulesets-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

 ** [ShowAWSManagedLicenseAssetRulesets](#API_ListLicenseAssetRulesets_RequestSyntax) **   <a name="licensemanager-ListLicenseAssetRulesets-request-ShowAWSManagedLicenseAssetRulesets"></a>
Specifies whether to show License Manager managed license asset rulesets.
Type: Boolean
Required: No

## Response Syntax
<a name="API_ListLicenseAssetRulesets_ResponseSyntax"></a>

```
{
   "LicenseAssetRulesets": [
      {
         "Description": "string",
         "LicenseAssetRulesetArn": "string",
         "Name": "string",
         "Rules": [
            {
               "RuleStatement": {
                  "InstanceRuleStatement": {
                     "AndRuleStatement": {
                        "MatchingRuleStatements": [
                           {
                              "Constraint": "string",
                              "KeyToMatch": "string",
                              "ValueToMatch": [ "string" ]
                           }
                        ],
                        "ScriptRuleStatements": [
                           {
                              "KeyToMatch": "string",
                              "Script": "string"
                           }
                        ]
                     },
                     "MatchingRuleStatement": {
                        "Constraint": "string",
                        "KeyToMatch": "string",
                        "ValueToMatch": [ "string" ]
                     },
                     "OrRuleStatement": {
                        "MatchingRuleStatements": [
                           {
                              "Constraint": "string",
                              "KeyToMatch": "string",
                              "ValueToMatch": [ "string" ]
                           }
                        ],
                        "ScriptRuleStatements": [
                           {
                              "KeyToMatch": "string",
                              "Script": "string"
                           }
                        ]
                     },
                     "ScriptRuleStatement": {
                        "KeyToMatch": "string",
                        "Script": "string"
                     }
                  },
                  "LicenseConfigurationRuleStatement": {
                     "AndRuleStatement": {
                        "MatchingRuleStatements": [
                           {
                              "Constraint": "string",
                              "KeyToMatch": "string",
                              "ValueToMatch": [ "string" ]
                           }
                        ],
                        "ScriptRuleStatements": [
                           {
                              "KeyToMatch": "string",
                              "Script": "string"
                           }
                        ]
                     },
                     "MatchingRuleStatement": {
                        "Constraint": "string",
                        "KeyToMatch": "string",
                        "ValueToMatch": [ "string" ]
                     },
                     "OrRuleStatement": {
                        "MatchingRuleStatements": [
                           {
                              "Constraint": "string",
                              "KeyToMatch": "string",
                              "ValueToMatch": [ "string" ]
                           }
                        ],
                        "ScriptRuleStatements": [
                           {
                              "KeyToMatch": "string",
                              "Script": "string"
                           }
                        ]
                     }
                  },
                  "LicenseRuleStatement": {
                     "AndRuleStatement": {
                        "MatchingRuleStatements": [
                           {
                              "Constraint": "string",
                              "KeyToMatch": "string",
                              "ValueToMatch": [ "string" ]
                           }
                        ],
                        "ScriptRuleStatements": [
                           {
                              "KeyToMatch": "string",
                              "Script": "string"
                           }
                        ]
                     },
                     "MatchingRuleStatement": {
                        "Constraint": "string",
                        "KeyToMatch": "string",
                        "ValueToMatch": [ "string" ]
                     },
                     "OrRuleStatement": {
                        "MatchingRuleStatements": [
                           {
                              "Constraint": "string",
                              "KeyToMatch": "string",
                              "ValueToMatch": [ "string" ]
                           }
                        ],
                        "ScriptRuleStatements": [
                           {
                              "KeyToMatch": "string",
                              "Script": "string"
                           }
                        ]
                     }
                  }
               }
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLicenseAssetRulesets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseAssetRulesets](#API_ListLicenseAssetRulesets_ResponseSyntax) **   <a name="licensemanager-ListLicenseAssetRulesets-response-LicenseAssetRulesets"></a>
License asset rulesets.
Type: Array of [LicenseAssetRuleset](API_LicenseAssetRuleset.md) objects

 ** [NextToken](#API_ListLicenseAssetRulesets_ResponseSyntax) **   <a name="licensemanager-ListLicenseAssetRulesets-response-NextToken"></a>
Token for the next set of results.
Type: String

## Errors
<a name="API_ListLicenseAssetRulesets_Errors"></a>

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
<a name="API_ListLicenseAssetRulesets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListLicenseAssetRulesets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListLicenseAssetRulesets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListLicenseAssetRulesets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListLicenseAssetRulesets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListLicenseAssetRulesets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListLicenseAssetRulesets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListLicenseAssetRulesets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListLicenseAssetRulesets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListLicenseAssetRulesets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListLicenseAssetRulesets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
