---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListEvaluationFormVersions.html
---

# ListEvaluationFormVersions
<a name="API_ListEvaluationFormVersions"></a>

Lists versions of an evaluation form in the specified Connect Customer instance.

## Request Syntax
<a name="API_ListEvaluationFormVersions_RequestSyntax"></a>

```
GET /evaluation-forms/{{InstanceId}}/{{EvaluationFormId}}/versions?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEvaluationFormVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EvaluationFormId](#API_ListEvaluationFormVersions_RequestSyntax) **   <a name="connect-ListEvaluationFormVersions-request-uri-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [InstanceId](#API_ListEvaluationFormVersions_RequestSyntax) **   <a name="connect-ListEvaluationFormVersions-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListEvaluationFormVersions_RequestSyntax) **   <a name="connect-ListEvaluationFormVersions-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListEvaluationFormVersions_RequestSyntax) **   <a name="connect-ListEvaluationFormVersions-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListEvaluationFormVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEvaluationFormVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EvaluationFormVersionSummaryList": [
      {
         "CreatedBy": "string",
         "CreatedTime": number,
         "EvaluationFormArn": "string",
         "EvaluationFormId": "string",
         "EvaluationFormVersion": number,
         "LastModifiedBy": "string",
         "LastModifiedTime": number,
         "Locked": boolean,
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEvaluationFormVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationFormVersionSummaryList](#API_ListEvaluationFormVersions_ResponseSyntax) **   <a name="connect-ListEvaluationFormVersions-response-EvaluationFormVersionSummaryList"></a>
Provides details about a list of evaluation forms belonging to an instance.
Type: Array of [EvaluationFormVersionSummary](API_EvaluationFormVersionSummary.md) objects

 ** [NextToken](#API_ListEvaluationFormVersions_ResponseSyntax) **   <a name="connect-ListEvaluationFormVersions-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListEvaluationFormVersions_Errors"></a>

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
<a name="API_ListEvaluationFormVersions_Examples"></a>

### Example
<a name="API_ListEvaluationFormVersions_Example_1"></a>

The following example lists the versions of an evaluation form. It returns up to 2 results.

#### Sample Request
<a name="API_ListEvaluationFormVersions_Example_1_Request"></a>

```
{
   "InstanceId": "[instance_id]",
   "EvaluationFormId": "[evaluation_form_id]",
   "MaxResults": 2
}
```

#### Sample Response
<a name="API_ListEvaluationFormVersions_Example_1_Response"></a>

```
{
   "EvaluationFormVersionSummaryList": [
      {
         "EvaluationFormArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/evaluation-form/[evaluation_form_id]",
         "EvaluationFormId": "[evaluation_form_id]",
         "EvaluationFormVersion": 1,
         "Locked": true,
         "Status": "DRAFT",
         "CreatedTime": "2023-05-04T00:24:01.490000-07:00",
         "CreatedBy": "arn:aws:sts::[account_id]:assumed-role/Admin/username",
         "LastModifiedTime": "2023-05-04T00:24:01.490000-07:00",
         "LastModifiedBy": "arn:aws:sts::[account_id]:assumed-role/Admin/username"
      },
      {
         "EvaluationFormArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/evaluation-form/[evaluation_form_id]",
         "EvaluationFormId": "[evaluation_form_id]",
         "EvaluationFormVersion": 2,
         "Locked": true,
         "Status": "DRAFT",
         "CreatedTime": "2023-05-04T00:31:11.923000-07:00",
         "CreatedBy": "arn:aws:sts::[account_id]:assumed-role/Admin/username",
         "LastModifiedTime": "2023-05-04T00:31:11.923000-07:00",
         "LastModifiedBy": "arn:aws:sts::[account_id]:assumed-role/Admin/username"
      }
   ],
   "NextToken": "ki3y3ZDTAKfGXYllAAAAqjCBpwYJKoZIhvcNAQcGoIGZ"
}
```

## See Also
<a name="API_ListEvaluationFormVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListEvaluationFormVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListEvaluationFormVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListEvaluationFormVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListEvaluationFormVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListEvaluationFormVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListEvaluationFormVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListEvaluationFormVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListEvaluationFormVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListEvaluationFormVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListEvaluationFormVersions)
