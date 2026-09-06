---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_ServiceAccessSecurityGroups.html
---

# ServiceAccessSecurityGroups
<a name="API_ServiceAccessSecurityGroups"></a>

The security groups that allow traffic between the Amazon EVS control plane and your VPC for Amazon EVS service access. If a security group is not specified, Amazon EVS uses the default security group in your account for service access.

## Contents
<a name="API_ServiceAccessSecurityGroups_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** securityGroups **   <a name="evs-Type-ServiceAccessSecurityGroups-securityGroups"></a>
The security groups that allow service access.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Length Constraints: Minimum length of 3. Maximum length of 25.
Pattern: `sg-[0-9a-zA-Z]*`
Required: No

## See Also
<a name="API_ServiceAccessSecurityGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/ServiceAccessSecurityGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/ServiceAccessSecurityGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/ServiceAccessSecurityGroups)
