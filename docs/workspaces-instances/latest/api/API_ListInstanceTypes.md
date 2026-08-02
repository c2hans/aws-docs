---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ListInstanceTypes.html
---

# ListInstanceTypes
<a name="API_ListInstanceTypes"></a>

Retrieves a list of instance types supported by Amazon WorkSpaces Instances, enabling precise workspace infrastructure configuration.

## Request Syntax
<a name="API_ListInstanceTypes_RequestSyntax"></a>

```
{
   "InstanceConfigurationFilter": {
      "BillingMode": "{{string}}",
      "PlatformType": "{{string}}",
      "Tenancy": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInstanceTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceConfigurationFilter](#API_ListInstanceTypes_RequestSyntax) **   <a name="workspacesinstances-ListInstanceTypes-request-InstanceConfigurationFilter"></a>
Optional filter to narrow instance type results based on configuration requirements. Only returns instance types that support the specified combination of tenancy, platform type, and billing mode.
Type: [InstanceConfigurationFilter](API_InstanceConfigurationFilter.md) object
Required: No

 ** [MaxResults](#API_ListInstanceTypes_RequestSyntax) **   <a name="workspacesinstances-ListInstanceTypes-request-MaxResults"></a>
Maximum number of instance types to return in a single API call. Enables pagination of instance type results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 600.
Required: No

 ** [NextToken](#API_ListInstanceTypes_RequestSyntax) **   <a name="workspacesinstances-ListInstanceTypes-request-NextToken"></a>
Pagination token for retrieving subsequent pages of instance type results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListInstanceTypes_ResponseSyntax"></a>

```
{
   "InstanceTypes": [
      {
         "InstanceType": "string",
         "SupportedInstanceConfigurations": [
            {
               "BillingMode": "string",
               "PlatformType": "string",
               "Tenancy": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInstanceTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceTypes](#API_ListInstanceTypes_ResponseSyntax) **   <a name="workspacesinstances-ListInstanceTypes-response-InstanceTypes"></a>
Collection of supported instance types for WorkSpaces Instances.
Type: Array of [InstanceTypeInfo](API_InstanceTypeInfo.md) objects

 ** [NextToken](#API_ListInstanceTypes_ResponseSyntax) **   <a name="workspacesinstances-ListInstanceTypes-response-NextToken"></a>
Token for retrieving additional instance types if the result set is paginated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListInstanceTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Indicates insufficient permissions to perform the requested action.
 ** Message **
Detailed explanation of the access denial.
HTTP Status Code: 400

 ** InternalServerException **
Indicates an unexpected server-side error occurred.
 ** Message **
Description of the internal server error.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
Indicates the request rate has exceeded limits.
 ** Message **
Description of the throttling event.
 ** QuotaCode **
Specific code for the throttling quota.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
 ** ServiceCode **
Code identifying the service experiencing throttling.
HTTP Status Code: 400

 ** ValidationException **
Indicates invalid input parameters in the request.
 ** FieldList **
List of fields that failed validation.
 ** Message **
Overall description of validation failures.
 ** Reason **
Specific reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListInstanceTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-instances-2022-07-26/ListInstanceTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-instances-2022-07-26/ListInstanceTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/ListInstanceTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-instances-2022-07-26/ListInstanceTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/ListInstanceTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-instances-2022-07-26/ListInstanceTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-instances-2022-07-26/ListInstanceTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-instances-2022-07-26/ListInstanceTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-instances-2022-07-26/ListInstanceTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/ListInstanceTypes)
