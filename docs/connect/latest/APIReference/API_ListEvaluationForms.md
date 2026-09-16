---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListEvaluationForms.html
---

# ListEvaluationForms
<a name="API_ListEvaluationForms"></a>

Lists evaluation forms in the specified Connect Customer instance.

## Request Syntax
<a name="API_ListEvaluationForms_RequestSyntax"></a>

```
GET /evaluation-forms/{{InstanceId}}?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEvaluationForms_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListEvaluationForms_RequestSyntax) **   <a name="connect-ListEvaluationForms-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListEvaluationForms_RequestSyntax) **   <a name="connect-ListEvaluationForms-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListEvaluationForms_RequestSyntax) **   <a name="connect-ListEvaluationForms-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListEvaluationForms_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEvaluationForms_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EvaluationFormSummaryList": [
      {
         "ActiveVersion": number,
         "CreatedBy": "string",
         "CreatedTime": number,
         "EvaluationFormArn": "string",
         "EvaluationFormId": "string",
         "LastActivatedBy": "string",
         "LastActivatedTime": number,
         "LastModifiedBy": "string",
         "LastModifiedTime": number,
         "LatestVersion": number,
         "Title": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEvaluationForms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationFormSummaryList](#API_ListEvaluationForms_ResponseSyntax) **   <a name="connect-ListEvaluationForms-response-EvaluationFormSummaryList"></a>
Provides details about a list of evaluation forms belonging to an instance.
Type: Array of [EvaluationFormSummary](API_EvaluationFormSummary.md) objects

 ** [NextToken](#API_ListEvaluationForms_ResponseSyntax) **   <a name="connect-ListEvaluationForms-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListEvaluationForms_Errors"></a>

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
<a name="API_ListEvaluationForms_Examples"></a>

### Example
<a name="API_ListEvaluationForms_Example_1"></a>

The following example lists all the evaluation forms in an instance. It returns up to 2 results.

#### Sample Request
<a name="API_ListEvaluationForms_Example_1_Request"></a>

```
{
   "InstanceId": "[instance_id]",
   "MaxResults": 2
}
```

#### Sample Response
<a name="API_ListEvaluationForms_Example_1_Response"></a>

```
{
   "EvaluationFormSummaryList": [
      {
         "EvaluationFormId": "[evaluation_form_id]",
         "EvaluationFormArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/evaluation-form/[evaluation_form_id]",
         "Title": "form-title",
         "CreatedTime": "2023-05-04T00:24:01.490000-07:00",
         "CreatedBy": "arn:aws:sts::[account_id]:assumed-role/Admin/username",
         "LastModifiedTime": "2023-05-04T00:24:01.490000-07:00",
         "LastModifiedBy": "arn:aws:sts::[account_id]:assumed-role/Admin/username",
         "LatestVersion": 1
      },
      {
         "EvaluationFormId": "[evaluation_form_id]",
         "EvaluationFormArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/evaluation-form/[evaluation_form_id]",
         "Title": "form-title",
         "CreatedTime": "2023-05-04T00:23:55.047000-07:00",
         "CreatedBy": "arn:aws:sts::[account_id]:assumed-role/Admin/username",
         "LastModifiedTime": "2023-05-04T00:23:55.047000-07:00",
         "LastModifiedBy": "arn:aws:sts::[account_id]:assumed-role/Admin/username",
         "LatestVersion": 1
      }
   ],
   "NextToken": "QH7ftooIJZMpObgG6DlPwu/AAABGTCCARUGCSqGSIb"
}
```

## See Also
<a name="API_ListEvaluationForms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListEvaluationForms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListEvaluationForms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListEvaluationForms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListEvaluationForms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListEvaluationForms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListEvaluationForms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListEvaluationForms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListEvaluationForms)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListEvaluationForms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListEvaluationForms)
