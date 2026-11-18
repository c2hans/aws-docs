---
source_url: https://docs.aws.amazon.com/awssupport/latest/user/support-interaction-perm-man-policy.html
---

# Option 1: Use the AWS managed policy (recommended)
<a name="support-interaction-perm-man-policy"></a>

If you currently have the AWSSupportAccess managed policy attached, no additional permissions are required. To use the functions included in the [Support Center Console API](aws-support-console.md), you must have the Support Center Console operations in your IAM policies. If you use your own policies instead of AWSSupportAccess, add the `support-console:*` actions to them. For more information, see [Adding IAM policies for the Support Center Console API operations](support-console-access-control.md).
