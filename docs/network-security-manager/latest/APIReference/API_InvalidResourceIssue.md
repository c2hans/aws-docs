---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_InvalidResourceIssue.html
---

# InvalidResourceIssue
<a name="API_InvalidResourceIssue"></a>

Describes a single related resource whose configuration does not match the intended configuration.

## Contents
<a name="API_InvalidResourceIssue_Contents"></a>

 ** actualValue **   <a name="networksecuritymanager-Type-InvalidResourceIssue-actualValue"></a>
The current attribute value on the resource.
Type: String
Required: No

 ** expectedValue **   <a name="networksecuritymanager-Type-InvalidResourceIssue-expectedValue"></a>
The attribute value that the policy configuration requires, such as the connectivity type for a subnet.
Type: String
Required: No

 ** resourceId **   <a name="networksecuritymanager-Type-InvalidResourceIssue-resourceId"></a>
The identifier of the resource, such as a subnet ARN.
Type: String
Required: No

## See Also
<a name="API_InvalidResourceIssue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/InvalidResourceIssue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/InvalidResourceIssue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/InvalidResourceIssue)
