---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateUsageProfile.html
---

# CreateUsageProfile
<a name="API_CreateUsageProfile"></a>

Creates an AWS Glue usage profile.

## Request Syntax
<a name="API_CreateUsageProfile_RequestSyntax"></a>

```
{
   "Configuration": {
      "JobConfiguration": {
         "{{string}}" : {
            "AllowedValues": [ "{{string}}" ],
            "DefaultValue": "{{string}}",
            "MaxValue": "{{string}}",
            "MinValue": "{{string}}"
         }
      },
      "SessionConfiguration": {
         "{{string}}" : {
            "AllowedValues": [ "{{string}}" ],
            "DefaultValue": "{{string}}",
            "MaxValue": "{{string}}",
            "MinValue": "{{string}}"
         }
      }
   },
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateUsageProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Configuration](#API_CreateUsageProfile_RequestSyntax) **   <a name="Glue-CreateUsageProfile-request-Configuration"></a>
A `ProfileConfiguration` object specifying the job and session values for the profile.
Type: [ProfileConfiguration](API_ProfileConfiguration.md) object
Required: Yes

 ** [Description](#API_CreateUsageProfile_RequestSyntax) **   <a name="Glue-CreateUsageProfile-request-Description"></a>
A description of the usage profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [Name](#API_CreateUsageProfile_RequestSyntax) **   <a name="Glue-CreateUsageProfile-request-Name"></a>
The name of the usage profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Tags](#API_CreateUsageProfile_RequestSyntax) **   <a name="Glue-CreateUsageProfile-request-Tags"></a>
A list of tags applied to the usage profile.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateUsageProfile_ResponseSyntax"></a>

```
{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateUsageProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateUsageProfile_ResponseSyntax) **   <a name="Glue-CreateUsageProfile-response-Name"></a>
The name of the usage profile that was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_CreateUsageProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationNotSupportedException **
The operation is not available in the region.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateUsageProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateUsageProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateUsageProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateUsageProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateUsageProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateUsageProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateUsageProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateUsageProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateUsageProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateUsageProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateUsageProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
