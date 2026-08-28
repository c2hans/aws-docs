---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_RunFleetAdvisorLsaAnalysis.html
---

# RunFleetAdvisorLsaAnalysis
<a name="API_RunFleetAdvisorLsaAnalysis"></a>

**Important**
 End of support notice: On May 20, 2026, AWS will end support for AWS DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor; console or AWS DMS Fleet Advisor; resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).

Runs large-scale assessment (LSA) analysis on every Fleet Advisor collector in your account.

## Response Syntax
<a name="API_RunFleetAdvisorLsaAnalysis_ResponseSyntax"></a>

```
{
   "LsaAnalysisId": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_RunFleetAdvisorLsaAnalysis_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LsaAnalysisId](#API_RunFleetAdvisorLsaAnalysis_ResponseSyntax) **   <a name="DMS-RunFleetAdvisorLsaAnalysis-response-LsaAnalysisId"></a>
The ID of the LSA analysis run.
Type: String

 ** [Status](#API_RunFleetAdvisorLsaAnalysis_ResponseSyntax) **   <a name="DMS-RunFleetAdvisorLsaAnalysis-response-Status"></a>
The status of the LSA analysis, for example `COMPLETED`.
Type: String

## Errors
<a name="API_RunFleetAdvisorLsaAnalysis_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_RunFleetAdvisorLsaAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/RunFleetAdvisorLsaAnalysis)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/RunFleetAdvisorLsaAnalysis)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/RunFleetAdvisorLsaAnalysis)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/RunFleetAdvisorLsaAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/RunFleetAdvisorLsaAnalysis)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/RunFleetAdvisorLsaAnalysis)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/RunFleetAdvisorLsaAnalysis)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/RunFleetAdvisorLsaAnalysis)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/RunFleetAdvisorLsaAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/RunFleetAdvisorLsaAnalysis)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
