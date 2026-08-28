---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListDomains.html
---

# ListDomains
<a name="API_ListDomains"></a>

Returns the list of domains registered in the account. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.

**Note**
This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains. The element must be set to `arn:aws:swf::AccountID:domain/*`, where *AccountID* is the account ID, with no dashes.
+ Use an `Action` element to allow or deny permission to call this action.
+ You cannot use an IAM policy to constrain this action's parameters.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_ListDomains_RequestSyntax"></a>

```
{
   "maximumPageSize": {{number}},
   "nextPageToken": "{{string}}",
   "registrationStatus": "{{string}}",
   "reverseOrder": {{boolean}}
}
```

## Request Parameters
<a name="API_ListDomains_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maximumPageSize](#API_ListDomains_RequestSyntax) **   <a name="SWF-ListDomains-request-maximumPageSize"></a>
The maximum number of results that are returned per call. Use `nextPageToken` to obtain further pages of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextPageToken](#API_ListDomains_RequestSyntax) **   <a name="SWF-ListDomains-request-nextPageToken"></a>
If `NextPageToken` is returned there are more results available. The value of `NextPageToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a `400` error: "`Specified token has exceeded its maximum lifetime`".
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [registrationStatus](#API_ListDomains_RequestSyntax) **   <a name="SWF-ListDomains-request-registrationStatus"></a>
Specifies the registration status of the domains to list.
Type: String
Valid Values: `REGISTERED | DEPRECATED`
Required: Yes

 ** [reverseOrder](#API_ListDomains_RequestSyntax) **   <a name="SWF-ListDomains-request-reverseOrder"></a>
When set to `true`, returns the results in reverse order. By default, the results are returned in ascending alphabetical order by `name` of the domains.
Type: Boolean
Required: No

## Response Syntax
<a name="API_ListDomains_ResponseSyntax"></a>

```
{
   "domainInfos": [
      {
         "arn": "string",
         "description": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_ListDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainInfos](#API_ListDomains_ResponseSyntax) **   <a name="SWF-ListDomains-response-domainInfos"></a>
A list of DomainInfo structures.
Type: Array of [DomainInfo](API_DomainInfo.md) objects

 ** [nextPageToken](#API_ListDomains_ResponseSyntax) **   <a name="SWF-ListDomains-response-nextPageToken"></a>
If a `NextPageToken` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in `nextPageToken`. Keep all other arguments unchanged.
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.

## Errors
<a name="API_ListDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedFault **
Returned when the caller doesn't have sufficient permissions to invoke the action.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

## Examples
<a name="API_ListDomains_Examples"></a>

### ListDomains Example
<a name="API_ListDomains_Example_1"></a>

This example illustrates one usage of ListDomains.

#### Sample Request
<a name="API_ListDomains_Example_1_Request"></a>

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
X-Amz-Date: Sun, 15 Jan 2012 03:09:58 GMT
X-Amz-Target: SimpleWorkflowService.ListDomains
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=ZCprC72dUxF9ca3w/tbwKZ8lBQn0jaA4xOJqDF0uqMI=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 86
Pragma: no-cache
Cache-Control: no-cache

{"registrationStatus": "REGISTERED",
 "maximumPageSize": 50,
 "reverseOrder": false}
```

#### Sample Response
<a name="API_ListDomains_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 568
Content-Type: application/json
x-amzn-RequestId: 67e874cc-3f26-11e1-9b11-7182192d0b57

{"domainInfos":
  [
  {"description": "music", "name": "867530901", "status": "REGISTERED"},
  {"description": "music", "name": "867530902", "status": "REGISTERED"},
  {"description": "", "name": "Demo", "status": "REGISTERED"},
  {"description": "", "name": "DemoDomain", "status": "REGISTERED"},
  {"description": "", "name": "Samples", "status": "REGISTERED"},
  {"description": "", "name": "testDomain2", "status": "REGISTERED"},
  {"description": "", "name": "testDomain3", "status": "REGISTERED"},
  {"description": "", "name": "testDomain4", "status": "REGISTERED"},
  {"description": "", "name": "zsxfvgsxcv", "status": "REGISTERED"}
  ]
}
```

## See Also
<a name="API_ListDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/ListDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/ListDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ListDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/ListDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ListDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/ListDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/ListDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/ListDomains)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/ListDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ListDomains)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
