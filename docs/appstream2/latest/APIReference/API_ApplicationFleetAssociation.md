---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ApplicationFleetAssociation.html
---

# ApplicationFleetAssociation
<a name="API_ApplicationFleetAssociation"></a>

Describes the application fleet association.

## Contents
<a name="API_ApplicationFleetAssociation_Contents"></a>

 ** ApplicationArn **   <a name="WorkSpacesApplications-Type-ApplicationFleetAssociation-ApplicationArn"></a>
The ARN of the application associated with the fleet.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** FleetName **   <a name="WorkSpacesApplications-Type-ApplicationFleetAssociation-FleetName"></a>
The name of the fleet associated with the application.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## See Also
<a name="API_ApplicationFleetAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ApplicationFleetAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ApplicationFleetAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ApplicationFleetAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
