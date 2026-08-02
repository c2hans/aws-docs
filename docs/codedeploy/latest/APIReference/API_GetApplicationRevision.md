---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetApplicationRevision.html
---

# GetApplicationRevision
<a name="API_GetApplicationRevision"></a>

Gets information about an application revision.

## Request Syntax
<a name="API_GetApplicationRevision_RequestSyntax"></a>

```
{
   "applicationName": "{{string}}",
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
<a name="API_GetApplicationRevision_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationName](#API_GetApplicationRevision_RequestSyntax) **   <a name="CodeDeploy-GetApplicationRevision-request-applicationName"></a>
The name of the application that corresponds to the revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [revision](#API_GetApplicationRevision_RequestSyntax) **   <a name="CodeDeploy-GetApplicationRevision-request-revision"></a>
Information about the application revision to get, including type and location.
Type: [RevisionLocation](API_RevisionLocation.md) object
Required: Yes

## Response Syntax
<a name="API_GetApplicationRevision_ResponseSyntax"></a>

```
{
   "applicationName": "string",
   "revision": {
      "appSpecContent": {
         "content": "string",
         "sha256": "string"
      },
      "gitHubLocation": {
         "commitId": "string",
         "repository": "string"
      },
      "revisionType": "string",
      "s3Location": {
         "bucket": "string",
         "bundleType": "string",
         "eTag": "string",
         "key": "string",
         "version": "string"
      },
      "string": {
         "content": "string",
         "sha256": "string"
      }
   },
   "revisionInfo": {
      "deploymentGroups": [ "string" ],
      "description": "string",
      "firstUsedTime": number,
      "lastUsedTime": number,
      "registerTime": number
   }
}
```

## Response Elements
<a name="API_GetApplicationRevision_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationName](#API_GetApplicationRevision_ResponseSyntax) **   <a name="CodeDeploy-GetApplicationRevision-response-applicationName"></a>
The name of the application that corresponds to the revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [revision](#API_GetApplicationRevision_ResponseSyntax) **   <a name="CodeDeploy-GetApplicationRevision-response-revision"></a>
Additional information about the revision, including type and location.
Type: [RevisionLocation](API_RevisionLocation.md) object

 ** [revisionInfo](#API_GetApplicationRevision_ResponseSyntax) **   <a name="CodeDeploy-GetApplicationRevision-response-revisionInfo"></a>
General information about the revision.
Type: [GenericRevisionInfo](API_GenericRevisionInfo.md) object

## Errors
<a name="API_GetApplicationRevision_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidRevisionException **
The revision was specified in an invalid format.
HTTP Status Code: 400

 ** RevisionDoesNotExistException **
The named revision does not exist with the user or AWS account.
HTTP Status Code: 400

 ** RevisionRequiredException **
The revision ID was not specified.
HTTP Status Code: 400

## Examples
<a name="API_GetApplicationRevision_Examples"></a>

### Example
<a name="API_GetApplicationRevision_Example_1"></a>

This example illustrates one usage of GetApplicationRevision.

#### Sample Request
<a name="API_GetApplicationRevision_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 215
X-Amz-Target: CodeDeploy_20141006.GetApplicationRevision
X-Amz-Date: 20160707T015403Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "applicationName": "TestApp-us-east-1",
    "revision": {
        "revisionType": "S3",
        "s3Location": {
            "bundleType": "zip",
            "eTag": "fff9102ckv48b652bf903700453f7408",
            "bucket": "project-1234",
            "key": "North-App.zip"
        }
    }
}
```

#### Sample Response
<a name="API_GetApplicationRevision_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 410338f8-88e0-11e5-bb59-fb8eade0dfc3
Content-Type: application/x-amz-json-1.1
Content-Length: 416

{
    "applicationName": "TestApp-us-east-1",
    "revision": {
        "revisionType": "S3",
        "s3Location": {
            "bucket": "project-1234",
            "bundleType": "zip",
            "eTag": "abc9102cff48b652bf903765453f7408",
            "key": "North-App.zip"
        }
    },
    "revisionInfo": {
        "deploymentGroups": [],
        "description": "Application revision registered by Deployment ID: d-D1EGTDV3C",
        "firstUsedTime": 1446232255.734,
        "lastUsedTime": 1446232255.734,
        "registerTime": 1446232255.734
    }
}
```

## See Also
<a name="API_GetApplicationRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/GetApplicationRevision)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/GetApplicationRevision)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/GetApplicationRevision)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/GetApplicationRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/GetApplicationRevision)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/GetApplicationRevision)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/GetApplicationRevision)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/GetApplicationRevision)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/GetApplicationRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/GetApplicationRevision)
