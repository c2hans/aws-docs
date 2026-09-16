---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeMatchmakingRuleSets.html
---

# DescribeMatchmakingRuleSets
<a name="API_DescribeMatchmakingRuleSets"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves the details for FlexMatch matchmaking rule sets. You can request all existing rule sets for the Region, or provide a list of one or more rule set names. When requesting multiple items, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a rule set is returned for each requested name.

 **Learn more**
+  [Build a rule set](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html)

## Request Syntax
<a name="API_DescribeMatchmakingRuleSets_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Names": [ "{{string}}" ],
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMatchmakingRuleSets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Limit](#API_DescribeMatchmakingRuleSets_RequestSyntax) **   <a name="gameliftservers-DescribeMatchmakingRuleSets-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [Names](#API_DescribeMatchmakingRuleSets_RequestSyntax) **   <a name="gameliftservers-DescribeMatchmakingRuleSets-request-Names"></a>
A list of one or more matchmaking rule set names to retrieve details for. (Note: The rule set name is different from the optional "name" field in the rule set body.) You can use either the rule set name or ARN value.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]*|^arn:.*:matchmakingruleset\/[a-zA-Z0-9-\.]*`
Required: No

 ** [NextToken](#API_DescribeMatchmakingRuleSets_RequestSyntax) **   <a name="gameliftservers-DescribeMatchmakingRuleSets-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_DescribeMatchmakingRuleSets_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RuleSets": [
      {
         "CreationTime": number,
         "RuleSetArn": "string",
         "RuleSetBody": "string",
         "RuleSetName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMatchmakingRuleSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuleSets](#API_DescribeMatchmakingRuleSets_ResponseSyntax) **   <a name="gameliftservers-DescribeMatchmakingRuleSets-response-RuleSets"></a>
A collection of requested matchmaking rule set objects.
Type: Array of [MatchmakingRuleSet](API_MatchmakingRuleSet.md) objects

 ** [NextToken](#API_DescribeMatchmakingRuleSets_ResponseSyntax) **   <a name="gameliftservers-DescribeMatchmakingRuleSets-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DescribeMatchmakingRuleSets_Errors"></a>

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

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## See Also
<a name="API_DescribeMatchmakingRuleSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeMatchmakingRuleSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeMatchmakingRuleSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeMatchmakingRuleSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeMatchmakingRuleSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeMatchmakingRuleSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeMatchmakingRuleSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeMatchmakingRuleSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeMatchmakingRuleSets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeMatchmakingRuleSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeMatchmakingRuleSets)
