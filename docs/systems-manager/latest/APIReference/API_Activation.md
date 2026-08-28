---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_Activation.html
---

# Activation
<a name="API_Activation"></a>

An activation registers one or more on-premises servers or virtual machines (VMs) with AWS so that you can configure those servers or VMs using Run Command. A server or VM that has been registered with AWS Systems Manager is called a managed node.

## Contents
<a name="API_Activation_Contents"></a>

 ** ActivationId **   <a name="systemsmanager-Type-Activation-ActivationId"></a>
The ID created by Systems Manager when you submitted the activation.
Type: String
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** CreatedDate **   <a name="systemsmanager-Type-Activation-CreatedDate"></a>
The date the activation was created.
Type: Timestamp
Required: No

 ** DefaultInstanceName **   <a name="systemsmanager-Type-Activation-DefaultInstanceName"></a>
A name for the managed node when it is created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** Description **   <a name="systemsmanager-Type-Activation-Description"></a>
A user defined description of the activation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** ExpirationDate **   <a name="systemsmanager-Type-Activation-ExpirationDate"></a>
The date when this activation can no longer be used to register managed nodes.
Type: Timestamp
Required: No

 ** Expired **   <a name="systemsmanager-Type-Activation-Expired"></a>
Whether or not the activation is expired.
Type: Boolean
Required: No

 ** IamRole **   <a name="systemsmanager-Type-Activation-IamRole"></a>
The AWS Identity and Access Management (IAM) role to assign to the managed node.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** RegistrationLimit **   <a name="systemsmanager-Type-Activation-RegistrationLimit"></a>
The maximum number of managed nodes that can be registered using this activation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** RegistrationsCount **   <a name="systemsmanager-Type-Activation-RegistrationsCount"></a>
The number of managed nodes already registered with this activation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** Tags **   <a name="systemsmanager-Type-Activation-Tags"></a>
Tags assigned to the activation.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

## See Also
<a name="API_Activation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/Activation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/Activation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/Activation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
