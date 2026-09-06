---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_GroupingConfiguration.html
---

# GroupingConfiguration
<a name="API_amazon-q-connect_GroupingConfiguration"></a>

The configuration information of the grouping of Amazon Q in Connect users.

## Contents
<a name="API_amazon-q-connect_GroupingConfiguration_Contents"></a>

 ** criteria **   <a name="connect-Type-amazon-q-connect_GroupingConfiguration-criteria"></a>
The criteria used for grouping Amazon Q in Connect users.
The following is the list of supported criteria values.
+  `RoutingProfileArn`: Grouping the users by their [Amazon Connect routing profile ARN](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html). User should have [SearchRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html) and [DescribeRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html) permissions when setting criteria to this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** values **   <a name="connect-Type-amazon-q-connect_GroupingConfiguration-values"></a>
The list of values that define different groups of Amazon Q in Connect users.
+ When setting `criteria` to `RoutingProfileArn`, you need to provide a list of ARNs of [Connect Customer routing profiles](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html) as values of this parameter.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_amazon-q-connect_GroupingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GroupingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GroupingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GroupingConfiguration)
