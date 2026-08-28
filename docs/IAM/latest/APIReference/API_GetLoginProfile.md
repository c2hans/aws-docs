---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetLoginProfile.html
---

# GetLoginProfile
<a name="API_GetLoginProfile"></a>

Retrieves the user name for the specified IAM user. A login profile is created when you create a password for the user to access the AWS Management Console. If the user does not exist or does not have a password, the operation returns a 404 (`NoSuchEntity`) error.

If you create an IAM user with access to the console, the `CreateDate` reflects the date you created the initial password for the user.

If you create an IAM user with programmatic access, and then later add a password for the user to access the AWS Management Console, the `CreateDate` reflects the initial password creation date. A user with programmatic access does not have a login profile unless you create a password for the user to access the AWS Management Console.

## Request Parameters
<a name="API_GetLoginProfile_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** UserName **
The name of the user whose login profile you want to retrieve.
This parameter is optional. If no user name is included, it defaults to the principal making the request. When you make this request with root user credentials, you must use an [AssumeRoot](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html) session to omit the user name.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: No

## Response Elements
<a name="API_GetLoginProfile_ResponseElements"></a>

The following element is returned by the service.

 ** LoginProfile **
A structure containing the user name and the profile creation date for the user.
Type: [LoginProfile](API_LoginProfile.md) object

## Errors
<a name="API_GetLoginProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetLoginProfile_Examples"></a>

### Example
<a name="API_GetLoginProfile_Example_1"></a>

This example illustrates one usage of GetLoginProfile.

#### Sample Request
<a name="API_GetLoginProfile_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetLoginProfile
&UserName=Bob
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetLoginProfile_Example_1_Response"></a>

```
<GetLoginProfileResponse>
 <GetLoginProfileResult>
    <LoginProfile>
       <UserName>Bob</UserName>
       <CreateDate>2011-09-19T23:00:56Z</CreateDate>
    </LoginProfile>
 </GetLoginProfileResult>
 <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
 </ResponseMetadata>
</GetLoginProfileResponse>
```

## See Also
<a name="API_GetLoginProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetLoginProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetLoginProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetLoginProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetLoginProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetLoginProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetLoginProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetLoginProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetLoginProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetLoginProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetLoginProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
