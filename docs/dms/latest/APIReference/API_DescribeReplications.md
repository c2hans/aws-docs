---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplications.html
---

# DescribeReplications
<a name="API_DescribeReplications"></a>

Provides details on replication progress by returning status information for one or more provisioned AWS DMS Serverless replications.

## Request Syntax
<a name="API_DescribeReplications_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_DescribeReplications_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeReplications_RequestSyntax) **   <a name="DMS-DescribeReplications-request-Filters"></a>
Filters applied to the replications.
 Valid filter names: `replication-config-arn` \| `replication-config-id`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeReplications_RequestSyntax) **   <a name="DMS-DescribeReplications-request-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeReplications_RequestSyntax) **   <a name="DMS-DescribeReplications-request-MaxRecords"></a>
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeReplications_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "Replications": [
      {
         "CdcStartPosition": "string",
         "CdcStartTime": number,
         "CdcStopPosition": "string",
         "FailureMessages": [ "string" ],
         "IsReadOnly": boolean,
         "PremigrationAssessmentStatuses": [
            {
               "AssessmentProgress": {
                  "IndividualAssessmentCompletedCount": number,
                  "IndividualAssessmentCount": number
               },
               "FailOnAssessmentFailure": boolean,
               "LastFailureMessage": "string",
               "PremigrationAssessmentRunArn": "string",
               "PremigrationAssessmentRunCreationDate": number,
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
               "Status": "string"
            }
         ],
         "ProvisionData": {
            "DateNewProvisioningDataAvailable": number,
            "DateProvisioned": number,
            "IsNewProvisioningAvailable": boolean,
            "ProvisionedCapacityUnits": number,
            "ProvisionState": "string",
            "ReasonForNewProvisioningData": "string"
         },
         "RecoveryCheckpoint": "string",
         "ReplicationConfigArn": "string",
         "ReplicationConfigIdentifier": "string",
         "ReplicationCreateTime": number,
         "ReplicationDeprovisionTime": number,
         "ReplicationLastStopTime": number,
         "ReplicationStats": {
            "ElapsedTimeMillis": number,
            "FreshStartDate": number,
            "FullLoadFinishDate": number,
            "FullLoadProgressPercent": number,
            "FullLoadStartDate": number,
            "StartDate": number,
            "StopDate": number,
            "TablesErrored": number,
            "TablesLoaded": number,
            "TablesLoading": number,
            "TablesQueued": number
         },
         "ReplicationType": "string",
         "ReplicationUpdateTime": number,
         "SourceEndpointArn": "string",
         "StartReplicationType": "string",
         "Status": "string",
         "StopReason": "string",
         "TargetEndpointArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeReplications_ResponseSyntax) **   <a name="DMS-DescribeReplications-response-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 ** [Replications](#API_DescribeReplications_ResponseSyntax) **   <a name="DMS-DescribeReplications-response-Replications"></a>
The replication descriptions.
Type: Array of [Replication](API_Replication.md) objects

## Errors
<a name="API_DescribeReplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeReplications_Examples"></a>

### Example
<a name="API_DescribeReplications_Example_1"></a>

This example illustrates one usage of DescribeReplications.

#### Sample Request
<a name="API_DescribeReplications_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>,
 SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.DescribeReplications
{
   "Filters":[
      {
         "Name":"endpoint-arn",
         "Values":[
            "arn:aws:dms:us-east
1:123456789012:endpoint:WTMG7G6X5TQ5GOQG46WGEBNMPDSH47J5JZHXUFI"
         ]
      }
   ],
   "MaxRecords":0,
   "Marker":""
}
```

#### Sample Response
<a name="API_DescribeReplications_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "Replications": {
      {
         "SourceEndpointArn": "arn:aws:dms:us-east-
1:123456789012:endpoint:5OFSBLSONLVVSYQAY7IBDSMCEHD6NU4FJQ5L7XY",
         "Status": "created",
         "ReplicationConfigIdentifier": "serverless-kms-0",
         "ReplicationStats": {
             "TablesLoading": 0,
             "TablesQueued": 0,
             "TablesErrored": 0,
             "FullLoadProgressPercent": 0,
             "TablesLoaded": 0,
             "ElapsedTimeMillis": 0
         },
         "ReplicationCreateTime": 1679665872.025,
         "ReplicationConfigArn": "arn:aws:dms:us-east-
1:123456789012:replication-config:ZKIB7GSLEJ2CIG5I6FGI6OR6Y25RRIDGG4H5OCY",
         "ReplicationType": "full-load-and-cdc",
         "ReplicationUpdateTime": 1679665872.025,
         "ProvisionData": {
             "IsNewProvisioningAvailable": false,
             "ProvisionedCapacityUnits": 0
         },
         "TargetEndpointArn": "arn:aws:dms:us-west-
2:123456789012:endpoint:WTMG7G6X5TQ5GOQG46WGEBNMPDSH47J5JZHXUFI",
         "FailureMessages": []
      }
   }
}
```

## See Also
<a name="API_DescribeReplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeReplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeReplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeReplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeReplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeReplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeReplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeReplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeReplications)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeReplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeReplications)
