---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListTaskTemplates.html
---

# ListTaskTemplates
<a name="API_ListTaskTemplates"></a>

Lists task templates for the specified Connect Customer instance.

## Request Syntax
<a name="API_ListTaskTemplates_RequestSyntax"></a>

```
GET /instance/{{InstanceId}}/task/template?maxResults={{MaxResults}}&name={{Name}}&nextToken={{NextToken}}&status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTaskTemplates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListTaskTemplates_RequestSyntax) **   <a name="connect-ListTaskTemplates-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListTaskTemplates_RequestSyntax) **   <a name="connect-ListTaskTemplates-request-uri-MaxResults"></a>
The maximum number of results to return per page.
It is not expected that you set this.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [Name](#API_ListTaskTemplates_RequestSyntax) **   <a name="connect-ListTaskTemplates-request-uri-Name"></a>
The name of the task template.
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [NextToken](#API_ListTaskTemplates_RequestSyntax) **   <a name="connect-ListTaskTemplates-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
It is not expected that you set this because the value returned in the previous response is always null.

 ** [Status](#API_ListTaskTemplates_RequestSyntax) **   <a name="connect-ListTaskTemplates-request-uri-Status"></a>
Marks a template as `ACTIVE` or `INACTIVE` for a task to refer to it. Tasks can only be created from `ACTIVE` templates. If a template is marked as `INACTIVE`, then a task that refers to this template cannot be created.
Valid Values: `ACTIVE | INACTIVE`

## Request Body
<a name="API_ListTaskTemplates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTaskTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TaskTemplates": [
      {
         "Arn": "string",
         "CreatedTime": number,
         "Description": "string",
         "Id": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTaskTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTaskTemplates_ResponseSyntax) **   <a name="connect-ListTaskTemplates-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
This is always returned as a null in the response.
Type: String

 ** [TaskTemplates](#API_ListTaskTemplates_ResponseSyntax) **   <a name="connect-ListTaskTemplates-response-TaskTemplates"></a>
Provides details about a list of task templates belonging to an instance.
Type: Array of [TaskTemplateMetadata](API_TaskTemplateMetadata.md) objects

## Errors
<a name="API_ListTaskTemplates_Errors"></a>

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

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListTaskTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListTaskTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListTaskTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListTaskTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListTaskTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListTaskTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListTaskTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListTaskTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListTaskTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListTaskTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListTaskTemplates)
