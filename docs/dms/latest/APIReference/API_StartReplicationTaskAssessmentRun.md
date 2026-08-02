---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun.html
---

# StartReplicationTaskAssessmentRun
<a name="API_StartReplicationTaskAssessmentRun"></a>

Starts a new premigration assessment run for one or more individual assessments of a migration task.

The assessments that you can specify depend on the source and target database engine and the migration type defined for the given task. To run this operation, your migration task must already be created. After you run this operation, you can review the status of each individual assessment. You can also run the migration task manually after the assessment run and its individual assessments complete.

## Request Syntax
<a name="API_StartReplicationTaskAssessmentRun_RequestSyntax"></a>

```
{
   "AssessmentRunName": "{{string}}",
   "Exclude": [ "{{string}}" ],
   "IncludeOnly": [ "{{string}}" ],
   "ReplicationTaskArn": "{{string}}",
   "ResultEncryptionMode": "{{string}}",
   "ResultKmsKeyArn": "{{string}}",
   "ResultLocationBucket": "{{string}}",
   "ResultLocationFolder": "{{string}}",
   "ServiceAccessRoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "ResourceArn": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_StartReplicationTaskAssessmentRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssessmentRunName](#API_StartReplicationTaskAssessmentRun_RequestSyntax) **   <a name="DMS-StartReplicationTaskAssessmentRun-request-AssessmentRunName"></a>
Unique name to identify the assessment run.
Type: String
Required: Yes

 ** [Exclude](#API_StartReplicationTaskAssessmentRun_RequestSyntax) **   <a name="DMS-StartReplicationTaskAssessmentRun-request-Exclude"></a>
Space-separated list of names for specific individual assessments that you want to exclude. These names come from the default list of individual assessments that AWS DMS supports for the associated migration task. This task is specified by `ReplicationTaskArn`.
You can't set a value for `Exclude` if you also set a value for `IncludeOnly` in the API operation.
To identify the names of the default individual assessments that AWS DMS supports for the associated migration task, run the `DescribeApplicableIndividualAssessments` operation using its own `ReplicationTaskArn` request parameter.
Type: Array of strings
Required: No

 ** [IncludeOnly](#API_StartReplicationTaskAssessmentRun_RequestSyntax) **   <a name="DMS-StartReplicationTaskAssessmentRun-request-IncludeOnly"></a>
Space-separated list of names for specific individual assessments that you want to include. These names come from the default list of individual assessments that AWS DMS supports for the associated migration task. This task is specified by `ReplicationTaskArn`.
You can't set a value for `IncludeOnly` if you also set a value for `Exclude` in the API operation.
To identify the names of the default individual assessments that AWS DMS supports for the associated migration task, run the `DescribeApplicableIndividualAssessments` operation using its own `ReplicationTaskArn` request parameter.
Type: Array of strings
Required: No

 ** [ReplicationTaskArn](#API_StartReplicationTaskAssessmentRun_RequestSyntax) **   <a name="DMS-StartReplicationTaskAssessmentRun-request-ReplicationTaskArn"></a>
Amazon Resource Name (ARN) of the migration task associated with the premigration assessment run that you want to start.
Type: String
Required: Yes

 ** [ResultEncryptionMode](#API_StartReplicationTaskAssessmentRun_RequestSyntax) **   <a name="DMS-StartReplicationTaskAssessmentRun-request-ResultEncryptionMode"></a>
Encryption mode that you can specify to encrypt the results of this assessment run. If you don't specify this request parameter, AWS DMS stores the assessment run results without encryption. You can specify one of the options following:
+  `"SSE_S3"` – The server-side encryption provided as a default by Amazon S3.
+  `"SSE_KMS"` – AWS Key Management Service (AWS KMS) encryption. This encryption can use either a custom KMS encryption key that you specify or the default KMS encryption key that DMS provides.
Type: String
Required: No

 ** [ResultKmsKeyArn](#API_StartReplicationTaskAssessmentRun_RequestSyntax) **   <a name="DMS-StartReplicationTaskAssessmentRun-request-ResultKmsKeyArn"></a>
ARN of a custom KMS encryption key that you specify when you set `ResultEncryptionMode` to `"SSE_KMS`".
Type: String
Required: No

 ** [ResultLocationBucket](#API_StartReplicationTaskAssessmentRun_RequestSyntax) **   <a name="DMS-StartReplicationTaskAssessmentRun-request-ResultLocationBucket"></a>
Amazon S3 bucket where you want AWS DMS to store the results of this assessment run.
Type: String
Required: Yes

 ** [ResultLocationFolder](#API_StartReplicationTaskAssessmentRun_RequestSyntax) **   <a name="DMS-StartReplicationTaskAssessmentRun-request-ResultLocationFolder"></a>
Folder within an Amazon S3 bucket where you want AWS DMS to store the results of this assessment run.
Type: String
Required: No

 ** [ServiceAccessRoleArn](#API_StartReplicationTaskAssessmentRun_RequestSyntax) **   <a name="DMS-StartReplicationTaskAssessmentRun-request-ServiceAccessRoleArn"></a>
ARN of the service role needed to start the assessment run. The role must allow the `iam:PassRole` action.
Type: String
Required: Yes

 ** [Tags](#API_StartReplicationTaskAssessmentRun_RequestSyntax) **   <a name="DMS-StartReplicationTaskAssessmentRun-request-Tags"></a>
One or more tags to be assigned to the premigration assessment run that you want to start.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_StartReplicationTaskAssessmentRun_ResponseSyntax"></a>

```
{
   "ReplicationTaskAssessmentRun": {
      "AssessmentProgress": {
         "IndividualAssessmentCompletedCount": number,
         "IndividualAssessmentCount": number
      },
      "AssessmentRunName": "string",
      "IsLatestTaskAssessmentRun": boolean,
      "LastFailureMessage": "string",
      "ReplicationTaskArn": "string",
      "ReplicationTaskAssessmentRunArn": "string",
      "ReplicationTaskAssessmentRunCreationDate": number,
      "ResultEncryptionMode": "string",
      "ResultKmsKeyArn": "string",
      "ResultLocationBucket": "string",
      "ResultLocationFolder": "string",
      "ResultStatistic": {
         "Cancelled": number,
         "Error": number,
         "Failed": number,
         "Passed": number,
         "Skipped": number,
         "Warning": number
      },
      "ServiceAccessRoleArn": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_StartReplicationTaskAssessmentRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationTaskAssessmentRun](#API_StartReplicationTaskAssessmentRun_ResponseSyntax) **   <a name="DMS-StartReplicationTaskAssessmentRun-response-ReplicationTaskAssessmentRun"></a>
The premigration assessment run that was started.
Type: [ReplicationTaskAssessmentRun](API_ReplicationTaskAssessmentRun.md) object

## Errors
<a name="API_StartReplicationTaskAssessmentRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** KMSAccessDeniedFault **
The ciphertext references a key that doesn't exist or that the DMS account doesn't have access to.
HTTP Status Code: 400

 ** KMSDisabledFault **
The specified KMS key isn't enabled.
HTTP Status Code: 400

 ** KMSFault **
An AWS Key Management Service (AWS KMS) error is preventing access to AWS KMS.
HTTP Status Code: 400

 ** KMSInvalidStateFault **
The state of the specified AWS KMS resource isn't valid for this request.
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **
 AWS DMS cannot access the KMS key.
 ** message **

HTTP Status Code: 400

 ** KMSNotFoundFault **
The specified AWS KMS entity or resource can't be found.
HTTP Status Code: 400

 ** ResourceAlreadyExistsFault **
The resource you are attempting to create already exists.
 ** message **

 ** resourceArn **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

 ** S3AccessDeniedFault **
Insufficient privileges are preventing access to an Amazon S3 object.
HTTP Status Code: 400

 ** S3ResourceNotFoundFault **
A specified Amazon S3 bucket, bucket folder, or other object can't be found.
HTTP Status Code: 400

## Examples
<a name="API_StartReplicationTaskAssessmentRun_Examples"></a>

### Example
<a name="API_StartReplicationTaskAssessmentRun_Example_1"></a>

This example illustrates one usage of StartReplicationTaskAssessmentRun.

#### Sample Request
<a name="API_StartReplicationTaskAssessmentRun_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256
Credential=<Credential>,
SignedHeaders=contenttype;date;host;user-
agent;x-amz-date;x-amz-target;x-amzn-
requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.StartReplicationTaskAssessmentRun
{
  "ReplicationTaskArn": "arn:aws:dms:us-west-2:123456789012:task:L6XROPGLRF25LCREVEDPT3XL5QJM5IZNUSVFV6Q",
  "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/Admin",
  "ResultLocationBucket": "s3-endpoint-bucket",
  "ResultLocationFolder": "",
  "AssessmentRunName": "Assessment-run-2020-07-10-18-02-12",
  "IncludeOnly": [
    "full-lob-not-nullable-at-target",
    "table-with-lob-but-without-primary-key-or-unique-constraint",
    "unsupported-data-types-in-source"
  ]
}
```

#### Sample Response
<a name="API_StartReplicationTaskAssessmentRun_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "ReplicationTaskAssessmentRun": {
    "AssessmentProgress": {
      "IndividualAssessmentCompletedCount": 0,
      "IndividualAssessmentCount": 3
    },
    "AssessmentRunName": "Assessment-run-2020-07-10-18-02-12",
    "ReplicationTaskArn": "arn:aws:dms:us-west-2:123456789012:task:L6XROPGLRF25LCREVEDPT3XL5QJM5IZNUSVFV6Q",
    "ReplicationTaskAssessmentRunArn": "arn:aws:dms:us-west-2:123456789012:assessment-run:W22Q73FR2FBBHSBENXMNMYEWFHX6YTIQUN4OTLA",
    "ReplicationTaskAssessmentRunCreationDate": 1594429350.259,
    "ResultEncryptionMode": "NONE",
    "ResultLocationBucket": "s3-endpoint-bucket",
    "ResultLocationFolder": "",
    "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/Admin",
    "Status": "starting"
  }
}
```

## See Also
<a name="API_StartReplicationTaskAssessmentRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StartReplicationTaskAssessmentRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StartReplicationTaskAssessmentRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StartReplicationTaskAssessmentRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StartReplicationTaskAssessmentRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StartReplicationTaskAssessmentRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StartReplicationTaskAssessmentRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StartReplicationTaskAssessmentRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StartReplicationTaskAssessmentRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StartReplicationTaskAssessmentRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StartReplicationTaskAssessmentRun)
