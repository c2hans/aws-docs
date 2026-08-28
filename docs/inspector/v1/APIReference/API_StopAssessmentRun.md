---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_StopAssessmentRun.html
---

# StopAssessmentRun
<a name="API_StopAssessmentRun"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Stops the assessment run that is specified by the ARN of the assessment run.

## Request Syntax
<a name="API_StopAssessmentRun_RequestSyntax"></a>

```
{
   "assessmentRunArn": "{{string}}",
   "stopAction": "{{string}}"
}
```

## Request Parameters
<a name="API_StopAssessmentRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [assessmentRunArn](#API_StopAssessmentRun_RequestSyntax) **   <a name="Inspector-StopAssessmentRun-request-assessmentRunArn"></a>
The ARN of the assessment run that you want to stop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [stopAction](#API_StopAssessmentRun_RequestSyntax) **   <a name="Inspector-StopAssessmentRun-request-stopAction"></a>
An input option that can be set to either START\_EVALUATION or SKIP\_EVALUATION. START\_EVALUATION (the default value), stops the AWS agent from collecting data and begins the results evaluation and the findings generation process. SKIP\_EVALUATION cancels the assessment run immediately, after which no findings are generated.
Type: String
Valid Values: `START_EVALUATION | SKIP_EVALUATION`
Required: No

## Response Elements
<a name="API_StopAssessmentRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopAssessmentRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 500

 ** InvalidInputException **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** NoSuchEntityException **
The request was rejected because it referenced an entity that does not exist. The error code describes the entity.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** ServiceTemporarilyUnavailableException **
The serice is temporary unavailable.
 ** canRetry **
You can wait and then retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 400

## Examples
<a name="API_StopAssessmentRun_Examples"></a>

### Example
<a name="API_StopAssessmentRun_Example_1"></a>

This example illustrates one usage of StopAssessmentRun.

#### Sample Request
<a name="API_StopAssessmentRun_Example_1_Request"></a>

```

                  POST / HTTP/1.1
                  Host: inspector.us-west-2.amazonaws.com
                  Accept-Encoding: identity
                  Content-Length: 117
                  X-Amz-Target: InspectorService.StopAssessmentRun
                  X-Amz-Date: 20160331T183401Z
                  User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
                  Content-Type: application/x-amz-json-1.1
                  Authorization: AUTHPARAMS
                  {
                    "assessmentRunArn": "arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-11LMTAVe"
                  }
```

#### Sample Response
<a name="API_StopAssessmentRun_Example_1_Response"></a>

```

                  HTTP/1.1 200 OK
                  x-amzn-RequestId: 23e1a935-f76f-11e5-92d3-7ba54a65df23
                  Content-Type: application/x-amz-json-1.1
                  Content-Length: 0
                  Date: Thu, 31 Mar 2016 18:34:02 GMT
```

## See Also
<a name="API_StopAssessmentRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/StopAssessmentRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/StopAssessmentRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/StopAssessmentRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/StopAssessmentRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/StopAssessmentRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/StopAssessmentRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/StopAssessmentRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/StopAssessmentRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/StopAssessmentRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/StopAssessmentRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
