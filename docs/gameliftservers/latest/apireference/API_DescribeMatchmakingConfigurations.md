---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeMatchmakingConfigurations.html
---

# DescribeMatchmakingConfigurations
<a name="API_DescribeMatchmakingConfigurations"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves the details of FlexMatch matchmaking configurations.

This operation offers the following options: (1) retrieve all matchmaking configurations, (2) retrieve configurations for a specified list, or (3) retrieve all configurations that use a specified rule set name. When requesting multiple items, use the pagination parameters to retrieve results as a set of sequential pages.

If successful, a configuration is returned for each requested name. When specifying a list of names, only configurations that currently exist are returned.

 **Learn more**

 [ Setting up FlexMatch matchmakers](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/matchmaker-build.html)

## Request Syntax
<a name="API_DescribeMatchmakingConfigurations_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Names": [ "{{string}}" ],
   "NextToken": "{{string}}",
   "RuleSetName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMatchmakingConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Limit](#API_DescribeMatchmakingConfigurations_RequestSyntax) **   <a name="gameliftservers-DescribeMatchmakingConfigurations-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages. This parameter is limited to 10.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Names](#API_DescribeMatchmakingConfigurations_RequestSyntax) **   <a name="gameliftservers-DescribeMatchmakingConfigurations-request-Names"></a>
A unique identifier for the matchmaking configuration(s) to retrieve. You can use either the configuration name or ARN value. To request all existing configurations, leave this parameter empty.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]*|^arn:.*:matchmakingconfiguration\/[a-zA-Z0-9-\.]*`
Required: No

 ** [NextToken](#API_DescribeMatchmakingConfigurations_RequestSyntax) **   <a name="gameliftservers-DescribeMatchmakingConfigurations-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [RuleSetName](#API_DescribeMatchmakingConfigurations_RequestSyntax) **   <a name="gameliftservers-DescribeMatchmakingConfigurations-request-RuleSetName"></a>
A unique identifier for the matchmaking rule set. You can use either the rule set name or ARN value. Use this parameter to retrieve all matchmaking configurations that use this rule set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]*|^arn:.*:matchmakingruleset\/[a-zA-Z0-9-\.]*`
Required: No

## Response Syntax
<a name="API_DescribeMatchmakingConfigurations_ResponseSyntax"></a>

```
{
   "Configurations": [
      {
         "AcceptanceRequired": boolean,
         "AcceptanceTimeoutSeconds": number,
         "AdditionalPlayerCount": number,
         "BackfillMode": "string",
         "ConfigurationArn": "string",
         "CreationTime": number,
         "CustomEventData": "string",
         "Description": "string",
         "FlexMatchMode": "string",
         "GameProperties": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "GameSessionData": "string",
         "GameSessionQueueArns": [ "string" ],
         "Name": "string",
         "NotificationTarget": "string",
         "RequestTimeoutSeconds": number,
         "RuleSetArn": "string",
         "RuleSetName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeMatchmakingConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Configurations](#API_DescribeMatchmakingConfigurations_ResponseSyntax) **   <a name="gameliftservers-DescribeMatchmakingConfigurations-response-Configurations"></a>
A collection of requested matchmaking configurations.
Type: Array of [MatchmakingConfiguration](API_MatchmakingConfiguration.md) objects

 ** [NextToken](#API_DescribeMatchmakingConfigurations_ResponseSyntax) **   <a name="gameliftservers-DescribeMatchmakingConfigurations-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DescribeMatchmakingConfigurations_Errors"></a>

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
<a name="API_DescribeMatchmakingConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeMatchmakingConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeMatchmakingConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeMatchmakingConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeMatchmakingConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeMatchmakingConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeMatchmakingConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeMatchmakingConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeMatchmakingConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeMatchmakingConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeMatchmakingConfigurations)
