---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutParameter.html
---

# PutParameter
<a name="API_PutParameter"></a>

Create or update a parameter in Parameter Store.

**Note**
Parameter Store throughput defines the number of API transactions per second (TPS) that Systems Manager can process. This applies to `GetParameter`, `GetParameters`, and `PutParameter` API calls for your AWS account and AWS Region. By default, Parameter Store is configured with a standard throughput quota suitable for low- to moderate-volume workloads. Applications that retrieve configuration data infrequently or operate at smaller scale can use this default setting without additional cost.
For higher-volume workloads, you can enable higher throughput. This increases the maximum number of supported transactions per second for your account and Region. Increased throughput supports applications and workloads that need concurrent access to multiple parameters. If you experience `ThrottlingException: Rate exceeded` errors, enable higher throughput. For more information, see [Changing Parameter Store throughput](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html).

## Request Syntax
<a name="API_PutParameter_RequestSyntax"></a>

```
{
   "AllowedPattern": "{{string}}",
   "DataType": "{{string}}",
   "Description": "{{string}}",
   "KeyId": "{{string}}",
   "Name": "{{string}}",
   "Overwrite": {{boolean}},
   "Policies": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Tier": "{{string}}",
   "Type": "{{string}}",
   "Value": "{{string}}"
}
```

## Request Parameters
<a name="API_PutParameter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllowedPattern](#API_PutParameter_RequestSyntax) **   <a name="systemsmanager-PutParameter-request-AllowedPattern"></a>
A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: AllowedPattern=^\\d\+$
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [DataType](#API_PutParameter_RequestSyntax) **   <a name="systemsmanager-PutParameter-request-DataType"></a>
The data type for a `String` parameter. Supported data types include plain text and Amazon Machine Image (AMI) IDs.
 **The following data type values are supported.**
+  `text`
+  `aws:ec2:image`
+  `aws:ssm:integration`
When you create a `String` parameter and specify `aws:ec2:image`, AWS Systems Manager validates the parameter value is in the required format, such as `ami-12345abcdeEXAMPLE`, and that the specified AMI is available in your AWS account.
If the action is successful, the service sends back an HTTP 200 response which indicates a successful `PutParameter` call for all cases except for data type `aws:ec2:image`. If you call `PutParameter` with `aws:ec2:image` data type, a successful HTTP 200 response does not guarantee that your parameter was successfully created or updated. The `aws:ec2:image` value is validated asynchronously, and the `PutParameter` call returns before the validation is complete. If you submit an invalid AMI value, the PutParameter operation will return success, but the asynchronous validation will fail and the parameter will not be created or updated. To monitor whether your `aws:ec2:image` parameters are created successfully, see [Setting up notifications or trigger actions based on Parameter Store events](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-cwe.html). For more information about AMI format validation , see [Native parameter support for Amazon Machine Image IDs](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-ec2-aliases.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [Description](#API_PutParameter_RequestSyntax) **   <a name="systemsmanager-PutParameter-request-Description"></a>
Information about the parameter that you want to add to the system. Optional but recommended.
Don't enter personally identifiable information in this field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [KeyId](#API_PutParameter_RequestSyntax) **   <a name="systemsmanager-PutParameter-request-KeyId"></a>
The AWS Key Management Service (AWS KMS) ID that you want to use to encrypt a parameter. Use a custom key for better security. Required for parameters that use the `SecureString` data type.
If you don't specify a key ID, the system uses the default key associated with your AWS account, which is not as secure as using a custom key.
+ To use a custom AWS KMS key, choose the `SecureString` data type with the `Key ID` parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([a-zA-Z0-9:/_-]+)$`
Required: No

 ** [Name](#API_PutParameter_RequestSyntax) **   <a name="systemsmanager-PutParameter-request-Name"></a>
The fully qualified name of the parameter that you want to create or update.
You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.
The fully qualified name includes the complete hierarchy of the parameter path and name. For parameters in a hierarchy, you must include a leading forward slash character (/) when you create or reference a parameter. For example: `/Dev/DBServer/MySQL/db-string13`
Naming Constraints:
+ Parameter names are case sensitive.
+ A parameter name must be unique within an AWS Region
+ A parameter name can't be prefixed with "`aws`" or "`ssm`" (case-insensitive).
+ Parameter names can include only the following symbols and letters: `a-zA-Z0-9_.-`

  In addition, the slash character ( / ) is used to delineate hierarchies in parameter names. For example: `/Dev/Production/East/Project-ABC/MyParameter`
+ Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a `ValidationException` error.
+ Parameter hierarchies are limited to a maximum depth of fifteen levels.
For additional information about valid values for parameter names, see [Creating Systems Manager parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html) in the * AWS Systems Manager User Guide*.
The reported maximum length of 2048 characters for a parameter name includes 1037 characters that are reserved for internal use by Systems Manager. The maximum length for a parameter name that you specify is 1011 characters.
This count of 1011 characters includes the characters in the ARN that precede the name you specify. This ARN length will vary depending on your partition and Region. For example, the following 45 characters count toward the 1011 character maximum for a parameter created in the US East (Ohio) Region: `arn:aws:ssm:us-east-2:111122223333:parameter/`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [Overwrite](#API_PutParameter_RequestSyntax) **   <a name="systemsmanager-PutParameter-request-Overwrite"></a>
Overwrite an existing parameter. The default value is `false`.
Type: Boolean
Required: No

 ** [Policies](#API_PutParameter_RequestSyntax) **   <a name="systemsmanager-PutParameter-request-Policies"></a>
One or more policies to apply to a parameter. This operation takes a JSON array. Parameter Store, a tool in AWS Systems Manager supports the following policy types:
Expiration: This policy deletes the parameter after it expires. When you create the policy, you specify the expiration date. You can update the expiration date and time by updating the policy. Updating the *parameter* doesn't affect the expiration date and time. When the expiration time is reached, Parameter Store deletes the parameter.
ExpirationNotification: This policy initiates an event in Amazon CloudWatch Events that notifies you about the expiration. By using this policy, you can receive notification before or after the expiration time is reached, in units of days or hours.
NoChangeNotification: This policy initiates a CloudWatch Events event if a parameter hasn't been modified for a specified period of time. This policy type is useful when, for example, a secret needs to be changed within a period of time, but it hasn't been changed.
All existing policies are preserved until you send new policies or an empty policy. For more information about parameter policies, see [Assigning parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [Tags](#API_PutParameter_RequestSyntax) **   <a name="systemsmanager-PutParameter-request-Tags"></a>
Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems Manager parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter. In this case, you could specify the following key-value pairs:
+  `Key=Resource,Value=S3bucket`
+  `Key=OS,Value=Windows`
+  `Key=ParameterType,Value=LicenseKey`
To add tags to an existing Systems Manager parameter, use the [AddTagsToResource](API_AddTagsToResource.md) operation.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

 ** [Tier](#API_PutParameter_RequestSyntax) **   <a name="systemsmanager-PutParameter-request-Tier"></a>
The parameter tier to assign to a parameter.
Parameter Store offers a standard tier and an advanced tier for parameters. Standard parameters have a content size limit of 4 KB and can't be configured to use parameter policies. You can create a maximum of 10,000 standard parameters for each Region in an AWS account. Standard parameters are offered at no additional cost.
Advanced parameters have a content size limit of 8 KB and can be configured to use parameter policies. You can create a maximum of 100,000 advanced parameters for each Region in an AWS account. Advanced parameters incur a charge. For more information, see [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html) in the * AWS Systems Manager User Guide*.
You can change a standard parameter to an advanced parameter any time. But you can't revert an advanced parameter to a standard parameter. Reverting an advanced parameter to a standard parameter would result in data loss because the system would truncate the size of the parameter from 8 KB to 4 KB. Reverting would also remove any policies attached to the parameter. Lastly, advanced parameters use a different form of encryption than standard parameters.
If you no longer need an advanced parameter, or if you no longer want to incur charges for an advanced parameter, you must delete it and recreate it as a new standard parameter.
 **Using the Default Tier Configuration**
In `PutParameter` requests, you can specify the tier to create the parameter in. Whenever you specify a tier in the request, Parameter Store creates or updates the parameter according to that request. However, if you don't specify a tier in a request, Parameter Store assigns the tier based on the current Parameter Store default tier configuration.
The default tier when you begin using Parameter Store is the standard-parameter tier. If you use the advanced-parameter tier, you can specify one of the following as the default:
+  **Advanced**: With this option, Parameter Store evaluates all requests as advanced parameters.
+  **Intelligent-Tiering**: With this option, Parameter Store evaluates each request to determine if the parameter is standard or advanced.

  If the request doesn't include any options that require an advanced parameter, the parameter is created in the standard-parameter tier. If one or more options requiring an advanced parameter are included in the request, Parameter Store create a parameter in the advanced-parameter tier.

  This approach helps control your parameter-related costs by always creating standard parameters unless an advanced parameter is necessary.
Options that require an advanced parameter include the following:
+ The content size of the parameter is more than 4 KB.
+ The parameter uses a parameter policy.
+ More than 10,000 parameters already exist in your AWS account in the current AWS Region.
For more information about configuring the default tier option, see [Specifying a default parameter tier](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html#ps-default-tier) in the * AWS Systems Manager User Guide*.
Type: String
Valid Values: `Standard | Advanced | Intelligent-Tiering`
Required: No

 ** [Type](#API_PutParameter_RequestSyntax) **   <a name="systemsmanager-PutParameter-request-Type"></a>
The type of parameter that you want to create.
 `SecureString` isn't currently supported for AWS CloudFormation templates.
Items in a `StringList` must be separated by a comma (,). You can't use other punctuation or special character to escape items in the list. If you have a parameter value that requires a comma, then use the `String` data type.
Specifying a parameter type isn't required when updating a parameter. You must specify a parameter type when creating a parameter.
Type: String
Valid Values: `String | StringList | SecureString`
Required: No

 ** [Value](#API_PutParameter_RequestSyntax) **   <a name="systemsmanager-PutParameter-request-Value"></a>
The parameter value that you want to add to the system. Standard parameters have a value limit of 4 KB. Advanced parameters have a value limit of 8 KB.
Parameters can't be referenced or nested in the values of other parameters. You can't include values wrapped in double brackets `{{}}` or `{{ssm:parameter-name}}` in a parameter value.
Type: String
Required: Yes

## Response Syntax
<a name="API_PutParameter_ResponseSyntax"></a>

```
{
   "Tier": "string",
   "Version": number
}
```

## Response Elements
<a name="API_PutParameter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tier](#API_PutParameter_ResponseSyntax) **   <a name="systemsmanager-PutParameter-response-Tier"></a>
The tier assigned to the parameter.
Type: String
Valid Values: `Standard | Advanced | Intelligent-Tiering`

 ** [Version](#API_PutParameter_ResponseSyntax) **   <a name="systemsmanager-PutParameter-response-Version"></a>
The new version number of a parameter. If you edit a parameter value, Parameter Store automatically creates a new version and assigns this new version a unique ID. You can reference a parameter version ID in API operations or in Systems Manager documents (SSM documents). By default, if you don't specify a specific version, the system returns the latest parameter value when a parameter is called.
Type: Long

## Errors
<a name="API_PutParameter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HierarchyLevelLimitExceededException **
A hierarchy can have a maximum of 15 levels. For more information, see [Requirements and constraints for parameter names](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-parameter-name-constraints.html) in the * AWS Systems Manager User Guide*.
 ** message **
A hierarchy can have a maximum of 15 levels. For more information, see [About requirements and constraints for parameter names](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html#sysman-parameter-name-constraints) in the * AWS Systems Manager User Guide*.
HTTP Status Code: 400

 ** HierarchyTypeMismatchException **
Parameter Store doesn't support changing a parameter type in a hierarchy. For example, you can't change a parameter from a `String` type to a `SecureString` type. You must create a new, unique parameter.
 ** message **
Parameter Store doesn't support changing a parameter type in a hierarchy. For example, you can't change a parameter from a `String` type to a `SecureString` type. You must create a new, unique parameter.
HTTP Status Code: 400

 ** IncompatiblePolicyException **
There is a conflict in the policies specified for this parameter. You can't, for example, specify two Expiration policies for a parameter. Review your policies, and try again.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidAllowedPatternException **
The request doesn't meet the regular expression requirement.
 ** message **
The request doesn't meet the regular expression requirement.
HTTP Status Code: 400

 ** InvalidKeyId **
The query key ID isn't valid.
HTTP Status Code: 400

 ** InvalidPolicyAttributeException **
A policy attribute or its value is invalid.
HTTP Status Code: 400

 ** InvalidPolicyTypeException **
The policy type isn't supported. Parameter Store supports the following policy types: Expiration, ExpirationNotification, and NoChangeNotification.
HTTP Status Code: 400

 ** ParameterAlreadyExists **
The parameter already exists. You can't create duplicate parameters.
HTTP Status Code: 400

 ** ParameterLimitExceeded **
You have exceeded the number of parameters for this AWS account. Delete one or more parameters and try again.
HTTP Status Code: 400

 ** ParameterMaxVersionLimitExceeded **
Parameter Store retains the 100 most recently created versions of a parameter. After this number of versions has been created, Parameter Store deletes the oldest version when a new one is created. However, if the oldest version has a *label* attached to it, Parameter Store won't delete the version and instead presents this error message:
 `An error occurred (ParameterMaxVersionLimitExceeded) when calling the PutParameter operation: You attempted to create a new version of parameter-name by calling the PutParameter API with the overwrite flag. Version version-number, the oldest version, can't be deleted because it has a label associated with it. Move the label to another version of the parameter, and try again.`
This safeguard is to prevent parameter versions with mission critical labels assigned to them from being deleted. To continue creating new parameters, first move the label from the oldest version of the parameter to a newer one for use in your operations. For information about moving parameter labels, see [Move a parameter label (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html#sysman-paramstore-labels-console-move) or [Move a parameter label (CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html#sysman-paramstore-labels-cli-move) in the * AWS Systems Manager User Guide*.
HTTP Status Code: 400

 ** ParameterPatternMismatchException **
The parameter name isn't valid.
 ** message **
The parameter name isn't valid.
HTTP Status Code: 400

 ** PoliciesLimitExceededException **
You specified more than the maximum number of allowed policies for the parameter. The maximum is 10.
HTTP Status Code: 400

 ** TooManyUpdates **
There are concurrent updates for a resource that supports one update at a time.
HTTP Status Code: 400

 ** UnsupportedParameterType **
The parameter type isn't supported.
HTTP Status Code: 400

## Examples
<a name="API_PutParameter_Examples"></a>

### Example
<a name="API_PutParameter_Example_1"></a>

This example illustrates one usage of PutParameter.

#### Sample Request
<a name="API_PutParameter_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 136
X-Amz-Target: AmazonSSM.PutParameter
X-Amz-Date: 20240316T000626Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240316/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Overwrite": true,
    "Type": "String",
    "Name": "EC2TestServerType",
    "Value": "t2.large",
    "Description": "Instance type for Test servers"
}
```

#### Sample Response
<a name="API_PutParameter_Example_1_Response"></a>

```
{
    "Version": 2
}
```

## See Also
<a name="API_PutParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/PutParameter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/PutParameter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PutParameter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/PutParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PutParameter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/PutParameter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/PutParameter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/PutParameter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/PutParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PutParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
