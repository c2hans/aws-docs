---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListResourceComplianceSummaries.html
---

# ListResourceComplianceSummaries
<a name="API_ListResourceComplianceSummaries"></a>

Returns a resource-level summary count. The summary includes information about compliant and non-compliant statuses and detailed compliance-item severity counts, according to the filter criteria you specify.

## Request Syntax
<a name="API_ListResourceComplianceSummaries_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourceComplianceSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListResourceComplianceSummaries_RequestSyntax) **   <a name="systemsmanager-ListResourceComplianceSummaries-request-Filters"></a>
One or more filters. Use a filter to return a more specific list of results.
Type: Array of [ComplianceStringFilter](API_ComplianceStringFilter.md) objects
Required: No

 ** [MaxResults](#API_ListResourceComplianceSummaries_RequestSyntax) **   <a name="systemsmanager-ListResourceComplianceSummaries-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListResourceComplianceSummaries_RequestSyntax) **   <a name="systemsmanager-ListResourceComplianceSummaries-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListResourceComplianceSummaries_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceComplianceSummaryItems": [
      {
         "ComplianceType": "string",
         "CompliantSummary": {
            "CompliantCount": number,
            "SeveritySummary": {
               "CriticalCount": number,
               "HighCount": number,
               "InformationalCount": number,
               "LowCount": number,
               "MediumCount": number,
               "UnspecifiedCount": number
            }
         },
         "ExecutionSummary": {
            "ExecutionId": "string",
            "ExecutionTime": number,
            "ExecutionType": "string"
         },
         "NonCompliantSummary": {
            "NonCompliantCount": number,
            "SeveritySummary": {
               "CriticalCount": number,
               "HighCount": number,
               "InformationalCount": number,
               "LowCount": number,
               "MediumCount": number,
               "UnspecifiedCount": number
            }
         },
         "OverallSeverity": "string",
         "ResourceId": "string",
         "ResourceType": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourceComplianceSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourceComplianceSummaries_ResponseSyntax) **   <a name="systemsmanager-ListResourceComplianceSummaries-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

 ** [ResourceComplianceSummaryItems](#API_ListResourceComplianceSummaries_ResponseSyntax) **   <a name="systemsmanager-ListResourceComplianceSummaries-response-ResourceComplianceSummaryItems"></a>
A summary count for specified or targeted managed nodes. Summary count includes information about compliant and non-compliant State Manager associations, patch status, or custom items according to the filter criteria that you specify.
Type: Array of [ResourceComplianceSummaryItem](API_ResourceComplianceSummaryItem.md) objects

## Errors
<a name="API_ListResourceComplianceSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidFilter **
The filter name isn't valid. Verify that you entered the correct name and try again.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_ListResourceComplianceSummaries_Examples"></a>

### Example
<a name="API_ListResourceComplianceSummaries_Example_1"></a>

This example illustrates one usage of ListResourceComplianceSummaries.

#### Sample Request
<a name="API_ListResourceComplianceSummaries_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListResourceComplianceSummaries
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240401T185225Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240401/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2
```

#### Sample Response
<a name="API_ListResourceComplianceSummaries_Example_1_Response"></a>

```
{
    "ResourceComplianceSummaryItems": [
        {
            "ComplianceType": "Association",
            "CompliantSummary": {
                "CompliantCount": 3,
                "SeveritySummary": {
                    "CriticalCount": 0,
                    "HighCount": 1,
                    "InformationalCount": 0,
                    "LowCount": 0,
                    "MediumCount": 0,
                    "UnspecifiedCount": 2
                }
            },
            "ExecutionSummary": {
                "ExecutionTime": 1585766022
            },
            "NonCompliantSummary": {
                "NonCompliantCount": 0,
                "SeveritySummary": {
                    "CriticalCount": 0,
                    "HighCount": 0,
                    "InformationalCount": 0,
                    "LowCount": 0,
                    "MediumCount": 0,
                    "UnspecifiedCount": 0
                }
            },
            "OverallSeverity": "HIGH",
            "ResourceId": "i-04bf6ad63bEXAMPLE",
            "ResourceType": "ManagedInstance",
            "Status": "COMPLIANT"
        },
        {
            "ComplianceType": "Patch",
            "CompliantSummary": {
                "CompliantCount": 27,
                "SeveritySummary": {
                    "CriticalCount": 0,
                    "HighCount": 0,
                    "InformationalCount": 0,
                    "LowCount": 0,
                    "MediumCount": 0,
                    "UnspecifiedCount": 27
                }
            },
            "ExecutionSummary": {
                "ExecutionId": "b95523e7-28e5-488e-a753-fd1d3EXAMPLE",
                "ExecutionTime": 1585244656,
                "ExecutionType": "Command"
            },
            "NonCompliantSummary": {
                "NonCompliantCount": 1,
                "SeveritySummary": {
                    "CriticalCount": 0,
                    "HighCount": 0,
                    "InformationalCount": 0,
                    "LowCount": 0,
                    "MediumCount": 0,
                    "UnspecifiedCount": 1
                }
            },
            "OverallSeverity": "UNSPECIFIED",
            "ResourceId": "i-04bf6ad63bEXAMPLE",
            "ResourceType": "ManagedInstance",
            "Status": "NON_COMPLIANT"
        }
    ]
}
```

## See Also
<a name="API_ListResourceComplianceSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListResourceComplianceSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListResourceComplianceSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListResourceComplianceSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListResourceComplianceSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListResourceComplianceSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListResourceComplianceSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListResourceComplianceSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListResourceComplianceSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListResourceComplianceSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListResourceComplianceSummaries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
