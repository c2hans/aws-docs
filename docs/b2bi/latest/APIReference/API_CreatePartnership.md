---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreatePartnership.html
---

# CreatePartnership
<a name="API_CreatePartnership"></a>

Creates a partnership between a customer and a trading partner, based on the supplied parameters. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.

## Request Syntax
<a name="API_CreatePartnership_RequestSyntax"></a>

```
{
   "capabilities": [ "{{string}}" ],
   "capabilityOptions": {
      "inboundEdi": {
         "x12": {
            "acknowledgmentOptions": {
               "functionalAcknowledgment": "{{string}}",
               "technicalAcknowledgment": "{{string}}"
            }
         }
      },
      "outboundEdi": { ... }
   },
   "clientToken": "{{string}}",
   "email": "{{string}}",
   "name": "{{string}}",
   "phone": "{{string}}",
   "profileId": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreatePartnership_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [capabilities](#API_CreatePartnership_RequestSyntax) **   <a name="b2bi-CreatePartnership-request-capabilities"></a>
Specifies a list of the capabilities associated with this partnership.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [capabilityOptions](#API_CreatePartnership_RequestSyntax) **   <a name="b2bi-CreatePartnership-request-capabilityOptions"></a>
Specify the structure that contains the details for the associated capabilities.
Type: [CapabilityOptions](API_CapabilityOptions.md) object
Required: No

 ** [clientToken](#API_CreatePartnership_RequestSyntax) **   <a name="b2bi-CreatePartnership-request-clientToken"></a>
Reserved for future use.
Type: String
Required: No

 ** [email](#API_CreatePartnership_RequestSyntax) **   <a name="b2bi-CreatePartnership-request-email"></a>
Specifies the email address associated with this trading partner.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 254.
Pattern: `[\w\.\-]+@[\w\.\-]+`
Required: Yes

 ** [name](#API_CreatePartnership_RequestSyntax) **   <a name="b2bi-CreatePartnership-request-name"></a>
Specifies a descriptive name for the partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Required: Yes

 ** [phone](#API_CreatePartnership_RequestSyntax) **   <a name="b2bi-CreatePartnership-request-phone"></a>
Specifies the phone number associated with the partnership.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 22.
Pattern: `\+?([0-9 \t\-()\/]{7,})(?:\s*(?:#|x\.?|ext\.?|extension) \t*(\d+))?`
Required: No

 ** [profileId](#API_CreatePartnership_RequestSyntax) **   <a name="b2bi-CreatePartnership-request-profileId"></a>
Specifies the unique, system-generated identifier for the profile connected to this partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [tags](#API_CreatePartnership_RequestSyntax) **   <a name="b2bi-CreatePartnership-request-tags"></a>
Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreatePartnership_ResponseSyntax"></a>

```
{
   "capabilities": [ "string" ],
   "capabilityOptions": {
      "inboundEdi": {
         "x12": {
            "acknowledgmentOptions": {
               "functionalAcknowledgment": "string",
               "technicalAcknowledgment": "string"
            }
         }
      },
      "outboundEdi": { ... }
   },
   "createdAt": "string",
   "email": "string",
   "name": "string",
   "partnershipArn": "string",
   "partnershipId": "string",
   "phone": "string",
   "profileId": "string",
   "tradingPartnerId": "string"
}
```

## Response Elements
<a name="API_CreatePartnership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capabilities](#API_CreatePartnership_ResponseSyntax) **   <a name="b2bi-CreatePartnership-response-capabilities"></a>
Returns one or more capabilities associated with this partnership.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [capabilityOptions](#API_CreatePartnership_ResponseSyntax) **   <a name="b2bi-CreatePartnership-response-capabilityOptions"></a>
Returns the structure that contains the details for the associated capabilities.
Type: [CapabilityOptions](API_CapabilityOptions.md) object

 ** [createdAt](#API_CreatePartnership_ResponseSyntax) **   <a name="b2bi-CreatePartnership-response-createdAt"></a>
Returns a timestamp for creation date and time of the partnership.
Type: Timestamp

 ** [email](#API_CreatePartnership_ResponseSyntax) **   <a name="b2bi-CreatePartnership-response-email"></a>
Returns the email address associated with this trading partner.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 254.
Pattern: `[\w\.\-]+@[\w\.\-]+`

 ** [name](#API_CreatePartnership_ResponseSyntax) **   <a name="b2bi-CreatePartnership-response-name"></a>
Returns a descriptive name for the partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.

 ** [partnershipArn](#API_CreatePartnership_ResponseSyntax) **   <a name="b2bi-CreatePartnership-response-partnershipArn"></a>
Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [partnershipId](#API_CreatePartnership_ResponseSyntax) **   <a name="b2bi-CreatePartnership-response-partnershipId"></a>
Returns the unique, system-generated identifier for a partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [phone](#API_CreatePartnership_ResponseSyntax) **   <a name="b2bi-CreatePartnership-response-phone"></a>
Returns the phone number associated with the partnership.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 22.
Pattern: `\+?([0-9 \t\-()\/]{7,})(?:\s*(?:#|x\.?|ext\.?|extension) \t*(\d+))?`

 ** [profileId](#API_CreatePartnership_ResponseSyntax) **   <a name="b2bi-CreatePartnership-response-profileId"></a>
Returns the unique, system-generated identifier for the profile connected to this partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [tradingPartnerId](#API_CreatePartnership_ResponseSyntax) **   <a name="b2bi-CreatePartnership-response-tradingPartnerId"></a>
Returns the unique, system-generated identifier for a trading partner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_CreatePartnership_Errors"></a>

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
<a name="API_CreatePartnership_Examples"></a>

### Example
<a name="API_CreatePartnership_Example_1"></a>

The following example creates a partnership. In the command, replace the parameters with your actual values for the new partnership.

The API call returns the details for you new partnership.

```
//Listing for createNewPartnership.txt
{
    "profileId": "p-ABCDE111122223333",
    "name": "John Smith",
    "email": "johns@example.com",
    "phone": "5555555555",
    "capabilities": [
         "ca-1111aaaa2222bbbb3"
    ],
    "capabilityOptions": {
        "outboundEdi": {
            "x12": {
                "common": {
                    "delimiters": {
                        "componentSeparator": ":",
                        "dataElementSeparator": ";",
                        "replacementCharacterSeparator": ",",
                        "segmentTerminator": "/"
                    },
                    "ediValidate": true
                }
            }
        }
    },
    "clientToken": "foo",
    "tags": [
        {
            "Key": "Test",
            "Value": "True"
        }
    ]
}
```

#### Sample Request
<a name="API_CreatePartnership_Example_1_Request"></a>

```
aws b2bi create-partnership --cli-input-json file://createNewPartnership.txt
```

#### Sample Response
<a name="API_CreatePartnership_Example_1_Response"></a>

```
{
    "profileId": "p-ABCDE111122223333",
    "partnershipId": "ps-7444460000cccc1111",
    "partnershipArn": "arn:aws:b2bi:us-east-1:500655546075:partnership/ps-444460000cccc1111",
    "name": "John Smith",
    "email": "johns@example.com",
    "phone": "5555555555",
    "capabilities": [
        "ca-1111aaaa2222bbbb3"
    ],
    "capabilityOptions": {
        "outboundEdi": {
            "x12": {
                "common": {
                    "delimiters": {
                        "componentSeparator": ":",
                        "dataElementSeparator": ";",
                        "segmentTerminator": "/"
                    }
                }
            }
        }
    },
    "tradingPartnerId": tp-1234abcd5678efghj",
    "createdAt": "2024-10-15T17:27:20.972Z"
}
```

### Example
<a name="API_CreatePartnership_Example_2"></a>

The following example creates a partnership with acknowledgment configuration, format configuration, and control number settings.

```
//Listing for createPartnershipWithAcknowledgment.txt
{
    "profileId": "p-ABCDE111122223333",
    "name": "John Smith",
    "email": "johns@example.com",
    "phone": "5555555555",
    "capabilities": [
         "ca-1111aaaa2222bbbb3"
    ],
    "capabilityOptions": {
        "outboundEdi": {
            "x12": {
                "common": {
                    "delimiters": {
                        "componentSeparator": ":",
                        "dataElementSeparator": ";",
                        "replacementCharacterSeparator": ",",
                        "segmentTerminator": "/"
                    },
                    "ediValidate": true,
                    "wrapOptions": {
                        "wrapBy": "SEGMENT",
                        "lineTerminator": "\n"
                    }
                },
                "headers": {
                    "controlNumbers": {
                        "startingInterchangeControlNumber": "000000001",
                        "startingFunctionalGroupControlNumber": "1",
                        "startingTransactionSetControlNumber": "0001"
                    },
                    "gs05TimeFormat": "HHMMSS"
                }
            }
        },
        "inboundEdi": {
            "x12": {
                "acknowledgmentOptions": {
                    "functionalAcknowledgment": "GENERATE_ALL_SEGMENTS",
                    "technicalAcknowledgment": "GENERATE_ALL_SEGMENTS"
                }
            }
        }
    },
    "clientToken": "foo",
    "tags": [
        {
            "Key": "Test",
            "Value": "True"
        }
    ]
}
```

#### Sample Request
<a name="API_CreatePartnership_Example_2_Request"></a>

```
aws b2bi create-partnership --cli-input-json file://createPartnershipWithAcknowledgment.txt
```

#### Sample Response
<a name="API_CreatePartnership_Example_2_Response"></a>

```
{
    "profileId": "p-ABCDE111122223333",
    "partnershipId": "ps-7444460000cccc1111",
    "partnershipArn": "arn:aws:b2bi:us-east-1:500655546075:partnership/ps-444460000cccc1111",
    "name": "John Smith",
    "email": "johns@example.com",
    "phone": "5555555555",
    "capabilities": [
        "ca-1111aaaa2222bbbb3"
    ],
    "capabilityOptions": {
        "outboundEdi": {
            "x12": {
                "common": {
                    "delimiters": {
                        "componentSeparator": ":",
                        "dataElementSeparator": ";",
                        "segmentTerminator": "/"
                    },
                    "ediValidate": true,
                    "wrapOptions": {
                        "wrapBy": "SEGMENT",
                        "lineTerminator": "\n"
                    }
                },
                "headers": {
                    "controlNumbers": {
                        "startingInterchangeControlNumber": "000000001",
                        "startingFunctionalGroupControlNumber": "1",
                        "startingTransactionSetControlNumber": "0001"
                    },
                    "gs05TimeFormat": "HHMMSS"
                }
            }
        },
        "inboundEdi": {
            "x12": {
                "acknowledgmentOptions": {
                    "functionalAcknowledgment": "GENERATE_ALL_SEGMENTS",
                    "technicalAcknowledgment": "GENERATE_ALL_SEGMENTS"
                }
            }
        }
    },
    "tradingPartnerId": "tp-1234abcd5678efghj",
    "createdAt": "2024-10-15T17:27:20.972Z"
}
```

## See Also
<a name="API_CreatePartnership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/CreatePartnership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/CreatePartnership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/CreatePartnership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/CreatePartnership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/CreatePartnership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/CreatePartnership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/CreatePartnership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/CreatePartnership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/CreatePartnership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/CreatePartnership)
