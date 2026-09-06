---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListAssessmentRuns.html
---

# ListAssessmentRuns
<a name="API_ListAssessmentRuns"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Lists the assessment runs that correspond to the assessment templates that are specified by the ARNs of the assessment templates.

## Request Syntax
<a name="API_ListAssessmentRuns_RequestSyntax"></a>

```
{
   "assessmentTemplateArns": [ "{{string}}" ],
   "filter": {
      "completionTimeRange": {
         "beginDate": {{number}},
         "endDate": {{number}}
      },
      "durationRange": {
         "maxSeconds": {{number}},
         "minSeconds": {{number}}
      },
      "namePattern": "{{string}}",
      "rulesPackageArns": [ "{{string}}" ],
      "startTimeRange": {
         "beginDate": {{number}},
         "endDate": {{number}}
      },
      "stateChangeTimeRange": {
         "beginDate": {{number}},
         "endDate": {{number}}
      },
      "states": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAssessmentRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [assessmentTemplateArns](#API_ListAssessmentRuns_RequestSyntax) **   <a name="Inspector-ListAssessmentRuns-request-assessmentTemplateArns"></a>
The ARNs that specify the assessment templates whose assessment runs you want to list.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** [filter](#API_ListAssessmentRuns_RequestSyntax) **   <a name="Inspector-ListAssessmentRuns-request-filter"></a>
You can use this parameter to specify a subset of data to be included in the action's response.
For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
Type: [AssessmentRunFilter](API_AssessmentRunFilter.md) object
Required: No

 ** [maxResults](#API_ListAssessmentRuns_RequestSyntax) **   <a name="Inspector-ListAssessmentRuns-request-maxResults"></a>
You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 10. The maximum value is 500.
Type: Integer
Required: No

 ** [nextToken](#API_ListAssessmentRuns_RequestSyntax) **   <a name="Inspector-ListAssessmentRuns-request-nextToken"></a>
You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListAssessmentRuns** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## Response Syntax
<a name="API_ListAssessmentRuns_ResponseSyntax"></a>

```
{
   "assessmentRunArns": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssessmentRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentRunArns](#API_ListAssessmentRuns_ResponseSyntax) **   <a name="Inspector-ListAssessmentRuns-response-assessmentRunArns"></a>
A list of ARNs that specifies the assessment runs that are returned by the action.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [nextToken](#API_ListAssessmentRuns_ResponseSyntax) **   <a name="Inspector-ListAssessmentRuns-response-nextToken"></a>
 When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

## Errors
<a name="API_ListAssessmentRuns_Errors"></a>

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

## Examples
<a name="API_ListAssessmentRuns_Examples"></a>

### Example
<a name="API_ListAssessmentRuns_Example_1"></a>

This example illustrates one usage of ListAssessmentRuns.

#### Sample Request
<a name="API_ListAssessmentRuns_Example_1_Request"></a>

```

               POST / HTTP/1.1
               Host: inspector.us-west-2.amazonaws.com
               Accept-Encoding: identity
               Content-Length: 2
               X-Amz-Target: InspectorService.ListAssessmentRuns
               X-Amz-Date: 20160323T194135Z
               User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
               Content-Type: application/x-amz-json-1.1
               Authorization: AUTHPARAMS
               {}
```

#### Sample Response
<a name="API_ListAssessmentRuns_Example_1_Response"></a>

```

               HTTP/1.1 200 OK
               x-amzn-RequestId: 410dabf6-f12f-11e5-8b5a-810259c0c3ae
               Content-Type: application/x-amz-json-1.1
               Content-Length: 215
               Date: Wed, 23 Mar 2016 19:41:36 GMT
               {
                  "assessmentRunArns":
                  [
                  "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE",
                  "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-v5D6fI3v"
                  ]
               }
```

## See Also
<a name="API_ListAssessmentRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/ListAssessmentRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/ListAssessmentRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/ListAssessmentRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/ListAssessmentRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ListAssessmentRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/ListAssessmentRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/ListAssessmentRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/ListAssessmentRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListAssessmentRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/ListAssessmentRuns)
