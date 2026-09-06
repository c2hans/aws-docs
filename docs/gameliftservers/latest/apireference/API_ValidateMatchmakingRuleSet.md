---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ValidateMatchmakingRuleSet.html
---

# ValidateMatchmakingRuleSet
<a name="API_ValidateMatchmakingRuleSet"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Validates the syntax of a matchmaking rule or rule set. This operation checks that the rule set is using syntactically correct JSON and that it conforms to allowed property expressions. To validate syntax, provide a rule set JSON string.

 **Learn more**
+  [Build a rule set](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html)

## Request Syntax
<a name="API_ValidateMatchmakingRuleSet_RequestSyntax"></a>

```
{
   "RuleSetBody": "{{string}}"
}
```

## Request Parameters
<a name="API_ValidateMatchmakingRuleSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [RuleSetBody](#API_ValidateMatchmakingRuleSet_RequestSyntax) **   <a name="gameliftservers-ValidateMatchmakingRuleSet-request-RuleSetBody"></a>
A collection of matchmaking rules to validate, formatted as a JSON string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: Yes

## Response Syntax
<a name="API_ValidateMatchmakingRuleSet_ResponseSyntax"></a>

```
{
   "Valid": boolean
}
```

## Response Elements
<a name="API_ValidateMatchmakingRuleSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Valid](#API_ValidateMatchmakingRuleSet_ResponseSyntax) **   <a name="gameliftservers-ValidateMatchmakingRuleSet-response-Valid"></a>
A response indicating whether the rule set is valid.
Type: Boolean

## Errors
<a name="API_ValidateMatchmakingRuleSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## See Also
<a name="API_ValidateMatchmakingRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ValidateMatchmakingRuleSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ValidateMatchmakingRuleSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ValidateMatchmakingRuleSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ValidateMatchmakingRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ValidateMatchmakingRuleSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ValidateMatchmakingRuleSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ValidateMatchmakingRuleSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ValidateMatchmakingRuleSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ValidateMatchmakingRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ValidateMatchmakingRuleSet)
