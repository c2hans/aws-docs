---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListWorkflowTypes.html
---

# ListWorkflowTypes
<a name="API_ListWorkflowTypes"></a>

Returns information about workflow types in the specified domain. The results may be split into multiple pages that can be retrieved by making the call repeatedly.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ You cannot use an IAM policy to constrain this action's parameters.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_ListWorkflowTypes_RequestSyntax"></a>

```
{
   "domain": "{{string}}",
   "maximumPageSize": {{number}},
   "name": "{{string}}",
   "nextPageToken": "{{string}}",
   "registrationStatus": "{{string}}",
   "reverseOrder": {{boolean}}
}
```

## Request Parameters
<a name="API_ListWorkflowTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domain](#API_ListWorkflowTypes_RequestSyntax) **   <a name="SWF-ListWorkflowTypes-request-domain"></a>
The name of the domain in which the workflow types have been registered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [maximumPageSize](#API_ListWorkflowTypes_RequestSyntax) **   <a name="SWF-ListWorkflowTypes-request-maximumPageSize"></a>
The maximum number of results that are returned per call. Use `nextPageToken` to obtain further pages of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [name](#API_ListWorkflowTypes_RequestSyntax) **   <a name="SWF-ListWorkflowTypes-request-name"></a>
If specified, lists the workflow type with this name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [nextPageToken](#API_ListWorkflowTypes_RequestSyntax) **   <a name="SWF-ListWorkflowTypes-request-nextPageToken"></a>
If `NextPageToken` is returned there are more results available. The value of `NextPageToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a `400` error: "`Specified token has exceeded its maximum lifetime`".
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [registrationStatus](#API_ListWorkflowTypes_RequestSyntax) **   <a name="SWF-ListWorkflowTypes-request-registrationStatus"></a>
Specifies the registration status of the workflow types to list.
Type: String
Valid Values: `REGISTERED | DEPRECATED`
Required: Yes

 ** [reverseOrder](#API_ListWorkflowTypes_RequestSyntax) **   <a name="SWF-ListWorkflowTypes-request-reverseOrder"></a>
When set to `true`, returns the results in reverse order. By default the results are returned in ascending alphabetical order of the `name` of the workflow types.
Type: Boolean
Required: No

## Response Syntax
<a name="API_ListWorkflowTypes_ResponseSyntax"></a>

```
{
   "nextPageToken": "string",
   "typeInfos": [
      {
         "creationDate": number,
         "deprecationDate": number,
         "description": "string",
         "status": "string",
         "workflowType": {
            "name": "string",
            "version": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkflowTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextPageToken](#API_ListWorkflowTypes_ResponseSyntax) **   <a name="SWF-ListWorkflowTypes-response-nextPageToken"></a>
If a `NextPageToken` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in `nextPageToken`. Keep all other arguments unchanged.
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.

 ** [typeInfos](#API_ListWorkflowTypes_ResponseSyntax) **   <a name="SWF-ListWorkflowTypes-response-typeInfos"></a>
The list of workflow type information.
Type: Array of [WorkflowTypeInfo](API_WorkflowTypeInfo.md) objects

## Errors
<a name="API_ListWorkflowTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedFault **
Returned when the caller doesn't have sufficient permissions to invoke the action.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** UnknownResourceFault **
Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

## Examples
<a name="API_ListWorkflowTypes_Examples"></a>

### ListWorkflowTypes Example
<a name="API_ListWorkflowTypes_Example_1"></a>

This example illustrates one usage of ListWorkflowTypes.

#### Sample Request
<a name="API_ListWorkflowTypes_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: swf.us-east-1.amazonaws.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.25) Gecko/20111212 Firefox/3.6.25 ( .NET CLR 3.5.30729; .NET4.0E)
Accept: application/json, text/javascript, */*
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
Content-Type: application/x-amz-json-1.0
X-Requested-With: XMLHttpRequest
X-Amz-Date: Sun, 15 Jan 2012 22:25:43 GMT
X-Amz-Target: SimpleWorkflowService.ListWorkflowTypes
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=uleWQSyVVf0+aG50IoBJG5h0hzxNFNT97Mkn/FSCQ+Q=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 110
Pragma: no-cache
Cache-Control: no-cache

{"domain": "867530901",
"registrationStatus": "REGISTERED",
"maximumPageSize": 50,
"reverseOrder": true}
```

#### Sample Response
<a name="API_ListWorkflowTypes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 174
Content-Type: application/json
x-amzn-RequestId: dcde6719-3fc7-11e1-9e8f-57bb03e21482

{"typeInfos":
[
{"creationDate": 1326481174.027,
"description": "Handle customer orders",
"status": "REGISTERED",
"workflowType":
{"name": "customerOrderWorkflow",
"version": "1.0"}
}
]
}
```

## See Also
<a name="API_ListWorkflowTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/ListWorkflowTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/ListWorkflowTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ListWorkflowTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/ListWorkflowTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ListWorkflowTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/ListWorkflowTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/ListWorkflowTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/ListWorkflowTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/ListWorkflowTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ListWorkflowTypes)
