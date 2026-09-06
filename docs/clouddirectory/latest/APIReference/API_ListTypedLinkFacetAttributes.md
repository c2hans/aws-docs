---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListTypedLinkFacetAttributes.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# ListTypedLinkFacetAttributes
<a name="API_ListTypedLinkFacetAttributes"></a>

Returns a paginated list of all attribute definitions for a particular [TypedLinkFacet](API_TypedLinkFacet.md). For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink).

## Request Syntax
<a name="API_ListTypedLinkFacetAttributes_RequestSyntax"></a>

```
POST /amazonclouddirectory/2017-01-11/typedlink/facet/attributes HTTP/1.1
x-amz-data-partition: {{SchemaArn}}
Content-type: application/json

{
   "MaxResults": {{number}},
   "Name": "{{string}}",
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListTypedLinkFacetAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SchemaArn](#API_ListTypedLinkFacetAttributes_RequestSyntax) **   <a name="amazoncds-ListTypedLinkFacetAttributes-request-SchemaArn"></a>
The Amazon Resource Name (ARN) that is associated with the schema. For more information, see [Arn Examples](arns.md).
Required: Yes

## Request Body
<a name="API_ListTypedLinkFacetAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListTypedLinkFacetAttributes_RequestSyntax) **   <a name="amazoncds-ListTypedLinkFacetAttributes-request-MaxResults"></a>
The maximum number of results to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Name](#API_ListTypedLinkFacetAttributes_RequestSyntax) **   <a name="amazoncds-ListTypedLinkFacetAttributes-request-Name"></a>
The unique name of the typed link facet.
Type: String
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

 ** [NextToken](#API_ListTypedLinkFacetAttributes_RequestSyntax) **   <a name="amazoncds-ListTypedLinkFacetAttributes-request-NextToken"></a>
The pagination token.
Type: String
Required: No

## Response Syntax
<a name="API_ListTypedLinkFacetAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Attributes": [
      {
         "DefaultValue": {
            "BinaryValue": blob,
            "BooleanValue": boolean,
            "DatetimeValue": number,
            "NumberValue": "string",
            "StringValue": "string"
         },
         "IsImmutable": boolean,
         "Name": "string",
         "RequiredBehavior": "string",
         "Rules": {
            "string" : {
               "Parameters": {
                  "string" : "string"
               },
               "Type": "string"
            }
         },
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListTypedLinkFacetAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attributes](#API_ListTypedLinkFacetAttributes_ResponseSyntax) **   <a name="amazoncds-ListTypedLinkFacetAttributes-response-Attributes"></a>
An ordered set of attributes associate with the typed link.
Type: Array of [TypedLinkAttributeDefinition](API_TypedLinkAttributeDefinition.md) objects

 ** [NextToken](#API_ListTypedLinkFacetAttributes_ResponseSyntax) **   <a name="amazoncds-ListTypedLinkFacetAttributes-response-NextToken"></a>
The pagination token.
Type: String

## Errors
<a name="API_ListTypedLinkFacetAttributes_Errors"></a>

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

## See Also
<a name="API_ListTypedLinkFacetAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes)
