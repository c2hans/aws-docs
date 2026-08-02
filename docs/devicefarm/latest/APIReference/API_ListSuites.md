---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListSuites.html
---

# ListSuites
<a name="API_ListSuites"></a>

Gets information about test suites for a given job.

## Request Syntax
<a name="API_ListSuites_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSuites_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_ListSuites_RequestSyntax) **   <a name="devicefarm-ListSuites-request-arn"></a>
The job's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [nextToken](#API_ListSuites_RequestSyntax) **   <a name="devicefarm-ListSuites-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListSuites_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "suites": [
      {
         "arn": "string",
         "counters": {
            "errored": number,
            "failed": number,
            "passed": number,
            "skipped": number,
            "stopped": number,
            "total": number,
            "warned": number
         },
         "created": number,
         "deviceMinutes": {
            "metered": number,
            "total": number,
            "unmetered": number
         },
         "message": "string",
         "name": "string",
         "result": "string",
         "started": number,
         "status": "string",
         "stopped": number,
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSuites_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSuites_ResponseSyntax) **   <a name="devicefarm-ListSuites-response-nextToken"></a>
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

 ** [suites](#API_ListSuites_ResponseSyntax) **   <a name="devicefarm-ListSuites-response-suites"></a>
Information about the suites.
Type: Array of [Suite](API_Suite.md) objects

## Errors
<a name="API_ListSuites_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListSuites_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListSuites)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListSuites)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListSuites)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListSuites)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListSuites)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListSuites)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListSuites)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListSuites)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListSuites)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListSuites)
