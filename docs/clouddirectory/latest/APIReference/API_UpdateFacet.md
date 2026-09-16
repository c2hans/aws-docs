---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_UpdateFacet.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# UpdateFacet
<a name="API_UpdateFacet"></a>

Does the following:

1. Adds new `Attributes`, `Rules`, or `ObjectTypes`.

1. Updates existing `Attributes`, `Rules`, or `ObjectTypes`.

1. Deletes existing `Attributes`, `Rules`, or `ObjectTypes`.

## Request Syntax
<a name="API_UpdateFacet_RequestSyntax"></a>

```
PUT /amazonclouddirectory/2017-01-11/facet HTTP/1.1
x-amz-data-partition: {{SchemaArn}}
Content-type: application/json

{
   "AttributeUpdates": [
      {
         "Action": "{{string}}",
         "Attribute": {
            "AttributeDefinition": {
               "DefaultValue": {
                  "BinaryValue": {{blob}},
                  "BooleanValue": {{boolean}},
                  "DatetimeValue": {{number}},
                  "NumberValue": "{{string}}",
                  "StringValue": "{{string}}"
               },
               "IsImmutable": {{boolean}},
               "Rules": {
                  "{{string}}" : {
                     "Parameters": {
                        "{{string}}" : "{{string}}"
                     },
                     "Type": "{{string}}"
                  }
               },
               "Type": "{{string}}"
            },
            "AttributeReference": {
               "TargetAttributeName": "{{string}}",
               "TargetFacetName": "{{string}}"
            },
            "Name": "{{string}}",
            "RequiredBehavior": "{{string}}"
         }
      }
   ],
   "Name": "{{string}}",
   "ObjectType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateFacet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SchemaArn](#API_UpdateFacet_RequestSyntax) **   <a name="amazoncds-UpdateFacet-request-SchemaArn"></a>
The Amazon Resource Name (ARN) that is associated with the [Facet](API_Facet.md). For more information, see [Arn Examples](arns.md).
Required: Yes

## Request Body
<a name="API_UpdateFacet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AttributeUpdates](#API_UpdateFacet_RequestSyntax) **   <a name="amazoncds-UpdateFacet-request-AttributeUpdates"></a>
List of attributes that need to be updated in a given schema [Facet](API_Facet.md). Each attribute is followed by `AttributeAction`, which specifies the type of update operation to perform.
Type: Array of [FacetAttributeUpdate](API_FacetAttributeUpdate.md) objects
Required: No

 ** [Name](#API_UpdateFacet_RequestSyntax) **   <a name="amazoncds-UpdateFacet-request-Name"></a>
The name of the facet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

 ** [ObjectType](#API_UpdateFacet_RequestSyntax) **   <a name="amazoncds-UpdateFacet-request-ObjectType"></a>
The object type that is associated with the facet. See [CreateFacet:ObjectType](API_CreateFacet.md#amazoncds-CreateFacet-request-ObjectType) for more details.
Type: String
Valid Values: `NODE | LEAF_NODE | POLICY | INDEX`
Required: No

## Response Syntax
<a name="API_UpdateFacet_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateFacet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateFacet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md) and check your permissions.
HTTP Status Code: 403

 ** FacetNotFoundException **
The specified [Facet](API_Facet.md) could not be found.
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

 ** InvalidFacetUpdateException **
An attempt to modify a [Facet](API_Facet.md) resulted in an invalid schema exception.
HTTP Status Code: 400

 ** InvalidRuleException **
Occurs when any of the rule parameter keys or values are invalid.
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
<a name="API_UpdateFacet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/UpdateFacet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/clouddirectory-2017-01-11/UpdateFacet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/UpdateFacet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/UpdateFacet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/UpdateFacet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/UpdateFacet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/UpdateFacet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/UpdateFacet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/UpdateFacet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/UpdateFacet)
