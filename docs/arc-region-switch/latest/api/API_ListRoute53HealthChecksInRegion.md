---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListRoute53HealthChecksInRegion.html
---

# ListRoute53HealthChecksInRegion
<a name="API_ListRoute53HealthChecksInRegion"></a>

List the Amazon Route 53 health checks in a specific AWS Region.

## Request Parameters
<a name="API_ListRoute53HealthChecksInRegion_RequestParameters"></a>

 ** arn **
The Amazon Resource Name (ARN) of the Arc Region Switch Plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

 ** hostedZoneId **
The hosted zone ID for the health checks.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** maxResults **
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** recordName **
The record name for the health checks.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Elements
<a name="API_ListRoute53HealthChecksInRegion_ResponseElements"></a>

The following elements are returned by the service.

 ** healthChecks **
List of the health checks requested.
Type: Array of [Route53HealthCheck](API_Route53HealthCheck.md) objects

 ** nextToken **
A pagination token. A response may contain no results while still including a `nextToken`. Continue paginating until `nextToken` is null to retrieve all results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListRoute53HealthChecksInRegion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403
HTTP Status Code: 403

 ** IllegalArgumentException **
The request processing has an invalid argument.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404
HTTP Status Code: 404

## See Also
<a name="API_ListRoute53HealthChecksInRegion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/ListRoute53HealthChecksInRegion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/ListRoute53HealthChecksInRegion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ListRoute53HealthChecksInRegion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/ListRoute53HealthChecksInRegion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ListRoute53HealthChecksInRegion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/ListRoute53HealthChecksInRegion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/ListRoute53HealthChecksInRegion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/ListRoute53HealthChecksInRegion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/ListRoute53HealthChecksInRegion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ListRoute53HealthChecksInRegion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
