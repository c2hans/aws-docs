---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetSecurityConfigurations.html
---

# GetSecurityConfigurations
<a name="API_GetSecurityConfigurations"></a>

Retrieves a list of all security configurations.

## Request Syntax
<a name="API_GetSecurityConfigurations_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSecurityConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetSecurityConfigurations_RequestSyntax) **   <a name="Glue-GetSecurityConfigurations-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetSecurityConfigurations_RequestSyntax) **   <a name="Glue-GetSecurityConfigurations-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

## Response Syntax
<a name="API_GetSecurityConfigurations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SecurityConfigurations": [
      {
         "CreatedTimeStamp": number,
         "EncryptionConfiguration": {
            "CloudWatchEncryption": {
               "CloudWatchEncryptionMode": "string",
               "KmsKeyArn": "string"
            },
            "DataQualityEncryption": {
               "DataQualityEncryptionMode": "string",
               "KmsKeyArn": "string"
            },
            "JobBookmarksEncryption": {
               "JobBookmarksEncryptionMode": "string",
               "KmsKeyArn": "string"
            },
            "S3Encryption": [
               {
                  "KmsKeyArn": "string",
                  "S3EncryptionMode": "string"
               }
            ]
         },
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetSecurityConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetSecurityConfigurations_ResponseSyntax) **   <a name="Glue-GetSecurityConfigurations-response-NextToken"></a>
A continuation token, if there are more security configurations to return.
Type: String

 ** [SecurityConfigurations](#API_GetSecurityConfigurations_ResponseSyntax) **   <a name="Glue-GetSecurityConfigurations-response-SecurityConfigurations"></a>
A list of security configurations.
Type: Array of [SecurityConfiguration](API_SecurityConfiguration.md) objects

## Errors
<a name="API_GetSecurityConfigurations_Errors"></a>

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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetSecurityConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetSecurityConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetSecurityConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetSecurityConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetSecurityConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetSecurityConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetSecurityConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetSecurityConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetSecurityConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetSecurityConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetSecurityConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
