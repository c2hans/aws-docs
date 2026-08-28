---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingAggregator.html
---

# GetFindingAggregator
<a name="API_GetFindingAggregator"></a>

**Note**
The *aggregation Region* is now called the *home Region*.

Returns the current configuration in the calling account for cross-Region aggregation. A finding aggregator is a resource that establishes the home Region and any linked Regions.

## Request Syntax
<a name="API_GetFindingAggregator_RequestSyntax"></a>

```
GET /findingAggregator/get/{{FindingAggregatorArn+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFindingAggregator_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FindingAggregatorArn](#API_GetFindingAggregator_RequestSyntax) **   <a name="securityhub-GetFindingAggregator-request-uri-FindingAggregatorArn"></a>
The ARN of the finding aggregator to return details for. To obtain the ARN, use `ListFindingAggregators`.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetFindingAggregator_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFindingAggregator_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FindingAggregationRegion": "string",
   "FindingAggregatorArn": "string",
   "RegionLinkingMode": "string",
   "Regions": [ "string" ]
}
```

## Response Elements
<a name="API_GetFindingAggregator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FindingAggregationRegion](#API_GetFindingAggregator_ResponseSyntax) **   <a name="securityhub-GetFindingAggregator-response-FindingAggregationRegion"></a>
The home Region. Findings generated in linked Regions are replicated and sent to the home Region.
Type: String
Pattern: `.*\S.*`

 ** [FindingAggregatorArn](#API_GetFindingAggregator_ResponseSyntax) **   <a name="securityhub-GetFindingAggregator-response-FindingAggregatorArn"></a>
The ARN of the finding aggregator.
Type: String
Pattern: `.*\S.*`

 ** [RegionLinkingMode](#API_GetFindingAggregator_ResponseSyntax) **   <a name="securityhub-GetFindingAggregator-response-RegionLinkingMode"></a>
Indicates whether to link all Regions, all Regions except for a list of excluded Regions, or a list of included Regions.
Type: String
Pattern: `.*\S.*`

 ** [Regions](#API_GetFindingAggregator_ResponseSyntax) **   <a name="securityhub-GetFindingAggregator-response-Regions"></a>
The list of excluded Regions or included Regions.
Type: Array of strings
Pattern: `.*\S.*`

## Errors
<a name="API_GetFindingAggregator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_GetFindingAggregator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetFindingAggregator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetFindingAggregator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetFindingAggregator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetFindingAggregator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetFindingAggregator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetFindingAggregator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetFindingAggregator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetFindingAggregator)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetFindingAggregator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetFindingAggregator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
