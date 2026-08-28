---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AccessPolicySummary.html
---

# AccessPolicySummary
<a name="API_AccessPolicySummary"></a>

Contains an access policy that defines an identity's access to an AWS IoT SiteWise Monitor resource.

## Contents
<a name="API_AccessPolicySummary_Contents"></a>

 ** id **   <a name="iotsitewise-Type-AccessPolicySummary-id"></a>
The ID of the access policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** identity **   <a name="iotsitewise-Type-AccessPolicySummary-identity"></a>
The identity (an IAM Identity Center user, an IAM Identity Center group, or an IAM user).
Type: [Identity](API_Identity.md) object
Required: Yes

 ** permission **   <a name="iotsitewise-Type-AccessPolicySummary-permission"></a>
The permissions for the access policy. Note that a project `ADMINISTRATOR` is also known as a project owner.
Type: String
Valid Values: `ADMINISTRATOR | VIEWER`
Required: Yes

 ** resource **   <a name="iotsitewise-Type-AccessPolicySummary-resource"></a>
The AWS IoT SiteWise Monitor resource (a portal or project).
Type: [Resource](API_Resource.md) object
Required: Yes

 ** creationDate **   <a name="iotsitewise-Type-AccessPolicySummary-creationDate"></a>
The date the access policy was created, in Unix epoch time.
Type: Timestamp
Required: No

 ** lastUpdateDate **   <a name="iotsitewise-Type-AccessPolicySummary-lastUpdateDate"></a>
The date the access policy was last updated, in Unix epoch time.
Type: Timestamp
Required: No

## See Also
<a name="API_AccessPolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AccessPolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AccessPolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AccessPolicySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
