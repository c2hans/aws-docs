---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListWorkforces.html
---

# ListWorkforces
<a name="API_ListWorkforces"></a>

Use this operation to list all private and vendor workforces in an AWS Region. Note that you can only have one private workforce per AWS Region.

## Request Syntax
<a name="API_ListWorkforces_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListWorkforces_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListWorkforces_RequestSyntax) **   <a name="sagemaker-ListWorkforces-request-MaxResults"></a>
The maximum number of workforces returned in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListWorkforces_RequestSyntax) **   <a name="sagemaker-ListWorkforces-request-NameContains"></a>
A filter you can use to search for workforces using part of the workforce name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-]){0,62}`
Required: No

 ** [NextToken](#API_ListWorkforces_RequestSyntax) **   <a name="sagemaker-ListWorkforces-request-NextToken"></a>
A token to resume pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListWorkforces_RequestSyntax) **   <a name="sagemaker-ListWorkforces-request-SortBy"></a>
Sort workforces using the workforce name or creation date.
Type: String
Valid Values: `Name | CreateDate`
Required: No

 ** [SortOrder](#API_ListWorkforces_RequestSyntax) **   <a name="sagemaker-ListWorkforces-request-SortOrder"></a>
Sort workforces in ascending or descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListWorkforces_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Workforces": [
      {
         "CognitoConfig": {
            "ClientId": "string",
            "UserPool": "string"
         },
         "FailureReason": "string",
         "IpAddressType": "string",
         "OidcConfig": {
            "AuthenticationRequestExtraParams": {
               "string" : "string"
            },
            "AuthorizationEndpoint": "string",
            "ClientId": "string",
            "Issuer": "string",
            "JwksUri": "string",
            "LogoutEndpoint": "string",
            "Scope": "string",
            "TokenEndpoint": "string",
            "UserInfoEndpoint": "string"
         },
         "SourceIpConfig": {
            "Cidrs": [ "string" ]
         },
         "Status": "string",
         "SubDomain": "string",
         "WorkforceArn": "string",
         "WorkforceName": "string",
         "WorkforceVpcConfig": {
            "SecurityGroupIds": [ "string" ],
            "Subnets": [ "string" ],
            "VpcEndpointId": "string",
            "VpcId": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkforces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListWorkforces_ResponseSyntax) **   <a name="sagemaker-ListWorkforces-response-NextToken"></a>
A token to resume pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [Workforces](#API_ListWorkforces_ResponseSyntax) **   <a name="sagemaker-ListWorkforces-response-Workforces"></a>
A list containing information about your workforce.
Type: Array of [Workforce](API_Workforce.md) objects

## Errors
<a name="API_ListWorkforces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListWorkforces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListWorkforces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListWorkforces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListWorkforces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListWorkforces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListWorkforces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListWorkforces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListWorkforces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListWorkforces)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListWorkforces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListWorkforces)
