---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeAssessmentTemplates.html
---

# DescribeAssessmentTemplates
<a name="API_DescribeAssessmentTemplates"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Describes the assessment templates that are specified by the ARNs of the assessment templates.

## Request Syntax
<a name="API_DescribeAssessmentTemplates_RequestSyntax"></a>

```
{
   "assessmentTemplateArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeAssessmentTemplates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [assessmentTemplateArns](#API_DescribeAssessmentTemplates_RequestSyntax) **   <a name="Inspector-DescribeAssessmentTemplates-request-assessmentTemplateArns"></a>
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Syntax
<a name="API_DescribeAssessmentTemplates_ResponseSyntax"></a>

```
{
   "assessmentTemplates": [
      {
         "arn": "string",
         "assessmentRunCount": number,
         "assessmentTargetArn": "string",
         "createdAt": number,
         "durationInSeconds": number,
         "lastAssessmentRunArn": "string",
         "name": "string",
         "rulesPackageArns": [ "string" ],
         "userAttributesForFindings": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ],
   "failedItems": {
      "string" : {
         "failureCode": "string",
         "retryable": boolean
      }
   }
}
```

## Response Elements
<a name="API_DescribeAssessmentTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentTemplates](#API_DescribeAssessmentTemplates_ResponseSyntax) **   <a name="Inspector-DescribeAssessmentTemplates-response-assessmentTemplates"></a>
Information about the assessment templates.
Type: Array of [AssessmentTemplate](API_AssessmentTemplate.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [failedItems](#API_DescribeAssessmentTemplates_ResponseSyntax) **   <a name="Inspector-DescribeAssessmentTemplates-response-failedItems"></a>
Assessment template details that cannot be described. An error code is provided for each failed item.
Type: String to [FailedItemDetails](API_FailedItemDetails.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 300.

## Errors
<a name="API_DescribeAssessmentTemplates_Errors"></a>

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

## Examples
<a name="API_DescribeAssessmentTemplates_Examples"></a>

### Example
<a name="API_DescribeAssessmentTemplates_Example_1"></a>

This example illustrates one usage of DescribeAssessmentTemplates.

#### Sample Request
<a name="API_DescribeAssessmentTemplates_Example_1_Request"></a>

```

               POST / HTTP/1.1
               Host: inspector.us-west-2.amazonaws.com
               Accept-Encoding: identity
               Content-Length: 110
               X-Amz-Target: InspectorService.DescribeAssessmentTemplates
               X-Amz-Date: 20160323T214822Z
               User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
               Content-Type: application/x-amz-json-1.1
               Authorization: AUTHPARAMS
               {
                 "assessmentTemplateArns": [
                   "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw"
                 ]
               }
```

#### Sample Response
<a name="API_DescribeAssessmentTemplates_Example_1_Response"></a>

```

               HTTP/1.1 200 OK
               x-amzn-RequestId: f73a449b-f140-11e5-b473-ed8493878c40
               Content-Type: application/x-amz-json-1.1
               Content-Length: 422
               Date: Wed, 23 Mar 2016 21:48:23 GMT
               {
                 "assessmentTemplates": [
                   {
                     "arn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw",
                     "assessmentTargetArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq",
                     "createdAt": 1458074191.844,
                     "durationInSeconds": 3600,
                     "name": "ExampleAssessmentTemplate",
                     "rulesPackageArns": [
                       "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP"
                     ],
                     "userAttributesForFindings": []
                   }
                 ],
                 "failedItems": {}
               }
```

## See Also
<a name="API_DescribeAssessmentTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/DescribeAssessmentTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/DescribeAssessmentTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/DescribeAssessmentTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/DescribeAssessmentTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/DescribeAssessmentTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/DescribeAssessmentTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/DescribeAssessmentTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/DescribeAssessmentTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/DescribeAssessmentTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/DescribeAssessmentTemplates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
