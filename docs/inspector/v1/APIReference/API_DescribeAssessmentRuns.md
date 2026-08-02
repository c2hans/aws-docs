---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeAssessmentRuns.html
---

# DescribeAssessmentRuns
<a name="API_DescribeAssessmentRuns"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Describes the assessment runs that are specified by the ARNs of the assessment runs.

## Request Syntax
<a name="API_DescribeAssessmentRuns_RequestSyntax"></a>

```
{
   "assessmentRunArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeAssessmentRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [assessmentRunArns](#API_DescribeAssessmentRuns_RequestSyntax) **   <a name="Inspector-DescribeAssessmentRuns-request-assessmentRunArns"></a>
The ARN that specifies the assessment run that you want to describe.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Syntax
<a name="API_DescribeAssessmentRuns_ResponseSyntax"></a>

```
{
   "assessmentRuns": [
      {
         "arn": "string",
         "assessmentTemplateArn": "string",
         "completedAt": number,
         "createdAt": number,
         "dataCollected": boolean,
         "durationInSeconds": number,
         "findingCounts": {
            "string" : number
         },
         "name": "string",
         "notifications": [
            {
               "date": number,
               "error": boolean,
               "event": "string",
               "message": "string",
               "snsPublishStatusCode": "string",
               "snsTopicArn": "string"
            }
         ],
         "rulesPackageArns": [ "string" ],
         "startedAt": number,
         "state": "string",
         "stateChangedAt": number,
         "stateChanges": [
            {
               "state": "string",
               "stateChangedAt": number
            }
         ],
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
<a name="API_DescribeAssessmentRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentRuns](#API_DescribeAssessmentRuns_ResponseSyntax) **   <a name="Inspector-DescribeAssessmentRuns-response-assessmentRuns"></a>
Information about the assessment run.
Type: Array of [AssessmentRun](API_AssessmentRun.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [failedItems](#API_DescribeAssessmentRuns_ResponseSyntax) **   <a name="Inspector-DescribeAssessmentRuns-response-failedItems"></a>
Assessment run details that cannot be described. An error code is provided for each failed item.
Type: String to [FailedItemDetails](API_FailedItemDetails.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 300.

## Errors
<a name="API_DescribeAssessmentRuns_Errors"></a>

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
<a name="API_DescribeAssessmentRuns_Examples"></a>

### Example
<a name="API_DescribeAssessmentRuns_Example_1"></a>

This example illustrates one usage of DescribeAssessmentRuns.

#### Sample Request
<a name="API_DescribeAssessmentRuns_Example_1_Request"></a>

```

               Host: inspector.us-west-2.amazonaws.com
               Accept-Encoding: identity
               Content-Length: 120
               X-Amz-Target: InspectorService.DescribeAssessmentRuns
               X-Amz-Date: 20160323T213431Z
               User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
               Content-Type: application/x-amz-json-1.1
               Authorization: AUTHPARAMS
               {
                 "assessmentRunArns": [
                   "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE"
                 ]
               }
```

#### Sample Response
<a name="API_DescribeAssessmentRuns_Example_1_Response"></a>

```

               HTTP/1.1 200 OK
               x-amzn-RequestId: 0834f495-f13f-11e5-8a9a-395a36305628
               Content-Type: application/x-amz-json-1.1
               Content-Length: 1156
               Date: Wed, 23 Mar 2016 21:34:32 GMT
               {
                 "assessmentRuns": [
                   {
                     "arn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE",
                     "assessmentTemplateArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw",
                     "completedAt": 1458680301.4,
                     "createdAt": 1458680170.035,
                     "dataCollected": true,
                     "durationInSeconds": 3600,
                     "name": "Run 1 for ExampleAssessmentTemplate",
                     "notifications": [],
                     "rulesPackageArns": [
                       "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP"
                     ],
                     "startedAt": 1458680170.161,
                     "state": "COMPLETED",
                     "stateChangedAt": 1458680301.4,
                     "stateChanges": [
                       {
                         "state": "CREATED",
                         "stateChangedAt": 1458680170.035
                       },
                       {
                         "state": "START_DATA_COLLECTION_PENDING",
                         "stateChangedAt": 1458680170.065
                       },
                       {
                         "state": "START_DATA_COLLECTION_IN_PROGRESS",
                         "stateChangedAt": 1458680170.096
                       },
                       {
                         "state": "COLLECTING_DATA",
                         "stateChangedAt": 1458680170.161
                       },
                       {
                         "state": "STOP_DATA_COLLECTION_PENDING",
                         "stateChangedAt": 1458680239.883
                       },
                       {
                         "state": "DATA_COLLECTED",
                         "stateChangedAt": 1458680299.847
                       },
                       {
                         "state": "EVALUATING_RULES",
                         "stateChangedAt": 1458680300.099
                       },
                       {
                         "state": "COMPLETED",
                         "stateChangedAt": 1458680301.4
                       }
                     ],
                     "userAttributesForFindings": []
                   }
                 ],
                 "failedItems": {}
               }
```

## See Also
<a name="API_DescribeAssessmentRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/DescribeAssessmentRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/DescribeAssessmentRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/DescribeAssessmentRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/DescribeAssessmentRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/DescribeAssessmentRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/DescribeAssessmentRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/DescribeAssessmentRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/DescribeAssessmentRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/DescribeAssessmentRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/DescribeAssessmentRuns)
