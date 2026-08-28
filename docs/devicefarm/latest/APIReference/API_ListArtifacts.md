---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListArtifacts.html
---

# ListArtifacts
<a name="API_ListArtifacts"></a>

Gets information about artifacts.

## Request Syntax
<a name="API_ListArtifacts_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "nextToken": "{{string}}",
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListArtifacts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_ListArtifacts_RequestSyntax) **   <a name="devicefarm-ListArtifacts-request-arn"></a>
The run, job, suite, or test ARN.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [nextToken](#API_ListArtifacts_RequestSyntax) **   <a name="devicefarm-ListArtifacts-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

 ** [type](#API_ListArtifacts_RequestSyntax) **   <a name="devicefarm-ListArtifacts-request-type"></a>
The artifacts' type.
Allowed values include:
+ FILE
+ LOG
+ SCREENSHOT
Type: String
Valid Values: `SCREENSHOT | FILE | LOG`
Required: Yes

## Response Syntax
<a name="API_ListArtifacts_ResponseSyntax"></a>

```
{
   "artifacts": [
      {
         "arn": "string",
         "extension": "string",
         "name": "string",
         "type": "string",
         "url": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListArtifacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [artifacts](#API_ListArtifacts_ResponseSyntax) **   <a name="devicefarm-ListArtifacts-response-artifacts"></a>
Information about the artifacts.
Type: Array of [Artifact](API_Artifact.md) objects

 ** [nextToken](#API_ListArtifacts_ResponseSyntax) **   <a name="devicefarm-ListArtifacts-response-nextToken"></a>
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

## Errors
<a name="API_ListArtifacts_Errors"></a>

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
<a name="API_ListArtifacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListArtifacts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListArtifacts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListArtifacts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListArtifacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListArtifacts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListArtifacts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListArtifacts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListArtifacts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListArtifacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListArtifacts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
