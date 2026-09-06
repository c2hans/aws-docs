---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListSamples.html
---

# ListSamples
<a name="API_ListSamples"></a>

Gets information about samples, given an AWS Device Farm job ARN.

## Request Syntax
<a name="API_ListSamples_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSamples_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_ListSamples_RequestSyntax) **   <a name="devicefarm-ListSamples-request-arn"></a>
The Amazon Resource Name (ARN) of the job used to list samples.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [nextToken](#API_ListSamples_RequestSyntax) **   <a name="devicefarm-ListSamples-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListSamples_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "samples": [
      {
         "arn": "string",
         "type": "string",
         "url": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSamples_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSamples_ResponseSyntax) **   <a name="devicefarm-ListSamples-response-nextToken"></a>
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

 ** [samples](#API_ListSamples_ResponseSyntax) **   <a name="devicefarm-ListSamples-response-samples"></a>
Information about the samples.
Type: Array of [Sample](API_Sample.md) objects

## Errors
<a name="API_ListSamples_Errors"></a>

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
<a name="API_ListSamples_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListSamples)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListSamples)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListSamples)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListSamples)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListSamples)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListSamples)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListSamples)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListSamples)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListSamples)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListSamples)
