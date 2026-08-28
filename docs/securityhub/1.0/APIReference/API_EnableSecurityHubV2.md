---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_EnableSecurityHubV2.html
---

# EnableSecurityHubV2
<a name="API_EnableSecurityHubV2"></a>

Enables the service in account for the current AWS Region or specified AWS Region.

## Request Syntax
<a name="API_EnableSecurityHubV2_RequestSyntax"></a>

```
POST /hubv2 HTTP/1.1
Content-type: application/json

{
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_EnableSecurityHubV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_EnableSecurityHubV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_EnableSecurityHubV2_RequestSyntax) **   <a name="securityhub-EnableSecurityHubV2-request-Tags"></a>
The tags to add to the hub V2 resource when you enable Security Hub.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_EnableSecurityHubV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "HubV2Arn": "string"
}
```

## Response Elements
<a name="API_EnableSecurityHubV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HubV2Arn](#API_EnableSecurityHubV2_ResponseSyntax) **   <a name="securityhub-EnableSecurityHubV2-response-HubV2Arn"></a>
The ARN of the V2 resource that was created.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_EnableSecurityHubV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_EnableSecurityHubV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/EnableSecurityHubV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/EnableSecurityHubV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/EnableSecurityHubV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/EnableSecurityHubV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/EnableSecurityHubV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/EnableSecurityHubV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/EnableSecurityHubV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/EnableSecurityHubV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/EnableSecurityHubV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/EnableSecurityHubV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
