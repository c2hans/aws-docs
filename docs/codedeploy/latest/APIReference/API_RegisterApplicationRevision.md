---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RegisterApplicationRevision.html
---

# RegisterApplicationRevision
<a name="API_RegisterApplicationRevision"></a>

Registers with AWS CodeDeploy a revision for the specified application.

## Request Syntax
<a name="API_RegisterApplicationRevision_RequestSyntax"></a>

```
{
   "applicationName": "{{string}}",
   "description": "{{string}}",
   "revision": {
      "appSpecContent": {
         "content": "{{string}}",
         "sha256": "{{string}}"
      },
      "gitHubLocation": {
         "commitId": "{{string}}",
         "repository": "{{string}}"
      },
      "revisionType": "{{string}}",
      "s3Location": {
         "bucket": "{{string}}",
         "bundleType": "{{string}}",
         "eTag": "{{string}}",
         "key": "{{string}}",
         "version": "{{string}}"
      },
      "string": {
         "content": "{{string}}",
         "sha256": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_RegisterApplicationRevision_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationName](#API_RegisterApplicationRevision_RequestSyntax) **   <a name="CodeDeploy-RegisterApplicationRevision-request-applicationName"></a>
The name of an AWS CodeDeploy application associated with the user or AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: Yes

 ** [description](#API_RegisterApplicationRevision_RequestSyntax) **   <a name="CodeDeploy-RegisterApplicationRevision-request-description"></a>
A comment about the revision.
Type: String
Required: No

 ** [revision](#API_RegisterApplicationRevision_RequestSyntax) **   <a name="CodeDeploy-RegisterApplicationRevision-request-revision"></a>
Information about the application revision to register, including type and location.
Type: [RevisionLocation](API_RevisionLocation.md) object
Required: Yes

## Response Elements
<a name="API_RegisterApplicationRevision_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RegisterApplicationRevision_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** DescriptionTooLongException **
The description is too long.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidRevisionException **
The revision was specified in an invalid format.
HTTP Status Code: 400

 ** RevisionRequiredException **
The revision ID was not specified.
HTTP Status Code: 400

## Examples
<a name="API_RegisterApplicationRevision_Examples"></a>

### Example
<a name="API_RegisterApplicationRevision_Example_1"></a>

This example illustrates one usage of RegisterApplicationRevision.

#### Sample Request
<a name="API_RegisterApplicationRevision_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 257
X-Amz-Target: CodeDeploy_20141006.RegisterApplicationRevision
X-Amz-Date: 20160707T024712Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "applicationName": "TestApp-us-east-1",
    "description": "New application registration",
    "revision": {
        "revisionType": "S3",
        "s3Location": {
            "bundleType": "zip",
            "eTag": "3fdd7b9196697a044d5af1d649e26a4a",
            "bucket": "project-1234",
            "key": "South-App.zip"
        }
    }
}
```

#### Sample Response
<a name="API_RegisterApplicationRevision_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 4ccc9cf0-88c9-11e5-8ce3-2704437d0309
Content-Type: application/x-amz-json-1.1
Content-Length: 0
```

## See Also
<a name="API_RegisterApplicationRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/RegisterApplicationRevision)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/RegisterApplicationRevision)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/RegisterApplicationRevision)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/RegisterApplicationRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/RegisterApplicationRevision)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/RegisterApplicationRevision)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/RegisterApplicationRevision)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/RegisterApplicationRevision)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/RegisterApplicationRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/RegisterApplicationRevision)
