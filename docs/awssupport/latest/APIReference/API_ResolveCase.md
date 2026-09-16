---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_ResolveCase.html
---

# ResolveCase
<a name="API_ResolveCase"></a>

Resolves a support case. This operation takes a `caseId` and returns the initial and final state of the case.

**Note**
You must have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan to use the AWS Support API. If you're in an AWS Region that doesn't offer one of these AWS Support plans, or if you haven't transitioned to one of these plans, you can use the AWS Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.
If you call the AWS Support API from an account that doesn't have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_ResolveCase_RequestSyntax"></a>

```
{
   "caseId": "{{string}}",
   "dryRun": {{boolean}}
}
```

## Request Parameters
<a name="API_ResolveCase_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [caseId](#API_ResolveCase_RequestSyntax) **   <a name="AWSSupport-ResolveCase-request-caseId"></a>
The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-exen-2025-c4c1d2bf33c5cf47*
Type: String

 ** [dryRun](#API_ResolveCase_RequestSyntax) **   <a name="AWSSupport-ResolveCase-request-dryRun"></a>
Specifies whether to validate the request without actually resolving the case. When set to `true`, the request is validated but the case isn't resolved, and the operation returns a `DryRunOperationException`. When omitted or set to `false`, the request runs normally.
Type: Boolean

## Response Syntax
<a name="API_ResolveCase_ResponseSyntax"></a>

```
{
   "finalCaseStatus": "string",
   "initialCaseStatus": "string"
}
```

## Response Elements
<a name="API_ResolveCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [finalCaseStatus](#API_ResolveCase_ResponseSyntax) **   <a name="AWSSupport-ResolveCase-response-finalCaseStatus"></a>
The status of the case after the [ResolveCase](#API_ResolveCase) request was processed.
Type: String

 ** [initialCaseStatus](#API_ResolveCase_ResponseSyntax) **   <a name="AWSSupport-ResolveCase-response-initialCaseStatus"></a>
The status of the case when the [ResolveCase](#API_ResolveCase) request was sent.
Type: String

## Errors
<a name="API_ResolveCase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CaseIdNotFound **
The requested `caseId` couldn't be located.
 ** message **
The requested `CaseId` could not be located.
HTTP Status Code: 400

 ** DryRunOperationException **
The request was valid, but the operation wasn't performed because `dryRun` was set to `true`.
HTTP Status Code: 400

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

## See Also
<a name="API_ResolveCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/ResolveCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/ResolveCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/ResolveCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/ResolveCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/ResolveCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/ResolveCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/ResolveCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/ResolveCase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/ResolveCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/ResolveCase)
