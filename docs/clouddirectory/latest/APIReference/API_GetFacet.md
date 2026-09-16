---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_GetFacet.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# GetFacet
<a name="API_GetFacet"></a>

Gets details of the [Facet](API_Facet.md), such as facet name, attributes, [Rule](API_Rule.md)s, or `ObjectType`. You can call this on all kinds of schema facets -- published, development, or applied.

## Request Syntax
<a name="API_GetFacet_RequestSyntax"></a>

```
POST /amazonclouddirectory/2017-01-11/facet HTTP/1.1
x-amz-data-partition: {{SchemaArn}}
Content-type: application/json

{
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetFacet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SchemaArn](#API_GetFacet_RequestSyntax) **   <a name="amazoncds-GetFacet-request-SchemaArn"></a>
The Amazon Resource Name (ARN) that is associated with the [Facet](API_Facet.md). For more information, see [Arn Examples](arns.md).
Required: Yes

## Request Body
<a name="API_GetFacet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_GetFacet_RequestSyntax) **   <a name="amazoncds-GetFacet-request-Name"></a>
The name of the facet to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

## Response Syntax
<a name="API_GetFacet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Facet": {
      "FacetStyle": "string",
      "Name": "string",
      "ObjectType": "string"
   }
}
```

## Response Elements
<a name="API_GetFacet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Facet](#API_GetFacet_ResponseSyntax) **   <a name="amazoncds-GetFacet-response-Facet"></a>
The [Facet](API_Facet.md) structure that is associated with the facet.
Type: [Facet](API_Facet.md) object

## Errors
<a name="API_GetFacet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md) and check your permissions.
HTTP Status Code: 403

 ** FacetNotFoundException **
The specified [Facet](API_Facet.md) could not be found.
HTTP Status Code: 400

 ** InternalServiceException **
Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/) site to see if there are any operational issues with the service.
HTTP Status Code: 500

 ** InvalidArnException **
Indicates that the provided ARN value is not valid.
HTTP Status Code: 400

 ** LimitExceededException **
Indicates that limits are exceeded. See [Limits](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/limits.html) for more information.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource could not be found.
HTTP Status Code: 404

 ** RetryableConflictException **
Occurs when a conflict with a previous successful write is detected. For example, if a write operation occurs on an object and then an attempt is made to read the object using “SERIALIZABLE” consistency, this exception may result. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
HTTP Status Code: 409

 ** ValidationException **
Indicates that your request is malformed in some manner. See the exception message.
HTTP Status Code: 400

## Examples
<a name="API_GetFacet_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_GetFacet_Example_1"></a>

This example illustrates one usage of GetFacet.

```
POST /amazonclouddirectory/2017-01-11/facet HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 17
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171005/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=70251faa630aeb0c6ca6375eefddef5fb0f956289eaf4a6fbb48ad7a34926aa6
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1
X-Amz-Date: 20171005T195712Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"Name": "node2"
}
```

### Example Response
<a name="API_GetFacet_Example_2"></a>

This example illustrates one usage of GetFacet.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 614b09f0-aa07-11e7-843e-9fad359f817f
Date: Thu, 05 Oct 2017 19:57:13 GMT
x-amzn-RequestId: 614b09f0-aa07-11e7-843e-9fad359f817f
Content-Type: application/json
Content-Length: 46

{
	"Facet": {
		"Name": "node2",
		"ObjectType": "NODE"
	}
}
```

## See Also
<a name="API_GetFacet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/GetFacet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/clouddirectory-2017-01-11/GetFacet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/GetFacet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/GetFacet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/GetFacet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/GetFacet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/GetFacet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/GetFacet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/GetFacet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/GetFacet)
