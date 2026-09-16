---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_GetSchemaAsJson.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# GetSchemaAsJson
<a name="API_GetSchemaAsJson"></a>

Retrieves a JSON representation of the schema. See [JSON Schema Format](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_jsonformat.html#schemas_json) for more information.

## Request Syntax
<a name="API_GetSchemaAsJson_RequestSyntax"></a>

```
POST /amazonclouddirectory/2017-01-11/schema/json HTTP/1.1
x-amz-data-partition: {{SchemaArn}}
```

## URI Request Parameters
<a name="API_GetSchemaAsJson_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SchemaArn](#API_GetSchemaAsJson_RequestSyntax) **   <a name="amazoncds-GetSchemaAsJson-request-SchemaArn"></a>
The ARN of the schema to retrieve.
Required: Yes

## Request Body
<a name="API_GetSchemaAsJson_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSchemaAsJson_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Document": "string",
   "Name": "string"
}
```

## Response Elements
<a name="API_GetSchemaAsJson_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Document](#API_GetSchemaAsJson_ResponseSyntax) **   <a name="amazoncds-GetSchemaAsJson-response-Document"></a>
The JSON representation of the schema document.
Type: String

 ** [Name](#API_GetSchemaAsJson_ResponseSyntax) **   <a name="amazoncds-GetSchemaAsJson-response-Name"></a>
The name of the retrieved schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-zA-Z0-9._-]*$`

## Errors
<a name="API_GetSchemaAsJson_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource could not be found.
HTTP Status Code: 404

 ** RetryableConflictException **
Occurs when a conflict with a previous successful write is detected. For example, if a write operation occurs on an object and then an attempt is made to read the object using “SERIALIZABLE” consistency, this exception may result. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
HTTP Status Code: 409

 ** ValidationException **
Indicates that your request is malformed in some manner. See the exception message.
HTTP Status Code: 400

 ** ValidationException **
Indicates that your request is malformed in some manner. See the exception message.
HTTP Status Code: 400

## Examples
<a name="API_GetSchemaAsJson_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_GetSchemaAsJson_Example_1"></a>

This example illustrates one usage of GetSchemaAsJson.

```
POST /amazonclouddirectory/2017-01-11/schema/json HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 0
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171005/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=1cac388e2c4c4fb13c1fa5d0dfceaffc827acddf559c1706168a5fd84932e4d6
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1
X-Amz-Date: 20171005T204308Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8
```

### Example Response
<a name="API_GetSchemaAsJson_Example_2"></a>

This example illustrates one usage of GetSchemaAsJson.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cc541a4e-aa0d-11e7-9e13-5b6a00750e59
Date: Thu, 05 Oct 2017 20:43:09 GMT
x-amzn-RequestId: cc541a4e-aa0d-11e7-9e13-5b6a00750e59
Content-Type: application/json
Content-Length: 6938

{
	"Document": "{\"sourceSchemaArn\":\"arn:aws:clouddirectory:us-west-2:45132example:schema/published/org/1\",\"facets\":{\"node2\":{\"facetAttributes\":{},\"objectType\":\"NODE\"},\"Organization\":{\"facetAttributes\":{\"account_id\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"account_name\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"telephone_number\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"description\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (country)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (state)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (street2)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (street1)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"web_site\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"email\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (city)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"organization_status\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (postal_code)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"}},\"objectType\":\"LEAF_NODE\"},\"nodex\":{\"facetAttributes\":{},\"objectType\":\"NODE\"},\"Legal_Entity\":{\"facetAttributes\":{\"industry_vertical\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"registered_company_name\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"billing_currency\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (country)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (state)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (street2)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (street1)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"tax_id\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (city)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"},\"mailing_address (postal_code)\":{\"attributeDefinition\":{\"attributeType\":\"STRING\",\"isImmutable\":false,\"attributeRules\":{\"nameLength\":{\"parameters\":{\"min\":\"1\",\"max\":\"1024\"},\"ruleType\":\"STRING_LENGTH\"}}},\"requiredBehavior\":\"NOT_REQUIRED\"}},\"objectType\":\"LEAF_NODE\"},\"policyfacet\":{\"facetAttributes\":{},\"objectType\":\"POLICY\"},\"node1\":{\"facetAttributes\":{},\"objectType\":\"NODE\"}},\"typedLinkFacets\":{\"exampletypedlink\":{\"facetAttributes\":{\"1\":{\"attributeDefinition\":{\"attributeType\":\"BINARY\",\"isImmutable\":false,\"attributeRules\":{}},\"requiredBehavior\":\"REQUIRED_ALWAYS\"}},\"identityAttributeOrder\":[\"1\"]},\"exampletypedlink8\":{\"facetAttributes\":{\"22\":{\"attributeDefinition\":{\"attributeType\":\"BINARY\",\"isImmutable\":false,\"attributeRules\":{}},\"requiredBehavior\":\"REQUIRED_ALWAYS\"}},\"identityAttributeOrder\":[\"22\"]}}}",
	"Name": "org"
}
```

## See Also
<a name="API_GetSchemaAsJson_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/GetSchemaAsJson)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/clouddirectory-2017-01-11/GetSchemaAsJson)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/GetSchemaAsJson)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/GetSchemaAsJson)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/GetSchemaAsJson)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/GetSchemaAsJson)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/GetSchemaAsJson)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/GetSchemaAsJson)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/GetSchemaAsJson)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/GetSchemaAsJson)
