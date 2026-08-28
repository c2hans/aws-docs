---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateFindingAggregator.html
---

# CreateFindingAggregator
<a name="API_CreateFindingAggregator"></a>

**Note**
The *aggregation Region* is now called the *home Region*.

Used to enable cross-Region aggregation. This operation can be invoked from the home Region only.

For information about how cross-Region aggregation works, see [Understanding cross-Region aggregation in Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html) in the * AWS Security Hub CSPM User Guide*.

## Request Syntax
<a name="API_CreateFindingAggregator_RequestSyntax"></a>

```
POST /findingAggregator/create HTTP/1.1
Content-type: application/json

{
   "RegionLinkingMode": "{{string}}",
   "Regions": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_CreateFindingAggregator_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateFindingAggregator_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RegionLinkingMode](#API_CreateFindingAggregator_RequestSyntax) **   <a name="securityhub-CreateFindingAggregator-request-RegionLinkingMode"></a>
Indicates whether to aggregate findings from all of the available Regions in the current partition. Also determines whether to automatically aggregate findings from new Regions as Security Hub CSPM supports them and you opt into them.
The selected option also determines how to use the Regions provided in the Regions list.
The options are as follows:
+  `ALL_REGIONS` - Aggregates findings from all of the Regions where Security Hub CSPM is enabled. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them.
+  `ALL_REGIONS_EXCEPT_SPECIFIED` - Aggregates findings from all of the Regions where Security Hub CSPM is enabled, except for the Regions listed in the `Regions` parameter. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them.
+  `SPECIFIED_REGIONS` - Aggregates findings only from the Regions listed in the `Regions` parameter. Security Hub CSPM does not automatically aggregate findings from new Regions.
+  `NO_REGIONS` - Aggregates no data because no Regions are selected as linked Regions.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [Regions](#API_CreateFindingAggregator_RequestSyntax) **   <a name="securityhub-CreateFindingAggregator-request-Regions"></a>
If `RegionLinkingMode` is `ALL_REGIONS_EXCEPT_SPECIFIED`, then this is a space-separated list of Regions that don't replicate and send findings to the home Region.
If `RegionLinkingMode` is `SPECIFIED_REGIONS`, then this is a space-separated list of Regions that do replicate and send findings to the home Region.
An `InvalidInputException` error results if you populate this field while `RegionLinkingMode` is `NO_REGIONS`.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_CreateFindingAggregator_ResponseSyntax"></a>

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
<a name="API_CreateFindingAggregator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FindingAggregationRegion](#API_CreateFindingAggregator_ResponseSyntax) **   <a name="securityhub-CreateFindingAggregator-response-FindingAggregationRegion"></a>
The home Region. Findings generated in linked Regions are replicated and sent to the home Region.
Type: String
Pattern: `.*\S.*`

 ** [FindingAggregatorArn](#API_CreateFindingAggregator_ResponseSyntax) **   <a name="securityhub-CreateFindingAggregator-response-FindingAggregatorArn"></a>
The ARN of the finding aggregator. You use the finding aggregator ARN to retrieve details for, update, and stop cross-Region aggregation.
Type: String
Pattern: `.*\S.*`

 ** [RegionLinkingMode](#API_CreateFindingAggregator_ResponseSyntax) **   <a name="securityhub-CreateFindingAggregator-response-RegionLinkingMode"></a>
Indicates whether to link all Regions, all Regions except for a list of excluded Regions, or a list of included Regions.
Type: String
Pattern: `.*\S.*`

 ** [Regions](#API_CreateFindingAggregator_ResponseSyntax) **   <a name="securityhub-CreateFindingAggregator-response-Regions"></a>
The list of excluded Regions or included Regions.
Type: Array of strings
Pattern: `.*\S.*`

## Errors
<a name="API_CreateFindingAggregator_Errors"></a>

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

## See Also
<a name="API_CreateFindingAggregator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/CreateFindingAggregator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/CreateFindingAggregator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CreateFindingAggregator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/CreateFindingAggregator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CreateFindingAggregator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/CreateFindingAggregator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/CreateFindingAggregator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/CreateFindingAggregator)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/CreateFindingAggregator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CreateFindingAggregator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
