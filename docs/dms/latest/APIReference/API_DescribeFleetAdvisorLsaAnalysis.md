---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeFleetAdvisorLsaAnalysis.html
---

# DescribeFleetAdvisorLsaAnalysis
<a name="API_DescribeFleetAdvisorLsaAnalysis"></a>

**Important**
 End of support notice: On May 20, 2026, AWS will end support for AWS DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor; console or AWS DMS Fleet Advisor; resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).

Provides descriptions of large-scale assessment (LSA) analyses produced by your Fleet Advisor collectors.

## Request Syntax
<a name="API_DescribeFleetAdvisorLsaAnalysis_RequestSyntax"></a>

```
{
   "MaxRecords": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFleetAdvisorLsaAnalysis_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxRecords](#API_DescribeFleetAdvisorLsaAnalysis_RequestSyntax) **   <a name="DMS-DescribeFleetAdvisorLsaAnalysis-request-MaxRecords"></a>
Sets the maximum number of records returned in the response.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeFleetAdvisorLsaAnalysis_RequestSyntax) **   <a name="DMS-DescribeFleetAdvisorLsaAnalysis-request-NextToken"></a>
If `NextToken` is returned by a previous response, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeFleetAdvisorLsaAnalysis_ResponseSyntax"></a>

```
{
   "Analysis": [
      {
         "LsaAnalysisId": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFleetAdvisorLsaAnalysis_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Analysis](#API_DescribeFleetAdvisorLsaAnalysis_ResponseSyntax) **   <a name="DMS-DescribeFleetAdvisorLsaAnalysis-response-Analysis"></a>
A list of `FleetAdvisorLsaAnalysisResponse` objects.
Type: Array of [FleetAdvisorLsaAnalysisResponse](API_FleetAdvisorLsaAnalysisResponse.md) objects

 ** [NextToken](#API_DescribeFleetAdvisorLsaAnalysis_ResponseSyntax) **   <a name="DMS-DescribeFleetAdvisorLsaAnalysis-response-NextToken"></a>
If `NextToken` is returned, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

## Errors
<a name="API_DescribeFleetAdvisorLsaAnalysis_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DescribeFleetAdvisorLsaAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeFleetAdvisorLsaAnalysis)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeFleetAdvisorLsaAnalysis)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeFleetAdvisorLsaAnalysis)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeFleetAdvisorLsaAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeFleetAdvisorLsaAnalysis)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeFleetAdvisorLsaAnalysis)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeFleetAdvisorLsaAnalysis)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeFleetAdvisorLsaAnalysis)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeFleetAdvisorLsaAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeFleetAdvisorLsaAnalysis)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
