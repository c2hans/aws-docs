---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CopySnapshot.html
---

# CopySnapshot
<a name="API_CopySnapshot"></a>

Copies a manual snapshot of an instance or disk as another manual snapshot, or copies an automatic snapshot of an instance or disk as a manual snapshot. This operation can also be used to copy a manual or automatic snapshot of an instance or a disk from one AWS Region to another in Amazon Lightsail.

When copying a *manual snapshot*, be sure to define the `source region`, `source snapshot name`, and `target snapshot name` parameters.

When copying an *automatic snapshot*, be sure to define the `source region`, `source resource name`, `target snapshot name`, and either the `restore date` or the `use latest restorable auto snapshot` parameters.

## Request Syntax
<a name="API_CopySnapshot_RequestSyntax"></a>

```
{
   "restoreDate": "{{string}}",
   "sourceRegion": "{{string}}",
   "sourceResourceName": "{{string}}",
   "sourceSnapshotName": "{{string}}",
   "targetSnapshotName": "{{string}}",
   "useLatestRestorableAutoSnapshot": {{boolean}}
}
```

## Request Parameters
<a name="API_CopySnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [restoreDate](#API_CopySnapshot_RequestSyntax) **   <a name="Lightsail-CopySnapshot-request-restoreDate"></a>
The date of the source automatic snapshot to copy. Use the `get auto snapshots` operation to identify the dates of the available automatic snapshots.
Constraints:
+ Must be specified in `YYYY-MM-DD` format.
+ This parameter cannot be defined together with the `use latest restorable auto snapshot` parameter. The `restore date` and `use latest restorable auto snapshot` parameters are mutually exclusive.
+ Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots).
Type: String
Required: No

 ** [sourceRegion](#API_CopySnapshot_RequestSyntax) **   <a name="Lightsail-CopySnapshot-request-sourceRegion"></a>
The AWS Region where the source manual or automatic snapshot is located.
Type: String
Valid Values: `us-east-1 | us-east-2 | us-west-1 | us-west-2 | eu-west-1 | eu-west-2 | eu-west-3 | eu-central-1 | eu-north-1 | eu-south-2 | ca-central-1 | ap-east-1 | ap-south-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | ap-northeast-2 | ap-southeast-3 | ap-southeast-5 | sa-east-1`
Required: Yes

 ** [sourceResourceName](#API_CopySnapshot_RequestSyntax) **   <a name="Lightsail-CopySnapshot-request-sourceResourceName"></a>
The name of the source instance or disk from which the source automatic snapshot was created.
Constraint:
+ Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots).
Type: String
Required: No

 ** [sourceSnapshotName](#API_CopySnapshot_RequestSyntax) **   <a name="Lightsail-CopySnapshot-request-sourceSnapshotName"></a>
The name of the source manual snapshot to copy.
Constraint:
+ Define this parameter only when copying a manual snapshot as another manual snapshot.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [targetSnapshotName](#API_CopySnapshot_RequestSyntax) **   <a name="Lightsail-CopySnapshot-request-targetSnapshotName"></a>
The name of the new manual snapshot to be created as a copy.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [useLatestRestorableAutoSnapshot](#API_CopySnapshot_RequestSyntax) **   <a name="Lightsail-CopySnapshot-request-useLatestRestorableAutoSnapshot"></a>
A Boolean value to indicate whether to use the latest available automatic snapshot of the specified source instance or disk.
Constraints:
+ This parameter cannot be defined together with the `restore date` parameter. The `use latest restorable auto snapshot` and `restore date` parameters are mutually exclusive.
+ Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots).
Type: Boolean
Required: No

## Response Syntax
<a name="API_CopySnapshot_ResponseSyntax"></a>

```
{
   "operations": [
      {
         "createdAt": number,
         "errorCode": "string",
         "errorDetails": "string",
         "id": "string",
         "isTerminal": boolean,
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "operationDetails": "string",
         "operationType": "string",
         "resourceName": "string",
         "resourceType": "string",
         "status": "string",
         "statusChangedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_CopySnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_CopySnapshot_ResponseSyntax) **   <a name="Lightsail-CopySnapshot-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CopySnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** AccountSetupInProgressException **
Lightsail throws this exception when an account is still in the setup in progress state.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## Examples
<a name="API_CopySnapshot_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Copy an automatic snapshot
<a name="API_CopySnapshot_Example_1"></a>

The following example creates a new manual snapshot named `CopiedAutoSnapshot-2019-09-25` as a copy of the existing automatic snapshot named `2019-09-25` from the `WordPress-1` instance in the `us-west-2` AWS Region.

#### Sample Request
<a name="API_CopySnapshot_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: lightsail.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: Lightsail_20161128.CopySnapshot
Content-Type: application/x-amz-json-1.1
User-Agent: AGENT
X-Amz-Date: 20190927T194244Z
Authorization: AUTHPARAMS
Content-Length: 150

{
	"sourceResourceName": "WordPress-1",
	"restoreDate": "2019-09-25",
	"targetSnapshotName": "CopiedAutoSnapshot-2019-09-25",
	"sourceRegion": "us-west-2"
}
```

#### Sample Response
<a name="API_CopySnapshot_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 27 Sep 2019 19:42:46 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 380
x-amzn-RequestId: 69449102-9023-431e-8a00-7EXAMPLE6970
Connection: keep-alive

{
	"operations": [{
		"createdAt": 1.56961336589E9,
		"id": "0710de23-b848-4146-887d-ec12093c049d",
		"isTerminal": false,
		"location": {
			"availabilityZone": "all",
			"regionName": "us-west-2"
		},
		"operationDetails": "us-west-2:WordPress-1",
		"operationType": "CopySnapshot",
		"resourceName": "CopiedAutoSnapshot-2019-09-25",
		"resourceType": "InstanceSnapshot",
		"status": "Started",
		"statusChangedAt": 1.56961336589E9
	}]
}
```

### Copy a manual snapshot
<a name="API_CopySnapshot_Example_2"></a>

The following example creates a new manual snapshot named `CopiedManualSnapshot-2019-09-25` as a copy of the existing manual snapshot named `WordPress-1-1569608575` in the `us-west-2` AWS Region.

#### Sample Request
<a name="API_CopySnapshot_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: lightsail.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: Lightsail_20161128.CopySnapshot
Content-Type: application/x-amz-json-1.1
User-Agent: AGENT
X-Amz-Date: 20190927T195200Z
Authorization: AUTHPARAMS
Content-Length: 134

{
	"sourceSnapshotName": "WordPress-1-1569608575",
	"targetSnapshotName": "CopiedManualSnapshot-2019-09-25",
	"sourceRegion": "us-west-2"
}
```

#### Sample Response
<a name="API_CopySnapshot_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 27 Sep 2019 19:52:01 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 395
x-amzn-RequestId: 5e3e211b-0afe-439e-bead-8EXAMPLEb3c8
Connection: keep-alive

{
	"operations": [{
		"createdAt": 1.569613921044E9,
		"id": "0d4f2d2a-78ce-44d1-82fe-33588af9afa0",
		"isTerminal": false,
		"location": {
			"availabilityZone": "all",
			"regionName": "us-west-2"
		},
		"operationDetails": "us-west-2:WordPress-1-1569608575",
		"operationType": "CopySnapshot",
		"resourceName": "CopiedManualSnapshot-2019-09-25",
		"resourceType": "InstanceSnapshot",
		"status": "Started",
		"statusChangedAt": 1.569613921044E9
	}]
}
```

## See Also
<a name="API_CopySnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CopySnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CopySnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CopySnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CopySnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CopySnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CopySnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CopySnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CopySnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CopySnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CopySnapshot)
