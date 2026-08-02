---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GeneratedPolicyProperties.html
---

# GeneratedPolicyProperties
<a name="API_GeneratedPolicyProperties"></a>

Contains the generated policy details.

## Contents
<a name="API_GeneratedPolicyProperties_Contents"></a>

 ** principalArn **   <a name="accessanalyzer-Type-GeneratedPolicyProperties-principalArn"></a>
The ARN of the IAM entity (user or role) for which you are generating a policy.
Type: String
Pattern: `arn:[^:]*:iam::[^:]*:(role|user)/.{1,576}`
Required: Yes

 ** cloudTrailProperties **   <a name="accessanalyzer-Type-GeneratedPolicyProperties-cloudTrailProperties"></a>
Lists details about the `Trail` used to generated policy.
Type: [CloudTrailProperties](API_CloudTrailProperties.md) object
Required: No

 ** isComplete **   <a name="accessanalyzer-Type-GeneratedPolicyProperties-isComplete"></a>
This value is set to `true` if the generated policy contains all possible actions for a service that IAM Access Analyzer identified from the CloudTrail trail that you specified, and `false` otherwise.
Type: Boolean
Required: No

## See Also
<a name="API_GeneratedPolicyProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GeneratedPolicyProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GeneratedPolicyProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GeneratedPolicyProperties)
