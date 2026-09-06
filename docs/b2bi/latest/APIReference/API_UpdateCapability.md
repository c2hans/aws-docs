---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UpdateCapability.html
---

# UpdateCapability
<a name="API_UpdateCapability"></a>

Updates some of the parameters for a capability, based on the specified parameters. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.

## Request Syntax
<a name="API_UpdateCapability_RequestSyntax"></a>

```
{
   "capabilityId": "{{string}}",
   "configuration": { ... },
   "instructionsDocuments": [
      {
         "bucketName": "{{string}}",
         "key": "{{string}}"
      }
   ],
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCapability_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [capabilityId](#API_UpdateCapability_RequestSyntax) **   <a name="b2bi-UpdateCapability-request-capabilityId"></a>
Specifies a system-assigned unique identifier for the capability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [configuration](#API_UpdateCapability_RequestSyntax) **   <a name="b2bi-UpdateCapability-request-configuration"></a>
Specifies a structure that contains the details for a capability.
Type: [CapabilityConfiguration](API_CapabilityConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [instructionsDocuments](#API_UpdateCapability_RequestSyntax) **   <a name="b2bi-UpdateCapability-request-instructionsDocuments"></a>
Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.
Type: Array of [S3Location](API_S3Location.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [name](#API_UpdateCapability_RequestSyntax) **   <a name="b2bi-UpdateCapability-request-name"></a>
Specifies a new name for the capability, to replace the existing name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Required: No

## Response Syntax
<a name="API_UpdateCapability_ResponseSyntax"></a>

```
{
   "capabilityArn": "string",
   "capabilityId": "string",
   "configuration": { ... },
   "createdAt": "string",
   "instructionsDocuments": [
      {
         "bucketName": "string",
         "key": "string"
      }
   ],
   "modifiedAt": "string",
   "name": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_UpdateCapability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capabilityArn](#API_UpdateCapability_ResponseSyntax) **   <a name="b2bi-UpdateCapability-response-capabilityArn"></a>
Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [capabilityId](#API_UpdateCapability_ResponseSyntax) **   <a name="b2bi-UpdateCapability-response-capabilityId"></a>
Returns a system-assigned unique identifier for the capability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [configuration](#API_UpdateCapability_ResponseSyntax) **   <a name="b2bi-UpdateCapability-response-configuration"></a>
Returns a structure that contains the details for a capability.
Type: [CapabilityConfiguration](API_CapabilityConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_UpdateCapability_ResponseSyntax) **   <a name="b2bi-UpdateCapability-response-createdAt"></a>
Returns a timestamp for creation date and time of the capability.
Type: Timestamp

 ** [instructionsDocuments](#API_UpdateCapability_ResponseSyntax) **   <a name="b2bi-UpdateCapability-response-instructionsDocuments"></a>
Returns one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.
Type: Array of [S3Location](API_S3Location.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [modifiedAt](#API_UpdateCapability_ResponseSyntax) **   <a name="b2bi-UpdateCapability-response-modifiedAt"></a>
Returns a timestamp for last time the capability was modified.
Type: Timestamp

 ** [name](#API_UpdateCapability_ResponseSyntax) **   <a name="b2bi-UpdateCapability-response-name"></a>
Returns the name of the capability, used to identify it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.

 ** [type](#API_UpdateCapability_ResponseSyntax) **   <a name="b2bi-UpdateCapability-response-type"></a>
Returns the type of the capability. Currently, only `edi` is supported.
Type: String
Valid Values: `edi`

## Errors
<a name="API_UpdateCapability_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.
HTTP Status Code: 400

 ** InternalServerException **
This exception is thrown when an error occurs in the AWS B2B Data Interchange service.
 ** retryAfterSeconds **
The server attempts to retry a failed command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.
 ** quotaCode **
The quota that was exceeded, which caused the exception.
 ** resourceId **
The ID for the resource that exceeded the quota, which caused the exception.
 ** resourceType **
The resource type (profile, partnership, transformer, or capability) that exceeded the quota, which caused the exception.
 ** serviceCode **
The code responsible for exceeding the quota, which caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.
 ** retryAfterSeconds **
The server attempts to retry a command that was throttled.
HTTP Status Code: 400

 ** ValidationException **
When you use Transformer APIs, `TestConversion`, or `TestParsing`, the service throws a validation exception if a rule is configured incorrectly. For example, a validation exception occurs when:
+ A rule references an element that doesn't exist in the selected transaction set
+ An element length rule specifies a minimum length less than 0
If your custom validation rules are configured correctly but the EDI validation fails due to those rules, this is expected behavior and doesn't result in a `ValidationException`.
For all other API operations, a validation exception occurs when a Trading Partner object can't be validated against a request from another object. This can happen during:
+ Standard EDI validation
+ Custom validation rule evaluation, such as when:
  + Element lengths don't meet specified constraints
  + Code list validations contain invalid codes
  + Required elements are missing based on your element requirement rules
HTTP Status Code: 400

## Examples
<a name="API_UpdateCapability_Examples"></a>

### Example
<a name="API_UpdateCapability_Example_1"></a>

The following example updates a capability.

#### Sample Request
<a name="API_UpdateCapability_Example_1_Request"></a>

```
{
    "capabilityId": "ca-1111aaaa2222bbbb3",
    "name": "b2biexample",
    "instructionsDocuments": [
        {
            "bucketName": "amzn-s3-demo-bucket",
            "key": "instructiondoc.txt"
        }
    ],
    "configuration": {
        "edi": {
            "type": {
                "x12Details": {
                    "transactionSet": "X12_110",
                    "version": "VERSION_4010"
                }
            },
            "inputLocation": {
                "bucketName": "amzn-s3-demo-bucket",
                "key": "input/"
            },
            "outputLocation": {
                "bucketName": "amzn-s3-demo-bucket",
                "key": "output/"
            },
            "transformerId": "tr-1234abcd5678efghj"
        }
    }
}
```

#### Sample Response
<a name="API_UpdateCapability_Example_1_Response"></a>

```
{
    "capabilityArn": "arn:aws:b2bi:us-west-2:123456789012:capability/ca-1111aaaa2222bbbb3",
    "capabilityId": "ca-1111aaaa2222bbbb3",
    "configuration": {
        "edi": {
            "type": {
                "x12Details": {
                    "transactionSet": "X12_110",
                    "version": "VERSION_4010"
                }
            },
            "inputLocation": {
                "bucketName": "amzn-s3-demo-bucket",
                "key": "input/"
            },
            "outputLocation": {
                "bucketName": "amzn-s3-demo-bucket",
                "key": "output/"
            },
            "transformerId": "tr-1234abcd5678efghj"
        }
    },
    "createdAt": "2023-11-01T21:51:05.504Z",
    "instructionsDocuments": [
        {
            "bucketName": "amzn-s3-demo-bucket",
            "key": "instructiondoc.txt"
        }
    ],
    "modifiedAt": "2023-11-01T21:51:05.504Z",
    "name": "b2biexample",
    "type": "edi"
}
```

## See Also
<a name="API_UpdateCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/UpdateCapability)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/UpdateCapability)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/UpdateCapability)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/UpdateCapability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/UpdateCapability)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/UpdateCapability)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/UpdateCapability)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/UpdateCapability)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/UpdateCapability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/UpdateCapability)
