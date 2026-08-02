---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteMatchmakingRuleSet.html
---

# DeleteMatchmakingRuleSet
<a name="API_DeleteMatchmakingRuleSet"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Deletes an existing matchmaking rule set. To delete the rule set, provide the rule set name. Rule sets cannot be deleted if they are currently being used by a matchmaking configuration.

 **Learn more**
+  [Build a rule set](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html)

## Request Syntax
<a name="API_DeleteMatchmakingRuleSet_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteMatchmakingRuleSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_DeleteMatchmakingRuleSet_RequestSyntax) **   <a name="gameliftservers-DeleteMatchmakingRuleSet-request-Name"></a>
A unique identifier for the matchmaking rule set to be deleted. (Note: The rule set name is different from the optional "name" field in the rule set body.) You can use either the rule set name or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]*|^arn:.*:matchmakingruleset\/[a-zA-Z0-9-\.]*`
Required: Yes

## Response Elements
<a name="API_DeleteMatchmakingRuleSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteMatchmakingRuleSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** TaggingFailedException **
The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## See Also
<a name="API_DeleteMatchmakingRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DeleteMatchmakingRuleSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DeleteMatchmakingRuleSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DeleteMatchmakingRuleSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DeleteMatchmakingRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DeleteMatchmakingRuleSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DeleteMatchmakingRuleSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DeleteMatchmakingRuleSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DeleteMatchmakingRuleSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DeleteMatchmakingRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DeleteMatchmakingRuleSet)
