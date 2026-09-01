---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListApplicationRevisions.html
---

# ListApplicationRevisions
<a name="API_ListApplicationRevisions"></a>

Lists information about revisions for an application.

## Request Syntax
<a name="API_ListApplicationRevisions_RequestSyntax"></a>

```
{
   "applicationName": "{{string}}",
   "deployed": "{{string}}",
   "nextToken": "{{string}}",
   "s3Bucket": "{{string}}",
   "s3KeyPrefix": "{{string}}",
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListApplicationRevisions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationName](#API_ListApplicationRevisions_RequestSyntax) **   <a name="CodeDeploy-ListApplicationRevisions-request-applicationName"></a>
 The name of an AWS CodeDeploy application associated with the user or AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: Yes

 ** [deployed](#API_ListApplicationRevisions_RequestSyntax) **   <a name="CodeDeploy-ListApplicationRevisions-request-deployed"></a>
 Whether to list revisions based on whether the revision is the target revision of a deployment group:
+  `include`: List revisions that are target revisions of a deployment group.
+  `exclude`: Do not list revisions that are target revisions of a deployment group.
+  `ignore`: List all revisions.
Type: String
Valid Values: `include | exclude | ignore`
Required: No

 ** [nextToken](#API_ListApplicationRevisions_RequestSyntax) **   <a name="CodeDeploy-ListApplicationRevisions-request-nextToken"></a>
An identifier returned from the previous `ListApplicationRevisions` call. It can be used to return the next set of applications in the list.
Type: String
Required: No

 ** [s3Bucket](#API_ListApplicationRevisions_RequestSyntax) **   <a name="CodeDeploy-ListApplicationRevisions-request-s3Bucket"></a>
 An Amazon S3 bucket name to limit the search for revisions.
 If set to null, all of the user's buckets are searched.
Type: String
Required: No

 ** [s3KeyPrefix](#API_ListApplicationRevisions_RequestSyntax) **   <a name="CodeDeploy-ListApplicationRevisions-request-s3KeyPrefix"></a>
 A key prefix for the set of Amazon S3 objects to limit the search for revisions.
Type: String
Required: No

 ** [sortBy](#API_ListApplicationRevisions_RequestSyntax) **   <a name="CodeDeploy-ListApplicationRevisions-request-sortBy"></a>
The column name to use to sort the list results:
+  `registerTime`: Sort by the time the revisions were registered with AWS CodeDeploy.
+  `firstUsedTime`: Sort by the time the revisions were first used in a deployment.
+  `lastUsedTime`: Sort by the time the revisions were last used in a deployment.
 If not specified or set to null, the results are returned in an arbitrary order.
Type: String
Valid Values: `registerTime | firstUsedTime | lastUsedTime`
Required: No

 ** [sortOrder](#API_ListApplicationRevisions_RequestSyntax) **   <a name="CodeDeploy-ListApplicationRevisions-request-sortOrder"></a>
 The order in which to sort the list results:
+  `ascending`: ascending order.
+  `descending`: descending order.
If not specified, the results are sorted in ascending order.
If set to null, the results are sorted in an arbitrary order.
Type: String
Valid Values: `ascending | descending`
Required: No

## Response Syntax
<a name="API_ListApplicationRevisions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "revisions": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListApplicationRevisions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListApplicationRevisions_ResponseSyntax) **   <a name="CodeDeploy-ListApplicationRevisions-response-nextToken"></a>
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list application revisions call to return the next set of application revisions in the list.
Type: String

 ** [revisions](#API_ListApplicationRevisions_ResponseSyntax) **   <a name="CodeDeploy-ListApplicationRevisions-response-revisions"></a>
A list of locations that contain the matching revisions.
Type: Array of [RevisionLocation](API_RevisionLocation.md) objects

## Errors
<a name="API_ListApplicationRevisions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** BucketNameFilterRequiredException **
A bucket name is required, but was not provided.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidBucketNameFilterException **
The bucket name either doesn't exist or was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeployedStateFilterException **
The deployed state filter was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidKeyPrefixFilterException **
The specified key prefix filter was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The next token was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidSortByException **
The column name to sort by is either not present or was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidSortOrderException **
The sort order was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_ListApplicationRevisions_Examples"></a>

### Example
<a name="API_ListApplicationRevisions_Example_1"></a>

This example illustrates one usage of ListApplicationRevisions.

#### Sample Request
<a name="API_ListApplicationRevisions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 45
X-Amz-Target: CodeDeploy_20141006.ListApplicationRevisions
X-Amz-Date: 20160707T021008Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
	"applicationName": "TestApp-us-east-1"
}
```

#### Sample Response
<a name="API_ListApplicationRevisions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 8000a419-88e2-11e5-b497-75c493756c4d
Content-Type: application/x-amz-json-1.1
Content-Length: 611

{
    "revisions": [
        {
            "revisionType": "S3",
            "s3Location": {
                "bucket": "project-1234",
                "bundleType": "zip",
                "eTag": "3fdd7b3456697a096d5af1d649e26a4a",
                "key": "North-App.zip"
            }
        },
        {
            "revisionType": "S3",
            "s3Location": {
                "bucket": "project-1234",
                "bundleType": "zip",
                "eTag": "\"3fdd7b9142497a096d5af1d649e26a4a\"",
                "key": "North-App.zip"
            }
        },
        {
            "revisionType": "S3",
            "s3Location": {
                "bucket": "project-1234",
                "bundleType": "zip",
                "eTag": "ffe5402cff48b652bf903700453f7408",
                "key": "North-App.zip"
            }
        },
        {
            "revisionType": "S3",
            "s3Location": {
                "bucket": "project-1234",
                "bundleType": "zip",
                "eTag": "fff9102vdf48b652bf903700453f7408",
                "key": "North-App.zip"
            }
        }
    ]
}
```

## See Also
<a name="API_ListApplicationRevisions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/ListApplicationRevisions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/ListApplicationRevisions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ListApplicationRevisions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/ListApplicationRevisions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ListApplicationRevisions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/ListApplicationRevisions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/ListApplicationRevisions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/ListApplicationRevisions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/ListApplicationRevisions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ListApplicationRevisions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
