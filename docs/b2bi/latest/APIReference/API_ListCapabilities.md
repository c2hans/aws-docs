---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListCapabilities.html
---

# ListCapabilities
<a name="API_ListCapabilities"></a>

Lists the capabilities associated with your AWS account for your current or specified region. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.

## Request Syntax
<a name="API_ListCapabilities_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCapabilities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListCapabilities_RequestSyntax) **   <a name="b2bi-ListCapabilities-request-maxResults"></a>
Specifies the maximum number of capabilities to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListCapabilities_RequestSyntax) **   <a name="b2bi-ListCapabilities-request-nextToken"></a>
When additional results are obtained from the command, a `NextToken` parameter is returned in the output. You can then pass the `NextToken` parameter in a subsequent command to continue listing additional resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListCapabilities_ResponseSyntax"></a>

```
{
   "capabilities": [
      {
         "capabilityId": "string",
         "createdAt": "string",
         "modifiedAt": "string",
         "name": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCapabilities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capabilities](#API_ListCapabilities_ResponseSyntax) **   <a name="b2bi-ListCapabilities-response-capabilities"></a>
Returns one or more capabilities associated with this partnership.
Type: Array of [CapabilitySummary](API_CapabilitySummary.md) objects

 ** [nextToken](#API_ListCapabilities_ResponseSyntax) **   <a name="b2bi-ListCapabilities-response-nextToken"></a>
When additional results are obtained from the command, a `NextToken` parameter is returned in the output. You can then pass the `NextToken` parameter in a subsequent command to continue listing additional resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListCapabilities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
This exception is thrown when an error occurs in the AWS B2B Data Interchange service.
 ** retryAfterSeconds **
The server attempts to retry a failed command.
HTTP Status Code: 500

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
<a name="API_ListCapabilities_Examples"></a>

### Example
<a name="API_ListCapabilities_Example_1"></a>

The following example lists the capabilities for your account and in your region. Note that in this example, there is only one capability listed: however, this call would return up to 50 capabilities.

#### Sample Request
<a name="API_ListCapabilities_Example_1_Request"></a>

```
{
    "maxResults": 50,
    "nextToken": "foo"
}
```

#### Sample Response
<a name="API_ListCapabilities_Example_1_Response"></a>

```
{
    "capabilities": [
        {
            "capabilityId": "ca-1111aaaa2222bbbb3",
            "createdAt": "2023-11-01T21:51:05.504Z",
            "modifiedAt": "2023-11-01T21:51:05.504Z",
            "name": "b2biexample",
            "type": "edi"
        }
    ],
    "nextToken": "foo"
}
```

## See Also
<a name="API_ListCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/ListCapabilities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/ListCapabilities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/ListCapabilities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/ListCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/ListCapabilities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/ListCapabilities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/ListCapabilities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/ListCapabilities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/ListCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/ListCapabilities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
