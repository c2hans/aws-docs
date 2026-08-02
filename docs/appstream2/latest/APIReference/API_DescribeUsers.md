---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeUsers.html
---

# DescribeUsers
<a name="API_DescribeUsers"></a>

Retrieves a list that describes one or more specified users in the user pool.

## Request Syntax
<a name="API_DescribeUsers_RequestSyntax"></a>

```
{
   "AuthenticationType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeUsers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuthenticationType](#API_DescribeUsers_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeUsers-request-AuthenticationType"></a>
The authentication type for the users in the user pool to describe. You must specify USERPOOL.
Type: String
Valid Values: `API | SAML | USERPOOL | AWS_AD`
Required: Yes

 ** [MaxResults](#API_DescribeUsers_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeUsers-request-MaxResults"></a>
The maximum size of each page of results.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeUsers_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeUsers-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeUsers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Users": [
      {
         "Arn": "string",
         "AuthenticationType": "string",
         "CreatedTime": number,
         "Enabled": boolean,
         "FirstName": "string",
         "LastName": "string",
         "Status": "string",
         "UserName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeUsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeUsers_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeUsers-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Minimum length of 1.

 ** [Users](#API_DescribeUsers_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeUsers-response-Users"></a>
Information about users in the user pool.
Type: Array of [User](API_User.md) objects

## Errors
<a name="API_DescribeUsers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeUsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeUsers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeUsers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeUsers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeUsers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeUsers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeUsers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeUsers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeUsers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeUsers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeUsers)
