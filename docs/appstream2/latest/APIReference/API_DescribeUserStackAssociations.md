---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeUserStackAssociations.html
---

# DescribeUserStackAssociations
<a name="API_DescribeUserStackAssociations"></a>

Retrieves a list that describes the UserStackAssociation objects. You must specify either or both of the following:
+ The stack name
+ The user name (email address of the user associated with the stack) and the authentication type for the user

## Request Syntax
<a name="API_DescribeUserStackAssociations_RequestSyntax"></a>

```
{
   "AuthenticationType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StackName": "{{string}}",
   "UserName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeUserStackAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuthenticationType](#API_DescribeUserStackAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeUserStackAssociations-request-AuthenticationType"></a>
The authentication type for the user who is associated with the stack. You must specify USERPOOL.
Type: String
Valid Values: `API | SAML | USERPOOL | AWS_AD`
Required: No

 ** [MaxResults](#API_DescribeUserStackAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeUserStackAssociations-request-MaxResults"></a>
The maximum size of each page of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 500.
Required: No

 ** [NextToken](#API_DescribeUserStackAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeUserStackAssociations-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [StackName](#API_DescribeUserStackAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeUserStackAssociations-request-StackName"></a>
The name of the stack that is associated with the user.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [UserName](#API_DescribeUserStackAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeUserStackAssociations-request-UserName"></a>
The email address of the user who is associated with the stack.
Users' email addresses are case-sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

## Response Syntax
<a name="API_DescribeUserStackAssociations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "UserStackAssociations": [
      {
         "AuthenticationType": "string",
         "SendEmailNotification": boolean,
         "StackName": "string",
         "UserName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeUserStackAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeUserStackAssociations_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeUserStackAssociations-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Minimum length of 1.

 ** [UserStackAssociations](#API_DescribeUserStackAssociations_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeUserStackAssociations-response-UserStackAssociations"></a>
The UserStackAssociation objects.
Type: Array of [UserStackAssociation](API_UserStackAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.

## Errors
<a name="API_DescribeUserStackAssociations_Errors"></a>

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

## See Also
<a name="API_DescribeUserStackAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeUserStackAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeUserStackAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeUserStackAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeUserStackAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeUserStackAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeUserStackAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeUserStackAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeUserStackAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeUserStackAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeUserStackAssociations)
