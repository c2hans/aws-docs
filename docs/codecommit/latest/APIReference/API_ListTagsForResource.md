---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Gets information about AWStags for a specified Amazon Resource Name (ARN) in AWS CodeCommit. For a list of valid resources in AWS CodeCommit, see [CodeCommit Resources and Operations](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats) in the* AWS CodeCommit User Guide*.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}",
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListTagsForResource_RequestSyntax) **   <a name="CodeCommit-ListTagsForResource-request-nextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Required: No

 ** [resourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="CodeCommit-ListTagsForResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource for which you want to get information about tags, if any.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTagsForResource_ResponseSyntax) **   <a name="CodeCommit-ListTagsForResource-response-nextToken"></a>
An enumeration token that allows the operation to batch the next results of the operation.
Type: String

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="CodeCommit-ListTagsForResource-response-tags"></a>
A list of tag key and value pairs associated with the specified resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** InvalidResourceArnException **
The value for the resource ARN is not valid. For more information about resources in AWS CodeCommit, see [CodeCommit Resources and Operations](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats) in the AWS CodeCommit User Guide.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** ResourceArnRequiredException **
A valid Amazon Resource Name (ARN) for an AWS CodeCommit resource is required. For a list of valid resources in AWS CodeCommit, see [CodeCommit Resources and Operations](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats) in the AWS CodeCommit User Guide.
HTTP Status Code: 400

## Examples
<a name="API_ListTagsForResource_Examples"></a>

### Example
<a name="API_ListTagsForResource_Example_1"></a>

This example illustrates one usage of ListTagsForResource.

#### Sample Request
<a name="API_ListTagsForResource_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: CodeCommit_20150413.ListTagsForResource
X-Amz-Date: 20190228T224019Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "resourceArn": "arn:aws:codecommit:us-east-2:123456789012:MySecretProjectRepo"
}
```

#### Sample Response
<a name="API_ListTagsForResource_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 81
Date: Thu, 28 Feb 2019 22:40:19 GMT

{
    "tags": {
        "Status": "Secret",
        "Team": "Saanvi"
    }
}
```

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ListTagsForResource)
