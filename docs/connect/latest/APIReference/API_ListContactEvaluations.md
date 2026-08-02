---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListContactEvaluations.html
---

# ListContactEvaluations
<a name="API_ListContactEvaluations"></a>

Lists contact evaluations in the specified Connect Customer instance.

## Request Syntax
<a name="API_ListContactEvaluations_RequestSyntax"></a>

```
GET /contact-evaluations/{{InstanceId}}?contactId={{ContactId}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListContactEvaluations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_ListContactEvaluations_RequestSyntax) **   <a name="connect-ListContactEvaluations-request-uri-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_ListContactEvaluations_RequestSyntax) **   <a name="connect-ListContactEvaluations-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [NextToken](#API_ListContactEvaluations_RequestSyntax) **   <a name="connect-ListContactEvaluations-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
This is not expected to be set because the value returned in the previous response is always null.

## Request Body
<a name="API_ListContactEvaluations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListContactEvaluations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EvaluationSummaryList": [
      {
         "Acknowledgement": {
            "AcknowledgedBy": "string",
            "AcknowledgedTime": number,
            "AcknowledgerComment": "string"
         },
         "AutoEvaluationEnabled": boolean,
         "AutoEvaluationStatus": "string",
         "CalibrationSessionId": "string",
         "ContactParticipant": {
            "ContactParticipantId": "string",
            "ContactParticipantRole": "string"
         },
         "CreatedTime": number,
         "EvaluationArn": "string",
         "EvaluationFormId": "string",
         "EvaluationFormTitle": "string",
         "EvaluationId": "string",
         "EvaluationType": "string",
         "EvaluatorArn": "string",
         "LastModifiedTime": number,
         "Score": {
            "AppliedWeight": number,
            "AutomaticFail": boolean,
            "EarnedPoints": number,
            "MaxBasePoint": number,
            "NotApplicable": boolean,
            "Percentage": number,
            "PerformanceCategory": "string"
         },
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContactEvaluations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationSummaryList](#API_ListContactEvaluations_ResponseSyntax) **   <a name="connect-ListContactEvaluations-response-EvaluationSummaryList"></a>
Provides details about a list of contact evaluations belonging to an instance.
Type: Array of [EvaluationSummary](API_EvaluationSummary.md) objects

 ** [NextToken](#API_ListContactEvaluations_ResponseSyntax) **   <a name="connect-ListContactEvaluations-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
This is always returned as null in the response.
Type: String

## Errors
<a name="API_ListContactEvaluations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_ListContactEvaluations_Examples"></a>

### Example
<a name="API_ListContactEvaluations_Example_1"></a>

The following example lists the contact evaluations for a contact.

#### Sample Request
<a name="API_ListContactEvaluations_Example_1_Request"></a>

```
{
   "InstanceId": "[instance_id]",
   "ContactId": "[contact_id]"
}
```

#### Sample Response
<a name="API_ListContactEvaluations_Example_1_Response"></a>

```
{
   "EvaluationSummaryList": [
      {
         "EvaluationId": "[evaluation_id]",
         "EvaluationArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/contact-evaluation/[evaluation_id]",
         "EvaluationFormTitle": "form-title",
         "EvaluationFormId": "[evaluation_form_id]",
         "Status": "DRAFT",
         "EvaluatorArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/agent/arn:aws:sts::[account_id]:assumed-role/Admin/username",
         "CreatedTime": "2023-05-04T01:16:29.693000-07:00",
         "LastModifiedTime": "2023-05-04T01:16:29.693000-07:00"
      },
   ]
}
```

## See Also
<a name="API_ListContactEvaluations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListContactEvaluations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListContactEvaluations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListContactEvaluations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListContactEvaluations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListContactEvaluations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListContactEvaluations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListContactEvaluations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListContactEvaluations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListContactEvaluations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListContactEvaluations)
