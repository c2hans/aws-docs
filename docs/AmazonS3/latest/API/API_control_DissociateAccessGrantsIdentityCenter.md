---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DissociateAccessGrantsIdentityCenter.html
---

# DissociateAccessGrantsIdentityCenter
<a name="API_control_DissociateAccessGrantsIdentityCenter"></a>

Dissociates the AWS IAM Identity Center instance from the S3 Access Grants instance.

Permissions
You must have the `s3:DissociateAccessGrantsIdentityCenter` permission to use this operation.

Additional Permissions
You must have the `sso:DeleteApplication` permission to use this operation.

## Request Syntax
<a name="API_control_DissociateAccessGrantsIdentityCenter_RequestSyntax"></a>

```
DELETE /v20180820/accessgrantsinstance/identitycenter HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_DissociateAccessGrantsIdentityCenter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [x-amz-account-id](#API_control_DissociateAccessGrantsIdentityCenter_RequestSyntax) **   <a name="AmazonS3-control_DissociateAccessGrantsIdentityCenter-request-header-AccountId"></a>
The AWS account ID of the S3 Access Grants instance.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_DissociateAccessGrantsIdentityCenter_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_DissociateAccessGrantsIdentityCenter_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_DissociateAccessGrantsIdentityCenter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## See Also
<a name="API_control_DissociateAccessGrantsIdentityCenter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DissociateAccessGrantsIdentityCenter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/DissociateAccessGrantsIdentityCenter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DissociateAccessGrantsIdentityCenter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DissociateAccessGrantsIdentityCenter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DissociateAccessGrantsIdentityCenter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DissociateAccessGrantsIdentityCenter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DissociateAccessGrantsIdentityCenter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DissociateAccessGrantsIdentityCenter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DissociateAccessGrantsIdentityCenter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DissociateAccessGrantsIdentityCenter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
