---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_StartAssessmentRun.html
---

# StartAssessmentRun
<a name="API_StartAssessmentRun"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Starts the assessment run specified by the ARN of the assessment template. For this API to function properly, you must not exceed the limit of running up to 500 concurrent agents per AWS account.

## Request Syntax
<a name="API_StartAssessmentRun_RequestSyntax"></a>

```
{
   "assessmentRunName": "{{string}}",
   "assessmentTemplateArn": "{{string}}"
}
```

## Request Parameters
<a name="API_StartAssessmentRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [assessmentRunName](#API_StartAssessmentRun_RequestSyntax) **   <a name="Inspector-StartAssessmentRun-request-assessmentRunName"></a>
You can specify the name for the assessment run. The name must be unique for the assessment template whose ARN is used to start the assessment run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Required: No

 ** [assessmentTemplateArn](#API_StartAssessmentRun_RequestSyntax) **   <a name="Inspector-StartAssessmentRun-request-assessmentTemplateArn"></a>
The ARN of the assessment template of the assessment run that you want to start.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Syntax
<a name="API_StartAssessmentRun_ResponseSyntax"></a>

```
{
   "assessmentRunArn": "string"
}
```

## Response Elements
<a name="API_StartAssessmentRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentRunArn](#API_StartAssessmentRun_ResponseSyntax) **   <a name="Inspector-StartAssessmentRun-response-assessmentRunArn"></a>
The ARN of the assessment run that has been started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

## Errors
<a name="API_StartAssessmentRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AgentsAlreadyRunningAssessmentException **
You started an assessment run, but one of the instances is already participating in another assessment run.
 ** agents **

 ** agentsTruncated **

 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** InternalException **
Internal server error.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 500

 ** InvalidCrossAccountRoleException **
Amazon Inspector Classic cannot assume the cross-account role that it needs to list your EC2 instances during the assessment run.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** InvalidInputException **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error code describes the limit exceeded.
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
<a name="API_StartAssessmentRun_Examples"></a>

### Example
<a name="API_StartAssessmentRun_Example_1"></a>

This example illustrates one usage of StartAssessmentRun.

#### Sample Request
<a name="API_StartAssessmentRun_Example_1_Request"></a>

```

                  POST / HTTP/1.1
                  Host: inspector.us-west-2.amazonaws.com
                  Accept-Encoding: identity
                  Content-Length: 142
                  X-Amz-Target: InspectorService.StartAssessmentRun
                  X-Amz-Date: 20160331T182519Z
                  User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
                  Content-Type: application/x-amz-json-1.1
                  Authorization: AUTHPARAMS
                  {
                    "assessmentRunName": "examplerun",
                    "assessmentTemplateArn": "arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T"
                  }
```

#### Sample Response
<a name="API_StartAssessmentRun_Example_1_Response"></a>

```

                  HTTP/1.1 200 OK
                  x-amzn-RequestId: ed349455-f76d-11e5-b473-ed8493878c40
                  Content-Type: application/x-amz-json-1.1
                  Content-Length: 116
                  Date: Thu, 31 Mar 2016 18:25:22 GMT
                  {
                    "assessmentRunArn": "arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-jOoroxyY"
                  }
```

## See Also
<a name="API_StartAssessmentRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/StartAssessmentRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/StartAssessmentRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/StartAssessmentRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/StartAssessmentRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/StartAssessmentRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/StartAssessmentRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/StartAssessmentRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/StartAssessmentRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/StartAssessmentRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/StartAssessmentRun)
