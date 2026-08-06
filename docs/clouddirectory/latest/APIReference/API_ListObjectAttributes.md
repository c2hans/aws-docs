---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListObjectAttributes.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# ListObjectAttributes
<a name="API_ListObjectAttributes"></a>

Lists all attributes that are associated with an object.

## Request Syntax
<a name="API_ListObjectAttributes_RequestSyntax"></a>

```
POST /amazonclouddirectory/2017-01-11/object/attributes HTTP/1.1
x-amz-data-partition: {{DirectoryArn}}
x-amz-consistency-level: {{ConsistencyLevel}}
Content-type: application/json

{
   "FacetFilter": {
      "FacetName": "{{string}}",
      "SchemaArn": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ObjectReference": {
      "Selector": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListObjectAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConsistencyLevel](#API_ListObjectAttributes_RequestSyntax) **   <a name="amazoncds-ListObjectAttributes-request-ConsistencyLevel"></a>
Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
Valid Values: `SERIALIZABLE | EVENTUAL`

 ** [DirectoryArn](#API_ListObjectAttributes_RequestSyntax) **   <a name="amazoncds-ListObjectAttributes-request-DirectoryArn"></a>
The Amazon Resource Name (ARN) that is associated with the [Directory](API_Directory.md) where the object resides. For more information, see [Arn Examples](arns.md).
Required: Yes

## Request Body
<a name="API_ListObjectAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FacetFilter](#API_ListObjectAttributes_RequestSyntax) **   <a name="amazoncds-ListObjectAttributes-request-FacetFilter"></a>
Used to filter the list of object attributes that are associated with a certain facet.
Type: [SchemaFacet](API_SchemaFacet.md) object
Required: No

 ** [MaxResults](#API_ListObjectAttributes_RequestSyntax) **   <a name="amazoncds-ListObjectAttributes-request-MaxResults"></a>
The maximum number of items to be retrieved in a single call. This is an approximate number.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListObjectAttributes_RequestSyntax) **   <a name="amazoncds-ListObjectAttributes-request-NextToken"></a>
The pagination token.
Type: String
Required: No

 ** [ObjectReference](#API_ListObjectAttributes_RequestSyntax) **   <a name="amazoncds-ListObjectAttributes-request-ObjectReference"></a>
The reference that identifies the object whose attributes will be listed.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

## Response Syntax
<a name="API_ListObjectAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Attributes": [
      {
         "Key": {
            "FacetName": "string",
            "Name": "string",
            "SchemaArn": "string"
         },
         "Value": {
            "BinaryValue": blob,
            "BooleanValue": boolean,
            "DatetimeValue": number,
            "NumberValue": "string",
            "StringValue": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListObjectAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attributes](#API_ListObjectAttributes_ResponseSyntax) **   <a name="amazoncds-ListObjectAttributes-response-Attributes"></a>
Attributes map that is associated with the object. `AttributeArn` is the key, and attribute value is the value.
Type: Array of [AttributeKeyAndValue](API_AttributeKeyAndValue.md) objects

 ** [NextToken](#API_ListObjectAttributes_ResponseSyntax) **   <a name="amazoncds-ListObjectAttributes-response-NextToken"></a>
The pagination token.
Type: String

## Errors
<a name="API_ListObjectAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md) and check your permissions.
HTTP Status Code: 403

 ** DirectoryNotEnabledException **
Operations are only permitted on enabled directories.
HTTP Status Code: 400

 ** FacetValidationException **
The [Facet](API_Facet.md) that you provided was not well formed or could not be validated with the schema.
HTTP Status Code: 400

 ** InternalServiceException **
Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/) site to see if there are any operational issues with the service.
HTTP Status Code: 500

 ** InvalidArnException **
Indicates that the provided ARN value is not valid.
HTTP Status Code: 400

 ** InvalidNextTokenException **
Indicates that the `NextToken` value is not valid.
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
<a name="API_ListObjectAttributes_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_ListObjectAttributes_Example_1"></a>

This example illustrates one usage of ListObjectAttributes.

```
POST /amazonclouddirectory/2017-01-11/object/attributes HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 84
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171017/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=192bfef84370989cc0ccc0760a138e2e49e4454e467f2247d98112507bee7ed7
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY
X-Amz-Date: 20171017T221819Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"ObjectReference": {
		"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TW45F26R1HTY2z-stwKBte_Q"
	}
}
```

### Example Response
<a name="API_ListObjectAttributes_Example_2"></a>

This example illustrates one usage of ListObjectAttributes.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 151ad236-b389-11e7-a6de-b54884d62153
Date: Tue, 17 Oct 2017 22:18:19 GMT
x-amzn-RequestId: 151ad236-b389-11e7-a6de-b54884d62153
Content-Type: application/json
Content-Length: 725

{
	"Attributes": [{
		"Key": {
			"FacetName": "INDEX",
			"Name": "index_is_unique",
			"SchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/CloudDirectory/1.0"
		},
		"Value": {
			"BinaryValue": null,
			"BooleanValue": true,
			"DatetimeValue": null,
			"NumberValue": null,
			"StringValue": null
		}
	}, {
		"Key": {
			"FacetName": "INDEX",
			"Name": "ordered_indexed_attributes",
			"SchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/CloudDirectory/1.0"
		},
		"Value": {
			"BinaryValue": null,
			"BooleanValue": null,
			"DatetimeValue": null,
			"NumberValue": null,
			"StringValue": "arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1*Organization*description"
		}
	}],
	"NextToken": null
}
```

## See Also
<a name="API_ListObjectAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ListObjectAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/clouddirectory-2017-01-11/ListObjectAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ListObjectAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ListObjectAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ListObjectAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ListObjectAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ListObjectAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ListObjectAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ListObjectAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ListObjectAttributes)
