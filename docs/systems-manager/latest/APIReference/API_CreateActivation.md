---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateActivation.html
---

# CreateActivation
<a name="API_CreateActivation"></a>

Generates an activation code and activation ID you can use to register your on-premises servers, edge devices, or virtual machine (VM) with AWS Systems Manager. Registering these machines with Systems Manager makes it possible to manage them using Systems Manager tools. You use the activation code and ID when installing SSM Agent on machines in your hybrid environment. For more information about requirements for managing on-premises machines using Systems Manager, see [Using AWS Systems Manager in hybrid and multicloud environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-hybrid-multicloud.html) in the * AWS Systems Manager User Guide*.

**Note**
Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, and on-premises servers and VMs that are configured for Systems Manager are all called *managed nodes*.

## Request Syntax
<a name="API_CreateActivation_RequestSyntax"></a>

```
{
   "DefaultInstanceName": "{{string}}",
   "Description": "{{string}}",
   "ExpirationDate": {{number}},
   "IamRole": "{{string}}",
   "RegistrationLimit": {{number}},
   "RegistrationMetadata": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateActivation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DefaultInstanceName](#API_CreateActivation_RequestSyntax) **   <a name="systemsmanager-CreateActivation-request-DefaultInstanceName"></a>
The name of the registered, managed node as it will appear in the AWS Systems Manager console or when you use the AWS command line tools to list Systems Manager resources.
Don't enter personally identifiable information in this field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [Description](#API_CreateActivation_RequestSyntax) **   <a name="systemsmanager-CreateActivation-request-Description"></a>
A user-defined description of the resource that you want to register with Systems Manager.
Don't enter personally identifiable information in this field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [ExpirationDate](#API_CreateActivation_RequestSyntax) **   <a name="systemsmanager-CreateActivation-request-ExpirationDate"></a>
The date by which this activation request should expire, in timestamp format, such as "2024-07-07T00:00:00". You can specify a date up to 30 days in advance. If you don't provide an expiration date, the activation code expires in 24 hours.
Type: Timestamp
Required: No

 ** [IamRole](#API_CreateActivation_RequestSyntax) **   <a name="systemsmanager-CreateActivation-request-IamRole"></a>
The name of the AWS Identity and Access Management (IAM) role that you want to assign to the managed node. This IAM role must provide AssumeRole permissions for the AWS Systems Manager service principal `ssm.amazonaws.com`. For more information, see [Create the IAM service role required for Systems Manager in a hybrid and multicloud environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-service-role.html) in the * AWS Systems Manager User Guide*.
You can't specify an IAM service-linked role for this parameter. You must create a unique role.
Type: String
Length Constraints: Maximum length of 64.
Required: Yes

 ** [RegistrationLimit](#API_CreateActivation_RequestSyntax) **   <a name="systemsmanager-CreateActivation-request-RegistrationLimit"></a>
Specify the maximum number of managed nodes you want to register. The default value is `1`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [RegistrationMetadata](#API_CreateActivation_RequestSyntax) **   <a name="systemsmanager-CreateActivation-request-RegistrationMetadata"></a>
Reserved for internal use.
Type: Array of [RegistrationMetadataItem](API_RegistrationMetadataItem.md) objects
Required: No

 ** [Tags](#API_CreateActivation_RequestSyntax) **   <a name="systemsmanager-CreateActivation-request-Tags"></a>
Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an activation to identify which servers or virtual machines (VMs) in your on-premises environment you intend to activate. In this case, you could specify the following key-value pairs:
+  `Key=OS,Value=Windows`
+  `Key=Environment,Value=Production`
When you install SSM Agent on your on-premises servers and VMs, you specify an activation ID and code. When you specify the activation ID and code, tags assigned to the activation are automatically applied to the on-premises servers or VMs.
You can't add tags to or delete tags from an existing activation. You can tag your on-premises servers, edge devices, and VMs after they connect to Systems Manager for the first time and are assigned a managed node ID. This means they are listed in the AWS Systems Manager console with an ID that is prefixed with "mi-". For information about how to add tags to your managed nodes, see [AddTagsToResource](API_AddTagsToResource.md). For information about how to remove tags from your managed nodes, see [RemoveTagsFromResource](API_RemoveTagsFromResource.md).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

## Response Syntax
<a name="API_CreateActivation_ResponseSyntax"></a>

```
{
   "ActivationCode": "string",
   "ActivationId": "string"
}
```

## Response Elements
<a name="API_CreateActivation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActivationCode](#API_CreateActivation_ResponseSyntax) **   <a name="systemsmanager-CreateActivation-response-ActivationCode"></a>
The code the system generates when it processes the activation. The activation code functions like a password to validate the activation ID.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 250.

 ** [ActivationId](#API_CreateActivation_ResponseSyntax) **   <a name="systemsmanager-CreateActivation-response-ActivationId"></a>
The ID number generated by the system when it processed the activation. The activation ID functions like a user name.
Type: String
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Errors
<a name="API_CreateActivation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidParameters **
You must specify values for all required parameters in the AWS Systems Manager document (SSM document). You can only supply values to parameters defined in the SSM document.
HTTP Status Code: 400

## Examples
<a name="API_CreateActivation_Examples"></a>

### Example
<a name="API_CreateActivation_Example_1"></a>

This example illustrates one usage of CreateActivation.

#### Sample Request
<a name="API_CreateActivation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.CreateActivation
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T135329Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 70

{
    "IamRole": "service-role/role_name"
}
```

#### Sample Response
<a name="API_CreateActivation_Example_1_Response"></a>

```
{
    "ActivationCode": "Fjz3/sZfSvv78EXAMPLE",
    "ActivationId": "e488f2f6-e686-4afb-8a04-ef6dfEXAMPLE"
}
```

## See Also
<a name="API_CreateActivation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/CreateActivation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/CreateActivation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CreateActivation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/CreateActivation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CreateActivation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/CreateActivation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/CreateActivation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/CreateActivation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/CreateActivation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CreateActivation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
