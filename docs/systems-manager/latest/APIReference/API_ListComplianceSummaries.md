---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListComplianceSummaries.html
---

# ListComplianceSummaries
<a name="API_ListComplianceSummaries"></a>

Returns a summary count of compliant and non-compliant resources for a compliance type. For example, this call can return State Manager associations, patches, or custom compliance types according to the filter criteria that you specify.

## Request Syntax
<a name="API_ListComplianceSummaries_RequestSyntax"></a>

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
<a name="API_ListComplianceSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListComplianceSummaries_RequestSyntax) **   <a name="systemsmanager-ListComplianceSummaries-request-Filters"></a>
One or more compliance or inventory filters. Use a filter to return a more specific list of results.
Type: Array of [ComplianceStringFilter](API_ComplianceStringFilter.md) objects
Required: No

 ** [MaxResults](#API_ListComplianceSummaries_RequestSyntax) **   <a name="systemsmanager-ListComplianceSummaries-request-MaxResults"></a>
The maximum number of items to return for this call. Currently, you can specify null or 50. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListComplianceSummaries_RequestSyntax) **   <a name="systemsmanager-ListComplianceSummaries-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListComplianceSummaries_ResponseSyntax"></a>

```
{
   "ComplianceSummaryItems": [
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
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListComplianceSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComplianceSummaryItems](#API_ListComplianceSummaries_ResponseSyntax) **   <a name="systemsmanager-ListComplianceSummaries-response-ComplianceSummaryItems"></a>
A list of compliant and non-compliant summary counts based on compliance types. For example, this call returns State Manager associations, patches, or custom compliance types according to the filter criteria that you specified.
Type: Array of [ComplianceSummaryItem](API_ComplianceSummaryItem.md) objects

 ** [NextToken](#API_ListComplianceSummaries_ResponseSyntax) **   <a name="systemsmanager-ListComplianceSummaries-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

## Errors
<a name="API_ListComplianceSummaries_Errors"></a>

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
<a name="API_ListComplianceSummaries_Examples"></a>

### Example
<a name="API_ListComplianceSummaries_Example_1"></a>

This example illustrates one usage of ListComplianceSummaries.

#### Sample Request
<a name="API_ListComplianceSummaries_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListComplianceSummaries
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240401T174348Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240401/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2
```

#### Sample Response
<a name="API_ListComplianceSummaries_Example_1_Response"></a>

```
{
    "ComplianceSummaryItems": [
        {
            "ComplianceType": "FleetTotal",
            "CompliantSummary": {
                "CompliantCount": 1,
                "SeveritySummary": {
                    "CriticalCount": 0,
                    "HighCount": 1,
                    "InformationalCount": 0,
                    "LowCount": 0,
                    "MediumCount": 0,
                    "UnspecifiedCount": 0
                }
            },
            "NonCompliantSummary": {
                "NonCompliantCount": 2,
                "SeveritySummary": {
                    "CriticalCount": 0,
                    "HighCount": 0,
                    "InformationalCount": 0,
                    "LowCount": 0,
                    "MediumCount": 0,
                    "UnspecifiedCount": 2
                }
            }
        },
        {
            "ComplianceType": "Association",
            "CompliantSummary": {
                "CompliantCount": 3,
                "SeveritySummary": {
                    "CriticalCount": 0,
                    "HighCount": 2,
                    "InformationalCount": 0,
                    "LowCount": 0,
                    "MediumCount": 0,
                    "UnspecifiedCount": 1
                }
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
            }
        },
        {
            "ComplianceType": "Patch",
            "CompliantSummary": {
                "CompliantCount": 1,
                "SeveritySummary": {
                    "CriticalCount": 0,
                    "HighCount": 0,
                    "InformationalCount": 0,
                    "LowCount": 0,
                    "MediumCount": 0,
                    "UnspecifiedCount": 1
                }
            },
            "NonCompliantSummary": {
                "NonCompliantCount": 2,
                "SeveritySummary": {
                    "CriticalCount": 0,
                    "HighCount": 0,
                    "InformationalCount": 0,
                    "LowCount": 0,
                    "MediumCount": 0,
                    "UnspecifiedCount": 2
                }
            }
        }
    ]
}
```

## See Also
<a name="API_ListComplianceSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListComplianceSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListComplianceSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListComplianceSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListComplianceSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListComplianceSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListComplianceSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListComplianceSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListComplianceSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListComplianceSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListComplianceSummaries)
