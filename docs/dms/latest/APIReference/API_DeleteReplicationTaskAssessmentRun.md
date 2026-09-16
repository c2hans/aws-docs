---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTaskAssessmentRun.html
---

# DeleteReplicationTaskAssessmentRun
<a name="API_DeleteReplicationTaskAssessmentRun"></a>

Deletes the record of a single premigration assessment run.

This operation removes all metadata that AWS DMS maintains about this assessment run. However, the operation leaves untouched all information about this assessment run that is stored in your Amazon S3 bucket.

## Request Syntax
<a name="API_DeleteReplicationTaskAssessmentRun_RequestSyntax"></a>

```
{
   "ReplicationTaskAssessmentRunArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteReplicationTaskAssessmentRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReplicationTaskAssessmentRunArn](#API_DeleteReplicationTaskAssessmentRun_RequestSyntax) **   <a name="DMS-DeleteReplicationTaskAssessmentRun-request-ReplicationTaskAssessmentRunArn"></a>
Amazon Resource Name (ARN) of the premigration assessment run to be deleted.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteReplicationTaskAssessmentRun_ResponseSyntax"></a>

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
<a name="API_DeleteReplicationTaskAssessmentRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationTaskAssessmentRun](#API_DeleteReplicationTaskAssessmentRun_ResponseSyntax) **   <a name="DMS-DeleteReplicationTaskAssessmentRun-response-ReplicationTaskAssessmentRun"></a>
The `ReplicationTaskAssessmentRun` object for the deleted assessment run.
Type: [ReplicationTaskAssessmentRun](API_ReplicationTaskAssessmentRun.md) object

## Errors
<a name="API_DeleteReplicationTaskAssessmentRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DeleteReplicationTaskAssessmentRun_Examples"></a>

### Example
<a name="API_DeleteReplicationTaskAssessmentRun_Example_1"></a>

This example illustrates one usage of DeleteReplicationTaskAssessmentRun.

#### Sample Request
<a name="API_DeleteReplicationTaskAssessmentRun_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DeleteReplicationTaskAssessmentRun
{
  "ReplicationTaskAssessmentRunArn": "arn:aws:dms:us-west-2:123456789012:assessment-run:FCBLKM7PRVDJ3S4DJKFZYV6XJE6KDMIUHJX4O4I"
}
```

#### Sample Response
<a name="API_DeleteReplicationTaskAssessmentRun_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "ReplicationTaskAssessmentRun": {
    "AssessmentProgress": {
      "IndividualAssessmentCompletedCount": 4,
      "IndividualAssessmentCount": 4
    },
    "AssessmentRunName": "myRun",
    "ReplicationTaskArn": "arn:aws:dms:us-west-2:123456789012:task:L6XROPGLRF25LCREVEDPT3XL5QJM5IZNUSVFV6A",
    "ReplicationTaskAssessmentRunArn": "arn:aws:dms:us-west-2:123456789012:assessment-run:FCBLKM7PRVDJ3S4DJKFZYV6XJE6KDMIUHJX4O4I",
    "ReplicationTaskAssessmentRunCreationDate": 1594068046.933,
    "ResultEncryptionMode": "NONE",
    "ResultLocationBucket": "amzn-s3-demo-bucket",
    "ResultLocationFolder": "myFolder",
    "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/Admin",
    "Status": "deleting"
  }
}
```

## See Also
<a name="API_DeleteReplicationTaskAssessmentRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DeleteReplicationTaskAssessmentRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DeleteReplicationTaskAssessmentRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DeleteReplicationTaskAssessmentRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DeleteReplicationTaskAssessmentRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DeleteReplicationTaskAssessmentRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DeleteReplicationTaskAssessmentRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DeleteReplicationTaskAssessmentRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DeleteReplicationTaskAssessmentRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DeleteReplicationTaskAssessmentRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DeleteReplicationTaskAssessmentRun)
