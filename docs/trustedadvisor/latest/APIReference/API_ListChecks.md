---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListChecks.html
---

# ListChecks
<a name="API_ListChecks"></a>

List a filterable set of Checks. This API provides global recommendations, eliminating the need to call the API in each AWS Region.

## Request Syntax
<a name="API_ListChecks_RequestSyntax"></a>

```
GET /v1/checks?awsService={{awsService}}&language={{language}}&maxResults={{maxResults}}&nextToken={{nextToken}}&pillar={{pillar}}&source={{source}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListChecks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [awsService](#API_ListChecks_RequestSyntax) **   <a name="ta-ListChecks-request-uri-awsService"></a>
The aws service associated with the check
Length Constraints: Minimum length of 2. Maximum length of 30.

 ** [language](#API_ListChecks_RequestSyntax) **   <a name="ta-ListChecks-request-uri-language"></a>
The ISO 639-1 code for the language that you want your checks to appear in.
Valid Values: `en | ja | zh | fr | de | ko | zh_TW | it | es | pt_BR | id`

 ** [maxResults](#API_ListChecks_RequestSyntax) **   <a name="ta-ListChecks-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [nextToken](#API_ListChecks_RequestSyntax) **   <a name="ta-ListChecks-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [pillar](#API_ListChecks_RequestSyntax) **   <a name="ta-ListChecks-request-uri-pillar"></a>
The pillar of the check
Valid Values: `cost_optimizing | performance | security | service_limits | fault_tolerance | operational_excellence`

 ** [source](#API_ListChecks_RequestSyntax) **   <a name="ta-ListChecks-request-uri-source"></a>
The source of the check
Valid Values: `aws_config | compute_optimizer | cost_explorer | lse | manual | pse | rds | resilience | resilience_hub | security_hub | stir | ta_check | well_architected | cost_optimization_hub`

## Request Body
<a name="API_ListChecks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListChecks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "checkSummaries": [
      {
         "arn": "string",
         "awsResourceTypes": [ "string" ],
         "awsServices": [ "string" ],
         "checkGranularity": "string",
         "description": "string",
         "id": "string",
         "metadata": {
            "string" : "string"
         },
         "name": "string",
         "pillars": [ "string" ],
         "recommendationId": "string",
         "resourceArnQueryable": boolean,
         "source": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListChecks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [checkSummaries](#API_ListChecks_ResponseSyntax) **   <a name="ta-ListChecks-response-checkSummaries"></a>
The list of Checks
Type: Array of [CheckSummary](API_CheckSummary.md) objects

 ** [nextToken](#API_ListChecks_ResponseSyntax) **   <a name="ta-ListChecks-response-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.

## Errors
<a name="API_ListChecks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Exception that access has been denied due to insufficient access
HTTP Status Code: 403

 ** InternalServerException **
Exception to notify that an unexpected internal error occurred during processing of the request
HTTP Status Code: 500

 ** ThrottlingException **
Exception to notify that requests are being throttled
HTTP Status Code: 429

 ** ValidationException **
Exception that the request failed to satisfy service constraints
HTTP Status Code: 400

## Examples
<a name="API_ListChecks_Examples"></a>

### List Checks With A Max Result
<a name="API_ListChecks_Example_1"></a>

List at most two Checks.

#### Sample Request
<a name="API_ListChecks_Example_1_Request"></a>

```
{
                    "maxResults": 2
                    }
```

#### Sample Response
<a name="API_ListChecks_Example_1_Response"></a>

```
{
                    "checkSummaries": [
                    {
                    "arn": "arn:aws:trustedadvisor:::check/1iG5NDGVre",
                    "awsServices": [
                    "EC2"
                    ],
                    "description": "Checks security groups for rules that allow unrestricted access to a resource. Unrestricted access increases opportunities for malicious activity (hacking, denial-of-service attacks, loss of data)",
                    "id": "1iG5NDGVre",
                    "metadata": {
                    "0": "Region",
                    "1": "Security Group Name",
                    "2": "Security Group ID",
                    "3": "Protocol",
                    "4": "Port",
                    "5": "Status",
                    "6": "IP Range"
                    },
                    "name": "Security Groups - Unrestricted Access",
                    "pillars": [
                    "security"
                    ],
                    "source": "ta_check",
                    "resourceArnQueryable": true,
                    "awsResourceTypes": [
                    "AWS::EC2::SecurityGroup"
                    ],
                    "checkGranularity": "resource",
                    "recommendationId": "9534ec9b-bf3a-44e8-8213-2ed68b39d9d5"
                    },
                    {
                    "arn": "arn:aws:trustedadvisor:::check/1qazXsw23e",
                    "awsServices": [
                    "RDS"
                    ],
                    "description": "Checks your usage of RDS and provides recommendations on purchase of Reserved Instances to help reduce costs incurred from using RDS On-Demand. AWS generates these recommendations by analyzing your On-Demand usage for the past 30 days. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of Reserved Instance to purchase to maximize your savings. This check covers recommendations based on partial upfront payment option with 1-year or 3-year commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.",
                    "id": "1qazXsw23e",
                    "metadata": {
                    "0": "Region",
                    "1": "Family",
                    "2": "Instance Type",
                    "3": "License Model",
                    "4": "Database Edition",
                    "5": "Database Engine",
                    "6": "Deployment Option",
                    "7": "Recommended number of Reserved Instances to purchase",
                    "8": "Expected Average Reserved Instance Utilization",
                    "9": "Estimated Savings with Recommendation (monthly)"
                    "10": "Upfront Cost of Reserved Instances",
                    "11": "Estimated cost of Reserved Instances (monthly)",
                    "12": "Estimated On-Demand Cost Post Recommended Reserved Instance Purchase (monthly)",
                    "13": "Estimated Break Even (months)",
                    "14": "Lookback Period (days)",
                    "15": "Term (years)"
                    },
                    "name": "Amazon Relational Database Service (RDS) Reserved Instance Optimization",
                    "pillars": [
                    "cost_optimizing"
                    ],
                    "source": "ta_check",
                    "resourceArnQueryable": false,
                    "awsResourceTypes": [],
                    "checkGranularity": "account",
                    "recommendationId": "8b602b6f-452d-4cb2-8a9e-c7650955d9cd"
                    },
                    {
                    "arn": "arn:aws:trustedadvisor:::check/1qw23er45t",
                    "awsServices": [
                    "Redshift"
                    ],
                    "description": "Checks your usage of Redshift and provides recommendations on purchase of Reserved Nodes to help reduce costs incurred from using Redshift On-Demand. AWS generates these recommendations by analyzing your On-Demand usage for the past 30 days. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of Reserved Nodes to purchase to maximize your savings. This check covers recommendations based on partial upfront payment option with 1-year or 3-year commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.",
                    "id": "1qw23er45t",
                    "metadata": {
                    "0": "Region",
                    "1": "Family",
                    "2": "Node Type",
                    "3": "Recommended number of Reserved Nodes to purchase",
                    "4": "Expected Average Reserved Node Utilization",
                    "5": "Estimated Savings with Recommendation (monthly)",
                    "6": "Upfront Cost of Reserved Nodes",
                    "7": "Estimated cost of Reserved Nodes (monthly)",
                    "8": "Estimated On-Demand Cost Post Recommended Reserved Nodes Purchase (monthly)",
                    "9": "Estimated Break Even (months)",
                    "10": "Lookback Period (days)",
                    "11": "Term (years)",
                    },
                    "name": "Amazon Redshift Reserved Node Optimization",
                    "pillars": [
                    "cost_optimizing"
                    ],
                    "source": "ta_check",
                    "resourceArnQueryable": false,
                    "awsResourceTypes": [],
                    "checkGranularity": "account",
                    "recommendationId": "4ecff4d4-1bc1-4c99-a5b8-0fff9ee500d6"
                    },
                    ],
                    "nextToken": "REDACTED"
                    }
```

## See Also
<a name="API_ListChecks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/ListChecks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/ListChecks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/ListChecks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/ListChecks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/ListChecks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/ListChecks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/ListChecks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/ListChecks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/ListChecks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/ListChecks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Trusted Advisor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query trustedadvisor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
