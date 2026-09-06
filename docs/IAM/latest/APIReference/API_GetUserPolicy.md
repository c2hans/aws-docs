---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUserPolicy.html
---

# GetUserPolicy
<a name="API_GetUserPolicy"></a>

Retrieves the specified inline policy document that is embedded in the specified IAM user.

**Note**
Policies returned by this operation are URL-encoded compliant with [RFC 3986](https://tools.ietf.org/html/rfc3986). You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the `decode` method of the `java.net.URLDecoder` utility class in the Java SDK. Other languages and SDKs provide similar functionality, and some SDKs do this decoding automatically.

An IAM user can also have managed policies attached to it. To retrieve a managed policy document that is attached to a user, use [GetPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicy.html) to determine the policy's default version. Then use [GetPolicyVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicyVersion.html) to retrieve the policy document.

For more information about policies, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.

## Request Parameters
<a name="API_GetUserPolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** PolicyName **
The name of the policy document to get.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** UserName **
The name of the user who the policy is associated with.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Response Elements
<a name="API_GetUserPolicy_ResponseElements"></a>

The following elements are returned by the service.

 ** PolicyDocument **
The policy document.
IAM stores policies in JSON format. However, resources that were created using CloudFormation templates can be formatted in YAML. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`

 ** PolicyName **
The name of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`

 ** UserName **
The user the policy is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`

## Errors
<a name="API_GetUserPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetUserPolicy_Examples"></a>

### Example
<a name="API_GetUserPolicy_Example_1"></a>

This example illustrates one usage of GetUserPolicy.

#### Sample Request
<a name="API_GetUserPolicy_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetUserPolicy
&UserName=Bob
&PolicyName=AllAccessPolicy
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetUserPolicy_Example_1_Response"></a>

```
<GetUserPolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
 <GetUserPolicyResult>
    <UserName>Bob</UserName>
    <PolicyName>AllAccessPolicy</PolicyName>
    <PolicyDocument>
    {"Version":"2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Action":"*","Resource":"*"}]}
    </PolicyDocument>
 </GetUserPolicyResult>
 <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
 </ResponseMetadata>
</GetUserPolicyResponse>
```

## See Also
<a name="API_GetUserPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetUserPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetUserPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetUserPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetUserPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetUserPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetUserPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetUserPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetUserPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetUserPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetUserPolicy)
