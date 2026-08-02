---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeDirectoryConfigs.html
---

# DescribeDirectoryConfigs
<a name="API_DescribeDirectoryConfigs"></a>

Retrieves a list that describes one or more specified Directory Config objects for WorkSpaces Applications, if the names for these objects are provided. Otherwise, all Directory Config objects in the account are described. These objects include the configuration information required to join fleets and image builders to Microsoft Active Directory domains.

Although the response syntax in this topic includes the account password, this password is not returned in the actual response.

## Request Syntax
<a name="API_DescribeDirectoryConfigs_RequestSyntax"></a>

```
{
   "DirectoryNames": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDirectoryConfigs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DirectoryNames](#API_DescribeDirectoryConfigs_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeDirectoryConfigs-request-DirectoryNames"></a>
The directory names.
Type: Array of strings
Required: No

 ** [MaxResults](#API_DescribeDirectoryConfigs_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeDirectoryConfigs-request-MaxResults"></a>
The maximum size of each page of results.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeDirectoryConfigs_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeDirectoryConfigs-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeDirectoryConfigs_ResponseSyntax"></a>

```
{
   "DirectoryConfigs": [
      {
         "CertificateBasedAuthProperties": {
            "CertificateAuthorityArn": "string",
            "Status": "string"
         },
         "CreatedTime": number,
         "DirectoryName": "string",
         "OrganizationalUnitDistinguishedNames": [ "string" ],
         "ServiceAccountCredentials": {
            "AccountName": "string",
            "AccountPassword": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDirectoryConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryConfigs](#API_DescribeDirectoryConfigs_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeDirectoryConfigs-response-DirectoryConfigs"></a>
Information about the directory configurations. Note that although the response syntax in this topic includes the account password, this password is not returned in the actual response.
Type: Array of [DirectoryConfig](API_DirectoryConfig.md) objects

 ** [NextToken](#API_DescribeDirectoryConfigs_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeDirectoryConfigs-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeDirectoryConfigs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDirectoryConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeDirectoryConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeDirectoryConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeDirectoryConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeDirectoryConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeDirectoryConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeDirectoryConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeDirectoryConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeDirectoryConfigs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeDirectoryConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeDirectoryConfigs)
