---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_GetDirectory.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# GetDirectory
<a name="API_GetDirectory"></a>

Retrieves metadata about a directory.

## Request Syntax
<a name="API_GetDirectory_RequestSyntax"></a>

```
POST /amazonclouddirectory/2017-01-11/directory/get HTTP/1.1
x-amz-data-partition: {{DirectoryArn}}
```

## URI Request Parameters
<a name="API_GetDirectory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DirectoryArn](#API_GetDirectory_RequestSyntax) **   <a name="amazoncds-GetDirectory-request-DirectoryArn"></a>
The ARN of the directory.
Required: Yes

## Request Body
<a name="API_GetDirectory_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDirectory_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Directory": {
      "CreationDateTime": number,
      "DirectoryArn": "string",
      "Name": "string",
      "State": "string"
   }
}
```

## Response Elements
<a name="API_GetDirectory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Directory](#API_GetDirectory_ResponseSyntax) **   <a name="amazoncds-GetDirectory-response-Directory"></a>
Metadata about the directory.
Type: [Directory](API_Directory.md) object

## Errors
<a name="API_GetDirectory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md) and check your permissions.
HTTP Status Code: 403

 ** InternalServiceException **
Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/) site to see if there are any operational issues with the service.
HTTP Status Code: 500

 ** InvalidArnException **
Indicates that the provided ARN value is not valid.
HTTP Status Code: 400

 ** LimitExceededException **
Indicates that limits are exceeded. See [Limits](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/limits.html) for more information.
HTTP Status Code: 400

 ** RetryableConflictException **
Occurs when a conflict with a previous successful write is detected. For example, if a write operation occurs on an object and then an attempt is made to read the object using “SERIALIZABLE” consistency, this exception may result. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
HTTP Status Code: 409

 ** ValidationException **
Indicates that your request is malformed in some manner. See the exception message.
HTTP Status Code: 400

## Examples
<a name="API_GetDirectory_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_GetDirectory_Example_1"></a>

This example illustrates one usage of GetDirectory.

```
POST /amazonclouddirectory/2017-01-11/directory/get HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 0
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171005/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=255eceb681267d8e41de7eb8983269fb61aa76fe56e2b36a4d0c4f855d9ae237
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY
X-Amz-Date: 20171005T202329Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8
```

### Example Response
<a name="API_GetDirectory_Example_2"></a>

This example illustrates one usage of GetDirectory.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0d9489ee-aa0b-11e7-a169-c5bf0acd39f4
Date: Thu, 05 Oct 2017 20:23:30 GMT
x-amzn-RequestId: 0d9489ee-aa0b-11e7-a169-c5bf0acd39f4
Content-Type: application/json
Content-Length: 185

{
	"Directory": {
		"CreationDateTime": 1.506115781186E9,
		"DirectoryArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY",
		"Name": "ExampleCD",
		"State": "ENABLED"
	}
}
```

## See Also
<a name="API_GetDirectory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/GetDirectory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/clouddirectory-2017-01-11/GetDirectory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/GetDirectory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/GetDirectory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/GetDirectory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/GetDirectory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/GetDirectory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/GetDirectory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/GetDirectory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/GetDirectory)
