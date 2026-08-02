---
source_url: https://docs.aws.amazon.com/cloud9/latest/APIReference/API_EnvironmentMember.html
---

# EnvironmentMember
<a name="API_EnvironmentMember"></a>

Information about an environment member for an AWS Cloud9 development environment.

## Contents
<a name="API_EnvironmentMember_Contents"></a>

 ** environmentId **   <a name="cloud9-Type-EnvironmentMember-environmentId"></a>
The ID of the environment for the environment member.
Type: String
Pattern: `^[a-zA-Z0-9]{8,32}$`
Required: Yes

 ** permissions **   <a name="cloud9-Type-EnvironmentMember-permissions"></a>
The type of environment member permissions associated with this environment member. Available values include:
+  `owner`: Owns the environment.
+  `read-only`: Has read-only access to the environment.
+  `read-write`: Has read-write access to the environment.
Type: String
Valid Values: `owner | read-write | read-only`
Required: Yes

 ** userArn **   <a name="cloud9-Type-EnvironmentMember-userArn"></a>
The Amazon Resource Name (ARN) of the environment member.
Type: String
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):(iam|sts)::\d+:(root|(user\/[\w+=/:,.@-]{1,64}|federated-user\/[\w+=/:,.@-]{2,32}|assumed-role\/[\w+=:,.@-]{1,64}\/[\w+=,.@-]{1,64}))$`
Required: Yes

 ** userId **   <a name="cloud9-Type-EnvironmentMember-userId"></a>
The user ID in AWS Identity and Access Management (IAM) of the environment member.
Type: String
Required: Yes

 ** lastAccess **   <a name="cloud9-Type-EnvironmentMember-lastAccess"></a>
The time, expressed in epoch time format, when the environment member last opened the environment.
Type: Timestamp
Required: No

## See Also
<a name="API_EnvironmentMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/EnvironmentMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/EnvironmentMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/EnvironmentMember)
