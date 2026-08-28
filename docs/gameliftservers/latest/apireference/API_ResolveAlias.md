---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ResolveAlias.html
---

# ResolveAlias
<a name="API_ResolveAlias"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Attempts to retrieve a fleet ID that is associated with an alias. Specify a unique alias identifier.

If the alias has a `SIMPLE` routing strategy, Amazon GameLift Servers returns a fleet ID. If the alias has a `TERMINAL` routing strategy, the result is a `TerminalRoutingStrategyException`.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_ResolveAlias_RequestSyntax"></a>

```
{
   "AliasId": "{{string}}"
}
```

## Request Parameters
<a name="API_ResolveAlias_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AliasId](#API_ResolveAlias_RequestSyntax) **   <a name="gameliftservers-ResolveAlias-request-AliasId"></a>
The unique identifier of the alias that you want to retrieve a fleet ID for. You can use either the alias ID or ARN value.
Type: String
Pattern: `^alias-\S+|^arn:.*:alias\/alias-\S+`
Required: Yes

## Response Syntax
<a name="API_ResolveAlias_ResponseSyntax"></a>

```
{
   "FleetArn": "string",
   "FleetId": "string"
}
```

## Response Elements
<a name="API_ResolveAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetArn](#API_ResolveAlias_ResponseSyntax) **   <a name="gameliftservers-ResolveAlias-response-FleetArn"></a>
 The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) associated with the GameLift fleet resource that this alias points to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_ResolveAlias_ResponseSyntax) **   <a name="gameliftservers-ResolveAlias-response-FleetId"></a>
The fleet identifier that the alias is pointing to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`

## Errors
<a name="API_ResolveAlias_Errors"></a>

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

 ** TerminalRoutingStrategyException **
The service is unable to resolve the routing for a particular alias because it has a terminal `RoutingStrategy` associated with it. The message returned in this exception is the message defined in the routing strategy itself. Such requests should only be retried if the routing strategy for the specified alias is modified.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_ResolveAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ResolveAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ResolveAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ResolveAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ResolveAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ResolveAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ResolveAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ResolveAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ResolveAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ResolveAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ResolveAlias)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
