---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_UpdateAssessmentTarget.html
---

# UpdateAssessmentTarget
<a name="API_UpdateAssessmentTarget"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Updates the assessment target that is specified by the ARN of the assessment target.

If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target.

## Request Syntax
<a name="API_UpdateAssessmentTarget_RequestSyntax"></a>

```
{
   "assessmentTargetArn": "{{string}}",
   "assessmentTargetName": "{{string}}",
   "resourceGroupArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateAssessmentTarget_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [assessmentTargetArn](#API_UpdateAssessmentTarget_RequestSyntax) **   <a name="Inspector-UpdateAssessmentTarget-request-assessmentTargetArn"></a>
The ARN of the assessment target that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [assessmentTargetName](#API_UpdateAssessmentTarget_RequestSyntax) **   <a name="Inspector-UpdateAssessmentTarget-request-assessmentTargetName"></a>
The name of the assessment target that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Required: Yes

 ** [resourceGroupArn](#API_UpdateAssessmentTarget_RequestSyntax) **   <a name="Inspector-UpdateAssessmentTarget-request-resourceGroupArn"></a>
The ARN of the resource group that is used to specify the new resource group to associate with the assessment target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## Response Elements
<a name="API_UpdateAssessmentTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateAssessmentTarget_Errors"></a>

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
<a name="API_UpdateAssessmentTarget_Examples"></a>

### Example
<a name="API_UpdateAssessmentTarget_Example_1"></a>

This example illustrates one usage of UpdateAssessmentTarget.

#### Sample Request
<a name="API_UpdateAssessmentTarget_Example_1_Request"></a>

```

                  POST / HTTP/1.1
                  Host: inspector.us-west-2.amazonaws.com
                  Accept-Encoding: identity
                  Content-Length: 206
                  X-Amz-Target: InspectorService.UpdateAssessmentTarget
                  X-Amz-Date: 20160331T185748Z
                  User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
                  Content-Type: application/x-amz-json-1.1
                  Authorization: AUTHPARAMS
                  {
                    "assessmentTargetArn": "arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX",
                    "assessmentTargetName": "Example",
                    "resourceGroupArn": "arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-yNbgL5Pt"
                  }
```

#### Sample Response
<a name="API_UpdateAssessmentTarget_Example_1_Response"></a>

```

                  HTTP/1.1 200 OK
                  x-amzn-RequestId: 76bc43e7-f772-11e5-a5f3-fb6257e71620
                  Content-Type: application/x-amz-json-1.1
                  Content-Length: 0
                  Date: Thu, 31 Mar 2016 18:57:49 GMT
```

## See Also
<a name="API_UpdateAssessmentTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/UpdateAssessmentTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/UpdateAssessmentTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/UpdateAssessmentTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/UpdateAssessmentTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/UpdateAssessmentTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/UpdateAssessmentTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/UpdateAssessmentTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/UpdateAssessmentTarget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/UpdateAssessmentTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/UpdateAssessmentTarget)
