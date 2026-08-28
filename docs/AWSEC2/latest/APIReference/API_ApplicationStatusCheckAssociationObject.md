---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ApplicationStatusCheckAssociationObject.html
---

# ApplicationStatusCheckAssociationObject
<a name="API_ApplicationStatusCheckAssociationObject"></a>

Information about an application status check association. Each item in the `associationSet` of a `DescribeApplicationStatusCheckAssociations` response is of this type.

## Contents
<a name="API_ApplicationStatusCheckAssociationObject_Contents"></a>

 ** applicationStatusCheckId **
The ID of the application status check.
Type: String
Required: No

 ** associationType **
The type of target that the application status check is associated with. Possible values:
+  `tag` – The check applies to current and future instances with a matching tag key-value pair.
+  `instance-id` – The check applies to a specific instance.
Type: String
Valid Values: `tag | instance-id`
Required: No

 ** key **
The key for the association. This value is present only for tag-based associations, where it contains the tag key. For instance-based associations, this value is absent.
Type: String
Required: No

 ** value **
The value for the association target. For tag-based associations, this is the tag value. For instance-based associations, this is the instance ID (for example, `i-0123456789abcdef0`).
Type: String
Required: No

## See Also
<a name="API_ApplicationStatusCheckAssociationObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ApplicationStatusCheckAssociationObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ApplicationStatusCheckAssociationObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ApplicationStatusCheckAssociationObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
