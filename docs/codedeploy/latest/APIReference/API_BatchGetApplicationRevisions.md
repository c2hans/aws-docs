---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetApplicationRevisions.html
---

# BatchGetApplicationRevisions
<a name="API_BatchGetApplicationRevisions"></a>

Gets information about one or more application revisions. The maximum number of application revisions that can be returned is 25.

## Request Syntax
<a name="API_BatchGetApplicationRevisions_RequestSyntax"></a>

```
{
   "applicationName": "{{string}}",
   "revisions": [
      {
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
   ]
}
```

## Request Parameters
<a name="API_BatchGetApplicationRevisions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationName](#API_BatchGetApplicationRevisions_RequestSyntax) **   <a name="CodeDeploy-BatchGetApplicationRevisions-request-applicationName"></a>
The name of an AWS CodeDeploy application about which to get revision information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [revisions](#API_BatchGetApplicationRevisions_RequestSyntax) **   <a name="CodeDeploy-BatchGetApplicationRevisions-request-revisions"></a>
An array of `RevisionLocation` objects that specify information to get about the application revisions, including type and location. The maximum number of `RevisionLocation` objects you can specify is 25.
Type: Array of [RevisionLocation](API_RevisionLocation.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchGetApplicationRevisions_ResponseSyntax"></a>

```
{
   "applicationName": "string",
   "errorMessage": "string",
   "revisions": [
      {
         "genericRevisionInfo": {
            "deploymentGroups": [ "string" ],
            "description": "string",
            "firstUsedTime": number,
            "lastUsedTime": number,
            "registerTime": number
         },
         "revisionLocation": {
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
         }
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetApplicationRevisions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationName](#API_BatchGetApplicationRevisions_ResponseSyntax) **   <a name="CodeDeploy-BatchGetApplicationRevisions-response-applicationName"></a>
The name of the application that corresponds to the revisions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [errorMessage](#API_BatchGetApplicationRevisions_ResponseSyntax) **   <a name="CodeDeploy-BatchGetApplicationRevisions-response-errorMessage"></a>
Information about errors that might have occurred during the API call.
Type: String

 ** [revisions](#API_BatchGetApplicationRevisions_ResponseSyntax) **   <a name="CodeDeploy-BatchGetApplicationRevisions-response-revisions"></a>
Additional information about the revisions, including the type and location.
Type: Array of [RevisionInfo](API_RevisionInfo.md) objects

## Errors
<a name="API_BatchGetApplicationRevisions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** BatchLimitExceededException **
The maximum number of names or IDs allowed for this request (100) was exceeded.
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
<a name="API_BatchGetApplicationRevisions_Examples"></a>

### Example
<a name="API_BatchGetApplicationRevisions_Example_1"></a>

This example illustrates one usage of BatchGetApplicationRevisions.

#### Sample Request
<a name="API_BatchGetApplicationRevisions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 284
X-Amz-Target: CodeDeploy_20141006.BatchGetApplicationRevisions
X-Amz-Date: 20160707T172627Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "applicationName": "TestApp-us-east-1",
    "revisions": [
        {
            "revisionType": "S3",
            "s3Location": {
                "bundleType": "zip",
                "version": "4eQLXx7nw0iP22hxwt2_YXrUq972qkG6",
                "bucket": "project-123",
                "key": "North-App.zip",
                "eTag": "3fdd7b9196697a096d5af1d649e26a4a"
            }
        },
        {
            "revisionType": "S3",
            "s3Location": {
                "bundleType": "zip",
                "version": "BXrUq974e0iP22hxwt2_QLXx7nw3kjB9",
                "bucket": "project-123",
                "key": "North-App-2.zip",
                "eTag": "4hfj7b911d649e26a4a45390a096d5af"
            }
        }
    ]
}
```

#### Sample Response
<a name="API_BatchGetApplicationRevisions_Example_1_Response"></a>

```
{
    "applicationName": "TestApp-us-east-1",
    "errorMessage": "",
    "revisions": [
        {
            "genericRevisionInfo": {
                "deploymentGroups": [
                    "dep-group-def-456"
                ],
                "description": "Application revision registered by Deployment ID: d-D1EGTDV3C",
                "firstUsedTime": 1446232255.734,
                "lastUsedTime": 1446232255.734,
                "registerTime": 1446232255.734
            },
            "revisionType": "S3",
            "s3Location": {
                "bucket": "project-1234",
                "bundleType": "zip",
                "eTag": "3fdd7b9196697a096d5af1d649e26a4a",
                "key": "North-App.zip",
                "version": "4eQLXx7nw0iP22hxwt2_YXrUq972qkG6"
            }
        },
        {
            "genericRevisionInfo": {
                "deploymentGroups": [
                    "dep-group-def-456"
                ],
                "description": "Application revision registered by Deployment ID: d-F8ROHSIK3K",
                "firstUsedTime": 1455988916.108,
                "lastUsedTime": 1455988916.288,
                "registerTime": 1455988912.217
            },
            "revisionType": "S3",
            "s3Location": {
                "bucket": "project-1234",
                "bundleType": "zip",
                "eTag": "4hfj7b911d649e26a4a45390a096d5af",
                "key": "North-App-2.zip",
                "version": "BXrUq974e0iP22hxwt2_QLXx7nw3kjB9"
            }
        }
    ]
}
```

## See Also
<a name="API_BatchGetApplicationRevisions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/BatchGetApplicationRevisions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/BatchGetApplicationRevisions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/BatchGetApplicationRevisions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/BatchGetApplicationRevisions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/BatchGetApplicationRevisions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/BatchGetApplicationRevisions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/BatchGetApplicationRevisions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/BatchGetApplicationRevisions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/BatchGetApplicationRevisions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/BatchGetApplicationRevisions)
