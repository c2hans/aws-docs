---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupIdentifier.html
---

# GroupIdentifier
<a name="API_GroupIdentifier"></a>

The unique identifiers for a resource group.

## Contents
<a name="API_GroupIdentifier_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Criticality **   <a name="ARG-Type-GroupIdentifier-Criticality"></a>
The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** Description **   <a name="ARG-Type-GroupIdentifier-Description"></a>
The description of the application group.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\sa-zA-Z0-9_\.-]*`
Required: No

 ** DisplayName **   <a name="ARG-Type-GroupIdentifier-DisplayName"></a>
The name of the application group, which you can change at any time.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** GroupArn **   <a name="ARG-Type-GroupIdentifier-GroupArn"></a>
The Amazon resource name (ARN) of the resource group.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: No

 ** GroupName **   <a name="ARG-Type-GroupIdentifier-GroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}`
Required: No

 ** Owner **   <a name="ARG-Type-GroupIdentifier-Owner"></a>
A name, email address or other identifier for the person or group who is considered as the owner of this group within your organization.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_GroupIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/GroupIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/GroupIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/GroupIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
