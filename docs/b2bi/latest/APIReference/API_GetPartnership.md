---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetPartnership.html
---

# GetPartnership
<a name="API_GetPartnership"></a>

Retrieves the details for a partnership, based on the partner and profile IDs specified. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.

## Request Syntax
<a name="API_GetPartnership_RequestSyntax"></a>

```
{
   "partnershipId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPartnership_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [partnershipId](#API_GetPartnership_RequestSyntax) **   <a name="b2bi-GetPartnership-request-partnershipId"></a>
Specifies the unique, system-generated identifier for a partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Response Syntax
<a name="API_GetPartnership_ResponseSyntax"></a>

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
   "modifiedAt": "string",
   "name": "string",
   "partnershipArn": "string",
   "partnershipId": "string",
   "phone": "string",
   "profileId": "string",
   "tradingPartnerId": "string"
}
```

## Response Elements
<a name="API_GetPartnership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capabilities](#API_GetPartnership_ResponseSyntax) **   <a name="b2bi-GetPartnership-response-capabilities"></a>
Returns one or more capabilities associated with this partnership.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [capabilityOptions](#API_GetPartnership_ResponseSyntax) **   <a name="b2bi-GetPartnership-response-capabilityOptions"></a>
Contains the details for an Outbound EDI capability.
Type: [CapabilityOptions](API_CapabilityOptions.md) object

 ** [createdAt](#API_GetPartnership_ResponseSyntax) **   <a name="b2bi-GetPartnership-response-createdAt"></a>
Returns a timestamp for creation date and time of the partnership.
Type: Timestamp

 ** [email](#API_GetPartnership_ResponseSyntax) **   <a name="b2bi-GetPartnership-response-email"></a>
Returns the email address associated with this trading partner.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 254.
Pattern: `[\w\.\-]+@[\w\.\-]+`

 ** [modifiedAt](#API_GetPartnership_ResponseSyntax) **   <a name="b2bi-GetPartnership-response-modifiedAt"></a>
Returns a timestamp that identifies the most recent date and time that the partnership was modified.
Type: Timestamp

 ** [name](#API_GetPartnership_ResponseSyntax) **   <a name="b2bi-GetPartnership-response-name"></a>
Returns the display name of the partnership
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.

 ** [partnershipArn](#API_GetPartnership_ResponseSyntax) **   <a name="b2bi-GetPartnership-response-partnershipArn"></a>
Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [partnershipId](#API_GetPartnership_ResponseSyntax) **   <a name="b2bi-GetPartnership-response-partnershipId"></a>
Returns the unique, system-generated identifier for a partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [phone](#API_GetPartnership_ResponseSyntax) **   <a name="b2bi-GetPartnership-response-phone"></a>
Returns the phone number associated with the partnership.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 22.
Pattern: `\+?([0-9 \t\-()\/]{7,})(?:\s*(?:#|x\.?|ext\.?|extension) \t*(\d+))?`

 ** [profileId](#API_GetPartnership_ResponseSyntax) **   <a name="b2bi-GetPartnership-response-profileId"></a>
Returns the unique, system-generated identifier for the profile connected to this partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [tradingPartnerId](#API_GetPartnership_ResponseSyntax) **   <a name="b2bi-GetPartnership-response-tradingPartnerId"></a>
Returns the unique identifier for the partner for this partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_GetPartnership_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
This exception is thrown when an error occurs in the AWS B2B Data Interchange service.
 ** retryAfterSeconds **
The server attempts to retry a failed command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.
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
<a name="API_GetPartnership_Examples"></a>

### Example
<a name="API_GetPartnership_Example_1"></a>

The following example retrieves details for the specified partnership.

#### Sample Request
<a name="API_GetPartnership_Example_1_Request"></a>

```
{
    "partnershipId": "ps-5555zzzz4444yyyyy"
}
```

#### Sample Response
<a name="API_GetPartnership_Example_1_Response"></a>

```
{
    "capabilities": [
        "ca-1111aaaa2222bbbb3"
    ],
    "createdAt": "2023-11-01T21:51:05.504Z",
    "email": "john@example.com",
    "modifiedAt": "2023-11-01T21:51:05.504Z",
    "name": "b2bipartner",
    "partnershipArn": "arn:aws:b2bi:us-west-2:123456789012:partnership/ps-5555zzzz4444yyyyy",
    "partnershipId": "ps-5555zzzz4444yyyyy",
    "phone": "5555555555",
    "profileId": "p-ABCDE111122223333",
    "tradingPartnerId": "tp-11112222333344445"
}
```

## See Also
<a name="API_GetPartnership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/GetPartnership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/GetPartnership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/GetPartnership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/GetPartnership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/GetPartnership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/GetPartnership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/GetPartnership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/GetPartnership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/GetPartnership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/GetPartnership)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
