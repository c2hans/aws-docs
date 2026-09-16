---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListDistributedGrants.html
---

# ListDistributedGrants
<a name="API_ListDistributedGrants"></a>

Lists the grants distributed for the specified license.

## Request Syntax
<a name="API_ListDistributedGrants_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "GrantArns": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDistributedGrants_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListDistributedGrants_RequestSyntax) **   <a name="licensemanager-ListDistributedGrants-request-Filters"></a>
Filters to scope the results. The following filters are supported:
+  `LicenseArn`
+  `GrantStatus`
+  `GranteePrincipalARN`
+  `ProductSKU`
+  `LicenseIssuerName`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [GrantArns](#API_ListDistributedGrants_RequestSyntax) **   <a name="licensemanager-ListDistributedGrants-request-GrantArns"></a>
Amazon Resource Names (ARNs) of the grants.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** [MaxResults](#API_ListDistributedGrants_RequestSyntax) **   <a name="licensemanager-ListDistributedGrants-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListDistributedGrants_RequestSyntax) **   <a name="licensemanager-ListDistributedGrants-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListDistributedGrants_ResponseSyntax"></a>

```
{
   "Grants": [
      {
         "GrantArn": "string",
         "GrantedOperations": [ "string" ],
         "GranteePrincipalArn": "string",
         "GrantName": "string",
         "GrantStatus": "string",
         "HomeRegion": "string",
         "LicenseArn": "string",
         "Options": {
            "ActivationOverrideBehavior": "string"
         },
         "ParentArn": "string",
         "StatusReason": "string",
         "Version": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDistributedGrants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Grants](#API_ListDistributedGrants_ResponseSyntax) **   <a name="licensemanager-ListDistributedGrants-response-Grants"></a>
Distributed grant details.
Type: Array of [Grant](API_Grant.md) objects

 ** [NextToken](#API_ListDistributedGrants_ResponseSyntax) **   <a name="licensemanager-ListDistributedGrants-response-NextToken"></a>
Token for the next set of results.
Type: String

## Errors
<a name="API_ListDistributedGrants_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameter values are not valid.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ListDistributedGrants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListDistributedGrants)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListDistributedGrants)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListDistributedGrants)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListDistributedGrants)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListDistributedGrants)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListDistributedGrants)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListDistributedGrants)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListDistributedGrants)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListDistributedGrants)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListDistributedGrants)
