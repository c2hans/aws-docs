---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_GetReplicationSet.html
---

# GetReplicationSet
<a name="API_GetReplicationSet"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Retrieve your Incident Manager replication set.

## Request Syntax
<a name="API_GetReplicationSet_RequestSyntax"></a>

```
GET /getReplicationSet?arn={{arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetReplicationSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetReplicationSet_RequestSyntax) **   <a name="IncidentManager-GetReplicationSet-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the replication set you want to retrieve.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

## Request Body
<a name="API_GetReplicationSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetReplicationSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "replicationSet": {
      "arn": "string",
      "createdBy": "string",
      "createdTime": number,
      "deletionProtected": boolean,
      "lastModifiedBy": "string",
      "lastModifiedTime": number,
      "regionMap": {
         "string" : {
            "sseKmsKeyId": "string",
            "status": "string",
            "statusMessage": "string",
            "statusUpdateDateTime": number
         }
      },
      "status": "string"
   }
}
```

## Response Elements
<a name="API_GetReplicationSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [replicationSet](#API_GetReplicationSet_ResponseSyntax) **   <a name="IncidentManager-GetReplicationSet-response-replicationSet"></a>
Details of the replication set.
Type: [ReplicationSet](API_ReplicationSet.md) object

## Errors
<a name="API_GetReplicationSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_GetReplicationSet_Examples"></a>

### Example
<a name="API_GetReplicationSet_Example_1"></a>

This example illustrates one usage of GetReplicationSet.

#### Sample Request
<a name="API_GetReplicationSet_Example_1_Request"></a>

```
GET /getReplicationSet?arn=arn%3Aaws%3Assm-incidents%3A%111122223333%3Areplication-set%2F40bd98f0-4110-2dee-b35e-b87006f9e172 HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.get-replication-set
X-Amz-Date: 20210810T224619Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210810/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_GetReplicationSet_Example_1_Response"></a>

```
{
    "replicationSet": {
        "createdBy": "arn:aws:iam::111122223333:user/exampleUser",
        "createdTime": "2021-08-10T21:03:21.332000+00:00",
        "deletionProtected": false,
        "lastModifiedBy": "arn:aws:iam::111122223333:user/exampleUser",
        "lastModifiedTime": "2021-08-10T21:03:21.332000+00:00",
        "regionMap": {
            "us-east-1": {
                "sseKmsKeyId": "arn:aws:kms:us-east-1:111122223333:key/de6a2f4e-5d40-4443-ad82-1db179510a32",
                "status": "ACTIVE"
            },
            "us-east-2": {
                "sseKmsKeyId": "arn:aws:kms:us-east-2:111122223333:key/6f1572c9-05ca-43cf-bf03-ee7bc93f59bd",
                "status": "ACTIVE",
                "statusMessage": "Tagging inaccessible"
            }
        },
        "status": "ACTIVE"
    }
}
```

## See Also
<a name="API_GetReplicationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/GetReplicationSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/GetReplicationSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/GetReplicationSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/GetReplicationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/GetReplicationSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/GetReplicationSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/GetReplicationSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/GetReplicationSet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/GetReplicationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/GetReplicationSet)
