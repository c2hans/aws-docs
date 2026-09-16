---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListIncomingTypedLinks.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# ListIncomingTypedLinks
<a name="API_ListIncomingTypedLinks"></a>

Returns a paginated list of all the incoming [TypedLinkSpecifier](API_TypedLinkSpecifier.md) information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink).

## Request Syntax
<a name="API_ListIncomingTypedLinks_RequestSyntax"></a>

```
POST /amazonclouddirectory/2017-01-11/typedlink/incoming HTTP/1.1
x-amz-data-partition: {{DirectoryArn}}
Content-type: application/json

{
   "ConsistencyLevel": "{{string}}",
   "FilterAttributeRanges": [
      {
         "AttributeName": "{{string}}",
         "Range": {
            "EndMode": "{{string}}",
            "EndValue": {
               "BinaryValue": {{blob}},
               "BooleanValue": {{boolean}},
               "DatetimeValue": {{number}},
               "NumberValue": "{{string}}",
               "StringValue": "{{string}}"
            },
            "StartMode": "{{string}}",
            "StartValue": {
               "BinaryValue": {{blob}},
               "BooleanValue": {{boolean}},
               "DatetimeValue": {{number}},
               "NumberValue": "{{string}}",
               "StringValue": "{{string}}"
            }
         }
      }
   ],
   "FilterTypedLink": {
      "SchemaArn": "{{string}}",
      "TypedLinkName": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ObjectReference": {
      "Selector": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListIncomingTypedLinks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DirectoryArn](#API_ListIncomingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListIncomingTypedLinks-request-DirectoryArn"></a>
The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
Required: Yes

## Request Body
<a name="API_ListIncomingTypedLinks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConsistencyLevel](#API_ListIncomingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListIncomingTypedLinks-request-ConsistencyLevel"></a>
The consistency level to execute the request at.
Type: String
Valid Values: `SERIALIZABLE | EVENTUAL`
Required: No

 ** [FilterAttributeRanges](#API_ListIncomingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListIncomingTypedLinks-request-FilterAttributeRanges"></a>
Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.
Type: Array of [TypedLinkAttributeRange](API_TypedLinkAttributeRange.md) objects
Required: No

 ** [FilterTypedLink](#API_ListIncomingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListIncomingTypedLinks-request-FilterTypedLink"></a>
Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls.
Type: [TypedLinkSchemaAndFacetName](API_TypedLinkSchemaAndFacetName.md) object
Required: No

 ** [MaxResults](#API_ListIncomingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListIncomingTypedLinks-request-MaxResults"></a>
The maximum number of results to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListIncomingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListIncomingTypedLinks-request-NextToken"></a>
The pagination token.
Type: String
Required: No

 ** [ObjectReference](#API_ListIncomingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListIncomingTypedLinks-request-ObjectReference"></a>
Reference that identifies the object whose attributes will be listed.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

## Response Syntax
<a name="API_ListIncomingTypedLinks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LinkSpecifiers": [
      {
         "IdentityAttributeValues": [
            {
               "AttributeName": "string",
               "Value": {
                  "BinaryValue": blob,
                  "BooleanValue": boolean,
                  "DatetimeValue": number,
                  "NumberValue": "string",
                  "StringValue": "string"
               }
            }
         ],
         "SourceObjectReference": {
            "Selector": "string"
         },
         "TargetObjectReference": {
            "Selector": "string"
         },
         "TypedLinkFacet": {
            "SchemaArn": "string",
            "TypedLinkName": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListIncomingTypedLinks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LinkSpecifiers](#API_ListIncomingTypedLinks_ResponseSyntax) **   <a name="amazoncds-ListIncomingTypedLinks-response-LinkSpecifiers"></a>
Returns one or more typed link specifiers as output.
Type: Array of [TypedLinkSpecifier](API_TypedLinkSpecifier.md) objects

 ** [NextToken](#API_ListIncomingTypedLinks_ResponseSyntax) **   <a name="amazoncds-ListIncomingTypedLinks-response-NextToken"></a>
The pagination token.
Type: String

## Errors
<a name="API_ListIncomingTypedLinks_Errors"></a>

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
<a name="API_ListIncomingTypedLinks_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_ListIncomingTypedLinks_Example_1"></a>

This example illustrates one usage of ListIncomingTypedLinks.

```
POST /amazonclouddirectory/2017-01-11/typedlink/incoming HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 84
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171017/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=fc13e2c9fb358918b87ada72c9dca32938fc33cf83e7774394fce55d755001dc
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY
X-Amz-Date: 20171017T204458Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"ObjectReference": {
		"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw"
	}
}
```

### Example Response
<a name="API_ListIncomingTypedLinks_Example_2"></a>

This example illustrates one usage of ListIncomingTypedLinks.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0b1ebdf5-b37c-11e7-9e13-5b6a00750e59
Date: Tue, 17 Oct 2017 20:45:00 GMT
x-amzn-RequestId: 0b1ebdf5-b37c-11e7-9e13-5b6a00750e59
Content-Type: application/json
Content-Length: 1530

{
	"LinkSpecifiers": [{
		"IdentityAttributeValues": [{
			"AttributeName": "22",
			"Value": {
				"BinaryValue": "",
				"BooleanValue": null,
				"DatetimeValue": null,
				"NumberValue": null,
				"StringValue": null
			}
		}],
		"SourceObjectReference": {
			"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWSvfuEnDqTdmeCuTs6YBNUA"
		},
		"TargetObjectReference": {
			"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw"
		},
		"TypedLinkFacet": {
			"SchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1",
			"TypedLinkName": "exampletypedlink8"
		}
	}, {
		"IdentityAttributeValues": [{
			"AttributeName": "22",
			"Value": {
				"BinaryValue": "MA==",
				"BooleanValue": null,
				"DatetimeValue": null,
				"NumberValue": null,
				"StringValue": null
			}
		}],
		"SourceObjectReference": {
			"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWSvfuEnDqTdmeCuTs6YBNUA"
		},
		"TargetObjectReference": {
			"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw"
		},
		"TypedLinkFacet": {
			"SchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1",
			"TypedLinkName": "exampletypedlink8"
		}
	}, {
		"IdentityAttributeValues": [{
			"AttributeName": "22",
			"Value": {
				"BinaryValue": "c3Ry",
				"BooleanValue": null,
				"DatetimeValue": null,
				"NumberValue": null,
				"StringValue": null
			}
		}],
		"SourceObjectReference": {
			"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWSvfuEnDqTdmeCuTs6YBNUA"
		},
		"TargetObjectReference": {
			"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw"
		},
		"TypedLinkFacet": {
			"SchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1",
			"TypedLinkName": "exampletypedlink8"
		}
	}],
	"NextToken": null
}
```

## See Also
<a name="API_ListIncomingTypedLinks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ListIncomingTypedLinks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/clouddirectory-2017-01-11/ListIncomingTypedLinks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ListIncomingTypedLinks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ListIncomingTypedLinks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ListIncomingTypedLinks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ListIncomingTypedLinks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ListIncomingTypedLinks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ListIncomingTypedLinks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ListIncomingTypedLinks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ListIncomingTypedLinks)
