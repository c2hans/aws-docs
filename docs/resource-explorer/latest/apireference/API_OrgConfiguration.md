---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_OrgConfiguration.html
---

# OrgConfiguration
<a name="API_OrgConfiguration"></a>

This is a structure that contains the status of AWS service access, and whether you have a valid service-linked role to enable multi-account search for your organization.

## Contents
<a name="API_OrgConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AWSServiceAccessStatus **   <a name="resourceexplorer-Type-OrgConfiguration-AWSServiceAccessStatus"></a>
This value displays whether your AWS service access is `ENABLED` or `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** ServiceLinkedRole **   <a name="resourceexplorer-Type-OrgConfiguration-ServiceLinkedRole"></a>
This value shows whether or not you have a valid a service-linked role required to start the multi-account search feature.
Type: String
Required: No

## See Also
<a name="API_OrgConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/OrgConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/OrgConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/OrgConfiguration)
