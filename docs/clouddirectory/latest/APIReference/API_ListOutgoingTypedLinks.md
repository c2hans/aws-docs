---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListOutgoingTypedLinks.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# ListOutgoingTypedLinks
<a name="API_ListOutgoingTypedLinks"></a>

Returns a paginated list of all the outgoing [TypedLinkSpecifier](API_TypedLinkSpecifier.md) information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink).

## Request Syntax
<a name="API_ListOutgoingTypedLinks_RequestSyntax"></a>

```
POST /amazonclouddirectory/2017-01-11/typedlink/outgoing HTTP/1.1
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
<a name="API_ListOutgoingTypedLinks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DirectoryArn](#API_ListOutgoingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListOutgoingTypedLinks-request-DirectoryArn"></a>
The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
Required: Yes

## Request Body
<a name="API_ListOutgoingTypedLinks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConsistencyLevel](#API_ListOutgoingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListOutgoingTypedLinks-request-ConsistencyLevel"></a>
The consistency level to execute the request at.
Type: String
Valid Values: `SERIALIZABLE | EVENTUAL`
Required: No

 ** [FilterAttributeRanges](#API_ListOutgoingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListOutgoingTypedLinks-request-FilterAttributeRanges"></a>
Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.
Type: Array of [TypedLinkAttributeRange](API_TypedLinkAttributeRange.md) objects
Required: No

 ** [FilterTypedLink](#API_ListOutgoingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListOutgoingTypedLinks-request-FilterTypedLink"></a>
Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.
Type: [TypedLinkSchemaAndFacetName](API_TypedLinkSchemaAndFacetName.md) object
Required: No

 ** [MaxResults](#API_ListOutgoingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListOutgoingTypedLinks-request-MaxResults"></a>
The maximum number of results to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListOutgoingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListOutgoingTypedLinks-request-NextToken"></a>
The pagination token.
Type: String
Required: No

 ** [ObjectReference](#API_ListOutgoingTypedLinks_RequestSyntax) **   <a name="amazoncds-ListOutgoingTypedLinks-request-ObjectReference"></a>
A reference that identifies the object whose attributes will be listed.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

## Response Syntax
<a name="API_ListOutgoingTypedLinks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TypedLinkSpecifiers": [
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
   ]
}
```

## Response Elements
<a name="API_ListOutgoingTypedLinks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOutgoingTypedLinks_ResponseSyntax) **   <a name="amazoncds-ListOutgoingTypedLinks-response-NextToken"></a>
The pagination token.
Type: String

 ** [TypedLinkSpecifiers](#API_ListOutgoingTypedLinks_ResponseSyntax) **   <a name="amazoncds-ListOutgoingTypedLinks-response-TypedLinkSpecifiers"></a>
Returns a typed link specifier as output.
Type: Array of [TypedLinkSpecifier](API_TypedLinkSpecifier.md) objects

## Errors
<a name="API_ListOutgoingTypedLinks_Errors"></a>

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

## See Also
<a name="API_ListOutgoingTypedLinks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ListOutgoingTypedLinks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/clouddirectory-2017-01-11/ListOutgoingTypedLinks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ListOutgoingTypedLinks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ListOutgoingTypedLinks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ListOutgoingTypedLinks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ListOutgoingTypedLinks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ListOutgoingTypedLinks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ListOutgoingTypedLinks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ListOutgoingTypedLinks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ListOutgoingTypedLinks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
