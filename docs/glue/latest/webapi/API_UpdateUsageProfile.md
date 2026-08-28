---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateUsageProfile.html
---

# UpdateUsageProfile
<a name="API_UpdateUsageProfile"></a>

Update an AWS Glue usage profile.

## Request Syntax
<a name="API_UpdateUsageProfile_RequestSyntax"></a>

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
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateUsageProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Configuration](#API_UpdateUsageProfile_RequestSyntax) **   <a name="Glue-UpdateUsageProfile-request-Configuration"></a>
A `ProfileConfiguration` object specifying the job and session values for the profile.
Type: [ProfileConfiguration](API_ProfileConfiguration.md) object
Required: Yes

 ** [Description](#API_UpdateUsageProfile_RequestSyntax) **   <a name="Glue-UpdateUsageProfile-request-Description"></a>
A description of the usage profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [Name](#API_UpdateUsageProfile_RequestSyntax) **   <a name="Glue-UpdateUsageProfile-request-Name"></a>
The name of the usage profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_UpdateUsageProfile_ResponseSyntax"></a>

```
{
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateUsageProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_UpdateUsageProfile_ResponseSyntax) **   <a name="Glue-UpdateUsageProfile-response-Name"></a>
The name of the usage profile that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_UpdateUsageProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
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

## See Also
<a name="API_UpdateUsageProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateUsageProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateUsageProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateUsageProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateUsageProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateUsageProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateUsageProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateUsageProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateUsageProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateUsageProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateUsageProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
