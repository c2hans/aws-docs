---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetUsageProfile.html
---

# GetUsageProfile
<a name="API_GetUsageProfile"></a>

Retrieves information about the specified AWS Glue usage profile.

## Request Syntax
<a name="API_GetUsageProfile_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetUsageProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_GetUsageProfile_RequestSyntax) **   <a name="Glue-GetUsageProfile-request-Name"></a>
The name of the usage profile to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetUsageProfile_ResponseSyntax"></a>

```
{
   "Configuration": {
      "JobConfiguration": {
         "string" : {
            "AllowedValues": [ "string" ],
            "DefaultValue": "string",
            "MaxValue": "string",
            "MinValue": "string"
         }
      },
      "SessionConfiguration": {
         "string" : {
            "AllowedValues": [ "string" ],
            "DefaultValue": "string",
            "MaxValue": "string",
            "MinValue": "string"
         }
      }
   },
   "CreatedOn": number,
   "Description": "string",
   "LastModifiedOn": number,
   "Name": "string"
}
```

## Response Elements
<a name="API_GetUsageProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Configuration](#API_GetUsageProfile_ResponseSyntax) **   <a name="Glue-GetUsageProfile-response-Configuration"></a>
A `ProfileConfiguration` object specifying the job and session values for the profile.
Type: [ProfileConfiguration](API_ProfileConfiguration.md) object

 ** [CreatedOn](#API_GetUsageProfile_ResponseSyntax) **   <a name="Glue-GetUsageProfile-response-CreatedOn"></a>
The date and time when the usage profile was created.
Type: Timestamp

 ** [Description](#API_GetUsageProfile_ResponseSyntax) **   <a name="Glue-GetUsageProfile-response-Description"></a>
A description of the usage profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 ** [LastModifiedOn](#API_GetUsageProfile_ResponseSyntax) **   <a name="Glue-GetUsageProfile-response-LastModifiedOn"></a>
The date and time when the usage profile was last modified.
Type: Timestamp

 ** [Name](#API_GetUsageProfile_ResponseSyntax) **   <a name="Glue-GetUsageProfile-response-Name"></a>
The name of the usage profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_GetUsageProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetUsageProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetUsageProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetUsageProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetUsageProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetUsageProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetUsageProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetUsageProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetUsageProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetUsageProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetUsageProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetUsageProfile)
