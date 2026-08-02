---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify. The resource can be a capability, partnership, profile, or transformer.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_ListTagsForResource_RequestSyntax) **   <a name="b2bi-ListTagsForResource-request-ResourceARN"></a>
Requests the tags associated with a particular Amazon Resource Name (ARN). An ARN is an identifier for a specific AWS resource, such as a capability, partnership, profile, or transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="b2bi-ListTagsForResource-response-Tags"></a>
Returns the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This exception is thrown when an error occurs in the AWS B2B Data Interchange service.
 ** retryAfterSeconds **
The server attempts to retry a failed command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.
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
<a name="API_ListTagsForResource_Examples"></a>

### Example
<a name="API_ListTagsForResource_Example_1"></a>

The following example lists the tags for the specified profile.

#### Sample Request
<a name="API_ListTagsForResource_Example_1_Request"></a>

```
{
    "ResourceARN": "arn:aws:b2bi:us-west-2:123456789012:profile/p-ABCDE111122223333"
}
```

#### Sample Response
<a name="API_ListTagsForResource_Example_1_Response"></a>

```
{
    "Tags": [
        {
            "Key": "sampleKey",
            "Value": "SampleValue"
        }
    ]
}
```

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/ListTagsForResource)
